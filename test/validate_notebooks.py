"""Validate this repository's Python and Julia Jupyter notebooks.

Run from the repository root with:
    uv run python test/validate_notebooks.py
"""

from __future__ import annotations

import ast
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STUDENT_DIR = ROOT / "notebooks" / "julia"
INSTRUCTOR_DIR = ROOT / "instructor" / "julia"
PYTHON_STUDENT_DIR = ROOT / "notebooks" / "python"
PYTHON_INSTRUCTOR_DIR = ROOT / "instructor" / "python"
JULIA_PROJECT = ROOT / "julia"


PARSER_SCRIPT = r"""
source = read(stdin, String)
expression = Meta.parseall(source)
function has_parse_error(node)
    node isa Expr || return false
    node.head in (:error, :incomplete) && return true
    return any(has_parse_error, node.args)
end
has_parse_error(expression) && error("Julia parse error found")
"""


def load_notebook(path: Path) -> dict:
    with path.open(encoding="utf-8") as notebook_file:
        return json.load(notebook_file)


def code_sources(notebook: dict) -> list[str]:
    return [
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    ]


def validate_structure(paths: list[Path]) -> tuple[list[str], list[str], set[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    kernel_names: set[str] = set()

    for path in paths:
        try:
            notebook = load_notebook(path)
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{path.relative_to(ROOT)}: invalid notebook JSON ({error})")
            continue

        kernelspec = notebook.get("metadata", {}).get("kernelspec", {})
        if kernelspec.get("language") != "julia":
            failures.append(f"{path.relative_to(ROOT)}: kernelspec language is not Julia")
        kernel_name = kernelspec.get("name")
        if not kernel_name:
            failures.append(f"{path.relative_to(ROOT)}: kernelspec name is missing")
        else:
            kernel_names.add(kernel_name)

        for cell_number, cell in enumerate(notebook.get("cells", []), start=1):
            language = cell.get("metadata", {}).get("language")
            if not language:
                warnings.append(
                    f"{path.relative_to(ROOT)} cell {cell_number}: metadata.language is missing"
                )
            elif cell.get("cell_type") == "code" and language != "julia":
                failures.append(
                    f"{path.relative_to(ROOT)} cell {cell_number}: code cell language is {language!r}"
                )

    return failures, warnings, kernel_names


def validate_kernel_discovery(kernel_names: set[str]) -> list[str]:
    result = subprocess.run(
        [sys.executable, "-m", "jupyter", "kernelspec", "list", "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        return [f"Could not list Jupyter kernels: {result.stderr.strip()}"]

    try:
        installed = set(json.loads(result.stdout).get("kernelspecs", {}))
    except json.JSONDecodeError as error:
        return [f"Jupyter returned invalid kernelspec JSON: {error}"]

    missing = sorted(kernel_names - installed)
    return [f"Jupyter cannot find kernelspec {name!r}" for name in missing]


def validate_student_syntax(paths: list[Path], julia: str) -> list[str]:
    failures: list[str] = []
    for path in paths:
        notebook = load_notebook(path)
        sources = code_sources(notebook)
        result = subprocess.run(
            [julia, f"--project={JULIA_PROJECT}", "--startup-file=no", "-e", PARSER_SCRIPT],
            cwd=ROOT,
            input="\n\n".join(sources).encode("utf-8"),
            capture_output=True,
            check=False,
        )
        if result.returncode:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            failures.append(f"{path.relative_to(ROOT)}: Julia syntax check failed\n{detail}")
        else:
            print(f"PASS student syntax: {path.relative_to(ROOT)}")
    return failures


def validate_python_structure(paths: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in paths:
        try:
            notebook = load_notebook(path)
        except (OSError, json.JSONDecodeError) as error:
            failures.append(f"{path.relative_to(ROOT)}: invalid notebook JSON ({error})")
            continue
        kernelspec = notebook.get("metadata", {}).get("kernelspec", {})
        if kernelspec.get("language") != "python" or kernelspec.get("name") != "python3":
            failures.append(f"{path.relative_to(ROOT)}: expected the python3 kernelspec")
        for cell_number, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") == "code":
                language = cell.get("metadata", {}).get("language")
                if language and language != "python":
                    failures.append(
                        f"{path.relative_to(ROOT)} cell {cell_number}: code cell language is {language!r}"
                    )
    return failures


def validate_python_student_syntax(paths: list[Path]) -> list[str]:
    failures: list[str] = []
    for path in paths:
        notebook = load_notebook(path)
        for cell_number, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            try:
                ast.parse(source, filename=f"{path.name}:cell {cell_number}")
            except SyntaxError as error:
                failures.append(
                    f"{path.relative_to(ROOT)} cell {cell_number}: Python syntax error: {error}"
                )
                break
        else:
            print(f"PASS Python student syntax: {path.relative_to(ROOT)}")
    return failures


def validate_instructor_execution(paths: list[Path], kernel_name: str) -> list[str]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="mtu-fin4000-julia-tests-") as output_dir:
        for path in paths:
            command = [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                f"--ExecutePreprocessor.kernel_name={kernel_name}",
                "--ExecutePreprocessor.timeout=180",
                f"--output-dir={output_dir}",
                str(path),
            ]
            result = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode:
                failures.append(
                    f"{path.relative_to(ROOT)}: execution failed\n"
                    f"{result.stderr.strip() or result.stdout.strip()}"
                )
                continue

            executed_path = Path(output_dir) / path.name
            try:
                executed = load_notebook(executed_path)
            except (OSError, json.JSONDecodeError) as error:
                failures.append(f"{path.relative_to(ROOT)}: executed output missing/invalid ({error})")
                continue

            cell_errors = [
                output
                for cell in executed.get("cells", [])
                for output in cell.get("outputs", [])
                if output.get("output_type") == "error"
            ]
            if cell_errors:
                error = cell_errors[0]
                failures.append(
                    f"{path.relative_to(ROOT)}: {error.get('ename')}: {error.get('evalue')}"
                )
            else:
                print(f"PASS instructor execution: {path.relative_to(ROOT)}")

    return failures


def validate_notebook_execution(paths: list[Path], kernel_name: str, language: str) -> list[str]:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix=f"mtu-fin4000-{language}-tests-") as output_dir:
        for path in paths:
            command = [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                f"--ExecutePreprocessor.kernel_name={kernel_name}",
                "--ExecutePreprocessor.timeout=180",
                f"--output-dir={output_dir}",
                str(path),
            ]
            result = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode:
                failures.append(
                    f"{path.relative_to(ROOT)}: execution failed\n"
                    f"{result.stderr.strip() or result.stdout.strip()}"
                )
                continue

            executed_path = Path(output_dir) / path.name
            try:
                executed = load_notebook(executed_path)
            except (OSError, json.JSONDecodeError) as error:
                failures.append(f"{path.relative_to(ROOT)}: executed output missing/invalid ({error})")
                continue

            cell_errors = [
                output
                for cell in executed.get("cells", [])
                for output in cell.get("outputs", [])
                if output.get("output_type") == "error"
            ]
            if cell_errors:
                error = cell_errors[0]
                failures.append(
                    f"{path.relative_to(ROOT)}: {error.get('ename')}: {error.get('evalue')}"
                )
            else:
                print(f"PASS {language} instructor execution: {path.relative_to(ROOT)}")

    return failures


def main() -> int:
    julia = shutil.which("julia")
    if not julia:
        print("ERROR: Julia is not on PATH. Install Julia and reopen the terminal.", file=sys.stderr)
        return 2

    student_paths = sorted(STUDENT_DIR.glob("*.ipynb"))
    instructor_paths = sorted(INSTRUCTOR_DIR.glob("*.ipynb"))
    if not student_paths or not instructor_paths:
        print("ERROR: expected Julia notebooks under notebooks/julia and instructor/julia.", file=sys.stderr)
        return 2

    all_paths = student_paths + instructor_paths
    failures, warnings, kernel_names = validate_structure(all_paths)
    failures.extend(validate_kernel_discovery(kernel_names))

    if len(kernel_names) != 1:
        failures.append(f"Julia notebooks specify inconsistent kernelspecs: {sorted(kernel_names)}")
    kernel_name = next(iter(kernel_names), "")

    print(f"Julia student notebooks: {len(student_paths)}")
    print(f"Julia instructor notebooks: {len(instructor_paths)}")
    python_student_paths = sorted(PYTHON_STUDENT_DIR.glob("*.ipynb"))
    python_instructor_paths = sorted(PYTHON_INSTRUCTOR_DIR.glob("*.ipynb"))
    if not python_student_paths or not python_instructor_paths:
        print("ERROR: expected Python notebooks under notebooks/python and instructor/python.", file=sys.stderr)
        return 2
    failures.extend(validate_python_structure(python_student_paths + python_instructor_paths))
    failures.extend(validate_kernel_discovery({"python3"}))
    print(f"Python student notebooks: {len(python_student_paths)}")
    print(f"Python instructor notebooks: {len(python_instructor_paths)}")

    failures.extend(validate_student_syntax(student_paths, julia))
    if kernel_name:
        failures.extend(validate_notebook_execution(instructor_paths, kernel_name, "Julia"))
    failures.extend(validate_python_student_syntax(python_student_paths))
    failures.extend(validate_notebook_execution(python_instructor_paths, "python3", "Python"))

    if failures:
        print(f"\nFAILURES: {len(failures)}")
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("\nAll Python and Julia notebook checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

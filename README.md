# mtu-fin4000
Jupyter Notebooks for MTU FIN-4000 Investment Analysis

Based upon:

Bodie, Z., Kane, A., & Marcus, A. (2023). Investments (13th ed.). McGraw Hill.

## Notebook environments

This repository supports Python notebooks in `notebooks/python/` and `instructor/python/`, as well as Julia notebooks in `notebooks/julia/` and `instructor/julia/`. Each language has its own environment.

### Python

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and a supported Python version, then run this from the repository root in PowerShell:

```powershell
uv sync
```

`uv sync` creates `.venv` and installs the dependencies from `pyproject.toml` and `uv.lock` (when present). In VS Code, install the Python and Jupyter extensions, then use **Python: Select Interpreter** to select this repository's `.venv`. Open a Python notebook and select the `.venv` Python environment as its kernel. For Julia notebooks, this lets the Jupyter extension discover the registered Julia kernels.

### Julia

Install Julia 1.10 or newer from [julialang.org](https://julialang.org/downloads/) and the Julia and Jupyter extensions in VS Code. From the repository root, instantiate the Julia project:

```powershell
julia --project=julia -e "using Pkg; Pkg.instantiate()"
```

To register a notebook kernel that always uses this repository's Julia project, run:

```powershell
julia --project=julia -e 'using IJulia; IJulia.installkernel("Julia (MTU FIN4000)", "--project=$(dirname(Base.active_project()))")'
```

Open a Julia notebook in VS Code and choose the **Julia (MTU FIN4000)** kernel; IJulia appends the installed Julia version to the displayed kernel name (currently **Julia (MTU FIN4000) 1.13**). The project in `julia/Project.toml` includes `FinanceModels`, `ActuaryUtilities`, `IJulia`, `Plots`, and the Julia standard libraries used by the notebooks.



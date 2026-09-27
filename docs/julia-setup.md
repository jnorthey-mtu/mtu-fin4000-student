# Julia Setup in VS Code (Windows)

This guide sets up Julia for this repository while keeping its dependencies isolated in `julia/Project.toml`. The resolved package versions are recorded in `julia/Manifest.toml`.

## 1. Install Julia

Install Juliaup from PowerShell using `winget`:

```powershell
winget install --id Julialang.Juliaup -e --accept-source-agreements --accept-package-agreements
```

Open a new PowerShell terminal and check the Julia launcher:

```powershell
julia --version
juliaup status
```

The first `julia` launch installs the default `release` channel if it is not already installed. Juliaup manages Julia versions and provides the `julia` command.

## 2. Check PATH

On Windows, the Juliaup command shims are exposed through `%LOCALAPPDATA%\Microsoft\WindowsApps`. This directory is commonly already on the user PATH. Check that PowerShell can find Julia:

```powershell
Get-Command julia
```

If the command is not found, add `%LOCALAPPDATA%\Microsoft\WindowsApps` to your **user** `Path` using Windows **Edit environment variables for your account**. Do not add a version-specific Julia installation directory; Juliaup manages the changing version location behind its shims. Close and reopen PowerShell and VS Code after changing PATH, then run `julia --version` again.

## 3. Install the repository's Julia packages

In VS Code, open this repository as the workspace and open a terminal at its root. Instantiate the environment:

```powershell
julia --project=julia -e "using Pkg; Pkg.instantiate()"
```

This installs the versions captured by `julia/Manifest.toml`, including `FinanceModels`, `ActuaryUtilities`, `IJulia`, and `Plots`. If the manifest is absent or intentionally regenerated, Julia resolves compatible versions from `julia/Project.toml` and writes a new manifest.

## 4. Configure Julia in VS Code

Install the **Julia** extension published by Julia Computing. Open the Command Palette (`Ctrl+Shift+P`) and run **Julia: Start REPL**. The extension should find the `julia` launcher on PATH. If it does not, restart VS Code after the PATH change and check `Get-Command julia` in a new integrated terminal.

To use the repository's project in the REPL, activate it from the repository root:

```julia
import Pkg
Pkg.activate("julia")
```

You can confirm the active project and installed packages with:

```julia
Pkg.status()
```

## 5. Use Julia in Jupyter notebooks

Install the **Jupyter** extension in VS Code as well. The Julia project already includes IJulia. Register a named kernel once from the Julia REPL started with this project active:

```julia
using IJulia
IJulia.installkernel(
    "Julia (MTU FIN4000)",
    "--project=" * dirname(Base.active_project()),
)
```

Open or create a Julia notebook under `notebooks/julia/` or `instructor/julia/`, use **Select Kernel**, and choose **Julia (MTU FIN4000)**. IJulia appends the installed Julia version to the displayed name (currently **Julia (MTU FIN4000) 1.13**). This kernel starts Julia with the repository's `julia/` project, regardless of the notebook's working directory. Python notebooks continue to use the repository's `uv`-managed `.venv` kernel.

## 6. Verify the setup

In a Julia REPL or a Julia notebook using the named kernel, run:

```julia
using FinanceModels, ActuaryUtilities
present_value(0.03, [5.0, 5.0, 105.0], [1, 2, 3])
```

The result should be approximately `105.6572`. To confirm the versions and active environment, run `using Pkg; Pkg.status()`.

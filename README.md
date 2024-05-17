# pycon-fastapi

FastAPI example notebooks created for PyCon US 2024.

Feel free to fork the repo and try adding your own endpoints to the API!

enjoy! --baronpythonist (Byron)

## Installation with conda and mamba on Windows

### Install miniconda

Open start menu and type `powershell`; then launch from results.

```powershell
winget install --id=Anaconda.Miniconda3 -e
conda update conda
conda init
```

### Install mamba

Open start menu and type `Anaconda`; then launch `Anaconda Powershell Prompt (miniconda3)`

```powershell
conda install -c conda-forge mamba
```

### Clone Github environment

1. Install git [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Within Powershell, `cd` to the desired parent directory, and then clone with `git clone https://github.com/baronpythonist/pycon-fastapi.git`
3. Run `cd pycon-fastapi` before continuing.

### Install FastAPI environment from YAML file

```powershell
mamba env create -f environment.yml
conda activate fastenv
```

### Install VS Code and basic extensions

1. Download installer from [https://code.visualstudio.com/download](https://code.visualstudio.com/download) and install.
2. Launch VSCode and go the the `Extensions` page from the sidebar.
3. Install these extensions:
    * `GitLens`
    * `Python`
    * `Jupyter`
    * `markdownlint` (optional)
4. Open the Git repo you cloned above with `File -> Open Folder...`.

## Open Jupyter notebook and run

1. Once the folder has been opened, double click on `PyConFastapi.ipynb` from the `Explorer` page.
2. From the top-right corner of the opened notebook, click the button that says `Select Kernel`.
3. Select `Python Environment` then `fastenv` to launch the correct kernel.
4. You are now ready to run the cells!

Whenever you run a cell with the `uvicorn.run(app)` command, go to [http://localhost:8000/docs](http://localhost:8000/docs) for the API's interactive documentation.  Once you are ready to move on in the notebook, `interupt` the running cell (it will never "finish" executing).  Happy learning!

## Troubleshooting

Just message me (on GitHub) and I will try to help.

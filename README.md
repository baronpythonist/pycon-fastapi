# pycon-fastapi

FastAPI example notebooks created for PyCon US 2024

enjoy! --baronpythonist (Byron)

## Installation with conda and mamba on Windows

### Install miniconda

Open start menu and type `powershell`; then launch from results.

```ps
winget install --id=Anaconda.Miniconda3 -e
conda update conda
conda init
```

### Install mamba

Open start menu and type `Anaconda`; then launch `Anaconda Powershell Prompt (miniconda3)`

```ps
conda install -c conda-forge mamba
```

### Clone Github environment

1. Install git [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Within Powershell, `cd` to the desired parent directory, and then clone with `git clone https://github.com/baronpythonist/pycon-fastapi.git`
3. Run `cd pycon-fastapi` before continuing.

### Install FastAPI environment from YAML file

```ps
mamba env create -f environment.yml
conda activate fastenv
```

## Run API

```ps
fastapi dev main.py
```

Then go to [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive documentation.

## Troubleshooting

Just message me and I will try to help

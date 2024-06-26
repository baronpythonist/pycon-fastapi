# Supercharging Your Web Development with FastAPI

Welcome to the exciting world of FastAPI, where web development meets speed and simplicity! In this live Jupyter demonstration, we'll delve into the ins and outs of FastAPI, a modern Python web framework that's been gaining traction for its lightning-fast performance and intuitive API design.

Whether you're a seasoned developer looking to streamline your workflow or a newcomer eager to explore the latest tools in Python web development, this session is tailor-made for you. Join us as we explore FastAPI's key features, walk through code examples, and demonstrate how it can revolutionize the way you build web applications - all within the interactive environment of Jupyter.

Get ready to supercharge your development process with FastAPI - because in the fast-paced world of web development, every millisecond counts!

Feel free to fork the repo and try adding your own endpoints to the API!

enjoy! --baronpythonist (Byron)  Intro generated by OpenAI's ChatGPT

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

# FCC python tools

This repository hosts code examples that use `uproot`, `awkward array`, and other core python packages to load and analyse FCC simulation.

## Setting up

To set up a `conda` environment and install the required packages into it, do:

```
source setup/setup_env.sh
```

This command will also install a full version of `ROOT` if you wish to use it for any analysis. After running this command, add the following line to your `.bashrc` or equivalent:

```
source $HOME/miniconda/etc/profile.d/conda.sh
```

To activate the `conda` environment, do:

```
source setup/setup.sh
```

which will put you into an environment called `fcc_pyenv`. To exit this environment, do:

```
conda deactivate
```

## Project overview

User ROOT files produced with [FCCSW](https://github.com/HEP-FCC/FCCSW) can be placed in the `data/` directory in the main project folder. Python code to perform specific tasks is housed in `fcc_python_tools/`, and example scripts for running analysis can be found in `examples/`. Plots produced with `matplotlib` are stored in the `output/plots` folder, and LaTeX tables in the `output/tables` folder. Users can store analysis results in dictionaries and persist them to `.json` files, and write the output to the `output/json` folder.

Shortcuts for these various locations are defined in the `fcc_python_tools/locations.py` script. Here, users can change the default data directory and output locations if desired, and also add additional shortucts. These shortcuts can be accessed with:
```
from fcc_python_tools.locations import loc
```
where `loc.ROOT` for example gives the home directory of the project.

This project is intended as an example analysis framework, to demonstrate how to load and analyse FCC simulation data and produce some useful output. Users are free to extend the code by adding their own functions into the  `fcc_python_tools` folder and writing their own dedicated analysis scripts.

## uproot and awkward array

Generated events produced in [FCCSW](https://github.com/HEP-FCC/FCCSW) are stored in `ROOT` files. In this project, these files are loaded using the [uproot](https://github.com/scikit-hep/uproot4) package, which provides fast, `ROOT`-independent file loading into python. The events are handled using [awkward array](https://github.com/scikit-hep/awkward-1.0), which provides `numpy`-like access to jagged data (different numbers of particles in each event). This enables analysis at array-level, where all events are analysed with a single command without the use of loops.

## Example notebooks

Example Jupyter notebooks are provided in the `examples` directory. If you are working with files on your own local mahcine (laptop, desktop), you can do:
```
jupyter notebook
```
to launch Jupyter in your local browser. You can then run notebooks from there. However, the examples provided use files stored on EOS which requires that we launch Jupyter from lxplus. 

### Running from lxplus

A few steps are required in order to launch the notebook on lxplus, but view it using your local borwser. From inside the main project folder, do:
```
jupyter notebook --no-browser --port=5679
```
Then in a terminal on your local machine, do:
```
ssh -N -f -L localhost:5678:localhost:5679 dhill@lxplusXXX.cern.ch
```
making sure to point to the exact machine number `XXX` on lxplus. Then paste the following into your browser:
```
localhost:5678
```
This will prompt you for a token, which you can find in your lxplus terminal. There will be output such as:
```
jupyter notebook --no-browser --port=5679
[I 12:48:13.606 NotebookApp] Loading IPython parallel extension
[I 12:48:13.608 NotebookApp] Serving notebooks from local directory: /afs/cern.ch/user/d/dhill/fcc_python_tools
[I 12:48:13.608 NotebookApp] Jupyter Notebook 6.1.4 is running at:
[I 12:48:13.608 NotebookApp] http://localhost:5679/?token=29366eba39c32878ea4553fd8d19835e16d217b5e008ce7e
[I 12:48:13.608 NotebookApp]  or http://127.0.0.1:5679/?token=29366eba39c32878ea4553fd8d19835e16d217b5e008ce7e
```
where you can see the token in the fifth line here.


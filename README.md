# FCC python tools

This repository hosts code examples that use `uproot`, `awkward array`, and other core python packages to load and analyse FCC simulation.

## Setting up

The simplest way to access the notebooks is using the CERN `Swan` service, which provides access via web browser to a CERN machine with a full LCG Python 3 setup. You can find details of Swan [here](https://swan.web.cern.ch/swan/). Using `Swan`, it is easy to open Jupyter notebooks on the CERN machine and interact with them using your browser. 

Once you are in `Swan`, a few more Python packages are required. This can be done by clicking the terminal icon in `Swan`, which will open a new page with a terminal. You will be placed in `/eos/user/j/jbloggs`, your EOS user area (if your name is Joe Bloggs!). In the terminal, do:
```
pip install --user awkward1 particle
```
At the moment, we need the master release of the `uproot4` package (eventually we can also just install the stable release with `pip`). To get the master and install it, do:
```
git clone https://github.com/scikit-hep/uproot4.git
cd uproot4
python setup.py install --user
```
To donwload the `fcc_python_tools` project code in `Swan`, click on the cloud icon with an arrow on the right of your `My Projects` screen. In the box which appears, paste this link:
```
https://github.com/donalrinho/fcc_python_tools.git
```
This will place `fcc_python_tools` into `/eos/user/j/jbloggs/SWAN_projects/fcc_python_tools`.



## Project overview

User ROOT files produced with [FCCSW](https://github.com/HEP-FCC/FCCSW) can be placed in the `data/` directory in the main project folder. Python code to perform specific tasks is housed in `fcc_python_tools/`, and example notebooks for running analysis can be found in `examples/`. Plots produced with `matplotlib` are stored in the `output/plots` folder, and LaTeX tables in the `output/tables` folder. Users can store analysis results in dictionaries and persist them to `.json` files, and write the output to the `output/json` folder.

Shortcuts for these various locations are defined in the `fcc_python_tools/locations.py` script. Here, users can change the default data directory and output locations if desired, and also add additional shortucts. These shortcuts can be accessed with:
```
from fcc_python_tools.locations import loc
```
where `loc.ROOT` for example gives the home directory of the project, and `loc.DATA` points to the data folder where you can put your ROOT files. 

This project is intended as an example analysis framework, to demonstrate how to load and analyse FCC simulation data and produce some useful output. Users are free to extend the code by adding their own functions into the `fcc_python_tools` folder and writing their own dedicated analysis scripts.

## uproot and awkward array

Generated events produced in [FCCSW](https://github.com/HEP-FCC/FCCSW) are stored in `ROOT` files. In this project, these files are loaded using the [uproot](https://github.com/scikit-hep/uproot4) package, which provides fast, `ROOT`-independent file loading into python. The events are handled using [awkward array](https://github.com/scikit-hep/awkward-1.0), which provides `numpy`-like access to jagged data (different numbers of particles in each event). This enables analysis at array-level, where all events are analysed with a single command without the use of loops.

## Running outside of Swan

Example Jupyter notebooks are provided in the `examples` directory. If you are working with the `fcc_python_tools` package on your own local mahcine (laptop or desktop with a Python environmet including the required packages), you can do:
```
jupyter notebook
```
to launch Jupyter in your local browser. You can then run notebooks from there and point to files on your own machine. However, the example notebooks provided use files stored on `EOS`. To access these files, you should use `Swan` as described above.

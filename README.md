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

User ROOT files produced with [FCCSW](https://github.com/HEP-FCC/FCCSW) can be placed in the `data/` directory in the main project folder. Python code to perform specific tasks is housed in `python/`, and example scripts for running analysis can be found in `examples/`. Plots produced with `matplotlib` are stored in the `output/plots` folder, and LaTeX tables in the `output/tables` folder. Users can store analysis results in dictionaries and persist them to `.json` files, and write the output to the `output/json` folder.

Shortcuts for these various locations are defined in the `fcc_python_tools/locations.py` script. Here, users can change the default data directory and output locations if desired, and also add additional shortucts. These shortcuts are accessed with:

```
from fcc_python_tools.locations import loc
```

where `loc.ROOT` for example provides the home directory of the project.

This project is intended as an example analysis framework, to demonstrate how to load and analyse FCC simulation data and produce some useful output. Users are free to extend the code by adding their own functions to `PYTHON` and writing their own dedicated analysis scripts.

## uproot and awkward array

Generated events produced in [FCCSW](https://github.com/HEP-FCC/FCCSW) are stored in `ROOT` files. In this project, these files are loaded using the [uproot](https://github.com/scikit-hep/uproot4) package, which provides fast, `ROOT`-independent file loading into python. The events are handled using [awkward array](https://github.com/scikit-hep/awkward-1.0), which provides `numpy`-like access to jagged data (different numbers of particles in each event). This enables analysis at array-level, where all events are analysed with a single command without the use of loops.

# FCC python tools

This repository hosts code that uses `uproot`, `awkward array`, and other core python packages to load and analyse FCC simulation.

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

In the `setup.sh` script, several environment variables are defined which can be added to by the user. ROOT files produced by FCCSW can be placed in `DATA` for example, and analysis scripts placed in `SCRIPTS`. Any `matplotlib` plots produced are saved in `PLOTS`, with LaTeX tables stored in `.tex` format in `TABLES`. Analysis results can be stored into dictionaries and written to `.json` files for subsequent use - these files are placed in `JSON`.

This project is intended as an example analysis framework, to demonstrate how to load and analyse FCC simulation data and produce some useful output. Users are free to extend the code by adding their own analysis scripts.

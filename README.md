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

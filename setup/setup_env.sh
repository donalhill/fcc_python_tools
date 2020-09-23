#Setup conda env to install all required packages into - includes root
wget -nv http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
source $HOME/miniconda/etc/profile.d/conda.sh
conda create -n fcc_pyenv python=3.7 root -c conda-forge
conda activate fcc_pyenv
conda config --env --add channels conda-forge
#Install required packages
conda install -y uncertainties matplotlib pandas jupyter ipykernel
pip install uproot4 awkward1 particle
#Enable our conda env for use in the Jupyter notebooks
python -m ipykernel install --user --name=fcc_pyenv

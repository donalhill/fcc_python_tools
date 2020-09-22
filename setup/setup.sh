#!/bin/bash

shopt -s expand_aliases

## Define root variable
export ANAROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"

set +u

source ~/miniconda/etc/profile.d/conda.sh
conda activate fcc_pyenv

cd $ANAROOT

export PYTHONPATH=$ANAROOT:$ANAROOT/python:$PYTHONPATH

# Locations
export DATA=$ANAROOT/data
export PYTHON=$ANAROOT/python
export EXAMPLES=$ANAROOT/examples
export PLOTS=$ANAROOT/output/plots
export TABLES=$ANAROOT/output/tables
export JSON=$ANAROOT/output/json

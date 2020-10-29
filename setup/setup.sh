#!/bin/bash

shopt -s expand_aliases

## Define root variable
export ANAROOT=${CERNBOX_HOME}SWAN_projects/fcc_python_tools

set +u

cd $ANAROOT

user=$USER
userfirst=${user:0:1}
export PATH=/eos/user/$userfirst/$user/.local/bin:$PATH
export PYTHONPATH=$HOME/.local/lib/python3.7/site-packages:$ANAROOT:$PYTHONPATH

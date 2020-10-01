#!/bin/bash

shopt -s expand_aliases

## Define root variable
export ANAROOT=${CERNBOX_HOME}SWAN_projects/fcc_python_tools

set +u

cd $ANAROOT

export PYTHONPATH=$ANAROOT:$PYTHONPATH

#!/bin/bash

if [ $# -eq 1 ]; then
    PROJECT_PATH=$1
else
    echo "ERROR: Please fill the first parameter with path."
    exit 1
fi

cd $PROJECT_PATH/git/tools

./normalize-permissions.sh $PROJECT_PATH
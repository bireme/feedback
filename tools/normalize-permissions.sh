#!/bin/bash

if [ $# -eq 1 ]; then
    PROJECT_PATH=$1
else
    echo "ERROR: Please fill the first parameter with path."
    exit 1
fi

chown -R root:bvs $PROJECT_PATH

find $PROJECT_PATH/bireme -type f -exec chmod 664 {} \;
find $PROJECT_PATH/bireme -type d -exec chmod 775 {} \; 
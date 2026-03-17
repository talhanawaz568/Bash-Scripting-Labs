#!/bin/bash

DIRECTORY="/root/filesystem/home/ubuntu/labs/error_handling/undir"

if [ -d "$DIRECTORY" ]; then
    echo "Directory exists."
else
    echo "Error: Directory does not exist."
    echo "Please create the directory before proceeding."
    exit 1
fi

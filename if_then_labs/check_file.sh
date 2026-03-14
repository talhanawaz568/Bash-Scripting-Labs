#!/bin/bash
FILENAME="example.txt"
if [ -f "$FILENAME" ]; then
	echo "File exits."
else
	echo "File not found."
fi

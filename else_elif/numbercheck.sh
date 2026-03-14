#!/bin/bash
if [ -z "$1" ]; then
	echo "No number Provided. Usage: ./numbercheck.sh <number>"
	exit 1
fi

number=$1

if [ "$number" -gt 10  ]; then
	echo "Above 10"
elif [ "$number" -eq 10 ]; then
	echo "Exactly 10"
else
	echo "Below 10"
fi


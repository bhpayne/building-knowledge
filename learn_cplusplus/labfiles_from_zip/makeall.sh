#!/bin/bash

# Run this script in the labfiles directory to build
# all the examples and solutions

# Note that there are two examples which intentionally
# have compile errors

# Use command line argument of 'clean' to delete all
# the .o files and all the executables

for i in `find $PWD -type d`
do
	cd $i
	if [ -f makefile ]
	then
		echo "RUNNING makefile in $i"
		if [ $# -eq 1 ]
		then
			make $1
		else
			make
		fi
	fi
done

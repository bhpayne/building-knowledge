#!/bin/bash
# Ben Payne <ben.is.located@gmail.com>
# run multiple Python scripts
if [ "$#" -ne 2 ]; then
  echo
  echo "     Usage: $0 <number of cores> <name of python file>" >&2
  echo
  exit 1
fi

# $1 = number of cores
# $2 = python file name

for (( core_indx=1; core_indx<=$1; core_indx++ ))
do
  echo "core number: $core_indx    number of cores: $1"
  echo "python $2 $core_indx $1" # $2 = python file name, $1 = number of cores
  python $2 $core_indx $1
  sleep 2
done

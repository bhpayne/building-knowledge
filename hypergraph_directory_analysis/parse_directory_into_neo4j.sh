#!/bin/bash

path_to_files=/Users/benpayne/Desktop
list_of_files=`find $path_to_files`

for elemnt in $list_of_files; do
  echo $elemnt
done
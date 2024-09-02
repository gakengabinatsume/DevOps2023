#!/bin/bash

#Input in the command line the file path or modify below

#file="C:\Users\Power User\Desktop\file.txt"
file=$12

#Input in the command line the search word (case-insensitive)

while IFS= read line
do
    grep -i $2
done <"$file"

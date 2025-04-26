#!/bin/bash
count=0
for D in */; 
do 
    cd $D;
    echo "Running in $D\n";
    mv *.$1 ../ ;
    echo "Switching back a dir\n";
    cd ..;
#    count=$((count + 1));  
done

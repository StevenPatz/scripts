#!/bin/bash
count=0
for D in */; 
do 
    cd $D;
    echo "Running in $D\n";
    cp ~/scripts/video/jpg_to_mp4.sh . ; mkdir img_in_order ; sh jpg_to_mp4.sh $1_$count;
    #cp ~/scripts/video/jpg_to_mp4.sh . ; mkdir img_in_order ; sh jpg_to_mp4.sh 20230529_safeway_$count;
    echo "Switching back a dir\n";
    cd ..;
    count=$((count + 1));  
done

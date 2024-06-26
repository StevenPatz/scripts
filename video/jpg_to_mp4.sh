#!/bin/bash
# TODO
x=1
echo "Starting the chopping process.\n\n"
for i in G*.JPG
  do 
    switcherooctl launch convert $i -gravity South -chop 0x850 $i
    [ $((x%10)) -eq 0 ] && echo -n "-"
    x=$(($x+1))
  done
echo "\n\n Starting the linking process.\n\n"
date=`date +%F`
if [ "$#" -lt "1" ]
  then echo
    echo "Please provide a name for the file"
    echo
  else 
    x=1;
    for i in G*.JPG
      do counter=$(printf %06d $x)
        ln "$i" img_in_order/img"$counter".jpg
        [ $((x%10)) -eq 0 ] && echo -n "+"
        x=$(($x+1))
      done
echo "\n"
switcherooctl launch ffmpeg -hide_banner -v warning -stats -i "img_in_order/img%06d.jpg" -r 30 -s hd1080 -preset slow -threads 15 -pix_fmt yuv444p $date_$1.mp4
fi

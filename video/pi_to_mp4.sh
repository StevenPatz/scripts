#!/bin/bash
x=1
echo "Starting the Pi jpg chopping process.\n\n"
for i in G*.jpg
  do 
    switcherooctl launch convert $i -gravity South -chop 0x650 $i
    [ $((x%10)) -eq 0 ] && echo -n "-"
    x=$(($x+1))
  done
 #In the GoPro script I had to create symlinks so that all the files are in order. For now, the way the Pi camera creates images, they are all in one directory and in order so the ffmpeg step can be run directly.
 #
 #
 # Will probably have to bring this back ( which is why I'm not straight up deleting it) once I figure out a structure for the Pi process.
 #
 #

# echo "\n\n Starting the linking process.\n\n"
# date=`date +%F`
# if [ "$#" -lt "1" ]
#   then echo
#     echo "Please provide a name for the file"
#     echo
#   else 
#     x=1;
#     for i in G*.JPG
#       do counter=$(printf %06d $x)
#         ln "$i" img_in_order/img"$counter".jpg
#         [ $((x%10)) -eq 0 ] && echo -n "+"
#         x=$(($x+1))
#       done
# echo "\n"
# switcherooctl launch ffmpeg -hide_banner -v warning -stats -i "img_in_order/img%06d.jpg" -r 30 -s hd1080 -preset slow -threads 15 -pix_fmt yuv444p $date_$1.mp4
# fi
echo "\n\n Making the Pi Video.\n\n"
ffmpeg -hide_banner -v warning -stats -i "G%07d.jpg" -r 30 -s hd1080 -preset slow -threads 16 -pix_fmt yuv444p $date_$1.mp4
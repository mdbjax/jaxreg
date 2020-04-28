#!/bin/bash 

# This script is used to correctly update the database with the proper container size
# Originally written to retroactively update sizes for previously uploaded containers when sizing was first implemented. 

#Get file 
du --apparent /var/www/images/*/*.sif | awk -F/ '{print $1 " " $6}' > /code/scripts/filenames.txt 
while read size filename; do
	export name=`echo $filename | awk 'BEGIN {FS="-sha256"}{print $1}'`
	#echo $name
	export version=${filename#"$name-"}
	export version=${version%".sif"}
	#echo $version 
	export size=$(($size / 1024 ))
	#echo $size
	echo "$name $version $size" >> /code/scripts/update_info
	#echo $version
	#for entry in $files; do
		 
	#done
done </code/scripts/filenames.txt

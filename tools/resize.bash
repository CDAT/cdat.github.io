#!/bin/bash

if [ $# -eq 0 ]
then
	echo "Usage: resize.bash /path/to/media"
	exit 1;
fi

media_dir=$1
if [ `basename $media_dir` = "media" ]
then
	echo "Found media directory... resizing"
	media_dir=${media_dir%/}

	for f in $media_dir/gallery/fullsize/*.png; do
		echo "Resizing $f";
		filename=${f##*/}
		convert $f -resize 300x250 $media_dir/gallery/thumbnails/$filename;
	done
else
	echo "Did not find media directory";
	exit 1;
fi


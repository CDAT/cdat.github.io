#!/bin/bash

if [ $# -eq 0 ]
then
	echo "Usage: deploy.bash /path/to/site-home/"
	exit 1;
fi

base_dir=$1;
media_dir=$base_dir'_site';

cd $base_dir;
git pull --recurse-submodules;
/usr/local/bin/jekyll b;
mkdir _site/gallery/thumbnails;
./_tools/resize.bash $media_dir;

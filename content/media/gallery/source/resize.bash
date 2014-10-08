for f in ../fullsize/*.png; do convert $f -resize 190x190 ../thumbnails/$f; done

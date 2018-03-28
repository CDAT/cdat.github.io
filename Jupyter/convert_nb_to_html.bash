#!/usr/bin/env bash
cd $1
jupyter-nbconvert $1.ipynb --to html
cat > tmp.txt << EOF
---
layout: default
title: $1 Tutorial
---

# $1 Tutorial
[download iPython Notebook]($1.ipynb)
EOF

cat tmp.txt $1.html > $1.html.final
rm tmp.txt $1.html
mv $1.html.final $1.html
cd ..

#!/usr/bin/env bash
cd $1
jupyter-nbconvert $1.ipynb --to markdown
cat > tmp.txt << EOF
---
layout: default
title: $1 Tutorial
---

# $1 Tutorial
[download iPython Notebook]($1.ipynb)
EOF

cat tmp.txt $1.md > $1.md.final
rm tmp.txt $1.md
mv $1.md.final $1.md
cd ..

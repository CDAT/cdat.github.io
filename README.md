# cdat.github.io
CDAT website

Note: After cloning this repo, you will want to update submodules in order to properly preview the site locally using Jekyll.

To include submodules:
```bash
cd cdat.github.io
git submodule update --init --recursive
```

To view the site on local machine with Jekyll:

```bash
conda install -c conda-forge ruby rb-jekyll
gem install pygments.rb
jekyll s
```

Then open browser to: 127.0.0.1:4000/tutorials.html
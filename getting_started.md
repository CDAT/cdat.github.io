---
title: Getting Started with CDAT
layout: default
---

# Welcome to CDAT!

After you've [installed](https://github.com/CDAT/cdat/wiki/install), the next thing to do is try out some examples from the [gallery](http://cdat.llnl.gov/gallery.html)!

To run the examples, you first have to use the unix `source` command to load the CDAT environment.

~~~bash
conda activate [YOUR_CDAT_CONDA_ENV]
~~~

On older anaconda version it might be

~~~bash
source activate [YOUR_CDAT_CONDA_ENV]
~~~

Once you've loaded the environment, you should be able to run the examples. They should output a .png file that has the same image as the example.

We strongly recommend using Jupyter notebook for the tutotrials

~~~
jupyter-notebook
~~~


We also recommend using the interactive python console for figuring out how to use CDAT's scripting capabilities.

To run the interactive console, use the `ipython` command, which should give you something like this:

~~~
Python 2.7.14 | packaged by conda-forge | (default, Dec 25 2017, 01:18:54) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
~~~

To learn more about `ipython`, you can read [this tutorial](http://ipython.org/ipython-doc/2/interactive/tutorial.html).


You can just type `import vcs, cdms2` to load the main two modules of UV-CDAT (to learn more about them, you can check out the [VCS Manual](http://uvcdat.llnl.gov/documentation/vcs/vcs.html) and the [CDMS Manual](http://uvcdat.llnl.gov/documentation/cdms/cdms.html)), then hit enter.

Here's a very simple example that walks you through the most basic steps:

~~~python
import vcs, cdms2, cdat_info

# Download sample data files

vcs.download_sample_data_files()

# The vcs_canvas is the root object of VCS
vcs_canvas = vcs.init()

cdms_file = cdms2.open(vcs.prefix + "/sample_data/clt.nc")

# We'll pull a variable out of the netCDF file
clt_variable = cdms_file("clt")

# And then we'll plot it using the default graphics method (a boxfill) and the default template.
vcs_canvas.plot(clt_variable)

# To output to a .png file, you can just do this:
vcs_canvas.png("clt.png")
# And that's it!
~~~

Hopefully that helps some! If you have any other questions, [let us know](http://cdat.llnl.gov/contact.html)!

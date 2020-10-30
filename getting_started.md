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

We strongly recommend using Jupyter notebooks for the tutorials. When you type the command below into your command-line window (e.g. Command Prompt for Windows or Terminal Window for Mac) it is best to have navigated via the command line to the folder that contains your Jupyter Notebooks either as single files (file extention .ipynb) or contained in subfolders. For additional help on Jupyter Notebooks see this [Jupyter Documentation](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) page.

~~~
jupyter notebook
~~~


We also recommend using the interactive python console for figuring out how to use CDAT's scripting capabilities.

To run the interactive console, use the `ipython` command, which should give you something like this:

~~~
Python 3.7.8 | packaged by conda-forge | (default, Jul 31 2020, 02:37:09) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.17.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
~~~

To learn more about `ipython`, you can read [this tutorial](http://ipython.org/ipython-doc/2/interactive/tutorial.html).


You can just type `import vcs, cdms2` to load the main two modules of UV-CDAT (to learn more about them, you can check out the [VCS Manual](https://cdat-vcs.readthedocs.io/en/latest/) and the [CDMS Manual](http://cdms.readthedocs.io/en/cdmsdocsmerge/)), then hit enter.

Here's a very simple example that walks you through the most basic steps:

~~~python
import vcs, cdms2
import os
import cdat_info

# Download sample data files

vcs.download_sample_data_files()

# The vcs_canvas is the root object of VCS
vcs_canvas = vcs.init()

cdms_file = cdms2.open(os.path.join(cdat_info.get_sampledata_path(), "clt.nc"))

# We'll pull a variable out of the netCDF file
clt_variable = cdms_file("clt")

# And then we'll plot it using the default graphics method (a boxfill) and the default template.
vcs_canvas.plot(clt_variable)

# To output to a .png file, you can just do this:
vcs_canvas.png("clt.png")
# And that's it!
~~~

Hopefully that helps some! If you have any other questions, [let us know](http://cdat.llnl.gov/contact.html)!

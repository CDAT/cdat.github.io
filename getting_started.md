---
title: Getting Started with UV-CDAT
layout: default
---

# Welcome to UV-CDAT!

After you've [installed](/installing.html), the next thing to do is try out some examples from the [gallery](/gallery.html)!

To run the examples, you first have to use the unix `source` command to load the UV-CDAT environment.

If you installed using a binary:

~~~bash
source /usr/local/uvcdat/bin/setup_runtime.sh
~~~

If you installed from source:

~~~bash
source /THE/PATH/YOU/INSTALLED/TO/bin/setup_runtime.sh
~~~

You can type `which python` to verify that you're properly set up (should output something like `/usr/local/uvcdat/bin/python` for a binary install, or the path to your installation followed by `/bin/python` for a source install)

Once you've loaded the environment, you should be able to run the examples. They should output a .png file that has the same image as the example.

We strongly recommend using the interactive python console for figuring out how to use UV-CDAT's scripting capabilities.

To run the interactive console, use the `ipython` command, which should give you something like this:

~~~
Python 2.7.10 (default, Sep 11 2015, 11:53:27)
Type "copyright", "credits" or "license" for more information.

IPython 3.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
~~~

To learn more about `ipython`, you can read [this tutorial](http://ipython.org/ipython-doc/2/interactive/tutorial.html).


You can just type `import vcs, cdms2` to load the main two modules of UV-CDAT (to learn more about them, you can check out the [VCS Manual](/documentation/vcs/vcs.html) and the [CDMS Manual](/documentation/cdms/cdms.html)), then hit enter.

Here's a very simple example that walks you through the most basic steps:

~~~python
import vcs, cdms2, cdat_info
# The vcs_canvas is the root object of VCS
vcs_canvas = vcs.init()

uvcdat_version = cdat_info.version()

# Now we'll load a netCDF file using CDMS2
if uvcdat_version[0] <= 2 and uvcdat_version[1] <= 2 and uvcdat_version[2] == 0:
    # This is the way to find the sample data if you installed 2.2.0 (from the binary)
    cdms_file = cdms2.open(vcs.prefix + "/sample_data/clt.nc")
else:
    # Versions newer than 2.2 use vcs.sample_data instead of vcs.prefix
    # This would only happen if you installed from source; the examples
    # in the gallery don't cover newer versions than 2.2,
    # since that's still the most recent version.
    cdms_file = cdms2.open(vcs.sample_data + "/clt.nc")

# We'll pull a variable out of the netCDF file
clt_variable = cdms_file("clt")

# And then we'll plot it using the default graphics method (a boxfill) and the default template.
vcs_canvas.plot(clt_variable)

# To output to a .png file, you can just do this:
vcs_canvas.png("clt.png")
# And that's it!
~~~

Hopefully that helps some! If you have any other questions, [let us know](/contact.html)!
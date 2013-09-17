##Post CDAT install, enabling VCDAT

Once CDAT is built with either [configure](https://github.com/UV-CDAT/uvcdat/wiki/Building-CDAT) or 

    DATCMakeBuild|CMake

You will need to run (using the executable located under your install path)

    easy_install lepl
    easy_install MyProxyClient

The VCDAT GUI has been rebuilt from ground up and is now part of UV-CDAT. You will need to clone the repo in a separate directory from the CDAT repo

    git clone git://uv-cdat.llnl.gov/uv-cdat.git

or if your git port is blocked by your institution

    git clone http://uv-cdat.llnl.gov/git/uv-cdat.git

Now actually build VCDAT

    cd uv-cdat/Packages/qtbrowser
    python setup.py install

You should now be able to find under your cdat install path:

    vcdat

uv-cdat should also download the latest vistrails sources for you. So you can try to launch vistrails and enable CDAT in it.

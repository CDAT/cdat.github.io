##Building CDAT

To install CDAT under /blabla directory:
    
    git clone git://uv-cdat.llnl.gov/cdat.git
    cd cdat
    ./configure --prefix=/blabla [--with-qt=/path/to/qt] [--with-qt-bin=/path/to/qt/bin/dir] [--with-qt-lib=/path/to/qt/lib/dir] [--with-qt-inc=/path/to/qt/include/dir] [--with-externals=/path/to/externals]
    # ON mac also add --enable-framework=/blabla #where /blabla matches prefix
    # By default Externals are built under [prefix]/Externals
    make

###Known Tweaks
####Mac

* Make sure to have --enable-framework= to match --prefix=
* 10.6 make sure you download 64bit version of Qt
* Qt args:

        --with-qt-bin=/usr/bin --with-qt-lib=/Library/Frameworks --with-qt-inc=/Library/Frameworks

####Linux

* The following packages should be installed before building CDAT
  * git
  * git-tk
  * qt4-devel
  * xorg-devel
  * CMake
  * gfortran
  * ssl-devel
  * xrender-devel
  * curl

####Ubuntu

* Correct qt args are:

        --with-qt-bin=/usr/bin --with-qt-lib=/usr/lib --with-qt-inc=/usr/include/qt4

####Externals Dependencies

Software | Minimum Required Version | Version Built by CDAT if not found on system
--- | --- | --- |
python | 2.7.0 | 2.7.1
setuptools | 0.6 | 0.6c11
numpy | 1.5.1 | 1.5.1
tcl/tk | 8.5.4 | 8.5.9
QT | 4.6.2 | 4.7.0
sip | 4.11.1 | 4.11.1
[PyQt]() | 4.7.6 | 4.7.7
readline | 5.2 | 6.2
zlib | any | 1.2.5
termcap | any | 1.3.1
freetype | 9.7.3 | 2.4.4
fontconfig | 2.4.2 | 2.8.0
pkg-config | 0.9.0 | 0.25.0
cairo | 1.8.10 | 1.10.2
libpixman | 0.20.2 | 0.20.2
ffmpeg | any | ?
jpeg | any | 6b
libpng | 1.4.1 | 1.5.1
libxml | 2.6.27 | 2.7.8
libxslt | 1.1.22 | 1.1.26
Ghostscript | any | ?
gifsicle | any | 1.58
pbmplus | any | ?
cmake | 2.8 | 2.8.2
jasper | any | 1.900.1 
g2clib | any | 1.2.4
libcurl | 7.19.7 | 7.21.3
hdf5 | 1.8.5.patch1 | 1.8.5.patch1
netcdf | 4.1.2 | 4.1.2
libuuid | any | 1.6.2
udunits2 | any | 2.1.14


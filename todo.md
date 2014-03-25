* ~~add to About   --> uvcdat-basics~~
* http://uvcdat.llnl.gov/installing.html
  *  ~~Obtaning -> ObtaIning~~
  *  ~~what platforms is uvcdat available on?~~
  *  ~~what packages are available in CDAT~~
  *  ~~some licensing information?~~ 
* ~~rename 'Documents' to Press~~
* ~~'Help->Tutorials' is not enough  rename Help to User Guides~~
* mobile menu is not displaying correctly
* ~~Should there be a 'sign' after the links that go to an external web page (ie, links to the cdat wiki?)~~
* ~~Maybe all the external links should open in the same window~~
  * ~~(with a target="uvcdat_out" directive) rather than opening plenty of new windows?~~
  * ~~**this is a browser setting tabs not windows**~~
* https://github.com/UV-CDAT/uvcdat/wiki/System-Requirements
  * Mac - All Versions : lots of typos
  * Linux - Ubunutu names=> ubuntu names - available form=> available from
* ~~You may want to add a 'Windows' section saying that cdat is not available for windows~~
* https://github.com/UV-CDAT/uvcdat/wiki/Install-Binaries
 * Current Version is: 1.2.0rc1	=> 1.4 ???
 * There should be an explicit link from this page to the sourceforge download page in section 1 http://sourceforge.net/projects/cdat/files/Releases/UV-CDAT/1.4/
  * WARNING! You are installing the binaries in '/', so it would be a good idea to give the required disk space (for each version/platform), so that the users don't crash their system by filling up their '/' (eg if home dir and /tmp are not on separate partitions)  
  * Download the tarsal	=> tarball
* https://github.com/UV-CDAT/uvcdat/releases  -> https://github.com/UV-CDAT/uvcdat/wiki/Roadmap-to-Release
  * 1.4.0 and uvcdat-1.4.0 => seem to be duplicates! => same for rc1 and rc2
  * It would be VERY useful to have a summary of the changes since the previous version, not just "Merge branch 'ubunutu-pkg-config-path'" or "Merge branch 'new_init_file'"
* https://github.com/UV-CDAT/uvcdat/wiki/Building-UVCDAT
  * "Building UV-CDAT with CMake is supported" => "You need a recent version of CMake (2.8.8 or later) in order to install UV-CDAT"
  * Charles, you may want to add a note that when you do a clone, you get the latest stable version, and not the tagged version listed on the 'releases' page. It's one of the many things that are not obvious for people who are not familiar with git. The fact that 2 people who get uvcdat at slightly different times may get slightly different versions
may be confusing
* add a page about the dependencies! Note: you should probably add the link to the apropriate Qt download page and let people know what compilation options they should use for qt, on the' Building-UVCDAT' or 'System-Requirements' pages
* on the building page, specify that the installed version of uv-cdat will be by default in the 'install' subdirectory of build (am I correct). You don't want them removing all (including 'install') the content of the build directory to make space
* tell people what initialization script they should run, in order to use what was just compiled
* What do I lose/gain if I turn the //ism off/on with
  * CDAT_BUILD_PARALLEL=OFF
* For the rebuild part, you should specify that you have to be in the build directory
* Also, what's not very clear is how can you start the test suite of uv-cdat (independently of the dashboard. Aashish mentionned that you have to turn on an option in ccmake, right? Which one? And what do you have to type (and where) to start the tests after the build is finished?
* It could be useful to tell the users how much space everything is going to take, and which directories have to be kept (and NOT moved/renamed), and which ones can be erased (eg, keep the installation dir of Qt, but not the compilation dir, etc...)

---

I thought I would try installing the CDAT redhat binaries on the brand
new Fedora Core 20 I have recently installed on my virtualbox. You will
find below lots of thoughts about the uv-cdat web site, and my final failure

1) I think that the download on the front page, in "UV-CDAT 1.5 has been
released! Download " should rather be a link to
https://github.com/UV-CDAT/uvcdat/wiki/Install-Binaries, rather than a
direct link to sourceforge. Because what do you do when you are on
sourceforge and you don't know anything about cdat?

2) There should be a link to the sf binaries install page at the top of
the Install binaries page!

3) When you are on the sourceforge page, and then go to the sf wiki
page, there should be a link back to the cdat binaries installation page

4) You have written on the web site
	
        sudo tar xjv qt-RH6-64bit-4.8.0.tar.bz2

I have TWO problems with that

a) it's missing the "f" option and should be "tar xjvf". Does not work
without the "f"

b) are you sure the file is in bzip format? Because I can untar it with
"tar xvf", but I get the following error if I use "xvjf"

        sudo tar xjvf /media/sf_jyp_scratch/UV-CDAT/qt-RH6-64bit-4.8.5.tar.bz2
        bzip2: (stdin) is not a bzip2 file.
        tar: Child returned status 2
        tar: Error is not recoverable: exiting now

        Untar+"j" worked fine with the uvcdat archive

5) It would be useful if you specified that the archives are going to
extract to usr/local/uvcdat and usr/local/Qt and how MUCH space is
required (so that you know before downloading the zip files). I get the
following on my system, after untarring

        du -sh Qt uvcdat
      	453M	Qt
      	2.1G	uvcdat

It's not thaaat much, but I'm doing it in a virtual machine where I only
have 30 Gb (including the system and everything) and I'm lucky I did not
have a predefined small /usr/local partition

6) Since you don't know the unix level of the people who are going to
install the binaries, you may want to help them by telling them to
download the tar files to a temporary directory. Because if they do it
on "/", they will have even less space for the installation!

	Download IN A TEMPORARY DIRECTORY and untar the binaries best matching
your OS.

  	    cd /
      	sudo tar xjvf <my_temp_directory>/UV-CDAT-[version number]-[your OS here].tar.bz2

7) Is it possible to trim down the installation (and download) by
removing the following directory ?

        du -sh uvcdat/1.5.0/vistrails/.git
      	152M	uvcdat/1.5.0/vistrails/.git


Now that I'm ready to use uvcdat, I initialize it with your init script,
and run into a missing OLD library that you don't mention in your
dependencies. See below

    > python -v
    [...]
    dlopen("/usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so", 2);
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File
    "/usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/__init__.py",
    line 28, in <module>
         import _vcs
    ImportError: libpng12.so.0: cannot open shared object file: No such file
    or directory
    >>>
    
    ldd /usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so
    [...]
    	libpng12.so.0 => not found
    [...]
    
    [root@lsce3017 ~]# rpm -qa | grep -i libpng
    libpng-1.6.3-3.fc20.i686
    libpng-1.6.3-3.fc20.x86_64
    libpng-devel-1.6.3-3.fc20.x86_64
    [root@lsce3017 ~]# yum --disablerepo=lsce search libpng
    [...]
    libpng12.x86_64 : Old version of libpng, needed to run old binaries
    
I install this libpng, try to import vcs and then get another problem!
It seems (see the ldd below) that my installed libxml2 lib is having
problems with a libz installed in uvcdat!

    $ python -v
    [...]
    >>> import vcs
    [...]
    dlopen("/usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so", 2);
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File
    "/usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/__init__.py",
    line 28, in <module>
         import _vcs
    ImportError: /lib64/libxml2.so.2: symbol gzopen64, version ZLIB_1.2.3.3
    not defined in file libz.so.1 with link time reference
    
    $ ldd /usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so
    /usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so:
    /usr/local/uvcdat/1.5.0/Externals/lib/libz.so.1: no version information
    available (required by /lib64/libxml2.so.2)
    /usr/local/uvcdat/1.5.0/lib/python2.7/site-packages/vcs/_vcs.so:
    /usr/local/uvcdat/1.5.0/Externals/lib/libz.so.1: no version information
    available (required by /lib64/libxml2.so.2)
    	linux-vdso.so.1 =>  (0x00007fffd8157000)
    	libfreetype.so.6 =>
    /usr/local/uvcdat/1.5.0/Externals/lib/libfreetype.so.6 (0x00007f8ea7f51000)
    	libcairo.so.2 => /usr/local/uvcdat/1.5.0/Externals/lib/libcairo.so.2
    (0x00007f8ea7bf6000)
    	libnetcdf.so.7 => /usr/local/uvcdat/1.5.0/Externals/lib/libnetcdf.so.7
    (0x00007f8ea7889000)
    	libpng15.so.15 => /usr/local/uvcdat/1.5.0/Externals/lib/libpng15.so.15
    (0x00007f8ea7652000)
    	libjasper.so.1 => /usr/local/uvcdat/1.5.0/Externals/lib/libjasper.so.1
    (0x00007f8ea73dd000)
    	libpython2.7.so.1.0 => /usr/local/uvcdat/1.5.0/lib/libpython2.7.so.1.0
    (0x00007f8ea6ffd000)
    	libQtCore.so.4 => /usr/local/Qt/4.8.5/lib/libQtCore.so.4
    (0x00007f8ea6b19000)
    	libQtGui.so.4 => /usr/local/Qt/4.8.5/lib/libQtGui.so.4 (0x00007f8ea5e25000)
    	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007f8ea5afb000)
    
What am I supposed to do here? Install libzip? Remove the libz.so.1 file
from your Externals? Change the LD_LIBRARY_PATH your init script sets up?

The way the installation page is designed (or maybe it is the way my
mind works)

	http://uvcdat.llnl.gov/installing.html

I ended up reading the "X Window System" section first.

This section is quite interesting (did not know about this nomachine
stuff), BUT it has nothing to do with installation (it's "remote usage
of something already installed") and should rather be in a yet to be
created FAQ page, probably in the "User Guides" ("Users' Guides"? =>
"Documentation") pull down menu


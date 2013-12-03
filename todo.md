add to 'About
+ what platforms is uvcdat available on?
+ what packages are available in CDAT
+ some licensing information? => I think you (Charles) answered this question

rename 'Documents'

'Help->Tutorials' is not enough


mobile menu is not displaying correctly

* http://uvcdat.llnl.gov/installing.html
	Obtaning -> ObtaIning

Should there be a 'sign' after the links that go to an external web page
(ie, links to the cdat wiki?)

* Maybe all the external links should open in the same window (with a
target="uvcdat_out" directive) rather than opening plenty of new windows?
//this is a browser setting tabs not windows!


* https://github.com/UV-CDAT/uvcdat/wiki/System-Requirements

Mac - All Versions : lots of typos

Linux
	ubunutu names	=> ubuntu names
	available form	=> available from

You may want to add a 'Windows' section saying that cdat is not
available for windows

* https://github.com/UV-CDAT/uvcdat/wiki/Install-Binaries

Current Version is: 1.2.0rc1	=> 1.4 ???

There should be an explicit link from this page to the sourceforge
download page in section 1
	http://sourceforge.net/projects/cdat/files/Releases/UV-CDAT/1.4/

WARNING! You are installing the binaries in '/', so it would be a good
idea to give the required disk space (for each version/platform), so
that the users don't crash their system by filling up their '/' (eg if
home dir and /tmp are not on separate partitions)

Download the tarsal	=> tarball

* https://github.com/UV-CDAT/uvcdat/releases

1.4.0 and uvcdat-1.4.0	=> seem to be duplicates!
	=> same for rc1 and rc2

It would be VERY useful to have a summary of the changes since the
previous version, not just "Merge branch 'ubunutu-pkg-config-path'" or
"Merge branch 'new_init_file'"

* https://github.com/UV-CDAT/uvcdat/wiki/Building-UVCDAT

"Building UV-CDAT with CMake is supported" => "You need a recent version
of CMake (2.8.8 or later) in order to install UV-CDAT"

* Charles, you may want to add a note that when you do a clone, you get
the latest stable version, and not the tagged version listed on the
'releases' page. It's one of the many things that are not obvious for
people who are not familiar with git. The fact that 2 people who get
uvcdat at slightly different times may get slightly different versions
may be confusing


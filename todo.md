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

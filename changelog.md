---
title: Changelog
layout: default

---
<a name="8.2.1"></a>

# Releases Notes from Github Repos for Milestone: 8.2.1
 
# cdat_info
 
## Closed Issues

### enhancement

 * ****: [need to turn off logging](https://github.com/CDAT/cdat_info/issues/2) ([#38](https://github.com/CDAT/cdat_info/pull/38), [#40](https://github.com/CDAT/cdat_info/pull/40), [#41](https://github.com/CDAT/cdat_info/pull/41))
 * ****: [Need mecanism to track cdat packages installed and othe rprovenance](https://github.com/CDAT/cdat_info/issues/4) ([#5](https://github.com/CDAT/cdat_info/pull/5))

## Merged Pull Requests

 * [#39: Try new conda recipes](https://github.com/CDAT/cdat_info/pull/39)

## Known Bugs

No known issues!
 
# cdms
 
## Closed Issues

### bug

 * ****: [AttributeError with cdscan](https://github.com/CDAT/cdms/issues/397) ([#399](https://github.com/CDAT/cdms/pull/399))

### pending-release

 * ****: [Attempt to import numpy.ma.rank failing with numpy 1.18.1](https://github.com/CDAT/cdms/issues/384) ([#389](https://github.com/CDAT/cdms/pull/389))
 * ****: [Problems with reading "big" arrays (>8.1Gb)](https://github.com/CDAT/cdms/issues/383) ([#389](https://github.com/CDAT/cdms/pull/389))
 * ****: [While importing cdms2 error pops up: ImportError: cannot import name 'rank'](https://github.com/CDAT/cdms/issues/396)
 * ****: [Problems with udunits in CDAT82](https://github.com/CDAT/cdms/issues/374)

## Merged Pull Requests

 * [#387: replaced numpy.rank() with numpy.ndim(), adding test_setdimattribute*](https://github.com/CDAT/cdms/pull/387)

## Known Bugs

No known issues!
 
# vcs
 
## Closed Issues

### bug

 * ****: [vcs 3D rotating globe animation not working properly](https://github.com/CDAT/vcs/issues/409)
 * ****: [an update triggers continents back on](https://github.com/CDAT/vcs/issues/397) ([#398](https://github.com/CDAT/vcs/pull/398))
 * ****: [transparency does not work for text](https://github.com/CDAT/vcs/issues/396)
 * ****: [text disappear in png with bg=False](https://github.com/CDAT/vcs/issues/308)
 * ****: [vector linewidth not working](https://github.com/CDAT/vcs/issues/381)
 * ****: [createprojection fails if 'polar' template is chosen](https://github.com/CDAT/vcs/issues/102)
 * ****: [manageElements.py setLineAttributes doesn't work](https://github.com/CDAT/vcs/issues/106)
 * ****: [vcs cannot go back into interact mode](https://github.com/CDAT/vcs/issues/86)

### duplicate

 * ****: [wind barb support](https://github.com/CDAT/vcs/issues/90)
 * ****: [dv3d plotting ad changing attributes breaks dv3d](https://github.com/CDAT/vcs/issues/87)

### enhancement

 * ****: [1D plot do not seem to show time/level if available ](https://github.com/CDAT/vcs/issues/415)
 * ****: [Developments with documentation](https://github.com/CDAT/vcs/issues/107)

### fixed in a branch

 * ****: [Automatic xticlabels2 and yticlabels2 don't work](https://github.com/CDAT/vcs/issues/142)

### invalid

 * ****: [Plots sometimes render text twice](https://github.com/CDAT/vcs/issues/124)
 * ****: [ bg=True freaks out on OSMesa builds](https://github.com/CDAT/vcs/issues/119)
 * ****: [Make VCS color palettes easier to edit/add](https://github.com/CDAT/vcs/issues/98)
 * ****: [Several marker problems/differences in 2.1.0 (compared to 1.5.1)](https://github.com/CDAT/vcs/issues/95)
 * ****: [x/yaxisconvert not respected anymore.](https://github.com/CDAT/vcs/issues/96)
 * ****: [Bring back x.colormapgui() (and add color related resources on the web/wiki)?](https://github.com/CDAT/vcs/issues/140)
 * ****: [after first plot you cannot switch between bg or fg](https://github.com/CDAT/vcs/issues/72)

## Merged Pull Requests

 * [#406: Rtd again](https://github.com/CDAT/vcs/pull/406)
 * [#411: Projected isofill bounds](https://github.com/CDAT/vcs/pull/411)
 * [#417: Extra dims slider](https://github.com/CDAT/vcs/pull/417)
 * [#445: Run tests with variants and fix flake8 failures](https://github.com/CDAT/vcs/pull/445)
 * [#446: Add makefile](https://github.com/CDAT/vcs/pull/446)

## Known Bugs

### Other

 * [axisconvert seems to force datawc to be in converted units](https://github.com/CDAT/vcs/issues/416)
 * [Canvas plot with ratio="autot" results in interaction errors](https://github.com/CDAT/vcs/issues/354)

 
# cdutil
 
## Closed Issues

## Merged Pull Requests

 * [#27: Migrate to circle ci](https://github.com/CDAT/cdutil/pull/27)

## Known Bugs

No known issues!
 
# genutil
 
## Closed Issues

### bug

 * ****: [Error in genutils.statistics.percentiles](https://github.com/CDAT/genutil/issues/38) ([#36](https://github.com/CDAT/genutil/pull/36), [#40](https://github.com/CDAT/genutil/pull/40))

## Merged Pull Requests

 * [#28: doesn't dump file unless asked, reads good var in assert func and sav](https://github.com/CDAT/genutil/pull/28)

## Known Bugs

No known issues!
 
# dv3d
 
## Closed Issues

## Merged Pull Requests

 * [#26: Pin mesalib libnetcdf nompi](https://github.com/CDAT/dv3d/pull/26)
 * [#27: Use makefile n matrix](https://github.com/CDAT/dv3d/pull/27)

## Known Bugs

No known issues!
 
# vcsaddons
 
## Closed Issues

## Merged Pull Requests

 * [#40: new baseline for newer vtk](https://github.com/CDAT/vcsaddons/pull/40)
 * [#43: Pin mesalib, add running tests with nompi and opempi libnetcdf, flix flake8](https://github.com/CDAT/vcsaddons/pull/43)
 * [#46: Use makefile n matrix](https://github.com/CDAT/vcsaddons/pull/46)

## Known Bugs

No known issues!
 
# wk
 
## Closed Issues

## Merged Pull Requests

 * [#13: add running tests with nompi, openmpi and mpich libnetcdf](https://github.com/CDAT/wk/pull/13)
 * [#14: add Makefile and use circleci 2.1 matrix](https://github.com/CDAT/wk/pull/14)

## Known Bugs

No known issues!


<a name="8.1"></a>

# Releases Notes from Github Repos for Milestone: 8.1
 
# vcs
 
## Closed Issues

### bug

 * ****: [template.tunits seems to be disabled](https://github.com/CDAT/vcs/issues/380)
 * ****: [portrait plot does not work with python 3 env](https://github.com/CDAT/vcs/issues/368)
 * ****: [cannot replace the default font](https://github.com/CDAT/vcs/issues/345)
 * ****: [text objects with prjection are broken](https://github.com/CDAT/vcs/issues/344)
 * ****: [vcs .addfont seems broken](https://github.com/CDAT/vcs/issues/343)
 * ****: [when 1d is flipped or 2 arrays are passed template shows min/max for xaxis not data](https://github.com/CDAT/vcs/issues/314)
 * ****: [Taylor Diagram with EzTemplate](https://github.com/CDAT/vcs/issues/272) ([#300](https://github.com/CDAT/vcs/pull/300))
 * ****: [Taylor diagram loses y-axis with 2.12 version](https://github.com/CDAT/vcs/issues/253)
 * ****: [3d_scalar seg faults on mac](https://github.com/CDAT/vcs/issues/245)
 * ****: [1D plots are taking longer than expected ](https://github.com/CDAT/vcs/issues/195) ([#334](https://github.com/CDAT/vcs/pull/334))

### enhancement

 * ****: [Color maps could look better](https://github.com/CDAT/vcs/issues/238)

### invalid

 * ****: [Postscript files are truncated on Mac OS X Sierra](https://github.com/CDAT/vcs/issues/310)

### question

 * ****: [Tick label size adjustment](https://github.com/CDAT/vcs/issues/339)
 * ****: [Plot creates new graphics method objects](https://github.com/CDAT/vcs/issues/268)
 * ****: [viewport error for polar map projection](https://github.com/CDAT/vcs/issues/262)

## Merged Pull Requests

 * [#118: otherwise will push on every commit](https://github.com/CDAT/vcs/pull/118)
 * [#120: correct travis syntax](https://github.com/CDAT/vcs/pull/120)
 * [#123: 121 missing value opacity](https://github.com/CDAT/vcs/pull/123)
 * [#131: Doctest cleanup](https://github.com/CDAT/vcs/pull/131)
 * [#295: Ez plot](https://github.com/CDAT/vcs/pull/295)
 * [#297: Cdat logo](https://github.com/CDAT/vcs/pull/297)
 * [#302: cdtime broken for py3](https://github.com/CDAT/vcs/pull/302)
 * [#316: [WIP] Log axes 2d](https://github.com/CDAT/vcs/pull/316)
 * [#317: fix #251](https://github.com/CDAT/vcs/pull/317)
 * [#319: Test for fillarea concave.](https://github.com/CDAT/vcs/pull/319)
 * [#378: Fix some places where the truncation fix was missed](https://github.com/CDAT/vcs/pull/378)
 * [#389: Add support for the 'reference' attribute on the vector gm](https://github.com/CDAT/vcs/pull/389)

## Known Bugs

### Other

b" * [b'vector linewidth not working'](b'https://github.com/CDAT/vcs/issues/381')"
b" * [b'template x/ymintics1 seems to be using line property of x/ytic1 for last label'](b'https://github.com/CDAT/vcs/issues/379')"
b" * [b'text disappear in png with bg=False'](b'https://github.com/CDAT/vcs/issues/308')"
b" * [b'Black png returned when using a vnc session'](b'https://github.com/CDAT/vcs/issues/117')"
 
# cdutil
 
## Closed Issues

## Merged Pull Requests

 * [#6: Documentation](https://github.com/CDAT/cdutil/pull/6)
 * [#7: Is monthly cal bug](https://github.com/CDAT/cdutil/pull/7)
 * [#8: add License files for conda-forge](https://github.com/CDAT/cdutil/pull/8)
 * [#22: Issu#136 region](https://github.com/CDAT/cdutil/pull/22)

## Known Bugs

No known issues!
 
# genutil
 
## Closed Issues

### enhancement

 * ****: [Docstrings](https://github.com/CDAT/genutil/issues/2) ([#22](https://github.com/CDAT/genutil/pull/22), [#21](https://github.com/CDAT/genutil/pull/21))

## Merged Pull Requests

 * [#7: Documentation](https://github.com/CDAT/genutil/pull/7)
 * [#8: add License files for conda-forge](https://github.com/CDAT/genutil/pull/8)

## Known Bugs

No known issues!
 
# dv3d
 
## Closed Issues

## Merged Pull Requests

 * [#24: forcing 3.6 python](https://github.com/CDAT/dv3d/pull/24)

## Known Bugs

No known issues!
 
# vcsaddons
 
## Closed Issues

### enhancement

 * ****: [parallelcoordinate plot fails if number of linecolors is greater than actual number of lines](https://github.com/CDAT/vcsaddons/issues/32) ([#33](https://github.com/CDAT/vcsaddons/pull/33))

## Merged Pull Requests

 * [#18: Ez plot](https://github.com/CDAT/vcsaddons/pull/18)
 * [#19: almost all fixed](https://github.com/CDAT/vcsaddons/pull/19)
 * [#20: Fixed EzPlot tests.](https://github.com/CDAT/vcsaddons/pull/20)
 * [#38: Bad conda](https://github.com/CDAT/vcsaddons/pull/38)
 * [#39: no dowgrade](https://github.com/CDAT/vcsaddons/pull/39)

## Known Bugs

No known issues!

# cdms
 
## Closed Issues

### bug

 * ****: [axis.clone does not clone anymore!](https://github.com/CDAT/cdms/issues/271) ([#272](https://github.com/CDAT/cdms/pull/272))
 * ****: [Axis units in .attributes and .units not equal](https://github.com/CDAT/cdms/issues/246) ([#267](https://github.com/CDAT/cdms/pull/267))
 * ****: [nightlies broken](https://github.com/CDAT/cdms/issues/245)
 * ****: [Shapes not aligned rrror when appending to a FileVariable in Python 3](https://github.com/CDAT/cdms/issues/240)
 * ****: [regrid broken?](https://github.com/CDAT/cdms/issues/237)
 * ****: [nc4 classic file can't be edited](https://github.com/CDAT/cdms/issues/144)

### cdms2

 * ****: [cdms not using latest netcdf.](https://github.com/CDAT/cdms/issues/241)

### critical

 * ****: [Extreme CPU load ~3100% during variable read from netcdf](https://github.com/CDAT/cdms/issues/264)
 * ****: [OSX ESMF authentication](https://github.com/CDAT/cdms/issues/173)

### enhancement

 * ****: [Propagate errors with context management](https://github.com/CDAT/cdms/issues/161)
 * ****: [cdms2 (NetCDF) maximum dimension name length is 256](https://github.com/CDAT/cdms/issues/158)
 * ****: [cdms2 axis cannot have dictionary as attribute values](https://github.com/CDAT/cdms/issues/156)

### help wanted

 * ****: [cdms logo](https://github.com/CDAT/cdms/issues/207)

### question

 * ****: [Augment cdms2.createAxis to accept "missing" argument](https://github.com/CDAT/cdms/issues/220)

## Merged Pull Requests

 * [#72: Verify that MV2.mean() works properly](https://github.com/CDAT/cdms/pull/72)
 * [#74: Adds support for **kwargs to MV2 operation classes](https://github.com/CDAT/cdms/pull/74)
 * [#75: added script to log in myproxy, needed for opendap esgf](https://github.com/CDAT/cdms/pull/75)
 * [#76: Fix #7 NC_STRING Support.](https://github.com/CDAT/cdms/pull/76)
 * [#80: otherwise will push on every commit](https://github.com/CDAT/cdms/pull/80)
 * [#82: correct travis syntax](https://github.com/CDAT/cdms/pull/82)
 * [#83: Glib2 travis issue [WIP]](https://github.com/CDAT/cdms/pull/83)
 * [#84: missing_value = 'N/A' led to fail](https://github.com/CDAT/cdms/pull/84)
 * [#86: Issue32](https://github.com/CDAT/cdms/pull/86)
 * [#88: Adding badges in readme](https://github.com/CDAT/cdms/pull/88)
 * [#89: Issue78 strvar](https://github.com/CDAT/cdms/pull/89)
 * [#90: Fix #87 ESMF periodicity](https://github.com/CDAT/cdms/pull/90)
 * [#91: add test for conda-forge](https://github.com/CDAT/cdms/pull/91)
 * [#92: Circleci mac](https://github.com/CDAT/cdms/pull/92)
 * [#93: Condaforgetest](https://github.com/CDAT/cdms/pull/93)
 * [#95: Revert "Condaforgetest"](https://github.com/CDAT/cdms/pull/95)
 * [#96: Revert "add test for conda-forge"](https://github.com/CDAT/cdms/pull/96)
 * [#97: issue #4 a.mean() fixed!](https://github.com/CDAT/cdms/pull/97)
 * [#210: removing dropbox code from run_tests.py](https://github.com/CDAT/cdms/pull/210)
 * [#211: Fix cdscan using opendap](https://github.com/CDAT/cdms/pull/211)
 * [#212: change conda-build](https://github.com/CDAT/cdms/pull/212)
 * [#213: Cdms2](https://github.com/CDAT/cdms/pull/213)
 * [#222: Fixesmf](https://github.com/CDAT/cdms/pull/222)
 * [#223: Cdmsdocsmerge](https://github.com/CDAT/cdms/pull/223)
 * [#224: Fixesmf](https://github.com/CDAT/cdms/pull/224)
 * [#227: Issue#225](https://github.com/CDAT/cdms/pull/227)
 * [#230: Issue#225](https://github.com/CDAT/cdms/pull/230)
 * [#297: Docstanya](https://github.com/CDAT/cdms/pull/297)
 * [#298: Docstanya](https://github.com/CDAT/cdms/pull/298)
 * [#301: V3.1.0 1](https://github.com/CDAT/cdms/pull/301)
 * [#302: upload 3.7](https://github.com/CDAT/cdms/pull/302)
 * [#303: recompile liners on mac](https://github.com/CDAT/cdms/pull/303)

## Known Bugs

### Other

b" * [b'ESMF conservative blending when you have missing values'](b'https://github.com/CDAT/cdms/issues/231')"
b" * [b'netcdf string variables unable to be read'](b'https://github.com/CDAT/cdms/issues/78')"
b' * [b"cdms2 seg faults when using unknown \'+rw\' mode for opening a file"](b\'https://github.com/CDAT/cdms/issues/77\')'

 
# cdtime
 
## Closed Issues

### bug

 * ****: [On mac, py27, cdat8 and nightly fail when installed from cdat channels](https://github.com/CDAT/cdtime/issues/27)
 * ****: [mac nightlies seem broken](https://github.com/CDAT/cdtime/issues/26)
 * ****: [time comparisons](https://github.com/CDAT/cdtime/issues/18)

### enhancement

 * ****: [cdtime nightly not generated.](https://github.com/CDAT/cdtime/issues/12)

## Merged Pull Requests

 * [#13: Issue 10 exception](https://github.com/CDAT/cdtime/pull/13)
 * [#14: change conda_upload.sh to use variant in conda build](https://github.com/CDAT/cdtime/pull/14)
 * [#15: update conda-upload to use conda-build 3.2.2](https://github.com/CDAT/cdtime/pull/15)
 * [#36: V3.1.0 1](https://github.com/CDAT/cdtime/pull/36)
 * [#37: V3.1.2](https://github.com/CDAT/cdtime/pull/37)

## Known Bugs

No known issues!


<a name="8.0"></a>

# Releases Notes from Github Repos for: 8.0
 
# cdat
 
## Closed Issues

### Bug

 * **Bug**: [lambert azimuthal proj seem to ignore user custom parameters](https://github.com/CDAT/cdat/issues/2059)
 * **Bug**: [meshfill with missing values in mesh broken.](https://github.com/CDAT/cdat/issues/1730)
 * **Bug**: [BUG: vcs.Canvas.switchfonts() doesn't work](https://github.com/CDAT/cdat/issues/2118)
 * **Bug**: [cdms cannot read in all requested data on some climo files](https://github.com/CDAT/cdat/issues/2071)
 * **Bug**: [VCS/VTK warnings and UV-CDAT logo missing in pdf/ps output files](https://github.com/CDAT/cdat/issues/1583)
 * **Bug**: [PCMDI tools problem - lats](https://github.com/CDAT/cdat/issues/1949)
 * **Bug**: [Plot vector for sub-region: "datawc" for vector plot not working](https://github.com/CDAT/cdat/issues/2186)
 * **Bug**: [vtk seg fault on (my) ubuntu 15.10](https://github.com/CDAT/cdat/issues/1887)
 * **Bug**: [cdms2.getGrid()/setGrid() doesn't work](https://github.com/CDAT/cdat/issues/1707)
 * **Bug**: [mean broken on MV array](https://github.com/CDAT/cdat/issues/2088)
 * **Bug**: [projections still broken](https://github.com/CDAT/cdat/issues/1640)
 * **Bug**: [text alignment seems a bit off](https://github.com/CDAT/cdat/issues/2082)
 * **Bug**: [CDMS2/MV2.newaxis doesn't work](https://github.com/CDAT/cdat/issues/1722)
 * **Bug**: [canvas.png writes a PNG with labels off if bg=0](https://github.com/CDAT/cdat/issues/1740)
 * **Enhancement**: [numpy.NewAxis broken](https://github.com/CDAT/cdat/issues/1974)

### Build

 * **Enhancement**: [Build on OS X 10.11 (with XCode 7.x)](https://github.com/CDAT/cdat/issues/1655)

### Enhancement

 * **Enhancement**: [Suppress numpy warnings?](https://github.com/CDAT/cdat/issues/1580)
 * **Enhancement**: [Status of ESMPy in UV-CDAT ?](https://github.com/CDAT/cdat/issues/1954)

### VCS

 * ****: [Implement gettextextent](https://github.com/CDAT/cdat/issues/2052)
 * ****: [vcs.Gfb.rename() seems to destroy the object that it's renaming](https://github.com/CDAT/cdat/issues/2116)
 * ****: [Discuss usefulness of outlines in plots](https://github.com/CDAT/cdat/issues/1996)

### cdms2

 * ****: [cdsm2 createGenericGrid need to be generic](https://github.com/CDAT/cdat/issues/2081)

## Merged Pull Requests


## Known Bugs

### Other

 * [opendap](https://github.com/CDAT/cdat/issues/2166)
 * [DV3D/VCS plot error](https://github.com/CDAT/cdat/issues/1867)
 * [Unable to load Ensembles dimension from Grads Ctl file](https://github.com/CDAT/cdat/issues/1823)

 
# cdms
 
## Closed Issues

### Can't reproduce

 * ****: [Suppress numpy warnings?](https://github.com/CDAT/cdms/issues/48)

### bug

 * ****: [cdms2 file variable does not support var.ndim](https://github.com/CDAT/cdms/issues/191)
 * ****: [division on loading loses grid](https://github.com/CDAT/cdms/issues/190) ([#192](https://github.com/CDAT/cdms/pull/192))
 * ****: [Cdunif getAttribute returns incomplete value](https://github.com/CDAT/cdms/issues/166)
 * ****: [useNetCDF3 does not work ](https://github.com/CDAT/cdms/issues/180)
 * ****: [mac python 3 seems broken](https://github.com/CDAT/cdms/issues/184)
 * ****: [numpy.NewAxis broken](https://github.com/CDAT/cdms/issues/6)
 * ****: [esmf regridder fills in data where non should be](https://github.com/CDAT/cdms/issues/208)
 * ****: [cdscan path needs a patch](https://github.com/CDAT/cdms/issues/71)
 * ****: [Unicode strings for axis names](https://github.com/CDAT/cdms/issues/225)
 * ****: [regrid2 vertical regridder seems broken](https://github.com/CDAT/cdms/issues/15)
 * ****: [File open fails when lon and lat are variables (not dimensions)](https://github.com/CDAT/cdms/issues/32)
 * ****: [can't delete file attribute](https://github.com/CDAT/cdms/issues/50)

### cdms2

 * ****: [test_Esmf_3x4_6x8_Conserve_Masked failed on MacOS (py2 & py3)](https://github.com/CDAT/cdms/issues/226)
 * ****: [Add NC_String type for netCDF file attributes](https://github.com/CDAT/cdms/issues/7)
 * ****: [conda seems to only upload numpy 1.11](https://github.com/CDAT/cdms/issues/209)
 * ****: [python 3 remaining fail tests](https://github.com/CDAT/cdms/issues/165)
 * ****: [CDMS2 fails during init for netCDF variable of type unsigned byte](https://github.com/CDAT/cdms/issues/10)
 * ****: [not all types are written correctly or even written](https://github.com/CDAT/cdms/issues/14)

### critical

 * ****: [cdms should report more details to anonymous usage sfotware](https://github.com/CDAT/cdms/issues/123)

### enhancement

 * ****: [osx now in nesii/label/dev-emsf](https://github.com/CDAT/cdms/issues/214)
 * ****: [remove libcf?](https://github.com/CDAT/cdms/issues/1)
 * ****: [data not tagged with lat , long](https://github.com/CDAT/cdms/issues/170)
 * ****: [cdms2 can only open cdscanned http files from the directory the file is at](https://github.com/CDAT/cdms/issues/51)
 * ****: [Building/testing modifies source tree](https://github.com/CDAT/cdms/issues/52)

### help wanted

 * ****: [CDMS2 2.12 wrongly scaling variable](https://github.com/CDAT/cdms/issues/174)

## Merged Pull Requests


## Known Bugs

### Other

 * [ESMF conservative blending when you have missing values](https://github.com/CDAT/cdms/issues/231)
 * [Can 2.8.0 still create netCDF3 Classic ?](https://github.com/CDAT/cdms/issues/99)
 * [cdms2.setAutoBounds('off') problem (OK with 'on')](https://github.com/CDAT/cdms/issues/98)
 * [netcdf string variables unable to be read](https://github.com/CDAT/cdms/issues/78)
 * [cdms2 seg faults when using unknown '+rw' mode for opening a file](https://github.com/CDAT/cdms/issues/77)

 
# vcs
 
## Closed Issues

### bug

 * ****: [taylordiagram . line_color should accept strings](https://github.com/CDAT/vcs/issues/218)
 * ****: [vcs gettextextent broken](https://github.com/CDAT/vcs/issues/277)
 * ****: [template.scalefont creates never removed textorientation object](https://github.com/CDAT/vcs/issues/235)
 * ****: [Coordinates displayed in interactive mode are not good (2.12 and earlier)](https://github.com/CDAT/vcs/issues/251)
 * ****: [fillarea creates black area](https://github.com/CDAT/vcs/issues/254)
 * ****: [meshfill wrap seems broken](https://github.com/CDAT/vcs/issues/323)
 * ****: [GetMaxNorm error when available vector data area is 'smaller' than vector graphics method?](https://github.com/CDAT/vcs/issues/184)
 * ****: [tayore diagrams std label always centered on template.datawc but should be centered on actual quadrans length](https://github.com/CDAT/vcs/issues/283)
 * ****: [vcs init seems to fail using ${HOME} correctly](https://github.com/CDAT/vcs/issues/145)

### enhancement

 * ****: [Print a helpful warning when using x.plot and DISPLAY is not set](https://github.com/CDAT/vcs/issues/211)
 * ****: [need a function to get the exact box around text not just bounding box](https://github.com/CDAT/vcs/issues/278)
 * ****: [Idea for canvas reinitialization: x.reinit()](https://github.com/CDAT/vcs/issues/275)
 * ****: [vcs.removeobject doex NOT error exit if trying to remove a non vcs object](https://github.com/CDAT/vcs/issues/234)
 * ****: [taylordiagram should be able to draw ids only in legend not on plot](https://github.com/CDAT/vcs/issues/222)
 * ****: [drawMarker and legend cannot not draw a line.](https://github.com/CDAT/vcs/issues/289)
 * ****: [taylor diagrams lack control of "standard deviation" label](https://github.com/CDAT/vcs/issues/282)
 * ****: [unexpected warning message.](https://github.com/CDAT/vcs/issues/309)
 * ****: [Remarks about vcs.download_sample_data_files](https://github.com/CDAT/vcs/issues/143)
 * ****: [Building/testing modifies source tree](https://github.com/CDAT/vcs/issues/301)
 * ****: [streamlines ](https://github.com/CDAT/vcs/issues/269)
 * ****: [we should be able to stop font scaling at some number for the drawLinesandMarkers](https://github.com/CDAT/vcs/issues/291)

### invalid

 * ****: [1d flip with only 1 axes seems broken](https://github.com/CDAT/vcs/issues/313)
 * ****: [x.plot(s,box) error](https://github.com/CDAT/vcs/issues/256)

## Merged Pull Requests


## Known Bugs

### Other

 * [3d broken?](https://github.com/CDAT/vcs/issues/318)
 * [axisconvert works only for "linear"](https://github.com/CDAT/vcs/issues/312)
 * [text disappear in png with bg=False](https://github.com/CDAT/vcs/issues/308)
 * [Black png returned when using a vnc session](https://github.com/CDAT/vcs/issues/117)

 
# cdutil
 
## Closed Issues

### bug

 * ****: [cdutil.generateLandSeaMask returns missing values in maks](https://github.com/CDAT/cdutil/issues/18) ([#19](https://github.com/CDAT/cdutil/pull/19))

## Merged Pull Requests


## Known Bugs

No known issues!
 
# genutil
 
## Closed Issues

### enhancement

 * ****: [FutureWarning in genutil.minmax (uvcdat 2.12)](https://github.com/CDAT/genutil/issues/14)

## Merged Pull Requests


## Known Bugs

No known issues!
 
# vcsaddons
 
## Closed Issues

### bug

 * ****: [polar list does not list all objects](https://github.com/CDAT/vcsaddons/issues/11)
 * ****: [polar magnitude_tick_angle does not respect theata_offset](https://github.com/CDAT/vcsaddons/issues/13)
 * ****: [polar plots seems to stack points with magnitude greater than max required at the edge of the plot](https://github.com/CDAT/vcsaddons/issues/9)
 * ****: [polar plots crashes if a value is less than thre minmum magnitude](https://github.com/CDAT/vcsaddons/issues/8)

### enhancement

 * ****: [polar should have a __slot__ to prevent setting bad attributes](https://github.com/CDAT/vcsaddons/issues/12)

## Merged Pull Requests


## Known Bugs

No known issues!
 
# cdtime
 
## Closed Issues

### bug

 * ****: [cdtime issue exception that seem to have no base class (python2 maybe 3)](https://github.com/CDAT/cdtime/issues/10)

### invalid

 * ****: [latest cdtime broken on py3](https://github.com/CDAT/cdtime/issues/16)

## Merged Pull Requests


## Known Bugs

No known issues!


<a name="2.12"></a>
# Releases Notes from Github Repos for Milestone: 2.12
 
# uvcdat
 
## Closed Issues

### Bug

 * **Bug**: [vcs.plot(iso) creates text object that are not removed after clear](https://github.com/CDAT/uvcdat/issues/1424)

### Enhancement

 * **Enhancement**: [logger should cache records until server acknowledge success](https://github.com/CDAT/uvcdat/issues/2172)
 * **Enhancement**: [submitPing should cache datsa in case server is dead](https://github.com/CDAT/uvcdat/issues/2174)

## Merged Pull Requests


## Known Bugs

### Other

 * [(python:26831): Gtk-WARNING **: Unable to find default local directory monitor type](https://github.com/CDAT/uvcdat/issues/2006)
 * [DV3D/VCS plot error](https://github.com/CDAT/uvcdat/issues/1867)

 
# cdms
 
## Closed Issues

### bug

 * ****: [Undefined local variable with regrid2.crossSection.get_latitude_wts_bnds](https://github.com/CDAT/cdms/issues/153) ([#154](https://github.com/CDAT/cdms/pull/154))
 * ****: [crossRegrid does not return an MV2](https://github.com/CDAT/cdms/issues/155)
 * ****: [nc4 classic file can't be edited](https://github.com/CDAT/cdms/issues/144)
 * ****: [netCDF4 file not readable by cdms2](https://github.com/CDAT/cdms/issues/149) ([#150](https://github.com/CDAT/cdms/pull/150))

## Merged Pull Requests

 * [#142: add mask to transient variable](https://github.com/CDAT/cdms/pull/142)

## Known Bugs

### Other

 * [cdscan path needs a patch](https://github.com/CDAT/cdms/issues/71)

 
# vcs
 
## Closed Issues

### bug

 * ****: [taylordiagram markers copied over from default andaffect default](https://github.com/CDAT/vcs/issues/216)
 * ****: [taylordiagram won't plot in jupyter](https://github.com/CDAT/vcs/issues/215)
 * ****: [taylordiagram drawing line between markers broken (clor)](https://github.com/CDAT/vcs/issues/219)
 * ****: [Catastrophic 2.8 and 2.10 x.plot failure on our new CentOS 7 server](https://github.com/CDAT/vcs/issues/230)
 * ****: [pngs do not clear object properly in some cases](https://github.com/CDAT/vcs/issues/203)
 * ****: [template.scalefont broken](https://github.com/CDAT/vcs/issues/205) ([#207](https://github.com/CDAT/vcs/pull/207))
 * ****: [3d_scalar seg faults on mac](https://github.com/CDAT/vcs/issues/245)
 * ****: [taylordiagram adds an extra marker if marker attributes set manually](https://github.com/CDAT/vcs/issues/223)

### enhancement

 * ****: [Color maps could look better](https://github.com/CDAT/vcs/issues/238) ([#244](https://github.com/CDAT/vcs/pull/244))
 * ****: [drawLinesAndTemplate could use new functionalities](https://github.com/CDAT/vcs/issues/224)
 * ****: [taylordiagram should draw legend](https://github.com/CDAT/vcs/issues/221)

### invalid

 * ****: [isof.fillareacolors does not like rgb tuple in list of colors](https://github.com/CDAT/vcs/issues/206)

## Merged Pull Requests


## Known Bugs

### Other

 * [Colormap for difference or anomaly field needs adjustment](https://github.com/CDAT/vcs/issues/246)

Unable to find milestone 2.12
 
# cdat_info
 
## Closed Issues

### enhancement

 * ****: [need to turn off logging](https://github.com/CDAT/cdat_info/issues/2)
 * ****: [Need mecanism to track cdat packages installed and othe rprovenance](https://github.com/CDAT/cdat_info/issues/4) ([#5](https://github.com/CDAT/cdat_info/pull/5))

## Merged Pull Requests


## Known Bugs

No known issues!
Unable to find milestone 2.12

<a name="2.10"></a>

# Releases Notes from Github Repos for Milestone: 2.10
 
# uvcdat
 
## Closed Issues

### Bug

 * **Bug**: [Conda install failing on OS X](https://github.com/CDAT/uvcdat/issues/2138)

### Enhancement

 * **Enhancement**: [ask anonymous should periodically ask again in case it's no](https://github.com/CDAT/uvcdat/issues/2178)
 * **Enhancement**: [Rebuild all packages with conda >= 2.0?](https://github.com/CDAT/uvcdat/issues/2171)
 * **Enhancement**: [cdat_info has debug print statement](https://github.com/CDAT/uvcdat/issues/2169)

## Merged Pull Requests


## Known Bugs

### Other

 * [cdms2.open fails on an xml file with "invalid" attributes](https://github.com/CDAT/uvcdat/issues/1942)
 * [ctest does not seem to post to cdash anymore](https://github.com/CDAT/uvcdat/issues/1929)
 * [vtk seg fault on (my) ubuntu 15.10](https://github.com/CDAT/uvcdat/issues/1887)
 * [DV3D/VCS plot error](https://github.com/CDAT/uvcdat/issues/1867)
 * [Unable to load Ensembles dimension from Grads Ctl file](https://github.com/CDAT/uvcdat/issues/1823)
 * [dv3d cannot go back into interact mode](https://github.com/CDAT/uvcdat/issues/1295)
 * [dv3d plotting ad changing attributes breaks dv3d](https://github.com/CDAT/uvcdat/issues/1286)
 * [Fix setup_runtime.sh script for DMG](https://github.com/CDAT/uvcdat/issues/409)
 
# cdms
 
## Closed Issues

### bug

 * ****: [cdutil.ANNUALCYCLE.departures lopping off the final month](https://github.com/CDAT/cdms/issues/36)
 * ****: [https dap broken](https://github.com/CDAT/cdms/issues/135)
 * ****: [ESMF linear regridding fails with periodic data](https://github.com/CDAT/cdms/issues/87)
 * ****: [test_fillvalue.py failed](https://github.com/CDAT/cdms/issues/29)
 * ****: [cdsm2 createGenericGrid need to be generic](https://github.com/CDAT/cdms/issues/5)
 * ****: [mean broken on MV array](https://github.com/CDAT/cdms/issues/4)
 * ****: [No boundary data error](https://github.com/CDAT/cdms/issues/108)
 * ****: [weird cdscan error](https://github.com/CDAT/cdms/issues/70)
 * ****: [implement context management with the `with` keyword ](https://github.com/CDAT/cdms/issues/94)
 * ****: [netcdf string variables unable to be read](https://github.com/CDAT/cdms/issues/78)
 * ****: [missing_value attribute in file not respected when reading in](https://github.com/CDAT/cdms/issues/18)

### critical

 * ****: [Update cdms2 to deal with all common datatypes (uint8, uint16, char, str etc)](https://github.com/CDAT/cdms/issues/63)
 * ****: [Upgrade ESMP to ESMpy](https://github.com/CDAT/cdms/issues/57)

### enhancement

 * ****: [flake8 / pep8 cdms2](https://github.com/CDAT/cdms/issues/133)
 * ****: [Warning from numpy1.9.0 in ESMP_API.py and avariable.py](https://github.com/CDAT/cdms/issues/62)
 * ****: [periodicity warnings](https://github.com/CDAT/cdms/issues/126)
 * ****: [uvcdat conda channel highest cdms2 version is 2.8.1.](https://github.com/CDAT/cdms/issues/128)
 * ****: [PET0.ESMF_LogFile should be turned off](https://github.com/CDAT/cdms/issues/106)
 * ****: [Docstrings](https://github.com/CDAT/cdms/issues/13)
 * ****: [Update numpy to 1.10](https://github.com/CDAT/cdms/issues/59)
 * ****: [MaskedArrayFutureWarning Numpy 1.11 - does this require some cdms tweaks?](https://github.com/CDAT/cdms/issues/122)

## Merged Pull Requests

 * [#134: fix https reading issue](https://github.com/CDAT/cdms/pull/134)

## Known Bugs

### Other

 * [variable loses mask after applying crossSectionRegrid](https://github.com/CDAT/cdms/issues/138)
 * [cdms2 seg faults when using unknown '+rw' mode for opening a file](https://github.com/CDAT/cdms/issues/77)
 * [cdscan path needs a patch](https://github.com/CDAT/cdms/issues/71)

 
# vcs
 
## Closed Issues

### bug

 * ****: [Portrait plot issues](https://github.com/CDAT/vcs/issues/146)
 * ****: [vcs does not respect geometry on newer mac XCode 8.3](https://github.com/CDAT/vcs/issues/147)
 * ****: [VCS/VTK warnings and UV-CDAT logo missing in pdf/ps output files](https://github.com/CDAT/vcs/issues/76)
 * ****: [Text location changes with `textAsPaths` setting](https://github.com/CDAT/vcs/issues/150)
 * ****: [text alignment seems a bit off](https://github.com/CDAT/vcs/issues/47)
 * ****: [gettextextent broken?](https://github.com/CDAT/vcs/issues/15)
 * ****: [boxfill missing value does not respect opacity](https://github.com/CDAT/vcs/issues/121)
 * ****: [vcs.Gfb.rename() seems to destroy the object that it's renaming](https://github.com/CDAT/vcs/issues/2)
 * ****: [If masking reduces the bounds of a dataset, plots look incomplete.](https://github.com/CDAT/vcs/issues/26)
 * ****: [isofill broken](https://github.com/CDAT/vcs/issues/5)
 * ****: [doc strings PR introduced bug in test suite](https://github.com/CDAT/vcs/issues/136)
 * ****: [meshfill broken](https://github.com/CDAT/vcs/issues/135)
 * ****: [canvas.png writes a PNG with labels off if bg=0](https://github.com/CDAT/vcs/issues/70)
 * ****: ['.py' extension on script functions not working](https://github.com/CDAT/vcs/issues/103)

### enhancement

 * ****: [VCS PDF filesize is much larger than what you would get from MPL](https://github.com/CDAT/vcs/issues/33)
 * ****: [Multiple parallel coordinates (y-axis) on single plot](https://github.com/CDAT/vcs/issues/11)
 * ****: [x.show('crap') could return a sorted list of valid options](https://github.com/CDAT/vcs/issues/139)

## Merged Pull Requests


## Known Bugs

### Other

 * [vcs window do not disappear](https://github.com/CDAT/vcs/issues/192)
 * [vcs init seems to fail using ${HOME} correctly](https://github.com/CDAT/vcs/issues/145)
 * [Black png returned when using a vnc session](https://github.com/CDAT/vcs/issues/117)
 * [vcs seg fault on ubuntu 16.04 using regular not nox vtk ](https://github.com/CDAT/vcs/issues/116)

 
# cdutil
 
## Closed Issues

### bug

 * ****: [cdutil.region.domain: variable loses unit attribute](https://github.com/CDAT/cdutil/issues/9)
 * ****: [Weight problems in cdutil.ANNUALCYCLE.climatology (daily data)](https://github.com/CDAT/cdutil/issues/4)

### enhancement

 * ****: [Docstrings](https://github.com/CDAT/cdutil/issues/1)

## Merged Pull Requests


## Known Bugs

# 2.8 Release Notes

## VCS:

 - [Fix export svg](https://github.com/CDAT/uvcdat/pull/2058)
 - [Add test for BUG #26: If masking reduces the bounds of a dataset, plots look incomplete. ](https://github.com/CDAT/uvcdat/pull/2134)
 - [utils.generate_time_labels(), wrong conversion to seconds?](https://github.com/CDAT/uvcdat/pull/2068)
 - [x.plot(s,bg=bg) does not output image](https://github.com/CDAT/uvcdat/pull/2137)
 - [Proposed new color names](https://github.com/CDAT/uvcdat/pull/2065)
 - [Legend offset new attribute](https://github.com/CDAT/uvcdat/pull/2069)
 - [System dependent outline](https://github.com/CDAT/uvcdat/pull/2070)
 - [Fix spaces flake8](https://github.com/CDAT/uvcdat/pull/2064)
 - [Fix bug with orthographic projection](https://github.com/CDAT/uvcdat/pull/2086)
 - [Fix for template name collision bug.](https://github.com/CDAT/uvcdat/pull/2087)
 - [corrected initil.attributes](https://github.com/CDAT/uvcdat/pull/2091)
 - [Fix flake8](https://github.com/CDAT/uvcdat/pull/2094)
 - [remove default parameter assignment on getcolors. Fixes #2097.](https://github.com/CDAT/uvcdat/pull/2098)
 - [BUG #1265: Fix datawc zoom-in for geographic projections.](https://github.com/CDAT/uvcdat/pull/2102)
 - [Viridis latest](https://github.com/CDAT/uvcdat/pull/2105)
 - [Remove trailing whitespace from utils.py](https://github.com/CDAT/uvcdat/pull/2111)
 - [All vcs docstrings updated merged](https://github.com/CDAT/uvcdat/pull/2117)
 - [fixes #2118](https://github.com/CDAT/uvcdat/pull/2120)
 - [Split repos](https://github.com/CDAT/uvcdat/pull/2123)
 - [Additional test for BUG #5: vtkPolyData::RemoveDeletedCells does not …](https://github.com/CDAT/uvcdat/pull/2124)
 - [Fix test suite vcs imports](https://github.com/CDAT/uvcdat/pull/2126)
 - [Improve put png](https://github.com/CDAT/uvcdat/pull/2127)
 - [Added test for drawLenged](https://github.com/CDAT/uvcdat/pull/2130)
 - [Docstring cleanup](https://github.com/CDAT/uvcdat/pull/2056)
 - [Docstring cleanup](https://github.com/CDAT/uvcdat/pull/2057)
 - [Adds support for gettextextent()](https://github.com/CDAT/uvcdat/pull/2053)
 - [BUG #1770: Display meshfill template elements through renderTemplate.](https://github.com/CDAT/uvcdat/pull/2049)
 - [BUG #1944: Rename line to linetype for isoline, unified1d and vector.](https://github.com/CDAT/uvcdat/pull/2046)
 - [allows user to set default range to use when calling getcolors](https://github.com/CDAT/vcs/pull/1)
 - [Fixes #2, Gfb.rename().](https://github.com/CDAT/vcs/pull/4)
 - [Fixes to queries.py documentation](https://github.com/CDAT/vcs/pull/7)
 - [Split repos](https://github.com/CDAT/vcs/pull/8)
 - [Revert "BUG #1265: Fix datawc zoom-in for geographic projections."](https://github.com/CDAT/vcs/pull/9)
 - [Fix isofill levels](https://github.com/CDAT/vcs/pull/10)
 - [Improve put png](https://github.com/CDAT/vcs/pull/12)
 - [VCS API Doc](https://github.com/CDAT/vcs/pull/16)
 - [Parallel coord](https://github.com/CDAT/vcs/pull/17)
 - [Documentation](https://github.com/CDAT/vcs/pull/20)
 - [Fix PEP8 convention issues with VTKPlots](https://github.com/CDAT/vcs/pull/24)
 - [Pcoords](https://github.com/CDAT/vcs/pull/25)
 - [BUG #26: If masking reduces the bounds of a dataset, plots look incomplete](https://github.com/CDAT/vcs/pull/27)
 - [patch : png compression level option from user](https://github.com/CDAT/vcs/pull/28)
 - [fixed flake8](https://github.com/CDAT/vcs/pull/30)

## CDMS:

 - [fix issue where cyclical would fail for non numerical axes](https://github.com/CDAT/cdms/pull/2)
 - [Numpy1 11](https://github.com/CDAT/cdms/pull/8)
 - [add docs](https://github.com/CDAT/cdms/pull/9)
 - [Adds basic .gitignore](https://github.com/CDAT/cdms/pull/11)
 - [Tests!](https://github.com/CDAT/cdms/pull/12)
 - [Np11](https://github.com/CDAT/cdms/pull/20)
 - [add UVCDAT testing](https://github.com/CDAT/cdms/pull/22)
 - [Ken drs file](https://github.com/CDAT/cdms/pull/24)
 - [Fixmasterpush](https://github.com/CDAT/cdms/pull/25)
 - [Np11](https://github.com/CDAT/uvcdat/pull/2136)
 - [got it to look into cdms repo to add tests](https://github.com/CDAT/uvcdat/pull/2133)

## VCSAddons:

 - [added possibility to scratch text next to markes in legend functions](https://github.com/CDAT/vcsaddons/pull/3)
 - [Parallel coord](https://github.com/CDAT/vcsaddons/pull/2)

## Build:

 - [need to pass -b to build cdat_info out of source](https://github.com/CDAT/uvcdat/pull/2051)


## UV-CDAT GUI:

 - Fixed issue where files were not caching properly due to use of URI and path
 - Fixed single color handling for all graphics methods, added color picker widget for linecolor/markercolor on 1ds
 - Fixed some issues with how dimensions were handled
 - Fixed bug where deselecting a vcs cell would raise an exception
 - Redesigned how time slider stuff is handled, severely improved code quality
 - Fixed lack of plotting due to missing now having list values instead of int


<a name="2.6"></a>

# 2.6 Changelog

## Closed Issues

### Build

 * **Enhancement**: [update bUILD_MODE instructions](https://github.com/CDAT/uvcdat/issues/1455)
 * **Bug**: [CMake build issue on travis](https://github.com/CDAT/uvcdat/issues/1839)
 * **Bug**: [Issue with setup_runtime.csh](https://github.com/CDAT/uvcdat/issues/1920)
 * **Bug**: [GEOS5_sample.nc not copied to correct sample_data directory for OSX](https://github.com/CDAT/uvcdat/issues/1581)
 * **Bug**: [make -j8 seems to sometimes disable matplotlib](https://github.com/CDAT/uvcdat/issues/1913)
 * **Bug**: [Parallel build causing problems with egg installs overwriting easy-install.pth](https://github.com/CDAT/uvcdat/issues/1817)

### Test Suite

 * **Enhancement**: [uvcdat testing checks too many images](https://github.com/CDAT/uvcdat/issues/1854) ([#1943](https://github.com/CDAT/uvcdat/pull/1943))

### VCS

 * **Bug**: [isofill vcs bug](https://github.com/CDAT/uvcdat/issues/1947) ([#2027](https://github.com/CDAT/uvcdat/pull/2027))
 * **Bug**: [ratio="autot" fails to correctly generate the initial ratio](https://github.com/CDAT/uvcdat/issues/1795)
 * **Bug**: [bad contouring algorithm](https://github.com/CDAT/uvcdat/issues/1959)
 * **Bug**: [autot tests seem to fail from master](https://github.com/CDAT/uvcdat/issues/1930)
 * **Bug**: [animation save does not preserve the colormap](https://github.com/CDAT/uvcdat/issues/1845) ([#2028](https://github.com/CDAT/uvcdat/pull/2028))
 * **Bug**: [Boxfill legend incorrect when there are fewer colors than levels](https://github.com/CDAT/uvcdat/issues/1894) ([#1895](https://github.com/CDAT/uvcdat/pull/1895))
 * **Enhancement**: [Enable postscript export to write text objects in addition to text as paths (shapes)](https://github.com/CDAT/uvcdat/issues/1537)

### VTK

 * **Bug**: [vtk has hard links that seem to prevent anaconda libraries relocation](https://github.com/CDAT/uvcdat/issues/1960)

### cdutil/genutil

 * **Bug**: [genutil broken in nightly](https://github.com/CDAT/uvcdat/issues/2035)

## Merged Pull Requests

 * [#1756: Enforce CMake minimum version 2.8.12](https://github.com/CDAT/uvcdat/pull/1756)
 * [#1932: 2.4.1rc test](https://github.com/CDAT/uvcdat/pull/1932)
 * [#1933: merging master into release](https://github.com/CDAT/uvcdat/pull/1933)
 * [#1934: Release](https://github.com/CDAT/uvcdat/pull/1934)
 * [#1941: Allow unicode strings for subsetting.](https://github.com/CDAT/uvcdat/pull/1941)
 * [#1945: Update README.md](https://github.com/CDAT/uvcdat/pull/1945)
 * [#1951: Cdat web plot subsetting](https://github.com/CDAT/uvcdat/pull/1951)
 * [#1952: Cdscan importable](https://github.com/CDAT/uvcdat/pull/1952)
 * [#1956: Fix continents=0](https://github.com/CDAT/uvcdat/pull/1956)
 * [#1966: Click info point dataset](https://github.com/CDAT/uvcdat/pull/1966)
 * [#1967: Reenable autot_axis tests. Keep max Y to 500.](https://github.com/CDAT/uvcdat/pull/1967)
 * [#1968: Improve testing by moving common code to testing module](https://github.com/CDAT/uvcdat/pull/1968)
 * [#1970: Marked export to gs as no longer supported](https://github.com/CDAT/uvcdat/pull/1970)
 * [#1978: Vcs fix geometry instantiation](https://github.com/CDAT/uvcdat/pull/1978)
 * [#1983: BUG: Fix memory override for vtkContourFiler in isofillpipeline.](https://github.com/CDAT/uvcdat/pull/1983)
 * [#1987: updated crypto to latest version so it builds on Ubuntu 16](https://github.com/CDAT/uvcdat/pull/1987)
 * [#1988: Compute vector scaling correctly](https://github.com/CDAT/uvcdat/pull/1988)
 * [#1989: Fix flake8 warnings and a test generated file](https://github.com/CDAT/uvcdat/pull/1989)
 * [#1990: Orthographic](https://github.com/CDAT/uvcdat/pull/1990)
 * [#1991: Added missing graphics method types to creategraphicsmethod](https://github.com/CDAT/uvcdat/pull/1991)
 * [#1992: Added option to export text as object or path](https://github.com/CDAT/uvcdat/pull/1992)
 * [#2000: Fix regression for test_vcs_png_window_resize](https://github.com/CDAT/uvcdat/pull/2000)
 * [#2001: BUG: Use the geometry argument, if available, for background tests](https://github.com/CDAT/uvcdat/pull/2001)
 * [#2003: Fixes failing DV3D tests and VCS behavior](https://github.com/CDAT/uvcdat/pull/2003)
 * [#2005: BUG: Extend the isoline attribute list with the last value from the e...](https://github.com/CDAT/uvcdat/pull/2005)
 * [#2007: BUG: datawc does not work on a time axis.](https://github.com/CDAT/uvcdat/pull/2007)
 * [#2012: Part-1 of improved RST docs for VCS](https://github.com/CDAT/uvcdat/pull/2012)
 * [#2013: Updated cmake to use new location for legal and readme](https://github.com/CDAT/uvcdat/pull/2013)
 * [#2015: Conda build](https://github.com/CDAT/uvcdat/pull/2015)
 * [#2017: Fixed extends not working if you have a premade list for custom.](https://github.com/CDAT/uvcdat/pull/2017)
 * [#2025: Vcsaddons histo polar](https://github.com/CDAT/uvcdat/pull/2025)
 * [#2029: Cmake find activate](https://github.com/CDAT/uvcdat/pull/2029)
 * [#2030: Vtk update leak](https://github.com/CDAT/uvcdat/pull/2030)
 * [#2032: needed to duplicate yr fully in case the year starts in October for e...](https://github.com/CDAT/uvcdat/pull/2032)
 * [#2036: Generated png should have same name with baseline](https://github.com/CDAT/uvcdat/pull/2036)
 * [#2037: Fix wrong tuple instance condition for axis getitem call](https://github.com/CDAT/uvcdat/pull/2037)

## Known Bugs

### Other

 * [(python:26831): Gtk-WARNING **: Unable to find default local directory monitor type](https://github.com/CDAT/uvcdat/issues/2006)
 * [Conda channel nightly updates not up-to-date](https://github.com/CDAT/uvcdat/issues/1997)
 * [numpy.NewAxis broken](https://github.com/CDAT/uvcdat/issues/1974)
 * [cdms2.open fails on an xml file with "invalid" attributes](https://github.com/CDAT/uvcdat/issues/1942)
 * [ctest does not seem to post to cdash anymore](https://github.com/CDAT/uvcdat/issues/1929)
 * [vtk seg fault on (my) ubuntu 15.10](https://github.com/CDAT/uvcdat/issues/1887)
 * [DV3D/VCS plot error](https://github.com/CDAT/uvcdat/issues/1867)
 * [Unable to load Ensembles dimension from Grads Ctl file](https://github.com/CDAT/uvcdat/issues/1823)


<a name="2.4.1"></a>

# 2.4.1 Changelog

## Closed Issues

### Build

 * **Bug**: [vcs import error](https://github.com/CDAT/uvcdat/issues/1914)
 * **Enhancement**: [Update eofs to 1.1.0](https://github.com/CDAT/uvcdat/issues/1910) ([#1911](https://github.com/CDAT/uvcdat/pull/1911))

### VCS

 * **Bug**: [`missing` color does not support all of the new color syntaxes.](https://github.com/CDAT/uvcdat/issues/1825) ([#1831](https://github.com/CDAT/uvcdat/pull/1831))
 * **Bug**: [Custom continents don't work](https://github.com/CDAT/uvcdat/issues/1826) ([#1828](https://github.com/CDAT/uvcdat/pull/1828))
 * **Enhancement**: [wide screen](https://github.com/CDAT/uvcdat/issues/1822)

### cdms2

 * **Bug**: [cdms2 seg fault on some weird types](https://github.com/CDAT/uvcdat/issues/1857) ([#1915](https://github.com/CDAT/uvcdat/pull/1915))

## Merged Pull Requests

 * [#1729: Ocgis](https://github.com/CDAT/uvcdat/pull/1729)
 * [#1752: several tweaks, mainly saving method results for re-use, to improve](https://github.com/CDAT/uvcdat/pull/1752)
 * [#1797: Adding a vagrant configuration for building with a GUI](https://github.com/CDAT/uvcdat/pull/1797)
 * [#1802: Update readme master](https://github.com/CDAT/uvcdat/pull/1802)
 * [#1803: Remove repo size](https://github.com/CDAT/uvcdat/pull/1803)
 * [#1806: Fit to viewport cleanup](https://github.com/CDAT/uvcdat/pull/1806)
 * [#1810: Uvcmetrics devel](https://github.com/CDAT/uvcdat/pull/1810)
 * [#1815: Issue1798 durack1 update matplotlib 1.5.0 to 1.5.1](https://github.com/CDAT/uvcdat/pull/1815)
 * [#1816: Issue1799 durack1 update scipy 0.16.1 to 0.17.0](https://github.com/CDAT/uvcdat/pull/1816)
 * [#1820: Issue 1801 old scr files](https://github.com/CDAT/uvcdat/pull/1820)
 * [#1821: On my computer with 2 very wide screens init default was super big](https://github.com/CDAT/uvcdat/pull/1821)
 * [#1827: Update vtk proj4 9 2](https://github.com/CDAT/uvcdat/pull/1827)
 * [#1829: BUG #1809: Error wrapping a curved grid with masking.](https://github.com/CDAT/uvcdat/pull/1829)
 * [#1830: Add test for BUG # 1728: wrapping data creates long cells](https://github.com/CDAT/uvcdat/pull/1830)
 * [#1841: Add nc_del_attr to Cdunif to allow attribute removal in netCDF files](https://github.com/CDAT/uvcdat/pull/1841)
 * [#1847: Fix macos inconsistency](https://github.com/CDAT/uvcdat/pull/1847)
 * [#1855: BUG #1849: Re-enable datawc for linear projection.](https://github.com/CDAT/uvcdat/pull/1855)
 * [#1862: BUG #1740: plotting with bg=0 produces labels off](https://github.com/CDAT/uvcdat/pull/1862)
 * [#1870: Mintics now properly support lists](https://github.com/CDAT/uvcdat/pull/1870)
 * [#1874: uri starting with file:// were not interpreted correctly](https://github.com/CDAT/uvcdat/pull/1874)
 * [#1875: Pcmdi only tools](https://github.com/CDAT/uvcdat/pull/1875)
 * [#1878: BUG #1811: Show point information for plots using geographic projecti...](https://github.com/CDAT/uvcdat/pull/1878)
 * [#1891: Revert "issue1539 durack1 update iPython 3.0.0 to 4.1.2"](https://github.com/CDAT/uvcdat/pull/1891)
 * [#1896: ENH: ratio=autot works for geographic projected datasets](https://github.com/CDAT/uvcdat/pull/1896)
 * [#1902: Build vcs without .egg by default](https://github.com/CDAT/uvcdat/pull/1902)
 * [#1904: BUG #1886: Polar projection does not change pole.](https://github.com/CDAT/uvcdat/pull/1904)
 * [#1908: Cleanup for conda and setuptools](https://github.com/CDAT/uvcdat/pull/1908)
 * [#1917: Fixed inconsistent test names and other related issues](https://github.com/CDAT/uvcdat/pull/1917)
 * [#1918: Added missing test file](https://github.com/CDAT/uvcdat/pull/1918)
 * [#1928: Allow canvas.plot to handle vcs addons](https://github.com/CDAT/uvcdat/pull/1928)
 * [#1932: 2.4.1rc test](https://github.com/CDAT/uvcdat/pull/1932)
 * [#1933: merging master into release](https://github.com/CDAT/uvcdat/pull/1933)
 * [#1934: Release](https://github.com/CDAT/uvcdat/pull/1934)

## Known Bugs

### Other

 * [running autot_title with setbgoutputdimensions leads to seg fault](https://github.com/CDAT/uvcdat/issues/1931)
 * [autot tests seem to fail from master](https://github.com/CDAT/uvcdat/issues/1930)
 * [ctest does not seem to post to cdash anymore](https://github.com/CDAT/uvcdat/issues/1929)
 * [make -j8 seems to sometimes disable matplotlib](https://github.com/CDAT/uvcdat/issues/1913)
 * [Boxfill legend incorrect when there are fewer colors than levels](https://github.com/CDAT/uvcdat/issues/1894)
 * [vtk seg fault on (my) ubuntu 15.10](https://github.com/CDAT/uvcdat/issues/1887)
 * [DV3D/VCS plot error](https://github.com/CDAT/uvcdat/issues/1867)
 * [animation save does not preserve the colormap](https://github.com/CDAT/uvcdat/issues/1845)
 * [CMake build issue on travis](https://github.com/CDAT/uvcdat/issues/1839)
 * [Unable to load Ensembles dimension from Grads Ctl file](https://github.com/CDAT/uvcdat/issues/1823)
 * [Parallel build causing problems with egg installs overwriting easy-install.pth](https://github.com/CDAT/uvcdat/issues/1817)
 * [ratio="autot" fails to correctly generate the initial ratio](https://github.com/CDAT/uvcdat/issues/1795)
 * [Meshfill leaves extra display plots lying around](https://github.com/CDAT/uvcdat/issues/1770)


<a name="2.4"></a>

# 2.4 Changelog

[New Features Documentation](/releases/2.4_features.html)

## Closed Issues

### ACME

 * **Bug**: [average() indentation error](https://github.com/CDAT/uvcdat/issues/1048)

### Build

 * **Bug**: [sample data doesn't get re-downloaded if it's deleted](https://github.com/CDAT/uvcdat/issues/133)
 * **Bug**: ["This warning is for project developers" message during ccmake?](https://github.com/CDAT/uvcdat/issues/462)
 * **Bug**: [Sample data is all over the place](https://github.com/CDAT/uvcdat/issues/1362)
 * **Bug**: [-DBUILD_PARALLEL=ON fails on mac (at least)](https://github.com/CDAT/uvcdat/issues/667)
 * **Bug**: [cdms2 not building in current master](https://github.com/CDAT/uvcdat/issues/1498)
 * **Bug**: [runtest does not understand mpi -n arg](https://github.com/CDAT/uvcdat/issues/1499) ([#1500](https://github.com/CDAT/uvcdat/pull/1500))
 * **Bug**: [Error building pyOpenSSL on OSX](https://github.com/CDAT/uvcdat/issues/1084)
 * **Bug**: [CMake not able to find gfortran installed via apt-get](https://github.com/CDAT/uvcdat/issues/1628)
 * **Bug**: [SciPy fails to build on CentOS 6.6](https://github.com/CDAT/uvcdat/issues/1192)
 * **Bug**: [openssl cmake error on RHEA](https://github.com/CDAT/uvcdat/issues/1751) ([#1756](https://github.com/CDAT/uvcdat/pull/1756))
 * **Bug**: [Fonts not installed at the right location on Mac OSX](https://github.com/CDAT/uvcdat/issues/1483)
 * **Bug**: [pip/easy_install error in some build](https://github.com/CDAT/uvcdat/issues/1486)
 * **Bug**: [Fix travis pyexpat build time error](https://github.com/CDAT/uvcdat/issues/1263) ([#1674](https://github.com/CDAT/uvcdat/pull/1674))
 * **Bug**: [VTK build error not reported to CDash](https://github.com/CDAT/uvcdat/issues/1317)
 * **Bug**: [pep8 executable looked for in wrong place on mac](https://github.com/CDAT/uvcdat/issues/1386) ([#1387](https://github.com/CDAT/uvcdat/pull/1387))
 * **Bug**: [flake8 not properly added to repo](https://github.com/CDAT/uvcdat/issues/1425) ([#1430](https://github.com/CDAT/uvcdat/pull/1430))
 * **Bug**: [fetching uvcdat-testdata broken on mac](https://github.com/CDAT/uvcdat/issues/1427)
 * **Bug**: [older git checkout error](https://github.com/CDAT/uvcdat/issues/1355)
 * **Bug**: [system picks up wrong pip when building ipython and tornado ](https://github.com/CDAT/uvcdat/issues/269)
 * **Bug**: [build on Ubuntu 15.10](https://github.com/CDAT/uvcdat/issues/1639)
 * **Bug**: [iPython3.0 merged update not found in master branch](https://github.com/CDAT/uvcdat/issues/1441)
 * **Enhancement**: [Update cython to 0.22](https://github.com/CDAT/uvcdat/issues/1128) ([#1436](https://github.com/CDAT/uvcdat/pull/1436))
 * **Enhancement**: [Update matplotlib to 1.4.3](https://github.com/CDAT/uvcdat/issues/1126) ([#1329](https://github.com/CDAT/uvcdat/pull/1329))
 * **Enhancement**: [Update IPython to 3.0](https://github.com/CDAT/uvcdat/issues/1127) ([#1330](https://github.com/CDAT/uvcdat/pull/1330), [#1443](https://github.com/CDAT/uvcdat/pull/1443))
 * **Enhancement**: [Update pip to 6.0.8](https://github.com/CDAT/uvcdat/issues/1053) ([#1382](https://github.com/CDAT/uvcdat/pull/1382))
 * **Enhancement**: [Update scipy to 0.16.1](https://github.com/CDAT/uvcdat/issues/1193) ([#1654](https://github.com/CDAT/uvcdat/pull/1654), [#1467](https://github.com/CDAT/uvcdat/pull/1467))
 * **Enhancement**: [Fix test suite for LEAN mode](https://github.com/CDAT/uvcdat/issues/1575) ([#1578](https://github.com/CDAT/uvcdat/pull/1578))
 * **Enhancement**: [Update python-seawater to 3.3.4](https://github.com/CDAT/uvcdat/issues/1686) ([#1687](https://github.com/CDAT/uvcdat/pull/1687))
 * **Enhancement**: [CMake warning that might break things eventually](https://github.com/CDAT/uvcdat/issues/1011) ([#1536](https://github.com/CDAT/uvcdat/pull/1536))
 * **Enhancement**: [Configuring travis/buildbot testing to be more robust](https://github.com/CDAT/uvcdat/issues/1384)
 * **Enhancement**: [Configure travis to additionally test "full" builds](https://github.com/CDAT/uvcdat/issues/1033)
 * **Enhancement**: [Update pyspharm](https://github.com/CDAT/uvcdat/issues/1070) ([#1444](https://github.com/CDAT/uvcdat/pull/1444))
 * **Enhancement**: [Update vacumm to source from github (2.5.1 to 3.0.0)](https://github.com/CDAT/uvcdat/issues/1635) ([#1685](https://github.com/CDAT/uvcdat/pull/1685))
 * **Enhancement**: [Update FFmpeg to 2.5.3](https://github.com/CDAT/uvcdat/issues/1029) ([#1381](https://github.com/CDAT/uvcdat/pull/1381))

### DV3D

 * **Bug**: [Fix vcs3d failing test ](https://github.com/CDAT/uvcdat/issues/1305)
 * **Bug**: [mac dv3d sample data put in different place](https://github.com/CDAT/uvcdat/issues/1501) ([#1503](https://github.com/CDAT/uvcdat/pull/1503))
 * **Bug**: [dv3d tests reverse baseline / test images](https://github.com/CDAT/uvcdat/issues/950)
 * **Bug**: [(q)uit does not work correctly in a DV3D interactive canvas (exits python)](https://github.com/CDAT/uvcdat/issues/953)
 * **Enhancement**: [DV3D keyword error](https://github.com/CDAT/uvcdat/issues/1152)

### UVCDAT GUI

 * **Bug**: [Full screen plots do not work](https://github.com/CDAT/uvcdat/issues/1638)
 * **Bug**: [Plots break after removing a cell and then adding it again.](https://github.com/CDAT/uvcdat/issues/1124)
 * **Bug**: [vcs anim and multiple canvas](https://github.com/CDAT/uvcdat/issues/338)
 * **Bug**: [generate range and pattern broken from GUI](https://github.com/CDAT/uvcdat/issues/1573)
 * **Bug**: [Warning: Stenciling is not enabled on Isoline](https://github.com/CDAT/uvcdat/issues/1576)
 * **Bug**: [GUI cannot switch dimensions](https://github.com/CDAT/uvcdat/issues/1375)
 * **Bug**: [Isoline Labels don't show up initially in GUI](https://github.com/CDAT/uvcdat/issues/1619)
 * **Bug**: [slab sub-selecting not working in UVCDAT GUI.](https://github.com/CDAT/uvcdat/issues/1466) ([#1637](https://github.com/CDAT/uvcdat/pull/1637))
 * **Bug**: [Colormap in GUI broken](https://github.com/CDAT/uvcdat/issues/1721)
 * **Bug**: [ uvcdat writing thousands of tempfiles to users' .uvcdat directory](https://github.com/CDAT/uvcdat/issues/1428)
 * **Bug**: [paraview still seems to be needed via matplotlib](https://github.com/CDAT/uvcdat/issues/165)
 * **Bug**: [Plots initially too big for plot window.](https://github.com/CDAT/uvcdat/issues/1632)
 * **Bug**: [clear seems to be not working on esgf search interface](https://github.com/CDAT/uvcdat/issues/151)
 * **Bug**: [http get method in esgf browser, probably need to be replaced with proper wget script](https://github.com/CDAT/uvcdat/issues/150) ([#1637](https://github.com/CDAT/uvcdat/pull/1637))
 * **Enhancement**: [animation frame not updated when runnnig vcs animation in gui](https://github.com/CDAT/uvcdat/issues/335) ([#1637](https://github.com/CDAT/uvcdat/pull/1637))
 * **Enhancement**: [animation loop keeps going even after unchecking it](https://github.com/CDAT/uvcdat/issues/336)
 * **Enhancement**: [Cosmetic Bug: dots in Scatter plot are hardly visible. ](https://github.com/CDAT/uvcdat/issues/1281) ([#1617](https://github.com/CDAT/uvcdat/pull/1617))
 * **Enhancement**: [Error message that makes no sense when trying to open a file that doesn't exists (from bookmarks for example)](https://github.com/CDAT/uvcdat/issues/87) ([#1662](https://github.com/CDAT/uvcdat/pull/1662), [#1394](https://github.com/CDAT/uvcdat/pull/1394))
 * **Enhancement**: [Redirect all (i.e. non-Python) application output to log file](https://github.com/CDAT/uvcdat/issues/1239) ([#1623](https://github.com/CDAT/uvcdat/pull/1623))
 * **Enhancement**: [Provide UI option to control labels spacing](https://github.com/CDAT/uvcdat/issues/1677)

### VCS

 * **Bug**: [vcs.Canvas.setantialiasing unusable](https://github.com/CDAT/uvcdat/issues/1400) ([#1422](https://github.com/CDAT/uvcdat/pull/1422))
 * **Enhancement**: [Labels are too close together](https://github.com/CDAT/uvcdat/issues/1339) ([#1485](https://github.com/CDAT/uvcdat/pull/1485))
 * **Bug**: [lambert proj appears to be broken??](https://github.com/CDAT/uvcdat/issues/1763) ([#1768](https://github.com/CDAT/uvcdat/pull/1768))
 * **Bug**: [Meshfill + interact() leads to error message](https://github.com/CDAT/uvcdat/issues/1764) ([#1769](https://github.com/CDAT/uvcdat/pull/1769))
 * **Bug**: [hatches/patterns don't work in vcs 2.0.beta](https://github.com/CDAT/uvcdat/issues/541) ([#1516](https://github.com/CDAT/uvcdat/pull/1516))
 * **Bug**: [isofill broken for discontinued](https://github.com/CDAT/uvcdat/issues/1734) ([#1735](https://github.com/CDAT/uvcdat/pull/1735))
 * **Bug**: [Meshfill plot does not wrap for bounds outside 0-360](https://github.com/CDAT/uvcdat/issues/1746)
 * **Bug**: [vcs_test_init_open_sizing fails on small monitors](https://github.com/CDAT/uvcdat/issues/1792)
 * **Bug**: [Remove x.png size parameters ?](https://github.com/CDAT/uvcdat/issues/1068)
 * **Bug**: [animation does not work on projected plots](https://github.com/CDAT/uvcdat/issues/1086) ([#1657](https://github.com/CDAT/uvcdat/pull/1657))
 * **Bug**: [XvsY error](https://github.com/CDAT/uvcdat/issues/1620) ([#1669](https://github.com/CDAT/uvcdat/pull/1669), [#1621](https://github.com/CDAT/uvcdat/pull/1621))
 * **Bug**: [Contour labels are don't show up in exported file (PDF)](https://github.com/CDAT/uvcdat/issues/1626)
 * **Bug**: [isolines GUI editor not connected](https://github.com/CDAT/uvcdat/issues/1625) ([#1688](https://github.com/CDAT/uvcdat/pull/1688))
 * **Bug**: [yname doesn't change with autot](https://github.com/CDAT/uvcdat/issues/1624)
 * **Bug**: [Animation and Resizing causes issues](https://github.com/CDAT/uvcdat/issues/1629) ([#1634](https://github.com/CDAT/uvcdat/pull/1634))
 * **Bug**: [Resize Window Core Dump](https://github.com/CDAT/uvcdat/issues/236)
 * **Bug**: [setting colormap on object seem to not be picked up](https://github.com/CDAT/uvcdat/issues/1271) ([#1523](https://github.com/CDAT/uvcdat/pull/1523))
 * **Bug**: [grabWindowPixmap() broken for QCDATWidget](https://github.com/CDAT/uvcdat/issues/1276)
 * **Bug**: [Patterns & Hatches on Boxfill, Isofill](https://github.com/CDAT/uvcdat/issues/1577) ([#1582](https://github.com/CDAT/uvcdat/pull/1582))
 * **Bug**: [Error when clicking on a_boxfill to get point values.](https://github.com/CDAT/uvcdat/issues/1374)
 * **Bug**: [renderTemplate needs list, gets None](https://github.com/CDAT/uvcdat/issues/1139)
 * **Bug**: [template.title.textorientation/table does not accept text object](https://github.com/CDAT/uvcdat/issues/1087) ([#1509](https://github.com/CDAT/uvcdat/pull/1509))
 * **Bug**: [Isofill Blank Spots on Solid with Indices/Levels](https://github.com/CDAT/uvcdat/issues/1645) ([#1700](https://github.com/CDAT/uvcdat/pull/1700))
 * **Bug**: [pattern are not wrapped around](https://github.com/CDAT/uvcdat/issues/1644) ([#1690](https://github.com/CDAT/uvcdat/pull/1690))
 * **Bug**: [vcs removeobject function broken](https://github.com/CDAT/uvcdat/issues/1423)
 * **Bug**: [New libx264/h264 library bug needs fix](https://github.com/CDAT/uvcdat/issues/1586) ([#1592](https://github.com/CDAT/uvcdat/pull/1592))
 * **Bug**: [Line width is inconsistent across platforms](https://github.com/CDAT/uvcdat/issues/1359) ([#1360](https://github.com/CDAT/uvcdat/pull/1360))
 * **Bug**: [x.close() brokn if more than one plot on](https://github.com/CDAT/uvcdat/issues/961)
 * **Bug**: [Continents are off](https://github.com/CDAT/uvcdat/issues/1106) ([#1706](https://github.com/CDAT/uvcdat/pull/1706), [#1717](https://github.com/CDAT/uvcdat/pull/1717))
 * **Bug**: [Editing a label, rotate to ~311 degrees, open font menu -> segfault](https://github.com/CDAT/uvcdat/issues/1093) ([#1514](https://github.com/CDAT/uvcdat/pull/1514))
 * **Bug**: [bad error message if png output dir doesn't exist](https://github.com/CDAT/uvcdat/issues/1396) ([#1556](https://github.com/CDAT/uvcdat/pull/1556))
 * **Bug**: [x.png(outFileName, width=XX, height=XX) doesn't resize output file](https://github.com/CDAT/uvcdat/issues/1588)
 * **Bug**: [fillarea dos not respect transparency](https://github.com/CDAT/uvcdat/issues/1732) ([#1733](https://github.com/CDAT/uvcdat/pull/1733))
 * **Bug**: [polar plot in isofill is not an option and isoline polar plot has wrong tic marks](https://github.com/CDAT/uvcdat/issues/729)
 * **Bug**: [can't switch to portrait mode while in background mode](https://github.com/CDAT/uvcdat/issues/1446) ([#1557](https://github.com/CDAT/uvcdat/pull/1557))
 * **Bug**: [Saving an animation at 4 frames per second on mac creates green animation](https://github.com/CDAT/uvcdat/issues/1118) ([#1564](https://github.com/CDAT/uvcdat/pull/1564))
 * **Bug**: [canvas.getcolormapname behaviour changed](https://github.com/CDAT/uvcdat/issues/1567) ([#1568](https://github.com/CDAT/uvcdat/pull/1568))
 * **Enhancement**: [colormap need user level func to set colorindices](https://github.com/CDAT/uvcdat/issues/1484) ([#1553](https://github.com/CDAT/uvcdat/pull/1553))
 * **Enhancement**: [Isofill does not work with mercator if given lat coordinates values -90, 90 (the edges)](https://github.com/CDAT/uvcdat/issues/587)
 * **Enhancement**: [Enable anti-aliasing ON by default and OFF for testing](https://github.com/CDAT/uvcdat/issues/1432) ([#1442](https://github.com/CDAT/uvcdat/pull/1442))
 * **Enhancement**: [turn antialiasing ON by default (and OFF in tests)](https://github.com/CDAT/uvcdat/issues/1433)
 * **Enhancement**: [VCS write metadata in image](https://github.com/CDAT/uvcdat/issues/1000)
 * **Enhancement**: [Provide a 'transparent' color for missing values (isofill/boxfill/etc... plots)](https://github.com/CDAT/uvcdat/issues/1042) ([#1516](https://github.com/CDAT/uvcdat/pull/1516))
 * **Enhancement**: [allow colors to define opacity](https://github.com/CDAT/uvcdat/issues/1643)
 * **Enhancement**: [allow user to reference color by string or rgba tuple](https://github.com/CDAT/uvcdat/issues/1642)
 * **Enhancement**: [EzTemplate object has no close function](https://github.com/CDAT/uvcdat/issues/1585) ([#1591](https://github.com/CDAT/uvcdat/pull/1591))
 * **Enhancement**: [setantialiasing not working if set too early](https://github.com/CDAT/uvcdat/issues/1447)

### VTK

 * **Bug**: [`size` keyword argument has no effect in `vcs.init`](https://github.com/CDAT/uvcdat/issues/1347) ([#1548](https://github.com/CDAT/uvcdat/pull/1548), [#1562](https://github.com/CDAT/uvcdat/pull/1562), [#1563](https://github.com/CDAT/uvcdat/pull/1563))

### VisTrails

 * **Bug**: [CDMS3DPlot -> CDMSCell connections are invalid](https://github.com/CDAT/uvcdat/issues/1346)

### cdms2

 * **Bug**: [cdms2 netcdf use parallel flag fails](https://github.com/CDAT/uvcdat/issues/1593)
 * **Bug**: [ESMF regrid problem](https://github.com/CDAT/uvcdat/issues/1125) ([#1574](https://github.com/CDAT/uvcdat/pull/1574))
 * **Bug**: [problem with opendap file](https://github.com/CDAT/uvcdat/issues/1475)
 * **Bug**: [Problems writing netcdf data - _FillValue error](https://github.com/CDAT/uvcdat/issues/1479)
 * **Bug**: [cdms2 cannot open files if xml generated by cdscan contains different base urls](https://github.com/CDAT/uvcdat/issues/1376)
 * **Bug**: [g2clib makefile typo](https://github.com/CDAT/uvcdat/issues/1460)
 * **Bug**: [MV2.array(0.).fill_value is NaN!](https://github.com/CDAT/uvcdat/issues/959) ([#1508](https://github.com/CDAT/uvcdat/pull/1508))
 * **Enhancement**: [cdms2.write can't write a _FillValue attribute?](https://github.com/CDAT/uvcdat/issues/1470) ([#1524](https://github.com/CDAT/uvcdat/pull/1524))
 * **Enhancement**: [createVariableCopy() upcasting variables open from cdml catalog files.](https://github.com/CDAT/uvcdat/issues/186) ([#1511](https://github.com/CDAT/uvcdat/pull/1511))
 * **Enhancement**: [try different opendap url to bypass what seems to be firewall issues on opendap ctest](https://github.com/CDAT/uvcdat/issues/1311)
 * **Enhancement**: [remove AutoAPI](https://github.com/CDAT/uvcdat/issues/1358) ([#1369](https://github.com/CDAT/uvcdat/pull/1369))
 * **Enhancement**: [enable netcdf parallel option](https://github.com/CDAT/uvcdat/issues/1324) ([#1388](https://github.com/CDAT/uvcdat/pull/1388))

### cdutil/genutil

 * **Bug**: [cdutil climos fail on file variables.](https://github.com/CDAT/uvcdat/issues/1391)

## Merged Pull Requests

 * [#993: Fix git clone & update helper scripts](https://github.com/CDAT/uvcdat/pull/993)
 * [#1261: Fix run tests buildbot](https://github.com/CDAT/uvcdat/pull/1261)
 * [#1321: Issue 1312 tag repos](https://github.com/CDAT/uvcdat/pull/1321)
 * [#1342: Sync release](https://github.com/CDAT/uvcdat/pull/1342)
 * [#1348: Vtk master bump](https://github.com/CDAT/uvcdat/pull/1348)
 * [#1357: Vtk master bump](https://github.com/CDAT/uvcdat/pull/1357)
 * [#1389: Developers documentation](https://github.com/CDAT/uvcdat/pull/1389)
 * [#1390: Sample data location updated](https://github.com/CDAT/uvcdat/pull/1390)
 * [#1392: New test for 11 & 12.](https://github.com/CDAT/uvcdat/pull/1392)
 * [#1393: Added a sleep for onscreen rendered tests](https://github.com/CDAT/uvcdat/pull/1393)
 * [#1402: Remove creation of redundant file in source tree by test](https://github.com/CDAT/uvcdat/pull/1402)
 * [#1403: Make tests fail if baselines not found](https://github.com/CDAT/uvcdat/pull/1403)
 * [#1404: Fix tag detection for git clone/update scripts](https://github.com/CDAT/uvcdat/pull/1404)
 * [#1418: Add flake8 test for vcs.](https://github.com/CDAT/uvcdat/pull/1418)
 * [#1421: Add flake8 test for xmgrace.](https://github.com/CDAT/uvcdat/pull/1421)
 * [#1426: Vtk ui test coverage](https://github.com/CDAT/uvcdat/pull/1426)
 * [#1435: Issue1108 durack1 update spyder 2.3.4 to 2.3.5.2](https://github.com/CDAT/uvcdat/pull/1435)
 * [#1440: R and rpy2](https://github.com/CDAT/uvcdat/pull/1440)
 * [#1449: keep track of temporry elets added hen plotting](https://github.com/CDAT/uvcdat/pull/1449)
 * [#1452: Fix CONTRIBUTING.md](https://github.com/CDAT/uvcdat/pull/1452)
 * [#1456: Bugfixes](https://github.com/CDAT/uvcdat/pull/1456)
 * [#1457: Allocate 512 char to save error message.](https://github.com/CDAT/uvcdat/pull/1457)
 * [#1478: Issue1477 durack1 update spyder 2.3.5.2 to 3.0.0](https://github.com/CDAT/uvcdat/pull/1478)
 * [#1480: no reason anymore to force pip at low version](https://github.com/CDAT/uvcdat/pull/1480)
 * [#1488: updated json](https://github.com/CDAT/uvcdat/pull/1488)
 * [#1490: Ansible vagrant install](https://github.com/CDAT/uvcdat/pull/1490)
 * [#1492: get cmor via git repo](https://github.com/CDAT/uvcdat/pull/1492)
 * [#1493: Pip no egg](https://github.com/CDAT/uvcdat/pull/1493)
 * [#1496: Skipped some unnecessary renders](https://github.com/CDAT/uvcdat/pull/1496)
 * [#1504: typo in rpy2 test](https://github.com/CDAT/uvcdat/pull/1504)
 * [#1507: Fix library problem when compiling python 2.7 and using VIM 7.4. Add ...](https://github.com/CDAT/uvcdat/pull/1507)
 * [#1513: Add PYPTHONPATH explicitly to cmake to make sure the right CYTHON is ...](https://github.com/CDAT/uvcdat/pull/1513)
 * [#1515: Added URI to cdmsfile objects (courtesy of @doutriaux1)](https://github.com/CDAT/uvcdat/pull/1515)
 * [#1518: RPM for 2.2.0](https://github.com/CDAT/uvcdat/pull/1518)
 * [#1522: Force build to use our Cython](https://github.com/CDAT/uvcdat/pull/1522)
 * [#1533: on the macbot it used to pick system png rather than XQuartz](https://github.com/CDAT/uvcdat/pull/1533)
 * [#1534: Skip label test for redhat only](https://github.com/CDAT/uvcdat/pull/1534)
 * [#1535: Pngupdate](https://github.com/CDAT/uvcdat/pull/1535)
 * [#1540: issue1538 durack1 update Cython 0.22.1 to 0.23.3](https://github.com/CDAT/uvcdat/pull/1540)
 * [#1541: issue1539 durack1 update iPython 3.0.0 to 4.0.0](https://github.com/CDAT/uvcdat/pull/1541)
 * [#1551: Skipping this test for RH6 as well](https://github.com/CDAT/uvcdat/pull/1551)
 * [#1552: Handle mercator infinity projection at 90,-90](https://github.com/CDAT/uvcdat/pull/1552)
 * [#1554: adds a warning about removing .dodsrc file](https://github.com/CDAT/uvcdat/pull/1554)
 * [#1558: disable testDistArray6Pes for 2.4](https://github.com/CDAT/uvcdat/pull/1558)
 * [#1559: new g2clib that allows to build libcdms w/o png](https://github.com/CDAT/uvcdat/pull/1559)
 * [#1560: Fix vector plots](https://github.com/CDAT/uvcdat/pull/1560)
 * [#1561: Add windfield dependency to rpy2 getting rid of parallel installation...](https://github.com/CDAT/uvcdat/pull/1561)
 * [#1565: Fix cmake binary download location](https://github.com/CDAT/uvcdat/pull/1565)
 * [#1572: Workaround for XCode7 and 10.11 SDK](https://github.com/CDAT/uvcdat/pull/1572)
 * [#1587: Flake8 thermo](https://github.com/CDAT/uvcdat/pull/1587)
 * [#1596: wrong baseline src file names](https://github.com/CDAT/uvcdat/pull/1596)
 * [#1600: set non parallel flag for cdscan](https://github.com/CDAT/uvcdat/pull/1600)
 * [#1601: Cdmsopenparallel](https://github.com/CDAT/uvcdat/pull/1601)
 * [#1602: Fixed doWrap method for vectors](https://github.com/CDAT/uvcdat/pull/1602)
 * [#1604: Issue png size updated](https://github.com/CDAT/uvcdat/pull/1604)
 * [#1605: Fix pattern 9](https://github.com/CDAT/uvcdat/pull/1605)
 * [#1615: turned off the keep flag that prevented to test results](https://github.com/CDAT/uvcdat/pull/1615)
 * [#1616: Fix TextCombined used wrong](https://github.com/CDAT/uvcdat/pull/1616)
 * [#1618: Made ESMF fail the build when fortran is the wrong version](https://github.com/CDAT/uvcdat/pull/1618)
 * [#1647: Fix compilation on Ubuntu with gcc 5.2.1](https://github.com/CDAT/uvcdat/pull/1647)
 * [#1652: issue1549 durack1 update Matplotlib 1.4.3 to 1.5.0](https://github.com/CDAT/uvcdat/pull/1652)
 * [#1653: issue1538 durack1 update Cython 0.23.3 to 0.23.4](https://github.com/CDAT/uvcdat/pull/1653)
 * [#1656: Set ffmpeg root when building ffmpeg](https://github.com/CDAT/uvcdat/pull/1656)
 * [#1658: load texttables and textorientations and text markers first](https://github.com/CDAT/uvcdat/pull/1658)
 * [#1661: Use cmake to download uvcmetrics test data](https://github.com/CDAT/uvcdat/pull/1661)
 * [#1667: Window flickering when png](https://github.com/CDAT/uvcdat/pull/1667)
 * [#1670: Pattern size scaling](https://github.com/CDAT/uvcdat/pull/1670)
 * [#1678: Continents & Continent Lines](https://github.com/CDAT/uvcdat/pull/1678)
 * [#1689: ENH: Add the ability to write/read PNG metadata](https://github.com/CDAT/uvcdat/pull/1689)
 * [#1691: Fixed cmake warning during configure step](https://github.com/CDAT/uvcdat/pull/1691)
 * [#1692: fix configure arguments separator](https://github.com/CDAT/uvcdat/pull/1692)
 * [#1693: Colormaps](https://github.com/CDAT/uvcdat/pull/1693)
 * [#1695: Revert "Fix #1539 - Update iPython 3.0.0 to 4.0.0"](https://github.com/CDAT/uvcdat/pull/1695)
 * [#1696: Now will work if there is no .uvcdat directory](https://github.com/CDAT/uvcdat/pull/1696)
 * [#1697: Altered some tests to ensure geometry](https://github.com/CDAT/uvcdat/pull/1697)
 * [#1699: fixed issue where old scr colormap file would not load opacity](https://github.com/CDAT/uvcdat/pull/1699)
 * [#1703: fixed tag point for external repos](https://github.com/CDAT/uvcdat/pull/1703)
 * [#1705: Fix rpm](https://github.com/CDAT/uvcdat/pull/1705)
 * [#1708: Increased threshold for pattern tests to allow meshfill to pass](https://github.com/CDAT/uvcdat/pull/1708)
 * [#1709: Fix initial size](https://github.com/CDAT/uvcdat/pull/1709)
 * [#1712: Fixed some bugs with continents line](https://github.com/CDAT/uvcdat/pull/1712)
 * [#1713: Fixed two bugs with matplotlib colormap import](https://github.com/CDAT/uvcdat/pull/1713)
 * [#1724: Fixed setcolorcell in vcs.utils](https://github.com/CDAT/uvcdat/pull/1724)
 * [#1727: Moved/renamed license](https://github.com/CDAT/uvcdat/pull/1727)
 * [#1731: Issue 1730 mesh with missing vertices](https://github.com/CDAT/uvcdat/pull/1731)
 * [#1736: Duplicate longitude wrap](https://github.com/CDAT/uvcdat/pull/1736)
 * [#1741: Noticklabelonellipticalprojections](https://github.com/CDAT/uvcdat/pull/1741)
 * [#1742: Revert "Check whether OpenSSL library and/or headers not found"](https://github.com/CDAT/uvcdat/pull/1742)
 * [#1744: BUG #1739: fitToViewport uses dataset bounds instead of recomputing them](https://github.com/CDAT/uvcdat/pull/1744)
 * [#1755: Fixes issue with incorrect URIs for opendap urls](https://github.com/CDAT/uvcdat/pull/1755)
 * [#1757: Fixed conversion to base64 string](https://github.com/CDAT/uvcdat/pull/1757)
 * [#1772: BUG: proj4 over option causes problems with polar projections](https://github.com/CDAT/uvcdat/pull/1772)
 * [#1774: Revert "BUG: proj4 over option causes problems with polar projections"](https://github.com/CDAT/uvcdat/pull/1774)
 * [#1778: Irregular cut wrap](https://github.com/CDAT/uvcdat/pull/1778)
 * [#1793: Got rid of screen size logic from test](https://github.com/CDAT/uvcdat/pull/1793)
 * [#1794: Fixed bug that was breaking continents when set at canvas level](https://github.com/CDAT/uvcdat/pull/1794)
 * [#1802: Update readme master](https://github.com/CDAT/uvcdat/pull/1802)

## Known Bugs

### Critical

 * [master fails some tests on RH6/CentOS6](https://github.com/CDAT/uvcdat/issues/1481)
 * [creating pngs in background mode leaks memory](https://github.com/CDAT/uvcdat/issues/1397)

### Other

 * [seg fault on a lambert projection](https://github.com/CDAT/uvcdat/issues/1804)
 * [can't read some old vcs scr files](https://github.com/CDAT/uvcdat/issues/1801)
 * [Disable projected click, fix time values](https://github.com/CDAT/uvcdat/pull/1800)
 * [ratio="autot" fails to correctly generate the initial ratio](https://github.com/CDAT/uvcdat/issues/1795)
 * [Fit to viewport needs updating for continent outline](https://github.com/CDAT/uvcdat/issues/1786)
 * [proj4 acting up on macs and ubuntu mesa](https://github.com/CDAT/uvcdat/issues/1777)
 * [Meshfill leaves extra display plots lying around](https://github.com/CDAT/uvcdat/issues/1770)
 * [test_vcs_animate_projected_meshfill_mollweide.png is not wrapped](https://github.com/CDAT/uvcdat/issues/1754)
 * [var.squeeze() truncates axis information](https://github.com/CDAT/uvcdat/issues/1738)
 * [CDMS2/MV2.newaxis doesn't work](https://github.com/CDAT/uvcdat/issues/1722)
 * [cdms2.getGrid()/setGrid() doesn't work](https://github.com/CDAT/uvcdat/issues/1707)
 * [Fix memory leak in cdtime](https://github.com/CDAT/uvcdat/issues/1698)
 * [Meshfill plot with Mercator projection issue](https://github.com/CDAT/uvcdat/issues/1671)
 * [Weight problems in cdutil.ANNUALCYCLE.climatology (daily data)](https://github.com/CDAT/uvcdat/issues/1664)
 * [projections still broken](https://github.com/CDAT/uvcdat/issues/1640)
 * [MPI builds and Python multiprocessing](https://github.com/CDAT/uvcdat/issues/1608)
 * [iso plot failure](https://github.com/CDAT/uvcdat/issues/1594)
 * [VCS/VTK warnings and UV-CDAT logo missing in pdf/ps output files](https://github.com/CDAT/uvcdat/issues/1583)
 * [cdscan hang](https://github.com/CDAT/uvcdat/issues/1546)
 * [Catch cdscan errors without triggering runtime failures](https://github.com/CDAT/uvcdat/issues/1512)
 * [Bad rendering of aeqd projection](https://github.com/CDAT/uvcdat/issues/1462)
 * [vcs.plot(iso) creates text object that are not removed after clear](https://github.com/CDAT/uvcdat/issues/1424)
 * [can't delete file attribute](https://github.com/CDAT/uvcdat/issues/1398)
 * [cdms2 can only open cdscanned http files from the directory the file is at](https://github.com/CDAT/uvcdat/issues/1368)



<a name="2.2"></a>

# 2.2 Changelog

## Closed Issues

### ACME

 * **Bug**: [No usch text combined](https://github.com/CDAT/uvcdat/issues/1096) ([#1107](https://github.com/CDAT/uvcdat/pull/1107))
 * **Bug**: [invalid framebuffer operation](https://github.com/CDAT/uvcdat/issues/1100)
 * **Bug**: [average() indentation error](https://github.com/CDAT/uvcdat/issues/1048) ([#1050](https://github.com/CDAT/uvcdat/pull/1050))

### Build

 * **Bug**: [esmp install broken](https://github.com/CDAT/uvcdat/issues/981) ([#982](https://github.com/CDAT/uvcdat/pull/982))
 * **Bug**: [Pyclimate not built with build mode all](https://github.com/CDAT/uvcdat/issues/1071) ([#1075](https://github.com/CDAT/uvcdat/pull/1075))
 * **Bug**: [mac build broken](https://github.com/CDAT/uvcdat/issues/991) ([#998](https://github.com/CDAT/uvcdat/pull/998), [#995](https://github.com/CDAT/uvcdat/pull/995))
 * **Bug**: [test failing because mean is different ](https://github.com/CDAT/uvcdat/issues/1063) ([#1076](https://github.com/CDAT/uvcdat/pull/1076))
 * **Bug**: [Building on OS X 10.10.2](https://github.com/CDAT/uvcdat/issues/1012)
 * **Bug**: [git_update.sh fails if updating to a tag](https://github.com/CDAT/uvcdat/issues/837)
 * **Bug**: [ctest 'fails' if python has not been run interactively at least once (anonymous logging problem)](https://github.com/CDAT/uvcdat/issues/456) ([#1102](https://github.com/CDAT/uvcdat/pull/1102))
 * **Bug**: [Out of source detection is broken](https://github.com/CDAT/uvcdat/issues/713)
 * **Bug**: [metrics not build if CDAT_BUILD_GUI=OFF](https://github.com/CDAT/uvcdat/issues/996)
 * **Bug**: [SciPy fails to build on CentOS 6.6](https://github.com/CDAT/uvcdat/issues/1192)
 * **Bug**: [scipy fails to build without -D__ACCELERATE__](https://github.com/CDAT/uvcdat/issues/966) ([#1165](https://github.com/CDAT/uvcdat/pull/1165))
 * **Enhancement**: [try to detect protocol for user](https://github.com/CDAT/uvcdat/issues/810)
 * **Enhancement**: [no need for git to check ssl](https://github.com/CDAT/uvcdat/issues/924)
 * **Enhancement**: [Several warnings during the cmake stage that should be cleaned?](https://github.com/CDAT/uvcdat/issues/825) ([#1062](https://github.com/CDAT/uvcdat/pull/1062))
 * **Enhancement**: [Update udunits to 2.2.x branch](https://github.com/CDAT/uvcdat/issues/847)
 * **Enhancement**: [Update netcdf to 4.3.2](https://github.com/CDAT/uvcdat/issues/846) ([#972](https://github.com/CDAT/uvcdat/pull/972))
 * **Enhancement**: [Update matplotlib to 1.4.2](https://github.com/CDAT/uvcdat/issues/841) ([#921](https://github.com/CDAT/uvcdat/pull/921))

### DV3D

 * **Bug**: [Slider issues with Hovmuller plot and vector slicer.](https://github.com/CDAT/uvcdat/issues/1146) ([#1147](https://github.com/CDAT/uvcdat/pull/1147))
 * **Bug**: [3D_Scalar Unexpected Error](https://github.com/CDAT/uvcdat/issues/884)
 * **Bug**: [dv3d list broken](https://github.com/CDAT/uvcdat/issues/1285) ([#1287](https://github.com/CDAT/uvcdat/pull/1287))

### Documentation

 * **Bug**: [UV-CDAT docs website: cdms/cdtime manual page problem](https://github.com/CDAT/uvcdat/issues/1136)
 * **Enhancement**: [Document for manual testing of GUI](https://github.com/CDAT/uvcdat/issues/1215)

### UVCDAT GUI

 * **Bug**: [Traceback on cell creation](https://github.com/CDAT/uvcdat/issues/1018)
 * **Bug**: [.vt doesn't have all the steps](https://github.com/CDAT/uvcdat/issues/283)
 * **Bug**: [Cython classmethod_utility_code used in VisTrails vtDVD3D](https://github.com/CDAT/uvcdat/issues/1056)
 * **Bug**: [GUI cannot load variable](https://github.com/CDAT/uvcdat/issues/1057)
 * **Bug**: [Refresh problem with 2.1](https://github.com/CDAT/uvcdat/issues/1007)
 * **Bug**: [Error while plotting meshfill plot](https://github.com/CDAT/uvcdat/issues/1284)
 * **Bug**: [Deleting all variables doesn't work if one variable is derived from another (in GUI).](https://github.com/CDAT/uvcdat/issues/897)
 * **Enhancement**: [animation processing message](https://github.com/CDAT/uvcdat/issues/642)
 * **Enhancement**: [uvcdat "executable" should unset env or it might be using the "Wrong" python](https://github.com/CDAT/uvcdat/issues/730)

### VCS

 * **Bug**: [lines drawn behind data](https://github.com/CDAT/uvcdat/issues/1143)
 * **Bug**: [The plotting of 120 plots and clearing  is taking too long](https://github.com/CDAT/uvcdat/issues/715)
 * **Bug**: [Cannot animate Isofill](https://github.com/CDAT/uvcdat/issues/1141) ([#1142](https://github.com/CDAT/uvcdat/pull/1142))
 * **Bug**: [ctest might fail because of too many digits on mean](https://github.com/CDAT/uvcdat/issues/952)
 * **Bug**: [animation boxfill broken](https://github.com/CDAT/uvcdat/issues/1234) ([#1236](https://github.com/CDAT/uvcdat/pull/1236))
 * **Bug**: [isoline labels text color broken](https://github.com/CDAT/uvcdat/issues/1230)
 * **Bug**: [wrapping labels seems to still not work](https://github.com/CDAT/uvcdat/issues/1133) ([#1172](https://github.com/CDAT/uvcdat/pull/1172))
 * **Bug**: [Error on meshfill](https://github.com/CDAT/uvcdat/issues/1245) ([#1247](https://github.com/CDAT/uvcdat/pull/1247))
 * **Bug**: [default boxfill wrong lat labels](https://github.com/CDAT/uvcdat/issues/960) ([#965](https://github.com/CDAT/uvcdat/pull/965), [#962](https://github.com/CDAT/uvcdat/pull/962))
 * **Bug**: [in some case the continents are not plotted properly (polar proj with north pole)](https://github.com/CDAT/uvcdat/issues/1020) ([#1022](https://github.com/CDAT/uvcdat/pull/1022))
 * **Bug**: [boxfill plots don't pick proper interval](https://github.com/CDAT/uvcdat/issues/867)
 * **Bug**: [markers not drawn if x world coordinate reversed](https://github.com/CDAT/uvcdat/issues/969) ([#970](https://github.com/CDAT/uvcdat/pull/970))
 * **Bug**: [Control + Click doesn't work in GUI](https://github.com/CDAT/uvcdat/issues/1163) ([#1169](https://github.com/CDAT/uvcdat/pull/1169))
 * **Bug**: [Ext1 and Ext2 are rendering incorrectly](https://github.com/CDAT/uvcdat/issues/1204) ([#1209](https://github.com/CDAT/uvcdat/pull/1209))
 * **Bug**: [clear canvas while animation running in GUI doesn't seem to stop it](https://github.com/CDAT/uvcdat/issues/1197) ([#1207](https://github.com/CDAT/uvcdat/pull/1207))
 * **Bug**: [animation vcs speed slider seem to have no effect](https://github.com/CDAT/uvcdat/issues/1196) ([#1202](https://github.com/CDAT/uvcdat/pull/1202))
 * **Bug**: [isofill masked does not align with isofill cells](https://github.com/CDAT/uvcdat/issues/1170) ([#1171](https://github.com/CDAT/uvcdat/pull/1171))
 * **Bug**: [Isoline labels broken](https://github.com/CDAT/uvcdat/issues/1132)
 * **Enhancement**: [animate.save() print statements](https://github.com/CDAT/uvcdat/issues/1085) ([#1121](https://github.com/CDAT/uvcdat/pull/1121))
 * **Enhancement**: [text rotation in VTK different from vcs way](https://github.com/CDAT/uvcdat/issues/503) ([#1013](https://github.com/CDAT/uvcdat/pull/1013))
 * **Enhancement**: [Fix vcs interact warnings ](https://github.com/CDAT/uvcdat/issues/651)
 * **Enhancement**: [mean on vcs plots should use cdutil.averager if possible](https://github.com/CDAT/uvcdat/issues/1024) ([#1028](https://github.com/CDAT/uvcdat/pull/1028))
 * **Enhancement**: [time slider should be disabled when running animation](https://github.com/CDAT/uvcdat/issues/1195) ([#1201](https://github.com/CDAT/uvcdat/pull/1201))

### VTK

 * **Bug**: [isolines labels are different between mac and linux](https://github.com/CDAT/uvcdat/issues/1160)

### cdms2

 * **Bug**: [load and close with large data files doesn't work](https://github.com/CDAT/uvcdat/issues/511)

### cdutil/genutil

 * **Bug**: [cdutil times criteriaargclim is useless and leads to error](https://github.com/CDAT/uvcdat/issues/984) ([#985](https://github.com/CDAT/uvcdat/pull/985))

## Merged Pull Requests

 * [#747: Fixing UVCDAT runtime environment](https://github.com/CDAT/uvcdat/pull/747)
 * [#944: Issue942 durack1 python279 update](https://github.com/CDAT/uvcdat/pull/944)
 * [#951: Vcs3D features for v2.1.1](https://github.com/CDAT/uvcdat/pull/951)
 * [#971: Fixes exception from VTKVCSBackend](https://github.com/CDAT/uvcdat/pull/971)
 * [#973: Build in source](https://github.com/CDAT/uvcdat/pull/973)
 * [#974: System python updated](https://github.com/CDAT/uvcdat/pull/974)
 * [#975: Update cmake to version 3.1 on travis before building](https://github.com/CDAT/uvcdat/pull/975)
 * [#979: Line duplicate points fix](https://github.com/CDAT/uvcdat/pull/979)
 * [#987: Create an option to enable vtkweb](https://github.com/CDAT/uvcdat/pull/987)
 * [#988: Setting the correct PYTHON_SITE_PACKAGES_PREFIX on Apple](https://github.com/CDAT/uvcdat/pull/988)
 * [#990: Merge remote-tracking branch 'origin/fix-quotes-updated' into release](https://github.com/CDAT/uvcdat/pull/990)
 * [#992: Updated packages reference](https://github.com/CDAT/uvcdat/pull/992)
 * [#993: Fix git clone & update helper scripts](https://github.com/CDAT/uvcdat/pull/993)
 * [#994: Checking for http and https as well now](https://github.com/CDAT/uvcdat/pull/994)
 * [#1005: do not turn off metrics when no GUI](https://github.com/CDAT/uvcdat/pull/1005)
 * [#1014: Update background color](https://github.com/CDAT/uvcdat/pull/1014)
 * [#1038: Optimize vtk](https://github.com/CDAT/uvcdat/pull/1038)
 * [#1047: 1. In the section involving 'allaxesdummy', where a dummy variable is cr...](https://github.com/CDAT/uvcdat/pull/1047)
 * [#1052: should address part of #729](https://github.com/CDAT/uvcdat/pull/1052)
 * [#1067: Line duplicate points fix](https://github.com/CDAT/uvcdat/pull/1067)
 * [#1069: Removes a warning](https://github.com/CDAT/uvcdat/pull/1069)
 * [#1072: Issue421 durack1 add seawater packages](https://github.com/CDAT/uvcdat/pull/1072)
 * [#1073: Issue423 durack1 add vacumm package](https://github.com/CDAT/uvcdat/pull/1073)
 * [#1089: Issue423 durack1 fix vacumm dependencies](https://github.com/CDAT/uvcdat/pull/1089)
 * [#1090: Remove pycharm and unnecessary README files](https://github.com/CDAT/uvcdat/pull/1090)
 * [#1091: Vcs2d interactions updated](https://github.com/CDAT/uvcdat/pull/1091)
 * [#1098: Fixes autot resizing when configurator instantiated](https://github.com/CDAT/uvcdat/pull/1098)
 * [#1110: Now we can build on Yosemite ](https://github.com/CDAT/uvcdat/pull/1110)
 * [#1113: VCS2D Animation while Interacting](https://github.com/CDAT/uvcdat/pull/1113)
 * [#1114: Added files](https://github.com/CDAT/uvcdat/pull/1114)
 * [#1115: adding ipython created cyclical deps](https://github.com/CDAT/uvcdat/pull/1115)
 * [#1119: Isofill on pointdata struct grid](https://github.com/CDAT/uvcdat/pull/1119)
 * [#1123: VTK can't seem to be able to use mac system headers](https://github.com/CDAT/uvcdat/pull/1123)
 * [#1135: Workaround for #1093](https://github.com/CDAT/uvcdat/pull/1135)
 * [#1138: Vcs3 d fix 2.2 interaction problems](https://github.com/CDAT/uvcdat/pull/1138)
 * [#1144: Issue 587 projected ticks](https://github.com/CDAT/uvcdat/pull/1144)
 * [#1145: Adding Dockerfiles for generating docker images](https://github.com/CDAT/uvcdat/pull/1145)
 * [#1153: Add vcs keywords](https://github.com/CDAT/uvcdat/pull/1153)
 * [#1154: Fix missing displays for animation/interaction](https://github.com/CDAT/uvcdat/pull/1154)
 * [#1156: Fix error in getCoordType](https://github.com/CDAT/uvcdat/pull/1156)
 * [#1157: vcs3D-return_to_shell_on_q_keypress_event](https://github.com/CDAT/uvcdat/pull/1157)
 * [#1159: Fix rc1 tests](https://github.com/CDAT/uvcdat/pull/1159)
 * [#1161: VCS2D Animation Speedup](https://github.com/CDAT/uvcdat/pull/1161)
 * [#1164: Time slider upgrade](https://github.com/CDAT/uvcdat/pull/1164)
 * [#1167: Target will now detach when configurator detaches](https://github.com/CDAT/uvcdat/pull/1167)
 * [#1168: Fixes ubuntu error that showed up for charles](https://github.com/CDAT/uvcdat/pull/1168)
 * [#1173: Changed 2D animation to use same type of animation speed as 3d](https://github.com/CDAT/uvcdat/pull/1173)
 * [#1177: Fixed some VTK error messages that showed up when ending configure](https://github.com/CDAT/uvcdat/pull/1177)
 * [#1178: Issue 1158 auto magic time labels](https://github.com/CDAT/uvcdat/pull/1178)
 * [#1179: Fix ratio resizing issue](https://github.com/CDAT/uvcdat/pull/1179)
 * [#1182: pickle would not work](https://github.com/CDAT/uvcdat/pull/1182)
 * [#1184: 3D support for vcs.update](https://github.com/CDAT/uvcdat/pull/1184)
 * [#1185: vtk_ui.Button tests](https://github.com/CDAT/uvcdat/pull/1185)
 * [#1190: Fix for clear and close for DV3D plots](https://github.com/CDAT/uvcdat/pull/1190)
 * [#1206: Made slider jump instead of animate, added test](https://github.com/CDAT/uvcdat/pull/1206)
 * [#1216: Newdiagtest](https://github.com/CDAT/uvcdat/pull/1216)
 * [#1218: New test, for spaghetti/multiline plots (plot set 3).](https://github.com/CDAT/uvcdat/pull/1218)
 * [#1219: Salinity](https://github.com/CDAT/uvcdat/pull/1219)
 * [#1221: Boxfill bug branch clean up](https://github.com/CDAT/uvcdat/pull/1221)
 * [#1225: Unstructured plots](https://github.com/CDAT/uvcdat/pull/1225)
 * [#1226: Added message in setup_runtime scripts](https://github.com/CDAT/uvcdat/pull/1226)
 * [#1227: Allow open/interact without plotting anything](https://github.com/CDAT/uvcdat/pull/1227)
 * [#1238: Newdiagstes charles](https://github.com/CDAT/uvcdat/pull/1238)
 * [#1240: Fixes typo in CDMS raise statements](https://github.com/CDAT/uvcdat/pull/1240)
 * [#1243: Fixes typo in CDMS raise statements](https://github.com/CDAT/uvcdat/pull/1243)
 * [#1244: Pressing the "i" key makes button disappear (and other issues)](https://github.com/CDAT/uvcdat/pull/1244)
 * [#1246: Colorpicker now uses manager correctly](https://github.com/CDAT/uvcdat/pull/1246)
 * [#1249: Meshfill animation](https://github.com/CDAT/uvcdat/pull/1249)
 * [#1255: Marker deletion](https://github.com/CDAT/uvcdat/pull/1255)
 * [#1257: Merge colorpicker changes into release](https://github.com/CDAT/uvcdat/pull/1257)
 * [#1258: Colorpicker renderer selection](https://github.com/CDAT/uvcdat/pull/1258)
 * [#1261: Fix run tests buildbot](https://github.com/CDAT/uvcdat/pull/1261)
 * [#1262: Update master](https://github.com/CDAT/uvcdat/pull/1262)
 * [#1267: Issue 903 turn off paraview](https://github.com/CDAT/uvcdat/pull/1267)
 * [#1269: Vcs3 d fix release issues](https://github.com/CDAT/uvcdat/pull/1269)
 * [#1270: Fixes more typos in raise statements](https://github.com/CDAT/uvcdat/pull/1270)
 * [#1273: Toolbar layout fixes](https://github.com/CDAT/uvcdat/pull/1273)
 * [#1296: Sync master](https://github.com/CDAT/uvcdat/pull/1296)
 * [#1298: Add lapack to libcf deps](https://github.com/CDAT/uvcdat/pull/1298)
 * [#1307: Fixed the ordering of images for regression testing](https://github.com/CDAT/uvcdat/pull/1307)
 * [#1316: Final commits to make buildbot pass](https://github.com/CDAT/uvcdat/pull/1316)

## Known Bugs

### Critical

 * [Taylor diagrams (plot set 14)](https://github.com/CDAT/uvcdat/issues/1180)
 * [Resize Window Core Dump](https://github.com/CDAT/uvcdat/issues/236)

### Other

 * [gui python script extensions are written as string when they should be boolean](https://github.com/CDAT/uvcdat/issues/1306)
 * [Fix vcs3d failing test ](https://github.com/CDAT/uvcdat/issues/1305)
 * [dv3d cannot go back into interact mode](https://github.com/CDAT/uvcdat/issues/1295)
 * [dv3d plotting ad changing attributes breaks dv3d](https://github.com/CDAT/uvcdat/issues/1286)
 * [setting colormap on object seem to not be picked up](https://github.com/CDAT/uvcdat/issues/1271)
 * [polar plot for sub zones seems to not work](https://github.com/CDAT/uvcdat/issues/1265)
 * [ESMF regrid problem](https://github.com/CDAT/uvcdat/issues/1125)
 * [Continents are off](https://github.com/CDAT/uvcdat/issues/1106)
 * [x/yaxisconvert not respected anymore.](https://github.com/CDAT/uvcdat/issues/1066)
 * [x.close() brokn if more than one plot on](https://github.com/CDAT/uvcdat/issues/961)
 * [(q)uit does not work correctly in a DV3D interactive canvas (exits python)](https://github.com/CDAT/uvcdat/issues/953)
 * [cdtime and big hours](https://github.com/CDAT/uvcdat/issues/781)
 * [-DBUILD_PARALLEL=ON fails on mac (at least)](https://github.com/CDAT/uvcdat/issues/667)
 * [The vectors are not drawn when using projection other than plat-caree.](https://github.com/CDAT/uvcdat/issues/653)
 * [Unable to write unsigned int8 variable in netcdf4 file (non-netcdf3 type)](https://github.com/CDAT/uvcdat/issues/481)
 * [Fix setup_runtime.sh script for DMG](https://github.com/CDAT/uvcdat/issues/409)
 * [system picks up wrong pip when building ipython and tornado ](https://github.com/CDAT/uvcdat/issues/269)

<a id="2.1"></a>

# 2.1 Changelog

## Closed Issues

### Build

 * **Bug**: [On Mac Udunits fails because of flex not found](https://github.com/CDAT/uvcdat/issues/733)
 * **Bug**: [CMOR doesn't build](https://github.com/CDAT/uvcdat/issues/786)
 * **Bug**: [visit_vtk failed to build: missing vtkPolyDataToPolyDataFilter.h](https://github.com/CDAT/uvcdat/issues/802)
 * **Bug**: [git_update.sh fails if updating to a tag](https://github.com/CDAT/uvcdat/issues/837)

### DV3D

 * **Enhancement**: [Change template name from xyt to Hovmoller-3D](https://github.com/CDAT/uvcdat/issues/765)
 * **Bug**: [3D_Scalar plot (xyt) gives errors plotting 3D variable with no time dimensions.](https://github.com/CDAT/uvcdat/issues/854)
 * **Bug**: [Plotted a 3D-scalar, and the vertical level reported in the heading appears to be upside-down.](https://github.com/CDAT/uvcdat/issues/853)
 * **Bug**: [Two UV-CDAT Labels in the Lower Right for 3D VCS Plots](https://github.com/CDAT/uvcdat/issues/858)
 * **Bug**: [ubuntu animations aren't saved](https://github.com/CDAT/uvcdat/issues/799)

### UVCDAT GUI

 * **Bug**: [rename colormap does not put it in list of available colormaps](https://github.com/CDAT/uvcdat/issues/829)
 * **Enhancement**: [Error messages when launching uvcdat on Rhea.](https://github.com/CDAT/uvcdat/issues/727)

### VCS

 * **Bug**: [meshfill missing color not respected](https://github.com/CDAT/uvcdat/issues/873)
 * ***Bug*: [Scatter plot labels](https://github.com/CDAT/uvcdat/issues/716)
 * **Bug**: [x.showbg() does not work in 2.0.0](https://github.com/CDAT/uvcdat/issues/863)
 * **Bug**: [x.interact() should print an error message when no canvas is open](https://github.com/CDAT/uvcdat/issues/862)
 * **Bug**: [cleanup EzTemplate](https://github.com/CDAT/uvcdat/issues/826)
 * **Bug**: [meshfill plot broekn with bg=0](https://github.com/CDAT/uvcdat/issues/804)
 * **Bug**: [continents chopped](https://github.com/CDAT/uvcdat/issues/693)
 * **Bug**: [yxvsx plot a black screen when no text and box1.priority = 0](https://github.com/CDAT/uvcdat/issues/706)
 * **Bug**: [x.clear does not do anything.](https://github.com/CDAT/uvcdat/issues/707)
 * **Bug**: [boxfill/isofill missing attrbute does not change coor of missing](https://github.com/CDAT/uvcdat/issues/855)
 * **Bug**: [VTK not mapping?](https://github.com/CDAT/uvcdat/issues/871)
 * **Bug**: [templates do not save associated texttable/orientation](https://github.com/CDAT/uvcdat/issues/816)
 * **Bug**: [oned plots wrong when levels are flipped](https://github.com/CDAT/uvcdat/issues/832)
 * **Bug**: [Can't load data in uvcdat 2.0.0 !](https://github.com/CDAT/uvcdat/issues/843) ([#852](https://github.com/CDAT/uvcdat/pull/852))
 * **Bug**: [xname and yname doesn't work](https://github.com/CDAT/uvcdat/issues/710)
 * **Bug**: [boxfill leve_1 level_2 reassigned](https://github.com/CDAT/uvcdat/issues/869)
 * **Bug**: [default boxfill wrong lat labels](https://github.com/CDAT/uvcdat/issues/960)
 * **Bug**: [isoline pure numpy fails](https://github.com/CDAT/uvcdat/issues/928) ([#929](https://github.com/CDAT/uvcdat/pull/929))
 * **Bug**: [template rescale could move things too far and lead to errors](https://github.com/CDAT/uvcdat/issues/805)
 * **Enhancement**: [drawing of colorbar in vcs too slow](https://github.com/CDAT/uvcdat/issues/849)
 * **Enhancement**: [white bg by default](https://github.com/CDAT/uvcdat/issues/817)
 * **Enhancement**: [Blank png: x.png does not set the alpha/transparency info correctly !](https://github.com/CDAT/uvcdat/issues/848)

### VTK

 * **Bug**: [Contours colored wrong when data has a wide range](https://github.com/CDAT/uvcdat/issues/851)

### VisTrails

 * **Bug**: [uvcdat script broken](https://github.com/CDAT/uvcdat/issues/894)

### cdms2

 * **Enhancement**: [convert cdtime object to datetime](https://github.com/CDAT/uvcdat/issues/771)

### cdutil/genutil

 * **Bug**: [full averaging weirdness](https://github.com/CDAT/uvcdat/issues/757)

## Merged Pull Requests

 * [#748: Removes scripts from images/ directory](https://github.com/CDAT/uvcdat/pull/748)
 * [#791: Fixes BUILDINSOURCE detection](https://github.com/CDAT/uvcdat/pull/791)
 * [#827: Vcs dv3d separate plot constituents updated](https://github.com/CDAT/uvcdat/pull/827)
 * [#828: Typo when disabling a package](https://github.com/CDAT/uvcdat/pull/828)
 * [#831: Patches Python to remove global OSX packages](https://github.com/CDAT/uvcdat/pull/831)
 * [#833: Makes missing GIT_PROTOCOL an error](https://github.com/CDAT/uvcdat/pull/833)
 * [#835: Makes git_update.sh handle detached heads](https://github.com/CDAT/uvcdat/pull/835)
 * [#836: Fixes typo in vistrails_external.cmake](https://github.com/CDAT/uvcdat/pull/836)
 * [#904: Issue 898 vertical flipped monotonic decreasing](https://github.com/CDAT/uvcdat/pull/904)
 * [#905: Issue 691 interact mac broken](https://github.com/CDAT/uvcdat/pull/905)
 * [#907: Vcs3 d fix z axis problems](https://github.com/CDAT/uvcdat/pull/907)
 * [#912: Vcs3 d fix animation exception](https://github.com/CDAT/uvcdat/pull/912)
 * [#936: update images for dv3d_hovmoller_test and dv3d_slider_test](https://github.com/CDAT/uvcdat/pull/936)
 * [#940: Fix error causing 3D plots to hang](https://github.com/CDAT/uvcdat/pull/940)

<a id="2.0"></a>

# 2.0 Changelog

## Closed Issues

### Build

 * **Bug**: [setup_runtime.sh needs to be sourced with full path ](https://github.com/CDAT/uvcdat/issues/522)
 * **Bug**: [some regrid test try to import matplotlib even though they don't really need it](https://github.com/CDAT/uvcdat/issues/574)
 * **Bug**: [VTK doesn't build (freetype headers problem)](https://github.com/CDAT/uvcdat/issues/594)
 * **Bug**: [Building on Mac OS X 10.9.4 doesn't locate sqlite3 (no build error)](https://github.com/CDAT/uvcdat/issues/588)
 * **Bug**: [mac os 10.8/10.9](https://github.com/CDAT/uvcdat/issues/562)
 * **Bug**: [CDAT_BUILD_MODE=ALL does NOT build ALL](https://github.com/CDAT/uvcdat/issues/544)
 * **Bug**: [uvcdat build needs QMake even for DEFAULT and no GUI](https://github.com/CDAT/uvcdat/issues/554)
 * **Enhancement**: [sciFuncs submodule needs to be put in our source code,](https://github.com/CDAT/uvcdat/issues/635)
 * **Enhancement**: [Binaries release for 2.0](https://github.com/CDAT/uvcdat/issues/618)

### UVCDAT GUI

 * **Bug**: [color map in GUI doesn't work](https://github.com/CDAT/uvcdat/issues/640)
 * **Bug**: [uvcdat gui vcs plots do not stick in spreadsheet](https://github.com/CDAT/uvcdat/issues/575)
 * **Bug**: [animation auto min/max is broken](https://github.com/CDAT/uvcdat/issues/639)
 * **Bug**: [Adjusting color map is broken](https://github.com/CDAT/uvcdat/issues/677)
 * **Bug**: [vcs windows do not stick in spreadsheet](https://github.com/CDAT/uvcdat/issues/589)

### VCS

 * **Bug**: [possible isofill issue](https://github.com/CDAT/uvcdat/issues/519)
 * **Bug**: [test set_opt_polar does not plot in bg](https://github.com/CDAT/uvcdat/issues/626)
 * **Bug**: [boxfill as a .list() that needs to be removed](https://github.com/CDAT/uvcdat/issues/625)
 * **Bug**: [kill uvcdat gui middle of animation generating leads to many vtk errors](https://github.com/CDAT/uvcdat/issues/617)
 * **Bug**: [yx datawc_y1, y2 not respected anymore....](https://github.com/CDAT/uvcdat/issues/669)
 * **Bug**: [animations now need PyQt4 old code seems broken](https://github.com/CDAT/uvcdat/issues/579)
 * **Bug**: [flip does not work when missing values](https://github.com/CDAT/uvcdat/issues/661)
 * **Bug**: [VCS won't plot when every value is exactly zero](https://github.com/CDAT/uvcdat/issues/648)
 * **Bug**: [Close Does Not Work](https://github.com/CDAT/uvcdat/issues/718)
 * **Bug**: [The "clear" does nothing. ](https://github.com/CDAT/uvcdat/issues/717)
 * **Bug**: [colormap does not stick on animation](https://github.com/CDAT/uvcdat/issues/676)
 * **Bug**: [VTKPlots.plotVectors points/attributes length mismatch](https://github.com/CDAT/uvcdat/issues/712)
 * **Bug**: [x.show missing](https://github.com/CDAT/uvcdat/issues/596)
 * **Bug**: [Isofill does not work with polar coordinates](https://github.com/CDAT/uvcdat/issues/586)
 * **Bug**: [boxfill draws outside range](https://github.com/CDAT/uvcdat/issues/620)
 * **Bug**: [boxfill not fully plotted (lat bit white)](https://github.com/CDAT/uvcdat/issues/627)
 * **Bug**: [test_dump_json broken](https://github.com/CDAT/uvcdat/issues/624)
 * **Bug**: [x.interact() fails in vcs (None object)](https://github.com/CDAT/uvcdat/issues/634)
 * **Bug**: [inverted levels do not plot properly](https://github.com/CDAT/uvcdat/issues/637)
 * **Bug**: [wrapping in projection not quite working](https://github.com/CDAT/uvcdat/issues/566)
 * **Bug**: [Scatter plot won't plot the scatters](https://github.com/CDAT/uvcdat/issues/724)
 * **Bug**: [meshfill does not seem to mask](https://github.com/CDAT/uvcdat/issues/551)
 * **Bug**: [X and Y axis lables (xname, yname) won't show up on for any graphics method on the plot](https://github.com/CDAT/uvcdat/issues/743)
 * **Bug**: [boxfill does NOT show all data](https://github.com/CDAT/uvcdat/issues/555)
 * **Bug**: [markers are stretched too much when x and y scales are too different](https://github.com/CDAT/uvcdat/issues/553)
 * **Bug**: [vcs init fails if no initial.attributes](https://github.com/CDAT/uvcdat/issues/614)
 * **Bug**: [Test cdms_load_and_plot_axis_variable fails](https://github.com/CDAT/uvcdat/issues/689)
 * **Enhancement**: [read new json formatted initial file attribute](https://github.com/CDAT/uvcdat/issues/597)
 * **Enhancement**: [remove setcolormap warning](https://github.com/CDAT/uvcdat/issues/598)
 * **Enhancement**: [easily removable error warning when saving to new json file](https://github.com/CDAT/uvcdat/issues/619)

### VisTrails

 * **Bug**: [vistrails module uvcdat_cdms missing](https://github.com/CDAT/uvcdat/issues/581)
 * **Bug**: [isoline plots don't plot on first try](https://github.com/CDAT/uvcdat/issues/611)

### cdms2

 * **Enhancement**: [Read ACME test data](https://github.com/CDAT/uvcdat/issues/658)

## Merged Pull Requests

 * [#739: Vcs3d record animation](https://github.com/CDAT/uvcdat/pull/739)


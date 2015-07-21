---
title: VCS Chapter 2
layout: docs
manual: vcs
index: 2
---





##  CHAPTER 2 VCS Installation and Setup

These steps below should be followed before running VCS, and are necessary in order to produce plots on the screen and in background mode. The steps include putting in place various input files and setting up fonts for XGKS.

###Mandatory Input Files

You must have the XGKS fonts directory set. XGKS is an implementation of the ANSI Graphical Kernel System in C, the programming language used to develop VCS. XGKS fonts pertain to those used for graphical displays on the VCS Canvas.

Before running VCS, it is necessary to set the environment variable XGKSFontDir. That is, enter:

```
setenv XGKSFontDir /the_absolute_path/fontdb
```

where `/the_absolute_path` denotes the absolute path location for the `/fontdb` directory.

It is best if this setenv statement is included in the `.login` or `.cshrc` file located in the user's home directory (`/$HOME`).

Note: if VCS aborts with the message:

```
"XGKS: can't load font 1 from /the_absolute_path./fontdb - aborting"
```

then the `XGKSFontDir` variable is improperly set.

Nine XGKS font styles are supported at this time (24 additional fonts are in the works):

  * SanSerif Roman 
  * Serif Roman 
  * Sanserif Bold Roman 
  * Serif Bold Roman 
  * Sanserif Italic Roman 
  * Serif Italic Roman 
  * Sanserif Script 
  * Serif Script 
  * Gothic 

###Recommended Input Files

It is strongly recommended that two input files be put in place before attempting to run VCS, but it is not necessary to have these files in place in order to run VCS. These include a file for specifying initial attributes called, "initial.attributes" and a file for printing hard copy output called, "HARD_COPY".

####File for Specifying Initial Attributes

At start-up, VCS reads a script file named initial.attributes that defines the initial settings of the VCS tables. Although not required to run VCS, this initial.attributes file contains many predefined settings to aid the beginning user of VCS. The path to the file must be:

```
/$HOME/PCMDI_GRAPHICS/initial.attributes
```

where `/$HOME` denotes the user's home directory. (Note, when VCS is executed for the first time, a `/PCMDI_GRAPHICS` subdirectory will be created automatically if it has not already been created.)

####Changing the initial.attributes File

The user can customize the contents of the initial.attributes file. This is most easily accomplished by changing the contents of a VCS object saving the state of the system with the use of the `saveVCSinitialattribute()` function.  This action will place a new initial.attributes file with the desired setting(s) in the user's

```
/$HOME/PCMDI_GRAPHICS
```

directory. For recovery purposes, the old initial.attributes file is copied to file initial.attributes% in the same directory.

<a name="hard_copy"></a>

####File for Printing

VCS graphical displays can be printed only if the user customizes a `HARD_COPY` file (included with the VCS software) for the home system. The path to the `HARD_COPY` file must be:

```
/$HOME/PCMDI_GRAPHICS/HARD_COPY
```

where `/$HOME` denotes the user's home directory. The `HARD_COPY` file contains the following necessary information for printing at the user's home site:

  * A list of the available home Postscript printing devices. 
  * The absolute path on the home system to the gplot executable (provided with the VCS software) that converts files in the Computer Graphics Metafile (CGM) format to Postscript files. 
  * Instructions for setting the environment aliases `landscape' and `portrait' that are used to generate Postscript files outside VCS. 

The setting for the environment variable `PRINTER`. (When `PRINTER` is set to `printer`, VCS assumes that the printer manager `lpr` is in use; when `PRINTER` is unset, VCS assumes that the printer manager is `lp`. Incidences of the message:

```
"Error - In sending CGM file to printer" are an indication of an incorrect
setting for the `PRINTER' environment variable.)"
```



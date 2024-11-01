---
title: VCS Chapter 1
layout: docs
manual: vcs
index: 1
---






##  CHAPTER 1 Introduction

The PCMDI Visualization Control System (VCS) is expressly designed to meet the needs of climate scientists. Because of the breadth of its capabilities, VCS can be a useful tool for other scientific applications as well. VCS allows wide-ranging changes to be made to the data display, provides for hardcopy output, and includes a means for recovery of a previous display.

### Basic Concepts of VCS

In the VCS model, the data display is defined by a trio of named object sets, designated the "primary objects" (or "primary elements"). These include:

  * the data, which define what is to be displayed and is ingested into the system via other PCMDI software components or via the Numeric module; 
  * the graphics method, which specifies the display technique; and 
  * the picture template, which determines the appearance of each segment of the display. Tables for manipulating these primary objects are stored in VCS for later recall and possible use.

In addition, detailed specification of the primary objects' attributes is provided by eight "secondary objects" (or secondary elements"):

  1. colormap: specification of combinations of 256 available colors 
  2. fill area: style, style index, and color index 
  3. format: specifications for converting numbers to display strings 
  4. line: line type, width and color index 
  5. list: a sequence of pairs of numerical and character values 
  6. marker: marker type, size, and color index 
  7. text: text font type, character spacing, expansion and color index 
  8. text orientation: character height, angle, path, and horizontal/vertical alignment 

By combining primary and secondary objects in various ways (either at the command line or in a program), the VCS user can comprehensively diagnose and intercompare climate model simulations. VCS provides capabilities to:

  * View, select and modify attributes of data variables and of their dimensions
  * Create and modify existing template attributes and graphics methods
  * Save the state-of-the-system as a script to be run interactively or in a program
  * Save a display as a Computer Graphics Metafile (CGM), GIF, Postscript, Sun Raster, or Encapsulated Postscript file 
  * Perform grid transformations and compute new data variables 
  * Create and modify color maps
  * zoom into a specified portion of a display 
  * Change the orientation (portrait vs. landscape) or size (partial vs. full-screen) of a display 
  * Animate a single data variable or more than one data variable simultaneously
  * Display different map projections


### Purpose of this document

This document will focus primarily on the VCS software commands necessary to operate VCS with minimal knowledge. The knowledge of VCS will gradually be increased allowing the user to construct more complex visualization operations that are vital to their scientific research. The material contained in this document will walk you through simple VCS operations and use CDMS module to ingest data sets and to manipulate the data before it is displayed. Because the best way to learn a new tool is by examples, this document is heavy on examples and provides an extensive command reference guide.





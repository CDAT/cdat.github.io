---
title: VCS Chapter 5
layout: docs
manual: vcs
index: 5
---





##  CHAPTER 5 VCS Command Reference Guide

If you want the full description of a command, then you've made it to the
right place.

Note, in the "Arguments" column, any item(s) surrounded by "[]" are optional to
the function.

<table class="table">
  <thead>
    <tr>
      <th>Command</th>

      <th>Description</th>

      <th>Arguments</th>

      <th>Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="4">
        <p><a name="initializing" ></a>Initializing</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="init" ></a>init</code></td>

      <td>
        <p>Initialize, Construct a VCS Canvas Object</p>

        

        <p>Construct the VCS Canas object. There can only be at most 8 VCS Canvases open
        at any given time.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs,cdms2

file=cdms2.open(`filename.nc')
slab=file.getslab('variable')
a=vcs.init()
# This examples constructs 4 VCS Canvas a.plot(slab)
# Plot slab using default settings
b=vcs.init()
# Construct VCS object
template=b.gettemplate('AMIP')
# Get 'example' template object
b.plot(slab,template)
# Plot slab using template 'AMIP'
c=vcs.init()
# Construct new VCS object
isofill=c.getisofill('quick')
# Get 'quick' isofill graphics method
c.plot(slab,template,isofill)
# Plot slab using template and isofill objects
d=vcs.init()
# Construct new VCS object
isoline=c.getisoline('quick')

# Get 'quick' isoline graphics method
c.plot(isoline,slab,template)
# Plot slab using isoline and template objects
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="help_commands" ></a>Help Commands</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="help" ></a>help</code></td>

      <td>
        <p>On-Line HELP!!!</p>

        

        <p>Gives insight to other VCS functions by providing a description and at least
        one example.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs

vcs.help()
vcs.help('init')
vcs.help('plot')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="objecthelp" ></a>objecthelp</code></td>

      <td>
        <p>Print out the object's doc string</p>

        

        <p>Print out information on VCS objects. See example on its use.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
ln=a.getline('red')
# Get a VCS line object
a.objecthelp(ln)
# This will print out information on how to use ln
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="canvas" ></a>Canvas</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="mode" ></a>mode</code></td>

      <td>
        <p>Update the VCS Canvas.</p>

        

        <p>Updating of the graphical displays on the VCS Canvas can be deferred until a
        later time. This is helpful when generating templates or displaying numerous
        plots. If a series of commands are given to VCS and the Canvas Mode is set to
        manual (i.e., 0), then no updating of the VCS Canvas occurs until the 'update'
        function is executed.</p>

        <p>Note, by default the VCS Canvas Mode is set to 'Automatic', which means VCS
        will update the VCS Canvas as necessary without prompting from the user.</p>
      </td>

      <td>
        <ul>
          <li>
            <p>mode</p>
            <p>Options:</p>
            <ul>
              <li>1 = automatic</li>

              <li>0 = manual</li>
            </ul>
          </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
...
a=vcs.init()
a.mode=0
# Set updating to manual mode
a.plot(array,'default','boxfill','quick')
box=x.getboxfill('quick')
box.color_1=100
box.xticlabels('lon30','lon30')
box.xticlabels('','')
box.datawc(1e20,1e20,1e20,1e20)
box.datawc(-45.0, 45.0, -90.0, 90.0)
...
a.update()
# Update the changes manually
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="update" ></a>update</code></td>

      <td>
        

        <p>If a series of commands are given to VCS and the Canvas Mode is set to manual,
        then use this function to update the VCS Canvas manually.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
...
a=vcs.init()
a.mode=0
# Go to manual mode a.plot(s,'default','boxfill','quick')
box=x.getboxfill('quick')
box.color_1=100
box.xticlabels('lon30','lon30')
box.xticlabels('','')
box.datawc(1e20,1e20,1e20,1e20)
box.datawc(-45.0, 45.0, -90.0, 90.0)
a.update()
# Update the changes manually
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="open" ></a>open</code></td>

      <td>
        

        <p>Open VCS Canvas object. This routine really just manages the VCS canvas. It
        will popup the VCS Canvas for viewing. It can be used to display the VCS
        Canvas.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.open()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="close" ></a>close</code></td>

      <td>
        

        <p>Close the VCS Canvas. It will remove the VCS Canvas object from the screen,
        but not deallocate it.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.close()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="portrait" ></a>portrait</code></td>

      <td>
        

        <p>Change the VCS Canvas orientation to Portrait.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.plot(array)
a.portrait()
# Change the VCS Canvas orientation and set object flag to portrait
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="landscape" ></a>landscape</code></td>

      <td>
        

        <p>Change the VCS Canvas orientation to Landscape.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.plot(array)
a.landscape()
# Change the VCS Canvas orientation and set object flag to landscape
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="page" ></a>page</code></td>

      <td>
        

        <p>Change the VCS Canvas orientation to either 'portrait' or 'landscape'.</p>

        <p>The orientation of the VCS Canvas and of cgm and raster images is controlled
        by the PAGE command. Only portrait (y &gt; x) or landscape (x &gt; y)
        orientations are permitted.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.plot(array)
a.page()
# Change the VCS Canvas orientation and set object flag to portrait
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="geometry" ></a>geometry</code></td>

      <td>
        

        <p>The geometry command is used to set the size and position of the VCS
        canvas.</p>
      </td>

      <td>
        <ul>
          <li>width</li>

          <li>height</li>

          <li>x position</li>

          <li>y position</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.geometry(450, 337,100, 100)
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="printing_and_saving_graphics"></a>Printing and Saving Graphics</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="printer" ></a>printer</code></td>

      <td>
        <p>Send plots to the printer</p>

        

        <p>This function creates a temporary cgm file and then sends it to the specified
        printer. Once the printer received the information, then the temporary cgm file
        is deleted. The temporary cgm file is created in the user's PCMDI_GRAPHICS
        directory.</p>

        <p>The PRINTER command is used to send the VCS Canvas plot(s) directly to the
        printer.</p>

        <p>Note: VCS graphical displays can be printed only if the user customizes a
        HARD_COPY file (included with the VCS software) for the home system. The path to
        the HARD_COPY file must be</p>
        <pre style="word-break:none;">
/$HOME/PCMDI_GRAPHICS/HARD_COPY
</pre>

        <p>where <code>/$HOME</code> denotes the user's home directory.</p>

        <p><a href="vcs-2.html#hard_copy">More information on the HARD_COPY file</a></p>
      </td>

      <td>
        <ul>
          <li>printer's name</li>

          <li>
            <p>[orientation]</p>

            <p>Options:</p>

            <ul>
              <li>l = landscape</li>

              <li>p = portrait</li>
            </ul>
          </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array)
a.printer('printer_name')
# Send plot(s) to postscript printer
a.printer('printer_name','p')
# Send plot(s) to the printer in portrait mode
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="gif" ></a>gif</code></td>

      <td>
        <p>Save plot(s) as gif image</p>

        

        <p>In some cases, the user may want to save the plot out as a gif image. This
        routine allows the user to save the VCS canvas output as a gif file.</p>

        <p>This file can be converted to other gif formats with the aid of xv and other
        such imaging tools found freely on the web.</p>

        <p>If no path/file name is given and no previously created gif file has been</p>

        <p>designated, then file</p>

        <p>/$HOME/PCMDI_GRAPHICS/default.gif</p>

        <p>will be used for storing gif images. However, if a previously created gif file
        is designated, that file will be used for gif output.</p>

        <p>By default, the page orientation is in Landscape mode (l). To translate the
        page orientation to portrait mode (p), enter 'p' as the second parameter.</p>

        <p>The GIF command is used to create or append to a gif file. There are two modes
        for saving a gif file: 'Append' mode (a) appends gif output to an existing gif
        file(i.e., making it an animated gif); 'Replace' (r) mode overwrites an existing
        gif file with new gif output.</p>
      </td>

      <td>
        <ul>
          <li>Filename to save</li>

          <li>
            <p>[merge]</p>

            <p>Options:</p>

            <ul>
              <li>a = append (or merge) image to an existing file</li>

              <li>r = replace file with new image</li>
            </ul>
          </li>

          <li>[orientation (l|p)]

            <ul>
              <li>l = landscape</li>

              <li>p = portrait</li>
            </ul>
          </li>

          <li>[geometry (<code>width</code>x<code>height</code>)]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array)
a.gif(filename='example.gif', merge='a', orientation='l', geometry='800x600')
# overwrite existing gif file (default is merge='r')
a.gif('example')
# overwrite existing gif file
a.gif('example',merge='r')
# merge gif image into existing gif file
a.gif('example',merge='a')
# merge gif image into existing gif file with landscape orientation
a.gif('example',orientation='l')
# merge gif image into existing gif file with portrait orientation
a.gif('example',orientation='p')
# merge gif image into existing gif file and set the gif geometry
a.gif('example',geometry='600x500')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="postscript" ></a>postscript</code></td>

      <td>
        <p>Save plot(s) to a postscript file</p>

        

        <p>Postscript output is another form of vector graphics. It is larger than its
        CGM output counter part, because it is stored out in ASCII format.</p>

        <p>There are two modes for saving a postscript file: `Append' (a) mode appends
        postscript output to an existing postscript file; and `Replace' (r) mode
        overwrites an existing postscript file with new postscript output. The default
        mode is to overwrite an existing postscript file (i.e. mode (r)).</p>
      </td>

      <td>
        <ul>
          <li>filename</li>

          <li>
            <p>[mode]</p>

            <p>Options:</p>

            <ul>
              <li>a = append (or merge) image to an existing file</li>

              <li>r = replace file with new image</li>
            </ul>
          </li>

          <li>[width of image]</li>

          <li>[height of image]</li>

          <li>
            <p>[units of width/height]</p>

            <p>Options:</p>

            <ul>
              <li>'in' or 'inches' &mdash; default</li>

              <li>'cm'</li>

              <li>'mm'</li>

              <li>'dot' or 'dots'</li>
            </ul>
          </li>

          <li>[left_margin]</li>

          <li>[right_margin]</li>

          <li>[top_margin]</li>

          <li>[bottom_margin]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array)
# Overwrite a postscript file
a.postscript('example')
# Append postscript to an existing file
a.postscript('example', 'a')
# Overwrite an existing file
a.postscript('example', 'r')
# Append postscript to an existing file
a.postscript('example', mode='a')
# US Legal (default)
a.postscript('example', width=11.5, height= 8.5)
# A4
a.postscript('example', width=21, height=29.7, units='cm')
# US Legal output and control of margins (for printer friendly output), default units 'inches'
a.postscript('example', right_margin=.2,left_margin=.2,top_margin=.2,bottom_margin=.2)
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="cgm" ></a>cgm</code></td>

      <td>
        

        <p>To save a graphics plot in VCS the user can call CGM along with the name of
        the output. This routine will save the displayed image on the VCS canvas as a
        binary vector graphics that can be imported into MSWord or Framemaker. CGM files
        are in ISO standards output format.</p>

        <p>The CGM command is used to create or append to a cgm file.</p>
      </td>

      <td>
        <ul>
          <li>
            <p>cgm file name</p>
          </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.plot(array,'default','isofill','quick')
# Note, if you don't specify the extension `.cgm' at the end of file name, then the extension `.cgm' will be put on for you.
a.cgm(o)
a.cgm('example')
# by default a cgm file will be appended it an existing file
a.cgm('example','a')
# 'a' will instruct cgm to append to an existing file
a.cgm('example','r')
# 'r' will instruct cgm to over write an existing file
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="raster" ></a>raster</code></td>

      <td>
        

        <p>In some cases, the user may want to save the plot out as an raster image. This
        routine allows the user to save the VCS canvas output as a SUN raster file.</p>

        <p>This file can be converted to other raster formats with the aid of xv and
        other such imaging tools found freely on the web.</p>

        <p>If no path/file name is given and no previously created raster file has been
        designated, then file</p>
        <pre>
/$HOME/PCMDI_GRAPHICS/default.ras
</pre>

        <p>will be used for storing raster images. However, if a previously created
        raster file is designated, that file will be used for raster output.</p>
      </td>

      <td>
        <ul>
          <li>
            <p>raster file name</p>
          </li>

          <li>
            <p>[mode]</p>

            <ul>
              <li>
                <p>'a'=will append raster image to an existing raster file</p>
              </li>

              <li>
                <p>'r'=will replace a raster file with a new raster file</p>
              </li>
            </ul>
          </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array)
# Note, if you don't specify the extension `.ras' at the end of file name, then the extension `.ras' will be put on for you.
a.raster('example','a')
# append raster image to existing file
a.raster('example','r')
# over write existing raster file
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="pstogif" ></a>pstogif</code></td>

      <td>
        

        <p>This function allows the user to convert a postscript file to a gif file.</p>
      </td>

      <td>
        <ul>
          <li>
            <p>postscript file name</p>
          </li>

          <li>
            <p>['l'=landscape 'p'=portrait]</p>
          </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array)
a.pstogif('filename.ps') # convert to landscape gif file
a.pstogif('filename.ps','l') # convert to landscape gif file
a.pstogif('filename.ps','p') # convert to portrait gif file
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="plot_and_clear_commands" ></a>Plot and
        Clear Commands</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="plot" ></a>plot</code></td>

      <td>
        

        <p>Plot an array(s) of data given a template and graphics method. The VCS
        template is used to define where the data and variable attributes will be
        displayed on the VCS Canvas. The VCS graphics method is used to define how the
        array(s) will be shown on the VCS Canvas.</p>
      </td>

      <td>
        <p>The form of the call is:</p>

        <p>plot(array1=None, array2=None, template_name=None,
        graphics_method=None,graphics_name=None, [key=value [, key=value [, ...]]])</p>
        <ul>
          <li>[array1] - NumPy Array, <code>2 &le; rank(array) &le; 5</code></li>
          <li>[array2] - NumPy Array, <code>2 &le; rank(array) &le; 5</code></li>
          <li>[template_name]</li>
          <li>[graphics_method]</li>
          <li>[graphics_name]</li>
          <li>[keyword arguments]</li>
        </ul>
        
        <p>See section <a href="vcs-4.html#4.5">4.5</a> for a detailed listing of possible plot options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
x=vcs.init()
# x is an instance of the VCS class object (constructor)
x.plot(array)
# this call will use default settings for template and boxfill
x.plot(array, 'AMIP', 'isofill','AMIP_psl')
# this is specifying the template and graphics method
t=x.gettemplate('AMIP')
# get a predefined the template 'AMIP'
vec=x.getvector('quick')
# get a predefined the vector graphics method 'quick'
x.plot(array1, array2, t, vec)
# plot the data as a vector using the 'AMIP' template
x.clear()
# clear the VCS Canvas of all plots
box=x.createboxfill('new')
# create boxfill graphics method 'new'
x.plot(box,t,array)
# plot array data using box 'new' and template 't'
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="boxfill_plot" ></a>boxfill</code></td>

      <td>
        <p>Generate a boxfill plot</p>

        

        <p>Generate a boxfill plot given the data, boxfill graphics method, and template.
        If no boxfill class object is given, then the 'default' boxfill graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('boxfill')
# Show all the existing boxfill graphics methods
box=a.getboxfill('quick')
# Create instance of 'quick'
a.boxfill(array,box)
# Plot array using specified box and default template
templt=a.gettemplate('AMIP')
# Create an instance of template 'AMIP'
a.clear()
# Clear VCS canvas
a.boxfill(array,box,template)
# Plot array using specified box and template
a.boxfill(box,array,template)
# Plot array using specified box and template
a.boxfill(template,array,box)
# Plot array using specified box and template
a.boxfill(template,array,box)
# Plot array using specified box and template
a.boxfill(array,'AMIP','quick')
# Use 'AMIP' template and 'quick' boxfill
a.boxfill('AMIP',array,'quick')
# Use 'AMIP' template and 'quick' boxfill
a.boxfill('AMIP','quick',array)
# Use 'AMIP' template and 'quick' boxfill
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="continents_plot" ></a>continents</code></td>

      <td>
        <p>Generate a continents plot</p>

        

        <p>Generate a continents plot given the continents graphics method, and template.
        If no continents class object is given, then the 'default' continents graphics
        method is used. Similarly, if no template class object is given, then the
        'default' template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('continents')
# Show all the existing continents graphics methods
con=a.getcontinents('quick')
# Create instance of 'quick'
a.continents(array,con)
# Plot array using specified con and default template
a.clear()
# Clear VCS canvas
a.continents(array,con,template)
# Plot array using specified con and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isofill_plot" ></a>isofill</code></td>

      <td>
        <p>Generate an isofill plot</p>

        

        <p>Generate a isofill plot given the data, isofill graphics method, and template.
        If no isofill class object is given, then the 'default' isofill graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('isofill')
# Show all the existing isofill graphics methods
iso=a.getisofill('quick')
# Create instance of 'quick'
a.isofill(array,iso)
# Plot array using specified iso and defaul template
a.clear()
# Clear VCS canvas
a.isofill(array,iso,template)
# Plot array using specified iso and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isoline_plot" ></a>isoline</code></td>

      <td>
        <p>Generate an isoline plot</p>

        

        <p>Generate a isoline plot given the data, isoline graphics method, and template.
        If no isoline class object is given, then the 'default' isoline graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.show('isoline')
# Show all the existing isoline graphics methods
iso=a.getisoline('quick')
# Create instance of 'quick'
a.isoline(array,iso)
# Plot array using specified iso and default template
a.clear()
# Clear VCS canvas a.isoline(array,iso,template)
# Plot array using specified iso and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="outfill_plot" ></a>outfill</code></td>

      <td>
        <p>Generate an outfill plot</p>

        

        <p>Generate a outfill plot given the data, outfill graphics method, and template.
        If no outfill class object is given, then the 'default' outfill graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.show('outfill')
# Show all the existing outfill graphics methods
out=a.getoutfill('quick')
# Create instance of 'quick'
a.outfill(array,out)
# Plot array using specified out and default template
a.clear()
# Clear VCS canvas
a.outfill(array,out,template)
# Plot array using specified out and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="outline_plot" ></a>outline</code></td>

      <td>
        <p>Generate an outline plot</p>

        

        <p>Generate a outline plot given the data, outline graphics method, and template.
        If no outline class object is given, then the 'default' outline graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('outline')
# Show all the existing outline graphics methods
out=a.getoutline('quick')
# Create instance of 'quick'
a.outline(array,out)
# Plot array using specified out and default template
a.clear()
# Clear VCS canvas a.outline(array,out,template)
# Plot array using specified out and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="scatter_plot" ></a>scatter</code></td>

      <td>
        <p>Generate a scatter plot</p>

        

        <p>Generate a scatter plot given the data, scatter graphics method, and template.
        If no scatter class object is given, then the 'default' scatter graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
a.show('scatter')
# Show all the existing scatter graphics methods
sct=a.getscatter('quick')
# Create instance of 'quick'
a.scatter(array1,array2,sct)
# Plot array using specified sct and default template
a.clear()
# Clear VCS canvas
a.scatter(array1,array2,sct,template)
# Plot array using specified sct and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="vector_plot" ></a>vector</code></td>

      <td>
        <p>Generate a vector plot</p>

        

        <p>Generate a vector plot given the data, vector graphics method, andtemplate. If
        no vector class object is given, then the 'default' vectorgraphics method is
        used. Similarly, if no template class object is given,then the 'default' template
        is used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('vector')
# Show all the existing vector graphics methods
vec=a.getvector('quick')
# Create instance of 'quick'
a.vector(array1,array2,vec)
# Plot array using specified vec and default template
a.clear()
# Clear VCS canvas
a.vector(array1,array2,vec,template)
# Plot array using specified vec and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="xvsy_plot" ></a>xvsy</code></td>

      <td>
        <p>Generate a Xvsy plot</p>

        

        <p>Generate a XvsY plot given the data, XvsY graphics method, and template. If no
        XvsY class object is given, then the 'default' XvsY graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xvsy')
# Show all the existing XvsY graphics methods
xy=a.getxvsy('quick')
# Create instance of 'quick'
a.xvsy(array1,array2,xy)
# Plot array using specified xy and default template
a.clear()
# Clear VCS canvas
a.xvsy(array1,array2,xy,template)
# Plot array using specified xy and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="xyvsy_plot" ></a>xyvsy</code></td>

      <td>
        <p>Generate a Xyvsy plot</p>

        

        <p>Generate a Xyvsy plot given the data, Xyvsy graphics method, and template. If
        no Xyvsy class object is given, then the 'default' Xyvsy graphics method is used.
        Simerly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xyvsy')
# Show all the existing Xyvsy graphics methods
xyy=a.getxyvsy('quick')
# Create instance of 'quick'
a.xyvsy(array,xyy)
# Plot array using specified xyy and default template
a.clear()
# Clear VCS canvas
a.xyvsy(array,xyy,template)
# Plot array using specified xyy and template

</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="yxvsx_plot" ></a>yxvsx</code></td>

      <td>
        <p>Generate a Yxvsx plot</p>

        

        <p>Generate a Yxvsx plot given the data, Yxvsx graphics method, and template. If
        no Yxvsx class object is given, then the 'default' Yxvsx graphics method is used.
        Simerly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td>
        <p>See plot command for options.</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('yxvsx')
# Show all the existing Yxvsx graphics methods
yxx=a.getyxvsx('quick')
# Create instance of 'quick'
a.yxvsx(array,yxx)
# Plot array using specified yxx and default template
a.clear()
# Clear VCS canvas
a.yxvsx(array,yxx,template)
# Plot array using specified yxx and template
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="clear" ></a>clear</code></td>

      <td>
        <p>At some point it will become necessary to clear all the plots from the VCS
        Canvas. This routine will remove all plots on the VCS Canvas.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.clear()
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="query_functions" ></a>Query Functions</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="graphicsmethodname"></a>graphicsmethodname</code></td>

      <td>
        

        <p>Returns the grapics method's type string: boxfill, isofill, isoline, outfill,
        outline, continents, scatter, vector, xvsy, xyvsy, yxvsx, 3d_scalar, or 3d_vector.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
box=a.getboxfill() # Get an default boxfill
iso=a.getisofill() # Get default isofill
ln=a.getline() # Get default line
print a.graphicsmethodname(box) # Will
# print 'boxfill'
print a.graphicsmethodname(iso) # Will
# print 'isofill'
print a.graphicsmethodname(ln) # Will return
# None, because ln is not a
# graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getcontinentstype"></a>getcontinentstype</code></td>

      <td>
        

        <p>Return continents type from VCS. Remember the value can only be between 0 and
        11.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
cont_type = a.getcontinentstype() # Get the
# continents type
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isgraphicsmethod"></a>isgraphicsmethod</code></td>

      <td>
        

        <p>Indicates if the entered argument is one of the following graphics methods:
        boxfill, isofill, isoline, outfill, outline, continents, scatter, vector, xvsy,
        xyvsy, yxvsx.</p>

        <p>Returns a 1, which indicates true, if the argment is one of the above.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
box=a.getboxfill('quick')
# To Modify an existing boxfill use:
    ...
if a.isgraphicsmethod(box):
    box.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isboxfill" ></a>isboxfill</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary boxfill graphics method object.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
box=a.getboxfill("quick")
# To Modify an existing boxfill object
...
if a.isboxfill(box):
    box.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="iscontinents" ></a>iscontinents</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary continents graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
con=a.getcontinents("quick")
# To Modify an existing continents object
...
if a.iscontinents(con):
    con.list()

</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isisofill" ></a>isisofill</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary isofill graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
iso=a.getisofill("quick")
# To Modify an existing isofill object
...
if a.isisofill(iso):
    iso.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isisoline" ></a>isisoline</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary isoline graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
iso=a.getisoline("quick")
# To Modify an existing isoline object
...
if a.isisoline(iso):
    iso.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isoutfill" ></a>isoutfill</code></td>

      <td>
        

        <p>Check to see if this object is a VCS primary outfill graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
out=a.getoutfill("quick")
# To Modify an existing outfill object
...

if a.isoutfill(out):
    out.list()

</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isoutline" ></a>isoutline</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary outline graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
out=a.getoutline("quick")
# To Modify an existing outline object
...
if a.isoutline(out):
    out.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isvector" ></a>isvector</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary vector graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
vec=a.getvector("quick")
# To Modify an existing vector object
...
if a.isvector(vec):
    vec.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isxvsy" ></a>isxvsy</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary xvsy graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
xy=a.getxvsy("quick")
# To Modify an existing xvsy object
...
if a.isxvsy(xy):
    xy.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isxyvsy" ></a>isxyvsy</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary Xyvsy graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
xyy=a.getxyvsy("quick")
# To Modify an existing Xyvsy object
...
if a.isxyvsy(xyy):
    xyy.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isyxvsx" ></a>isyxvsx</code></td>

      <td>
        

        <p>Check to see if an object is a VCS primary yxvsx graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
yxx=a.getyxvsx("quick")
# To Modify an existing yxvsx object
...
if a.isyxvsx(yxx):
    yxx.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="is3d_scalar"></a>is3d_scalar</code></td>

      <td>
        <p>Check to see if an object is a VCS primary 3d_scalar graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td>
        <ul>
          <li>Object to Check</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a = vcs.init()
scalar = a.getxyvsy("quick")
# To Modify an existing 3d_scalar object
...
if vcs.is3d_scalar(scalar):
    scalar.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="is3d_vector"></a>is3d_vector</code></td>

      <td>
        <p>Check to see if an object is a VCS primary 3d_vector graphics method.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td>
        <ul>
          <li>Object to Check</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a = vcs.init()
vector = a.getxyvsy("quick")
# To Modify an existing 3d_vector object
...
if vcs.is3d_vector(vector):
    vector.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="istemplate" ></a>istemplate</code></td>

      <td>
        

        <p>Indicates if the entered argument a template.</p>

        <p>Returns a 1 if the argment true.</p>

        <p>Otherwise, it will return a 0, indicating false.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
templt=a.gettemplate('quick')
# Modify an existing template named 'quick'
...
if a.istemplate(templt):
    templt.list()
# If it is a template then list its members
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="issecondaryobject"></a>issecondaryobject</code></td>

      <td>
        

        <p>In addition, detailed specification of the primary elements' (or primary class
        elements'), attributes is provided by eight secondary elements or (secondary
        class elements):</p>

        <p>1.) colormap: specification of combinations of 256 available colors</p>

        <p>2.) fill area: style, style index, and color index</p>

        <p>3.) format: specifications for converting numbers to display strings</p>

        <p>4.) line: line type, width, and color index</p>

        <p>5.) list: a sequence of pairs of numerical and character values</p>

        <p>6.) marker: marker type, size, and color index</p>

        <p>7.) text table: text font type, character spacing, expansion, and color
        index</p>

        <p>8.) text orientation: character height, angle, path, and horizontal/vertical
        alignment</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
line=a.getline('red')
# To Modify an existing line object
...
if a.issecondaryobject(line):
    box.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isfillarea" ></a>isfillarea</code></td>

      <td>
        

        <p>Check to see if an object is a VCS secondary fillarea.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
fa=a.getfillarea("def37")
# To Modify an existing fillarea object
...
if a.isfillarea(fa):
    fa.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="isline" ></a>isline</code></td>

      <td>
        

        <p>Check to see if this object is a VCS secondary line.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
ln=a.getline("red")
# To Modify an existing line object
...
if a.isline(ln):
    ln.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="ismarker" ></a>ismarker</code></td>

      <td>
        

        <p>Check to see if an object is a VCS secondary marker.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
mk=a.getmarker("red")
# To Modify an existing marker object
...
if a.ismarker(mk):
    mk.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="istextcombined"></a>istextcombined</code></td>

      <td>
        

        <p>Check to see if an object is a VCS secondary text combined.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
tc=a.gettextcombined("std", "7left")
# To Modify existing text table and orientation objects
...
if a.istextcombined(tc):
    tc.list()
if a.istexttable(tc):
    tc.list()
if a.istextorientation(tc):
    tc.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="istextorientation"></a>istextorientation</code></td>

      <td>
        

        <p>Check to see if an object is a VCS secondary text orientation.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
to=a.gettextorientation("7left")
# To Modify an existing text orientation object
...
if a.istextorientation(to):
    to.list()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="istexttable" ></a>istexttable</code></td>

      <td>
        

        <p>Check to see if an object is a VCS secondary text table.</p>
      </td>

      <td><ul><li>Object to Query</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
a=vcs.init()
tt=a.gettexttable("std")
# To Modify an existing text table object
...
if a.istexttable(tt):
    tt.list()
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="list_elements" ></a>List Available Templates,
        Graphics Methods and Secondary Objects</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="listelements" ></a>listelements</code></td>

      <td>
        

        <p>Returns a Python list of all the VCS class objects.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.listelements()
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="show" ></a>show</code></td>

      <td>
        

        <p>Show the list of VCS primary and secondary class objects.</p>
      </td>

      <td><ul><li>Type of objects to list</li></ul></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('boxfill')
a.show('isofill')
a.show('template')
a.show('line')
a.show('marker')
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="graphics_method_objects" ></a>Graphics
        Method Objects</p>
      </th>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="boxfill" ></a>Boxfill</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createboxfill" ></a>createboxfill</code></td>

      <td>
        

        <p>Create a new boxfill graphics method given the name and the existingboxfill
        graphics method to copy the attributes from. If no existing boxfill graphics
        method name is given, then the default boxfill graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new boxfill name</p></li>
          <li> <p>[name of boxfill to copy attributes from]</p> </li>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('boxfill')
box=a.createboxfill('example1')
a.show('boxfill')
box=a.createboxfill('example2','quick')
a.show('boxfill')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getboxfill" ></a>getboxfill</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a boxfill
        class object from an existing VCS boxfill graphics method. If no boxfill name is
        given, then boxfill 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createboxfill function.)</p>
      </td>

      <td>
        <ul>
          <li>[boxfill name]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('boxfill')
# Show all the existing boxfill graphics methods
box=a.getboxfill()
# box instance of 'default' boxfill graphics method
box2=a.getboxfill('quick')
# box2 instance of existing 'quick' boxfill graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: boxfillobject</p>

        

        <p>The boxfill graphics method (Gfb) displays a two-dimensional data array by
        surrounding each data value by a colored grid box.</p>

        <p>This class is used to define a boxfill table entry used in VCS, or it can be
        used to change some or all of the attributes in an existing boxfill table entry.
        Other Useful Functions:</p>
        <pre>a=vcs.init() # Constructor

# Show predefined boxfill graphics methods
a.show('boxfill') 

# Change the VCS color map
a.setcolormap("AMIP") 

# Plot data 's' with boxfill 'b' and 'default' template
a.boxfill(s, b, 'default') 
# Updates the VCS Canvas at user's request
a.update() 
# If 1, then automatic update, else if 0, then use the update function to update the VCS Canvas.
a.mode=1, or 0</pre>
        <p>See <a herf="vcs-6.html#boxfill">Chapter 6</a> for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li>name</li>

          <li>projection</li>

          <li>xticlabels1</li>

          <li>xticlabels2</li>

          <li>xmtics1</li>

          <li>xmtics2</li>

          <li>yticlabels1</li>

          <li>yticlabels2</li>

          <li>ymtics1</li>

          <li>ymtics2</li>

          <li>datawc_x1</li>

          <li>datawc_y1</li>

          <li>datawc_x2</li>

          <li>datawc_y2</li>

          <li>xaxisconvert</li>

          <li>yaxisconvert</li>

          <li>level_1</li>

          <li>level_2</li>

          <li>color_1</li>

          <li>color_2</li>

          <li>legend_type</li>

          <li>legend</li>

          <li>ext_1</li>

          <li>ext_2</li>

          <li>missing</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of boxfill use:
    box=a.createboxfill('new','quick')
# Copies content of 'quick' to 'new'
box=a.createboxfill('new')
# Copies content of 'default' to 'new'

# To Modify an existing boxfill use: box=a.getboxfill('AMIP_psl') box.list()
# Will list all the boxfill attribute values
box.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'} box.xticlabels1=lon30 box.xticlabels2=lon30 box.xticlabels(lon30, lon30)
# Will set them both
box.xmtics1=''
box.xmtics2=''
box.xmtics(lon30, lon30)
# Will set them both
box.yticlabels1=lat10 box.yticlabels2=lat10
box.yticlabels(lat10, lat10)
# Will set them both
box.ymtics1='' box.ymtics2='' box.ymtics(lat10, lat10)
# Will set them both
box.datawc_y1=-90.0 box.datawc_y2=90.0 box.datawc_x1=-180.0 box.datawc_x2=180.0 box.datawc(-90,90,-180,180)
box.exts('n', 'y' )
# Will set them both
# Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
box.xyscale('linear', 'area_wt')
# Will set them both
level_1=1e20
level_2=1e20
box.levels(10, 90)
# Will set them both
color_1=16
color_2=239
box.colors(16, 239 )
# Will set them both
legend_type='VCS'
legend=''
ext_1='n'
ext_2='y'
missing=241
# Color index value range 0 to 255

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="continents" ></a>Continents</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createcontinents"></a>createcontinents</code></td>

      <td>
        

        <p>Create a new continents graphics method given the name and the existing
        continents graphics method to copy the attributes from. If no existing continents
        graphics method name is given, then the default continents graphics method will
        be used as the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new continents name</p></li>
          <li>[name of continents to copy from]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('continents')
con=a.createcontinents('example1',)
a.show('continents')
con=a.createcontinents('example2','quick')
a.show('continents')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getcontinents" ></a>getcontinents</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a
        continents class object from an existing VCS continents graphics method. If no
        continents name is given, then continents 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createcontinents function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[continents name]</p> </li>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('continents')
# Show all the existing continents graphics methods
con=a.getcontinents()
# con instance of 'default' continents graphics method
con2=a.getcontinents('quick')
# con2 instance of existing 'quick' continents graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: continentsobject</p>

        

        <p>The Continents graphics method draws a predefined, generic set of continental
        outlines in a longitude by latitude space. (To draw continental outlines, no
        external data set is required.)</p>

        <p>This class is used to define an continents table entry used in VCS, or it can
        be used to change some or all of the continents attributes in an existing
        continents table entry.</p>

        <p>Other Useful Functions:</p>

        <p><code>a=vcs.init()</code> Constructor</p>

        <p><code>a.show('continents')</code> Show predefined boxfill graphics methods</p>

        <p><code>a.show('line')</code> Show predefined line class objects</p>

        <p><code>a.setcolormap("AMIP")</code> Change the VCS color map</p>

        <p><code>a.continents(c,'default')</code> Plot continents, where 'c' is the defined continents
        object</p>

        <p><code>a.update()</code> Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>

        <p>See <a href="vcs-6.html#continents">Chapter 6</a> for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>type</p></li>
        </ul>
      </td>
      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of continents use:
    con=a.createcontinents('new','quick')
#copies content of 'quick' to 'new'
con=a.createcontinents('new')
# copies content of 'default' to 'new'

# To Modify an existing continents use:
    con=a.getcontinents('AMIP_psl')
con.list()
# Will list all the continents attribute values
con.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
con.xticlabels1=lon30
con.xticlabels2=lon30
con.xticlabels(lon30, lon30)
# Will set them both
con.xmtics1=''
con.xmtics2=''
con.xmtics(lon30, lon30)
# Will set them both
con.yticlabels1=lat10
con.yticlabels2=lat10
con.yticlabels(lat10, lat10)
# Will set them both
con.ymtics1=''
con.ymtics2=''
con.ymtics(lat10, lat10)
# Will set them both
con.datawc_y1=-90.0
con.datawc_y2=90.0
con.datawc_x1=-180.0
con.datawc_x2=180.0
con.datawc(-90, 90, -180, 180) # Will set them all
# Specify the continents line style (or type):
    con.line=0 # Same as con.line='solid'
con.line=1 # Same as con.line='dash'
con.line=2 # Same as con.line='dot'
con.line=3 # Same as con.line='dash-dot'
con.line=4 # Same as con.line='long-dash'
# There are three possibilities for setting the line #color indices (Ex):
    con.linecolor=22 # Same as con.line-color=(22)
con.linecolor=([22])
# Will set the continents to a specific color index
con.linecolor=None # Turns off the line color index, defaults to Black

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="isofill" ></a>Isofill</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createisofill" ></a>createisofill</code></td>

      <td>
        

        <p>Create a new isofill graphics method given the name and the existing isofill
        graphics method to copy the attributes from. If no existing isofill graphics
        method name is given, then the default isofill graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new isofill name</p> </lI>
          <li> <p>[name of isofill to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('isofill')
iso=a.createisofill('example1',)
a.show('isofill')
iso=a.createisofill('example2','quick')
a.show('isofill')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getisofill" ></a>getisofill</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a isofill
        class object from an existing VCS isofill graphics method. If no isofill name is
        given, then isofill 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createisofill function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[isofill name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('isofill')
# Show all the existing isofill graphics methods
iso=a.getisofill()
# iso instance of 'default' isofill graphics method
iso2=a.getisofill('quick')
# iso2 instance of existing 'quick' isofill graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: isofillobject</p>

        

        <p>The Isofill graphics method fills the area between selected isolevels (levels
        of constant value) of a two-dimensional array with a user-specified color. The
        example below shows how to display an isofill plot on the VCS Canvas and how to
        create and remove isofill isolevels.</p>

        <p>This class is used to define an isofill table entry used in VCS, or it can be
        used to change some or all of the isofill attributes in anexisting isofill table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p><code>a=vcs.init()</code> Constructor</p>

        <p><code>a.show('isofill')</code> Show predefined isofill graphics methods</p>

        <p><code>a.show('fillarea')</code> Show predefined fillarea objects</p>

        <p><code>a.show('template')</code> Show predefined fillarea objects</p>

        <p><code>a.setcolormap("AMIP")</code> Change the VCS color map</p>

        <p><code>a.createtemplate('test')</code> Create a template</p>

        <p><code>a.createfillarea('fill')</code> Create a fillarea</p>

        <p><code>a.gettemplate('AMIP')</code> Get an existing template</p>

        <p><code>a.getfillarea('def37')</code> Get an existing fillarea</p>

        <p><code>a.isofill(s,i,t)</code> Plot array 's' with isofill 'i' and template 't'</p>

        <p><code>a.update()</code> Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS Canvas.</p>

        <p>See <a href="vcs-6.html#isofill">Chapter 6</a> for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>missing</p></li>
          <li><p>ext_1</p></li>
          <li><p>ext_2</p></li>
          <li><p>fillareaindices</p></li>
          <li><p>fillareastyle</p></li>
          <li><p>fillareacolors</p></li>
          <li><p>levels</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of isofill use:
    iso=a.createisofill('new','quick')
# Copies content of 'quick' to 'new'
iso=a.createisofill('new')
# Copies content of 'default' to 'new'

# To Modify an existing isofill use:
    iso=a.getisofill('AMIP_psl')

iso.list()
# Will list all the isofill attribute values
iso.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
iso.xticlabels1=lon30
iso.xticlabels2=lon30
iso.xticlabels(lon30, lon30)
# Will set them both
iso.xmtics1=''
iso.xmtics2=''
iso.xmtics(lon30, lon30)
# Will set them both
iso.yticlabels1=lat10
iso.yticlabels2=lat10
iso.yticlabels(lat10, lat10)
# Will set them both
iso.ymtics1=''
iso.ymtics2=''
iso.ymtics(lat10, lat10)
# Will set them both
iso.datawc_y1=-90.0
iso.datawc_y2=90.0
iso.datawc_x1=-180.0
iso.datawc_x2=180.0
iso.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
iso.xyscale('linear', 'area_wt') # Will set them both
missing=241 # Color index value range 0 to 255
# There are two possibilities for setting the isofill levels:
    # A) Levels are all contiguous (Examples):
    iso.levels=([0,20,25,30,35,40],)
iso.levels=([0,20,25,30,35,40,45,50])
iso.levels=[0,20,25,30,35,40]
iso.levels=(0.0,20.0,25.0,30.0,35.0,40.0,50.0)
# B) Levels are not contiguous (Examples):
    iso.levels=([0,20],[30,40],[50,60])
iso.levels=([0,20,25,30,35,40],[30,40],[50,60])
iso.fillareaindices=(7,fill,4,9,fill,15) # Set index using fillarea
fill.list() # list fillarea attributes
fill.style='hatch' # change style
fill.color=241 # change color
fill.index=3 # change style index

ext_1='n'
ext_2='y'
iso.exts('n', 'y' ) # Will set them both

# There are three possibilities for setting the fillarea color indices (Ex):
    iso.fillareacolors=([22,33,44,55,66,77])
iso.fillareacolors=(16,19,33,44)
iso.fillareacolors=None

# There are three possibilities for setting the fillarea style (Ex):
    iso.fillareastyle = 'solid'
iso.fillareastyle = 'hatch'
iso.fillareastyle = 'pattern'
# There are two ways to set the fillarea hatch or pattern indices (Ex):
    iso.fillareaindices=([1,3,5,6,9,20])
iso.fillareaindices=(7,1,4,9,6,15)
See using fillarea objects below!

# Using the fillarea secondary object (Ex):
    f=createfillarea('fill1')
# To Create a new instance of fillarea use:
    fill=a.createisofill('new','quick') # Copies 'quick' to 'new'
fill=a.createisofill('new') # Copies 'default' to 'new'

# To Modify an existing isofill use:
    fill=a.getisofill('def37')

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="isoline" ></a>Isoline</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createisoline" ></a>createisoline</code></td>

      <td>
        

        <p>Create a new isoline graphics method given the name and the existing isoline
        graphics method to copy the attributes from. If no existing isoline graphics
        method name is given, then the default isoline graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned.
        Graphicsmethod names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new isoline name</p></li>
          <li><p>[name of isoline to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('isoline')
iso=a.createisoline('example1',)
a.show('isoline')
iso=a.createisoline('example2','quick')
a.show('isoline')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getisoline" ></a>getisoline</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a isoline
        class object from an existing VCS isoline graphics method. If no isoline name is
        given, then isoline 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createisoline function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[isoline name]</p> </li> 
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('isoline')
# Show all the existing isoline graphics methods
iso=a.getisoline()
# iso instance of 'default' isoline graphics method
iso2=a.getisoline('quick')
# iso2 instance of existing 'quick' isoline graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: isolineobject</p>

        <p>The Isoline graphics method draws lines of constant value at specified levels
        in order to graphically represent a two-dimensional array. It also labels the
        values of these isolines on the VCS Canvas. The example below shows how to plot
        isolines of different types at specified levels and how to create isoline labels
        having user-specified text and line type and color.</p>

        <p>This class is used to define an isoline table entry used in VCS, or it can be
        used to change some or all of the isoline attributes in an existing isoline table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('isoline') Show predefined isoline graphics methods</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.update() Updates the VCS Canvas at user's request</p>

        <p>a.mode=1, or 0 If 1, then automatic update, else if 0, then use update
        function.</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.isoline(s,a,'default') Plot data 's' with isoline 'i' and 'default'
        template</p>

        <p>tion to update the VCS Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>label</p></li>
          <li><p>line</p></li>
          <li><p>linecolors</p></li>
          <li><p>text</p></li>
          <li><p>textcolors</p></li>
          <li><p>level</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of isoline use:
    iso=a.createisoline('new','quick')
# Copies content of 'quick' to 'new'
iso=a.createisoline('new')
# Copies content of 'default' to 'new'

# To Modify an existing isoline use:
    iso=a.getisoline('AMIP_psl')
iso.list()
# Will list all the isoline attribute values
iso.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
iso.xticlabels1=lon30
iso.xticlabels2=lon30
iso.xticlabels(lon30, lon30)
# Will set them both
iso.xmtics1=''
iso.xmtics2=''
iso.xmtics(lon30, lon30)
# Will set them both
iso.yticlabels1=lat10
iso.yticlabels2=lat10
iso.yticlabels(lat10, lat10)
# Will set them both
iso.datawc_y1=-90.0
iso.datawc_y2=90.0
iso.datawc_x1=-180.0
iso.datawc_x2=180.0
iso.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
iso.xyscale('linear', 'area_wt') # Will set them both
# There are many possibilities ways to set the isoline values:
    # A) As a list of tuples (Examples):
    iso.level=[(23,32,45,50,76),]
iso.level=[(22,33,44,55,66)]
iso.level=[(20,0.0),(30,0),(50,0)]
iso.level=[(23,32,45,50,76), (35, 45, 55)]
# B) As a tuple of lists (Examples):
    iso.level=([23,32,45,50,76],)
iso.level=([22,33,44,55,66])
iso.level=([23,32,45,50,76],)
iso.level=([0,20,25,30,35,40],[30,40],[50,60]
)
# C) As a list of lists (Examples):
    iso.level=[[20,0.0],[30,0],[50,0]]
# D) As a tuple of tuples (Examples):
    iso.level=((20,0.0),(30,0),(50,0),(60,0),(70,0))
# Note: a combination of a pair (i.e., (30,0) or [30,0]) represents the isoline value plus it increment value. Thus, to let VCS generate "default" isolines enter the following:
    iso.level=[[0,1e20]]
# Same as iso.level=((0,1e20),)

Displaying isoline labels:
    iso.label='y'
# Same as iso.label=1, will display isoline labels
iso.label='n'
# Same as iso.label=0, will turn isoline labels off
# color index
iso.linecolors=None # Turns off the line color index

There are three ways to specify the text or font number:
    iso.text=(1,2,3,4,5,6,7,8,9) # Font numbers are between 1 and 9
iso.text=[9,8,7,6,5,4,3,2,1]
iso.text=([1,3,5,6,9,2])
iso.text=None # Removes the text settings
There are three possibilities for setting the text color indices (Ex.):
    iso.textcolors=([22,33,44,55,66,77])
iso.textcolors=(16,19,33,44)
iso.textcolors=None # Turns off the text color index
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="outfill" ></a>Outfill</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createoutfill" ></a>createoutfill</code></td>

      <td>
        

        <p>Create a new outfill graphics method given the name and the existing outfill
        graphics method to copy the attributes from. If no existing outfill graphics
        method name is given, then the default outfill graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new outfill name</p></li>
          <li> <p>[name of outfill to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('outfill')
out=a.createoutfill('example1',)
a.show('outfill')
out=a.createoutfill('example2','quick')
a.show('outfill')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getoutfill" ></a>getoutfill</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a outfill
        class object from an existing VCS outfill graphics method. If no outfill name is
        given, then outfill 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createoutfill function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[outfill name]</p> </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('outfill')
# Show all the existing outfill graphics methods
out=a.getoutfill()
# out instance of 'default' outfill graphics method
out2=a.getoutfill('quick')
# out2 instance of existing 'quick' outfill graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: outfillobject</p>

        

        <p>The outfill graphics method fills a set of integer values in any data
        array.</p>

        <p>Its primary purpose is to display continents by filling their area as defined
        by a surface type array that indicates land, ocean, and sea-ice points. The
        example below shows how to apply the outfill graphics method and how to
        modify</p>

        <p>Fillarea and outfill attributes. Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('outfill') Show predefined outfill graphics methods</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.outfill(s,o,'default') Plot data 's' with outfill 'o' and 'default'
        template</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1,
        then automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>fillareastyle</p></li>
          <li><p>fillareaindex</p></li>
          <li><p>fillareacolor</p></li>
          <li><p>outfill</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of outfill use:
    out=a.createoutfill('new','quick')
# Copies content of 'quick' to 'new'
out=a.createoutfill('new')
# Copies content of 'default' to 'new'


# To Modify an existing outfill use:
    out=a.getoutfill('AMIP_psl')
out.list()
# Will list all the outfill attribute values
out.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
out.xticlabels1=lon30
out.xticlabels2=lon30
out.xticlabels(lon30, lon30)
# Will set them both
out.xmtics1=''
out.xmtics2=''
out.xmtics(lon30, lon30)
# Will set them both
out.yticlabels1=lat10
out.yticlabels2=lat10
out.yticlabels(lat10, lat10)
# Will set them both
out.datawc_y1=-90.0
out.datawc_y2=90.0
out.datawc_x1=-180.0
out.datawc_x2=180.0
out.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
out.xyscale('linear', 'area_wt') # Will set them both
# Specify the outfill fill values:
    out.outfill=([0,1,2,3,4]) # Same as below
out.outfill=(0,1,2,3,4) # Will specify the outfill values
# There are four possibilities for setting the color index (Ex):
    out.fillareacolor=22 # Same as below
out.fillareacolor=(22) # Same as below
out.fillareacolor=([22]) # Will set the outfill to a specific color index
out.fillareacolor=None # Turns off the color index

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="outline" ></a>Outline</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createoutline" ></a>createoutline</code></td>

      <td>
        

        <p>Create a new outline graphics method given the name and the existing outline
        graphics method to copy the attributes from. If no existing outline graphics
        method name is given, then the default outline graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new outline name</p> </li>
          <li> <p>[name of outline to copy attributes from]</p> </li>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('outline')
out=a.createoutline('example1',)
a.show('outline')
out=a.createoutline('example2','quick')
a.show('outline')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getoutline" ></a>getoutline</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a outline
        class object from an existing VCS outline graphics method. If no outline name is
        given, then outline 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createoutline function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[outline name]</p></li>
        </ul>
       </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('outline')
# Show all the existing outline graphics methods
out=a.getoutline()
# out instance of 'default' outline graphics method
out2=a.getoutline('quick')
# out2 instance of existing 'quick' outline graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: outlineobject</p>

        

        <p>The Outline graphics method outlines a set of integer values in any data
        array.</p>

        <p>Its primary purpose is to display continental outlines as defined by a
        surface</p>

        <p>type array that indicates land, ocean, and sea-ice points. The example
        below</p>

        <p>shows how to change such an outline by modifying its attributes.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('outline') Show predefined outline graphics methods</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.outline(s,o,'default') Plot data 's' with outline 'o' and 'default'
        template</p>

        <p>a.update()</p>

        <p>Updates the VCS Canvas at user's request a.mode=1, or 0 # If 1, then automatic
        update, else if 0, then use u pdate function to update the VCS Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>outline</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of outline use:
    out=a.createoutline('new','quick')
# Copies content of 'quick' to 'new'
out=a.createoutline('new')
# Copies content of 'default' to 'new'


# To Modify an existing outline use:
    out=a.getoutline('AMIP_psl')
out.list()
# Will list all the outline attribute values
out.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
out.xticlabels1=lon30
out.xticlabels2=lon30
out.xticlabels(lon30, lon30)
# Will set them both
out.xmtics1=''
out.xmtics2=''
out.xmtics(lon30, lon30)
# Will set them both
out.yticlabels1=lat10
out.yticlabels2=lat10
out.yticlabels(lat10, lat10)
# Will set them both
out.ymtics1=''
out.ymtics2=''
out.ymtics(lat10, lat10)
# Will set them both
 xyvsyobjectout.datawc_y1=-90.0
out.datawc_y2=90.0
out.datawc_x1=-180.0
out.datawc_x2=180.0
out.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
out.xyscale('linear', 'area_wt') # Will set them both
# Specify the outline fill values:
    out.outline=([0,1,2,3,4]) # Same as below
out.outline=(0,1,2,3,4) # Will specify the outline values
# Specify the outline line type:
    out.line=0 # same as out.line = 'solid'
out.line=1 # same as out.line = 'dash'
out.line=2 # same as out.line = 'dot'
out.line=3
# same as out.line = 'dash-dot'
out.line=4 # same as out.line = 'long-dash'

# There are four possibilities for setting the line color index (Ex):
    out.linecolor=22 # Same as below
# Same as below
out.linecolor=([22]) # Will set the outline to a specific color index
out.linecolor=None # Turns off the color index

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="scatter" ></a>Scatter</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createscatter" ></a>createscatter</code></td>

      <td>
        

        <p>Create a new scatter graphics method given the name and the existing mscatter
        graphics method to copy the attributes from. If no existing scatter graphics
        method name is given, then the default scatter graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique</p>
      </td>

      <td>
        <ul>
          <li> <p>new scatter name</p> </li>
          <li><p>[name of scatter to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('scatter')
sct=a.createscatter('example1',)
a.show('scatter')
sct=a.createscatter('example2','quick')
a.show('scatter')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getscatter" ></a>getscatter</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a scatter
        class object from an existing VCS scatter graphics method. If no scatter name is
        given, then scatter 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createscatter function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[scatter name]</p> </li>
        </uL>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('scatter')
# Show all the existing scatter graphics methods
sct=a.getscatter()
# sct instance of 'default' scatter graphics method
sct2=a.getscatter('quick')
# sct2 instance of existing 'quick' scatter graphics method

</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: scatterobject</p>

        

        <p>The Scatter graphics method displays a scatter plot of two 4-dimensional data
        arrays, e.g. A(x,y,z,t) and B(x,y,z,t). The example below shows how to change the
        marker attributes of a scatter plot.</p>

        <p>This class is used to define an scatter table entry used in VCS, or it can be
        used to change some or all of the scatter attributes in an existing scatter table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('scatter') Show predefined scatter graphics methods</p>

        <p>a.show('marker') Show predefined marker objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.scatter(s1, s2, s,'default') Plot data 's1' and 's2' with scatter 's' and
        'default' template</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>

          <li><p>projection</p></li>

          <li><p>xticlabels1</p></li>

          <li><p>xticlabels2</p></li>

          <li><p>xmtics1</p></li>

          <li><p>xmtics2</p></li>

          <li><p>yticlabels1</p></li>

          <li><p>yticlabels2</p></li>

          <li><p>ymtics1</p></li>

          <li><p>ymtics2</p></li>

          <li><p>datawc_x1</p></li>

          <li><p>datawc_y1</p></li>

          <li><p>datawc_x2</p></li>

          <li><p>datawc_y2</p></li>

          <li><p>xaxisconvert</p></li>

          <li><p>yaxisconvert</p></li>

          <li><p>marker</p></li>

          <li><p>markercolor</p></li>

          <li><p>markersize</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of scatter use:
    sr=a.createscatter('new','quick')
# copies content of 'quick' to 'new'
sr=a.createscatter('new')
# copies content of 'default' to 'new'

# To Modify an existing scatter use:
    sr=a.getscatter('AMIP_psl')
sr.list()
# Will list all the scatter attribute values
sr.projection='linear'
# Can only be 'linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
sr.xticlabels1=lon30
sr.xticlabels2=lon30
sr.xticlabels(lon30, lon30)
# Will set them both
sr.xmtics1=''
sr.xmtics2=''
sr.xmtics(lon30, lon30)
# Will set them both
sr.yticlabels1=lat10
sr.yticlabels2=lat10
sr.yticlabels(lat10, lat10)
# Will set them both
sr.ymtics1=''
sr.ymtics2=''
sr.ymtics(lat10, lat10)
# Will set them both
sr.datawc_y1=-90.0
sr.datawc_y2=90.0
sr.datawc_x1=-180.0
sr.datawc_x2=180.0
sr.datawc(-90, 90, -180, 180) # Will set them all
sr.xaxisconvert='linear'
sr.yaxisconvert='linear'
sr.xyscale('linear', 'area_wt') # Will set them both
# Specify the marker type:
    sr.marker=1 # Same as sr.marker='dot'
sr.marker=2 # Same as sr.marker='plus'
sr.marker=3 # Same as sr.marker='star'
sr.marker=4 # Same as sr.marker='circle'
sr.marker=5 # Same as sr.marker='cross'
sr.marker=6 # Same as sr.marker='diamond'
sr.marker=7
# Same as sr.marker='triangle_up'
sr.marker=8 # Same as sr.marker='triangle_down'
sr.marker=9 # Same as sr.marker='triangle_left'
sr.marker=10 # Same as sr.marker='triangle_right'
sr.marker=11 # Same as sr.marker='square'
sr.marker=12 # Same as sr.marker='diamond_fill'
sr.marker=13 # Same as sr.marker='triangle_up_fill'
sr.marker=14 # Same as sr.marker='triangle_down_fill'
sr.marker=15 # Same as sr.marker='triangle_left_fill'
sr.marker=16
# Same as below
sr.markercolors=(22) # Same as below
sr.markercolors=([22]) # Will set the markers to a specific
# color index
sr.markercolors=None # Color index defaults to Black

#To set the Marker sizie:
    sr.markersize=5
sr.markersize=55
sr.markersize=100
sr.markersize=300
sr.markersize=None

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="vector" ></a>Vector</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createvector" ></a>createvector</code></td>

      <td>
        

        <p>Create a new vector graphics method given the name and the existing vector
        graphics method to copy the attributes from. If no existing vector graphics
        method name is given, then the default vector graphics method will be used as the
        graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new vector name</p> </li>
          <li> <p>[name of vector to copy attributes from]</p> </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('vector')
vec=a.createvector('example1',)
a.show('vector')
vec=a.createvector('example2','quick')
a.show('vector')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getvector" ></a>getvector</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a vector
        class object from an existing VCS vector graphics method. If no vector name is
        given, then vector 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createvector function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[vector name]</p> </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('vector')
# Show all the existing vector graphics methods
vec=a.getvector()
# vec instance of 'default' vector graphics method
vec2=a.getvector('quick')
# vec2 instance of existing 'quick' vector graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: vectorobject</p>

        

        <p>The vector graphics method displays a vector plot of a 2D vector field.
        Vectors</p>

        <p>are located at the coordinate locations and point in the direction of the data
        vector field. Vector magnitudes are the product of data vector field lengths and
        a scaling factor. The example below shows how to modify the vector's line, scale,
        alignment, type, and reference.</p>

        <p>This class is used to define an vector table entry used in VCS, or it can be
        used to change some or all of the vector attributes in an existing vector table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('vector') Show predefined vector graphics methods</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color Map</p>

        <p>a.vector(s1, s2, v,'default') Plot data 's1', and 's2' with vector 'v' and
        'default' template</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>scale</p></li>
          <li><p>alignment</p></li>
          <li><p>type</p></li>
          <li><p>reference</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of vector use:
    vc=a.createvector('new','quick')
# Copies content of 'quick' to 'new'
vc=a.createvector('new')
# Copies content of 'default' to 'new'

# To Modify an existing vector use:
    vc=a.getvector('AMIP_psl')
vc.list()
# Will list all the vector attribute values
vc.projection='linear'
# Can only be 'linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
vc.xticlabels1=lon30
vc.xticlabels2=lon30
vc.xticlabels(lon30, lon30)
# Will set them both
vc.xmtics1=''
vc.xmtics2=''
vc.xmtics(lon30, lon30)
# Will set them both
vc.yticlabels1=lat10
vc.yticlabels2=lat10
vc.yticlabels(lat10, lat10)
# Will set them both
vc.ymtics1=''
vc.ymtics2=''
vc.ymtics(lat10, lat10)
# Will set them both
vc.datawc_y1=-90.0
vc.datawc_y2=90.0
vc.datawc_x1=-180.0
vc.datawc_x2=180.0
vc.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
vc.xyscale('linear', 'area_wt') # Will set them both
# Specify the line style:
    vc.line=0 # Same as vc.line='solid'
vc.line=1 # Same as vc.line='davc.line=2 # Same as vc.line='dot'
vc.line=3 # Same as vc.line='dash-dot'
vc.line=4 # Same as vc.line='long-dot'
# Specify the line color of the vectors:
    vc.linecolor=16
# Color range: 16 to 230, default line color is black
# Specify the vector scale factor:
    vc.scale=2.0 # Can be an integer or float
# Specify the vector alignment:
    vc.alignment=0
# Same as vc.alignment='head'
vc.alignment=1 # Same as vc.alignment='center'
vc.alignment=2 # Same as vc.alignment='tail'
# Specify the vector type:
    vc.type=0 # Same as vc.type='arrow head'
vc.type=1 # Same as vc.type='wind barbs'
vc.type=2 # Same as vc.type='solid arrow head'

Specify the vector reference:
    vc.reference=4 # Can be an integer or float

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="xvsy" ></a>XvsY</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createxvsy" ></a>createxvsy</code></td>

      <td>
        

        <p>Create a new XvsY graphics method given the name and the existing XvsY
        graphics method to copy the attributes from. If no existing XvsY graphics method
        name is given, then the default XvsY graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new xvsy name</p> </li>
          <li> <p>[name of xvsy to copy attributes from]</p>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xvsy')
xy=a.createxvsy('example1',)
a.show('xvsy')
xy=a.createxvsy('example2','quick')
a.show('xvsy')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getxvsy" ></a>getxvsy</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a XvsY
        class object from an existing VCS XvsY graphics method. If no XvsY name is given,
        then XvsY 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createxvsy function.)</p>
      </td>

      <td>
        <ul>
          <li> <p>[xvsy name]</p> </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xvsy')
# Show all the existing XvsY xy=a.getxvsy()
# graphics methods xy instance of 'default' XvsY graphics method
xy2=a.getxvsy('quick')
# xy2 instance of existing 'quick' XvsY graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: xvsyobject</p>

        

        <p>The XvsY graphics method displays a line plot from two 1D data arrays, that is
        X(t) and Y(t), where t represents the 1D coordinate values. The example below
        shows how to change line and marker attributes for the XvsY graphics method.</p>

        <p>This class is used to define an XvsY table entry used in VCS, or it can be
        used to change some or all of the XvsY attributes in an existing XvsY table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('xvsy') Show predefined XvsY graphics methonds</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.show('marker') Show predefined VCS marker objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.xvsy(s1, s2, ,x,'default') Plot data 's1' and 's2' with XvsY 'x' and
        'default' template</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to Update the VCS
        Canvas.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>marker</p></li>
          <li><p>markercolor</p></li>
          <li><p>markersize</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of XvsY use:
    xy=a.createxvsy('new','quick')
# Copies content of 'quick' to 'new'
xy=a.createxvsy('new')
# Copies content of 'default' to 'new'

# To Modify an existing XvsY use:
    xy=a.getxvsy('AMIP_psl')
xy.list()
# Will list all the XvsY attribute values
xy.projection='linear'
# Can only be 'linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
xy.xticlabels1=lon30
xy.xticlabels2=lon30
xy.xticlabels(lon30, lon30)
# Will set them both
xy.xmtics1=''
xy.xmtics2=''
xy.xmtics(lon30, lon30)
# Will set them both
xy.yticlabels1=lat10
xy.yticlabels2=lat10
xy.yticlabels(lat10, lat10)
# Will set them both
xy.datawc_y1=-90.0
xy.datawc_y2=90.0
xy.datawc_x1=-180.0
xy.datawc_x2=180.0
xy.datawc(-90, 90, -180, 180) # Will set them all
xaxisconvert='linear'
yaxisconvert='linear'
xy.xyscale('linear', 'area_wt') # Will set them both
# Specify the XvsY line type:
    xy.line=0 # same as xy.line = 'solid'
xy.line=1 # same as xy.line = 'dash'
xy.line=2 # same as xy.line = 'dot'
xy.line=3 # same as xy.line = 'dash-dot'
xy.line=4 # same as xy.line = 'long-dash
# Specify the Xvsy line color:
    xy.line# color range: 16 to 230, default color is black
# Specify the XvsY marker type:
    xy.marker=1 # Same as xy.marker='dot'
xy.marker=2 # Same as xy.marker='plus'
xy.marker=3
color=16 # color index
# Same as xy.marker='star'
xy.marker=4 # Same as xy.marker='circle'
xy.marker=5 # Same as xy.marker='cross'
xy.marker=6 # Same as xy.marker='diamond'
xy.marker=7 # Same as xy.marker='triangle_up'
xy.marker=8 # Same as xy.marker='triangle_down'
xy.marker=9 # Same as xy.marker='triangle_left'
xy.marker=10 # Same as xy.marker='triangle_right'
xy.marker=11 # Same as xy.marker='square'
xy.marker=12
# Same as xy.marker='square'
xy.marker=12 # Same as xy.marker='diamond_fill'
xy.marker=13 # Same as xy.marker='triangle_up_fill'
xy.marker=14 # Same as xy.marker='triangle_down_fill'
xy.marker=15 # Same as xy.marker='triangle_left_fill'
xy.marker=16 # Same as xy.marker='triangle_right_fill'
xy.marker=17 # Same as xy.marker='square_fill'
xy.marker=None # Draw no markers
</pre>

        <p>There are four possibilities for setting the marker color index
        (<strong>Example</strong>):</p>
        <pre style="word-break:normal;">
xy.markercolors=22 # Same as below
xy.markercolors=(22) # Same as below
xy.markercolors=([22]) # Will set the markers to a specific
xy.markercolors=None # Color index defaults to Black
</pre>

        <p>To set the XvsY Marker sizie:</p>
        <pre style="word-break:normal;">
xy.markersize=5
xy.markersize=55
xy.markersize=100
xy.markersize=300
xy.markersize=None
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="xyvsy" ></a>Xyvsy</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createxyvsy" ></a>createxyvsy</code></td>

      <td>
        

        <p>Create a new Xyvsy graphics method given the name and the existing Xyvsy
        graphics method to copy the attributes from. If no existing Xyvsy graphics method
        name is given, then the default Xyvsy graphics method will be used as the
        graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li> <p>new xyvsy name</p> </li>
          <li> <p>[name of xyvsy to copy attributes from]</p> </li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xyvsy')
xyy=a.createxyvsy('example1',)
a.show('xyvsy')
xyy=a.createxyvsy('example2','quick')
a.show('xyvsy')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getxyvsy" ></a>getxyvsy</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a Xyvsy
        class object from an existing VCS Xyvsy graphics method. If no Xyvsy name is
        given, then Xyvsy 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createxyvsy function.)</p>
      </td>

      <td>
        <p>[xyvsy name]</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('xyvsy')
# Show all the existing Xyvsy graphics methods
xyy=a.getxyvsy()
# xyy instance of 'default' Xyvsy graphics method
xyy2=a.getxyvsy('quick')
# xyy2 instance of existing 'quick' Xyvsy graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: xyvsyobject</p>

        

        <p>The Xyvsy graphics method displays a line plot from a 1D data array (i.e. a
        plot of X(y), where y represents the 1D coordinate values). The example below
        ributes for the Xyvsy graphics method.</p>

        <p>This class is used to define an Xyvsy table entry used in VCS, or it can be
        used to change some or all of the Xyvsy attributes in an existing Xyvsy table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('xyvsy') Show predefined Xyvsy graphics methonds</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.show('marker') Show predefined VCS marker objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.xyvsy(s, x, 'default') Plot data 's' with Xyvsy 'x' and 'default'
        template</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1,
        then automatic update, else if 0, then use update function.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>xaxisconvert</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>marker</p></li>
          <li><p>markercolor</p></li>
          <li><p>markersize</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of Xyvsy use:
    xyy=a.createxyvsy('new','quick')
# Copies content of 'quick' to 'new'
xyy=a.createxyvsy('new')
# Copies content of 'default' to 'new'

# To Modify an existing Xyvsy use:
    xyy=a.getxyvsy('AMIP_psl')
xyy.list()
# Will list all the Xyvsy attribute values
xyy.projection='linear'
# Can only be 'linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
xyy.xticlabels1=lon30
xyy.xticlabels2=lon30
xyy.xticlabels(lon30, lon30)
# Will set them both
xyy.xmtics1=''
xyy.xmtics2=''
xyy.xmtics(lon30, lon30)
# Will set them both
xyy.yticlabels1=lat10
xyy.yticlabels2=lat10
xyy.yticlabels(lat10, lat10)
# Will set them both
xyy.ymtics1=''
xyy.ymtics2=''
xyy.ymtics(lat10, lat10)
# Will set them both
xyy.datawc_y1=-90.0
xyy.datawc_y2=90.0
xyy.datawc_x1=-180.0
xyy.datawc_x2=180.0
xyy.datawc(-90, 90, -180, 180) # Will set them all
xyy.xaxisconvert='linear'
# Specify the Xyvsy line type:
    xyy.line=0 # same as xyy.line = 'solid'
xyy.line=1 # same as xyy.line = 'dash'
xyy.line=2 # same as xyy.line = 'dot'
xyy.line=3
same as xyy.line = 'dash-dot'
xyy.line=4 # same as xyy.line = 'long-dash
# Specify the Xyvsy line color:
    xyy.linecolor=16 # color range: 16 to 230, default color is black
# Specify the Xyvsy marker type:
    xyy.marker=1 # Same as xyy.marker='dot'
xyy.marker=2 # Same as xyy.marker='plus'
xyy.marker=3 # Same as xyy.marker='star'
xyy.marker=4
# Same as xyy.marker='circle'
xyy.marker=5 # Same as xyy.marker='cross'
xyy.marker=6 # Same as xyy.marker='diamond'
xyy.marker=7 # Same as xyy.marker='triangle_up'
xyy.marker=8 # Same as xyy.marker='triangle_down'
xyy.marker=9 # Same as xyy.marker='triangle_left'
xyy.marker=10 # Same as xyy.marker='triangle_right'
xyy.marker=11 # Same as xyy.marker='square'
xyy.marker=12 # Same as xyy.marker='diamond_fill'
xyy.marker=13
# Same as xyy.marker='triangle_up_fill'
xyy.marker=14 # Same as xyy.marker='triangle_down_fill'
xyy.marker=15 # Same as xyy.marker='triangle_left_fill'
xyy.marker=16 # Same as xyy.marker='triangle_right_fill'
xyy.marker=17 # Same as xyy.marker='square_fill'
xyy.marker=None # Draw no markers
</pre>

        <p>There are four possibilities for setting the marker color index (Ex):</p>
        <pre style="word-break:normal;">
xyy.markercolors=22 # Same as below
xyy.markercolors=(22) # Same as below
xyy.markercolors=([22]) # Will set the markers to a specific
# color index
xyy.markercolors=None # Color index defaults to Black
</pre>

        <p>To set the Xyvsy Marker sizie:</p>
        <pre style="word-break:normal;">
xyy.markersize=5
xyy.markersize=55
xyy.markersize=100
xyy.markersize=300
xyy.markersize=None
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="yxvsx" ></a>Yxvsx</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createyxvsx" ></a>createyxvsx</code></td>

      <td>
        

        <p>Create a new Yxvsx graphics method given the name and the existing Yxvsx
        graphics method to copy the attributes from. If no existing Yxvsx graphics method
        name is given, then the default Yxvsx graphics method will be used as the
        graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique</p>
      </td>

      <td>
        <ul>
          <li><p>new yxvsx name</p></li>
          <li><p>[name of yxvsx to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('yxvsx')
yxx=a.createyxvsx('example1',)
a.show('yxvsx')
yxx=a.createyxvsx('example2','quick')
a.show('yxvsx')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getyxvsx" ></a>getyxvsx</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a Yxvsx
        class object from an existing VCS Yxvsx graphics method. If no Yxvsx name is
        given, then Yxvsx 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createyxvsx function.)</p>
      </td>

      <td>
        <ul>
          <li><p>[yxvsx name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('yxvsx')
# Show all the existing Yxvsx graphics methods
yxx=a.getyxvsx()
# yxx instance of 'default' Yxvsx graphics method
yxx2=a.getyxvsx('quick')
# yxx2 instance of existing 'quick' Yxvsx graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: yxvsxobject</p>

        

        <p>The Yxvsx graphics method displays a line plot from a 1D data array (i.e.
        aplot of Y(x), where y represents the 1D coordinate values). The example
        belowshows how to change line and marker attributes for the Yxvsx graphics
        method.</p>

        <p>This class is used to define an Yxvsx table entry used in VCS, or it can
        beused to change some or all of the Yxvsx attributes in an existing Yxvsx table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('yxvsx') Show predefined Yxvsx graphics methonds</p>

        <p>a.show('line') Show predefined VCS line objects</p>

        <p>a.show('marker') Show predefined VCS marker objects</p>

        <p>a.setcolormap("AMIP") Change the VCS color map</p>

        <p>a.yxvsx(s, x, 'default') Plot data 's' with Yxvsx 'x' and 'default'
        template</p>

        <p>a.update() Updates the VCS Canvas at user's request</p>

        <p>a.mode=1, or 0 If 1, then automatic update, else if 0, then use update
        function.</p>

        <p>See Chapter 6 for additional information.</p>
      </td>

      <td>
        <p>Attributes:</p>
        <ul>
          <li><p>name</p></li>
          <li><p>projection</p></li>
          <li><p>xticlabels1</p></li>
          <li><p>xticlabels2</p></li>
          <li><p>xmtics1</p></li>
          <li><p>xmtics2</p></li>
          <li><p>yticlabels1</p></li>
          <li><p>yticlabels2</p></li>
          <li><p>ymtics1</p></li>
          <li><p>ymtics2</p></li>
          <li><p>datawc_x1</p></li>
          <li><p>datawc_y1</p></li>
          <li><p>datawc_x2</p></li>
          <li><p>datawc_y2</p></li>
          <li><p>yaxisconvert</p></li>
          <li><p>line</p></li>
          <li><p>linecolor</p></li>
          <li><p>marker</p></li>
          <li><p>markercolor</p></li>
          <li><p>markersize</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of Yxvsx use:
    yxx=a.createxyvsy('new','quick')
# Copies content of 'quick' to 'new'
yxx=a.createxyvsy('new')
# Copies content of 'default' to 'new'

# To Modify an existing Yxvsx use:
    yxx=a.getxyvsy('AMIP_psl')
yxx.list()
# Will list all the Yxvsx attribute values
yxx.projection='linear'
# Can only be 'linear'
lon30={-180:'180W',-150:'150W',0:'Eq'}
yxx.xticlabels1=lon30
yxx.xticlabels2=lon30
yxx.xticlabels(lon30, lon30)
# Will set them both
yxx.xmtics1=''
yxx.xmtics2=''
yxx.xmtics(lon30, lon30)
# Will set them both
yxx.yticlabels1=lat10
yxx.yticlabels2=lat10
yxx.yticlabels(lat10, lat10
# Will set them both
yxx.datawc_y1=-90.0
yxx.datawc_y2=90.0
yxx.datawc_x1=-180.0
yxx.datawc_x2=180.0
yxx.datawc(-90, 90, -180, 180) # Will set them all
yxx.yaxisconvert='linear'
# Specify the Yxvsx line type:
    yxx.line=0 # same as yxx.line = 'solid'
yxx.line=1 # same as yxx.line = 'dash'
yxx.line=2 # same as yxx.line = 'dot'
yxx.line=3
# same as yxx.line = 'dash-dot'
yxx.line=4 # same as yxx.line = 'long-dash
# Specify the Yxvsx line color:
    yxx.linecolor=16 # color range: 16 to 230, default color is black
yxx.linecolor=16 # color range: 16 to 230, default color is black
# Specify the Yxvsx marker type:
    yxx.marker=1 # Same as yxx.marker='dot'
yxx.marker=2 # Same as yxx.marker='plus'
yxx.marker=3 # Same as yxx.marker='star'
yxx.marker=4 # Same as yxx.marker='circle'
yxx.marker=5 # Same as yxx.marker='cross'
yxx.marker=6 # Same as yxx.marker='diamond'
yxx.marker=7 # Same as yxx.marker='triangle_up'
yxx.marker=8 # Same as yxx.marker='triangle_down'
yxx.marker=9 # Same as yxx.marker='triangle_left'
yxx.marker=10 # Same as yxx.marker='triangle_right'
yxx.marker=11 # Same as yxx.marker='square'
yxx.marker=12 # Same as yxx.marker='diamond_fill'
yxx.marker=13 # Same as yxx.marker='triangle_up_fill'
yxx.marker=14 # Same as yxx.marker='triangle_down_fill'
yxx.marker=15 # Same as yxx.marker='triangle_left_fill'
yxx.marker=16 # Same as yxx.marker='triangle_right_fill'
yxx.marker=17 # Same as yxx.marker='square_fill'
yxx.marker=None # Draw no markers
# There are four possibilities for setting the marker color index (Example):
    yxx.markercolors=22 # Same as below
yxx.markercolors=(22) # Same as below
yxx.markercolors=([22])
# Will set the markers to a specific color index
yxx.markercolors=None # Color index defaults to Black
# To set the Yxvsx Marker size:
    yxx.markersize=5
yxx.markersize=55
yxx.markersize=100
yxx.markersize=300
yxx.markersize=None
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="3d_scalar"></a>3D Scalar</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="create3d_scalar"></a>create3d_scalar</code></td>

      <td>
        

        <p>Create a new Yxvsx graphics method given the name and the existing Yxvsx
        graphics method to copy the attributes from. If no existing Yxvsx graphics method
        name is given, then the default Yxvsx graphics method will be used as the
        graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique</p>
      </td>

      <td>
        <ul>
          <li>new 3d_scalar name</li>

          <li>[existing 3d_vector to copy attributes from]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('3d_scalar')
# Show all the existing 3d_scalar graphics methods
scalar = a.create3d_scalar('quick')
# scalar is a new 3d_scalar that copies the 'default' 3d_scalar graphics method
scalar2 = a.create3d_scalar('test', 'quick')
# scalar2 is a new 3d_scalar that copies the existing 'quick' 3d_scalar graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="get3d_scalar" ></a>get3d_scalar</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a boxfill
        class object from an existing VCS boxfill graphics method. If no boxfill name is
        given, then boxfill 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createboxfill function.)</p>
      </td>

      <td>
        <ul>
          <li>[3d_scalar name]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('3d_scalar')
# Show all the existing 3d_scalar graphics methods
scalar = a.get3d_scalar()
# scalar is an instance of the 'default' 3d_scalar graphics method
scalar2 = a.get3d_scalar('quick')
# scalar2 is an instance of the existing 'quick' 3d_scalar graphics method
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="3d_vector"></a>3D Vector</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="create3d_vector"></a>create3d_vector</code></td>

      <td>
        

        <p>Create a new 3d_vector graphics method given the name and the existing
        3d_vector graphics method to copy the attributes from. If no existing 3d_vector
        graphics method name is given, then the default 3d_vector graphics method will be
        used as the graphics method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Graphics
        method names must be unique</p>
      </td>

      <td>
        <ul>
          <li>new 3d_vector name</li>

          <li>[existing 3d_vector to copy attributes from]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('3d_vector')
# Show all the existing 3d_vector graphics methods
vector = a.create3d_vector('quick')
# vector is a new 3d_vector that copies the 'default' 3d_vector graphics method
vector2 = a.create3d_vector("test", 'quick')
# vector2 is a new 3d_vector that copies the 'quick' 3d_vector graphics method
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="get3d_vector" ></a>get3d_vector</code></td>

      <td>
        

        <p>VCS contains a list of graphics methods. This function will create a 3d_vector
        class object from an existing VCS 3d_vector graphics method. If no 3d_vector name
        is given, then 3d_vector 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the create3d_vector function.)</p>
      </td>

      <td>
        <ul>
          <li>[3d_vector name]</li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('3d_vector')
# Show all the existing 3d_vector graphics methods
vector = a.get3d_vector()
# vector is an instance of the 'default' 3d_vector graphics method
vector2 = a.get3d_vector('quick')
# vector2 is an instance of the existing 'quick' 3d_vector graphics method
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="picture_template" ></a>Picture Template</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createtemplate"></a>createtemplate</code></td>

      <td>
        

        <p>Create a new template given the name and the existing template to copy the
        attributes from. If no existing template name is given, then the default template
        will be used as the template to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Template
        names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new template name</p></li>
          <li><p>[name of template to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('template')
# Show all the existing templates
con=a.createtemplate('example1')
# create 'example1' template from 'default' template
a.show('template')
# Show all the existing templates
con=a.createtemplate('example2','quick')
# create 'example2' from 'quick' template
a.listelements('template')
# Show all the templates as a Python list
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="gettemplate" ></a>gettemplate</code></td>

      <td>
        

        <p>VCS contains a list of predefined templates. This function will create a
        template class object from an existing VCS template. If no template name is
        given, then template 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createtemplate function.)</p>
      </td>

      <td>
        <ul>
          <li><p>[template name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('template')
# Show all the existing templates
templt=a.gettemplate()
# templt instance of 'default' template
templt2=a.gettemplate('quick')
# templt2 contains 'quick' template
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: templateobject</p>

        

        <p>The template primary method (P) determines the location of each picture
        segment, the space to be allocated to it, and related properties relevant to its
        display.</p>

        <p>Other Useful Functions:</p>

        <p>a.show('template') Show predefined templates</p>

        <p>a.show('texttable') Show predefined text table methods</p>

        <p>a.show('textorientation') Show predefined text orientation methods</p>

        <p>a.show('line') Show predefined line methods</p>

        <p>a.listelements('template') Show templates as a Python list</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use the update function toupdate the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>See <a href="vcs-6.html#template">Chapter 6</a> for the long list of options.</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of boxfill use:
    box=a.createboxfill('new','quick')
# Copies content of 'quick' to 'new'
box=a.createboxfill('new')
# Copies content of 'default' to 'new'

# To Modify an existing boxfill use:
    box=a.getboxfill('AMIP_psl')

# To Create a new instance of template use:
    tpl=a.createtemplate('new','AMIP')
# Copies content of 'AMIP' to 'new'
tpl=a.createtemplate('new')
# Copies content of 'default' to 'new'

# To Modify an existing template use:
    tpl=a.gettemplate('AMIP')
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="secondary_objects" ></a>Secondary Objects</p>
      </th>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="colormap_commands" ></a>Colormap Commands</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="setcolormap" ></a>setcolormap</code></td>

      <td>
        <p>It is necessary to change the colormap. This routine will change the VCS color
        map.</p>

        <p>If the visual display is 16-bit, 24-bit, or 32-bit TrueColor, then a redrawing
        of the VCS Canvas is made every time the colormap is changed.</p>
      </td>

      <td>
        <ul>
          <li><p>colormap</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.setcolormap("AMIP")
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="setcolorcell" ></a>setcolorcell</code></td>

      <td>
        

        <p>Set a individual color cell in the active colormap. If default is the active
        colormap, then return an error string.</p>

        <p>If the visul display is 16-bit, 24-bit, or 32-bit TrueColor, then a redrawing
        of the VCS Canvas is made evertime the color cell is changed.</p>

        <p>Note, the user can only change color cells 0 through 239 and R,G,Bvalue must
        range from 0 to 100. Where 0 represents no color intensity and 100 is the
        greatest color intensity.</p>
      </td>

      <td>
        <ul>
          <li><p>colormap layout: default to 239</p></li>
          <li><p>R - Red intensity value: 0 to 100</p></li>
          <li><p>G - Green intensity value: 0 to 100</p></li>
          <li><p>B - Blue intensity value: 0 to 100</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.setcolormap("AMIP")
a.setcolorcell(11,0,0,0)
a.setcolorcell(21,100,0,0)
a.setcolorcell(31,0,100,0)
a.setcolorcell(41,0,0,100)
a.setcolorcell(51,100,100,100)
a.setcolorcell(61,70,70,70)
</pre>
      </td>
    </tr>
<!--
    <tr>
      <td><code><a name="colormapgui" ></a>colormapgui</code></td>

      <td>
        

        <p>Run the VCS colormap interface.</p>

        <p>The colormapgui command is used to bring up the VCS colormap interface. The
        interface is used to select, create, change, or remove colormaps.</p>

        <p>Note:</p>

        <p>The colormapgui GUI will only work for 8-bit 'Pseudo Color'.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.colormapgui()
</pre>
      </td>
    </tr>-->
    <tr>
      <th colspan="4">
        <p><a name="fill_area" ></a>Fill Area</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createfillarea"></a>createfillarea</code></td>

      <td>
        

        <p>Create a new fillarea secondary method given the name and the existing
        fillarea secondary method to copy the attributes from. If no existing fillarea
        secondary method name is given, then the default fillarea secondary method will
        be used as the secondary method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Secondary
        method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new fillarea name</p></li>
          <li><p>[name of fillarea to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('fillarea')
fa=a.createfillarea('example1',)
a.show('fillarea')
fa=a.createfillarea('example2','black')
a.show('fillarea')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getfillarea" ></a>getfillarea</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a fillarea
        class object from an existing VCS fillarea secondary method. If no fillarea name
        is given, then fillarea 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.
        However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createfillarea function.)</p>
      </td>

      <td>
        <ul>
          <li><p>[fillarea name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('fillarea')
# Show all the existing fillarea secondary methods
fa=a.getfillarea()
# fa instance of 'default' fillarea secondary method
fa2=a.getfillarea('quick')
# fa2 instance of existing 'quick' fillarea secondary method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: fillareaobject</p>

        

        <p>The Fillarea class object allows the user to edit fillarea attributes,
        including</p>

        <p>fillarea interior style, style index, and color index.</p>

        <p>This class is used to define an fillarea table entry used in VCS, or itcan be
        used to change some or all of the fillarea attributes in an existing fillarea
        table entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('fillarea') Show predefined fillarea objects</p>

        <p>a.update() # Updates the VCS Canvas at user's request a.mode=1, or 0 If 1,
        then automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>style</p></li>
          <li><p>index</p></li>
          <li><p>color</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of fillarea use:
    fa=a.createfillarea('new','def37')
# Copies content of 'def37' to 'new'
fa=a.createfillarea('new')
# Copies content of 'default' to 'new'

# To Modify an existing fillarea use:
    fa=a.getfillarea('red')

# fa.list()
# Will list all the fillarea attribute values

# There are three possibilities for setting the isofill style (Ex):
    fa.style = 'solid'
fa.style = 'hatch'
fa.style = 'pattern'
fa.index=1
# Range from 1 to 20
fa.color=100
# Range from 1 to 256

# Specify the fillarea index:
    fa.index=1
fa.index=2
fa.index=3
fa.index=4
fa.index=5
fa.index=6
fa.index=7
fa.index=8
fa.index=9
fa.index=10
fa.index=11
fa.index=12
fa.index=13
fa.index=14
fa.index=15
fa.index=16
fa.index=17
fa.index=18
fa.index=19
fa.index=20
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="line" ></a>Line</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createline" ></a>createline</code></td>

      <td>
        

        <p>Create a new line secondary method given the name and the existing line
        secondary method to copy the attributes from. If no existing line secondary
        method name is given, then the default line secondary method will be used as the
        secondary method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned. Secondary
        method names must be unique</p>
      </td>

      <td>
        <ul>
          <li><p>new line name</p></li>
          <li><p>[name of line to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('line')
ln=a.createline('example1',)
a.show('line')
ln=a.createline('example2','black')
a.show('line')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getline" ></a>getline</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a line
        class object from an existing VCS line secondary method. If no line name is
        given, then line 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.</p>

        <p>However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createline function.)</p>
      </td>

      <td>
        <p>[line name]</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('line')
# Show all the existing line secondary methods
ln=a.getline()
# ln instance of 'default' line secondary method
ln2=a.getline('quick')
# ln2 instance of existing 'quick' line secondary method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: lineobject</p>

        

        <p>The Line object allows the manipulation of line type, width, and color
        index.</p>

        <p>This class is used to define an line table entry used in VCS, or itcan be used
        to change some or all of the line attributes in an existing line table entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('line') Show predefined line objects</p>

        <p>a.update() # Updates the VCS Canvas at user's request a.mode=1, or 0 If 1,
        then automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>type</p></li>
          <li><p>width</p></li>
          <li><p>color</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of line use:
    ln=a.createline('new','red')
# Copies content of 'red' to 'new'
ln=a.createline('new')
# Copies content of 'default' to 'new'

# To Modify an existing line use:
    ln=a.getline('red')
ln.list()
# Will list all the line attribute values
ln.color=100
# Range from 1 to 256
ln.width=100
# Range from 1 to 300

# Specify the line type:
    ln.type='solid'
# Same as ln.type=0
ln.type='dash'
# Same as ln.type=1
ln.type='dot'
# Same as ln.type=2
ln.type='dash-dot'
# Same as ln.type=3
ln.type='long-dash'
# Same as ln.type=4

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="marker" ></a>Marker</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createmarker" ></a>createmarker</code></td>

      <td>
        

        <p>Create a new marker secondary method given the name and the existing marker
        secondary method to copy the attributes from. If no existing marker secondary
        method name is given, then the default marker secondary method will be used as
        the secondary method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned.</p>

        <p>Secondary method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new marker name</p></li>
          <li><p>[name of marker to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('marker')
mrk=a.createmarker('example1',)
a.show('marker')
mrk=a.createmarker('example2','black')
a.show('boxfill')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="getmarker" ></a>getmarker</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a marker
        class object from an existing VCS marker secondary method. If no marker name is
        given, then marker 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.</p>

        <p>However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createmarker function.)</p>
      </td>

      <td>
        <p>[marker name]</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('marker')
# Show all the existing marker secondary methods
mrk=a.getmarker()
# mrk instance of 'default' marker secondary method
mrk2=a.getmarker('quick')
# mrk2 instance of existing 'quick' marker secondary method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: markerobject</p>

        

        <p>The Marker object allows the manipulation of marker type, size, and color
        index.</p>

        <p>This class is used to define an marker table entry used in VCS, or it can be
        used to change some or all of the marker attributes in an existing marker table
        entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('marker') Show predefined marker objects</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>type</p></li>
          <li><p>size</p></li>
          <li><p>color</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of marker use:
    mk=a.createmarker('new','red')
# Copies content of 'red' to 'new'
mk=a.createmarker('new')
# Copies content of 'default' to 'new'

# To Modify an existing marker use:
    mk=a.getmarker('red')

mk.list()
# Will list all the marker attribute values
mk.color=100
# Range from 1 to 256
mk.size=100
# Range from 1 to 300

# Specify the marker type:
    mk.type='dot'
# Same as mk.type=1
mk.type='plus'
# Same as mk.type=2
mk.type='star'
# Same as mk.type=3
mk.type='circle'
# Same as mk.type=4
mk.type='cross'
# Same as mk.type=5
mk.type='diamond'
# Same as mk.type=6
mk.type='triangle_up'
# Same as mk.type=7
mk.type='triangle_down' # Same as mk.type=8
mk.type='triangle_left' # Same as mk.type=9
mk.type='triangle_right' # Same as mk.type=10
mk.type='square'
# Same as mk.type=11
mk.type='diamond_fill' # Same as mk.type=12
mk.type='triangle_up_fill' # Same as mk.type=13
mk.type='triangle_down_fill' # Same as mk.type=14
mk.type='triangle_left_fill' # Same as mk.type=15
mk.type='triangle_right_fill' # Same as mk.type=16
mk.type='square_fill' # Same as mk.type=17

</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="text-combined"></a>Text-Combined</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createtextcombined"></a>createtextcombined</code></td>

      <td>
        

        <p>Create a new textcombined secondary method given the names and the existing
        texttable and textorientation secondary methods to copy the attributes from. If
        no existing texttable and textorientation secondary method names are given, then
        the default texttable and textorientation secondary methods will be used as the
        secondary method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned.</p>

        <p>Secondary method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new textcombined name</p></li>
          <li><p>[name of textcombined to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('texttable')
a.show('textorientation')
tc=a.createtextcombined('example1','std','example1','7left')
a.show('texttable')
a.show('textorientation')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="gettextcombined"></a>gettextcombined</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a
        textcombined class object from an existing VCS texttable secondary method and an
        existing VCS textorientation secondary method. If no texttable or textorientation
        names are given, then the 'default' names will be used in both cases.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.</p>

        <p>However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createtextcombined function.)</p>
      </td>

      <td>
        <ul>
          <li><p>[textcombined name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('texttable')
# Show all the existing texttable secondary methods
a.show('textorientation')
# Show all the existing textorientation secondary methods
tc=a.gettextcombined()
# Use 'default' for texttable and textorientation
tc2=a.gettextcombined('std','7left')
# Use 'std' texttable and '7left' textorientation
if istextcombined(tc):
    # Check to see if tc is a textcombined
tc.list()
# Print out all its attriubtes
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: textcombinedobject</p>

        

        <p>The (Tc) Text Combined class will combine a text table class and a text
        orientation class together. From combining the two classess, the user will be
        able to set attributes for both classes (i.e., define the font, spacing,
        expansion, color index, height, angle, path, vertical alignment, and horizontal
        alignment).</p>

        <p>This class is used to define and list a combined text table and text
        orientation</p>

        <p>entry used in VCS.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>font</p></li>
          <li><p>spacing</p></li>
          <li><p>expansion</p></li>
          <li><p>color</p></li>
          <li><p>name</p></li>
          <li><p>height</p></li>
          <li><p>angel</p></li>
          <li><p>path</p></li>
          <li><p>halign</p></li>
          <li><p>valign</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of text table use:
    tc=a.createtextcombined('new_tt','std','new_to','7left')
# Copies content of 'std' to 'new_tt' and '7left' to 'new_to'


# To Modify an existing texttable use:
    tc=a.gettextcombined('std','7left')
tc.list()
# Will list all the textcombined attribute values (i.e., texttable and textorientation attributes

# Specify the text font type:
    tc.font=1
# The font value must be in the range 1 to 9

#Specify the text spacing:
    tc.spacing=2
# The spacing value must be in the range -50 to 50

# Specify the text expansion:
    tc.expansion=100
# The expansion value ranges from 50 to 150

# Specify the text color:
    tc.color=241
# The text color value ranges from 1 to 257
# Specify the text height:
    tc.height=20 # The height value must be in the range 1 to 100
# Specify the text angle:
    tc.angle=0 # The angle value ran # Specify the text path:
    tc.path='right' # Same as tc.path=0
tc.path='left' # Same as tc.path=1
tc.path='up' # Same as tc.path=2 ges from 0 to 360
tc.path='down' # Same as tc.path=3
# Specify the text horizontal alignment:
    tc.halign='right' # Same as tc.halign=0
tc.halign='center' # Same as tc.halign=1
tc.halign='right' # Same as tc.halign=2
# Specify the text vertical alignment:
    tc.valign='tcp' # Same as tcvalign=0
tc.valign='cap' # Same as tcvalign=1
tc.valign='half' # Same as tcvalign=2
tc.valign='base' # Same as tcvalign=3
tc.valign='bottom' # Same as tcvalign=4
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="text-orientation"></a>Text-Orientation</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createtextorientation"></a>createtextorientation</code></td>

      <td>
        

        <p>Create a new textorientation secondary method given the name and he existing
        textorientation secondary method to copy the attributes from. If no existing
        textorientation secondary method name is given, then the default textorientation
        secondary method will be used as the secondary method to which the attributes
        will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned.</p>

        <p>Secondary method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new textorientation name</p></li>
          <li><p>[name of textorientation to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('textorientation')
to=a.createtextorientation('example1')
a.show('textorientation')
to=a.createtextorientation('example2','black')
a.show('textorientation')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="gettextorientation"></a>gettextorientation</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a
        textorientation class object from an existing VCS textorientation secondary
        method. If no textorientation name is given, then textorientation 'default' will
        be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.</p>

        <p>However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createtextorientation function.)</p>
      </td>

      <td>
        <p>[textorientation name]</p>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('textorientation')
# Show all the existing textorientation secondary methods
to=a.gettextorientation()
# to instance of 'default' textorientation secondary method
to2=a.gettextorientation('quick')
# to2 instance of existing 'quick' textorientation secondary method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: textorientationobject</p>

        

        <p>The (To) Text Orientation lists text attribute set names that define the font,
        spacing, expansion, and color index.</p>

        <p>This class is used to define an text orientation table entry used in VCS, or
        it can be used to change some or all of the text orientation attributes in an
        existing text orientation table entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('textorientation') Show predefined text orientation objects</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>height</p></li>
          <li><p>angel</p></li>
          <li><p>path</p></li>
          <li><p>halign</p></li>
          <li><p>valign</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of text orientation use:
    to=a.createtextorientation('new','7left')
# Copies content of '7left' to 'new'
to=a.createtextorientation('new')
# Copies content of 'default' to 'new'

# To Modify an existing textorientation use:
    to=a.gettextorientation('7left')
to.list()
# Will list all the textorientation attribute values

# Specify the text height:
    to.height=20
# The height value must be in the range 1 to 100

#ecify the text angle:
    to.angle=0
# The angle value must be in the range 0 to 360

# Specify the text path:
    to.path='right'
# Same as to.path=0
to.path='left'
# Same as to.path=1
to.path='up'
# Same as to.path=2
to.path='down'
# Same as to.path=3
# Specify the text horizontal alignment:
    to.halign='right' # Same as to.halign=0
to.halign='center' # Same as to.halign=1
to.halign='right'
# Same as to.halign=2
# Specify the text vertical alignment:
    to.valign='top' # Same as tovalign=0
to.valign='cap'
# Same as tovalign=1
to.valign='half' # Same as tovalign=2
to.valign='base' # Same as tovalign=3
to.valign='bottom'
# Same as tovalign=4
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="text-table"></a>Text-Table</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="createtexttable"></a>createtexttable</code></td>

      <td>
        

        <p>Create a new texttable secondary method given the name and the existing
        texttable secondary method to copy the attributes from. If no existing texttable
        secondary method name is given, then the default texttable secondary method will
        be used as the secondary method to which the attributes will be copied from.</p>

        <p>If the name provided already exists, then a error will be returned.</p>

        <p>Secondary method names must be unique.</p>
      </td>

      <td>
        <ul>
          <li><p>new texttable name</p></li>
          <li><p>[name of texttable to copy attributes from]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('texttable')
tt=a.createtexttable('example1',)
a.show('texttable')
tt=a.createtexttable('example2','black')
a.show('texttable')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="gettexttable" ></a>gettexttable</code></td>

      <td>
        

        <p>VCS contains a list of secondary methods. This function will create a
        texttable class object from an existing VCS texttable secondary method. If no
        texttable name is given, then texttable 'default' will be used.</p>

        <p>Note, VCS does not allow the modification of 'default' attribute sets.</p>

        <p>However, a 'default' attribute set that has been copied under a different name
        can be modified. (See the createtexttable function.)</p>
      </td>

      <td>
        <ul>
          <li><p>[texttable name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.show('texttable')
# Show all the existing texttable secondary methods
tt=a.gettexttable()
# tt instance of 'default' texttable secondary method
tt2=a.gettexttable('quick')
# tt2 instance of existing 'quick' texttable secondary method
</pre>
      </td>
    </tr>

    <tr>
      <td></td>

      <td>
        <p>Object: texttableobject</p>

        

        <p>The (Tt) Text Table lists text attribute set names that define the font,
        spacing, expansion, and color index.</p>

        <p>This class is used to define an text table table entry used in VCS, or it can
        be used to change some or all of the text table attributes in an existing text
        table table entry.</p>

        <p>Other Useful Functions:</p>

        <p>a=vcs.init() Constructor</p>

        <p>a.show('texttable') Show predefined text table objects</p>

        <p>a.update() Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
        automatic update, else if 0, then use update function to update the VCS
        Canvas.</p>
      </td>

      <td>
        <ul>
          <li><p>name</p></li>
          <li><p>font</p></li>
          <li><p>spacing</p></li>
          <li><p>expansion</p></li>
          <li><p>color</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()

# To Create a new instance of text table use:
    tt=a.createtexttable('new','std')
# Copies content of 'std' to 'new'
tt=a.createtexttable('new')
# Copies content of 'default' to 'new'

# To Modify an existing texttable use:
    tt=a.gettexttable('std')
tt.list()
# Will list all the texttable attribute values

# Specify the text font type:
    tt.font=1
# The font value must be in the range 1 to 9

# Specify the text spacing:
    tt.spacing=2
# The spacing value must be in the range -50 to 50

# Specify the text expansion:
    tt.expansion=100
# The expansion value must be in the range 50 to 150

# Specify the text color:
    tt.color=241
# The text color attribute value must be in the range 1 to 257
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="remove_objects" ></a>Remove Objects</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="removeobject" ></a>removeobject</code></td>

      <td>
        

        <p>The user has the ability to create primary and secondary class objects. This
        function allows the user to remove these objects from the appropriate class
        list.</p>

        <p>Note, To remove the object completely from Python, remember to use the "del"
        function.</p>

        <p>Also note, The user is not allowed to remove a "default" class object.</p>
      </td>

      <td>
        <ul>
          <li><p>object</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
line=a.getline('red')
# To Modify an existing line object
iso=a.createisoline('dean')
# Create an instance of an isoline object
...
a.removeobject(line)
# Removes line object from VCS list
del line
# Destroy instance "line", garbage collection
a.removeobject(iso)
# Remove isoline object from VCS list
del iso
# Destroy instance "iso", garbage collection
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="set_continents_type" ></a>Set Continents
        Type</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="setcontinentstype"></a>setcontinentstype</code></td>

      <td>
        

        <p>One has the option of using continental maps that are predefined or that are
        user-defined. Predefined continental maps are either internal to VCS or are
        specified by external files. User-defined continental maps are specified by
        additional external files that must be read as input.</p>

        <p>The continents-type values are integers ranging from 0 to 11, where:</p>

        <p>0 signifies "No Continents"</p>

        <p>1 signifies "Fine Continents"</p>

        <p>2 signifies "Coarse Continents"</p>

        <p>3 signifies "United States" (with "Fine Continents")</p>

        <p>4 signifies "Political Borders" (with "Fine Continents")</p>

        <p>5 signifies "Rivers" (with "Fine Continents")</p>

        <p>Values 6 through 11 signify the line type defined by the files</p>

        <p>data_continent_other7 through data_continent_other12.</p>
      </td>

      <td>
        <ul>
          <li><p>continents type number, ranging from 0 to 11</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
# Set continents to "United States"
a.setcontinentstype(3)
a.plot(array,'default','isofill','quick'
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="set_default_methods" ></a>Set Default Picture Template and Graphics Methods</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="set" ></a>set</code></td>

      <td>
        

        <p>Set the default VCS primary class objects: template and graphics methods.</p>

        <p>Keep in mind the template, determines the appearance of each graphics segment;
        the graphic method specifies the display technique; and the data defines what is
        to be displayed. Note, the data cannot be set with this function.</p>
      </td>

      <td>
        <ul>
          <li><p>template or graphics methods type,</p></li>
          <li><p>[template name or graphics method name]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.set('isofill','quick')
# Changes the default graphics method to Isofill: 'quick'
a.plot(array)
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="animation" ></a>Animation</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="animate" ></a>animate</code></td>

      <td>
        

        <p>Animate the contents of the VCS Canvas. Currently, only one display can be
        shown in the VCS Canvas for the animation to work.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.animate()
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="flush_section" ></a>Flush</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="flush" ></a>flush</code></td>

      <td>
        

        <p>The flush command executes all buffered X events in the que.</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.flush()
</pre>
      </td>
    </tr>

    <tr>
      <th colspan="4">
        <p><a name="grid_section" ></a>Grid</p>
      </th>
    </tr>

    <tr>
      <td><code><a name="grid" ></a>grid</code></td>

      <td>
        

        <p>Set the default plotting region for variables that have more dimension values
        than the graphics method. This will also be used for animating plots over the
        third and fourth dimensions.</p>
      </td>

      <td>
        <ul>
          <li><p>([first dim's 1st value, first dim's last value] ,..., [last dim's 1st value, last dim's last value]</p></li>
        </ul>
      </td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a=vcs.init()
a.grid(12,24, -70,70, -150,150)
a.plot(array,'default','isofill','quick')
</pre>
      </td>
    </tr>

    <tr>
      <td><code><a name="resetgrid" ></a>resetgrid</code></td>

      <td>
        

        <p>Set the plotting region to default values. That is, let the variable's
        dimension values determine the grid</p>
      </td>

      <td></td>

      <td>
        <p>Example of Use:</p>
        <pre style="word-break:normal;">
import vcs
a=vcs.init()
a=vcs.init()
a.resetgrid()
a.plot(array,'default','isofill','quick')
</pre>
      </td>
    </tr>
  </tbody>
  </table>




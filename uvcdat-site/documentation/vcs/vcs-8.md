---
title: VCS Chapter 8
layout: docs
manual: vcs
index: 8
---






##  CHAPTER 8 VCS Examples
This section shows useful VCS examples.

<a name="simple_plot"></a>

###Simple Plotting Example:

{% highlight python %}
#
# Simple Plot module
#
############################################################################
#                                                                          #
# Module: simpleplot module                                                #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Simple plotting example.                                    #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################

def simpleplot():
    
    import vcs,cdms2 # import vcs and cdms
    
    #####################################################################
    # See the CDMS document on how to ingest data. Also see the CU and  #
    # the Numeric documents on alternative ways to import data into VCS #
    #####################################################################
    
    f = cdms2.openDataset('example.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data

    #######################################################################
    # Basically to plot using the VCS module, three steps are required:   #
    # importing the vcs module; initializing the VCS Canvas Object, and   #
    # plotting the data on the VCS Canvas.                                #
    #######################################################################
    
    x = vcs.init() # initialize vcs
    x.plot(s,variable = clt) # plot data using default values

    print '*******************************************************************'
    print '****** ******'
    print '****** SIMPLE PLOTTING COMPLETED ******'
    print '****** ******'
    print '*******************************************************************'

if __name__ == "__main__":
    simpleplot()
{% endhighlight %}


<a name="simple_overlay"></a>

###Simple Overlay Plot Example:

``` python
#
# Simple Overlay Plot module
#
############################################################################
#                                                                          #
# Module: simpleoverlay module                                             #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Simple overlay plotting example                             #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################

def simpleoverlay():
    import vcs,cdms2 # import vcs and cdms

    #####################################################################
    # See the CDMS document on how to ingest data. Also see the CU and  #
    # the Numeric documents on alternative ways to import data into VCS #
    #####################################################################

    f = cdms2.openDataset('example.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data

    ########################################################################
    # Basically to plot using the VCS module, three steps are required:    #
    # importing the vcs module; initializing the VCS Canvas Object, and    #
    # plot the data on the VCS Canvas.                                     #
    #                                                                      #
    # Note:                                                                #
    # In the example below, we are using isofill and isoline to plot the   #
    # data. We could just as easily used the `plot()' function to achieve  #
    # the same result:                                                     #
    # x.plot(s,'default', `isofill', variable = clt)                       #
    # x.plot(s,'default_dud', `isoline', variable = clt)                   #
    # Note:                                                                #
    # `default' and `default_dud' are passed as the second argument in     #
    # plot routines, respectfully. `default' represents a VCS template     #
    # that displays the text and plot lengend, while `default_dud' is a    #
    # VCS template that will only display the data on the VCS Canvas.      #
    ########################################################################

    x = vcs.init() # initialize vcs
    x.isofill(s,'default',variable = clt) # plot data using default values
    x.isoline(s,'default_dud',variable = clt) # overlay isolines over isofill plot

    print '*****************************************************************'
    print '****** ******'
    print '****** SIMPLE OVERLAY COMPLETED ******'
    print '****** ******'
    print '*****************************************************************'

if __name__ == "__main__":
    simpleoverlay()
{% highlight text %}

<a name="boxfill"></a>

###Boxfill Graphics Method Example:

{% highlight python %}
#
# Example Boxfill (Gfb) module
#
############################################################################
#                                                                          #
# Module: exampleboxfill module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's boxfill graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################

def exampleboxfill():
    import vcs,cdms2 # import vcs and cdms

    f = cdms2.openDataset('example.nc') # open example file
    
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data
    
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','boxfill','quick',variable = clt)# plot slab the old way
    x.geometry(450,337) # change the geometry
    
    print x.listelements('boxfill') # print boxfill Python list

    x.show('boxfill') # show list of boxfill graphics methods
    a = x.getboxfill('quick') # get 'quick' boxfill graphics method

    if x.isgraphicsmethod(a): # check for graphics method
        print 'Yes, this is a graphics method'

    if x.isboxfill(a): # check for boxfill
        print 'Yes, this is a isofill graphics method'

    a.list() # list its attributes
    a.color_1 = 50 # change color_1 index attribute
    a.xticlabels('lon30','lon30') # change xlabels attribute
    a.xticlabels('','') # change remove xlables from plot
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change region
    a.datawc(1e20,1e20,1e20,1e20) # change region back
    a.xticlabels('*') # change attribute labels back

    x.mode = 0 # turn atomatic update off

    a.color_1 = 100 # change color_1 attribute
    a.color_2 = 200 # change color_2 index value
    a.xticlabels('lon30','lon30') # change attribute
    a.yticlabels('','') # change y-labels off attribute
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change region

    x.update() # view changes now
    
    a.script('test','w') # save 'quick' boxfill as a Python script

    x.mode = 1 # turn atomatic update mode back on

    a.color_1 = 16 # change color_1 attribute
    a.color_2 = 239 # change color_2 index value
    a.level_1 = 20 # change level_1
    a.level_2 = 80 # change level_2
    a.datawc(1e20,1e20,1e20,1e20) # change region back
    a.yticlabels('*') # change y-labels attribute

    x.scriptobject(a,'test', 'a') # append 'quick' to the existing file
    
    a.script('test.scr','w') # save 'quick' as a VCS script file

    x.show('template') # show the list of templates
    
    t = x.createtemplate('test','AMIPDUD')# create template 'test' from AMIPDUD

    x.clear() # clear the VCS Canvas
    x.boxfill(s,a,'default') # plot using default template
    x.clear() # clear the VCS Canvas
    x.boxfill(a,'default',s) # plot using default template, but, reverse the order
    x.clear() # clear the VCS Canvas
    x.boxfill(s,a,t) # plot using template 'test'
    x.clear() # clear the VCS Canvas
    x.boxfill(a,s,t) # plot using template 'test', but reverse the objects
    x.clear() # clear the VCS Canvas
    x.boxfill(t,a,s) # plot using template 'test', but reverse the objects
    x.clear() # clear the VCS Canvas

    x.plot(t,a,s) # plot using the new way
    x.clear() # clear the VCS Canvas
    x.plot(a,t,s) # plot using the new way
    x.clear() # clear the VCS Canvas
    x.plot(s,t,a) # plot using the new way
    x.clear() # clear the VCS Canvas
    x.plot('default',a,s) # plot using the new way
    x.clear() # clear the VCS Canvas
    x.plot('default',s) # plot using the new way


    x.show('boxfill') # show boxfill list without test2

    a = x.createboxfill('test2','quick') # create 'test2' from 'quick'
    a.color_1 = 50 # change color level
    a.list() # list its attributes
    x.show('boxfill') # show boxfill list with test2
    x.removeobject(a) # remove test2 from boxfill list
    x.show('boxfill') # show boxfill list without test2

    print '*******************************************************************'
    print '****** ******'
    print '****** BOXFILL EXAMPLE COMPLETED ******'
    print '****** ******'
    print '*******************************************************************'

if __name__ == "__main__":
    exampleboxfill()
{% endhighlight %}

<a name="continents"></a>

###Continents Graphics Method Example:

{% highlight python %}
#
# Example Continents (Gcon) module
#
############################################################################
#                                                                          #
# Module: examplecontinents module                                         #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example of VCS's continents graphics method.                #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs modules.                                                     #
#                                                                          #
############################################################################
def examplecontinents():
    import vcs # import vcs and cdms2

    x = vcs.init() # construct vcs canvas

    x.plot('default','continents','quick')# plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location


    x.show('continents') # show list of continents
    a = x.getcontinents('quick') # get 'quick' continents
    
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    
    if x.iscontinents(a): # test object 'a' if continents
        print 'Yes, this is an continents graphics method'
    a.list() # list the continents' attributes and values

    a.script('test','w') # save 'quick' continents as a Python script

    a.xticlabels('','') # remove the x-axis
    a.xticlabels('lon30','lon30') # change the x-axis
    a.xticlabels('*') # put the x-axis
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change the region
    a.datawc(1e20,1e20,1e20,1e20) # put the region back

    a.line = 1 # same as 'dash', change the line style
    a.line = 2 # same as 'dot', change the line style
    a.line = 3 # same as 'dash-dot', change the line style
    a.line = 0 # same as 'solid', change the line style
    a.line = 4 # same as 'long-dash', change the line style
    a.linecolor = (77) # change the line color
    a.linecolor = 16 # change the line color
    a.linecolor = 44 # same as a.linecolor = (44)
    a.linecolor = None # use the default line color, black
    a.line = None # use default line style, solid black line

    x.clear() # clear the VCS Canvas
    x.continents(a,'default') # plot continents using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a) # plot continents using template 't', and continents 'a'
    x.clear() # clear the VCS Canvas
    x.continents(a,t) # plot continents

    #########################################################################
    # Create line object 'l' from the default line                          #
    #########################################################################
    x.show('line')
    l = x.createline('test')

    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'

    if x.isline(l): # check to see if it is a line object
        print 'Yes, this is a line object.'

    l.list() # list the line's attributes and values

    #########################################################################
    # Use the create line object 'l' from above and modify the line object  #
    #########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.type = 'dash' # change the line type

    x.show('continents') # show list of continents
    r = x.createcontinents('test2','quick')# create continents 'test2'
    x.show('continents') # show list of continents
    x.removeobject(r) # remove continents 'test2'
    x.show('continents') # show list of continents

    ######################################################################
    # to see how x.update and x.mode work, see testoutline.py            #
    ######################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '**********************************************************'
    print '****** ******'
    print '****** CONTINENTS COMPLETED ******'
    print '****** ******'
    print '**********************************************************'


if __name__ == "__main__":
examplecontinents()
{% endhighlight %}

<a name="isofill"></a>

###Isofill Graphics Method Example:

{% highlight python %}
#
# Example Isofill (Gfi) module
#
############################################################################
#                                                                          #
# Module: exampleisofill module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's isofill graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################
def exampleisofill():
    import vcs,cdms2 # import vcs and cdms

    f = cdms2.openDataset('clt.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','isofill','quick')# plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    x.show('isofill') # show list of isofill graphics method
    a = x.getisofill('quick') # get 'quick' isofill graphics method
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isisofill(a): # test object 'a' if isofill
        print 'Yes, this is an isofill graphics method'
    a.list() # list the isofill's attributes and values

    a.script('test','w') # save 'quick' isofill as a Python script


    x.show('colormap') # list all the colormaps
    x.setcolormap("AMIP") # change the colormap from default to AMIP

    a.missing = 241 # change the missing background color to black

    a.xticlabels('lon30','lon30') # change the x-axis
    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change the region
    a.datawc(1e20,1e20,1e20,1e20) # put the region back

    a.levels = ([0,220],[230,240],[250,260]) # change the isofill levels
    a.levels = ([0,220,225,230,235,240],[230,240],[250,260]) # change the isofill
    levels
    a.levels = ([0,220,225,230,235,240],) # change the isofill levels
    a.levels = ([0,220,225,230,235,240,245,250]) # change the isofill levels
    a.levels = [0,220,225,230,235,240] # change the isofill levels
    a.levels = (0.0,220.0,225.0,230.0,235.0,240.0,250.0) # change the isofill levels
    a.levels = ([1e20]) # change back to default settings
    a.levels = (0,220,225,230,235,240,250,260,270) # change the isofill levels

    #########################################################################
    # Below will produce an error. Later, if needed, I will add this        #
    # functionality.                                                        #
    #a.levels = ('0','20','25','30') # this will produce an error           #
    #########################################################################

    a.ext_1 = 'y' # add the extended legend arrow to the left
    a.ext_1 = 'n' # remove the extended legend arrow to the left
    a.ext_2 = 'y' # add the extended legend arrow to the right
    a.ext_2 = 'n' # remove the extended legend arrow to the right
    a.exts('y','y') # add the extended legend arrow to left and right
    a.exts('n','n') # remove the extended legend arrow to left and right

    a.fillareastyle = 'pattern' # change the fill style to pattern
    a.fillareastyle = 'hatch' # change the fill style to hatch
    a.fillareaindices = ([1,3,5,6,9,20]) # set the hatch index patterns

    a.fillareacolors = ([22,33,44,55,66,77]) # set the fill area color indices
    a.fillareacolors = None # use default color indices
    a.fillareastyle = 'solid' # change the fill style back to solid

    x.clear() # clear the VCS Canvas
    x.isofill(s,a,'default') # plot isofill using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
       x.show('template') # show the list of templates

    x.show('fillarea') # show the list of fillarea secondary objects
    f = x.getfillarea('def37') # get fillarea 'def37'
    if x.issecondaryobject(f): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isfillarea(f): # check to see if it is a fill area
        print 'Yes, this is a fill area object.'
    f.list() # list the fillarea's attributes and values

    a.levels = (220,225,230,235,240,250,260,270,280,290,300,310) # change the
    isofill levels
    x.clear() # clear the VCS Canvas
    x.plot(a,t,s) # plot array using isofill 'a' and template 't'
    a.list() # list isofill's attributes
    a.fillareaindices = (3,4,7,9,11) # set the indices
    a.fillareaindices = (f,f,f,f,f,f) # set the indices using the fillarea object
    a.fillareaindices = (f,2,4,7) # reset the indices using the fillarea object
    a.fillareaindices = (7,f,f,f,8) # resett the indices using the fillare object

    f.color = 44 # change the fillarea object's color
    f.style = 'hatch' # change the fillarea object's fill style

    x.scriptobject(a,'test') # save 'quick' isofill as a Python script
    x.scriptobject(f,'test') # save 'def37' fill area as a Python script

    x.show('isofill') # show list of isofill
    r = x.createisofill('test2','quick') # create isofill 'test2'
    x.show('isofill') # show list of isofill
    x.removeobject(r) # remove isofill 'test2'
    x.show('isofill') # show list of isofill

    #############################################################################
    # to see how x.update and x.mode work, see testisofill.py                   #
    #############################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0

    print '**************************************************'
    print '****** ******'
    print '****** ISOFILL COMPLETED ******'
    print '****** ******'
    print '**************************************************'

if __name__ == "__main__":
    exampleisofill()
{% endhighlight %}

<a name="isoline"></a>

###Isoline Graphics Method Example:

{% highlight python %}
#
# Example Isoline (Gi) module
#
############################################################################
#                                                                          #
# Module: exampleisoline module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's isoline graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################
def exampleisoline():
import vcs,cdms2 # import vcs and cdms

f = cdms2.openDataset('clt.nc') # open example file
clt = f.variables['clt'] # get variable clt
s = clt[0] # get clt data
x = vcs.init() # construct vcs canvas

x.plot(s,'default','isoline','quick',variable = clt)# plot slab the old way
x.geometry(450,337,0,0) # change geometry and location
x.geometry(900,675,0,0) # change geometry and location

x.show('isoline') # show list of isoline
a = x.getisoline('quick') # get isoline 'quick'
if x.isgraphicsmethod(a): # test object 'a' for graphics method
print 'Yes, this is a graphics method'
if x.isisoline(a): # test object 'a' for isoline
print 'Yes, this is an isoline graphics method'
a.list() # list the isoline's attributes and values

a.script('test','w') # save 'quick' isoline as a Python script

a.xticlabels('lon30','lon30') # change the x-axis
a.xticlabels('','') # remove the x-axis
a.xticlabels('*') # put the x-axis back
a.datawc(-45.0, 45.0, -90.0, 90.0) # change the region
a.datawc(1e20,1e20,1e20,1e20) # put the region back

#########################################################################
# Set the isoline level vales                                           #
#########################################################################
a.level = ([20,0.0],[30,0],[50,0],[60,0]) # change the isoline values
a.level = [[20,0.0],[30,0],[50,0]] # change the isoline values
a.level = ((20,0.0),(30,0),(50,0),(60,0),(70,0)) # change the isoline values
a.level = (25,35,45,55) # change the isoline values
a.level = [(22,33,44,55,66)] # change the isoline values
a.level = [(23,32,45,50,76),] # change the isoline values
a.level = [0] # same as a.level = (0,)
a.level = [[0,1e20]] # same as a.level = ((0,1e20),), use default settings

#########################################################################
# Turn on and off the isoline level labels                              #
#########################################################################
a.label = 'y' # same as a.label = 1
a.label = 'n' # same as a.label = 0

#########################################################################
# Set the line style and line color                                     #
#########################################################################
a.level = ((20,0.0),(30,0),(50,0),(60,0),(70,0)) # change the isoline values
a.line = [1,3,0,4] # same as a.line = (1,3,0,4)
a.line = (['dash','long-dash','solid'])# same as a.line = ([2,4,0])
a.line = [2,4,1,3,2,0]
a.linecolors = ([22,33,44,55,66,77]) # change the line color
a.linecolors = (16,19,33,44) # change the line color
a.linecolors = None # use the default line color
a.line = None # use the default line style, which is solid

#########################################################################
# Set the text font and text color                                      #
#########################################################################
a.label = 'y' # same as a.label = 1
a.text = (1,2,3,4,5,6,7,8,9) # select fonts from 1 through 9
a.text = [9,8,7,6,5,4,3,2,1]
a.text = ([1,3,5,6,9,2])
a.textcolors = ([22,33,44,55,66,77]) # set the text color
a.textcolors = (16,19,33,44)
a.textcolors = None # use default text color, black
a.text = None # use default font, 1

#########################################################################
# Create template 'test' from the default template                      #
#########################################################################
x.show('template') # show the list of templates
t = x.createtemplate('test') # create template 'test' from 'default' template
if x.istemplate(t): # test whether 't' is a template or not
x.show('template') # show the list of templates

#########################################################################
# Create line object 'l' from the default line                          #
#########################################################################
x.show('line')
l = x.createline('test')
if x.issecondaryobject(l): # check to see if it is a secondary object
print 'Yes, this is a secondary object.'
if x.isline(l): # check to see if it is a line object
print 'Yes, this is a line object.'
l.list() # list the line's attributes and values

x.clear() # clear the VCS Canvas
x.isoline(s,a,t) # plot the array using the template and isoline object
x.clear() # clear the VCS Canvas
x.plot(t,a,s) # plot again using the new way

#########################################################################
# Use the create line object 'l' from above and modify the line object  #
#########################################################################
a.line = [1,3,0,4] # same as a.line = (1,3,0,4)
a.line = ([2,4,0]) # same as a.line = (['dash', 'long-dash', 'solid'])
a.line = (l,4,l,0) # use the line object
a.line = (l,3,4,2,0)
l.list() # list the line object attributes and values
l.color = 44 # change the line color
l.type = 'dash' # change the line type

#########################################################################
# Create the three types of text objects                                #
#########################################################################
tc = x.createtextcombined('testc','std', 'testc','7left')
if x.istextcombined(tc):
print '*** textcombined listings ***'
tc.list()

tt = x.createtexttable('testt', 'default')
if x.istexttable(tt):
print '*** texttable listings ***'
tt.list()

to = x.createtextorientation('testo')
if x.istextorientation(to):
print '*** textorientation listings ***'
to.list()

#########################################################################
# Use the text objects in the isoline plot                              #
#########################################################################
a.label = 'y' # make sure that the labels are turn on
a.text = ([1,3,5,6,9,2]) # set the font
a.text = ([tc,tt,to,6,9,2]) # use the created text objects and fonts

#########################################################################
# Change the text object values                                         #
#########################################################################
tc.font = 3 # changing isoline level 20
tc.height = 15
tc.angle = 180
tc.color = 242
tt.font = 2 # changing isoline level 30
tt.spacing = 20
to.height = 15 # changing isoline level 50
to.path = 'down'

a.text = None # use default font, which is font 1
a.line = None # use default line, which is solid

x.show('isoline') # show list of isoline
r = x.createisoline('test2','quick') # create isoline 'test2'
x.show('isoline') # show list of isoline
x.removeobject(r) # remove isoline 'test2'
x.show('isoline') # show list of isoline

#####################################################################
# to see how x.update and x.mode work, see testisoline.py           #
#####################################################################
#x.update()
#x.mode = 1
#x.mode = 0
print '***************************************************'
print '****** ******'
print '****** ISOLINE COMPLETED ******'
print '****** ******'
print '***************************************************'

if __name__ == "__main__":
    exampleisoline()
{% endhighlight %}

<a name="outfill"></a>

###Outfill Graphics Method Example:

{% highlight python %}
#
# Example Outfill (Gfo) module
#
############################################################################
#                                                                          #
# Module: exampleoutfill module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's outfill graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################
def exampleoutfill():
    import vcs,cdms2 # import vcs and cdms

    f = cdms2.openDataset('example.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','outfill','quick',variable = clt)# plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    f2 = cdms2.openDataset('examlpe.nc') # open surface data
    sft = f2.variables['sft'] # get surface sft
    s = sft[...] # get sft data

    x.clear() # clear the VCS Canvas
    x.plot(s,'default','outfill','quick',variable = sft)# plot the surface data

    x.show('outfill') # show list of outfill
    a = x.getoutfill('quick') # get 'quick' outfill
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isoutfill(a): # test object 'a' if outfill
        print 'Yes, this is an outfill graphics method'
    a.list() # list the outfill's attributes and values

    a.script('test','w') # save 'quick' outfill as a Python script


    a.xticlabels('lon30','lon30') # change the x-axis
    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change the region
    a.datawc(1e20,1e20,1e20,1e20) # put the region back

    a.fillareastyle = 'hatch' # change the fill style to hatch
    a.fillareaindex = 11 # change the hatch index pattern
    a.fillareacolor = (77) # change the hatch color
    a.fillareacolor = 16 # chnage the hatch color
    a.fillareacolor = 44 # same as a.fillareacolor = (44)
    a.fillareacolor = None # use the default hatch color (black)
    a.outfill = ([0]) # set the outfill value
    a.outfill = ([1]) # set the outfill value
    a.outfill = ([0,1]) # set the outfill value
    a.outfill = ([0]) # set the outfill value


    x.clear() # clear the VCS Canvas
    x.outfill(s,a,'default') # plot outfill using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,s) # plot outfill template 't', outfill 'a', and array 's'
    x.clear() # clear the VCS Canvas
    x.outfill(a,s,t) # plot using outfill 'a', array 's', and template 't'

    x.show('fillarea') # show the list of fillarea secondary objects
    f = x.getfillarea('def37') # get fillarea 'def37'
    if x.issecondaryobject(f): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isfillarea(f): # check to see if it is a fill area
        print 'Yes, this is a fill area object.'
    f.list() # list the fillarea's attributes and values

    a.fillareastyle = f
    f.color = 44 # change the fillarea object's color
    f.style = 'hatch' # change the fillarea object's fill style

    x.show('outfill') # show list of outfill
    r = x.createoutfill('test2','quick') # create outfill 'test2'
    x.show('outfill') # show list of outfill
    x.removeobject(r) # remove outfill 'test2'
    x.show('outfill') # show list of outfill


    ##################################################################
    # to see how x.update and x.mode work, see testoutfill.py        #
    ##################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '***************************************************'
    print '****** ******'
    print '****** OUTFILL COMPLETED ******'
    print '****** ******'
    print '***************************************************'

if __name__ == "__main__":
    exampleoutfill()
{% endhighlight %}

<a name="outline"></a>

###Outline Graphics Method Example:

{% highlight python %}
#
# Example Outline (Go) module
#
############################################################################
#                                                                          #
# Module: exampleoutline module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's outline graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                            #
#                                                                          #
############################################################################
def exampleoutline():
    import vcs,cdms2 # import vcs and cdms

    f = cdms2.openDataset('example.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','outline','quick',variable = clt)# plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location


    f2 = cdms2.openDataset('example.nc') # open surface data
    sft = f2.variables['sft'] # get variable sft
    s = sft[...] # get sft data
    x.clear() # clear the VCS Canvas
    x.plot(s,'default','outline','quick',variable = sft)# plot the surface data

    x.show('outline') # show list of outline
    a = x.getoutline('quick') # get 'quick' outline
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isoutline(a): # test object 'a' if outline
        print 'Yes, this is an outline graphics method'
    a.list() # list the isoline's attributes and values

    a.script('test','w') # save 'quick' outline as a Python script

    a.xticlabels('lon30','lon30') # change the x-axis
    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis
    a.datawc(-45.0, 45.0, -90.0, 90.0) # change the region
    a.datawc(1e20,1e20,1e20,1e20) # put the region back

    a.line = 0 # same as 'solid', change the line style
    a.line = 1 # same as 'dash', change the line style
    a.line = 2 # same as 'dot', change the line style
    a.line = 3 # same as 'dash-dot', change the line style
    a.line = 4 # same as 'long-dash', change the line style
    a.linecolor = (77) # change the line color
    a.linecolor = 16 # change the line color
    a.linecolor = 44 # same as a.linecolor = (44)
    a.linecolor = None # use the default line color, black
    a.line = None # use default line style, solid black line

    a.outline = ([0]) # set the outline value
    a.outline = ([1]) # set the outline value
    a.outline = ([0,1]) # set the outline value
    a.outline = ([0]) # set the outline value

    x.clear() # clear the VCS Canvas
    x.outline(s,a,'default') # plot outline using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,s) # plot outline template 't', outline 'a', and array 's'
    x.clear() # clear the VCS Canvas
    x.outline(a,s,t) # plot using outline 'a', array 's', and template 't'

    #########################################################################
    # Create line object 'l' from the default line                          #
    #########################################################################
    x.show('line')
    l = x.createline('test')
    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isline(l): # check to see if it is a line object
        print 'Yes, this is a line object.'
    l.list() # list the line's attributes and values

    #########################################################################
    # Use the create line object 'l' from above and modify the line object  #
    #########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.type = 'dash' # change the line type


    x.show('outline') # show list of outline
    r = x.createoutline('test2','quick') # create outline 'test2'
    x.show('outline') # show list of outline
    x.removeobject(r) # remove outline 'test2'
    x.show('outline') # show list of outline


    #####################################################################
    # to see how x.update and x.mode work, see testoutline.py           #
    #####################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '**************************************************'
    print '****** ******'
    print '****** OUTFILL COMPLETED ******'
    print '****** ******'
    print '**************************************************'

if __name__ == "__main__":
    exampleoutfill()
{% endhighlight %}


<a name="scatter"></a>

###Scatter Graphics Method Example:

{% highlight python %}
#
# Example Scatter (GSp) module
#
############################################################################
#                                                                          #
# Module: examplescatter module                                            #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's scatter graphics method.               #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplescatter():
    import vcs,cdms2 # import vcs, cdms2

    f = cdms2.open('clt2.nc') # open clt file
    u = f.getslab('u') # get slab u
    v = f.getslab('v') # get slab v

    x = vcs.init() # construct vcs canvas

    x.plot(u, v, 'default','scatter','quick')# plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    a = x.getscatter('quick') # get 'quick' scatter
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isscatter(a): # test object 'a' if scatter
        print 'Yes, this is an scatter graphics method'
    a.list() # list the scatter's attributes and values

    a.script('test','w') # save 'quick' scatter as a Python script


    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis

    ############################################################################
    # Change the scatter marker type                                           #
    ############################################################################
    a.marker = 1 # same as a.marker = 'dot'
    a.marker = 2 # same as a.marker = 'plus'
    a.marker = 3 # same as a.marker = 'star'
    a.marker = 4 # same as a.marker = 'circle'
    a.marker = 5 # same as a.marker = 'cross'
    a.marker = 6 # same as a.marker = 'diamond'
    a.marker = 7 # same as a.marker = 'triangle_up'
    a.marker = 8 # same as a.marker = 'triangle_down'
    a.marker = 9 # same as a.marker = 'triangle_left'
    a.marker = 10 # same as a.marker = 'triangle_right'
    a.marker = 11 # same as a.marker = 'square'
    a.marker = 12 # same as a.marker = 'diamond_fill'
    a.marker = 13 # same as a.marker = 'triangle_up_fill'
    a.marker = 14 # same as a.marker = 'triangle_down_fill'
    a.marker = 15 # same as a.marker = 'triangle_left_fill'
    a.marker = 16 # same as a.marker = 'triangle_right_fill'
    a.marker = 17 # same as a.marker = 'square_fill'

    ############################################################################
    # Change the scatter marker size                                           #
    ############################################################################
    a.markersize = 5
    a.markersize = 55
    a.markersize = 100
    a.markersize = 300
    a.markersize = 15

    ############################################################################
    # Change the scatter marker color                                          #
    ############################################################################
    a.markercolor = (77)
    a.markercolor = 16
    a.markercolor = 44 # same as a.markercolor = (44)

    ############################################################################
    # Change the scatter settings to default                                   #
    ############################################################################
    a.markercolor = None
    a.markersize = None
    a.marker = None

    a.marker = 1 # same as a.marker = 'dot'

    x.clear() # clear the VCS Canvas
    x.scatter(u, v, a,'default') # plot scatter using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,u,v) # plot scatter template 't', outline 'a', and arrays 'u':'v'
    x.clear() # clear the VCS Canvas
    x.scatter(a,u,v,t) # plot using outline 'a', array 'u':'v', and template 't'

    x.show('marker') # show the list of marker secondary objects
    m = x.getmarker('red') # get marker 'red'
    if x.issecondaryobject(m): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.ismarker(m): # check to see if it is a fill area
        print 'Yes, this is a marker object.'
    m.list() # list the marker's attributes and values

    ###########################################################################
    # Use the create marker object 'm' from above and modify the line object  #
    ###########################################################################
    a.marker = m # use the marker object
    m.list() # list the marker object attributes and values
    m.color = 44 # change the marker color
    m.type = 'square' # change the marker type
    m.size = 20 # change the marker size

    x.show('scatter') # show list of scatter
    r = x.createscatter('test2','quick') # create scatter 'test2'
    x.show('scatter') # show list of scatter
    x.removeobject(r) # remove scatter 'test2'
    x.show('scatter') # show list of scatter

    #####################################################################
    # to see how x.update and x.mode work, see testoutline.py           #
    #####################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '***************************************************'
    print '****** ******'
    print '****** SCATTER COMPLETED ******'
    print '****** ******'
    print '***************************************************'

if __name__ == "__main__":
    examplescatter()
{% endhighlight %}

<a name="vector"></a>

###Vector Graphics Method Example:

{% highlight python %}
#
# Example Vector (Gv) module
#
############################################################################
#                                                                          #
# Module: examplevector module                                             #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Used to test VCS's vector graphics method.                  #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplevector():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    u = f.getslab('u',':',':',-10.,0.,0,10)# get slab u
    v = f.getslab('v',':',':',-10.,0.,0,10)# get slab v
    x = vcs.init() # construct vcs canvas

    x.plot(u, v, 'default','vector','quick') # plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    a = x.getvector('quick') # get 'quick' vector
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isvector(a): # test object 'a' if vector
        print 'Yes, this is an vector graphics method'
    a.list() # list the vector's attributes and values

    a.script('test','w') # save 'quick' vector as a Python script


    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis

    ############################################################################
    # Change the vector scale                                                  #
    ############################################################################
    a.scale = 2.0
    a.scale = 5.0
    a.scale = 1.5
    a.scale = 0.0
    a.scale = -1.5
    a.scale = -2.0
    a.scale = -5.0

    ############################################################################
    # Change the vector typeiiiiiii                                            #
    ############################################################################
    a.type = 0 # same as a.type = 'arrows'
    a.type = 1 # same as a.type = 'barbs'
    a.type = 2 # same as a.type = 'solidarrows'

    ############################################################################
    # Change the vector reference                                              #
    ############################################################################
    a.reference = 10.
    a.reference = 100.
    a.reference = 4.
    a.reference = 5.

    ############################################################################
    # Change the vector alignment                                              #
    ############################################################################
    a.alignment = 'head' # same as a.alignment = 0
    a.alignment = 'center' # same as a.alignment = 1
    a.alignment = 'tail' # same as a.alignment = 2

    ############################################################################
    # Change the vector line                                                   #
    ############################################################################
    a.line = 0 # same as 'solid'
    a.line = 1 # same as 'dash'
    a.line = 2 # same as 'dot'
    a.line = 3 # same as 'dash-dot'
    a.line = 4 # same as 'long-dash'
    a.line = None # use default line

    ############################################################################
    # Change the vector line color                                             #
    ############################################################################
    a.linecolor = (77)
    a.linecolor = 16
    a.linecolor = 44 # same as a.color = (44)
    a.linecolor = None

    x.clear() # clear the VCS Canvas
    x.vector(u, v, a,'default') # plot vector using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,u,v) # plot vector template 't', outline 'a', and arrays 'u':'v'
    x.clear() # clear the VCS Canvas
    x.vector(a,u,v,t) # plot using outline 'a', array 'u':'v', and template 't'

    x.show('line') # show the list of line secondary objects
    l = x.getline('red') # get line 'red'
    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isline(l): # check to see if it is a line
        print 'Yes, this is a line object.'
    l.list() # list the line's attributes and values

    ###########################################################################
    # Use the create line object 'm' from above and modify the line object    #
    ###########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.style = 'square' # change the line type
    l.width = 4 # change the line size

    x.show('vector') # show list of vector
    r = x.createvector('test2','quick') # create vector 'test2'
    x.show('vector') # show list of vector
    x.removeobject(r) # remove vector 'test2'
    x.show('vector') # show list of vector

    #########################################################################
    # to see how x.update and x.mode work, see testoutline.py               #
    #########################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '*************************************************'
    print '****** ******'
    print '****** VECTOR COMPLETED ******'
    print '****** ******'
    print '*************************************************'

if __name__ == "__main__":
    examplevector()
{% endhighlight %}

<a name="xvsy"></a>

###XvsY Graphics Method Example:

{% highlight python %}
#
# Example XvsY (GXY) module
#
############################################################################
#                                                                          #
# Module: examplexvsy module                                               #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's XvsY graphics method.                  #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplexvsy():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    u = f.getslab('u') # get slab u
    v = f.getslab('v') # get slab v
    x = vcs.init() # construct vcs canvas

    x.plot(u, v, 'default','xvsy','quick') # plot slabs the old way
    x.geometry(450,337,100,0) # change the geometry and location

    a = x.getxvsy('quick') # get 'quick' xvsy
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isxvsy(a): # test object 'a' if xvsy
        print 'Yes, this is an xvsy graphics method'
    a.list() # list the xvsy's attributes and values

    a.script('test','w') # save 'quick' xvsy as a Python script

    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis

    ############################################################################
    # Change the xvsy line                                                     #
    ############################################################################
    a.line = 0 # same as 'solid'
    a.line = 1 # same as 'dash'
    a.line = 2 # same as 'dot'
    a.line = 3 # same as 'dash-dot'
    a.line = 4 # same as 'long-dash'

    ############################################################################
    # Change the xvsy line color                                               #
    ############################################################################
    a.linecolor = (77)
    a.linecolor = 16
    a.linecolor = 44 # same as a.color = (44)
    a.linecolor = None

    ############################################################################
    # Change the xvsy marker                                                   #
    ############################################################################
    a.marker = 1 # Same as a.marker = 'dot'
    a.marker = 2 # Same as a.marker = 'plus'
    a.marker = 3 # Same as a.marker = 'star'
    a.marker = 4 # Same as a.marker = 'circle'
    a.marker = 5 # Same as a.marker = 'cross'
    a.marker = 6 # Same as a.marker = 'diamond'
    a.marker = 7 # Same as a.marker = 'triangle_up'
    a.marker = 8 # Same as a.marker = 'triangle_down'
    a.marker = 9 # Same as a.marker = 'triangle_left'
    a.marker = 10 # Same as a.marker = 'triangle_right'
    a.marker = 11 # Same as a.marker = 'square'
    a.marker = 12 # Same as a.marker = 'diamond_fill'
    a.marker = 13 # Same as a.marker = 'triangle_up_fill'
    a.marker = 14 # Same as a.marker = 'triangle_down_fill'
    a.marker = 15 # Same as a.marker = 'triangle_left_fill'
    a.marker = 16 # Same as a.marker = 'triangle_right_fill'
    a.marker = 17 # Same as a.marker = 'square_fill'
    a.marker = None # Draw no markers

    ############################################################################
    # Change the xvsy marker color                                             #
    ############################################################################
    a.marker = 'dot'
    a.markercolor = 16
    a.markercolor = 44 # same as a.markercolor = (44)
    a.markercolor = None

    ############################################################################
    # Change the xvsy marker size                                              #
    ############################################################################
    a.markersize = 5
    a.markersize = 55
    a.markersize = 10
    a.markersize = 100
    a.markersize = 300
    a.markersize = None

    x.clear() # clear the VCS Canvas
    x.xvsy(u, v, a,'default') # plot xvsy using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,u,v) # plot xvsy template 't', outline 'a', and arrays 'u':'v'
    x.clear() # clear the VCS Canvas
    x.xvsy(a,u,v,t) # plot using outline 'a', array 'u':'v', and template 't'

    x.show('line') # show the list of line secondary objects
    l = x.getline('red') # get line 'red'
    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isline(l): # check to see if it is a line
        print 'Yes, this is a line object.'
    l.list() # list the line's attributes and values

    ###########################################################################
    # Use the create line object 'm' from above and modify the line object    #
    ###########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.style = 'dot' # change the line type
    l.width = 4 # change the line size

    x.show('marker') # show the list of marker secondary objects
    m = x.getmarker('red') # get marker 'red'
    if x.issecondaryobject(m): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.ismarker(m): # check to see if it is a fill area
        print 'Yes, this is a marker object.'
    m.list() # list the marker's attributes and values

    ###########################################################################
    # Use the create marker object 'm' from above and modify the line object  #
    ###########################################################################
    a.marker = m # use the marker object
    m.list() # list the marker object attributes and values
    m.color = 44 # change the marker color
    m.type = 'square' # change the marker type
    m.size = 20 # change the marker size

    x.show('xvsy') # show list of xvsy
    r = x.createxvsy('test2','quick') # create xvsy 'test2'
    x.show('xvsy') # show list of xvsy
    x.removeobject(r) # remove xvsy 'test2'
    x.show('xvsy') # show list of xvsy

    #####################################################################
    # to see how x.update and x.mode work, see testoutline.py           #
    #####################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '**********************************************'
    print '****** ******'
    print '****** XvsY COMPLETED ******'
    print '****** ******'
    print '*********************************************'

if __name__ == "__main__":
    examplexvsy()
{% endhighlight %}


<a name="xyvsy"></a>

###Xyvsy Graphics Method Example:

{% highlight python %}
#
# Example Xyvsy (GXy) module
#
############################################################################
#                                                                          #
# Module: examplexyvsy module                                              #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's Xyvsy graphics method.                 #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplexyvsy():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    u = f.getslab('u') # get slab u
    x = vcs.init() # construct vcs canvas

    x.plot(u, 'default','xyvsy','quick') # plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    a = x.getxyvsy('quick') # get 'quick' xyvsy
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isxyvsy(a): # test object 'a' if xyvsy
        print 'Yes, this is an xyvsy graphics method'
    a.list() # list the xyvsy's attributes and values

    a.script('test','w') # save 'quick' xyvsy as a Python script

    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis

    ############################################################################
    # Change the xyvsy line                                                    #
    ############################################################################
    a.line = 0 # same as 'solid'
    a.line = 1 # same as 'dash'
    a.line = 2 # same as 'dot'
    a.line = 3 # same as 'dash-dot'
    a.line = 4 # same as 'long-dash'

    ############################################################################
    # Change the xyvsy line color                                              #
    ############################################################################
    a.linecolor = (77)
    a.linecolor = 16
    a.linecolor = 44 # same as a.color = (44)
    a.linecolor = None

    ############################################################################
    # Change the xyvsy marker                                                  #
    ############################################################################
    a.marker = 1 # Same as a.marker = 'dot'
    a.marker = 2 # Same as a.marker = 'plus'
    a.marker = 3 # Same as a.marker = 'star'
    a.marker = 4 # Same as a.marker = 'circle'
    a.marker = 5 # Same as a.marker = 'cross'
    a.marker = 6 # Same as a.marker = 'diamond'
    a.marker = 7 # Same as a.marker = 'triangle_up'
    a.marker = 8 # Same as a.marker = 'triangle_down'
    a.marker = 9 # Same as a.marker = 'triangle_left'
    a.marker = 10 # Same as a.marker = 'triangle_right'
    a.marker = 11 # Same as a.marker = 'square'
    a.marker = 12 # Same as a.marker = 'diamond_fill'
    a.marker = 13 # Same as a.marker = 'triangle_up_fill'
    a.marker = 14 # Same as a.marker = 'triangle_down_fill'
    a.marker = 15 # Same as a.marker = 'triangle_left_fill'
    a.marker = 16 # Same as a.marker = 'triangle_right_fill'
    a.marker = 17 # Same as a.marker = 'square_fill'
    a.marker = None # Draw no markers

    ############################################################################
    # Change the xyvsy marker color                                            #
    ############################################################################
    a.marker = 'dot'
    a.markercolor = 16
    a.markercolor = 44 # same as a.markercolor = (44)
    a.markercolor = None

    ############################################################################
    # Change the xyvsy marker size                                             #
    ############################################################################
    a.markersize = 5
    a.markersize = 55
    a.markersize = 10
    a.markersize = 100
    a.markersize = 300
    a.markersize = None

    x.clear() # clear the VCS Canvas
    x.xyvsy(u, a,'default') # plot xyvsy using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,u) # plot xyvsy template 't', outline 'a', and arrays 'u':'v'
    x.clear() # clear the VCS Canvas
    x.xyvsy(a,u,t) # plot using outline 'a', array 'u':'v', and template 't'

    x.show('line') # show the list of line secondary objects
    l = x.getline('red') # get line 'red'
    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isline(l): # check to see if it is a line
        print 'Yes, this is a line object.'
    l.list() # list the line's attributes and values

    ###########################################################################
    # Use the create line object 'm' from above and modify the line object    #
    ###########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.style = 'dot' # change the line type
    l.width = 4 # change the line size

    x.show('marker') # show the list of marker secondary objects
    m = x.getmarker('red') # get marker 'red'
    if x.issecondaryobject(m): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.ismarker(m): # check to see if it is a fill area
        print 'Yes, this is a marker object.'
    m.list() # list the marker's attributes and values

    ###########################################################################
    # Use the create marker object 'm' from above and modify the line object  #
    ###########################################################################
    a.marker = m # use the marker object
    m.list() # list the marker object attributes and values
    m.color = 44 # change the marker color
    m.type = 'square' # change the marker type
    m.size = 20 # change the marker size

    x.show('xyvsy') # show list of xyvsy
    r = x.createxyvsy('test2','quick') # create xyvsy 'test2'
    x.show('xyvsy') # show list of xyvsy
    x.removeobject(r) # remove xyvsy 'test2'
    x.show('xyvsy') # show list of xyvsy

    ###################################################################
    # to see how x.update and x.mode work, see testoutline.py         #
    ###################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '***********************************************'
    print '****** ******'
    print '****** Xyvsy COMPLETED ******'
    print '****** ******'
    print '***********************************************'

if __name__ == "__main__":
    examplexyvsy()
{% endhighlight %}

<a name="yxvsx"></a>

###Yxvsx Graphics Method Example:

{% highlight python %}
#
# Example Yxvsx (GYx) module
#
############################################################################
#                                                                          #
# Module: exampleyxvsx module                                              #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's Yxvsx graphics method.                 #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def exampleyxvsx():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    u = f.getslab('u') # get slab u
    x = vcs.init() # construct vcs canvas

    x.plot(u, 'default','yxvsx','quick') # plot slab the old way
    x.geometry(450,337,100,0) # change the geometry and location

    a = x.getyxvsx('quick') # get 'quick' yxvsx
    if x.isgraphicsmethod(a): # test object 'a' for graphics method
        print 'Yes, this is a graphics method'
    if x.isyxvsx(a): # test object 'a' if yxvsx
        print 'Yes, this is an yxvsx graphics method'
    a.list() # list the yxvsx's attributes and values

    a.script('test','w') # save 'quick' yxvsx as a Python script

    a.xticlabels('','') # remove the x-axis
    a.xticlabels('*') # put the x-axis

    ############################################################################
    # Change the yxvsx line                                                    #
    ############################################################################
    a.line = 0 # same as 'solid'
    a.line = 1 # same as 'dash'
    a.line = 2 # same as 'dot'
    a.line = 3 # same as 'dash-dot'
    a.line = 4 # same as 'long-dash'

    ############################################################################
    # Change the yxvsx line color                                              #
    ############################################################################
    a.linecolor = (77)
    a.linecolor = 16
    a.linecolor = 44 # same as a.color = (44)
    a.linecolor = None

    ############################################################################
    # Change the yxvsx marker                                                  #
    ############################################################################
    a.marker = 1 # Same as a.marker = 'dot'
    a.marker = 2 # Same as a.marker = 'plus'
    a.marker = 3 # Same as a.marker = 'star'
    a.marker = 4 # Same as a.marker = 'circle'
    a.marker = 5 # Same as a.marker = 'cross'
    a.marker = 6 # Same as a.marker = 'diamond'
    a.marker = 7 # Same as a.marker = 'triangle_up'
    a.marker = 8 # Same as a.marker = 'triangle_down'
    a.marker = 9 # Same as a.marker = 'triangle_left'
    a.marker = 10 # Same as a.marker = 'triangle_right'
    a.marker = 11 # Same as a.marker = 'square'
    a.marker = 12 # Same as a.marker = 'diamond_fill'
    a.marker = 13 # Same as a.marker = 'triangle_up_fill'
    a.marker = 14 # Same as a.marker = 'triangle_down_fill'
    a.marker = 15 # Same as a.marker = 'triangle_left_fill'
    a.marker = 16 # Same as a.marker = 'triangle_right_fill'
    a.marker = 17 # Same as a.marker = 'square_fill'
    a.marker = None # Draw no markers

    ############################################################################
    # Change the yxvsx marker color                                            #
    ############################################################################
    a.marker = 'dot'
    a.markercolor = 16
    a.markercolor = 44 # same as a.markercolor = (44)
    a.markercolor = None

    ############################################################################
    # Change the yxvsx marker size                                             #
    ############################################################################
    a.markersize = 5
    a.markersize = 55
    a.markersize = 10
    a.markersize = 100
    a.markersize = 300
    a.markersize = None

    x.clear() # clear the VCS Canvas
    x.yxvsx(u, a,'default') # plot yxvsx using 'default' template

    x.show('template') # show the list of templates
    t = x.createtemplate('test') # create template 'test' from 'default' template
    if x.istemplate(t): # test whether 't' is a template or not
        x.show('template') # show the list of templates

    x.clear() # clear the VCS Canvas
    x.plot(t,a,u) # plot yxvsx template 't', outline 'a', and arrays 'u':'v'
    x.clear() # clear the VCS Canvas
    x.yxvsx(a,u,t) # plot using outline 'a', array 'u':'v', and template 't'

    x.show('line') # show the list of line secondary objects
    l = x.getline('red') # get line 'red'
    if x.issecondaryobject(l): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.isline(l): # check to see if it is a line
        print 'Yes, this is a line object.'
    l.list() # list the line's attributes and values

    ###########################################################################
    # Use the create line object 'm' from above and modify the line object    #
    ###########################################################################
    a.line = l # use the line object
    l.list() # list the line object attributes and values
    l.color = 44 # change the line color
    l.style = 'dot' # change the line type
    l.width = 4 # change the line size

    x.show('marker') # show the list of marker secondary objects
    m = x.getmarker('red') # get marker 'red'
    if x.issecondaryobject(m): # check to see if it is a secondary object
        print 'Yes, this is a secondary object.'
    if x.ismarker(m): # check to see if it is a fill area
        print 'Yes, this is a marker object.'
    m.list() # list the marker's attributes and values

    ###########################################################################
    # Use the create marker object 'm' from above and modify the line object  #
    ###########################################################################
    a.marker = m # use the marker object
    m.list() # list the marker object attributes and values
    m.color = 44 # change the marker color
    m.type = 'square' # change the marker type
    m.size = 20 # change the marker size

    x.show('yxvsx') # show list of yxvsx
    r = x.createyxvsx('test2','quick') # create yxvsx 'test2'
    x.show('yxvsx') # show list of yxvsx
    x.removeobject(r) # remove yxvsx 'test2'
    x.show('yxvsx') # show list of yxvsx

    ##################################################################
    # to see how x.update and x.mode work, see testoutline.py        #
    ##################################################################
    #x.update()
    #x.mode = 1
    #x.mode = 0
    print '***********************************************'
    print '****** ******'
    print '****** Yxvsx COMPLETED ******'
    print '****** ******'
    print '***********************************************'

if __name__ == "__main__":
    exampleyxvsx()
{% endhighlight %}

<a name="colormap"></a>

###Colormap Example:

{% highlight python %}
#
# Example Colormap (Cp) module
#
############################################################################
#                                                                          #
# Module: examplecolormap module                                           #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's color map.                             #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplecolormap():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('example.nc') # open clt file
    s = f.getslab('clt') # get slab clt
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','isofill','quick')# plot slab the old way
    x.geometry(450,337,0,0) # change the geometry

    x.setcolormap("AMIP") # change the colormap

    ############################################################
    # Change the color map cell 31.                            #
    ############################################################
    x.setcolorcell(31,0,0,0)
    x.setcolorcell(31,100,0,0)
    x.setcolorcell(31,0,100,0)
    x.setcolorcell(31,0,0,100)
    x.setcolorcell(31,100,100,100)
    x.setcolorcell(31,70,70,70)

    #################################################################
    # NOTE:                                                         #
    # The colormapgui command will only work if the display         #
    # depth is set to 8-bit pseudo color. The next release          #
    # will allow for the colormap's graphical user interface        #
    # (GUI) and the animation's GUI to work in 16-, 24-, or         #
    # 32-bit True color visual classes.                             #
    #################################################################
    x.colormapgui()


    print '*****************************************************'
    print '****** ******'
    print '****** COLORMAP COMPLETED ******'
    print '****** ******'
    print '*****************************************************'


if __name__ == "__main__":
    examplecolormap()
{% endhighlight %}

<a name="hardcopy"></a>

###Hardcopy Example:

{% endhighlight %}python
#
# Example Hardcopy module
#
############################################################################
#                                                                          #
# Module: examplehardcopy module                                           #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Exmaple use of VCS's hard copy.                             #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def examplehardcopy():
    import vcs,cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    s = f.getslab('clt') # get slab clt
    x = vcs.init() # construct vcs canvas

    x.plot(s,'default','isofill','quick', bg = 1) # plot slab the old way, but in
    background
    x.gif('test') # generate gif file
    x.postscript('test') # generate postscript file
    x.cgm('test') # generate cgm file
    x.raster(`test') # generate a raster file

    x.setcolormap("AMIP") # change the colormap
    x.clear() # clear all segments

    t1 = x.createtemplate('test1','AMIP_1of2') # create template 'test' from AMIPDUD
    t2 = x.createtemplate('test2','AMIP_2of2') # create template 'test' from AMIPDUD
    isof = x.createisofill('test') # create isofill graphics method from default
    isol = x.createisoline('test') # create isoline graphics method from default

    ######################################################################
    # draw isofill plot on top, then an isoline plot on the bottom       #
    ######################################################################
    x.plot(s,t1,isof, bg = 1) # generate isofill plot in background
    x.plot(s,t2, isol, bg = 1) # generate isoline plot in background
    x.gif('test2.gif') # generate gif file
    x.postscript('test2.ps') # generate postscript file
    x.cgm('test2.cgm') # generate cgm file

    x.clear() # clear all segments

    ######################################################################
    # draw isofill plot, then overlay an isoline plot                    #
    ######################################################################
    x.plot(s, isof, bg = 1) # generate isofill plot
    x.plot(s, isol, 'default', bg = 1) # generate isoline plot
    x.gif('test3.gif') # generate gif file

    x.clear() # clear all segments
    x.setcolormap("default") # change colormap to default
    x.plot(s,bg = 1) # plot boxfill
    x.postscript('test4.ps') # create a postscript file
    x.('test4.ps') # generate a gif file from the postscript file

    print '*****************************************************'
    print '****** ******'
    print '****** HARDCOPY COMPLETED ******'
    print '****** ******'
    print '*****************************************************'


if __name__ == "__main__":
	examplehardcopy()
```

<a name="picture_template"></a>

###Picture Template Example:

{% highlight python %}                                                                           
# Example Picture Template (P) module
#
############################################################################
#                                                                          #
# Module: exampletemplate module                                           #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Example use of VCS's template object.                       #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
                                                                          
                                                                          
                                                                          
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                              #
#                                                                          #
############################################################################
def exampletemplate():
    import vcs, cdms2 # import vcs and cdms2

    f = cdms2.open('clt.nc') # open clt file
    s = f.getslab('clt') # get slab clt
    x = vcs.init() # construct vcs canvas

    x.show('template') # show the list of templates
    t = x.createtemplate('test','AMIP') # create template 'test' from AMIP
    x.show('template') # show the list of templates

    t.script('test','w') # save test template as a Python script

    g = x.createisofill('test') # create isofill 'test' from 'default' isofill

    x.plot(g,s,t) # make isofill plot
    # x.isofill(g,s,t) # make isofill plot


    #############################################################################
    # Show the many different ways to show the template members (attributes)    #
    # and their values.                                                         #
    #############################################################################
    t.list() # list the templates members
    t.list('text') # list only text members, same as t.list('Pt')
    t.list('format') # list only format members, same as t.list('Pf')
    t.list('xtickmarks') # list only xtickmarks members, same as t.list('Pxt')
    t.list('ytickmarks') # list only ytickmarks members, same as t.list('Pyt')
    t.list('xlabels') # list only xlabels members, same as t.list('Pxl')
    t.list('ylabels') # list only ylabels members, same as t.list('Pyl')
    t.list('boxeslines') # list only boxeslines members, same as t.list('Pbl')
    t.list('legend') # list only legend member, same as t.list('Pls')
    t.list('data') # list only data member, same as t.list('Pds')
    t.list('file') # list only file member and its values
    t.file.list() # list only file member and its values
    t.list('mean') # list only mean member and its values
    t.mean.list() # list only mean member and its values

    #############################################################################
    # The screen x and y positions on the screen are normalized between 0 and 1 #
    # for both the x and y axis.                                                #
    #############################################################################
    t.mean.priority = 0 # remove the "Mean" text from the plot
    t.mean.priority = 1 # re-display the "Mean" text on the plot
    t.mean.x = 0.5 # move the "Mean" text to x-axis center
    t.mean.y = 0.5 # move the "Mean" text to y-axis center

    #############################################################################
    # Position the data in front of the "Mean" text, then move the "Mean" text  #
    # in front of the data.                                                     #
    #############################################################################
    t.data.priority = 2
    t.data.priority = 3

    #############################################################################
    # Change the font representation for the "Mean" text.                       #
    # You can set the text by using text objects or text names.                 #
    #############################################################################
    tt = x.createtexttable('test')
    to = x.createtextorientation('test')
    t.mean.texttable = tt # set texttable by using texttable object
    t.mean.textorientation = 'test' # set textorientation by using textorientation
    name
    t.mean.list() # show the mean member and their new values
    tt.font = 2 # change the font
    to.height = 40 # change the height

    #############################################################################
    # Change the legend space.                                                  #
    #############################################################################
    t.legend.list() # list the legend members
    x.mode = 0 # turn the automatic update off
    t.legend.x1 = 0.85
    t.legend.y1 = 0.90
    t.legend.x2 = 0.95
    t.legend.y2 = 0.16
    x.update()

    print '*****************************************************'
    print '****** ******'
    print '****** TEMPLATE COMPLETED ******'
    print '****** ******'
    print '*****************************************************'

if __name__ == "__main__":
    exampletemplate()
{% endhighlight %}

<a name="simple_animation"></a>

###Simple Animation Example:

{% highlight python %}
#
# Simple animation module
#
############################################################################
#                                                                          #
# Module: simpleanimation module                                           #
#                                                                          #
# Copyright: 2000, Regents of the University of California                 #
# This software may not be distributed to others without                   #
# permission of the author.                                                #
#                                                                          #
# Author: Dean N. Williams, Lawrence Livermore National Laboratory         #
# williams13@llnl.gov                                                      #
#                                                                          #
# Description: Simple animation example.                                   #
# NOTE:                                                                    #
# The animation module will only work if the display                       #
# depth is set to 8-bit pseudo color. The next release                     #
# will allow for the animation's graphical user                            #
# interface (GUI) and the colormap's GUI to display                        #
# in 16-, 24-, or 32-bit True color visual classess.                       #
#                                                                          #
# Version: 1.0                                                             #
#                                                                          #
############################################################################
#
#
#
############################################################################
#                                                                          #
# Import: vcs and cdms2 modules.                                           #
#                                                                          #
############################################################################
def simpleanimation():
    import vcs,cdms2 # import vcs and cdms

    #####################################################################
    # See the CDMS document on how to ingest data. Also see the CU and  #
    # the Numeric documents on alternative ways to import data into VCS #
    #####################################################################

    f = cdms2.openDataset('example.nc') # open example file
    clt = f.variables['clt'] # get variable clt
    s = clt[0] # get clt data

    ##################################################################
    # At the moment, VCS can only animate one variable at a time.    #
    ##################################################################
    x = vcs.init() # initialize vcs
    x.plot(s,variable = clt) # plot data using default values
    x.animate()
    print '*********************************************************************'
    print '****** ******'
    print '****** SIMPLE ANIMATION COMPLETED ******'
    print '****** ******'
    print '*********************************************************************'

if __name__ == "__main__":
    simpleanimation()
{% endhighlight %}

<a name="vcs3D_animation"></a>

### Simple Animation Example Using vcs3D:

{% highlight python %}
#
# When the window appears, click in the 'configure' button and then the 'animate' button.   
# You can then click on the 'run' button to start the animation.
# The most relevant plot configuration buttons are 'Basemap Opacity', 'Choose Colormap', 'Toggle Colorbar', and 'Scale Colormap'.   
# The animation is saved to disk when the "record" button is toggled off.  
# Shift-rightclick for point query operations.
#

def simpleanimation():
	import vcs, cdms2, sys
	x = vcs.init()
	f = cdms2.open(sys.prefix+"/sample_data/clt.nc")   
	v = f["clt"] 
	dv3d = vcs.get3d_scalar()
	x.plot( v, dv3d )
	x.interact()

if __name__ == "__main__":
    simpleanimation()
{% endhighlight %}

<a name="vcs3D_vector"></a>

###Vector Plot Example Using vcs3D:

{% highlight python %}
#
# There are buttons for adjusting the glyph size, density, and colors.   
# It won't animate because the clt dataset contains only one time step for the u,v data.  
#

def simplevector():
	import vcs, cdms2, sys
	x = vcs.init()
	f = cdms2.open(sys.prefix+"/sample_data/clt.nc")  
	v = f["v"]
	u = f["u"]  
	dv3d = vcs.get3d_vector()
	dv3d.BasemapOpacity = 0.15
	x.plot( u, v, dv3d )
	x.interact()

if __name__ == "__main__":
    simplevector()
{% endhighlight %}

<a name="vcs3D_volume"></a>

###Volume Render Example Using vcs3D:

{% highlight python %}
#
# There are buttons for adjusting the transfer function, opacity, colormap, and color scaling of the volume rendering.    
#

def simplevolume():
    import vcs, cdms2, sys
    x = vcs.init()
    f = cdms2.open(sys.prefix+"/sample_data/geos5-sample.nc")  
    u = f["uwnd"]  
    dv3d = vcs.get3d_scalar() 
    dv3d.VerticalScaling = 3.0 
    dv3d.ScaleOpacity = [0.0, 0.8]
    dv3d.ScaleColormap = [-46.0, 45, 1] 
    dv3d.ScaleTransferFunction =  [8.6, 76.7, 1] 
    dv3d.BasemapOpacity = [0.5]
    dv3d.XSlider = vcs.off 
    dv3d.ZSlider = vcs.off 
    dv3d.YSlider = vcs.off 
    dv3d.ToggleVolumePlot = vcs.on 
    dv3d.ToggleSurfacePlot = vcs.off
    dv3d.Camera={ 'Position': (-161, -171, 279), 'ViewUp': (.29, 0.67, 0.68), 'FocalPoint': (146.7, 8.5, -28.6) } 
    x.plot( u, dv3d )
    x.interact()

if __name__ == "__main__":
    simplevolume()
{% endhighlight %}


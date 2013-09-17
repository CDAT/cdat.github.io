##UVCDAT Plots

We need to identify commonalities between the variosu type of plots in UVCDAT    

This page first describes the various types of plots and their components.

###VCS/CDAT
VCS plots are divided into 3 concepts

* Data: i.e. WHAT you want to plot
* Graphics Method: i.e HOW you want to plot it (isofill,boxfill, contour, etc...)
* Templates: i.e WHERE to plot things

###Data
The data is really a Varialbe i.e data+metadata, that tells the plot what to plot, what the range in both values and spatial (and/or temporal etc...) are

###Graphics Method
The graphics methods describe how the data will be plotted. VCS graphics methods are:

* Boxfill
* Isofill
* Isoline
* Meshfill (a boxfill with irregular boxes/polygons)
* Vector
* Scatter
* 2D: Y(x), X(y), XvsY
* Taylordiagrams (really a special case, probably should be moved to addons)
* Outfill
* Outline

Most graphic methods have a common set of attributes:

* datawc_x1, datawc_x2, datawc_y1, datawc_y2 : which describe the X/Y world coordinate to actually draw
* datawc_timeunits and datawc_calendar: if a axis of the plot variable is a time axis it will convert the axis to these untis/calendar. This will allow plotting data with different units to overlay properly.
* x/yticlabels1/2 : 2 sets of labels to plot can be a simple list of values or a dictionary containing a pair value:text to plot
* x/ymtics1/2 : 2 sets of subticks to draw (no text associated)
* projection : for lat/lon plots
* x/yaxisconvert : axis transformation (when applicable)

###Templates
Templates object describe in detail where things should be drawn, as well as font and lines thickness.    

A full template object is listed bellow but it's most important components are:

* data : with attributes x1,x2,y1,y2 which describe (in %) the area of the page where the data will be drawn (using whatever specified graphic method)
* legend : with attributes x1,x2,y1,y2 which describes in % the area of the page where the legend will be drawn
* title/

example:

    ----------Template (P) member (attribute) listings ----------
    Canvas Mode = 1
    method = P
    name = __temp_15277
    orientation = 0
    member =  file
        priority = 1
        x = 0.0500000007451
        y = 0.0130000002682
        texttable = default
        textorientation = default
    member =  function
        priority = 1
        x = 0.0500000007451
        y = 0.0130000002682
        texttable = default
        textorientation = default
    member =  logicalmask
        priority = 1
        x = 0.0500000007451
        y = 0.0329999998212
        texttable = default
        textorientation = default
    member =  transformation
        priority = 1
        x = 0.0500000007451
        y = 0.0529999993742
        texttable = default
        textorientation = default
    member =  source
        priority = 1
        x = 0.0500000007451
        y = 0.941999971867
        texttable = default
        textorientation = default
    member =  dataname
        priority = 1
        x = 0.0500000007451
        y = 0.922999978065
        texttable = default
        textorientation = default
    member =  title
        priority = 1
        x = 0.15000000596
        y = 0.922999978065
        texttable = default
        textorientation = default
    member =  units
        priority = 1
        x = 0.670000016689
        y = 0.922999978065
        texttable = default
        textorientation = default
    member =  crdate
        priority = 1
        x = 0.75
        y = 0.922999978065
        texttable = default
        textorientation = default
    member =  crtime
        priority = 1
        x = 0.850000023842
        y = 0.922999978065
        texttable = default
        textorientation = default
    ember =  comment1
        priority = 1
        x = 0.10000000149
        y = 0.954999983311
        texttable = default
        textorientation = default
    member =  comment2
        priority = 1
        x = 0.10000000149
        y = 0.975000023842
        texttable = default
        textorientation = default
    member =  comment3
        priority = 1
        x = 0.10000000149
        y = 0.995000004768
        texttable = default
        textorientation = default
    member =  comment4
        priority = 1
        x = 0.10000000149
        y = 0.999000012875
        texttable = default
        textorientation = default
    member =  xname
        priority = 0
        x = 0.5
        y = 0.277000010014
        texttable = default
        textorientation = defcenter
    member =  yname
        priority = 0
        x = 0.0168999992311
        y = 0.420033991337
        texttable = default
        textorientation = defcentup
    member =  zname
        priority = 1
        x = 0.0
        y = 0.995000004768
        texttable = default
        textorientation = default
    member =  tname
        priority = 1
        x = 0.0
        y = 0.995000004768
        texttable = default
        textorientation = default
    member =  xunits
        priority = 0
        x = 0.600000023842
        y = 0.277000010014
        texttable = default
        textorientation = default
    member =  yunits
        priority = 0
        x = 0.019999999553
        y = 0.658999979496
        texttable = default
        textorientation = defcentup
    member =  zunits
        priority = 1
        x = 0.0
        y = 0.995000004768
        texttable = default
        textorientation = default
    member =  tunits
        priority = 1
        x = 0.0
        y = 0.995000004768
        texttable = default
        textorientation = default
    member =  xvalue
        priority = 1
        x = 0.800000011921
        y = 0.941999971867
        format = default
        texttable = default
        textorientation = default
    member =  yvalue
        priority = 1
        x = 0.800000011921
        y = 0.922999978065
        format = default
        texttable = default
        textorientation = default
    member =  zvalue
        priority = 1
        x = 0.800000011921
        y = 0.902999997139
        format = default
        texttable = default
        textorientation = default
    member =  tvalue
        priority = 1
        x = 0.800000011921
        y = 0.883000016212
        format = default
        texttable = default
        textorientation = default
    member =  mean
        priority = 1
        x = 0.0500000007451
        y = 0.899999976158
        format = default
        texttable = default
        textorientation = default
    member =  min
        priority = 1
        x = 0.449999988079
        y = 0.899999976158
        format = default
        texttable = default
        textorientation = default
    member =  max
        priority = 1
        x = 0.25
        y = 0.899999976158
        format = default
        texttable = default
        textorientation = default
    member =  xtic1
        priority = 1
        y1 = 0.259999990463
        y2 = 0.24699999392
        line = default
    member =  xtic2
        priority = 1
        y1 = 0.860000014305
        y2 = 0.871999979019
        line = default
    member =  xmintic1
        priority = 0
        y1 = 0.259999990463
        y2 = 0.256999999285
        line = default
    member =  xmintic2
        priority = 0
        y1 = 0.860000014305
        y2 = 0.862999975681
        line = default
    member =  ytic1
        priority = 1
        x1 = 0.0500000007451
        x2 = 0.0399999991059
        line = default
    member =  ytic2
        priority = 1
        x1 = 0.949999988079
        x2 = 0.959999978542
        line = default
    member =  ymintic1
        priority = 0
        x1 = 0.0500000007451
        x2 = 0.0450000017881
        line = default
    member =  ymintic2
        priority = 0
        x1 = 0.949999988079
        x2 = 0.954999983311
        line = default
    member =  xlabel1
        priority = 1
        y = 0.234999999404
        texttable = default
        textorientation = defcenter
    member =  xlabel2
        priority = 0
        y = 0.870000004768
        texttable = default
        textorientation = defcenter
    member =  ylabel1
        priority = 1
        x = 0.0399999991059
        texttable = default
        textorientation = defright
    member =  ylabel2
        priority = 0
        x = 0.959999978542
        texttable = default
        textorientation = default
    member =  box1
        priority = 1
        x1 = 0.0500000007451
        y1 = 0.259999990463
        x2 = 0.949999988079
        y2 = 0.860000014305
        line = default
    member =  box2
        priority = 0
        x1 = 0.0
        y1 = 0.300000011921
        x2 = 0.920000016689
        y2 = 0.879999995232
        line = default
    member =  box3
        priority = 0
        x1 = 0.0
        y1 = 0.319999992847
        x2 = 0.910000026226
        y2 = 0.860000014305
        line = default
    member =  box4
        priority = 0
        x1 = 0.0
        y1 = 0.0
        x2 = 0.0
        y2 = 0.0
        line = default
    member =  line1
        priority = 0
        x1 = 0.0500000007451
        y1 = 0.560000002384
        x2 = 0.949999988079
        y2 = 0.560000002384
        line = default
    member =  line2
        priority = 0
        x1 = 0.5
        y1 = 0.259999990463
        x2 = 0.5
        y2 = 0.860000014305
        line = default
    member =  line3
        priority = 0
        x1 = 0.0
        y1 = 0.52999997139
        x2 = 0.899999976158
        y2 = 0.52999997139
        line = default
    member =  line4
        priority = 0
        x1 = 0.0
        y1 = 0.990000009537
        x2 = 0.899999976158
        y2 = 0.990000009537
        line = default
    member =  legend
        priority = 1
        x1 = 0.0500000007451
        y1 = 0.129999995232
        x2 = 0.949999988079
        y2 = 0.159999996424
        line = default
        texttable = default
        textorientation = defcenter
    member =  data
        priority = 1
        x1 = 0.0500000007451
        y1 = 0.259999990463
        x2 = 0.949999988079
        y2 = 0.860000014305

###VtDV3D
###Paraview
###Visit

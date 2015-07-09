import cdms2
import cdutil
import vcs

varin = "tas"
model = "MERRA"
# open MERRA

url = 'http://dataserver.nccs.nasa.gov/thredds/dodsC/bypass/CREATE-IP/%s/mon/atmos/%s.ncml' # noqa

f1 = cdms2.open(url % (model, varin))

tas = f1(varin)

tas_global = cdutil.averager(tas, axis='xy', weights=['generate', 'equal'])

tas_global.id = model

x = tas_global

v = vcs.init()
v.setcolormap = 'rainbow'

# Create x vs. y graphics method object and template:

my_gm = v.createyxvsx('my_graph_meth', 'default')

my_tpl = v.createtemplate('my_template', 'default')


# Set plot symbol to square and linestyle to dashed:

my_gm.marker = 5
my_gm.line = 0
my_gm.linecolor = 142


# 150=red 40 = blue  75 green 252 grey

# Set coordinates (normalized units) for lower-left and upper-
#  right bounding box (bbll*, bbur*); set height of font for
#  the overall title (title_fontht), [xy]titles (xytitle_fontht),
#  and for the tick labels (ticklabel_fontht); set length of tick
#  marks (in normalized units):

bbllx = 0.11
bblly = 0.25
bburx = 0.95
bbury = 0.85
title_fontht = 20
xytitle_fontht = 20
ticklabel_fontht = 20
ticklength = 0.01


# Set font to use for the ticklabels (ticklabel_font) and the
#  titles (titles_font):

ticklabel_font = 2
titles_font = 2


# Set conversion factor to multiply font height coordinates by
#  to obtain the value in normalized coordinates.  This is set
#  by trial-and-error:

fontht2norm = 0.0007


# Create text-table and text-orientation objects for x- and
#  y-axis tick labels and using them set font and font height.
#  Also set y-axis tick labels to be vertically aligned at the
#  mid-way point:

ttab_xticklabel = v.createtexttable('xticklabel_ttab', 'default')
ttab_yticklabel = v.createtexttable('yticklabel_ttab', 'default')
tori_xticklabel = v.createtextorientation('xticklabel_tori', 'defcenter')
tori_yticklabel = v.createtextorientation('yticklabel_tori', 'default')

ttab_xticklabel.font = ticklabel_font
ttab_yticklabel.font = ticklabel_font
tori_xticklabel.height = ticklabel_fontht
tori_yticklabel.height = ticklabel_fontht
tori_yticklabel.valign = 'half'


# Create text-combined objects for overall title and axis
#  titles and set font, height, and content:

text_title = v.createtext('title_ttab',
                          'default',
                          'title_tori',
                          'defcenter')

text_title.font = titles_font
text_title.height = title_fontht
text_title.string = model + ' ' + varin

text_xtitle = v.createtext('xtitle_ttab',
                           'default',
                           'xtitle_tori',
                           'defcenter')

text_xtitle.font = titles_font
text_xtitle.height = xytitle_fontht
text_xtitle.string = 'Year'

text_ytitle = v.createtext('ytitle_ttab',
                           'default',
                           'ytitle_tori',
                           'defcentup')

text_ytitle.font = titles_font
text_ytitle.height = xytitle_fontht
text_ytitle.string = 'Cloud %'


# Turn off some default titling fields:

my_tpl.xname.priority = 0
my_tpl.yname.priority = 0
my_tpl.mean.priority = 0
my_tpl.max.priority = 0
my_tpl.min.priority = 0


# Set position of data field, plot box, and x-axis bottom ticks
#  and labels; set text-table and text-orientation of x-axis bottom
#  labels; turn off upper-right set of tick labels:

my_tpl.data.x1 = my_tpl.box1.x1 = bbllx
my_tpl.data.y1 = my_tpl.box1.y1 = bblly
my_tpl.data.x2 = my_tpl.box1.x2 = bburx
my_tpl.data.y2 = my_tpl.box1.y2 = bbury

my_tpl.xtic1.y1 = bblly - ticklength
my_tpl.xtic1.y2 = bblly
my_tpl.xlabel1.y = bblly - (3.0 * ticklength)
my_tpl.xlabel1.texttable = ttab_xticklabel
my_tpl.xlabel1.textorientation = tori_xticklabel

my_tpl.xtic2.priority = 0
my_tpl.ytic2.priority = 0
my_tpl.legend.priority = 0

# Calculate "nice" x-axis labels and set them into the graphics
#  method, with no more than 8 ticks on the axis:

# my_gm.xticlabels1 = vcs.mklabels( vcs.mkscale(min(x), max(x), 8) )


# Calculate "nice" y-axis labels, set them in the graphics method,
#  calculate y-axis title location based on the longest label
#  length, set y-axis ticks and tick label locations, and set
#  text-table and text-orientation for y-axis tick labels:

ylabels = vcs.mklabels(vcs.mkscale(min(x), max(x)))
my_gm.yticlabels1 = ylabels
longest_ylabels = \
    max([len(ylabels.values()[i]) for i in range(len(ylabels))])

my_tpl.ytic1.x1 = bbllx - ticklength
my_tpl.ytic1.x2 = bbllx
my_tpl.ylabel1.x = bbllx - ticklength \
    - (longest_ylabels * ticklabel_fontht * fontht2norm)
my_tpl.ylabel1.texttable = ttab_yticklabel
my_tpl.ylabel1.textorientation = tori_yticklabel


# Position overall title, x-axis title, and y-axis title:

text_title.x = [(bburx - bbllx) / 2.0 + bbllx]
text_title.y = [bbury + (1.7 * title_fontht * fontht2norm)]

text_xtitle.x = [(bburx - bbllx) / 2.0 + bbllx]
text_xtitle.y = [my_tpl.xlabel1.y - (1.7 * title_fontht * fontht2norm)]

text_ytitle.x = [my_tpl.ylabel1.x - (1.6 * title_fontht * fontht2norm)]
text_ytitle.y = [(bbury - bblly) / 2.0 + bblly]


# Render plot, plot overall title, x-axis title, and y-axis title:

v.plot(x, my_gm, my_tpl, name=' ')

v.plot(text_title)
v.plot(text_xtitle)
v.plot(text_ytitle)


# output of the plot:
raw_input()
v.png('%s %s.png' % (model, varin))


# ====== end of file ======

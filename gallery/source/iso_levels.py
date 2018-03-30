import vcs
import cdms2

"""
An example demonstrating the use of templates, as well as the
importance of setting levels appropriately for your visualization.
"""
vcs.download_sample_data_files()

# Let's use an aspect ratio of 2:1 width/height
canvas = vcs.init(size=2)
cdmsfile = cdms2.open(vcs.sample_data + "/geos5-sample.nc")
# Extend the longitude to wrap around
sphu = cdmsfile("sphu", longitude=(0, 360))


# Create a base template and place all of the labels that we want
root_template = vcs.createtemplate("reduced")
root_template.blank(["mean", "max", "min", "zvalue", "dataname", "crtime", "ytic2", "xtic2"])

# Shrink data and box1 a little horizontally
root_template.data.x2 -= .05
root_template.box1.x2 -= .05

# Move the legend to the right side
root_template.legend.x1 = root_template.data.x2 + .01
root_template.legend.x2 = root_template.data.x2 + .03
root_template.legend.y1 = root_template.data.y1
root_template.legend.y2 = root_template.data.y2

# Create a left/top aligned textorientation for the labels
textorientation = vcs.createtextorientation()
textorientation.halign = 'left'
textorientation.valign = 'half'
root_template.legend.textorientation = textorientation.name

# Align title and units to the left side of the data
root_template.title.x = root_template.data.x1
root_template.units.x = root_template.title.x
root_template.units.y = root_template.title.y - .03
root_template.crdate.x = root_template.data.x2
right_align = vcs.createtextorientation()
right_align.halign = "right"
root_template.crdate.textorientation = right_align

# Template Construction

# We want to build our templates to look like this:

"""
------------------------
|        |             |
|  Top   |             |
|________|    Right    |
|        |             |
| Bottom |             |
|________|_____________|
"""


# Top template; off to the left, only the top half of the canvas
top_template = vcs.createtemplate("top", "reduced")

# Resize and move template
# Scale accepts a "font" keyword argument that will prevent it from scaling the fonts
top_template.scale(.5, "y", font=False)
top_template.scale(.25, "x", font=False)
top_template.move(.325, "y")

# Adjust the axis units
top_template.yname.x = .025
top_template.xname.y -= .015

# Nudge the template a bit to the left
top_template.move(-.01, "x")

# Adjust the axis value labels
top_template.xlabel1.y = .565
top_template.ylabel1.x = .036


# Bottom template; exactly the same as top, but lower down
bottom_template = vcs.createtemplate("bottom", "top")
bottom_template.move(-.475, "y")


# Template for the right side (much larger than top/bottom)
right_template = vcs.createtemplate("right", "reduced")
right_template.scale(.55, "x", font=False)
right_template.move(.275, "x")

# Scale the template to have a data height that aligns with other two plots
new_height = top_template.data.y2 - bottom_template.data.y1

# Get the % difference
scale_factor = new_height / (right_template.data.y2 - right_template.data.y1)
# Move the template to the correct Y position
ydiff = bottom_template.data.y1 - right_template.data.y1
right_template.move(ydiff, "y")
right_template.scale(scale_factor, "xy", font=False)

# Adjust the labels to line up with top_template
right_template.title.y = top_template.title.y
right_template.units.y = top_template.units.y
right_template.crdate.y = top_template.crdate.y

# Create the graphics methods we'll use

# Show fewer xticlabels in order to actually be able to read them
reduced_labels = vcs.createisofill("reduced", "default")
# You use a dictionary that maps values 0 <= x < 360 to strings
reduced_labels.xticlabels1 = {0: "0", 60: "60E", 120: "120E", 180: "180W",
                              240: "120W", 300: "60W", 360: "0"}

# isofill will use the naive minmax approach
isofill = vcs.createisofill("minmax", "reduced")

# Extract the minimum and maximum levels of sphu
# This will extract the minimum and maximum values from
# all time slices, which may be an issue for your dataset.
# If you want to do an animation, it's a good appraoch.
# If you're just looking at a single time slice, you're better off
# using our automatic level generator.
minval, maxval = vcs.minmax(sphu)
# Automatically create levels based on a minimum and maximum value
# It will round to surround the min and max
isofill.levels = vcs.mkscale(minval, maxval)
# Automatically retrieve colors for the scale
isofill.fillareacolors = vcs.getcolors(isofill.levels)

# isofill2 uses curated levels
# I used the built-in levels, took a look at the visualization, and selected
# the band of values that took up the most space in the heatmap.
isofill2 = vcs.createisofill("manual", "reduced")
isofill2.levels = vcs.mkscale(.2 * 10 ** -5, .5 * 10 ** -5)
# Since there are values outside of the upper and lower bounds I provided,
# let's turn on extensions to allow those values to be accomodated for.
isofill2.ext_1 = True
isofill2.ext_2 = True
isofill2.fillareacolors = vcs.getcolors(isofill2.levels)


# Now we'll drop some labels onto the plots...
plot_titles = vcs.createtext()
plot_titles.string = ["All Times Min/Max Levels", "Autolevels", "Manual Levels"]
left_center = (top_template.data.x2 + top_template.data.x1) / 2.
right_center = (right_template.data.x2 + right_template.data.x1) / 2.
# Center on the plots
plot_titles.x = [left_center, left_center, right_center]
# Place above the variable title
plot_titles.y = [top_template.title.y + .05, bottom_template.title.y + .05, right_template.title.y + .05]
plot_titles.halign = "center"
plot_titles.height = 19
plot_titles.font = "Clarendon"
canvas.plot(plot_titles)

# This will use the minmax level range, and provide the least detail
canvas.plot(sphu, top_template, isofill)
# This will use the automatic levels, and provide good detail
canvas.plot(sphu, bottom_template, reduced_labels)
# This will use the manual levels, and provide the most detail for lower
# values, though it loses some of the higher value details.
canvas.plot(sphu, right_template, isofill2)

canvas.png("iso_levels.png", height=600)

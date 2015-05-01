import vcs
import cdms2

# Open data file
f = cdms2.open('./plot_colors.nc')

# Get the variable
s = f("cfsr")

#Filter the variable by lat and long
s = s(lat = (25., 75.6), lon = (25., 85.))

# Initialize a canvas
x = vcs.init()
# Set canvas resolution

# Set canvas colormap
x.setcolormap("bl_to_darkred")

# Set up some levels to filter data by
levs = [-1e20, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -.5, 0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 1e20]

# Retrieve the colors that would best spread the supplied range of colors
cols = vcs.getcolors(levs, range(239, 11, -1))

# Create and initilize an isofill
iso = x.createisofill()
iso.levels = levs

# Draw the extension arrows on either side of the color legend
iso.ext_1 = "y"
iso.ext_2 = "y"

# Set the fill colors to the ones we retrieved earlier
iso.fillareacolors = cols

# Create a label
txt = x.createtext()
txt.string = "Moscow"
txt.height = 20
txt.x = .28
txt.y = .62

# Create another label
txt2 = x.createtext()
txt2.x = .73
txt2.y = .33
txt2.string = "Pakistan"
txt2.priority = 10
txt2.height = 20
# Change the color so we can see this label a little better
txt2.color = 242
txt2.angle = -45

# Plot the cfsr variable from lat 25 to lat 75.6, and from lon 25 to lon 85 using the isofill defined above
x.plot(s, iso, continents = 4)

# Create, initialize, and plot an isoline to delimit the fill zones
lines = vcs.createisoline()
lines.levels = levs
x.plot(s, lines)

# Plot the labels we defined
x.plot(txt)
x.plot(txt2)

x.png("plot_colors.png")

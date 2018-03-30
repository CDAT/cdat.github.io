import vcs
import cdms2

# Open data file
f = cdms2.open('./plot_wave.nc')

# Get the variable
s = f("t_dep")

# Filter the variable based on latitude
s = s(latitude = (0, 90.))

# Initialize the canvas
x = vcs.init()

# Set the size of the canvas


# Change the colormap
x.setcolormap("bl_to_darkred")

# Set up some levels to filter out data
levs = [-1e20, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 1e20]

# Retrieve the colors that would best spread the supplied range of colors
cols = vcs.getcolors(levs, range(25, 239))

# Create and initialize the isofill object
iso = x.createisofill()
iso.levels = levs

# Draw the extension arrows on either side of the color legend
iso.ext_1 = "y"
iso.ext_2 = "y"

# Set the colors to the ones we set up earlier
iso.fillareacolors = cols

# Plot the t_dep variable from lat 0 to lat 90, using the isofill defined above
x.plot(s, iso, continents = 4)

# Create and initialize an isoline object
lines = vcs.createisoline()
lines.levels = levs

# Plot the same data, to outline the isofill colors
x.plot(s, lines)

# Save out a PNG file with the results
x.png('plot_wave.png')


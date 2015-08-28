import cdms2
import cdutil
import vcs
import EzTemplate


varin = "hus"

# latutude bounds for averaging
lat_a = (32, 37)
lat_b = (37, 40)

# longitude bounds for averaging
lon_a = (-118, -122)
lon_b = (-122, -125)

# time bounds for plot
time = ("2005-10-01", "2005-12-31")

path = "hovmoeller_hus.nc"


f = cdms2.open(path)

y = f(varin)

# Slice a
y1 = y(order="10", time=time, latitude=lat_a, longitude=lon_a)

# Slice b
y2 = y(order="10", time=time, latitude=lat_b, longitude=lon_b)

# reverse order of level and time to make horizontal Hovmoeller plot


# average latitude and longitude over specified regions
yave1 = cdutil.averager(y1, axis='xy')
yave2 = cdutil.averager(y2, axis='xy')

cdutil.times.setTimeBoundsDaily(y)

x = vcs.init()
bg = False
iso = x.createisofill()
M = EzTemplate.Multi(rows=2, columns=1)

template = vcs.createtemplate()
template.blank()

template.data.priority = 1
template.box1.priority = 1
template.xtic1.priority = 1
template.xlabel1.priority = 1
template.xlabel1.y = .22
template.xname.priority = 1
template.yname.priority = 1
template.ylabel1.priority = 1

M.template = template.name
M.legend.direction = 'horizontal'
M.margins.left = .07
M.margins.right = .02
M.margins.bottom = .15
M.margins.top = .15
M.legend.thickness = .2
M.legend.stretch = 1.0
M.spacing.vertical = .1
M.spacing.horizontal = .05

x.setcolormap('bl_to_darkred')

levels = [0, .001, .0025, .005, .0075, .01, .025, .05, .075, .1]

# set contour levels
iso.levels = levels
iso.ext_1 = "n"
iso.ext_2 = "y"

# Plot labels
txt = x.createtext()
txt.To.height = 16

txt.x = [.05]  # Will automatically be repeated to match number of strings
txt.y = [.87, .47]

string_format = "Latitude {lat} Longitude {lon}"

txt.string = [string_format.format(lat=lat_a, lon=lon_a),
              string_format.format(lat=lat_b, lon=lon_b)]

t = M.get(legend='none')

yave1.id = varin
yave2.id = varin
lines = vcs.createisoline()

# put labels on isolines? "y' or 'n'
lines.label = 'n'

# add isolines over color fill contours
lines.levels = levels

x.plot(yave1, t, iso, bg=1)

x.plot(yave1, t, lines, bg=1)
t = M.get(legend='none')
# second plot

lines = vcs.createisoline()
x.plot(yave2, t, iso, bg=1)
x.plot(yave2, t, lines, bg=1)

x.plot(txt, bg=1)

# Diagram Title
header = x.createtext()
header.To.height = 24
header.To.halign = "center"
header.To.valign = "top"
header.x = .5
header.y = .95

header.string = ["Specific Humidity (Oct 2005 - Jan 2006)"]

x.plot(header, bg=1)

x.png("hovmuller_hus.png")

################################################################################################# 
# This Python script plots JJA climatology at surface level, which given from one of CMIP5 models
# 
# Ji-Woo Lee, LLNL, August 2016
################################################################################################# 
import cdms2 as cdms
import cdutil
import cdtime
import vcs

#================================================================================================
# Data
#------------------------------------------------------------------------------------------------
# open file from local -- DATA was downloaded from ESGF
odir = '/cmip5_css02/data/cmip5/output1/NIMR-KMA/HadGEM2-AO/historical/mon/atmos/Amon/r1i1p1/pr/1/' # Put your data directory here
nc = 'pr_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'
f = cdms.open(odir+nc)

# Load variable ---
d = f('pr',longitude=(-180,180))*86400. # kg/m2/s1 to mm/day
d.units='mm/day'

# Time period for climatology calculation ---
start_year = 1949
end_year = 2010

start_time = cdtime.comptime(start_year)
end_time =cdtime.comptime(end_year)

# Calculate JJA seasonal climatology ---
d_jja = cdutil.JJA.climatology(d(time=(start_time,end_time)))
d_jja.units = 'mm/day'
d_jja.long_name = 'JJA clim. precip., '+str(start_year)+'-'+str(end_year)
d_jja.id = 'pr'
d_jja.model = 'HadGEM2-AO'

#================================================================================================
# Plot
#------------------------------------------------------------------------------------------------
# Create canvas ---
canvas = vcs.init(geometry=(1200,800))
canvas.open()

# Set plot type ---
iso = canvas.createisofill()

# Color setup ---
levs = range(3,33,3) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
iso.levels = levs
iso.ext_2 ="y"

cmap = vcs.createcolormap("my_colormap", "rainbow") #you can specify which colormap you want to copy from in the second argument
for i in range(255):
  r, g, b, _ = cmap.getcolorcell(i)
  cmap.setcolorcell(i, r, g, b, 50) # Transparency: 0-100
canvas.setcolormap(cmap)

# Plot ---
canvas.plot(d_jja,iso)

# Set title ---
plot_title = vcs.createtext()
plot_title.x = .5
plot_title.y = .98
plot_title.height = 24
plot_title.halign = "center"
plot_title.valign = "top"
plot_title.color="black"
plot_title.string = d_jja.model+' '+'ex2_pr_jja_clim'
canvas.plot(plot_title)

# Drop output as image file ---
canvas.png("example_sfc_pr_jja_clim")

################################################################################################# 
# This Python script plots JJA climatology at 500 hPa level, which given from one of CMIP5 models
# 
# Ji-Woo Lee, LLNL, August 2016
################################################################################################# 

import cdms2 as cdms
import cdutil
import cdtime
import vcs
from cdms2 import MV

#================================================================================================
# Data
#------------------------------------------------------------------------------------------------
# List of variables to plot ---
vars = ['zg','ta','ua','va']
nvar = len(vars)

# Time period ---
start_year = 1949
end_year = 2010
start_time = cdtime.comptime(start_year)
end_time = cdtime.comptime(end_year)

# Dictionary for variables ---
data = {}

# Bring data in ---
for var in vars[0:nvar]:
  print var

  # Open file (In this example case, data was downloaded from ESGF. Please prepare your data) ---
  odir = '/cmip5_css02/data/cmip5/output1/NIMR-KMA/HadGEM2-AO/historical/mon/atmos/Amon/r1i1p1/'+var+'/1/' # Put your data directory here
  nc = var+'_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'
  f = cdms.open(odir+nc)

  # Load variable ---
  d = f(var,lev=50000)

  # Calculate JJA seasonal climatology ---
  data[var] = cdutil.JJA.climatology(d(time=(start_time,end_time)))

  # Close file ---
  f.close()

#================================================================================================
# Plot
#------------------------------------------------------------------------------------------------
# Create canvas ---
canvas = vcs.init(geometry=(1200,800))
canvas.open()
template = canvas.createtemplate()
template.blank(['title','mean','min','max','dataname','crdate','crtime','units']) ## Turn off additional information
#template.list() ## This commend could give list of items 

# Set ploting range ---
lat1=-60
lat2=80
lon1=0
lon2=360

# Wind speed ---
data['wnd'] = MV.sqrt(data['ua']**2+data['va']**2)
iso = canvas.createisofill()
iso.datawc_x1 = lon1
iso.datawc_x2 = lon2
iso.datawc_y1 = lat1
iso.datawc_y2 = lat2
canvas.setcolormap('blue_to_orange')
canvas.plot(data['wnd'],iso,template)

# Geopotential height field ---
lines1 = vcs.createisoline()
lines1.datawc_x1 = lon1
lines1.datawc_x2 = lon2
lines1.datawc_y1 = lat1
lines1.datawc_y2 = lat2
lines1.linecolors = ['black']
lines1.line=['solid']
lines1.label = 'y'
lines1.textcolors=['black']
canvas.plot(data['zg'],lines1,template)

# T field ---
lines2 = vcs.createisoline()
lines2.datawc_x1 = lon1
lines2.datawc_x2 = lon2
lines2.datawc_y1 = lat1
lines2.datawc_y2 = lat2
lines2.linecolors = ['red']
lines2.line=['dot']
lines2.label = 'y'
lines2.textcolors=['red']
canvas.plot(data['ta'],lines2,template)

# Plot wind field (vector) ---
vec = vcs.createvector()
ua2 = data['ua'][...,::3,::3] ## Resample U field to reduce vector density to half
va2 = data['va'][...,::3,::3] ## Resample V filed to reduce vector density to half
vec.datawc_x1 = lon1
vec.datawc_x2 = lon2
vec.datawc_y1 = lat1
vec.datawc_y2 = lat2
canvas.plot(ua2,va2,vec,template)

# Set title ---
plot_title = vcs.createtext()
plot_title.x = .5
plot_title.y = .98
plot_title.height = 24
plot_title.halign = 'center'
plot_title.valign = 'top'
plot_title.color='black'
plot_title.string = 'JJA mean climatology, 500 hPa'
canvas.plot(plot_title)

# Save output as image file ---
canvas.png('example_500mb_wnd_ts_gph_jja_clim')

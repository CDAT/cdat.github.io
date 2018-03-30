import cdms2 as cdms 
import string
import cdutil
import cdtime
import vcs
import numpy as np
import genutil

#=================================================
# PART 0 : User setting
#-------------------------------------------------
# plot_area is domain selector, 
#           available options are: global / asia
#plot_area = "asia"
plot_area = "global" 

start_year = 1950
end_year = 2000
#-------------------------------------------------

if plot_area == "global":
  lat1=-60
  lat2=80
  lon1=0
  lon2=360
  lint=20 # line interval
elif plot_area == "asia":
  lat1=-10
  lat2=55
  lon1=65
  lon2=155
  lint=10 # line interval

#=================================================
# PART 1 : Field to plot --- prepare data array
#-------------------------------------------------
data_dir='/work/lee1043/cdat/sample_input/' # Put your input directory path here

# Below files were downloaded from ESGF
file1 = 'pr_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'
file2 = 'ua_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'
file3 = 'va_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'
file4 = 'zg_Amon_HadGEM2-AO_historical_r1i1p1_186001-200512.nc'

f1 = cdms.open(data_dir+file1)
f2 = cdms.open(data_dir+file2)
f3 = cdms.open(data_dir+file3)
f4 = cdms.open(data_dir+file4)

d1 = f1('pr')*86400.
d2 = f2('ua',lev=85000)
d3 = f3('va',lev=85000)
d4 = f4('zg',lev=50000)

cdutil.setTimeBoundsMonthly(d1)
cdutil.setTimeBoundsMonthly(d2)
cdutil.setTimeBoundsMonthly(d3)
cdutil.setTimeBoundsMonthly(d4)

start_time = cdtime.comptime(start_year)
end_time = cdtime.comptime(end_year+1)

da1 = cdutil.JJA.climatology(d1(time=(start_time,end_time)))
da2 = cdutil.JJA.climatology(d2(time=(start_time,end_time)))
da3 = cdutil.JJA.climatology(d3(time=(start_time,end_time)))
da4 = cdutil.JJA.climatology(d4(time=(start_time,end_time)))

# 500 GPH global anomaly from zonal mean
da4_zonal_avg = cdutil.averager(da4,axis='x')
da4,da4_zonal_avg = genutil.grower(da4,da4_zonal_avg) # Matching dimension for subtraction
da4 = da4 - da4_zonal_avg

#=================================================
# PART 2 : GRAPHIC (plotting)
#-------------------------------------------------
# Create canvas
canvas = vcs.init(geometry=(900,800))
canvas.open()
#canvas.drawlogooff()
template = canvas.createtemplate()

# Turn off no-needed information
template.blank(["title","mean","min","max","dataname","crdate","crtime",
                "units","zvalue","tvalue","xunits","yunits","xname","yname"]) 

#-------------------------------------------------
# Plot Precip field (shaded)
#- - - - - - - - - - - - - - - - - - - - - - - - - 
iso = canvas.createisofill()
iso.datawc_x1 = lon1
iso.datawc_x2 = lon2
iso.datawc_y1 = lat1
iso.datawc_y2 = lat2
canvas.setcolormap("ltbl_to_drkbl")
iso.levels = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iso.ext_1 = "n" # control colorbar edge (arrow extention on/off)
iso.ext_2 = "y" # control colorbar edge (arrow extention on/off)
#=== below is for adjusting colormap
cols = [0]+vcs.getcolors(iso.levels)
del(cols[-1])
iso.fillareacolors = cols
#--- end adjusting
canvas.plot(da1,iso,template)

#-------------------------------------------------
# Plot 500 hPa GPH anomaly (line)
#- - - - - - - - - - - - - - - - - - - - - - - - - 
lines = vcs.createisoline()
lines.datawc_x1 = lon1
lines.datawc_x2 = lon2
lines.datawc_y1 = lat1
lines.datawc_y2 = lat2
lines.label = 'y'
lines.linewidths = [3,3,3,3,3,3]
#-- (1) Positive value -- solid line
lines.levels = range(10,60,lint)
lines.line = ['solid']
lines.linecolors = ['blue']
lines.textcolors = ['blue']
canvas.plot(da4,lines,template)
#-- (2) Negative value -- dot line
lines.levels = range(-60,-10,lint)
lines.line = ['dot','dot','dot','dot','dot','dot']
lines.linecolors = ['red']
lines.textcolors = ['red']
canvas.plot(da4,lines,template)

#-------------------------------------------------
# Plot 850 hPa wind field (vector)
#- - - - - - - - - - - - - - - - - - - - - - - - - 
vec = vcs.createvector()
ua = da2[...,::3,::3] ## Resample U field to reduce vector density
va = da3[...,::3,::3] ## Resample V filed to reduce vector density
vec.datawc_x1 = lon1
vec.datawc_x2 = lon2
vec.datawc_y1 = lat1
vec.datawc_y2 = lat2
canvas.plot(ua,va,vec,template)

#-------------------------------------------------
# Title
#- - - - - - - - - - - - - - - - - - - - - - - - - 
plot_title = vcs.createtext()
plot_title.x = .5
plot_title.y = .91
plot_title.height = 24
plot_title.halign = "center"
plot_title.valign = "top"
plot_title.color="black"
plot_title.string = 'JJA Precip., 850 UV, & 500 GPH anom: '+str(start_year)+'-'+str(end_year)
canvas.plot(plot_title)

#-------------------------------------------------
# Drop output as image file (--- vector image?)
#- - - - - - - - - - - - - - - - - - - - - - - - - 
canvas.png("Clim_JJA_precip_850uv_500gpha_"+plot_area+".png")

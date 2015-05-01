
import sys,os
import vcs
import sys
import cdms2
import vtk
import os
import MV2
bg = not False
x=vcs.init()

x.setcolormap("rainbow")
gm = vcs.createboxfill()

p = vcs.createprojection()
ptype = int('0')
p.type = ptype
gm.projection = p

xtra = {}
gm.datawc_y1=-90.0
gm.datawc_y2=0.0
xtra["latitude"] = (-90.0,0.0)

gm.datawc_x1=0.0
gm.datawc_x2=360.0
xtra["longitude"] = (0.0,360.0)


f=cdms2.open(os.path.join(vcs.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_boxfill_0_proj_SH_0_360_via_gm.png')

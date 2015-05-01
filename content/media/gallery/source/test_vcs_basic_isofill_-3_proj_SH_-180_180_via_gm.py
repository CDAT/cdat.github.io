
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
gm = vcs.createisofill()

p = vcs.createprojection()

ptype = int('-3')
p.type = ptype
gm.projection = p

xtra = {}
gm.datawc_y1=-90.0
gm.datawc_y2=0.0
xtra["latitude"] = (-90.0,0.0)

gm.datawc_x1=-180.0
gm.datawc_x2=180.0
xtra["longitude"] = (-180.0,180.0)


f=cdms2.open(os.path.join(vcs.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_isofill_-3_proj_SH_-180_180_via_gm.png')

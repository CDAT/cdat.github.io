
import sys,os
import vcs
import sys
import cdms2
import vtk
import os
import MV2
bg = not False
x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")
x.setcolormap("rainbow")
gm = vcs.createvector()

p = vcs.createprojection()

ptype = int('-3')
p.type = ptype
gm.projection = p

xtra = {}
gm.datawc_y1=0.0
gm.datawc_y2=90.0

xtra["latitude"] = (90.0,0.0)


f=cdms2.open(os.path.join(sys.prefix,'sample_data','clt.nc'))
u=f("u",**xtra)
v=f("v",**xtra)
x.plot(u,v,gm,bg=bg)



x.png('test_vcs_basic_vector_-3_proj_gmflip_NH_via_gm.png')

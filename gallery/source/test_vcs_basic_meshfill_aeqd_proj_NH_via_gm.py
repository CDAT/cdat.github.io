
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
gm = vcs.createmeshfill()

p = vcs.createprojection()
ptype = 'aeqd'
p.type = ptype
gm.projection = p

xtra = {}
gm.datawc_y1=90.0
gm.datawc_y2=0.0
xtra["latitude"] = (90.0,0.0)


f=cdms2.open(os.path.join(vcs.prefix,'sample_data','sampleCurveGrid4.nc'))
s=f("sample",**xtra)
gm.mesh=True
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_meshfill_aeqd_proj_NH_via_gm.png')

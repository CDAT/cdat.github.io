
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


xtra = {}
f=cdms2.open(os.path.join(vcs.prefix,'sample_data','sampleCurveGrid4.nc'))
s=f("sample",**xtra)
gm.mesh=True
s=MV2.masked_less(s,1150.)
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_meshfill_masked.png')

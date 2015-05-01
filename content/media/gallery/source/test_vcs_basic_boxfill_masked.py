
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


xtra = {}
f=cdms2.open(os.path.join(vcs.prefix,'sample_data','clt.nc'))
s=f("clt",**xtra)
s=MV2.masked_greater(s,78.)
x.plot(s,gm,bg=bg)



x.png('test_vcs_basic_boxfill_masked.png')

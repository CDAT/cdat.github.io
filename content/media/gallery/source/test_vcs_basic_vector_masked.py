
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
gm = vcs.createvector()


xtra = {}
f=cdms2.open(os.path.join(vcs.prefix,'sample_data','clt.nc'))
u=f("u",**xtra)
v=f("v",**xtra)
u=MV2.masked_greater(u,58.)
x.plot(u,v,gm,bg=bg)



x.png('test_vcs_basic_vector_masked.png')

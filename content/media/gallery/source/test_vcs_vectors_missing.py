import sys,os
import vcs
import cdms2
import MV2

x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")
x.setcolormap("rainbow")
gm=vcs.createvector()
gm.scale = 1.
nm_xtra=""
xtra = {}

f=cdms2.open(os.path.join(sys.prefix,"sample_data","clt.nc"))
u=f("u")
v=f("v")
u=MV2.masked_greater(u,35.)
v=MV2.masked_greater(v,888.)

x.plot(u,v,gm,bg=True)

fnm = "test_vcs_vectors_missing" 
x.png(fnm)
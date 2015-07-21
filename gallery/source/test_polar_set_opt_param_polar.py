import vcs
import cdms2
import sys
import os

f=cdms2.open(os.path.join(vcs.prefix,'sample_data','clt.nc'))
s=f("clt",slice(0,1),squeeze=1)
x=vcs.init()
i=x.createisofill()
p=x.getprojection("polar")
i.projection=p
x.open()
x.plot(s,i)
fnm= "test_polar_set_opt_param_polar.png"
x.png(fnm)

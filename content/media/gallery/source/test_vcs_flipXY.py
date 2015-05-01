import vcs, cdms2, sys, os

x=vcs.init()



f=cdms2.open(os.path.join(vcs.prefix,"sample_data","ta_ncep_87-6-88-4.nc"))

vr = "ta"
s=f(vr,slice(0,1),longitude=slice(90,91),squeeze=1,latitude=(90,-90))
x.plot(s)
fnm = "test_vcs_flipXY.png"
x.png(fnm)

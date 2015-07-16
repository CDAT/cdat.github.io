import cdms2,vcs, sys

x=vcs.init()
f=cdms2.open(vcs.prefix+"/sample_data/clt.nc")
s=f("clt",slice(0,1),squeeze=1)
b=x.createboxfill()
b.level_1=20
b.level_2=80
x.plot(s,b)

fnm = "test_boxfill_lev1_lev2.png"

x.png(fnm)

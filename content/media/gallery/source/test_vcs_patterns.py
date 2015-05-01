import vcs,cdms2,sys

f=cdms2.open(vcs.prefix+"/sample_data/clt.nc")

s=f("clt",time=slice(0,1),squeeze=1)
x=vcs.init()

iso = vcs.createisofill("isoleg")
iso.levels = [0,10,20,30,40,50,60,70,80,90,100]
iso.fillareacolors = vcs.getcolors([0,10,20,30,40,50,60,70,80,90,100])
iso.fillareastyle = "pattern"
iso.fillareindices= [4,5,6,7,8,9,10,11,12,13,14,15]
x.plot(s,iso)
fnm = "test_vcs_patterns.png"
x.png(fnm)

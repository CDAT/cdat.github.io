import sys, vcs, cdms2

cdmsfile = cdms2.open(vcs.prefix+"/sample_data/clt.nc")
data = cdmsfile('clt')
x = vcs.init()
x.plot(data)
x.close()
x.plot(data[4][1:89])
fnm = "test_vcs_close.png"
x.png(fnm)

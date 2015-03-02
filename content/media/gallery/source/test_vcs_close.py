import sys, vcs, cdms2

cdmsfile = cdms2.open(sys.prefix+"/sample_data/clt.nc")
data = cdmsfile('clt')
x = vcs.init()
x.plot(data, bg=1)
x.close()
x.plot(data[4][1:89], bg=1)
fnm = "test_vcs_close.png"
x.png(fnm)
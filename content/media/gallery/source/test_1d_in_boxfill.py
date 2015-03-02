import vcs,numpy,os,sys

x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")

d = numpy.sin(numpy.arange(100))

b = x.createboxfill()

x.plot(d,b,bg=1)


fnm = "test_1d_in_boxfill.png"
x.png(fnm)
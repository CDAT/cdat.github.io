import vcs,numpy

x=vcs.init()
x.setbgoutputdimensions(1200,1091,units="pixels")

d = numpy.sin(numpy.arange(100))
d=numpy.reshape(d,(10,10))


one = x.create1d()

x.plot(d,one,bg=1)


fnm = "test_1D_with_manyDs.png"
x.png(fnm)

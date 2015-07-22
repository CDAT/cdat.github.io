import vcs,numpy

x=vcs.init()


d = numpy.sin(numpy.arange(100))
d=numpy.reshape(d,(10,10))


one = x.create1d()

x.plot(d,one)


fnm = "test_1D_with_manyDs.png"
x.png(fnm)

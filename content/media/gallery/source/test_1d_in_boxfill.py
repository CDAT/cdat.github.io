import vcs,numpy,os,sys

x=vcs.init()


d = numpy.sin(numpy.arange(100))

b = x.createboxfill()

x.plot(d,b)


fnm = "test_1d_in_boxfill.png"
x.png(fnm)

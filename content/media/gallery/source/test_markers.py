import vcs

x=vcs.init()


m = x.createmarker()
m.x=[[0.,],[5,],[10.,],[15.]]
m.y=[[0.,],[5,],[10.,],[15.]]
m.worldcoordinate=[-5,20,-5,20]

m.type=['plus','diamond','square_fill',"hurricane"]
m.color=[242,243,244,242]
m.size=[20,20,20,5]
x.plot(m)
fnm= "test_markers.png"

x.png(fnm)

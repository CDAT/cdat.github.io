import vcs

x=vcs.init()

txt=x.createtext()
txt.x = [.0000005,.00000005,.5,.99999,.999999]
txt.y=[0.05,.9,.5,.9,0.05]
txt.string = ["SAMPLE TEXT A","SAMPLE TEXT B","SAMPLE TEXT C","SAMPLE TEXT D","SAMPLE TEXT E"]
txt.halign = "center"
txt.valign="base"
txt.angle=45
x.plot(txt)
fnm = "test_basic_text.png"
x.png(fnm)

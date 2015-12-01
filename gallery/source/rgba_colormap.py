import vcs, cdms2, os

colormap = vcs.createcolormap("transparent")
for i in range(5, 240):
    percent = int(100 * (i - 5) / 234.)
    colormap.index[i][3] = percent

canvas = vcs.init()
canvas.setcolormap(colormap)

cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")
canvas.plot(clt)
canvas.png("rgba_colormap")
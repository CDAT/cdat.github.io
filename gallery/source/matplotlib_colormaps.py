import vcs, cdms2, os

vcs.download_sample_data_files()

cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")

canvas = vcs.init()

colormap = vcs.matplotlib2vcs("jet")
canvas.setcolormap(colormap)
canvas.plot(clt)
canvas.png("matplotlib_colormaps")

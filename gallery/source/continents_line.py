import vcs, cdms2, os

vcs.download_sample_data_files()

cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")

canvas = vcs.init()

thick_line = canvas.createline()
thick_line.width = 2
thick_line.color = [(0, 0, 0, 50)]

canvas.plot(clt, continents_line=thick_line)
canvas.png("continents_line")

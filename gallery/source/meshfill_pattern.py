import vcs, cdms2, os

vcs.download_sample_data_files()

# An example demonstrating patterns with meshfill
cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")

canvas = vcs.init()
mesh = canvas.createmeshfill()
mesh.mesh = True
mesh.fillareastyle = "hatch"
# Refer to http://uvcdat.llnl.gov/examples/pattern_chart.html for a list of patterns
mesh.fillareaindices = [1, 2, 3, 4, 5]
mesh.fillareaopacity = [50.0, 85.1, 23.5, 99.9, 100]
mesh.levels = [0, 20, 40, 60, 80, 100]
mesh.fillareacolors = vcs.getcolors(mesh.levels)

canvas.plot(clt, mesh)
canvas.png("meshfill_pattern")

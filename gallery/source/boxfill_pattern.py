import vcs, cdms2, os

vcs.download_sample_data_files()

# An example demonstrating patterns with meshfill
cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")

canvas = vcs.init()
box = canvas.createboxfill()

box.boxfill_type = "custom"
box.fillareastyle = "hatch"
# Refer to http://uvcdat.llnl.gov/examples/pattern_chart.html for a list of patterns
box.fillareaindices = [1, 2, 3, 4, 5]
box.fillareaopacity = [50.0, 85.1, 23.5, 99.9, 100]
box.levels = [0, 20, 40, 60, 80, 100]
box.fillareacolors = vcs.getcolors(box.levels)

canvas.plot(clt, box)
canvas.png("boxfill_pattern")
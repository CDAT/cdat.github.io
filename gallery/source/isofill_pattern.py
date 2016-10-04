import vcs, cdms2, os

vcs.download_sample_data_files()

# An example demonstrating patterns with meshfill
cltfile = cdms2.open(os.path.join(vcs.sample_data, "clt.nc"))
clt = cltfile("clt")

canvas = vcs.init()
iso = canvas.createisofill()

iso.fillareastyle = "hatch"
# Refer to http://uvcdat.llnl.gov/examples/pattern_chart.html for a list of patterns
iso.fillareaindices = [1, 2, 3, 4, 5]
iso.levels = [0, 20, 40, 60, 80, 100]
iso.fillareaopacity = [50.0, 85.1, 23.5, 99.9, 100]
iso.fillareacolors = vcs.getcolors(iso.levels)

canvas.plot(clt, iso)
canvas.png("isofill_pattern")
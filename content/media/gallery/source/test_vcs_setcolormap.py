import cdms2
import os
import sys
import vcs

cdmsfile = cdms2.open(os.path.join(vcs.prefix,"sample_data","clt.nc"))
data = cdmsfile('clt')

x=vcs.init()


t=x.gettemplate('default')
x.plot(data, t, bg=True)

# This should force the image to update
x.setcolormap('bl_to_drkorang')

testFilename = "test_vcs_setcolormap.png"
x.png(testFilename)

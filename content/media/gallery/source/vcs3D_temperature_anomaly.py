'''
Created on Jun 18, 2014

@author: tpmaxwel
'''

import vcs, cdms2, cdutil, genutil, sys

x = vcs.init()
f = cdms2.open( vcs.prefix+"/sample_data/geos5-sample.nc" )  
dv3d = vcs.get3d_scalar()    
dv3d.ToggleVolumePlot = vcs.on
dv3d.ScaleColormap = [-15.0, 15.0, 1] 
dv3d.ScaleTransferFunction =  [ 3.64, 24, 1]
dv3d.VerticalScaling = 6.0 
dv3d.Camera={'Position': (-161, -171, 279), 'ViewUp': (.29, 0.67, 0.68), 'FocalPoint': (146.7, 8.5, -28.6)}
dv3d_v = vcs.get3d_scalar()   
v0 = f["tmpu"] 
va = cdutil.averager( v0, axis='x' )
v01,va1=genutil.grower(v0,va)
v = v01 - va1
x.plot( v, dv3d )
x.interact()

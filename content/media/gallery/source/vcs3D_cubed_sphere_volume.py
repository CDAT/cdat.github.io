import vcs, cdms2, sys

x = vcs.init()
f = cdms2.open( "vcs3D_cubed_sphere_volume.nc" )   
v = f["RELHUM"] 
dv3d = vcs.get3d_scalar()
dv3d.ScaleTransferFunction = [ 78.7, 132.0 ]
dv3d.ScaleColormap = [ 75.4, 100.0 ]
dv3d.ScaleOpacity = [0.27, 1.0]
dv3d.PointSize = [5, 2]
dv3d.VerticalScaling = [ 1.7 ]
dv3d.ToggleVolumePlot = vcs.on
dv3d.ToggleSphericalProj = vcs.on
dv3d.Camera = {'Position': (-108.11442471080369, -476.65927617219285, 84.45227482307195), 'ViewUp': ( 0.0, 0.0, 1.0), 'FocalPoint': (0, 0, 0)}
x.plot( v, dv3d, grid_file="vcs3D_cubed_sphere_volume_grid.nc" )
x.interact()

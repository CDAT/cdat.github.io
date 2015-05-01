import vcs, cdms2, sys
x = vcs.init()
f = cdms2.open( vcs.prefix+"/sample_data/geos5-sample.nc" ) 
v = f["uwnd"]
dv3d = vcs.get3d_scalar()    
dv3d.ToggleClipping = ( 40, 360, -28, 90 )
dv3d.YSlider = ( 0.0, vcs.off)
dv3d.XSlider = ( 180.0, vcs.on ) 
dv3d.ZSlider = ( 0.0, vcs.on )
dv3d.ToggleVolumePlot = vcs.on
dv3d.ToggleSurfacePlot = vcs.on 
dv3d.IsosurfaceValue = 31.0
dv3d.ScaleOpacity = [0.0, 1.0]
dv3d.BasemapOpacity = 0.5
dv3d.Camera={ 'Position': (-161, -171, 279), 
              'ViewUp': (.29, 0.67, 0.68), 
              'FocalPoint': (146.7, 8.5, -28.6)  }
dv3d.VerticalScaling = 5.0 
dv3d.ScaleColormap = [ -46.0, 48.0 ] 
dv3d.ScaleTransferFunction =  [ 12.0, 77.0 ]

x.plot( v, dv3d )
x.interact()

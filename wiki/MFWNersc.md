##Embarrassingly Parallel Examples Run In Serial From Michael Wehner

All files are globally readable at NERSC

###Example 1: Annual Mean from Monthly Data

    cd /project/projectdirs/m1517/ACE/cam5.1/control/0.25_degree/monthly
    python
    /global/homes/m/mwehner/pyfiles/make_annual_average_from_monthly.py
    TREFHT_cam5_1_amip_run2.cam2.h0.1979-2005.xml TREFHT
    
This takes about 6 minutes on hppper
    
    python
    /global/homes/m/mwehner/pyfiles/make_annual_average_from_monthly.py
    T_cam5_1_amip_run2.cam2.h0.1979-2005.xml T

This takes about 45 minutes on hopper because it lev/lat/lon

code:

    import cdms2,cdutil,sys
    cdms2.setNetcdfShuffleFlag(0)
    cdms2.setNetcdfDeflateFlag(0)
    cdms2.setNetcdfDeflateLevelFlag(0)
    f=sys.argv[1]
    v=sys.argv[2]
    file=cdms2.open(f)
    var=file.getslab(v)
    cdutil.times.setTimeBoundsMonthly(var)
    v=cdutil.YEAR.get(var)
    outfile=cdms.open('annual_'+sys.argv[2]+'_'+f+'.nc','w')
    outfile.write(v)
    for a in file.listglobal():
    setattr(outfile,a,getattr(file,a))
    outfile.close()

Example 2: Spatial Average (lat/lon)

This is a case that is embarrassingly parallel in time.

    cd /project/projectdirs/m1517/ACE/cam5.1/control/0.25_degree/monthly
    python /global/homes/m/mwehner/pyfiles/make_global_avg.py TREFHT_cam5_1_amip_run2.cam2.h0.1979-2005.xml TREFHT

This example takes about 1.5 minutes.

    python /global/homes/m/mwehner/pyfiles/make_global_avg.py T_cam5_1_amip_run2.cam2.h0.1979-2005.xml T

This example takes about 30 times longer because it is lev/lat/lon  

code:

    import cdms2, sys, MV2, cdutil
    cdms2.setNetcdfShuffleFlag(0)
    cdms2.setNetcdfDeflateFlag(0)
    cdms2.setNetcdfDeflateLevelFlag(0)
    var=sys.argv[2]
    # open up the source variables
    f=cdms2.open(sys.argv[1])
    x=f(var)
    xglobal_avg=cdutil.averager(x, axis='xy', weights='weighted')
    xglobal_avg.id=var+'_global_avg'
    fo=cdms.open(sys.argv[1]+'global_avg.nc','w')
    fo.write(xglobal_avg)
    fo.close()

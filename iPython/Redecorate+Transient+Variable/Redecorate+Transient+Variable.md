---
layout: default
title: Redecorate+Transient+Variable Tutorial
---

# Redecorate+Transient+Variable Tutorial
[download iPython Notebook](Redecorate+Transient+Variable.ipynb)

This Jupyter Notebook shows how to *redecorate* a transient variable that became a numpy array


```python
# import modules
import MV2
import cdms2
import numpy
import cdat_info  # for sample data
```


```python
# open some data
f=cdms2.open(cdat_info.get_sampledata_path()+"/clt.nc")
s=f("clt")
print type(s)
```

    <class 'cdms2.tvariable.TransientVariable'>



```python
# Now run an operation on this MV2 that turns it to munpy array
fft_s = numpy.fft.fft(s)
print type(fft_s)  # numpy array
```

    <type 'numpy.ndarray'>



```python
# now put back dimensions on it
fft_s = MV2.array(fft_s)
fft_s.setAxisList(s.getAxisList())

# Dimensions are back
print fft_s.getAxisIds()
```

    ['time', 'latitude', 'longitude']



```python
# now puts the attributes on it
for a in s.attributes:
    setattr(fft_s,a,getattr(s,a))
fft_s.info()
```

    *** Description of Slab variable_14 ***
    id: variable_14
    shape: (120, 46, 72)
    filename: 
    missing_value: (1+0j)
    comments: YONU_AMIP1
    grid_name: YONU4X5
    grid_type: gaussian
    time_statistic: average
    long_name: Total cloudiness
    units: %
    tileIndex: None
    Grid has Python id 0x7f58311cba50.
    Gridtype: generic
    Grid shape: (46, 72)
    Order: yx
    ** Dimension 1 **
       id: time
       Designated a time axis.
       units:  months since 1979-1-1 0
       Length: 120
       First:  0.0
       Last:   119.0
       Other axis attributes:
          calendar: gregorian
          axis: T
          realtopology: linear
       Python id:  0x7f58311cbf10
    ** Dimension 2 **
       id: latitude
       Designated a latitude axis.
       units:  degrees_north
       Length: 46
       First:  -90.0
       Last:   90.0
       Other axis attributes:
          long_name: Latitude
          axis: Y
          realtopology: linear
       Python id:  0x7f58311cb610
    ** Dimension 3 **
       id: longitude
       Designated a longitude axis.
       units:  degrees_east
       Length: 72
       First:  -180.0
       Last:   175.0
       Other axis attributes:
          modulo: 360.0
          realtopology: circular
          long_name: Longitude
          topology: circular
          axis: X
       Python id:  0x7f58311cbf90
    *** End of description for variable_14 ***


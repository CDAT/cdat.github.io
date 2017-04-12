---
layout: default
title: streamlines Tutorial
---

# streamlines Tutorial
[download iPython Notebook](streamlines.ipynb)


```python
import warnings
warnings.filterwarnings('ignore')
import vcs
import cdms2
```


```python
# Download the sample data if needed
# vcs.download_sample_data_files()
# read clt.nc
f=cdms2.open(vcs.sample_data+"/clt.nc")
```


```python
# read two variables
u = f("u")
v = f("v")
```


```python
# initialize vcs
x=vcs.init()
```


```python
# create the streamline graphics method
gm = x.createstreamline()
# streamlines are colored by vector magnitude
gm.coloredbyvector = True
# We want 10 glyphs(arrows) per streamline
gm.numberofglyphs = 10
# We place 400 random seeds in a circle that covers the data. This means fewer seeds will be inside the data.
# The number of seeds inside the data will result in streamlines.
gm.numberofseeds = 400
gm.filledglyph = True
```


```python
# use the robinson projection for the data.
p = x.createprojection()
p.type = 'robinson'
gm.projection = p
```


```python
# create the stremline plot
x.plot(u, v, gm, bg=1)
```




![png](streamlines_files/streamlines_6_0.png)




```python
#create a red colormap with low values mapped to low opacity
cmap = x.createcolormap()
for i in range(256):
    cmap.setcolorcell(i,100.,0,0,i/2.55)
x.setcolormap(cmap)
#replot
x.plot(u, v, gm, bg=1)
```




![png](streamlines_files/streamlines_7_0.png)




```python

```

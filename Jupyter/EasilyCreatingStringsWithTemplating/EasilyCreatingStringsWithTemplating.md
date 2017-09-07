---
layout: default
title: EasilyCreatingStringsWithTemplating Tutorial
---

# EasilyCreatingStringsWithTemplating Tutorial
[download iPython Notebook](EasilyCreatingStringsWithTemplating.ipynb)


```python
import genutil
# Define your string template
file_template = "%(path)/%(variable).%(model).nc"
# Create a StringConstructor object
S = genutil.StringConstructor(file_template)
# Fill the StringConstructor with the values for each key
S.path = "blah"
S.variable = "tas"
S.model= "CNRM"
my_path = S()
print "My file path is:",my_path
```

    My file path is: blah/tas.CNRM.nc



```python
# You can also pass keys at retrieval time
print "My file path for variable 'pr' is:",S(variable="pr")
```

    My file path for variable 'pr' is: blah/pr.CNRM.nc



```python
# You can easily loop through keys like this:
for model in ["modelA","modelB","modelC"]:
    for variable in ["tas","pr","zg","u","v"]:
        S.model = model
        path = S(variable=variable)
        print "PATH IS:",path
```

    PATH IS: blah/tas.modelA.nc
    PATH IS: blah/pr.modelA.nc
    PATH IS: blah/zg.modelA.nc
    PATH IS: blah/u.modelA.nc
    PATH IS: blah/v.modelA.nc
    PATH IS: blah/tas.modelB.nc
    PATH IS: blah/pr.modelB.nc
    PATH IS: blah/zg.modelB.nc
    PATH IS: blah/u.modelB.nc
    PATH IS: blah/v.modelB.nc
    PATH IS: blah/tas.modelC.nc
    PATH IS: blah/pr.modelC.nc
    PATH IS: blah/zg.modelC.nc
    PATH IS: blah/u.modelC.nc
    PATH IS: blah/v.modelC.nc



```python
# in some case you can even reverse ingeneer
print "key/values pairs:",S.reverse(path)
```

    key/values pairs: {'variable': 'v', 'path': 'blah', 'model': 'modelC'}



```python

```

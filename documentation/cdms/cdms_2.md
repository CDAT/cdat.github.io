---
title: CDMS Chapter 2
layout: docs
manual: cdms
index: 2
---






### CHAPTER 2 CDMS Python Application Programming Interface

<a name="2.1"></a>

#### 2.1 Overview

This chapter describes the CDMS Python application programming interface (API). Python is a popular public-domain, object-oriented language. Its features include support for object-oriented development, a rich set of programming constructs, and an extensible architecture. CDMS itself is implemented in a mixture of C and Python. In this chapter the assumption is made that the reader is familiar with the basic features of the Python language.

Python supports the notion of a module, which groups together associated classes and methods. The import command makes the module accessible to an application. This chapter documents the cdms, cdtime, and regrid modules.

The chapter sections correspond to the CDMS classes. Each section contains tables base. If no parent, the datapath is absolute.describing the class internal (non-persistent) attributes, constructors (functions for creating an object), and class methods (functions). A method can return an instance of a CDMS class, or one of the Python types:


<a name="table_2.1"></a>

###### Table 2.1 Python types used in CDMS


 Type  | Description 
 ----  | -----------
 Array | Numeric or masked multidimensional data array. All elements of the array are of the same type. Defined in the Numeric and MA modules. 
 Comptime | Absolute time value, a time with representation (year, month, day, hour, minute, second). Defined in the cdtime module. cf. reltime 
 Dictionary | An unordered 2,3collection of objects, indexed by key. All dictionaries in CDMS are indexed by strings, e.g.: `axes['time']` 
 Float | Floating-point value. 
 Integer | Integer value. 
 List    | An ordered sequence of objects, which need not be of the same type. New members can be inserted or appended. Lists are denoted with square brackets, e.g., `[1, 2.0, 'x', 'y']` 
 None | No value returned. 
 Reltime | Relative time value, a time with representation (value, units since basetime). Defined in the cdtime module. cf. comptime 
 Tuple | An ordered sequence of objects, which need not be of the same type. Unlike lists, tuples elements cannot be inserted or appended. Tuples are denoted with parentheses, e.g., `(1, 2.0, 'x', 'y')` 

<a name="2.2"></a>

#### 2.2 A first example

The following Python script reads January and July monthly temperature data from an input dataset, averages over time, and writes the results to an output file. The input temperature data is ordered (time, latitude, longitude).

{% highlight python %}
1   #!/usr/bin/env python
2   import cdms
3   from cdms import MV
4   jones = cdms.open('/pcmdi/cdms/obs/jones_mo.nc')
5   tasvar = jones['tas']
6   jans = tasvar[0::12]
7   julys = tasvar[6::12]
8   janavg = MV.average(jans)
9   janavg.id = "tas_jan"
10  janavg.long_name = "mean January surface temperature"
11  julyavg = MV.average(julys)
12  julyavg.id = "tas_jul"
13  julyavg.long_name = "mean July surface temperature"
14  out = cdms.open('janjuly.nc','w')
15  out.write(janavg)
16  out.write(julyavg)
17  out.comment = "Average January/July from Jones dataset"
18  jones.close()
19  out.close()
{% endhighlight %}



| Line | Notes |
| ---- | ----- |
| 2,3  |  Makes the CDMS and MV modules available. MV defines arithmetic functions. |
|  4 |  Opens a netCDF file read-only. The result jones is a dataset object. |
| 5 |  Gets the surface air temperature variable. 'tas' is the name of the    variable in the input dataset. This does not actually read the data. |
| 6 |  Read all January monthly mean data into a variable jans. Variables can be sliced like arrays. The slice operator [0::12] means take every 12th slice from dimension 0, starting at index 0 and ending at the last index. If the stride 12 were omitted, it would default to 1. Note that the variable is actually 3-dimensional. Since no slice is specified for the second or third dimensions, all values of those 2,3 dimensions are retrieved. The slice operation could also have been written [0::12, : , :]. Also note that the same script works for multi-file datasets. CDMS opens the needed data files, extracts the appropriate slices, and concatenates them into the result array. |
| 7 |  Reads all July data into a masked array julys. |
| 8 |  Calculate the average January value for each grid zone. Any missing data is handled automatically. |
| 9,10  |  Set the variable id and long_name attributes. The id is used as the name of the variable when plotted or written to a file. |
| 14 |  Create a new netCDF output file named 'janjuly.nc' to hold the results. |
| 15 |  Write the January average values to the output file. The variable will have id "tas_jan" in the file. `write` is a utility function which creates the variable in the file, then writes data to the variable. A more general method of data output is first to create a variable, then set a slice of the variable. Note that janavg and julavg have the same latitude and longitude information as tasvar. It is carried along with the computations. |
| 17 |  Set the global attribute 'comment'. |
| 18 |  Close the output file. |

<a name="2.3"></a>

#### 2.3 cdms module

The cdms module is the Python interface to CDMS. The objects and methods in this chapter are made accessible with the command:

{% highlight python %}
import cdms
{% endhighlight %}

The functions described in this section are not associated with a class. Rather, they are called as module functions, e.g.,

{% highlight python %}
file = cdms.open('sample.nc')
{% endhighlight %}


<a name="table_2.2"></a>

###### Table 2.2 cdms module functions

<table class="table">
  <tr>

    <th>Type</th>

    <th>Definition</th>
  </tr>
<tr>
<td><code>Variable</code> </td><td> <code>asVariable(s)</code>: Transform <code>s</code> into a transient variable. <code>s</code> is a masked array, Numeric array, or Variable. If <code>s</code> is already a transient variable, <code>s</code> is returned. See also: <code>isVariable</code>.</td>
</tr>
<tr>
<td><code>Axis</code> </td><td> <code>createAxis(data, bounds=None)</code>: Create a one-dimensional coordinate Axis, which is not associated with a file or dataset. This is useful for creating a grid which is not contained in a file or dataset. <code>data</code> is a one-dimensional, monotonic Numeric array. <code>bounds</code> is an array of shape <code>(len(data),2)</code>, such that for all <code>i</code>, <code>data[i]</code> is in the range <code>[bounds[i,0],bounds[i,1] ]</code>. If <code>bounds</code> is not specified, the default boundaries are generated at the midpoints between the consecutive data values, provided that the autobounds mode is 'on' (the default). See <code>setAutoBounds</code>. Also see: <code>CdmsFile.createAxis</code></td>
</tr>
<tr>
<td><code>Axis</code> </td><td> <code>createEqualAreaAxis(nlat)</code>: Create an equal-area latitude axis. The latitude values range from north to south, and for all axis values <code>x[i]</code>, <code>sin(x[i])sin(x[i+1])</code> is constant. <code>nlat</code> is the axis length. The axis is not associated with a file or dataset.</td>
</tr>
<tr>
<td><code>Axis</code> </td><td> <code>createGaussianAxis(nlat)</code>: Create a Gaussian latitude axis. Axis values range from north to south. <code>nlat</code> is the axis length. The axis is not associated with a file or dataset.</td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createGaussianGrid(nlats, xorigin=0.0, order="yx")</code>: Create a Gaussian grid, with shape <code>(nlats, 2*nlats)</code>. <code>nlats</code> is the number of latitudes. <code>xorigin</code> is the origin of the longitude axis. <code>order</code> is either "yx" (lat-lon, default) or "xy" (lon-lat) </td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createGenericGrid(latArray, lonArray,  latBounds=None, lonBounds=None, order="yx", mask=None)</code>: Create a generic grid, that is, a grid which is not typed as Gaussian, uniform, or equal-area. The grid is not associated with a file or dataset. <code>latArray</code> is a NumPy array of latitude values. <code>lonArray</code> is a NumPy array of longitude values. <code>latBounds</code> is a NumPy array having shape <code>(len(latArray),2)</code>, of latitude boundaries. <code>lonBounds</code> is a NumPy array having shape <code>(len(lonArray),2)</code>, of longitude boundaries. <code>order</code> is a <code>string</code> specifying the order of the axes, either "yx" for (latitude, longitude), or "xy" for the reverse. <code>mask</code> (optional) is an <code>integer</code>-valued NumPy mask array, having the same shape and ordering as the grid.</td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createGlobalMeanGrid(grid)</code>: Generate a grid for calculating the global mean via a regridding operation. The return grid is a single zone covering the range of the input grid. <code>grid</code> is a RectGrid.</td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createRectGrid(lat, lon, order, type="generic", mask=None)</code>: Create a rectilinear grid, not associated with a file or dataset. This might be used as the target grid for a regridding operation. <code>lat</code> is a latitude axis, created by <code>cdms.createAxis</code>. <code>lon</code> is a longitude axis, created by <code>cdms.createAxis</code>. <code>order</code> is a string with value "yx" (the first grid dimension is latitude) or "xy" (the first grid dimension is longitude). <code>type</code> is one of 'gaussian','uniform','equalarea',or 'generic'. If specified, <code>mask</code> is a two-dimensional, logical Numeric array (all values are zero or one) with the same shape as the grid.</td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createUniformGrid(startLat, nlat, deltaLat, start-Lon, nlon, deltaLon, order="yx", mask=None)</code>: Create a uniform rectilinear grid. The grid is not associated with a file or dataset. The grid boundaries are at the midpoints of the axis values. <code>startLat</code> is the starting latitude value. <code>nlat</code> is the number of latitudes. If <code>nlat</code> is 1, the grid latitude boundaries will be <code>startLat</code> +/- <code>deltaLat/2</code>. <code>deltaLat</code> is the increment between latitudes. <code>startLon</code> is the starting longitude value. <code>nlon</code> is the number of longitudes. If <code>nlon</code> is 1, the grid longitude boundaries will be <code>startLon</code> +/- <code>deltaLon/2</code>. <code>deltaLon</code> is the increment between longitudes. <code>order</code> is a string with value "yx" (the first grid dimension is latitude) or "xy" (the first grid dimension is longitude). If specified, <code>mask</code> is a two-dimensional, logical Numeric array (all values are zero or one) with the same shape as the grid.</td>
</tr>
<tr>
<td><code>Axis</code> </td><td> <code>createUniformLatitudeAxis(startLat, nlat, deltaLat)</code>: Create a uniform latitude axis. The axis boundaries are at the midpoints of the axis values. The axis is designated as a circular latitude axis. <code>startLat</code> is the starting latitude value. <code>nlat</code> is the number of latitudes. <code>deltaLat</code> is the increment between latitudes.</td>
</tr>
<tr>
<td><code>RectGrid</code> </td><td> <code>createZonalGrid(grid)</code>: Create a zonal grid. The output grid has the same latitude as the input grid, and a single longitude. This may be used to calculate zonal averages via a regridding operation. <code>grid</code> is a RectGrid.</td>
</tr>
<tr>
<td><code>Axis</code> </td><td> <code>createUniformLongitudeAxis(startLon, nlon, delta-Lon)</code>: Create a uniform longitude axis. The axis boundaries are at the midpoints of the axis values. The axis is designated as a circular longitude axis. <code>startLon</code> is the starting longitude value. <code>nlon</code> is the number of longitudes. <code>deltaLon</code> is the increment between longitudes.</td>
</tr>
<tr>
<td><code>Variable</code> </td><td> <code>createVariable(array, typecode=None, copy=0, savespace=0, mask=None, fill_value=None, grid=None, axes=None, attributes=None, id=None)</code>: This function is documented in Table 2.34 on page 90.</td>
</tr>
<tr>
<td><code>Integer</code> </td><td> <code>getAutoBounds()</code>: Get the current autobounds mode. Returns 0, 1, or 2. See <code>setAutoBounds</code>.</td>
</tr>
<tr>
<td><code>Integer</code> </td><td> <code>isVariable(s)</code>: Return <code>1</code> if <code>s</code> is a variable, <code>0</code> otherwise. See also: <code>asVariable</code>.</td>
</tr>
<tr>
<td><code>Dataset</code> or <code>CdmsFile</code> </td><td> <code>open(url,mode='r')</code>: Open or create a <code>Dataset</code> or <code>CdmsFile</code>. <code>url</code> is a Uniform Resource Locator, referring to a cdunif or XML file. If the URL has the extension '.xml' or '.cdml', a <code>Dataset</code> is returned, otherwise a <code>CdmsFile</code> is returned. If the URL protocol is 'http', the file must be a '.xml' or '.cdml' file, and the mode must be 'r'. If the protocol is 'file' or is omitted, a local file or dataset is opened. <code>mode</code> is the open mode. See Table 2.24 on page 70.
<p>
<b>Example</b>: Open an existing dataset:

<code>f = cdms.open("sampleset.xml")</code>
</p>
<p>
<b>Example</b>: Create a netCDF file:

<code>f = cdms.open("newfile.nc",'w')</code>
</p>
</td>
</tr>
<tr>
<td><code>List</code> </td><td> <code>order2index (axes, orderstring)</code>: Find the index permutation of axes to match order. Return a list of indices. <code>axes</code> is a list of axis objects. <code>orderstring</code> is defined as in <code>orderparse</code>.</td>
</tr>
<tr>
<td><code>List</code></td><td><code>orderparse(orderstring)</code>: Parse an order string. Returns a list of axes specifiers. <code>orderstring</code> consists of:
  <ul>

    <li> Letters t, x, y, z meaning time, longitude, latitude, level</li>

    <li> Numbers 0-9 representing position in axes</li>

    <li> Dash (-) meaning insert the next available axis here.</li>

    <li> The ellipsis ... meaning fill these positions with any remaining axes.</li>

    <li> (name) meaning an axis whose id is name</li>
  </ul>
</td>
</tr>
<tr>
  <td><code>None</code></td><td><code>setAutoBounds(mode)</code>: Set autobounds mode. In some circumstances CDMS can generate boundaries for 1-D axes and rectilinear grids, when the bounds are not explicitly defined. The autobounds mode determines how this is done: If <code>mode</code> is <code>'grid'</code> or <code>2</code> (the default), the <code>getBounds</code> method will automatically generate boundary information for an axis or grid if the axis is designated as a latitude or longitude axis, and the boundaries are not explicitly defined. If <code>mode</code> is <code>'on'</code> or <code>1</code>, the <code>getBounds</code> method will automatically generate boundary information for an axis or grid, if the boundaries are not explicitly defined. If <code>mode</code> is <code>'off'</code> or <code>0</code>, and no boundary data is explicitly defined, the bounds will NOT be generated; the <code>getBounds</code> method will return <code>None</code> for the boundaries. Note: In versions of CDMS prior to V4.0, the default <code>mode</code> was <code>'on'</code>.</td>
</tr>
<tr>
  <td><code>None</code></td><td><code>setClassifyGrids(mode)</code>: Set the grid classification mode. This affects how grid type is determined, for the purpose of generating grid boundaries. If <code>mode</code> is <code>'on'</code> (the default), grid type is determined by a grid classification method, regardless of the value of <code>grid.get-Type()</code>. If <code>mode</code> is <code>'off'</code>, the value of <code>grid.getType()</code> determines the grid type</td>
</tr>
<tr>
  <td><code>None</code></td><td><code>writeScripGrid(path, grid, gridTitle=None)</code>: Write a grid to a SCRIP grid file. <code>path</code> is a string, the path of the SCRIP file to be created. <code>grid</code> is a CDMS grid object. It may be rectangular. <code>gridTitle</code> is a string ID for the grid.</td>
</tr>
</table>


<a name="table_2.3"></a>

###### Table 2.3 Class Tags 


Tag | Class
--- | ---
'axis' | Axis
'database' | Database
'dataset' | Dataset, CdmsFile
'grid' | RectGrid
'variable' | Variable
'xlink' | Xlink


<a name="2.4"></a>

#### 2.4 CdmsObj

A CdmsObj is the base class for all CDMS database objects. At the application level, CdmsObj objects are never created and used directly. Rather the subclasses of CdmsObj (Dataset, Variable, Axis, etc.) are the basis of user application programming.

All objects derived from CdmsObj have a special attribute .attributes. This is a Python dictionary, which contains all the external (persistent) attributes associated with the object. This is in contrast to the internal, non-persistent attributes of an object, which are built-in and predefined. When a CDMS object is written to a file, the external attributes are written, but not the internal attributes.

**Example**: get a list of all external attributes of obj.

{% highlight python %}
extatts = obj.attributes.keys()
{% endhighlight %}


<a name="table_2.4"></a>

###### Table 2.4 Attributes common to all CDMS objects


Type | Name | Definition
---- | ---- | ----------
Dictionary | attributes | External attribute dictionary for this object.



<a name="table_2.5"></a>

###### Table 2.5 Getting and setting attributes

<table class="table">
  <tr>

    <th>Type</th>

    <th>Definition</th>
  </tr>
  <tr>
<td>various</td><td><code>value = obj.attname</code><p>Get an internal or external attribute value. If the attribute is external, it is read from the database. If the attribute is not already in the database, it is created as an external attribute. Internal attributes cannot be created, only referenced.</p>
</td>
</tr>
<tr>
<td>various</td><td><code>obj.attname = value</code><p>Set an internal or external attribute value. If the attribute is external, it is written to the database.</p></td>
</tr>
</table>

<a name="2.5"></a>

#### 2.5 CoordinateAxis

A CoordinateAxis is a variable that represents coordinate information. It may be contained in a file or dataset, or may be transient (memoryresident). Setting a slice of a file CoordinateAxis writes to the file, and referencing a file CoordinateAxis slice reads data from the file. Axis objects are also used to define the domain of a Variable.

CDMS defines several different types of CoordinateAxis objects. Table 2.9 on page 45 documents methods that are common to all CoordinateAxis types. Table 2.10 on page 48 specifies methods that are unique to 1D Axis objects.


<a name="table_2.6"></a>

###### Table 2.6 CoordinateAxis types


Type | Definition
-------| ----------
`CoordinateAxis` | A variable that represents coordinate information. Has subtypes `Axis2D` and `AuxAxis1D`.
`Axis` | A one-dimensional coordinate axis whose values are strictly monotonic. Has subtypes `DatasetAxis`, `FileAxis`, and `TransientAxis`. May be an index axis, mapping a range of integers to the equivalent floating point value. If a latitude or longitude axis, may be associated with a `RectGrid`.
`Axis2D` | A two-dimensional coordinate axis, typically a latitude or longitude axis related to a `CurvilinearGrid`. Has subtypes `DatasetAxis2D`, `FileAxis2D`, and `TransientAxis2D`.
`AuxAxis1D` | A one-dimensional coordinate axis whose values need not be monotonic. Typically a latitude or longitude axis associated with a `GenericGrid`. Has subtypes `DatasetAuxAxis1D`, `FileAuxAxis1D`, and `TransientAuxAxis1D`. An axis in a `CdmsFile` may be designated the unlimited axis, meaning that it can be extended in length after the initial definition. There can be at most one unlimited axis associated with a `CdmsFile`.


<a name="table_2.7"></a>

###### Table 2.7 CoordinateAxis Internal Attributes


Type | Name | Definition
-----|----- | ----------
`Dictionary` | `attributes` | External attribute dictionary.
`String` | `id` | CoordinateAxis identifer.
`Dataset` | `parent` | The dataset which contains the variable.
`Tuple` | `shape` | The length of each axis.



<a name="table_2.8"></a>

###### Table 2.8 Axis Constructors


| Constructor | Description
|------------|------------ 
| `cdms.createAxis(data, bounds=None)` | Create an axis which is not associated with a dataset or file. See Table 2.2 on page 33.
|-----------|------------
| `Dataset.createAxis(name,ar)` | Create an `Axis` in a `Dataset`. (This function is not yet implemented. )
|-----------|------------
|`CdmsFile.createAxis(name,ar,unlimited=0)` | Create an Axis in a `CdmsFile`. `name` is the string `name` of the `Axis`. `ar` is a 1-D data array which defines the `Axis` values. It may have the value `None` if an unlimited axis is being defined. At most one `Axis` in a `CdmsFile` may be designated as being unlimited, meaning that it may be extended in length. To define an axis as unlimited, either:
| | A) set `ar` to `None`, and leave `unlimited` undefined, or
| | B) set `ar` to the initial 1-D array, and set `unlimited` to `cdms.Unlimited`
|-----------|------------
| `cdms.createEqualAreaAxis(nlat)` | See Table 2.2 on page 33.
|-----------|------------
| `cdms.createGaussianAxis(nlat)` | See Table 2.2 on page 18.
|-----------|------------
| `cdms.createUniformLatitudeAxis(startlat, nlat, deltalat)` | See Table 2.2 on page 18.
|-----------|------------
| `cdms.createUniformLongitudeAxis(startlon, nlon, deltalon)` | See Table 2.2 on page 18.
|-----------|------------  


<a name="table_2.9"></a>

###### Table 2.9 CoordinateAxis Methods


Type | Method | Definition
:--- | :--- | :---
`Array` | `array = axis[i:j]` | Read a slice of data from the external file or dataset. Data is returned in the physical ordering defined in the dataset. See Table 2.11 on page 51 for a description of slice operators.
`None` | `axis[i:j] = array` | Write a slice of data to the external file. Dataset axes are read-only.
`None` | `assignValue(array)` | Set the entire value of the axis. `array` is a Numeric array, of the same dimensionality as the axis.
`Axis` | `clone(copyData=1)` | Return a copy of the axis, as a transient axis. If copyData is 1 (the default) the data itself is copied. 
`None` | `designateLatitude(persistent=0)` | Designate the axis to be a latitude axis. If persistent is true, the external file or dataset (if any) is modified. By default, the designation is temporary.
`None` | `designateLevel(persistent=0)` | Designate the axis to be a vertical level axis. If persistent is true, the external file or dataset (if any) is modified. By default, the designation is temporary.
`None` | `designateLongitude(persistent=0, modulo=360.0)` | Designate the axis to be a longitude axis. `modulo` is the modulus value. Any given axis value `x` is treated as equivalent to `x + modulus`. If `persistent` is true, the external file or dataset (if any) is modified. By default, the designation is temporary.
`None` | `designateTime(persistent=0, calendar = cdtime.MixedCalendar)` | Designate the axis to be a time axis. If `persistent` is true, the external file or dataset (if any) is modified. By default, the designation is temporary. `calendar` is defined as in `getCalendar()`.
`Array` | `getBounds()` | Get the associated boundary array. The shape of the return array depends on the type of axis:
 | | `Axis`: `(n,2)`
 | | `Axis2D`: `(i,j,4)`
 | | `AuxAxis1D`: `(ncell, nvert)` where nvert is the maximum number of vertices of a cell.
 | |If the boundary array of a latitude or longitude `Axis` is not explicitly defined, and `autoBounds` mode is on, a default array is generated by calling `genGenericBounds`. Otherwise if auto-Bounds mode is off, the return value is `None`. See `setAutoBounds`.
`Integer` | `getCalendar()` | Returns the calendar associated with the `(time)`axis. Possible return values, as defined in the `cdtime` module, are:
  ||  `cdtime.GregorianCalendar`: the standard Gregorian calendar
  ||  `cdtime.MixedCalendar`: mixed Julian/Gregorian calendar
  ||  `cdtime.JulianCalendar`: years divisible by 4 are leap years
  ||  `cdtime.NoLeapCalendar`: a year is 365 days
  ||  `cdtime.Calendar360`: a year is 360 days
  ||  `None`: no calendar can be identified
  || Note: If the axis is not a time axis, the global, file-related calendar is returned.
  `Array` | `getValue()` | Get the entire axis vector.
  `Integer` | `isLatitude()` | Returns true iff the axis is a latitude axis.
  `Integer` | `isLevel()` | Returns true iff the axis is a level axis.
  `Integer` | `isLongitude()` | Returns true iff the axis is a longitude axis.
  `Integer` | `isTime()` | Returns true iff the axis is a time axis.
`Integer` |`len(axis)` | The length of the axis if one-dimensional. If multidimensional, the length of the first dimension.
`Integer` | `size()` | The number of elements in the axis.
`String` |  `typecode()` | The `Numeric` datatype identifier.


<a name="table_2.10"></a>

###### Table 2.10 Axis Methods, additional to CoordinateAxis methods


Type | Method | Definition
:--- | :--- | :---
`List` of component times | `asComponentTime(calendar=None)` | `Array` version of `cdtime tocomp`. Returns a `List` of component times.
`List` of relative times | `asRelativeTime()` | `Array` version of `cdtime torel`. Returns a `List` of relative times.
`None` | `designateCircular(modulo, persistent=0)` | Designate the axis to be circular. `modulo` is the modulus value. Any given axis value `x` is treated as equivalent to `x + modulus`. If `persistent` is `True`, the external file or dataset (if any) is modified. By default, the designation is temporary.
`Integer` | `isCircular()` | Returns `True` if the axis has circular topology. An axis is defined as circular if:
  | |  `axis.topology == 'circular'`, or
  ||  `axis.topology` is undefined, and the axis is a longitude. The default cycle for circular axes is 360.0
`Integer` | `isLinear()` | Returns `True` if the axis has a linear representation.
`Tuple` | `mapInterval(interval)` | Same as `mapIntervalExt`, but returns only the tuple `(i,j)`, and `wraparound` is restricted to one cycle.
`(i,j,k)` |  `mapIntervalExt(interval)` | Map a coordinate interval to an index `interval`. `interval` is a tuple having one of the forms:
  || `(x,y)`
  || `(x,y,indicator)`
  || `(x,y,indicator,cycle)`
  || `None or ':'`
  || where `x` and `y` are coordinates indicating the interval `[x,y)`, and: 
  || `indicator` is a two or three-character string, where the first character is `'c'` if the interval is closed on the left, `'o'` if open, and the second character has the same meaning for the right-hand point. If present, the third character specifies how the interval should be intersected with the axis:
  || `'n'` - select node values which are contained in the interval
  || `'b'` -select axis elements for which the corresponding cell boundary intersects the interval
  || `'e'` - same as n, but include an extra node on either side
  || `'s'` - select axis elements for which the cell boundary is a subset of the interval
  || The default indicator is 'ccn', that is, the interval is closed, and nodes in the interval are selected. 
  || If `cycle` is specified, the axis is treated as circular with the given cycle value. By default, if `axis.isCircular()` is true, the axis is treated as circular with a default modulus of `360.0`.
|| An interval of `None` or `':'` returns the full index interval of the axis.
|| The method returns the corresponding index interval as a 3tuple `(i,j,k)`, where `k` is the integer stride, and `[i.j)` is the half-open index interval `i <= k < j` `(i >= k > j if k < 0)`, or `none` if the intersection is empty.
||for an axis which is circular (`axis.topology == 'circular'`), `[i,j)` is interpreted as follows, where `n = len(axis)`
|| if `0 <= i < n` and `0 <= j <= n`, the interval does not wrap around the axis endpoint.
|| otherwise the interval wraps around the axis endpoint. 
|| see also: `mapinterval`, `variable.subregion()`
`transientaxis` | `subaxis(i,j,k=1)` | create an axis associated with the integer range `[i:j:k]`. the stride `k` can be positive or negative. wraparound is supported for longitude dimensions or those with a modulus attribute.


<a name="table_2.11"></a>

###### table 2.11 axis slice operators  


slice | definition
--- | ---
`[i]` |  the `ith` element, starting with index `0`
`[i:j]` |  the `ith` element through, but not including, element `j`
`[i:]`  | the `ith` element through and including the end
`[:j]`  | the beginning element through, but not including, element `j`
`[:]`  | the entire array
`[i:j:k]` |   every `kth` element, starting at `i`, through but not including `j`
`[-i]`  | the `ith` element from the end. `-1` is the last element.

**example:** 

a longitude axis has value `[0.0, 2.0, ..., 358.0]`, of length `180`. map the coordinate interval `-5.0 <= x < 5.0` to index interval(s), with wraparound. the result index interval `-2 <= n < 3` wraps around, since `-2 < 0`, and has a stride of `1`. this is equivalent to the two contiguous index intervals `2 <= n < 0` and `0 <= n < 3`

{% highlight python %}
>>> axis.isCircular()
1
>>> axis.mapIntervalExt((-5.0,5.0,'co'))
(-2,3,1)
{% endhighlight %}

<a name="2.6"></a>

#### 2.6 CdmsFile

A `CdmsFile` is a physical file, accessible via the `cdunif` interface. netCDF files are accessible in read-write mode. All other formats (DRS, HDF, GrADS/GRIB, POP, QL) are accessible read-only.

As of CDMS V3, the legacy cuDataset interface is also supported by Cdms-Files. See "cu Module" on page 180.


<a name="table_2.12"></a>

###### Table 2.12 CdmsFile Internal Attributes


Type | Name | Definition
:--- | :--- | :---
`Dictionary` | `attributes` | Global, external file attributes
`Dictionary` | `axes` | Axis objects contained in the file.
`Dictionary` | `grids` | Grids contained in the file.
`String` | `id` | File pathname.
`Dictionary` | `variables` | Variables contained in the file.


<a name="table_2.13"></a>

###### Table 2.13 CdmsFile Constructors


Constructor | Description
--- | ---
`fileobj = cdms.open(path, mode)` | Open the file specified by path returning a CdmsFile object. `path` is the file pathname, a string. `mode` is the open mode indicator, as listed in Table 2.24 on page 70.
`fileobj = cdms.createDataset(path)` | Create the file specified by path, a string.


<a name="table_2.14"></a>

###### Table 2.14 CdmsFile Methods

<table class="table">
  <thead>
    <tr>
      <th style="text-align: left">Type</th>
      <th style="text-align: left">Method</th>
      <th style="text-align: left">Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code>Transient-Variable</code></td>
      <td style="text-align: left"><code>fileobj(varname, selector)</code></td>
      <td style="text-align: left"><p>Calling a <code>CdmsFile</code> object as a function reads the region of data specified by the <code>selector</code>. The result is a transient variable, unless <code>raw = 1</code> is specified. See "Selectors" on page 103.</p><p><strong>Example:</strong> The following reads data for variable 'prc', year 1980:</p><pre style="word-break:normal;">f = cdms.open('test.nc')
x = f('prc', time=('1980-1','1981-1'))</pre></td>
    </tr>
    <tr>
      <td style="text-align: left"><p><code>Variable</code>, <code>Axis</code>, or <code>Grid</code></p></td>
      <td style="text-align: left"><p><code>fileobj['id']</code></p></td>
      <td style="text-align: left"><p>Get the persistent variable, axis or grid object having the string identifier. This does not read the data for a variable.</p><p><strong>Example:</strong> The following gets the persistent variable <code>v</code>, equivalent to <code>v = f.variables['prc']</code>.</p>
      <pre style="word-break:normal;">f = cdms.open('sample.nc')
v = f['prc']</pre><p><strong>Example:</strong> The following gets the axis named time, equivalent to <code>t = f.axes['time']</code>.</p>
      <p><code>t = f['time']</code></p></td>
    </tr>
    <tr>
      <td style="text-align: left"><code>None</code></td>
      <td style="text-align: left"><code>close()</code></td>
      <td style="text-align: left">Close the file.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Axis</code></td>
      <td style="text-align: left"><code>copyAxis(axis, newname=None)</code></td>
      <td style="text-align: left">Copy <code>axis</code> values and attributes to a new axis in the file. The returned object is persistent: it can be used to write axis data to or read axis data from the file. If an axis already exists in the file, having the same name and coordinate values, it is returned. It is an error if an axis of the same name exists, but with different coordinate values. <code>axis</code> is the axis object to be copied. <code>newname</code>, if specified, is the string identifier of the new axis object. If not specified, the identifier of the input axis is used.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Grid</code></td>
      <td style="text-align: left"><code>copyGrid(grid, newname=None)</code></td>
      <td style="text-align: left">Copy grid values and attributes to a new grid in the file. The returned grid is persistent. If a grid already exists in the file, having the same name and axes, it is returned. An error is raised if a grid of the same name exists, having different axes. <code>grid</code> is the grid object to be copied. <code>newname</code>, if specified is the string identifier of the new grid object. If unspecified, the identifier of the input grid is used.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Axis</code></td>
      <td style="text-align: left"><code>createAxis(id, ar, unlimited=0)</code></td>
      <td style="text-align: left">Create a new <code>Axis</code>. This is a persistent object which can be used to read or write axis data to the file. <code>id</code> is an alphanumeric string identifier, containing no blanks. <code>ar</code> is the one-dimensional axis array. Set <code>unlimited</code> to <code>cdms.Unlimited</code> to indicate that the axis is extensible.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>RectGrid</code></td>
      <td style="text-align: left"><code>createRectGrid(id, lat, lon, order, type="generic", mask=None)</code></td>
      <td style="text-align: left">Create a <code>RectGrid</code> in the file. This is not a persistent object: the order, type, and mask are not written to the file. However, the grid may be used for regridding operations. <code>lat</code> is a latitude axis in the file. <code>lon</code> is a longitude axis in the file. <code>order</code> is a string with value <code>"yx"</code> (the first grid dimension is latitude) or <code>"xy"</code> (the first grid dimension is longitude). <code>type</code> is one of <code>'gaussian'</code>,<code>'uniform'</code>,<code>'equalarea'</code>, or <code>'generic'</code>. If specified, <code>mask</code> is a two-dimensional, logical Numeric array (all values are zero or one) with the same shape as the grid.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Variable</code></td>
      <td style="text-align: left"><code>createVariable(String id, String datatype,List axes, fill_value=None)</code></td>
      <td style="text-align: left">Create a new Variable. This is a persistent object which can be used to read or write variable data to the file. <code>id</code> is a String name which is unique with respect to all other objects in the file. <code>datatype</code> is an <code>MA</code> typecode, e.g., <code>MA.Float</code>, <code>MA.Int</code>. <code>axes</code> is a list of Axis and/or Grid objects. <code>fill_value</code> is the missing value (optional).</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Variable</code></td>
      <td style="text-align: left"><code>createVariableCopy(var, newname=None)</code></td>
      <td style="text-align: left"><p>Create a new <code>Variable</code>, with the same name, axes, and attributes as the input variable. An error is raised if a variable of the same name exists in the file. <code>var</code> is the <code>Variable</code> to be copied. <code>newname</code>, if specified is the name of the new variable. If unspecified, the returned variable has the same name as <code>var</code>.</p><p><strong>Note:</strong> Unlike copyAxis, the actual data is not copied to the new variable.</p></td>
    </tr>
    <tr>
      <td style="text-align: left"><code>CurveGrid</code> or <code>Generic-Grid</code></td>
      <td style="text-align: left"><code>readScripGrid(self, whichGrid='destination', check-Grid=1)</code></td>
      <td style="text-align: left">Read a curvilinear or generic grid from a SCRIP netCDF file. The file can be a SCRIP grid file or remapping file. If a mapping file, <code>whichGrid</code> chooses the grid to read, either <code>"source"</code> or <code>"destination"</code>. If <code>checkGrid</code> is <code>1</code> (default), the grid cells are checked for convexity, and 'repaired' if necessary. Grid cells may appear to be nonconvex if they cross a <code>0 / 2pi</code> boundary. The repair consists of shifting the cell vertices to the same side modulo 360 degrees.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>None</code></td>
      <td style="text-align: left"><code>sync()</code></td>
      <td style="text-align: left">Writes any pending changes to the file.</td>
    </tr>
    <tr>
      <td style="text-align: left"><code>Variable</code></td>
      <td style="text-align: left"><pre style="word-break:normal;">write(var, attributes=None, axes=None, extbounds=None, id=None, extend=None, fill_value=None, index=None, typecode=None)</pre></td>
      <td style="text-align: left"><p>Write a variable or array to the file. The return value is the associated file variable.</p><p>If the variable does not exist in the file, it is first defined and  all attributes written, then the data is written. By default, the time dimension of the variable is defined as the unlimited dimension of the file. If the data is already defined, then data is extended or overwritten depending on the value of keywords <code>extend</code> and <code>index</code>, and the unlimited dimension values associated with <code>var</code>.</p><p><code>var</code> is a Variable, masked array, or Numeric array. <code>attributes</code> is the attribute dictionary for the variable. The default is <code>var.attributes</code>. <code>axes</code> is the list of file axes comprising the domain of the variable. The default is to copy <code>var.getAxisList()</code>. <code>extbounds</code> is the unlimited dimension bounds. Defaults to <code>var.getAxis(0).getBounds()</code>. <code>id</code> is the variable name in the file. Default is <code>var.id</code>. <code>extend = 1</code> causes the first dimension to be unlimited: iteratively writeable. The default is <code>None</code>, in which case the first dimension is extensible if it is <code>time.Set</code> to <code>0</code> to turn off this behaviour. <code>fill_value</code> is the missing value flag. <code>index</code> is the extended dimension index to write to. The default index is determined by lookup relative to the existing extended dimension.</p>
      <p><strong>Note:</strong> data can also be written by setting a slice of a file variable, and attributes can be written by setting an attribute of a file variable.</p>
      </td>
    </tr>
  </tbody>
</table>


<a name="table_2.15"></a>

###### Table 2.15 CDMS Datatypes


CDMS Datatype | Definition
---|---
`CdChar` | character
`CdDouble` | double-precision floating-point
`CdFloat` | floating-point
`CdInt`  | integer
`CdLong`|long integer
`CdShort`|short integer

<a name="2.7"></a>

#### 2.7 Database

A Database is a collection of datasets and other CDMS objects. It consists of a hierarchical collection of objects, with the database being at the root, or top of the hierarchy. A database is used to:

- search for metadata
- access data 
- provide authentication and access control for data and metadata 

The figure below illustrates several important points:

- Each object in the database has a relative name of the form tag=id. The id of an object is unique with respect to all objects contained in the parent.

- The name of the object consists of its relative name followed by the relative name(s) of its antecedent objects, up to and including the database name. In the figure below, one of the variables has name `"variable=ua,dataset=ncep_reanalysis_mo,database=CDMS"`.

- Subordinate objects are thought of as being contained in the parent. In this example, the database 'CDMS' contains two datasets, each of which contain several variables.

![Diagram 1](/images/diagram1.jpg)

###### Figure 1

<a name="2.7.1"></a>

##### 2.7.1 Overview

To access a database:

<ol>
  <li>Open a connection. The connect method opens a database connection. connect takes a database URI and returns a database object: <code>db = cdms.connect("ldap://dbhost.llnl.gov/database=CDMS,ou=PCMDI,o=LLNL,c=US")</code>
  </li>
  <li><p>Search the database, locating one or more datasets, variables, and/or other objects.</p><p>The database searchFilter method searches the database. A single database connection may be used for an arbitrary number of searches.</p>
<p>
<b>Example</b>: Find all observed datasets
</p><p>
<code>result = db.searchFilter(category="observed",tag="dataset")</code>
</p>
<p>Searches can be restricted to a subhierarchy of the database.</p>
<p><b>Example:</b> Search just the dataset <code>'ncep_reanalysis_mo'</code>:</p>
<p>
<code>result = db.searchFilter(relbase="dataset=ncep_reanalysis")</code>
</p>
</li>
<li>Refine the search results if necessary. The result of a search can be narrowed with the searchPredicate method.</li>
<li>
  <p>Process the results. A search result consists of a sequence of entries. Each entry has a name, the name of the CDMS object, and an attribute dictionary, consisting of the attributes located by the search:</p>
<p><code>
for entry in result:
  print entry.name, entry.attributes
</code></p>
</li>
<li><p>Access the data. The CDMS object associated with an entry is obtained from the getObject method:</p>
<p><code>obj = entry.getObject()</code></p>
<p>
If the id of a dataset is known, the dataset can be opened directly with the open method:
</p>
<p><code>dset = db.open("ncep_reanalysis_mo")</code></p>
</li>
<li>
<p>Close the database connection:
</p><p>
<code>db.close()</code>
</p>
</li>
</ol>


<a name="table_2.16"></a>

###### Table 2.16 Database Internal Attributes


|Type|Name|Summary|
|---|---|---|
|`Dictionary`|`attributes`|Database attribute dictionary|
|`LDAP`|`db`|(LDAP only) LDAP database object|
|`String`|`netloc`|Hostname, for server-based databases|
|`String`|`path`|path name|
|`String`|`uri`|Uniform Resource Identifier|


<a name="table_2.17"></a>

###### Table 2.17 Database Constructors


|Constructor|Description|
|---|---|
|`db = cdms.connect(uri=None, user="", password="")`|Connect to the database. `uri` is the Universal Resource Indentifier of the database. The form of the URI depends on the implementation of the database. For a Lightweight Directory Access Protocol (LDAP) database, the form is: `ldap://host[:port]/dbname`. For example, if the database is located on host dbhost.llnl.gov, and is named `'database=CDMS,ou=PCMDI,o=LLNL,c=US'`, the URI is: `ldap://dbhost.llnl.gov/database=CDMS,ou=PCMDI,o=LLNL,c=US`. If unspecified, the URI defaults to the value of environment variable CDMSROOT. `user` is the user ID. If unspecified, an anonymous connection is made. `password` is the user password. A password is not required for an anonymous connection|


<a name="table_2.18"></a>

###### Table 2.18 Database Methods


<table class="table">
<tr>
<th>Type</th>
<th>Method</th>
<th>Definition</th>
</tr>
<tr>
<td>None</td>
<td><code>close()</code></td>
<td>Close a database connection.</td></tr>
<tr>
<td>List</td>
<td><code>listDatasets()</code></td><td>Return a list of the dataset IDs in this database. A dataset ID can be passed to the <code>open</code> command.</td></tr>
<tr>
<td>Dataset</td>
<td><code>open(dsetid, mode='r')</code></td><td>
<p>Open a dataset.</p>
<p><code>dsetid</code> is the string dataset identifier</p>
<p><code>mode</code> is the open mode, 'r' - read-only, 'r+' - read-write, 'w' - create.</p>
<p><code>openDataset</code> is a synonym for <code>open</code>.</p></td></tr>
<tr>
<td>SearchResult</td>
<td>
  <pre style="word-break: normal;">
searchFilter(filter=None, tag=None, relbase=None, scope=Subtree, attnames=None, timeout=None)
  </pre>
</td>
<td>
  <p>Search a CDMS database.</p>
  <p><code>filter</code> is the string search filter. Simple filters have the form "tag = value". Simple filters can be combined using logical operators '&amp;', '|', '!' in prefix notation.</p>
  <p><b>Example:</b></p>
  <p>The filter <code>'(&amp;(objec)(id=cli))'</code> finds all variables named "cli".</p>
  <p>A formal definition of search filters is provided in the following section.</p>
  <p><code>tag</code> restricts the search to objects with that tag ("dataset" | "variable" | "database" | "axis" | "grid").</p>
  <p><code>relbase</code> is the relative name of the base object of the search. The search is restricted to the base object and all objects below it in the hierarchy.</p>
  <p><b>Example:</b></p>
 <p>To search only dataset 'ncep_reanalysis_mo', specify:</p>
 <p>
  <code>relbase="dataset=ncep_reanalysis_mo" </code>
  </p>
  <p>
  To search only variable 'ua' in 'ncep_reanalysis_mo', use:
  </p>
  <p>
<code>relbase="variable=ua,dataset=ncep_reanalysis_mo"</code></p>
<p>If no base is specified, the entire database is searched. See the <code>scope</code> argument also.</p>
<p>
  <code>scope</code> is the search scope (<b>Subtree</b> | <b>Onelevel</b> | <b>Base</b>).
</p>
   <ul>
    <li><b>Subtree</b> searches the base object and its descendants.</li>
    <li><b>Onelevel</b> searches the base object and its immediate descendants.</li>
    <li><b>Base</b>searches the base object alone.</li>
   </ul>
<p>The default is <b>Subtree</b>.</p>
<p>
<code>attnames</code>: list of attribute names. Restricts the attributes returned. If <code>None</code>, all attributes are returned. Attributes 'id' and 'objectclass' are always included in the list.
</p>
<p>
<code>timeout</code>: integer number of seconds before timeout. The default is no timeout.</p>
</td>
</tr>
</table>


<a name="2.7.2"></a>

##### 2.7.2 Searching a database

The `searchFilter` method is used to search a database. The result is called a search result, and consists of a sequence of result entries.

In its simplest form, `searchFilter` takes an argument consisting of a string filter. The search returns a sequence of entries, corresponding to those objects having an attribute which matches the filter. Simple filters have the form (tag = value), where value can contain wildcards. For example:

{% highlight text %}
(id = ncep*)
(project = AMIP2)
{% endhighlight %}

Simple filters can be combined with the logical operators '&', '|', '!'. For example,

{% highlight text %}
(&(id = bmrc*)(project = AMIP2))
{% endhighlight %}

matches all objects with id starting with bmrc, and a project attribute with value 'AMIP2'.

Formally, search filters are strings defined as follows:

{% highlight text %}
filter ::= "(" filtercomp ")"

filtercomp ::= "&" filterlist | # and
"|" filterlist | # or
"!" filterlist | # not
simple

filterlist ::= filter | filter filterlist
simple ::= tag op value
op ::= "=" | # equality

"~=" | # approximate equality
"<=" | # lexicographically less than or equal to
">=" # lexicographically greater than or equal to

tag ::= string attribute name
value ::= string attribute value, may include '*' as a wild card
{% endhighlight %}

Attribute names are defined in the chapter on "Climate Data Markup Language (CDML)" on page 149. In addition, some special attributes are defined for convenience:

- `category` is either "experimental" or "observed"
- `parentid` is the ID of the parent dataset
- `project` is a project identifier, e.g., "AMIP2"
- `objectclass` is the list of tags associated with the object. 

The set of objects searched is called the search scope. The top object in the hierarchy is the base object. By default, all objects in the database are searched, that is, the database is the base object. If the database is very large, this may result in an unnecessarily slow or inefficient search. To remedy this the search scope can be limited in several ways:

- The base object can be changed.
- The scope can be limited to the base object and one level below, or to just the base object.
- The search can be restricted to objects of a given class (dataset, variable, etc.)
- The search can be restricted to return only a subset of the object attributes 
- The search can be restricted to the result of a previous search. 
- 
A search result is accessed sequentially within a for loop:

{% highlight python %}
result = db.searchFilter('(&(category=obs*)(id=ncep*))')
for entry in result:
  print entry.name
{% endhighlight %}

Search results can be narrowed using `searchPredicate`. In the following example, the result of one search is itself searched for all variables defined on a 94x192 grid:

{% highlight python %}
>>> result = db.searchFilter('parentid=ncep*',tag="variable")
>>> len(result)
65
>>> result2 = result.searchPredicate(lambda x: 

x.getGrid().shape==(94,192))
>>> len(result2)
3
>>> for entry in result2: print entry.name
variable=rluscs,dataset=ncep_reanalysis_mo,database=CDMS,ou=PCMDI,

      o=LLNL, c=US
variable=rlds,dataset=ncep_reanalysis_mo,database=CDMS,ou=PCMDI,

      o=LLNL, c=US
variable=rlus,dataset=ncep_reanalysis_mo,database=CDMS,ou=PCMDI,

      o=LLNL, c=US
{% endhighlight %}


<a name="table_2.19"></a>

###### Table 2.19 SearchResult Methods


|Type|Method|Definition|
|---|---|---|
|ResultEntry|`[i]`| Return the i-th search result. Results can also be returned in a for loop: `for entry in db.searchResult(tag="dataset"):`|
|Integer|`len()`|Number of entries in the result.|
|SearchResult|`searchPredicate(predicate, tag=None)`|Refine a search result, with a predicate search. `predicate` is a function which takes a single CDMS object and returns true (1) if the object satisfies the predicate, 0 if not. `tag` restricts the search to objects of the class denoted by the tag. **Note**: In the current implementation, `searchPredicate`is much less efficient than `searchFilter`. For best performance, use `searchFilter` to narrow the scope of the search, then use `searchPredicate` for more general searches.|


A search result is a sequence of result entries. Each entry has a string name, the name of the object in the database hierarchy, and an attribute dictionary. An entry corresponds to an object found by the search, but differs from the object, in that only the attributes requested are associated with the entry. In general, there will be much more information defined for the associated CDMS object, which is retrieved with the `getObject` method.


<a name="table_2.20"></a>

###### Table 2.20 ResultEntry Attributes


|Type|Name|Description|
|---|---|---|
|String|`name`|The name of this entry in the database.|
|Dictionary|`attributes`|The attributes returned from the search. `attributes[key]` is a list of all string values associated with the key|



<a name="table_2.21"></a>

###### Table 2.21 ResultEntry Methods


Type|Method|Definition
---|---|---
`CdmsObj`|`getObject()`|Return the CDMS object associated with this entry. **Note:** For many search applications it is unnecessary to access the associated CDMS object. For best performance this function should be used only when necessary, for example, to retrieve data associated with a variable.

<a name="2.7.3"></a>

##### 2.7.3 Accessing data

To access data via CDMS:

1. Locate the dataset ID. This may involve searching the metadata.
2. Open the dataset, using the open method.
3. Reference the portion of the variable to be read. 

In the next example, a portion of variable 'ua' is read from dataset 'ncep\_reanalysis\_mo':

{% highlight python %}
dset = db.open('ncep_reanalysis_mo')
ua = dset.variables['ua']
data = ua[0,0]
{% endhighlight %}

<a name="2.7.4"></a>

##### 2.7.4 Examples of database searches

In the following examples, db is the database opened with

{% highlight python %}
db = cdms.connect()
{% endhighlight %}

This defaults to the database defined in environment variable `CDMSROOT`.

**Example:**
List all variables in dataset 'ncep\_reanalysis\_mo':

{% highlight python %}
for entry in db.searchFilter(filter = "parentid=ncep_reanalysis_mo",
tag = "variable"):
  print entry.name
{% endhighlight %}

**Example:**
Find all axes with bounds defined:

{% highlight python %}
for entry in db.searchFilter(filter="bounds=*",tag="axis"):
  print entry.name
{% endhighlight %}

**Example:**
Locate all GDT datasets:

{% highlight python %}
for entry in
db.searchFilter(filter="Conventions=GDT*",tag="dataset"):
print entry.name
{% endhighlight %}

**Example:**
Find all variables with missing time values, in observed datasets:

{% highlight python %}
def missingTime(obj):
  time = obj.getTime()
  return time.length != time.partition_length

result = db.searchFilter(filter="category=observed")
for entry in result.searchPredicate(missingTime):
  print entry.name
{% endhighlight %}

**Example:**
Find all CMIP2 datasets having a variable with id "hfss":

{% highlight python %}
for entry in db.searchFilter(filter = "(&(project=CMIP2)(id=hfss))", tag = "variable"):
  print entry.getObject().parent.id
{% endhighlight %}

**Example:**
Find all observed variables on 73x144 grids:

{% highlight python %}
result = db.searchFilter(category='obs*')
for entry in result.searchPredicate(lambda x: x.getGrid().shape==(73,144),tag="variable"):
  print entry.name
{% endhighlight %}

**Example:**
Find all observed variables with more than 1000 timepoints:

{% highlight python %}
result = db.searchFilter(category='obs*')
for entry in result.searchPredicate(lambda x: len(x.getTime())>1000, tag = "variable"):
  print entry.name, len(entry.getObject().getTime())
{% endhighlight %}

**Example:**
Find the total number of each type of object in the database

{% highlight python %}
print len(db.searchFilter(tag="database")),"database"
print len(db.searchFilter(tag="dataset")),"datasets"
print len(db.searchFilter(tag="variable")),"variables"
print len(db.searchFilter(tag="axis")),"axes"
{% endhighlight %}

<a name="2.8"></a>

#### 2.8 Dataset

A Dataset is a virtual file. It consists of a metafile, in CDML/XML representation, and one or more data files.

As of CDMS V3, the legacy cuDataset interface is supported by Datasets. See "cu Module" on page 180.


<a name="table_2.22"></a>

###### Table 2.22 Dataset Internal Attributes 


Type | Name | Description
---| ---| ---
Dictionary |    `attributes`     | Dataset external attributes.
Dictionary    | `axes`     |Axes contained in the dataset.
String    | `datapath` |    Path of data files, relative to the parent database. If no parent, the datapath is absolute.
Dictionary | `grids` | Grids contained in the dataset.
String | `mode` | Open mode.
Database | `parent` | Database which contains this dataset. If the dataset is not part of a database, the value is `None`.
String | `uri` | Uniform Resource Identifier of this dataset.
Dictionary | `variables` | Variables contained in the dataset.
Dictionary | `xlinks` | External links contained in the dataset.


<a name="table_2.23"></a>

###### Table 2.23 Dataset Constructors


|Constructor |Description|
|---|---|
|`datasetobj = cdms.open(String uri, String mode='r')`|Open the dataset specified by the Universal Resource Indicator, a CDML file. Returns a Dataset object. mode is one of the indicators listed in Table 2.24 on page 70. `openDataset` is a synonym for `open`|


<a name="table_2.24"></a>

###### Table 2.24 Open Modes


|Mode|Definition|
|---|---|
|'r'|read-only|
|'r+'|read-write|
|'a'|read-write. Open the file if it exists, otherwise create a new file|
|'w'|Create a new file, read-write|


<a name="table_2.25"></a>

###### Table 2.25 Dataset Methods


<table class="table">
    <tbody>
      <tr>
        <th>Type</th>

        <th>Method</th>

        <th>Definition</th>
      </tr>

      <tr>
        <td>Transient-Variable</td>

        <td><code>datasetobj(varname, selector)</code></td>

        <td>
          Calling a Dataset object as a function reads the region of data defined by the
          selector. The result is a transient variable, unless <code>raw = 1</code> is
          specified. See "Selectors" on page 103.

          <p><b>Example:</b> The following reads data for variable 'prc', year 1980:</p>
          <pre style="word-break:normal;">
f = cdms.open('test.xml')
x = f('prc', time=('1980-1','1981-1'))</pre>
        </td>
      </tr>

      <tr>
        <td>Variable, Axis, or Grid</td>

        <td><code>datasetobj['id']</code></td>

        <td>
          <p>The square bracket operator applied to a dataset gets the persistent
          variable, axis or grid object having the string identifier. This does not read
          the data for a variable. Returns <code>None</code> if not found.</p>

          <p><b>Example:</b></p>
          <pre style="word-break:normal;">
f = cdms.open('sample.xml')
v = f['prc']</pre>

          <p>gets the persistent variable v, equivalent to <code>v =
          f.variables['prc']</code>.</p>

          <p><b>Example:</b></p>

          <p><code>t = f['time']</code><br />
          gets the axis named 'time', equivalent to <code>t = f.axes['time']</code></p>
        </td>
      </tr>

      <tr>
        <td><code>None</code><br />
        <br /></td>

        <td><code>close()</code></td>

        <td>Close the dataset.</td>
      </tr>

      <tr>
        <td>
          <p><code>RectGrid</code></p>
        </td>

        <td>
          <p><code>createRectGrid(id, lat, lon, order, type="generic",
          mask=None)</code></p>
        </td>

        <td>
          <p>Create a RectGrid in the dataset. This is not a persistent object: the
          order, type, and mask are not written to the dataset. However, the grid may be
          used for regridding operations.</p>

          <p><code>lat</code> is a latitude axis in the dataset.</p>

          <p><code>lon</code> is a longitude axis in the dataset.</p>

          <p><code>order</code> is a string with value "yx" (the first grid dimension is
          latitude) or "xy" (the first grid dimension is longitude).</p>

          <p><code>type</code> is one of 'gaussian','uniform','equalarea',or
          'generic'</p>

          <p>If specified, <code>mask</code> is a two-dimensional, logical Numeric array
          (all values are zero or one) with the same shape as the grid.</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>Axis</p>
        </td>

        <td>
          <p><code>getAxis(id)</code></p>
        </td>

        <td>
          <p>Get an axis object from the file or dataset.</p>

          <p><code>id</code> is the string axis identifier.</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>Grid</p>
        </td>

        <td>
          <p><code>getGrid(id)</code></p>
        </td>

        <td>
          <p>Get a grid object from a file or dataset.</p>

          <p><code>id</code> is the string grid identifier.</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>List</p>
        </td>

        <td>
          <p><code>getPaths()</code></p>
        </td>

        <td>
          <p>Get a sorted list of pathnames of datafiles which comprise the dataset. This
          does not include the XML metafile path, which is stored in the .uri
          attribute.</p>
        </td>
      </tr>

      <tr>
        <td>
          <p>Variable</p>
        </td>

        <td>
          <p><code>getVariable(id)</code></p>
        </td>

        <td>
          <p>Get a variable object from a file or dataset.</p>

          <p><code>id</code> is the string variable identifier.</p>
        </td>
      </tr>

    <tr>
      <td>CurveGrid or GenericGrid</td>

      <td><code>readScripGrid(self, whichGrid='destination', check-or Generic-Grid=1)</code></td>

      <td>
        <p>Read a curvilinear or generic grid from a SCRIP dataset. The dataset can be a SCRIP grid file or remapping file.</p>

        <p>If a mapping file, <code>whichGrid</code> chooses the grid to read, either <code>"source"</code> or <code>"destination"</code>.</p>

        <p>If <code>checkGrid</code> is 1 (default), the grid cells are checked for convexity, and 'repaired' if necessary. Grid cells may appear to be nonconvex if they cross a <code>0 / 2pi</code> boundary. The repair consists of shifting the cell vertices to the same side modulo 360 degrees.</p>
      </td>
    </tr>

    <tr>
      <td>None<br /><br /></td>
      <td><code>sync()</code></td>
      <td>Write any pending changes to the dataset.</td>
    </tr>
  </tbody>
</table>



<a name="2.9"></a>

#### 2.9 MV module

The fundamental CDMS data object is the variable. A variable is comprised of:

- a masked data array, as defined in the NumPy MA module.
- a domain: an ordered list of axes and/or grids.
- an attribute dictionary. 

The MV module is a work-alike replacement for the MA module, that carries along the domain and attribute information where appropriate. MV provides the same set of functions as MA. However, MV functions generate transient variables as results. Often this simplifies scripts that perform computation. MA is part of the Python Numeric package, documented at http://www.numpy.org.

MV can be imported with the command:

{% highlight text %}
import MV
{% endhighlight %}

The command

{% highlight text %}
from MV import *
{% endhighlight %}

allows use of MV commands without any prefix.

Table 2.26 on page 75 lists the constructors in MV. All functions return a transient variable. In most cases the keywords axes, attributes, and id are available. axes is a list of axis objects which specifies the domain of the variable. attributes is a dictionary. id is a special attribute string that serves as the identifier of the variable, and should not contain blanks or non-printing characters. It is used when the variable is plotted or written to a file. Since the id is just an attribute, it can also be set like any attribute:

{% highlight text %}
var.id = 'temperature'
{% endhighlight %}

For completeness MV provides access to all the MA functions. The functions not listed in the following tables are identical to the corresponding MA function: `allclose`, `allequal`, `common_fill_value`, `compress`, `create_mask`, `dot`, `e`, `fill_value`, `filled`, `get_print_limit`, `getmask`, `getmaskarray`, `identity`, `indices`, `innerproduct`, `isMA`, `isMaskedArray`, `is_mask`, `isarray`, `make_mask`, `make_mask_none`, `mask_or`, `masked`, `pi`, `put`, `putmask`, `rank`, `ravel`, `set_fill_value`, `set_print_limit`, `shape`, `size`. See the documentation at http://numpy.sourceforge.net for a description of these functions.



<a name="table_2.26"></a>

###### Table 2.26 Variable Constructors in module MV


|Constructor|Description|
|---|---|
|`arrayrange(start, stop=None, step=1, typecode=None, axis=None, attributes=None, id=None)`|Just like `MA.arange()` except it returns a variable whose type can be specfied by the keyword argument typecode. The axis, attribute dictionary, and string identifier of the result variable may be specified. _Synonym:_ `arange`|
|`masked_array(a, mask=None, fill_value=None, axes=None, attributes=None, id=None)`|Same as MA.masked_array but creates a variable instead. If no axes are specified, the result has default axes, otherwise axes is a list of axis objects matching a.shape.|
|`masked_object(data, value, copy=1, savespace=0, axes=None, attributes=None, id=None)`|Create variable masked where exactly data equal to value. Create the variable with the given list of axis objects, attribute dictionary, and string id.|
|`masked_values(data, value, rtol=1e-05, atol=1e-08, copy=1, savespace=0, axes=None, attributes=None, id=None)`|Constructs a variable with the given list of axes and attribute dictionary, whose mask is set at those places where `abs(data - value) &lt; atol + rtol * abs(data)`. This is a careful way of saying that those elements of the data that have value = value (to within a tolerance) are to be treated as invalid. If data is not of a floating point type, calls masked_object instead.|
|`ones(shape, typecode='l', savespace=0, axes=none, attributes=none, id=none)`|return an array of all ones of the given length or shape.|
|`reshape(a, newshape, axes=none, attributes=none, id=none)`|copy of a with a new shape.|
|`resize(a, new_shape, axes=none, attributes=none, id=none)`|return a new array with the specified shape. the original arrays total size can be any size.|
|`zeros(shape, typecode='l', savespace=0, axes=none, attributes=none, id=none)`|an array of all zeros of the given length or shape|

The following table describes the MV non-constructor functions. with the exception of argsort, all functions return a transient variable.


<a name="table_2.27"></a>

###### Table 2.27 MV functions


|Function|Description|
|---|---|
|`argsort(x, axis=-1, fill_value=None)`|Return a Numeric array of indices for sorting along a given axis.|
|`asarray(data, typecode=None)`|Same as `cdms.createVariable(data, typecode, copy=0)`. This is a short way of ensuring that something is an instance of a variable of a given type before proceeding, as in `data = asarray(data)`. Also see the variable `astype()` function.|
|`average(a, axis=0, weights=None)`|Computes the average value of the non-masked elements of x along the selected axis. If weights is given, it must match the size and shape of x, and the value returned is: `sum(a*weights)/sum(weights)` In computing these sums, elements that correspond to those that are masked in x or weights are ignored.|
|`choose(condition, t)`|Has a result shaped like array condition. `t` must be a tuple of two arrays `t1` and `t2`. Each element of the result is the corresponding element of `t1`where `condition` is true, and the corresponding element of `t2` where `condition` is false. The result is masked where `condition` is masked or where the selected element is masked.|
|`concatenate(arrays, axis=0, axisid=None, axisattributes=None)`|Concatenate the arrays along the given axis. Give the extended axis the id and attributes provided - by default, those of the first array.|
|`count(a, axis=None)`|Count of the non-masked elements in `a`, or along a certain axis.|
|`isMaskedVariable(x)`|Return true if `x` is an instance of a variable.|
|`masked_equal(x, value)`|`x` masked where `x` equals the scalar value. For floating point values consider `masked_values(x, value)` instead.|
|`masked_greater(x, value)`|`x` masked where `x > value`|
|`masked_greater_equal(x, value)`|`x` masked where `x >= value`|
|`masked_less(x, value)`|`x` masked where `x &lt; value`|
|`masked_less_equal(x, value)`|`x` masked where `x &le; value`|
|`masked_not_equal(x, value)`|`x` masked where `x != value`|
|`masked_outside(x, v1, v2)`|`x` with mask of all values of `x` that are outside `[v1,v2]`|
|`masked_where(condition, x, copy=1)`|Return `x` as a variable masked where condition is true. Also masked where `x` or `condition` masked. `condition` is a masked array having the same shape as `x`.|
|`maximum(a, b=None)`|Compute the maximum valid values of `x` if `y` is `None`; with two arguments, return the element-wise larger of valid values, and mask the result where either `x` or `y` is masked.|
|`minimum(a, b=None)`|Compute the minimum valid values of `x` if `y` is None; with two arguments, return the element-wise smaller of valid values, and mask the result where either `x` or `y` is masked.|
|`outerproduct(a, b)`|Return a variable such that `result[i, j] = a[i] * b[j]`. The result will be masked where `a[i]` or `b[j]` is masked.|
|`power(a, b)`|`a**b`|
|`product(a, axis=0, fill_value=1)`|Product of elements along axis using `fill_value` for missing elements.|
|`repeat(ar, repeats, axis=0)`|Return `ar` repeated `repeats` times along `axis`. `repeats` is a sequence of length `ar.shape[axis]` telling how many times to repeat each element.|
|`set_default_fill_value(value_type, value)`|Set the default fill value for `value_type` to `value`. `value_type` is a string: 'real','complex','character','integer',or 'object'. `value` should be a scalar or single-element array.|
|`sort(ar, axis=-1)`|Sort array `ar` elementwise along the specified axis. The corresponding axis in the result has dummy values.|
|`sum(a, axis=0, fill_value=0)`|Sum of elements along a certain axis using `fill_value` for missing.|
|`take(a, indices, axis=0)`|Return a selection of items from `a`. See the documentation in the Numeric manual.|
|`transpose(ar, axes=None)`|Perform a reordering of the axes of array ar depending on the tuple of indices axes; the default is to reverse the order of the axes.|
|`where(condition, x, y)`|`x` where `condition` is true, `y` otherwise|


<a name="2.10"></a>

#### 2.10 HorizontalGrid
A HorizontalGrid represents a latitude-longitude coordinate system. In addition, it optionally describes how lat-lon space is partitioned into cells. Specifically, a HorizontalGrid:

  - consists of a latitude and longitude coordinate axis.
  - may have associated boundary arrays describing the grid cell boundaries,
  - may optionally have an associated logical mask. 

CDMS supports several types of HorizontalGrids:


<a name="table_2.28"></a>

###### Table 2.28


|Grid Type|Definition|
|---|---|
|`RectGrid`|Associated latitude an longitude are 1-D axes, with strictly monotonic values.|
|`CurveGrid`|Latitude and longitude are 2-D coordinate axes (Axis2D).|
|`GenericGrid`|Latitude and longitude are 1-D auxiliary coordinate axis (AuxAxis1D)|


<a name="table_2.29"></a>

###### Table 2.29 HorizontalGrid Internal Attribute


|Type|Name|Definition|
|---|---|---|
|Dictionary|`attributes`|External attribute dictionary.|
|String|`id`|The grid identifier.|
|Dataset or CdmsFile|`parent`|The dataset or file which contains the grid.|
|Tuple|`shape`|The shape of the grid, a 2-tuple|

Table 2.31 on page 82 describes the methods that apply to all types of HorizontalGrids. Table 2.32 on page 86 describes the additional methods that are unique to RectGrids.


<a name="table_2.30"></a>

###### Table 2.30 RectGrid Constructors


|Constructor|Description|
|---|---|
|`cdms.createRectGrid(lat, lon, order, type="generic", mask=None)`|Create a grid not associated with a file or dataset. See Table 2.2 on page 33.|
|`CdmsFile.createRectGrid(id, lat, lon, order, type="generic", mask=None)`|Create a grid associated with a file. See Table 2.14 on page 53.|
|`Dataset.createRectGrid(id, lat, lon, order, type="generic", mask=None)`|Create a grid associated with a dataset. See Table 2.25 on page 71.|
|`cdms.createGaussianGrid(nlats, xorigin=0.0, order="yx")`|See Table 2.2 on page 33.|
|`cdms.createGenericGrid(latArray, lonArray, latBounds=None, lonBounds=None, order="yx", mask=None)`|See Table 2.2 on page 18.|
|`cdms.createGlobalMeanGrid(grid)`|See Table 2.2 on page 18.|
|`cdms.createRectGrid(lat, lon, order, type="generic", mask=None)`|See Table 2.2 on page 18.|
|`cdms.createUniformGrid(startLat, nlat, deltaLat, startLon, nlon, deltaLon, order="yx", mask=None)`|See Table 2.2 on page 18.|
|`cdms.createZonalGrid(grid)`|See Table 2.2 on page 18|
    


<a name="table_2.31"></a>

###### Table 2.31 HorizontalGrid Methods  

<table class="table">
  <tbody>
    <tr>
      <th>Type</th>

      <th>Method</th>

      <th>Description</th>
    </tr>

    <tr>
      <td>
        <p><span>Horizontal-Grid</span></p>
      </td>

      <td><code>clone()</code></td>

      <td>
        <p>Return a transient copy of the grid.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getAxis(Integer n)</code></td>

      <td>
        <p>Get the n-th axis.n is either 0 or 1.</p>
      </td>
    </tr>

    <tr>
      <td>Tuple</td>

      <td><code>getBounds()</code></td>

      <td>
        <p>Get the grid boundary arrays.</p>

        <p>Returns a tuple <code>(latitudeArray, longitudeArray)</code>, where
        latitudeArray is a Numeric array of latitude bounds, and similarly for
        longitudeArray.The shape of latitudeArray and longitudeArray depend on the type
        of grid:</p>

        <ul>
          <li>for rectangular grids with shape (nlat, nlon), the boundary arrays have
          shape (nlat,2) and (nlon,2).</li>

          <li>for curvilinear grids with shape (nx, ny), the boundary arrays each have
          shape (nx, ny, 4).</li>

          <li>for generic grids with shape (ncell,), the boundary arrays each have
          shape (ncell, nvert) where nvert is the maximum number of vertices per
          cell.</li>
        </ul>

        <p>For rectilinear grids: If no boundary arrays are explicitly defined (in the
        file or dataset), the result depends on the auto- Bounds mode (see
        <code>cdms.setAutoBounds</code>) and the grid classification mode (see
        <code>cdms.setClassifyGrids</code>). By default, autoBounds mode is enabled, in
        which case the boundary arrays are generated based on the type of grid. If
        disabled, the return value is (None,None).For rectilinear grids: The grid
        classification mode specifies how the grid type is to be determined. By
        default, the grid type (Gaussian, uniform, etc.) is determined by calling
        <span>grid.classifyInFamily</span>. If the mode is 'off'
        <span>grid.getType</span> is used instead.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getLatitude()</code></td>

      <td>
        <p>Get the latitude axis of this grid.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getLongitude()</code></td>

      <td>
        <p>Get the latitude axis of this grid.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getMask()</code></td>

      <td>
        <p>Get the mask array of this grid, if any.Returns a 2-D Numeric array, having
        the same shape as the grid. If the mask is not explicitly defined, the return
        value is <code>None</code>.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getMesh(self, transpose=None)</code></td>

      <td>
        <p>Generate a mesh array for the meshfill graphics method.If transpose is
        defined to a tuple, say (1,0), first transpose latbounds and lonbounds
        according to the tuple, in this case (1,0,2).</p>
      </td>
    </tr>

    <tr>
      <td>None</td>

      <td><code>setBounds(latBounds, lonBounds, persistent=0)</code></td>

      <td>
        <p>Set the grid boundaries.<code>latBounds</code> is a NumPy array of shape
        (n,2), such that the boundaries of the kth axis value are
        <code>[latBounds[k,0],latBounds[k,1] ]</code>. <code>lonBounds</code> is
        defined similarly for the longitude array. <b>Note:</b> By default, the
        boundaries are not written to the file or dataset containing the grid (if any).
        This allows bounds to be set on read-only files, for regridding. If the
        optional argument <code>persistent</code> is set to 1, the boundary array is
        written to the file.</p>
      </td>
    </tr>

    <tr>
      <td>None</td>

      <td><code>setMask(mask, persistent=0)</code></td>

      <td>
        <p>Set the grid mask. If <code>persistent == 1</code>, the mask values are
        written to the associated file, if any. Otherwise, the mask is associated with
        the grid, but no I/O is generated. <code>mask</code> is a two-dimensional,
        Boolean-valued Numeric array, having the same shape as the grid.</p>
      </td>
    </tr>

    <tr>
      <td>Horizontal-Grid</td>

      <td><code>subGridRegion(latInterval, lonInterval)</code></td>

      <td>
        <p>Create a new grid corresponding to the coordinate region defined by
        <code>latInterval, lonInterval.</code></p>

        <p><code>latInterval</code> and <code>lonInterval</code> are the coordinate
        intervals for latitude and longitude, respectively.</p>

        <p>Each interval is a tuple having one of the forms:</p>

        <ul>
          <li><code>(x,y)</code></li>

          <li><code>(x,y,indicator)</code></li>

          <li><code>(x,y,indicator,cycle)</code></li>

          <li><code>None</code></li>
        </ul>

        <p>where <code>x</code> and <code>y</code> are coordinates indicating the
        interval <code>[x,y)</code>, and:</p>

        <p><code><span>indicator</span></code> is a two-character string, where the
        first character is 'c' if the interval is closed on the left, 'o' if open, and
        the second character has the same meaning for the right-hand point. (Default:
        'co').</p>

        <p><span>If <code>cycle</code> is specified, the axis is treated as circular
        with the given cycle value. By default, if <code>grid.isCircular()</code> is
        true, the axis is treated as circular with a default value of 360.0.</span></p>

        <p>An interval of <code>None</code> returns the full index interval of the
        axis.</p>

        <p>If a mask is defined, the subgrid also has a mask corresponding to the index
        ranges.Note: The result grid is not associated with any file or dataset.</p>
      </td>
    </tr>

    <tr>
      <td>
        <p>Transient-CurveGrid</p>
      </td>

      <td><code>toCurveGrid(gridid=None)</code></td>

      <td>
        <p>Convert to a curvilinear grid. If the grid is already curvilinear, a copy of
        the grid object is returned. <code>gridid</code> is the string identifier of
        the resulting curvilinear grid object. If unspecified, the grid ID is copied.
        <b>Note:</b> This method does not apply to generic grids.</p>
      </td>
    </tr>

    <tr>
      <td>
        <p>Transient-GenericGrid</p>
      </td>

      <td><code>toGenericGrid(gridid=None)</code></td>

      <td>
        <p>Convert to a generic grid. If the grid is already generic, a copy of the
        grid is returned. <code>gridid</code> is the string identifier of the resulting
        curvilinear grid object. If unspecified, the grid ID is copied.</p>
      </td>
    </tr>
  </tbody>
</table>
 


<a name="table_2.32"></a>

###### Table 2.32 RectGrid Methods, additional to HorizontalGrid Methods   


<table class='table'>
  <tr>
    <th>Type</th>

    <th>Method</th>

    <th>Description</th>
  </tr>

  <tr>
    <td>String</td>

    <td><code>getOrder()</code></td>

    <td>Get the grid ordering, either "yx" if latitude is the first axis, or "xy" if
    longitude is the first axis.</td>
  </tr>

  <tr>
    <td>String</td>

    <td><code>getType()</code></td>

    <td>Get the grid type, either "gaussian", "uniform", "equalarea", or
    "generic".</td>
  </tr>

  <tr>
    <td>(Array,Array)</td>

    <td><code>getWeights()</code></td>

    <td>
      <p>Get the normalized area weight arrays, as a tuple <code>(latWeights,
      lonWeights)</code>. It is assumed that the latitude and longitude axes are
      defined in degrees.</p>

      <p>The latitude weights are defined as:</p>

      <p><code>latWeights[i] = 0.5 * abs(sin(latBounds[i+1]) -
      sin(latBounds[i]))</code></p>

      <p>The longitude weights are defined as:</p>

      <p><code>lonWeights[i] = abs(lonBounds[i+1] - lonBounds[i])/360.0</code></p>

      <p>For a global grid, the weight arrays are normalized such that the sum of the
      weights is 1.0</p>

      <p><b>Example:</b></p>

      <p>Generate the 2-D weights array, such that <code>weights[i.j]</code> is the
      fractional area of grid zone <code>[i,j]</code>.</p>
      <pre style="word-break:normal;">
from cdms import MV
latwts, lonwts = grid.getWeights()
weights = MV.outerproduct(latwts, lonwts)
</pre>

      <p>Also see the function <code>area_weights</code> in module
      <code>pcmdi.weighting</code>.</p>
    </td>
  </tr>

  <tr>
    <td>None</td>

    <td><code>setType(gridtype)</code></td>

    <td>Set the grid type. <code>gridtype</code> is one of "gaussian", "uniform",
    "equalarea", or "generic".</td>
  </tr>

  <tr>
    <td>RectGrid</td>

    <td><code>subGrid((latStart,latStop),(lonStart,lonStop))</code></td>

    <td>
      <p>Create a new grid, with latitude index range [latStart : latStop] and
      longitude index range [lonStart : lonStop]. Either index range can also be
      specified as None, indicating that the entire range of the latitude or longitude
      is used.</p>

      <p><b>Example:</b></p>

      <p>This creates newgrid corresponding to all latitudes and index range
      [lonStart:lonStop] of oldgrid.</p>

      <p><code>newgrid = oldgrid.subGrid(None, (lonStart, lonStop))</code></p>

      <p>If a mask is defined, the subgrid also has a mask corresponding to the index
      ranges.</p>

      <p><b>Note:</b> The result grid is not associated with any file or dataset.</p>
    </td>
  </tr>

  <tr>
    <td>RectGrid</td>

    <td><code>transpose()</code></td>

    <td>
      <p>Create a new grid, with axis order reversed. The grid mask is also
      transposed.</p>

      <p><b>Note:</b> The result grid is not associated with any file or dataset.</p>
    </td>
  </tr>
</table>
 

<a name="2.11"></a>

#### 2.11 Variable

A Variable is a multidimensional data object, consisting of:

 - a multidimensional data array, possibly masked,
 - a collection of attributes
 - a domain, an ordered tuple of CoordinateAxis objects. 

A Variable which is contained in a Dataset or CdmsFile is called a persistent variable. Setting a slice of a persistent Variable writes data to the Dataset or file, and referencing a Variable slice reads data from the Dataset. Variables may also be transient, not associated with a Dataset or CdmsFile.

Variables support arithmetic operations, including the basic Python operators (+,,*,/,**, abs, and sqrt), as well as the operations defined in the MV module. The result of an arithmetic operation is a transient variable, that is, the axis information is transferred to the result.

The methods subRegion and subSlice return transient variables. In addition, a transient variable may be created with the cdms.createVariable method. The vcs and regrid module methods take advantage of the attribute, domain, and mask information in a transient variable.


<a name="table_2.33"></a>

###### Table 2.33 Variable Internal Attributes


|Type|Name|Definition|
|---|---|---|
|Dictionary|`attributes`|External attribute dictionary.|
|String|`id`|Variable identifier.|
|String|`name\_in\_file`|The name of the variable in the file or files which represent the dataset. If different from id, the variable is aliased.|
|Dataset or CdmsFile|`parent`|The dataset or file which contains the variable.|
|Tuple|`shape`|The length of each axis of the variable|


<a name="table_2.34"></a>

###### Table 2.34 Variable Constructors

<table class="table">
    <tr>
      <th>Constructor</th>

      <th>Description</th>
    </tr>

    <tr>
      <td><code>Dataset.createVariable(String id, String datatype, List axes)</code></td>

      <td>Create a Variable in a Dataset. This function is not yet implemented.</td>
    </tr>

    <tr>
      <td><code>CdmsFile.createVariable(String id, String datatype, List
      axesOr-Grids)</code></td>

      <td>Create a Variable in a CdmsFile. <code>id</code> is the name of the variable.
      <code>datatype</code> is the MA or Numeric typecode, for example, MA.Float.
      <code>axesOrGrids</code> is a list of Axis and/or Grid objects, on which the
      variable is defined. Specifying a rectilinear grid is equivalent to listing the
      grid latitude and longitude axes, in the order defined for the grid. **Note:** this
      argument can either be a list or a tuple. If the tuple form is used, and there is
      only one element, it must have a following comma, e.g.:
      <code>(axisobj,)</code>.</td>
    </tr>

    <tr>
      <td><pre style="word-break:normal;">cdms.createVariable(array, typecode=None, copy=0, savespace=0,mask=None, fill_value=None, grid=None, axes=None,attributes=None, id=None)</pre></td>

      <td>Create a transient variable, not associated with a file or dataset.
      <code>array</code> is the data values: a Variable, masked array, or Numeric array.
      <code>typecode</code> is the MA typecode of the array. Defaults to the typecode of
      array. <code>copy</code> is an integer flag: if 1, the variable is created with a
      copy of the array, if 0 the variable data is shared with array.
      <code>savespace</code> is an integer flag: if set to 1, internal Numeric operations
      will attempt to avoid silent upcasting. <code>mask</code> is an array of integers
      with value 0 or 1, having the same shape as array. array elements with a
      corresponding mask value of 1 are considered invalid, and are not used for
      subsequent Numeric operations. The default mask is obtained from array if present,
      otherwise is None. <code>fill_value</code> is the missing value flag. The default
      is obtained from array if possible, otherwise is set to 1.0e20 for floating point
      variables, 0 for integer-valued variables. <code>grid</code> is a rectilinear grid
      object. <code>axes</code> is a tuple of axis objects. By default the axes are
      obtained from array if present. Otherwise for a dimension of length n, the default
      axis has values [0., 1., ..., double(n)]. <code>attributes</code> is a dictionary
      of attribute values. The dictionary keys must be strings. By default the dictionary
      is obtained from array if present, otherwise is empty. <code>id</code> is the
      string identifier of the variable. By default the id is obtained from array if
      possible, otherwise is set to 'variable_n' for some integer n.</td>
    </tr>
  </table>



<a name="table_2.35"></a>
  
###### Table 2.35 Variable Methods

<table class="table">
    <tr>
      <th>Type</th>

      <th>Method</th>

      <th>Definition</th>
    </tr>

    <tr>
      <td>Variable</td>

      <td><code>tvar = var[ i:j, m:n]</code></td>

      <td>Read a slice of data from the file or dataset, resulting in a transient
      variable. Singleton dimensions are 'squeezed' out. Data is returned in the physical
      ordering defined in the dataset. The forms of the slice operator are listed in
      Table 2.36 on page 102.</td>
    </tr>

    <tr>
      <td>None</td>

      <td><code>var[ i:j, m:n] = array</code></td>

      <td>Write a slice of data to the external dataset. The forms of the slice operator
      are listed in Table 2.21 on page 32. (Variables in CdmsFiles only)</td>
    </tr>

    <tr>
      <td>Variable</td>

      <td><code>tvar = var(selector)</code></td>

      <td>Calling a variable as a function reads the region of data defined by the
      selector. The result is a transient variable, unless raw=1 keyword is specified.
      See "Selectors" on page 103.</td>
    </tr>

    <tr>
      <td>None</td>

      <td><code>assignValue(Array ar)</code></td>

      <td>Write the entire data array. Equivalent to <code>var[:] = ar</code>. (Variables
      in CdmsFiles only).</td>
    </tr>

    <tr>
      <td>Variable</td>

      <td><code>astype(typecode)</code></td>

      <td>Cast the variable to a new datatype. Typecodes are as for MV, MA, and Numeric
      modules.</td>
    </tr>

    <tr>
      <td>Variable</td>

      <td><code>clone(copyData=1)</code></td>

      <td>
        <p>Return a copy of a transient variable.</p>

        <p>If copyData is 1 (the default) the variable data is copied as well. If
        copyData is 0, the result transient variable shares the original transient
        variables data array.</p>
      </td>
    </tr>

    <tr>
      <td>Transient Variable</td>

      <td><pre style="word-break:normal;">crossSectionRegrid(newLevel, newLatitude, method="log", missing=None, order=None)</pre></td>

      <td>
        <p>Return a lat/level vertical cross-section regridded to a new set of latitudes
        newLatitude and levels newLevel. The variable should be a function of latitude,
        level, and (optionally) time.</p>

        <p><code>newLevel</code> is an axis of the result pressure levels.</p>

        <p><code>newLatitude</code> is an axis of the result latitudes.</p>

        <p><code>method</code> is optional, either "log" to interpolate in the log of
        pressure (default), or "linear" for linear interpolation.</p>

        <p><code>missing</code> is a missing data value. The default is
        <code>var.getMissing()</code></p>

        <p><code>order</code> is an order string such as "tzy" or "zy". The default is
        <code>var.getOrder()</code>.</p>

        <p><i>See also:</i> <code>regrid</code>, <code>pressureRegrid</code>.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getAxis(n)</code></td>

      <td>
        <p>Get the n-th axis.</p>

        <p><code>n</code> is an integer.</p>
      </td>
    </tr>

    <tr>
      <td>List</td>

      <td><code>getAxisIds()</code></td>

      <td>Get a list of axis identifiers.</td>
    </tr>

    <tr>
      <td>Integer</td>

      <td><code>getAxisIndex(axis_spec)</code></td>

      <td>
        <p>Return the index of the axis specificed by axis_spec. Return -1 if no
        match.</p>

        <p><code>axis_spec</code> is a specification as defined for getAxisList</p>
      </td>
    </tr>

    <tr>
      <td>List</td>

      <td><code>getAxisList(axes=None, omit=None, order=None)</code></td>

      <td>
        <p>Get an ordered list of axis objects in the domain of the variable.</p>

        <p>If <code>axes</code> is not <code>None</code>, include only certain axes.
        Otherwise axes is a list of specifications as described below. Axes are returned
        in the order specified unless the order keyword is given.</p>

        <p>If <code>omit</code> is not <code>None</code>, omit those specified by an
        integer dimension number. Otherwise omit is a list of specifications as described
        below.</p>

        <p><code>order</code> is an optional string determining the output order.</p>

        <p>Specifications for the axes or omit keywords are a list, each element having
        one of the following forms:</p>

        <ul>
          <li>an integer dimension index, starting at 0.</li>

          <li>a string representing an axis id or one of the strings 'time', 'latitude',
          'lat', 'longitude', 'lon', 'lev' or 'level'.</li>

          <li>a function that takes an axis as an argument and returns a value. If the
          value returned is true, the axis matches.</li>

          <li>an axis object; will match if it is the same object as axis.</li>
        </ul>

        <p><code>order</code> can be a string containing the characters t,x,y,z, or -. If
        a dash ('-') is given, any elements of the result not chosen otherwise are filled
        in from left to right with remaining candidates.</p>
      </td>
    </tr>

    <tr>
      <td>List</td>

      <td><code>getAxisListIndex(axes=None, omit=None, order=None)</code></td>

      <td>Return a list of indices of axis objects. Arguments are as for
      getAxisList.</td>
    </tr>

    <tr>
      <td>List</td>

      <td><code>getDomain()</code></td>

      <td>Get the domain. Each element of the list is itself a tuple of the form
      <code>(axis,start,length,true_length)</code> where axis is an axis object, start is
      the start index of the domain relative to the axis object, length is the length of
      the axis, and true_length is the actual number of (defined) points in the domain.
      <i>See also:</i> <code>getAxisList</code>.</td>
    </tr>

    <tr>
      <td>Horizontal-Grid</td>

      <td><code>getGrid()</code></td>

      <td>Return the associated grid, or <code>None</code> if the variable is not
      gridded.</td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getLatitude()</code></td>

      <td>Get the latitude axis, or <code>None</code> if not found.</td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getLevel()</code></td>

      <td>Get the vertical level axis, or <code>None</code> if not found.</td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getLongitude()</code></td>

      <td>Get the longitude axis, or <code>None</code> if not found.</td>
    </tr>

    <tr>
      <td>Various</td>

      <td><code>getMissing()</code></td>

      <td>Get the missing data value, or <code>None</code> if not found.</td>
    </tr>

    <tr>
      <td>String</td>

      <td><code>getOrder()</code></td>

      <td>
        <p>Get the order string of a spatio-temporal variable. The order string specifies
        the physical ordering of the data. It is a string of characters with length equal
        to the rank of the variable, indicating the order of the variable's time, level,
        latitude, and/or longitude axes. Each character is one of:</p>

        <ul>
          <li>'t': time</li>

          <li>'z': vertical level</li>

          <li>'y': latitude</li>

          <li>'x': longitude</li>

          <li>'-': the axis is not spatio-temporal.</li>
        </ul>

        <p><b>Example:</b></p>

        <p>A variable with ordering "tzyx" is 4-dimensional, where the ordering of axes
        is (time, level, latitude, longitude).</p>

        <p><b>Note:</b> The order string is of the form required for the order argument
        of a regridder function.</p>
      </td>
    </tr>

    <tr>
      <td>List</td>

      <td><code>getPaths(*intervals)</code></td>

      <td>
        <p>Get the file paths associated with the index region specified by
        intervals.</p>

        <p><code>intervals</code> is a list of scalars, 2-tuples representing [i,j),
        slices, and/or Ellipses. If no <code>argument(s)</code> are present, all file
        paths associated with the variable are returned.</p>

        <p>Returns a list of tuples of the form (path,slicetuple), where path is the path
        of a file, and slicetuple is itself a tuple of slices, of the same length as the
        rank of the variable, representing the portion of the variable in the file
        corresponding to intervals.</p>

        <p><b>Note:</b> This function is not defined for transient variables.</p>
      </td>
    </tr>

    <tr>
      <td>Axis</td>

      <td><code>getTime()</code></td>

      <td>Get the time axis, or <code>None</code> if not found.</td>
    </tr>

    <tr>
      <td>Integer</td>

      <td><code>len(var)</code></td>

      <td>
        <p>The length of the first dimension of the variable. If the variable is
        zero-dimensional (scalar), a length of 0 is returned.</p>

        <p><b>Note:</b> <code>size()</code> returns the total number of elements.</p>
      </td>
    </tr>

    <tr>
      <td>Transient Variable</td>

      <td><code>pressureRegrid (newLevel, method="log", missing=None,
      order=None)</code></td>

      <td>
        <p>Return the variable regridded to a new set of pressure levels newLevel. The
        variable must be a function of latitude, longitude, pressure level, and
        (optionally) time.</p>

        <p><code>newLevel</code> is an axis of the result pressure levels.</p>

        <p><code>method</code> is optional, either "log" to interpolate in the log of
        pressure (default), or "linear" for linear interpolation.</p>

        <p><code>missing</code> is a missing data value. The default is
        <code>var.getMissing()</code></p>

        <p><code>order</code> is an order string such as "tzyx" or "zyx". The default is
        <code>var.getOrder()</code></p>

        <p>See also: <code>regrid</code>, <code>crossSectionRegrid</code>.</p>
      </td>
    </tr>

    <tr>
      <td>Integer</td>

      <td><code>rank()</code></td>

      <td>The number of dimensions of the variable.</td>
    </tr>

    <tr>
      <td>Transient</td>

      <td>
        <pre style="word-break:normal;">
regrid (togrid, missing=None, order=None, Variable mask=None)
</pre>
      </td>

      <td>
        <p>Return the variable regridded to the horizontal grid togrid.</p>

        <p><code>missing</code> is a Float specifying the missing data value. The default
        is 1.0e20.</p>

        <p><code>order</code> is a string indicating the order of dimensions of the
        array. It has the form returned from <code>variable.getOrder()</code>. For
        example, the string "tzyx" indicates that the dimension order of array is (time,
        level, latitude, longitude). If unspecified, the function assumes that the last
        two dimensions of array match the input grid.</p>

        <p><code>mask</code> is a Numeric array, of datatype Integer or Float, consisting
        of ones and zeros. A value of 0 or 0.0 indicates that the corresponding data
        value is to be ignored for purposes of regridding. If mask is two-dimensional of
        the same shape as the input grid, it overrides the mask of the input grid. If the
        mask has more than two dimensions, it must have the same shape as array. In this
        case, the missing data value is also ignored. Such an n-dimensional mask is
        useful if the pattern of missing data varies with level (e.g., ocean data) or
        time. Note: If neither missing or mask is set, the default mask is obtained from
        the mask of the array if any.</p>

        <p>See also: <code>crossSectionRegrid</code>, <code>pressureRegrid</code>.</p>
      </td>
    </tr>

    <tr>
      <td><code>None</code></td>

      <td><code>setAxis(n, axis)</code></td>

      <td>Set the n-th axis (0-origin index) of to a copy of axis.</td>
    </tr>

    <tr>
      <td><code>None</code></td>

      <td><code>setAxisList(axislist)</code></td>

      <td>Set all axes of the variable. axislist is a list of axis objects.</td>
    </tr>

    <tr>
      <td><code>None</code></td>

      <td><code>setMissing(value)</code></td>

      <td>Set the missing value.</td>
    </tr>

    <tr>
      <td>Integer</td>

      <td><code>size()</code></td>

      <td>Number of elements of the variable.</td>
    </tr>

    <tr>
      <td>Variable</td>

      <td>
        <pre style="word-break:normal;">
subRegion(*region, time=None, level=None, latitude=None, longitude=None, squeeze=0, raw=0)
</pre>
      </td>

      <td>
        <p>Read a coordinate region of data, returning a transient variable. A region is
        a hyperrectangle in coordinate space.</p>

        <p><code>region</code> is an argument list, each item of which specifies an
        interval of a coordinate axis. The intervals are listed in the order of the
        variable axes. If trailing dimensions are omitted, all values of those dimensions
        are retrieved. If an axis is circular (axis.isCircular() is true) or cycle is
        specified (see below), then data will be read with wraparound in that dimension.
        Only one axis may be read with wraparound. A coordinate interval has one of the
        forms listed in Table 2.37 on page 102. Also see
        <code>axis.mapIntervalExt</code>.</p>

        <p>The optional keyword arguments <code>time</code>, <code>level</code>,
        <code>latitude</code>, and <code>longitude</code> may also be used to specify the
        dimension for which the interval applies. This is particularly useful if the
        order of dimensions is not known in advance. An exception is raised if a keyword
        argument conflicts with a positional region argument.</p>

        <p>The optional keyword argument <code>squeeze</code> determines whether or not
        the shape of the returned array contains dimensions whose length is 1; by default
        this argument is 0, and such dimensions are not 'squeezed out'.</p>

        <p>The optional keyword argument <code>raw</code> specifies whether the return
        object is a variable or a masked array. By default, a transient variable is
        returned, having the axes and attributes corresponding to2,3 the region read. If
        raw=1, an MA masked array is returned, equivalent to the transient variable
        without the axis and attribute information.</p>
      </td>
    </tr>

    <tr>
      <td>Variable</td>

      <td>
        <pre style="word-break:normal;">
subSlice(*specs, time=None, level=None, latitude=None, longitude=None, squeeze=0, raw=0)
</pre>
      </td>

      <td>
        <p>Read a slice of data, returning a transient variable. This is a functional
        form of the slice operator [] with the squeeze option turned off.</p>

        <p><code>specs</code> is an argument list, each element of which specifies a
        slice of the corresponding dimension. There can be zero or more positional
        arguments, each of the form:</p>

        <ul>
          <li>a single integer n, meaning <code>slice(n, n+1)</code></li>

          <li>an instance of the slice class</li>

          <li>a tuple, which will be used as arguments to create a slice</li>

          <li>':', which means a slice covering that entire dimension</li>

          <li>Ellipsis (...), which means to fill the slice list with ':' leaving only
          enough room at the end for the remaining positional arguments</li>

          <li>a Python slice object, of the form <code>slice(i,j,k)</code></li>
        </ul>

        <p>If there are fewer slices than corresponding dimensions, all values of the
        trailing dimensions are read.</p>

        <p>The keyword arguments are defined as in subRegion.</p>

        <p>There must be no conflict between the positional arguments and the
        keywords.</p>

        <p>In <code>(a)-(c)</code> and (f), negative numbers are treated as offsets from
        the end of that dimension, as in normal Python indexing.</p>
      </td>
    </tr>

    <tr>
      <td>String</td>

      <td><code>typecode()</code></td>

      <td>The Numeric datatype identifier.</td>
    </tr>
  </table>

**Example:** Get a region of data.

Variable ta is a function of (time, latitude, longitude). Read data corresponding to all times, latitudes -45.0 up to but not including+45.0, longitudes 0.0 through and including longitude 180.0:

{% highlight python %}
data = ta.subRegion(':', (-45.0,45.0,'co'), (0.0, 180.0))
{% endhighlight %}

or equivalently:

{% highlight python %}
data = ta.subRegion(latitude=(-45.0,45.0,'co'), longitude=(0.0,
180.0)
{% endhighlight %}

Read all data for March, 1980:

{% highlight python %}
data = ta.subRegion(time=('1980-3','1980-4','co'))
{% endhighlight %}


<a name="table_2.36"></a>

###### Table 2.36 Variable Slice Operators


|Operator|Description|
|---|---|
|`[i]`|The ith element, zero-origin indexing.|
|`[i:j]`|The ith element through, but not including, element j|
|`[i:]`|The ith element through the end|
|`[:j]`|The beginning element through, but not including, element j|
|`[:]`|The entire array|
|`[i:j:k]`|Every kth element|
|`[i:j, m:n]`|Multidimensional slice|
|`[i, ..., m]`|(Ellipsis) All dimensions between those specified.|
|`[-1]`|Negative indices 'wrap around'. -1 is the last element|


<a name="table_2.37"></a>

###### Table 2.37 Index and Coordinate Intervals


|Interval Definition  |Example Interval Definition|Example|
|---|---|---|
|`x`|single point, such that axis[i]==x In general x is a scalar. If the axis is a time axis, x may also be a cdtime relative time type, component time type, or string of the form 'yyyy-mm-dd hh:mi:ss' (where trailing fields of the string may be omitted.|`180.0`<br/>`cdtime.reltime(48,"hour s since 1980-1")`<br/>`'1980-1-3'`|
|`(x,y)`|indices i such that x &le; axis[i] &le; y|`(-180,180)`|
|`(x,y,'co')`|`x ≤ axis[i] < y`. The third item is defined as in mapInterval.|`(-90,90,'cc')`|
|`(x,y,'co',cycle)`|`x ≤ axis[i]< y`, with wraparound <br/> **Note:** It is not necesary to specify the cycle of a circular longitude axis, that is, for which `axis.isCircular()` is true.|`( 180, 180, 'co', 360.0)`|
|`slice(i,j,k)`|slice object, equivalent to i:j:k in a slice operator. Refers to the indices i, i+k, i+2k, ... up to but not including index j. If i is not specified or is None it defaults to 0. If j is not specified or is None it defaults to the length of the axis. The stride k defaults to 1. k may be negative.|`slice(1,10)`<br/>`slice(,,-1)` reverses the direction of the axis.|
|`':'`|all axis values of one dimension|  |
|`Ellipsis`|all values of all intermediate axes| |  


<a name="2.11.1"></a>

##### 2.11.1 Selectors

A selector is a specification of a region of data to be selected from a variable. For example, the statement

{% highlight python %}
x = v(time='1979-1-1', level=(1000.0,100.0))
{% endhighlight %}

means 'select the values of variable v for time '1979-1-1' and levels 1000.0 to 100.0 inclusive, setting x to the result.' Selectors are generally used to represent regions of space and time.

The form for using a selector is

{% highlight python %}
result = v(s)
{% endhighlight %}

where v is a variable and s is the selector. An equivalent form is

{% highlight python %}
result = f('varid', s)
{% endhighlight %}

where f is a file or dataset, and 'varid' is the string ID of a variable.

A selector consists of a list of selector components. For example, the selector

{% highlight python %}
time='1979-1-1', level=(1000.0,100.0)
{% endhighlight %}

has two components: time='1979-1-1', and level=(1000.0,100.0). This illustrates that selector components can be defined with keywords, using the form:

{% highlight python %}
keyword=value
{% endhighlight %}

Note that for the keywords time, level, latitude, and longitude, the selector can be used with any variable. If the corresponding axis is not found, the selector component is ignored. This is very useful for writing general purpose scripts. The required keyword overrides this behavior. These keywords take values that are coordinate ranges or index ranges as defined in Table 2.37 on page 102.

The following keywords are available: Another form of selector components is the positional form, where the component order corresponds to the axis order of a variable. For example:


<a name="table_2.38"></a>

###### Table 2.38 Selector keywords


|Keyword|Description|Value|
|---|---|---|
|`axisid`|Restrict the axis with ID axisid to a value or range of values.|See Table 2.37 on page 102|
|`grid`|Regrid the result to the grid.|Grid object|
|`latitude`|Restrict latitude values to a value or range. Short form: lat|See Table 2.37 on page 102|
|`level`|Restrict vertical levels to a value or range. Short form: lev|See Table 2.37 on page 102|
|`longitude`|Restrict longitude values to a value or range. Short form: lon|See Table 2.37 on page 102|
|`order`|Reorder the result.|Order string, e.g., "tzyx"|
|`raw`|Return a masked array (MA.array) rather than a transient variable.|0: return a transient variable (default); =1: return a masked array.|
|`required`|Require that the axis IDs be present.|List of axis identifiers.|
|`squeeze`|Remove singleton dimensions from the result.|0: leave singleton dimensions (default); 1: remove singleton dimensions.|
|`time`|Restrict time values to a value or range.|See Table 2.37 on page 10|


Another form of selector components is the positional form, where the component
order corresponds to the axis order of a variable. For example:

{% highlight python %}
x9 = hus(('1979-1-1','1979-2-1'),1000.0)
{% endhighlight %}

reads data for the range ('1979-1-1','1979-2-1') of the first axis, and coordinate value 1000.0 of the second axis. Non-keyword arguments of the form(s) listed in Table 2.37 on page 102 are treated as positional. Such selectors are more concise, but not as general or flexible as the other types described in this section.

Selectors are objects in their own right. This means that a selector can be defined and reused, independent of a particular variable. Selectors are constructed using the cdms.selectors.Selector class. The constructor takes an argument list of selector components. For example:

{% highlight python %}
from cdms.selectors import Selector
sel = Selector(time=('1979-1-1','1979-2-1'), level=1000.)
x1 = v1(sel)
x2 = v2(sel)
{% endhighlight %}

For convenience CDMS provides several predefined selectors, which can be used directly or can be combined into more complex selectors. The selectors time, level, latitude, longitude, and required are equivalent to their keyword counterparts. For example:

{% highlight python %}
from cdms import time, level
x = hus(time('1979-1-1','1979-2-1'), level(1000.))
{% endhighlight %}

and

{% highlight python %}
x = hus(time=('1979-1-1','1979-2-1'), level=1000.)
{% endhighlight %}

are equivalent. Additionally, the predefined selectors `latitudeslice`, `longitudeslice`, `levelslice`, and `timeslice` take arguments `(startindex, stopindex[, stride])`:

{% highlight python %}
from cdms import timeslice, levelslice
x = v(timeslice(0,2), levelslice(16,17))
{% endhighlight %}

Finally, a collection of selectors is defined in module cdutil.region:

{% highlight python %}
from cdutil.region import *
NH=NorthernHemisphere=domain(latitude=(0.,90.)
SH=SouthernHemisphere=domain(latitude=(-90.,0.))
Tropics=domain(latitude=(-23.4,23.4))
NPZ=AZ=ArcticZone=domain(latitude=(66.6,90.))
SPZ=AAZ=AntarcticZone=domain(latitude=(-90.,-66.6))
{% endhighlight %}

Selectors can be combined using the &amp; operator, or by refining them in the call:

{% highlight python %}
from cdms.selectors import Selector
from cdms import level
sel2 = Selector(time=('1979-1-1','1979-2-1'))
sel3 = sel2 & level(1000.0)
x1 = hus(sel3)
x2 = hus(sel2, level=1000.0)
{% endhighlight %}
 

<a name="2.11.2"></a>

##### 2.11.2 Selector examples

CDMS provides a variety of ways to select or slice data. In the following examples, variable hus is contained in file sample.nc, and is a function of (time, level, latitude, longitude). Time values are monthly starting at 1979-1-1. There are 17 levels, the last level being 1000.0. The name of the vertical level axis is 'plev'. All the examples select the first two times and the last level. The last two examples remove the singleton level dimension from the result array.

{% highlight python %}
import cdms
f = cdms.open('sample.nc')
hus = f.variables['hus']

# Keyword selection
x = hus(time=('1979-1-1','1979-2-1'), level=1000.)

# Interval indicator (see mapIntervalExt)
x = hus(time=('1979-1-1','1979-3-1','co'), level=1000.)

# Axis ID (plev) as a keyword
x = hus(time=('1979-1-1','1979-2-1'), plev=1000.)

# Positional
x9 = hus(('1979-1-1','1979-2-1'),1000.0)

# Predefined selectors
from cdms import time, level
x = hus(time('1979-1-1','1979-2-1'), level(1000.))

from cdms import timeslice, levelslice
x = hus(timeslice(0,2), levelslice(16,17))

# Call file as a function
x = f('hus', time=('1979-1-1','1979-2-1'), level=1000.)

# Python slices
x = hus(time=slice(0,2), level=slice(16,17))

# Selector objects
from cdms.selectors import Selector
sel = Selector(time=('1979-1-1','1979-2-1'), level=1000.)
x = hus(sel)

sel2 = Selector(time=('1979-1-1','1979-2-1'))
sel3 = sel2 & level(1000.0)
x = hus(sel3)
x = hus(sel2, level=1000.0)

# Squeeze singleton dimension (level)
x = hus[0:2,16]
x = hus(time=('1979-1-1','1979-2-1'), level=1000., squeeze=1)

f.close()
{% endhighlight %}

<a name="2.12"></a>

#### 2.12 Examples

<a name="2.12.1"></a>

##### 2.12.1 Example 1

In this example, two datasets are opened, containing surface air temperature ('tas') and upper-air temperature ('ta') respectively. Surface air temperature is a function of (time, latitude, longitude). Upper-air temperature is a function of (time, level, latitude, longitude). Time is assumed to have a relative representation in the datasets (e.g., with units 'months since basetime').

Data is extracted from both datasets for January of the first input year through December of the second input year. For each time and level, three quantities are calculated: slope, variance, and correlation. The results are written to a netCDF file. For brevity, the functions `corrCoefSlope` and `removeSeasonalCycle` are omitted.

{% highlight python %}
1.  import cdms
    import MV

    # Calculate variance, slope, and correlation of    
    # surface air temperature with upper air temperature
    # by level, and save to a netCDF file. 'pathTa' is the location of
    # the file containing 'ta', 'pathTas' is the file with contains 'tas'.
    # Data is extracted from January of year1 through December of year2.
    def ccSlopeVarianceBySeasonFiltNet(pathTa,pathTas,month1,month2):

        # Open the files for ta and tas
        fta = cdms.open(pathTa)
        ftas = cdms.open(pathTas)

2.      #Get upper air temperature
        taObj = fta['ta']
        levs = taObj.getLevel()

        #Get the surface temperature for the closed interval [time1,time2]
        tas = ftas('tas', time=(month1,month2,'cc'))

        # Allocate result arrays
        newaxes = taObj.getAxisList(omit='time')
        newshape = tuple([len(a) for a in newaxes])
        cc = MV.zeros(newshape, typecode=MV.Float, axes=newaxes, id='correlation')
        b = MV.zeros(newshape, typecode=MV.Float, axes=newaxes, id='slope')
        v = MV.zeros(newshape, typecode=MV.Float, axes=newaxes, id='variance')

        # Remove seasonal cycle from surface air temperature
        tas = removeSeasonalCycle(tas)

        # For each level of air temperature, remove seasonal cycle
        # from upper air temperature, and calculate statistics
5.      for ilev in range(len(levs)):

            ta = taObj(time=(month1,month2,'cc'), \
                       level=slice(ilev, ilev+1), squeeze=1)
            ta = removeSeasonalCycle(ta)   
            cc[ilev], b[ilev] = corrCoefSlope(tas ,ta)
            v[ilev] = MV.sum( ta**2 )/(1.0*ta.shape[0])

        # Write slope, correlation, and variance variables
6.      f = cdms.open('CC_B_V_ALL.nc','w')
        f.title = filtered
        f.write(b)
        f.write(cc)
        f.write(v)
        f.close()

7.  if __name__=='__main__':
        pathTa = '/pcmdi/cdms/sample/ccmSample_ta.xml'
        pathTas = '/pcmdi/cdms/sample/ccmSample_tas.xml'  
        # Process Jan80 through Dec81
        ccSlopeVarianceBySeasonFiltNet(pathTa,pathTas,'80-1','81-12')
{% endhighlight %}

**Notes:**

  1. Two modules are imported, `cdms`, and `MV`. `MV` implements arithmetic functions.
  2.  `taObj` is a file (persistent) variable. At this point, no data has actually been read. This happens when the file variable is sliced, or when the subRegion function is called. levs is an axis.
  3.  Calling the file like a function reads data for the given variable and time range. Note that month1 and month2 are time strings.
  4. In contrast to `taObj`, the variables `cc`, `b`, and `v` are transient variables, not associated with a file. The assigned names are used when the variables are written.
  5.  Another way to read data is to call the variable as a function. The squeeze option removes singleton axes, in this case the level axis.
  6.  Write the data. Axis information is written automatically.
  7.  This is the main routine of the script. `pathTa` and `pathTas` pathnames. Data is processed from January 1980 through December 1981. 


<a name="2.12.2"></a>

##### 2.12.2 Example 2

In the next example, the pointwise variance of a variable over time is calculated, for all times in a dataset. The name of the dataset and variable are entered, then the variance is calculated and plotted via the vcs module.

{% highlight python %}
        #!/usr/bin/env python
        #
        # Calculates gridpoint total variance
        # from an array of interest
        #

        import cdms
        from MV import *

        # Wait for return in an interactive window

        def pause():
            print Hit return to continue: ,
            line = sys.stdin.readline()

1.      # Calculate pointwise variance of variable over time
        # Returns the variance and the number of points
        # for which the data is defined, for each grid point
        def calcVar(x):
            # Check that the first axis is a time axis
            firstaxis = x.getAxis(0)
            if not firstaxis.isTime():
                raise 'First axis is not time, variable:', x.id
            
            n = count(x,0)
            sumxx = sum(x*x)
            sumx = sum(x)
            variance = (n*sumxx -(sumx * sumx))/(n * (n-1.))

            return variance, n

        if __name__=='__main__':
            import vcs, sys

            print 'Enter dataset path [/pcmdi/cdms/obs/erbs_mo.xml]: ',
            path = string.strip(sys.stdin.readline())
            if path=='': path='/pcmdi/cdms/obs/erbs_mo.xml'

2.          # Open the dataset
            dataset = cdms.open(path)

            # Select a variable from the dataset
            print 'Variables in file:',path
            varnames = dataset.variables.keys()
            varnames.sort()
            for varname in varnames:

                var = dataset.variables[varname]
                if hasattr(var,'long_name'):
                    long_name = var.long_name
                elif hasattr(var,'title'):
                    long_name = var.title
                else:
                    long_name = '?'

            print '%-10s: %s'%(varname,long_name)
            print 'Select a variable: ',
3.          varname = string.strip(sys.stdin.readline())
            var = dataset(varname)
            dataset.close()

            # Calculate variance, count, and set attributes
            variance,n = calcVar(var)
            variance.id = 'variance_%s'%var.id
            n.id = 'count_%s'%var.id
            if hasattr(var,'units'):
                variance.units = '(%s)^2'%var.units
        
            # Plot variance
            w=vcs.init()
4.          w.plot(variance)
            pause()
            w.clear()
            w.plot(n)
            pause()
            w.clear()
{% endhighlight %}

The result of running this script is as follows:

{% highlight pycon %}
% calcVar.py
Enter dataset path [/pcmdi/cdms/sample/obs/erbs_mo.xml]:

Variables in file: /pcmdi/cdms/sample/obs/erbs_mo.xml
albt    : Albedo TOA [%]
albtcs : Albedo TOA clear sky [%]
rlcrft  : LW Cloud Radiation Forcing TOA [W/m^2]
rlut    : LW radiation TOA (OLR) [W/m^2]
rlutcs : LW radiation upward TOA clear sky [W/m^2]
rscrft : SW Cloud Radiation Forcing TOA [W/m^2]
rsdt    : SW radiation downward TOA [W/m^2]
rsut    : SW radiation upward TOA [W/m^2]
rsutcs : SW radiation upward TOA clear sky [W/m^2]
Select a variable: albt

<The variance is plotted>

Hit return to continue:

<The number of points is plotted>
{% endhighlight %}

**Notes:**

  1.  n = count(x, 0) returns the pointwise number of valid values, summing across axis 0, the first axis. count is an MV function. 
  2. dataset is a Dataset or CdmsFile object, depending on whether a .xml or .nc pathname is entered. dataset.variables is a dictionary mapping variable name to file variable.
  3. var is a transient variable.
  4. Plot the variance and count variables. Spatial longitude and latitude information are carried with the computations, so the continents are plotted correctly. 



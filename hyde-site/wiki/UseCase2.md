##Use-case 2
###High res, parallel, time average

**Use Case**: High spatial resolution, parallel, time average    
**Actor**: Climate/Data Scientist    
**Use Scenario**: A user requests a data set be averaged across a number of time steps.

* More than one processor is used to iterate through 3D time steps, run a filter on each, and render a 3D image.
* The data should be high resolution, ie. 1/10-degree global ocean (3600x2400x42).
* The data should be structured, ie. Rectilinear grid.
* The data for each time step should be divided spatially and distributed across more than one processor.
* The operation should return a single time step of the same spatial resolution as the time series that contains the positional temporal average.
  * For example 3 time steps = {1,2,3}, {1,2,6}, {7,8,9}
  * Return value is {3, 4, 6}

**Alternative Paths**:    
**Exceptional Cases**:    
**Frequence**: Medium    
**Criticality**: High    
**Risk**: High    

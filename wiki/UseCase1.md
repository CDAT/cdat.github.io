##Use-case 1: High res, parallel, image sequence
**Use Case**: High spatial resolution, parallel, image sequence production    
**Actor**: Climate/Data Scientist    
**Use Scenario**: The user chooses to produce an image sequence by producing one picture per time step. More than one processor is used to iterate through 3D time steps, run a filter on each, and render a 3D image.

* The data should be high resolution, ie. 1/10-degree global ocean (3600x2400x42).
* The data should be structured, ie. Rectilinear grid.
* The data for each time step should be divided spatially and distributed across more than one processor.
* The data should have a filter, run in parallel, which produces geometry, which is then rendered and composited to produce a single image.

**Alternative Paths**:    
**Exceptional Cases**:    
**Frequency**: High    
**Criticality**: High    
**Risk**: High    
**3/13/2011**: Andy Bauer has successfully run a proof of concept on use-case 1 using VTK and reading, extracting surface, and rendering 360, 1.4 GB files, across 4 processor groups (operating on 4 time steps simultaneously) using 40 cores to operate on each time step. This took less than 3.5 minutes.  Our user was taking more than an hour to do a similar pipeline.

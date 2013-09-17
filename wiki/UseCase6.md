##Use case 6
###Convert from hybrid to std pressure levels

**Use Case**: Convert from hybrid to std pressure levels    
**Actor**: Climate/Data Scientist    
**Background**: models are usually not stored on pressure levels (there are 17 standard pressure level in AR4) on some sort of hybrid level coordinate system. In order to easily compare between model they are usually interpolated back to standard pressure level.    
**Difficulties**: Be careful not to interpolate below ground (pressure asked for is less than Ps)    
**Alternative Paths**: Different sigma coordinate systems    
**Exceptional Cases**:

1. identify file(s) covering period to convert
2. compute "pressure" field over time covered   
typically you will need the (1d, 30 levels) hybrid coefficient from the model and the surface pressure (2d lat/lon):    
compute P = B*Ps + A*P0
3. for each output level to a linear/log interpolation from pressure field to actual output pressure (mask out bellow ground)
4. dump out result

**Frequency**: Medium    
**Criticality**: Medium    
**Risk**: Medium    

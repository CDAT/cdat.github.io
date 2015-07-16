##Use case 7
###Compute a time series

**Use Case**: Compute a time series    
**Actor**: Climate/Data Scientist    
**Details**: A lot can be told by simply averaging a region together (el nino, global ,Northern hemisphere) this is typically a drop in dimensionality.  Read a spatial region and return a single point.    
**Use Scenario**:

1. identify need file(s) to cover time period
2. identify non-time dimensions
3. average over non-time dims, be careful if user want to average, them in specific order or all at once (get different results if missing values)
4. dump out result

**Difficulties**: order of averaging does matter when missing values, keeps weights around between each round    
**Alternative Path**: single location, difference between 2 location (North Atlantic Oscillation, etc...)     
**Exceptional Cases**:    
**Frequency**: Medium    
**Criticality**: Medium     
**Risk**: Medium     

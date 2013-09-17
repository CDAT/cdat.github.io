##Use case 4
###Compute multi-model ensemble mean

**Use Case**: average multi-model ensemble time steps    
**Actor**: Climate/Data Scientist    
**Background**: This is basically the same problem as case 3 but each member is on a different grid. Once we averaged over all realization and got an idea of what "each" model does. It is useful to compute the mean model, that gives an idea of what "models" think.
**Use Scenario**: User has coinciding time steps from a variety of models, run with the same starting conditions.  For each time step, an average of the ensemble of data sets should be calculated, which requires regridding and/or registration of the data sets.

1. identify all models for this ensemble
2. identify common time between each runs
3. identify a target grid to which all model will be regridded
4. average ensemble members over common time and on common grid
5. dump out result

**Difficulties**: 

* Identify files to use.
* Identify which time period each member covers and decide what to do if not common across members.
* Pay attention to missing values.
* Decide on a regridding method and a target grid that make sense.

**Alternative Paths**: Calculate the median as it is usually preferred to the mean model (eliminates out-layers).    
**Exceptional Cases**: The XML are not present then "generate them" (makes more sense) or "do w/o them".    
**Frequency**: Medium    
**Criticalityv: Medium    
**Risk**: Medium    

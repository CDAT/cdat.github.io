##Use case 5
###Compute departures from a climatological DJF

**Use Case**: Compute departures from a climatological DJF    
**Actor**: Climate/Data Scientist    
**Background**: Scientist like to focus on  seasons (DJF, MAM, JJA, SON), or annual cycle (average of each month). They also like to see which seasons/month/years stand out. They do that by removing the "climatological" season from each individual season    
**Use Scenario**:

1. identify file(s) covering the time period to compute climatology over
2. compute climatological annual cycle over period of reference (climatology is defined usually has a 30 years average)
average DJF over the period of reference
WARNING  DJF is TRICKY for example the first DJF only has 2 months, the last one  only has 1 month. Rules need to be put in place to decide how to weight  these cases! WARNIG 2: Time bounds MATTER, for dataset expressed in  "months since" Jan and February have the same length (1 month), but for  dataset expressed in "days since" Jan has a length of 31 whereas Feb has  a length of 28 (and even 29 every 4th years) once each DJF has been  computed, average them all together, that our climatological DJF
3. identify file(s) covering departures to be computed
can be longer than ref period
4. compute seasonal means
Repeat the first part of the process for computing the climatology, obtaining the "Seasons"
5. remove climatology from #4
6. dump out result

**Difficulties**: 

* Time bounds matter!
* Missing values!

**Alternative Paths**: annual cycle instead of DJF    
**Exceptional Cases**:    
**Frequency**: Medium    
**Criticality**: Medium    
**Risk**: Medium    

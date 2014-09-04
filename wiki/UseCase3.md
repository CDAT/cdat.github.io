##Use Case 3
###Compute ensemble mean

**Use Case**: Compute ensemble mean    
**Actor**: Climate/Data Scientist    
**Background**: Usually for each experiment the modeling groups will produce multiple "realization" of the same experiment. Averaging over all these realizations helps removing the "natural" noise (due to the chaotic nature of the system). Therefore giving us a good idea of what the model really does. Typically for AR4 there were at most 10 such realizations per experiment, there will likely be more int he future.    
**Use Scenario**: 

1. identify all runs for the ensemble and the files for each run.
An example AR4 ncar-ccsm3 model in the box below.  The one CDAT would actually use is highlighted, these xml files are recognized by CDAT and have aggregation of all the .nc files.   So in this case we would need to open these 9 files.
2. identify common time between each runs
In this case all realization cover the same 1870 thru 1999 period. But we cannot assume this. In the case they do not cover the same periods, a decision needs to be made: Compute over the commno period only, or compute over the "union" of times and weight each time according to the number of models.
3. average ensemble members over common time
in this case basically for each time step add all 9 realization together
WARNING: We HAVE TO be carefull about missing values, for 3D fields some "bellow ground" values might be masked. These will be different for each time step and each model. That means we cannot assume the sum will be divided by 9 at the end!!!
4. dump out result: array or to file (in case memory is not big enough)

**Difficulties**:

* Identify files to use
* Identify which time period each member covers and decide what to do if not common across members
* Pay attention to missing values

**Alternative Paths**: Compute percentiles (median or 10 percentile for example) instead of mean.    
**Exceptional Cases**: The xml are not present then "generate them" (makes more sense) or "do w/o them"     
**Frequency**: Medium    
**Criticality**: Medium    
**Risk**: Medium    

    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1870-01_cat_1879-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1880-01_cat_1889-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1890-01_cat_1899-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1900-01_cat_1909-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1910-01_cat_1919-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1920-01_cat_1929-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1930-01_cat_1939-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1940-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1950-01_cat_1959-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1960-01_cat_1969-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1970-01_cat_1979-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1980-01_cat_1989-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_A1.20C3M_1.CCSM.atmm.1990-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run1/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run2/ta_A1.20C3M_2.CCSM.atmm.1870-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run2/ta_A1.20C3M_2.CCSM.atmm.1950-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run2/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1870-01_cat_1889-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1890-01_cat_1899-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1900-01_cat_1909-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1910-01_cat_1919-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1920-01_cat_1929-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1930-01_cat_1939-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1940-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1950-01_cat_1959-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1960-01_cat_1969-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1970-01_cat_1979-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1980-01_cat_1989-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_A1.20C3M_3.CCSM.atmm.1990-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run3/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run4/ta_A1.20C3M_4.CCSM.atmm.1870-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run4/ta_A1.20C3M_4.CCSM.atmm.1950-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run4/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1870-01_cat_1879-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1880-01_cat_1889-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1890-01_cat_1899-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1900-01_cat_1909-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1910-01_cat_1919-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1920-01_cat_1929-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1930-01_cat_1939-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1940-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1950-01_cat_1959-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1960-01_cat_1969-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1970-01_cat_1979-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1980-01_cat_1989-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_A1.20C3M_5.CCSM.atmm.1990-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run5/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run6/ta_A1.20C3M_6.CCSM.atmm.1870-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run6/ta_A1.20C3M_6.CCSM.atmm.1950-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run6/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run7/ta_A1.20C3M_7.CCSM.atmm.1870-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run7/ta_A1.20C3M_7.CCSM.atmm.1950-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run7/ta_ncar_ccsm3_0.xml
    20c3m/atm/mo/ta/ncar_ccsm3_0/run9/ta_A1.20C3M_9.CCSM.atmm.1870-01_cat_1949-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run9/ta_A1.20C3M_9.CCSM.atmm.1950-01_cat_1999-12.nc
    20c3m/atm/mo/ta/ncar_ccsm3_0/run9/ta_ncar_ccsm3_0.xml

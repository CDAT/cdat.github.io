##Uses Cases For Parallelizing

###Use Case 3: Compute ensemble mean

* Details: Usually for each experiment the modeling groups will produce multiple "realization" of the same experiment. Averaging over all these realizations helps removing the "natural" noise (due to the chaotic nature of the system). Therefore giving us a good idea of what the model really does. Typically for AR4 there were at most 10 such realization per experiment. But I think they expect more this time around
* Sticky Points:
  * Identify files to use
  * identify which time period each member covers and decide what to do if not common across members
  * pay attention to missing values
* Possible Variation:
  * Compute percentiles (median or 10 percentile for example) instead of mean.
* Steps:

1. identify all runs for this ensemble and the files for each run, example AR4 ncar-ccsm3 model:

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

  * I highlighted the one CDAT would actually use, these xml files are recognized by CDAT has an aggregation of all the .nc files.
  * So in this case we would need to open these 9 files. One could conceive that the xml are not present though. Therefore we need to decide  if we want to "generate them" (makes more sense) or "do w/o them"
2. identify common time between each runs In this case all realization cover the same 1870 thru 1999 period. But we cannot assume this. In the case they do not cover the same periods, a decision needs to be made: Compute over the commno period only, or compute over the "union" of times and weight each time according to the number of models.
3. average ensemble members over common time in this case basically for each time step add all 9 realization together
WARNING: We HAVE TO be carefull about missing values, for 3D fields some "bellow ground" values might be masked. These will be different for each time step and each model. That means we cannot assume the sum will be divided by 9 at the end!!!
4. dump out result: array or to file (in case memory is not big enough)

###Use case 4: Compute multi-model ensemble mean (kind of a super case 1)

* **Details:** This is basically the same problem as case 1 but each member is on a different grid. Once we averaged over all realization and got an idea of what "each" model does. It is useful to compute the mean model, that gives an idea of what "models" think
* Sticky points:
  * see case 1
  * decide on a regridding method and a target grid that make sense.
* Possible variation:
) In this case the median is usually preferred to the mean model (eliminates out-layers)
* Steps:

1. identify all models for this ensemble
2. identify common time between each runs
3. identify a target grid to which all model will be regridded
4. average ensemble members over common time and on common grid
5. dump out result

###Use case 5: Compute departures from a climatological DJF

* **Details**: Scientist like to focus on  seasons (DJF, MAM, JJA, SON), or annual cycle (average of each month). They also like to see which seasons/month/years stand out. They do that by removing the "climatological" season from each individual season
* Sticky points:
  * Time bounds matter!
  * Missing values!
* Possible variations:
  * annual cycle instead of DJF
* Steps:

1. identify file(s) covering the time period to compute climatology over
2. compute climatological annual cycle over period of reference (climatology is defined usually has a 30 years average)
average DJF over the period of reference
WARNING DJF is TRICKY for example the first DJF only has 2 months, the last one only has 1 month. Rules need to be put in place to decide how to weight these cases!
WARNIG 2: Time bounds MATTER, for dataset expressed in "months since" Jan and February have the same length (1 month), but for dataset expressed in "days since" Jan has a length of 31 whereas Feb has a length of 28 (and even 29 every 4th years)
once each DJF has been computed, average them all together, that our climatological DJF
3. identify file(s) covering departures to be computed
can be longer than ref period
4. compute seasonal means
Repeat the first part of the process for computing the climatology, obtaining the "Seasons"
5. remove climatology from step 4
6. dump out result

###Use case 6: Convert from hybrid to std pressure levels

* **Details**: models are usually not stored on pressure levels (there are 17 standard pressure level in AR4) on some sort of hybrid level coordinate system. In order to easily compare between model they are usually interpolated back to standard pressure level.
* Sticky Points:
  * Be careful not to interpolate below ground (pressure asked for is less than Ps)
* Possible variant:
  * Different sigma coordinate systems
* Steps:

1. identify file(s) covering period to convert
2. compute "pressure" field over time covered typically you will need the (1d, 30 levels) hybrid coefficient from the model and the surface pressure (2d lat/lon):
compute P = B*Ps + A*P0
3. for each output level to a linear/log interpolation from pressure field to actual output pressure (mask out bellow ground)
4. dump out result

###Use case 7: Compute a time series

* **Details**: A lot can be told by simply averaging a region together (el nino, global ,Northern hemisphere)
* Sticky points:
 * order of averaging does matter when missing values, keeps weights around between each round
* Possible Variation:
  * single location, difference between 2 location (North Atlantic Oscillation, etc...)
* Steps:

1. identify need file(s) to cover time period
2. identify non-time dimensions
3. average over non-time dims, be careful if user want to average, them in specific order or all at once (get different results if missing values)
4. dump out result

####Use case 8: Computing a zonal mean

* **Details** :most fileds have a strong latitudinal component and it can be easier to look at them once it has been zonally averaged.
* Sticky points:
  * Pretty straight forward
* Possible variation:
  * Use level instead of longitude average
* Steps:

1. identify need file(s) to cover time period
2. identify "zonal" dimension (longitude)
3. average over "zonal" dim
4. dump out result

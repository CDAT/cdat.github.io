##UVCDAT News

####2013-04-05 - Paraview's Spatio-Temporal Analysis Tools on Titan
This is part of the work that Kitware has done for the UV-CDAT project. The concept of spatio-temporal parallelism is to partition the work with respect to both spatial and temporal dimensions. This helps reduce both interprocess communication and file IO contention for fast processing of temporal data sets for large amounts of time steps.    
The installation on Titan includes pre-built Python scripts that do image outputs and temporal statistics for both the MOC and MHT computation. The Python scripts are located at /lustre/widow2/proj/paraview/POPSpatioTemporalScripts. These should not need to be modified. I've also included batch submission scripts to help in running jobs. These will need to be modified for the location of the input POP raw data files as well as the output files (directions are included in each batch submission script).

---

**Edit conflict** - other version:

* Additionally, other Python scripts can easily be generated. See the   UV-CDAT STP Wiki document for more information on that.[Paraview STP Page](https://docs.google.com/a/kitware.com/document/d/1KE-yu9NnhcrR6YI6HxLTsysscxCfXXoa1yyZmY0It-0/edit?usp=drive_web)

---

**Edit conflict** - your version:

* Additionally, other Python scripts can easily be generated. See the UV-CDAT STP Wiki document for more information on that. [UV-CDAT STP Page](https://docs.google.com/a/kitware.com/document/d/1KE-yu9NnhcrR6YI6HxLTsysscxCfXXoa1yyZmY0It-0/edit?usp=drive_web)

---

**End of edit conflict**


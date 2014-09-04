##UV-CDAT Variables

This page describes the Variable Module to be used by different workflows in UV-CDAT.    
A Variable is a handler to data.    
A Variable has a name.    
A Variable requires the following information:    

* reader (Dave Koop mentioned that a Variable could have a reader as an input port, it will be used to read the data)
  * [DAK] We could also pass a Variable to a reader; the idea here is that the identification of a variable could be separated from the loading step (which might be tool-dependent).
* filename and name of the variable in the file (local files)
* host, port, user, password (remote files)

Depending on the type of Variable users can also say which region of the data they want.  In cdat, you can set a axesArgString, that tells which time frames, longitude and latitude range you want.    
The operation above can be applied on a Variable after it is defined.     

**Question for Berk**: *Does ParaView support region selection?*    

    There are some operations that are commonly applied to a Variable. For example,
    * sum,
    * average,
    * difference (using 2 Variables),
    * zonal average (average along a latitude).

    All these operations will produce another Variable.

**Question for all**: *How these operations will be performed? Immediately or not? For example, if there are multiple operations they could be packaged and sent to be performed somewhere and the results sent downstream*    

    "We have discussed that Variables pointing to data to be read in parallel will be a special case
    and it will be likely implemented using another module like ParallelVariable as it is 
    very different from a regular Variable."

**Question for Berk**: *Can you elaborate on this? When talking to Dave Koop he asked if the Parallel Variables will be used differently.*

    Specifically, I am wondering whether a ParallelVariable
    is a specialization of Variable, or if it must be totally separate.
    if we separate the loading step from the definition of a Variable, 
    can a ParallelVariable simply use a different "loader"?

    It would be good if we could query the Variable source for metadata, 
    so we can list all the variables present in a file (this could 
    probably be done in the configuration GUI)

**Question for Dean**: *Is it possible to load just pieces of data from ESGF or the user always has to download all related files and from there load only the parts it interests him/her?*

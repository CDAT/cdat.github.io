##Vistrails XML Descriptions

These are extra attributes to the xml descriptions that I need them to be added and that were not included:    

**codepath**: it is a reference to the class the generated the description    
Example:    

    <diagnostic 
      author="PCMDI's software team" 
      programminglanguage="Python" 
      type="class" url="http://cdat.sf.net">" 
      version="5.0.0.alpha7" 
      codepath="vcs.Canvas.Canvas"
    >

I also added a **required** attribute to the input elements in `<input> </input>` to specify if an input is required for the method to be executed.     
Example:

    <input>
      <slab1 
        doc="Data at least 1D, last dimension will be plotted"
        instance="cdms2.tvariable.TransientVariable/numpy.core.ma.MaskedArray/numpy.ndarray/list"
        position="0" required="True"
      />
      <slab2 
        doc="Data at least 1D, last dimension will be plotted"
        instance="cdms2.tvariable.TransientVariable/numpy.core.ma.MaskedArray/numpy.ndarray/list"
        position="0" required="False"
      />
    </input>

Also long time ago (I don't know if it is still the case), there are some inputs that are not defined in the xml. For example, the plot method defines only two inputs and some options.     
But when we look at the documentation:     

    plot(array1=None, array2=None, template_name=None, graphics_method=None, graphics_name=None, [key=value [, key=value [, ...]]])

We see that there are extra inputs: template_name, graphics_method and graphics_name not specified in the xml but that need to be added.

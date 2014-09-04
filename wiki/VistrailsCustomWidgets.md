##UV-CDAT Custom Widgets

This page explains how to include a custom widget inside UV-CDAT using VisTrails workflows.    
The idea is to expose some parameters of a workflow that can be configurable on the UV-CDAT Window and display the workflow results on the SpreadSheet.    
We will walk through the process using the "ParaView Simple Plot" widget as an example.    
The ParaView Simple Plot is a simple 2D plot that receives cdat file/variable as an input and uses ParaView to plot it. On the UV-CDAT Window, it displays an interactive widget that allows the users to change the color map. This is how the widget looks in UV-CDAT:    

<img src="http://uvcdat.llnl.gov/media/images/wiki/pv_custom_widget_full.png">    

###Building the workflow
In order to build a workflow suitable to be embedded in the UV-CDAT window, it needs to comply with a few guidelines.    
First you have to name the parameters you want to expose so VisTrails sends them to UV-CDAT Window and get the changes back to the workflow. These are the parameters that the user has control over. In our example, we expose a single parameter of type TransferFunction from vtkScaledTransferFunction module and we named it **colormap**.     

<img src="http://uvcdat.llnl.gov/media/images/wiki/pv_simple_plot_colormap.png">    


To name a parameter, you need to assign an alias to it by clicking on the type of the parameter in the *Set Methods* panel. This will show a dialog similar to the image below asking you for an alias name. Make sure the aliases are unique in a workflow.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/alias_dialog.png">    

Our workflow also contains three other input parameters that instead of being exposed together with the colormap widget, they will be integrated with already existing widgets in UV-CDAT. These input parameters are an input file name, the name of the variable (that will be plotted) and its axes. This will allow for the reuse of input parameters across the widgets. So in our example, we named the input file from the *open* module at the top of the workflow as **filename** , the variable name (the *value* parameter from the *String* module labeled as *varname* displayed on the top left the workflow) as **varname** and the axes parameter from the **Variable** module as **axes**.

<img src="http://uvcdat.llnl.gov/media/images/wiki/pv_simple_plot_workflow.png">    

So when the user selects the filename, the variable name and the dimensions in the variable in UV-CDAT window (see figure below), they will also be sent to the workflow.

<img src="http://uvcdat.llnl.gov/media/images/wiki/uv_cdat_main_window.png">    

As the UVCDAT Window also controls the row and column in the spreadsheet where the plot is sent, your workflow should also include a *CellLocation* module for each cell it contains. Give also aliases to the row and column parameters. In our example they were named **row** and **col** , respectively.    
Now you should tag your workflow in the History View and save it to the plots folder in the cdat package folder. In our case we saved as *paraview.vt* . If you open it in VisTrails, you can see the aliases when you select the corresponding modules:

<img src="http://uvcdat.llnl.gov/media/images/wiki/paraview_vistrail.png">    

###Creating the configuration file
Now that we created the workflow with the aliased parameters and tagged in the history view, we need to create a configuration file so the parameters are correctly integrated to the UV-CDAT Window. For the *ParaView Simple Plot* widget, we create a *paraview_simple.cfg* file with the following contents:


    [global]
    cellnum = 1
    filenum = 1
    varnum = 1
    workflow_tag = Simple Plot
    filetypes = CDAT: cdms, ctl, dic, hdf, nc, xml
    qt_filter = ;;CDAT data (*.cdms *.ctl *.dic *.hdf *.nc *.xml)
    filename_alias1 = filename
    varname_alias1 = varname
    axes_alias1 = axes
    dependencies = edu.utah.sci.vistrails.vtk, edu.utah.sci.eranders.ParaView
    [cell1]
    celltype = PVCell
    row_alias = row
    col_alias = col

The **global** section contains the following parameters:

* [global] section parameters

parameter | description
--- | ---
cellnum | The number of cells in the workflow
filenum | The number of input files required by your workflow
varnum | The number of input variables required by your workflow
workflow_tag | The name you tagged your workflow in the History view
filetypes  | What type of input files your workflow support
qt_filter | File names filter used by PyQt filename dialog
filename_alias1 | The name of the alias for the first input file. If there are two input files, also include a filename_alias2 parameter
varname_alias1 | The name of the alias for the variable name. If there are two variables, also include a varname_alias2 parameter
axes_alias1 | The name of the alias for the axes parameter in variable 1. If there are two variables, also include a axes_alias2 parameter
dependencies | The packages your workflow depend on, besides the cdat package.

For each spreadsheet cell module in the workflow, you will need a **cell<num>** section in the config file with the following parameters:

* [cell<num>] section parameters

parameter | description
--- | ---
celltype | The type of the spreadsheet cell
row_alias | The name of the alias for the row
col_alias | The name of the alias for the column

###Adding to the registry
Now all we have to do is tell VisTrails to load the widget. This is done by editing the **registry.cfg** file in the same directory. We will add a section with the name of the widget and that contains the names of the configuration file and the vistrail file with the workflow. This is the current state of the **registry.cfg** file:

    [Volume Rendering]
    config_file = volume_rendering.cfg
    vt_file = volume_rendering.vt

    [ParaView Simple Plot]
    config_file = paraview_simple.cfg
    vt_file = paraview.vt

###Manipulating the widget
Every time the user hits apply, the provenance of that workflow is kept in the current tree. This is done by copying the original
Simple Plot
workflow to the current vistrail (a node with the name of the widget is created) and children nodes will be created with the parameter changes the user generated by interacting with the UV-CDAT window.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/interaction_tree.png">    

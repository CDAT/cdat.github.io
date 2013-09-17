##VCS Canvas Plot Control

You can control the type of plot via the Plot Tab.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/plottab.png">    

Most plots are VCS plots: Boxfill, Isofill, Isoline, Meshfill, Outfill, Outline, Scatter, Taylordiagram, Vector, XvsY, Xyvsy, Yxvsx        
Once you select a plot    

<img src="http://uvcdat.llnl.gov/media/images/wiki/selectplot.png">    
 
It automatically populates the bottom part with settings specific for this plot, in vcs case, you will see 2 lists: 1 for the templates and one for the type of gm you selected:    

<img src="http://uvcdat.llnl.gov/media/images/wiki/lists.png">    

Clicking on the name of a graphic method or template will update its settings in the bottom part of the screen, if this part is greyed out that means you cannot edit this specific template/gm    

<img src="http://uvcdat.llnl.gov/media/images/wiki/settings2.png">    

The important part to understand is how the GUI decides what to plot where.     
All of this is controlled via the Page Layout Section    

<img src="http://uvcdat.llnl.gov/media/images/wiki/pagelayout.png">    

You can add as many layouts as you want via the add layout button    
A layout consist of a template, a graphic method and a (many) variables to plot      
You can drag and drop a template from the "template list" into the template box of the layout    

<img src="http://uvcdat.llnl.gov/media/images/wiki/templatelist.png">
<img src="http://uvcdat.llnl.gov/media/images/wiki/templatebox.png">        

Same for graphics methods, they can be drag and dropped from the graphics method list into the GM box    

<img src="http://uvcdat.llnl.gov/media/images/wiki/gmlist.png">
<img src="http://uvcdat.llnl.gov/media/images/wiki/gmbox.png">    

Finally variable(s) can also be drag and dropped from the variable list into the corresponding variable box    

<img src="http://uvcdat.llnl.gov/media/images/wiki/variablelist.png">
<img src="http://uvcdat.llnl.gov/media/images/wiki/variablebox.png">    

If any of the template/graphicsmethod/variable box is on the layout is empty , the GUI will use whatever is selected in the corresponding template/gm/variable list box.    
Finally the destination of the plot is controlled via the "Canvas" box    

<img src="http://uvcdat.llnl.gov/media/images/wiki/canvastarget.png">      

Press plot to see the results.    

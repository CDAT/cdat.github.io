##Subsetting Dimensions

Goal: To introduce you to dimension subsetting, node striding, and, reversing.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatdims.png">    

There are three ways to subset a dimension:    
Method 1: Edit the "longitude" dimensions coordinate value entry window. In the window, replace text with -90:90 by 5. Then press the Enter key to register the change.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatlon.png">    

Remember: the text string represents first : last by stride.    
Method 2: Select the arrow button to the right of the "latitude" entry window. Select the -70 value in the item list to get the first or single value. Repeat the process and select 70. This will complete the range for the "latitude" dimension (i.e., "-70 : 70 by 1") . See images below.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatsel1.png">
<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatsel2.png">        
 
Method 3: For the time dimension, move the top slider to "1982-1-1 0:0" to set the first value and the bottom slider to "1984-12-1 0:0" to set the last value. The first values under the sliders represent the first value (i.e., 1982-1-1 0:0) and the second value under the sliders represent the second or last value (i.e., 1984-12-1 0:0). These values are dynamically updated as the sliders move.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatsubtime.png">    

Try Reversing the Dimension Order: To reverse the order of the "longitude" dimension, move the top slider to the right and stop at the value of 175 and the bottom slider to the left and stop at the value of -180 . Notice the change in the values under the sliders.    

<img src="http://uvcdat.llnl.gov/media/images/wiki/vcdatrevertlon.png">    

Plot, you should see:    

<img src="http://uvcdat.llnl.gov/media/images/wiki/lonrevertedplot.png">

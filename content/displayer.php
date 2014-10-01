<?php

isset($_REQUEST['file']) ? $file_name = $_REQUEST['file'] : $file_name = "default";

$image_path     = "media/gallery/fullsize/" . $file_name . ".png";
$thumbnail_path = "media/gallery/thumbnail/" . $file_name . ".png";
$source_path    = "media/gallery/source/" . $file_name . ".py";

if (($source_file = fopen($source_path, "r+")) === FALSE){
  $source = "No Source File Available";
  $show = FALSE;
}  
else{
  while(($buffer = fgets($source_file)) !== FALSE)
	  $source .= $buffer;
  fclose($source_file);
  $show = TRUE;
}


echo "<h2>" . $file_name . "</h2>";
echo "(";
if($show) echo "<a href=\"" . $source_path . "\">Source code</a>, ";
echo "<a href=\"" . $image_path . "\">png</a>)<br/>";
echo "&nbsp;<br/>";
echo "<img src=\"" . $image_path . "\"><br/>";
echo "&nbsp;<br/>";
echo "<pre>" . $source . "</pre>";

?>

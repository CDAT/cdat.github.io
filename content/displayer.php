<?php

isset($_REQUEST['file']) ? $file_name = $_REQUEST['file'] : $file_name = "default";

$image_path     = "media/gallery/fullsize/" . $file_name . ".png";
$thumbnail_path = "media/gallery/thumbnail/" . $file_name . ".png";
$source_path    = "media/gallery/source/" . $file_name . ".py";

if (($source_file = fopen($source_path, "r+")) === FALSE) die("Error opening Source file.");
else{
  while(($buffer = fgets($source_file)) !== FALSE)
	$source .= $buffer;
}
fclose($source_file);

echo "<h2>" . $file_name . "</h2>";
echo "(<a href=\"" . $source_path . "\">Source code</a>, <a href=\"" . $image_path . "\">png</a>)<br/>";
echo "<img src=\"" . $image_path . "\"><br/>";
echo "<pre>" . $source . "</pre>";

?>

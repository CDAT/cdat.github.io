<?php

function get_projections($projection) {
  include_once("projection_classifier.php");
  $projection = strtolower($projection);
  return filter_files("has_projection", $projection);
}

function get_graphics_methods($method) {
	include_once("gm_classifier.php");
	$method = strtolower($method);
	return filter_files("has_gm", $method);
}

function get_all() {
	return filter_files(TRUE, TRUE);
}

function filter_files($filter, $type) {
  $files = array();
  foreach (scandir("media/gallery/source") as $sourcefile) {

  	// Check if we have permissions to read the file
  	if (is_readable("media/gallery/source/$sourcefile") === FALSE) {
  		continue;
  	}

  	// Check if the file is a hidden file
    if (strpos($sourcefile, ".") === 0) {
        continue;
    }

    // Check if the file is a python file
	$pathinfo = pathinfo($sourcefile);
	if ($pathinfo["extension"] !== "py") {
		continue;
	}

	// Load the file
    $file = file_get_contents("media/gallery/source/$sourcefile");

    // Using $filter, remove unwanted files
    if ($filter === TRUE || $filter($file, $type)) {
    	$filename = $pathinfo["filename"];
		$files[] = "$filename.png";
    }
    
  }
  return $files;
} 
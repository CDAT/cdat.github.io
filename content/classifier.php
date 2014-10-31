<?php

function get_projections($projection, $files = NULL) {
  include_once("projection_classifier.php");
  $projection = strtolower($projection);
  return filter_files("has_projection", $projection, $files);
}

function get_graphics_methods($method, $files = NULL) {
  include_once("gm_classifier.php");
  $method = strtolower($method);
  return filter_files("has_gm", $method, $files);
}

function get_templates($templates, $files=NULL) {
  include_once("template_classifier.php");
  $template = strtolower($templates);
  return filter_files("has_template", $template, $files);
}

function get_all() {
  return filter_files(TRUE, TRUE, NULL);
}

function filter_files($filter, $type, $sourcefiles) {
  if ($sourcefiles === NULL) {
    $sourcefiles = scandir("media/gallery/source");
  }

  // print "$type: <pre>" . var_export($sourcefiles, TRUE) . "</pre>";
  $files = array();
  foreach ($sourcefiles as $sourcefile) {
    if (substr($sourcefile, -3) !== ".py") {
      $sourcefile = "$sourcefile.py";
    }
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
      $files[] = $filename;
    }

  }
  return $files;
} 

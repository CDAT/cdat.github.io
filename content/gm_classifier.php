<?php

function clean_gm($gm) {
  $parts = explode("_", $gm);
  $cleaned = array();
  foreach ($parts as $part) {
    if ($part == "3d") {
      $part = "3D";
    } else {
      $part = ucfirst($part);
    }
    $cleaned[] = $part;
  }

  return implode(" ", $cleaned);
}

function all_gms() {

	return array(
		"boxfill",
		"continents",
		"isofill",
		"isoline",
		"outfill",
		"outline",
		"scatter",
		"vector",
		"xvsy",
		"xyvsy",
		"yxvsx",
		"template",
    "3d_scalar",
    "3d_vector",
    "text",
    "marker",
  );
}

function has_gm($file, $method) {

  $methods = all_gms();
	if (!in_array($method, $methods)) {
		return FALSE;
	}
  
  $gm_re = "/(get|create)$method/";
  // 0 or FALSE is a failure, so we can do single =
  return preg_match($gm_re, $file) != FALSE; 
}

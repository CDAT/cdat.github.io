<?php

function has_gm($file, $method) {
	$methods = array(
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
	);

	if (!in_array($method, $methods)) {
		return FALSE;
	}
  
  $gm_re = "/(get|create)$method/";
  // 0 or FALSE is a failure, so we can do single =
  return preg_match($gm_re, $file) != FALSE; 
}

<?php
function clean_primitive($prim) {
  $parts = explode("_", $prim);
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

function all_primitives() {
    return array(
      "text",
      "marker",
    );
}

function has_primitive($file, $primitive) {
  $primitives = all_primitives();
  if (!in_array($primitive, $primitives)) {
    return FALSE;
  }

  $prim_re = "/(get|create)$primitive/";
  // 0 or FALSE is a failure, so we can do single =
  return preg_match($prim_re, $file) != FALSE; 
}
<?php

function clean_gm($gm) {
  $gm = strtolower($gm);
  $clean = array(
    "1d" => "One Dimension",
    "oned" => "One Dimension",
    'xvsy' => 'X vs Y',
    'xyvsy' => 'XY vs Y',
    'yxvsx' => 'YX vs X',
  );

  if (isset($clean[$gm])) {
    return $clean[$gm];
  }

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
    "meshfill",
    "1d",
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

  if ($method == "1d") {
    $method = "1d|oneD";
  }
  $gm_re = "/(get|create)$method/";
  // 0 or FALSE is a failure, so we can do single =
  return preg_match($gm_re, $file) != FALSE; 
}

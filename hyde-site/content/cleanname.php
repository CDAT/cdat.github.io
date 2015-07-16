<?php
function cleanName($filename){

  if (strpos($filename, "test_vcs_basic_") === 0) {
    return cleanTestVCSBasic($filename);
  }
  
  if( strpos($filename, "test_") === 0 ) {
    $filename = substr($filename, strlen("test_"), strlen($filename));
  }

  $cleanname = str_replace('_', ' ', $filename);

  $cleanname = clean_common_parts($cleanname);

  return $cleanname;
}

function clean_common_parts($name) {
  $parts = explode(" ", $name);

  $common = array(
    "vcs" => "VCS",
    "1d" => "1D",
    "3d" => "3D",
    "vcs3d" => "VCS 3D",
    "eztemplate" => "EzTemplate",
    "legd" => "Legend",
    "glb" => "Global",
  );

  $clean = array();
  foreach ($parts as $part) {
    $part = strtolower($part);
    if (isset($common[$part])) {
      $clean[] = $common[$part];
    } else {
      $clean[] = ucfirst($part);
    }
  }

  return implode(" ", $clean);
}

function cleanTestVCSBasic($filename) {
    include_once("projection_classifier.php");
    $projections = all_projections();

    $name = "VCS Basic ";
    $rest = substr($filename, strlen("test_vcs_basic_"));
    $pathinfo = pathinfo($rest);
    $rest = $pathinfo["filename"];
    $parts = explode("_", $rest);
    
    include_once("gm_classifier.php");
    $name .= clean_gm(array_shift($parts)); # graph type

    $capitalized = array(
      "aeqd" => "AEQD",
      "proj" => "Projection",
      "SH" => "Southern Hemisphere",
      "NH" => "Northern Hemisphere",
      "masked" => "Masked",
      "zero" => "Zeroed",
      "gm" => FALSE,
      "via" => "via GM",
      "gmflip" => "GM&mdash;Flipped"
    );

    $cleaned = array();
    foreach ($parts as $part) {
      if (is_numeric($part)) {
        if (isset($projections[(int)$part])) {
          $part = $projections[(int)$part];
          $part = clean_projection($part);
          $cleaned[] = $part;
          continue;
        }
      }
      if (isset($capitalized[$part])) {
        $new = $capitalized[$part];
        if ($new == FALSE) {
          continue;
        }

        if ($new == "Projection") {
          $previous = array_pop($cleaned);
          if ($previous !== NULL) {
            $new = "$previous $new";
          }
        }

        $cleaned[] = $new;
      } else {
        $cleaned[] = ucfirst($part);
      }
    }

    if ($cleaned) {

      $name .= "<br/>(" . implode(", ", $cleaned) . ")";
    }

    return $name;
}
?>

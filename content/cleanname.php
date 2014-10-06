<?php
function cleanName($filename){

  if (strpos($filename, "test_vcs_basic_") === 0) {
    return cleanTestVCSBasic($filename);
  }
  
  if( substr($filename, 0 , 5) === "test_" ) {
    $filename = substr($filename, 5, strlen($filename));
  }

  $cleanname = str_replace('_', ' ', $filename);

  return $cleanname;
}

function cleanTestVCSBasic($filename) {
    $name = "VCS Basic ";
    $rest = substr($filename, strlen("test_vcs_basic_"));
    $pathinfo = pathinfo($rest);
    $rest = $pathinfo["filename"];
    $parts = explode("_", $rest);

    $name .= ucfirst(array_shift($parts)); # graph type

    $capitalized = array(
      "aeqd" => "AEQD",
      "proj" => "Projection",
      "SH" => "Southern Hemisphere",
      "NH" => "Northern Hemisphere",
      "masked" => "Masked",
      "zero" => "Zeroed",
      "gm" => FALSE,
      "via" => "via GM",
      "gmflip" => "GM&emdash;Flipped"
    );

    $cleaned = array();
    foreach ($parts as $part) {
      if (isset($capitalized[$part])) {
        $new = $capitalized[$part];
        if ($new == FALSE) {
          continue;
        }
        $cleaned[] = $new;
      } else {
        $cleaned[] = ucfirst($part);
      }
    }

    if ($cleaned) {
      $name .= " (" . implode(", ", $cleaned) . ")";
    }

    return $name;
}
?>

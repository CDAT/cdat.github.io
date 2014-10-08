<?php
function cleanName($filename){

  if (strpos($filename, "test_vcs_basic_") === 0) {
    return cleanTestVCSBasic($filename);
  }
  
  if( strpos($filename, "test_") === 0 ) {
    $filename = substr($filename, strlen("test_"), strlen($filename));
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
      "gmflip" => "GM&mdash;Flipped"
    );

    $cleaned = array();
    foreach ($parts as $part) {
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

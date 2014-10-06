<?php
function cleanName($filename){

  if( substr($filename, 0 , 5) === "test_" )
    $filename = substr($filename, 5, strlen($filename));

  $cleanname = str_replace('_', ' ', $filename);
  return $cleanname;
}
?>

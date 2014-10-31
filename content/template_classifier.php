<?php

function clean_template($template) {
  $template = strtolower($template);
  $clean = array(
    "eztemplate" => "EzTemplate",
  );

  if (isset($clean[$template])) {
    return $clean[$template];
  }

  $parts = explode("_", $template);
  $cleaned = array();
  foreach ($parts as $part) {
    $part = ucfirst($part);
    $cleaned[] = $part;
  }

  return implode(" ", $cleaned);
}

function all_templates() {

  return array(
    "eztemplate",
  );
}

function has_template($file, $template) {
  $templates = all_templates();
  
  if (in_array($template, $templates) === FALSE) {
    return FALSE;
  }

  return strpos($file, clean_template($template)) !== FALSE;
}

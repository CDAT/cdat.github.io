<?php include_once("cleanname.php") ?>

<?php
error_reporting(E_ERROR | E_PARSE);

isset($_REQUEST['file']) ? $file_name = $_REQUEST['file'] : $file_name = "default";

$image_path     = "media/gallery/fullsize/" . $file_name . ".png";
$thumbnail_path = "media/gallery/thumbnail/" . $file_name . ".png";
$source_path    = "media/gallery/source/" . $file_name . ".py";

$other_path     = "media/gallery/other";

$others = array();

foreach (scandir($other_path) as $other) {
  if (strpos($other, $file_name) === 0) {
    // Create a list of associated files
    $others[] = $other_path . "/" . $other;
  }
}

$source = file_get_contents($source_path);

if ($source === FALSE) {
  $source = "No Source File Available";
  $show = FALSE;
} else {
  $show = TRUE;
}

?>
  <h2><?php echo cleanName($file_name); ?></h2>
  <p>
    (<a href="<?php echo $image_path; ?>">png</a>)
    <?php foreach ($others as $filepath): ?>
    (<a href="<?php echo $filepath; ?>"><?php
      $parts = explode(".", $filepath);
      $last_part = array_pop($parts);
      echo $last_part;
      if ($last_part == "nc") {
        $has_datafile = TRUE;
      }
    ?></a>)
    <?php endforeach; ?>
    <?php if ($show): ?>
    <a href="<?php echo $source_path; ?>">Source</a>
    <?php endif; ?>
  </p>
  <p><img src="<?php echo $image_path; ?>" /></p>
  <?php if ($has_datafile): ?>
  <div class="alert alert-warning">
    This script requires data sets linked above (<b>nc</b> files) in order to run.
  </div>
  <?php endif; ?>
  <pre><?php echo $source; ?></pre>

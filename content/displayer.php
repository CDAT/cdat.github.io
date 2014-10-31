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
  $file_info = pathinfo($other);
  if ($file_info["filename"] === $file_name) {
    $others[$file_info["extension"]] = $other_path . "/$other";
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
    <?php foreach ($others as $extension=>$filepath): ?>
    (<a href="<?php echo $filepath; ?>"><?php echo $extension; ?></a>)
    <?php endforeach; ?>
    <?php if ($show): ?>
    <a href="<?php echo $source_path; ?>">Source</a>
    <?php endif; ?>
  </p>
  <p><img src="<?php echo $image_path; ?>" /></p>
  <pre><?php echo $source; ?></pre>

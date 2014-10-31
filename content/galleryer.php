<?php 
  include_once("cleanname.php");
  include_once("classifier.php");
?>
<style>
.example {
  float:left;
  height:350px;
  width:350px;
  word-break:normal;
  margin:10px;
}

.img_wrapper {
  height: 250px;
  width: 300px;
  
  margin-left:auto;
  margin-right:auto;

  text-align: center;

  margin-bottom:10px;
  /* image centering magic */
  font: 0/0 a;
}

/* magic to vertically center image */
.img_wrapper:before {
  content: ' ';
  display:inline-block;
  vertical-align: middle;
  height:100%;
}

.example img {
  display:inline-block;
  vertical-align: middle;
}

.example a {
  display:block;
}

.example p {
  padding-left:5px;
  padding-right:5px;
  text-align:center;
}
</style>


<?php

$files = NULL;
$classifications = array();
if (isset($_REQUEST["graphics_method"])) {
  $files = get_graphics_methods($_REQUEST["graphics_method"], $files);
  $classifications[] = htmlentities(clean_gm($_REQUEST["graphics_method"])) . " graphics method";
}

if (isset($_REQUEST["primitive"])) {
  $files = get_primitives($_REQUEST["primitive"], $files);
  $classifications[] = htmlentities(clean_primitive($_REQUEST["primitive"])) . " primitive";
}

if (isset($_REQUEST["projection"])) {
  $files = get_projections($_REQUEST["projection"], $files);
  $classifications[] = htmlentities(clean_projection($_REQUEST["projection"])) . " projection";
}

if (isset($_REQUEST["template"])) {
  $files = get_templates($_REQUEST["template"], $files);
  $classifications[] = htmlentities(clean_template($_REQUEST["template"])) . " template";
}

if ($files === NULL) {
  $classification = "All Examples";
  $files = get_all();
}

?>
  <h4>
<?php
if ($classifications) {
  echo "Examples using the ";
  while ($class = array_shift($classifications)) {
    echo "$class";
    switch (count($classifications)) {
      case 0:
        echo ":";
        break;
      case 1:
        echo " and ";
        break;
      default:
        echo ", ";
    }
  }
} else {
  echo "All Examples";
}
?>
</h4>

<!-- the filter bar -->
<?php include "filters.php"; ?>

<?php
foreach ($files as $file):
?>

<div class="example">
	<a href="display.php?file=<?php print $file; ?>">
    <div class="img_wrapper">
        <img src="media/gallery/thumbnails/<?php print $file; ?>.png" />
    </div>
    <p><?php print cleanName($file); ?></p>
	</a>
</div>

<?php endforeach; ?>

<?php if (count($files) == 0): ?>
  <h4>No examples match selected filters</h4>
<?php endif; ?>

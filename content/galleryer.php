<?php 
  include_once("cleanname.php");
  include_once("classifier.php");
?>
<style>
.example {
  float:left;
  height:275px;
  width:350px;
  word-break:normal;
  border:1px solid #CCC;
  
  margin:10px;
}

.img_wrapper {
  height: 190px;
  width: 190px;
  
  margin-left:auto;
  margin-right:auto;

  text-align: center;

  margin-bottom:10px;
  /* image centering magic */
  font: 0/0 a;
}

/* magic to veritcally center image */
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

if (isset($_REQUEST["graphics_method"])) {
  $files = get_graphics_methods($_REQUEST["graphics_method"]);
  $classification = "Examples using the " . htmlentities($_REQUEST["graphics_method"]) . " graphics method";
} elseif (isset($_REQUEST["projection"])) {
  $files = get_projections($_REQUEST["projection"]);
  $classification = "Examples using the " . htmlentities($_REQUEST["projection"]) . " projection";
} else {
  $classification = "All Examples";
  $files = get_all();
}

?>
<h4><?php echo $classification; ?>:</h4>

<?php
foreach ($files as $file):
  $name = substr($file, 0 , -4);
?>

<div class="example">
	<a href="display.php?file=<?php print $name; ?>">
    <div class="img_wrapper">
        <img src="media/gallery/thumbnails/<?php print $file; ?>" />
    </div>
    <p><?php print cleanName($name); ?></p>
	</a>
</div>

<?php endforeach; ?>

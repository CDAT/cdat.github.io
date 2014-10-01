<style>
.example {
  float:left;
  height:250px;
  width:375px;
  word-break:normal;
}

</style>
<?php

$dir = "media/gallery/thumbnails";
foreach (scandir($dir) as $file):
  if (strpos($file, ".") === 0) {
    continue;
  }
  $name = substr($file, 0 , -4);
?>

<div class="example">
	<a href="display.php?file=<?php print $name; ?>">
	<img src="media/gallery/thumbnails/<?php print $file; ?>" />
	<p><?php print $name; ?></p>
	</a>
</div>

<?php endforeach; ?>

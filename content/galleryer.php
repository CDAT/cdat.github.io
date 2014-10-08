<?php include_once("cleanname.php") ?>
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

  font: 0/0 a;
}

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

$dir = "media/gallery/thumbnails";
foreach (scandir($dir) as $file):
  if (strpos($file, ".") === 0) {
    continue;
  }
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

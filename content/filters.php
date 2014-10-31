<style>
  .filter {
    width:50%;
    box-sizing:border-box;
    -moz-box-sizing:border-box;
    border:1px solid #CCC;
    border-radius:5px;
    margin:1%;
  }

  .filter_body > ul > li {
    list-style-type:none; 
    margin-left:-25px;
  }

  .filter_sign  {
    width:25px;
    text-align:center;
    display:inline-block;
  }

  .filter_body {
    margin:0;
  }

  .filter_header {
    padding:10px;
    font-size:1.2em;
  }

  .filter_body.in {
    border-top:1px solid #CCC;
  }

  .filter .filter{
    width:48%;
    float:left;
  }

  .filter .filter .filter_header {
    font-size:1em;
  }

  .filter .filter:nth-child(odd) {
    margin-right:1%;
  }
  .filter .filter:nth-child(even) {
    margin-left:1%;
  }

</style>
<?php
  function build_url($arg, $value) {
    $our_args = array(
      "graphics_method" => @$_REQUEST["graphics_method"],
      "projection" => @$_REQUEST["projection"],
      "template" => @$_REQUEST["template"],
    );

    if ($our_args[$arg] == $value) {
      unset($our_args[$arg]);
    } else { 
      $our_args[$arg] = $value;
    }

    return "gallery.php?" . http_build_query($our_args);
  }



  if (isset($_REQUEST["graphics_method"])) {
    $gm = $_REQUEST["graphics_method"];
  } else {
    $gm = NULL;
  }
  if (isset($_REQUEST["projection"])) {
    $proj = $_REQUEST["projection"];
  } else {
    $proj = NULL;
  }
  if (isset($_REQUEST["template"])) {
    $temp = $_REQUEST["template"];
  } else {
    $temp = NULL;
  }

  // Build a filter accordion
  function make_filter($type, $label, $options, $value, $url_arg, $cleaner) {
    ?>
      <div class="filter" id="<?php echo $type; ?>">
        <div class="filter_group">
          <div class="filter_header">
            <a class="filter_toggle" data-toggle="collapse" data-parent="#gm" href="#collapse_<?php echo $type; ?>">
              <?php echo $label; ?>
            </a>
          </div>
          <div class="filter_body collapse <?php if ($value !== NULL) { echo "in"; } ?>" id="collapse_<?php echo $type; ?>">
            <ul>
              <?php foreach ($options as $option): ?>
                <li>
                  <div class='filter_sign'>
                    <i class='<?php if ($value === $option) { echo 'icon-minus-sign'; } else { echo 'icon-plus-sign'; } ?>'></i>
                  </div>
                  <a href="<?php echo build_url($url_arg, $option); ?>"><?php echo $cleaner($option); ?></a>
                </li>
              <?php endforeach; ?>
            </ul>
          </div>
        </div>
      </div>
    <?php
  }
?>
<!-- all filters accordion -->
<div class="filter" id="filter_grouper">
  <div class="filter_group">
    <div class='filter_header'>
      <a class="filter_toggle" data-toggle="collapse" data-parent="#filter_grouper" href="#collapse_filters">
        Filters
      </a>
      <?php if ($gm != NULL || $proj != NULL || $temp != NULL): ?>
        <small class="pull-right"><a href="gallery.php">(Remove Filters)</a></small>
      <?php endif; ?>
    </div>
    <div class="filter_body collapse <?php if ($gm !== NULL || $proj !== NULL || $temp !== NULL) { echo "in"; } ?>" id="collapse_filters">
      <?php
        include_once("gm_classifier.php");
        make_filter("gm", "Graphics Method", all_gms(), $gm, "graphics_method", "clean_gm");
        
        include_once("projection_classifier.php");
        make_filter("projection", "Projection", all_projections(), $proj, "projection", "clean_projection");

        include_once("template_classifier.php");
        make_filter("template", "Template", all_templates(), $temp, "template", "clean_template");
      ?>
    </div>
  </div>
</div>
  <script>
  $("body").ready(function(){
    // Add disclosure arrows to the filter accordion items
    $(".filter_header>a").prepend($(document.createElement("i")).addClass("icon-chevron-right").addClass("toggle_arrow")).click(function(){
      var arrow = $(this).find(".toggle_arrow");
      arrow.toggleClass("icon-chevron-right").toggleClass("icon-chevron-down");
    });

    $(".toggle_arrow").each(function(ind, el) {
      var $this = $(el);
      var body = $this.parent().parent().parent().find(".filter_body");
      if (body.hasClass("in")) {
        $this.toggleClass("icon-chevron-right").toggleClass("icon-chevron-down");
      } 
    });
  });
  </script>

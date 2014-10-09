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
?>
<div class="filter" id="filter_grouper">
  <div class="filter_group">
    <div class='filter_header'>
      <a class="filter_toggle" data-toggle="collapse" data-parent="#filter_grouper" href="#collapse_filters">
        Filters
      </a>
      <?php if ($gm != NULL || $proj != NULL): ?>
        <small class="pull-right"><a href="gallery.php">(Remove Filters)</a></small>
      <?php endif; ?>
    </div>
    <div class="filter_body collapse <?php if ($gm !== NULL || $proj !== NULL) { echo "in"; } ?>" id="collapse_filters">
      <div class="filters">
        <div class="filter" id="gm">
          <div class="filter_group">
            <div class="filter_header">
              <a class="filter_toggle" data-toggle="collapse" data-parent="#gm" href="#collapse_gm">
                Graphics Methods
              </a>
            </div>
            <div class="filter_body collapse <?php if ($gm !== NULL) { echo "in"; } ?>" id="collapse_gm">
            <ul>
              <?php include_once("gm_classifier.php"); ?>
              <?php foreach (all_gms() as $method): ?>
                <li><div class='filter_sign'><i class='<?php if ($gm === $method) { echo 'icon-minus-sign'; } else { echo 'icon-plus-sign'; } ?>'></i></div><a href="<?php echo build_url("graphics_method", $method); ?>"><?php echo clean_gm($method); ?></a></li>
              <?php endforeach; ?>
            </ul>
          </div>
          </div>
        </div>
      </div>
      <div class="filter" id="projection">
          <div class="filter_group">
            <div class="filter_header">
              <a class="filter_toggle" data-toggle="collapse" data-parent="#projection" href="#collapse_projection">
                Projection
              </a>
            </div>
            <div class="filter_body collapse <?php if ($proj !== NULL) { echo "in"; } ?>" id="collapse_projection">
              <ul>
                  <?php include_once("projection_classifier.php"); ?>
                  <?php foreach (all_projections() as $projection): ?>
                    <li><div class='filter_sign'><i class='<?php if ($proj === $projection) { echo 'icon-minus-sign'; } else { echo 'icon-plus-sign'; } ?>'></i></div><a  href="<?php echo build_url("projection", $projection); ?>"><?php echo clean_projection($projection); ?></a></li>
                  <?php endforeach; ?>
              </ul>
            </div>
          </div>
        </div>
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

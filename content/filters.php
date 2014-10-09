<style>
  .filter {
    width:50%;
    box-sizing:border-box;
    -moz-box-sizing:border-box;
    border:1px solid #CCC;
    border-radius:5px;
    margin:1%;
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

<div class="filter" id="filter_grouper">
  <div class="filter_group">
    <div class='filter_header'>
      <a class="filter_toggle" data-toggle="collapse" data-parent="#filter_grouper" href="#collapse_filters">
        Filters
      </a>
      <?php if (@$param_set): ?>
        <small class="pull-right"><a href="gallery.php">(Remove Filters)</a></small>
      <?php endif; ?>
    </div>
    <div class="filter_body collapse" id="collapse_filters">
      <div class="filters">
        <div class="filter" id="gm">
          <div class="filter_group">
            <div class="filter_header">
              <a class="filter_toggle" data-toggle="collapse" data-parent="#gm" href="#collapse_gm">
                Graphics Methods
              </a>
            </div>
            <div class="filter_body collapse" id="collapse_gm">
            <ul>
              <?php include_once("gm_classifier.php"); ?>
              <?php foreach (all_gms() as $method): ?>
                <li><a href="gallery.php?graphics_method=<?php echo urlencode($method); ?>"><?php echo clean_gm($method); ?></a></li>
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
            <div class="filter_body collapse" id="collapse_projection">
              <ul>
                  <?php include_once("projection_classifier.php"); ?>
                  <?php foreach (all_projections() as $projection): ?>
                    <li><a href="gallery.php?projection=<?php echo urlencode($projection); ?>"><?php echo clean_projection($projection); ?></a></li>
                  <?php endforeach; ?>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>

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
              <li><a href="gallery.php?graphics_method=boxfill">Boxfill</a></li>
              <li><a href="gallery.php?graphics_method=continents">Continents</a></li>
              <li><a href="gallery.php?graphics_method=isofill">Isofill</a></li>
              <li><a href="gallery.php?graphics_method=isoline">Isoline</a></li>
              <li><a href="gallery.php?graphics_method=outfill">Outfill</a></li>
              <li><a href="gallery.php?graphics_method=outline">Outline</a></li>
              <li><a href="gallery.php?graphics_method=scatter">Scatter</a></li>
              <li><a href="gallery.php?graphics_method=vector">Vector</a></li>
              <li><a href="gallery.php?graphics_method=xvsy">Xvsy</a></li>
              <li><a href="gallery.php?graphics_method=xyvsy">Xyvsy</a></li>
              <li><a href="gallery.php?graphics_method=yxvsx">Yxvsx</a></li>
              <li><a href="gallery.php?graphics_method=template">Template</a></li>
              <li><a href="gallery.php?graphics_method=3d_scalar">3D Scalar</a></li>
              <li><a href="gallery.php?graphics_method=3d_vector">3D Vector</a></li>
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
              <li><a href="gallery.php?projection=aeqd">AEQD</a></li>
              <li><a href="gallery.php?projection=polar%20(non%20gctp)">Polar (non-GCTP)</a></li>
              <li><a href="gallery.php?projection=mollweide%20(non%20gctp)">Mollweide (non-GCTP)</a></li>
              <li><a href="gallery.php?projection=robinson%20(non%20gctp)">Robinson (non-GCTP)</a></li>
              <li><a href="gallery.php?projection=linear">Linear</a></li>
              <li><a href="gallery.php?projection=utm">UTM</a></li>
              <li><a href="gallery.php?projection=state%20plane">State Plane</a></li>
              <li><a href="gallery.php?projection=albers%20equal area">Albers Equal Area</a></li>
              <li><a href="gallery.php?projection=lambert">Lambert</a></li>
              <li><a href="gallery.php?projection=mercator">Mercator</a></li>
              <li><a href="gallery.php?projection=polar">Polar</a></li>
              <li><a href="gallery.php?projection=polyconic">Polyconic</a></li>
              <li><a href="gallery.php?projection=equid%20conic a">Equid Conic A</a></li>
              <li><a href="gallery.php?projection=transverse%20mercator">Transverse Mercator</a></li>
              <li><a href="gallery.php?projection=stereographic">Stereographic</a></li>
              <li><a href="gallery.php?projection=lambert%20azimuthal">Lambert Azimuthal</a></li>
              <li><a href="gallery.php?projection=azimuthal">Azimuthal</a></li>
              <li><a href="gallery.php?projection=gnomonic">Gnomonic</a></li>
              <li><a href="gallery.php?projection=orthographic">Orthographic</a></li>
              <li><a href="gallery.php?projection=gen.%20vert.%20near%20per">Gen. Vert. Near Per</a></li>
              <li><a href="gallery.php?projection=sinusoidal">Sinusoidal</a></li>
              <li><a href="gallery.php?projection=equirectangular">Equirectangular</a></li>
              <li><a href="gallery.php?projection=miller">Miller</a></li>
              <li><a href="gallery.php?projection=van%20der grinten">Van der Grinten</a></li>
              <li><a href="gallery.php?projection=hotin">Hotin</a></li>
              <li><a href="gallery.php?projection=robinson">Robinson</a></li>
              <li><a href="gallery.php?projection=space%20oblique">Space Oblique</a></li>
              <li><a href="gallery.php?projection=alaska">Alaska</a></li>
              <li><a href="gallery.php?projection=interrupted%20goode">Interrupted Goode</a></li>
              <li><a href="gallery.php?projection=mollweide">Mollweide</a></li>
              <li><a href="gallery.php?projection=interrupted%20mollweide">Interrupted Mollweide</a></li>
              <li><a href="gallery.php?projection=hammer">Hammer</a></li>
              <li><a href="gallery.php?projection=wagner%20iv">Wagner IV</a></li>
              <li><a href="gallery.php?projection=wagner%20vii">Wagner VII</a></li>
              <li><a href="gallery.php?projection=oblated">Oblated</a></li>
            </ul>
          </div>
          </div>
        </div>
      </div>
    </div>
</div>

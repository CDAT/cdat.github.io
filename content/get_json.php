<?php

/* This script acts as a data middleman between the UV-CDAT Usage API and the d3
 * charts.
 *
 * Because of same origin policy
 * (http://en.wikipedia.org/wiki/Same_origin_policy), we can't grab the usage
 * JSON directly using JavaScript; we need to go through a script on our server
 * side first.
 *
 * This script caches fetched data as "<type>.<days>.json", and overwrites cache
 * files when they become out of date.
 *
 * To use this script, call it with the HTTP GET variables `type` and `days`
 * like so:
 *
 *   http://.../get_json.php?type=domain&days=2
 *
 * `days` is optional and defaults to 0 (all data).
 */

/* Number of seconds to allow the use of cached data. Set to 0 to never create
 * cache files. (TODO: Setting to 0 breaks the graph.)
 */
$cache_lifespan = 60 * 60;

$type = $_GET['type'];
if ($type != 'country'  &&
    $type != 'domain'   &&
    $type != 'platform' &&
    $type != 'source'
   ) exit('Bad type.');

$days = $_GET['days'];
if (is_numeric($_GET['days']))
  $days = $_GET['days'];
else
  $days = 0;

$cache_file = "json/$type.$days-day.json";

// Refresh the cache file if it doesn't exist, or if the old one is expired
if (!file_exists($cache_file) || time() - filemtime($cache_file) > $cache_lifespan) {
  $json = `curl http://uv-cdat.llnl.gov/UVCDATUsage/log/json/$type/?days=$days`;
  if ($cache_lifespan != 0) {
    touch($cache_file);
    if (is_writable($cache_file))
      file_put_contents($cache_file, $json);
    else
      exit("<div class='error'>Error: Cache file <tt>$cache_file</tt> not writable.</div>");
  }
  print $json;
} else {
  print file_get_contents($cache_file);
}

?>

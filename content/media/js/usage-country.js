// Where should the JSON for the chart come from?
//var json_url = "get_json.php?type=country&days=0";
var json_url = "http://uvcdat.llnl.gov/UVCDATUsage/log/json/country/?days=0";

// Set dimensions of the chart
var width = 960,
height = 500,
radius = Math.min(width, height) / 2;

// Set colors to use for each slice
var color = d3.scale.ordinal()
.range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

var arc = d3.svg.arc()
.outerRadius(radius - 10)
.innerRadius(0);

var pie = d3.layout.pie()
.sort(null)
.value(function(d) { return d[1]; });

var svg = d3.select("#top").append("svg")
.attr("width", width)
.attr("height", height)
.append("g")
.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// Get JSON (must be a URL on this server -- see "Same origin policy" on Wikipedia)
d3.json(json_url, function(error, data) {

  // We assume the data is contained inside one parent element with some
  // human-readable name. Here we jump inside that parent element.
  data = data.countries;
  // data = data[Object.keys(data)[0]]; // Generic version

  // Force all values to be positive
  data.forEach(function(d) {
    d[1] = +d[1];
  });

  /* Draw stuff */

  var g = svg.selectAll(".arc")
  .data(pie(data))
  .enter().append("g")
  .attr("class", "arc");

  g.append("path")
  .attr("d", arc)
  .style("fill", function(d) { return color(d.data[0]); });

  g.append("text")
  .attr("transform", function(d) {
    var c = arc.centroid(d),
    x = c[0],
    y = c[1],
    // pythagorean theorem for hypotenuse
    h = Math.sqrt(x*x + y*y);
    return "translate(" + (x/h * radius) +  ',' +
      (y/h * radius) +  ")"; 
  })
  .attr("text-anchor", function(d) {
    // are we past the center?
    return (d.endAngle + d.startAngle)/2 > Math.PI ?
      "end" : "start";
  })
  .attr("dy", ".35em")
  .text(function(d) { return d.data[0]; });



});

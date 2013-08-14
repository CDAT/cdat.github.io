// Where should the JSON for the chart come from?
var json_url = "get_json.php?type=domain&days=1";

// Set dimensions of the chart
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width  = 750 - margin.left - margin.right,
    height = 500 - margin.top  - margin.bottom;

var formatPercent = d3.format(".0");

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(formatPercent);

var svg = d3.select("#top").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Get JSON (must be a URL on this server -- see "Same origin policy" on Wikipedia)
d3.json(json_url, function(error, data) {

  // We assume the data is contained inside one parent element with some
  // human-readable name. Here we jump inside that parent element.
  //data = data.domains;
  data = data[Object.keys(data)[0]]; // Generic version

  // Force all values to be positive
  data.forEach(function(d) {
    d[1] = +d[1];
  });

  // Set domains
  x.domain(data.map(function(d) { return d[0]; }));
  y.domain([0, d3.max(data, function(d) { return d[1]; })]);

  // Draw x axis
  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  // Draw y axis
  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Program events logged");

  // Draw bars
  svg.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d[0]); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d[1]); })
      .attr("height", function(d) { return height - y(d[1]); });

});


var margin = { top: 20, right: 30, bottom: 30, left: 20 };
var height = 500 - margin.left - margin.right;
var barWidth = 20;
var flag = 0;

var x = d3.scale.linear().range([0, height]);

var chart = d3.select(".chart")

var allgroup = chart.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var tooltip = chart.append("text")
        .style("visibility", "hidden");

d3.tsv("state_population_gdp.tsv", type, function (error, data) {
        x.domain([0, d3.max(data, function (d) { return d.population; })]);

        // change the width and height to show all the bar
        chart.attr("height", 1500);
        chart.attr("width", margin.top + barWidth * data.length);

        var bar = allgroup.selectAll("g")
                .data(data)
                .enter().append("g")
                // change the position of the bar
                .attr("transform", function (d, i) { return "translate(" + i * barWidth + ", 0)"; });

        // change the width and height of the rect
        bar.append("rect")
                .attr("height", function (d) { return x(d.population); })
                .attr("width", barWidth - 1)

                .attr("y", function (d) { return height - x(d.population); })

                // default color: steelblue
                .attr("fill", "steelblue")

                .on("mouseover", function (d, i) {
                        // change the position of text
                        var myRect = d3.select(this);
                        var tipx = barWidth * i + 15;
                        var tipy = myRect.attr("y") - 20;
                        tooltip.attr("x", tipx);
                        tooltip.attr("y", tipy);
                        tooltip.attr("dx", 35);
                        tooltip.attr("dy", 35);
                        tooltip.style("visibility", "visible");
                        tooltip.style("fill", "black");
                        tooltip.text(d.population);

                        // change color when mouse moving in
                        flag = 1 - flag;
                        myRect.attr("fill", flag ? "darkorange" : "steelblue");
                })
                .on("mouseout", function () {
                        tooltip.style("visibility", "hidden");

                        // change color when mouse moving out
                        var myRect = d3.select(this);
                        flag = 1 - flag;
                        myRect.attr("fill", flag ? "darkorange" : "steelblue");
                });

});

function type(d) {
        d.population = +d.population;
        return d;
}


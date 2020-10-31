var margin = { top: 20, right: 30, bottom: 30, left: 100 };
var svgHeight = 500 - margin.top - margin.bottom;
var svgWidth = 960 - margin.left - margin.right;
var flag = 0;

var xScale = d3.scale.linear().range([0, svgWidth]);
var yScale = d3.scale.linear().range([svgHeight, 0]);
var xAxis = d3.svg.axis();
var yAxis = d3.svg.axis();
var svg = d3.select("svg")
        .attr("width", svgWidth + margin.left + margin.right)
        .attr("height", svgHeight + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
var infoText = svg.append("text")
        .style("visibility", "hidden");

d3.tsv("state_population_gdp.tsv", type, function (error, data) {
        // change domain based on data
        xScale.domain([0, d3.max(data, function (d) { return d.population; })]);
        yScale.domain([0, d3.max(data, function (d) { return d.gdp; })]);

        // add the axis
        xAxis.scale(xScale).orient("bottom");
        svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + svgHeight + ")")
                .call(xAxis);

        yAxis.scale(yScale).orient("left")
        svg.append("g")
                .attr("class", "y axis")
                .attr("transform", "translate(" + 0 + ", 0)")
                .call(yAxis);

        // add axis labels
        svg.append("text")
                .attr("x", svgWidth - 80)
                .attr("y", (svgHeight + margin.bottom - 40))
                .text("population");

        svg.append("text")
                .attr("x", -10)
                .attr("y", 20)
                .attr("transform", "rotate(-90)")
                .text("gdp");

        // add points
        var points = svg.selectAll("circle")
                .data(data)
                .enter();

        points.append("circle")
                .attr("r", 5)
                .attr("cx", function (d) { return xScale(d.population); })
                .attr("cy", function (d) { return yScale(d.gdp); })
                .attr("fill", "steelblue")

                .on("mouseover", function (d, i) {
                        var myCircle = d3.select(this);

                        // show text
                        var textPosX = myCircle.attr('cx');
                        var textPosY = myCircle.attr('cy');
                        infoText.attr('x', textPosX)
                        infoText.attr('y', textPosY)
                        infoText.attr("dx", 35);
                        infoText.attr("dy", 35);
                        infoText.style("visibility", "visible");
                        infoText.style("fill", "black");
                        infoText.text(d.state + ': ' + d.gdp / d.population);

                        // change color when mouse moving in
                        flag = 1 - flag;
                        myCircle.attr("fill", flag ? "darkorange" : "steelblue");
                })

                .on("mouseout", function () {
                        infoText.style("visibility", "hidden");

                        // change color when mouse moving out
                        var myCircle = d3.select(this);
                        flag = 1 - flag;
                        myCircle.attr("fill", flag ? "darkorange" : "steelblue");
                })
                ;


});

function type(d) {
        d.population = +d.population; // coerce to number
        d.gdp = +d.gdp;
        return d;
}
function renderChart(data) {
        var bar = document.getElementById("bar");
        var max = data[0];
        for (var index in data) {
                if (data[index] > max)
                        max = data[index];
        }
        var percent = 300 / max;
        var i = 0;
        var rectWidth = 15;
        var leftMargin = 5;
        var rectMargin = 1;
        var rectMaxHeight = 300;
        var textSize = 5;
        var flag = 0;
        var rectLis = [];
        var textLis = [];

        // console.log(data)
        bar.style.height = rectMaxHeight + "px";

        for (let index = 0; index < data.length; index++) {
                // add rect
                var rect = document.createElement("div");
                rect.id = "rect_" + index;
                rect.style.height = Math.round(percent * data[index]) + "px";
                rect.style.width = rectWidth + "px";
                rect.style.left = (index * rectWidth) + leftMargin + "px";
                rect.style.top = rectMaxHeight - Math.round(percent * data[index]) + "px";
                rect.style.marginLeft = (index * rectMargin) + "px";
                rect.style.position = "absolute";
                rect.style.background = "none repeat scroll 0 0 steelblue";
                rectLis.push(rect);
                bar.appendChild(rect);

                // add text
                var text = document.createElement("div");
                text.id = "text_" + index;
                text.style.height = textSize + "px";
                text.style.left = (index * rectWidth) + leftMargin - textSize * 5 + "px";
                text.style.top = rectMaxHeight - Math.round(percent * data[index]) - textSize * 5 + "px";
                text.style.marginLeft = (index * rectMargin) + "px";
                text.style.position = "absolute";
                text.style.visibility = "hidden";
                text.innerHTML = data[index];
                textLis.push(text);
                bar.appendChild(text);
        }

        // add listener event
        for (let i = 0; i < rectLis.length; i++) {
                rectLis[i].addEventListener("mouseover", function () {
                        flag = 1 - flag;
                        rectLis[i].style.backgroundColor = flag ? "darkorange" : "steelblue";
                        textLis[i].style.visibility = "visible";

                });
                rectLis[i].addEventListener("mouseout", function () {
                        flag = 1 - flag;
                        rectLis[i].style.backgroundColor = flag ? "darkorange" : "steelblue";
                        textLis[i].style.visibility = "hidden";
                });
        }
}

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
                var data = [];
                var lines = xhttp.responseText.trim().split('\r\n');
                for (let i = 1; i < lines.length; i++) {
                        var line = lines[i];
                        var items = line.split("\t");
                        var state = items[0];
                        var population = parseInt(items[1]);
                        var gdp = parseInt(items[2]);
                        data.push(population)
                }
                renderChart(data);
        };
};
xhttp.open("GET", "state_population_gdp.tsv", true);
xhttp.send();
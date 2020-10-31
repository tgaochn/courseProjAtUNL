// define graph template
var cy = cytoscape({
    container: document.querySelector('#cy'),

    boxSelectionEnabled: false,
    autounselectify: true,

    style: cytoscape.stylesheet()
        .selector('node')
        .css({
            'content': 'data(id)',
            'text-valign': 'center',
            'color': 'white',
            'text-outline-width': 2,
            'background-color': '#999',
            'text-outline-color': '#999'
        })
        .selector('edge')
        .css({
            'curve-style': 'bezier',
            'target-arrow-shape': 'triangle',
            'target-arrow-color': '#ccc',
            'line-color': '#ccc',
            'width': 1
        })
        .selector(':selected')
        .css({
            'background-color': 'black',
            'line-color': 'black',
            'target-arrow-color': 'black',
            'source-arrow-color': 'black'
        })
        .selector('.faded')
        .css({
            'opacity': 0.25,
            'text-opacity': 0
        }),

    layout: {
        name: 'grid',
        padding: 10
    }
});

cy.on('tap', 'node', function (e) {
    var node = e.cyTarget;
    var neighborhood = node.neighborhood().add(node);

    cy.elements().addClass('faded');
    neighborhood.removeClass('faded');
});

cy.on('tap', function (e) {
    if (e.cyTarget === cy) {
        cy.elements().removeClass('faded');
    }
});
// graph template end ---------------------------------------

// load data from neo4j
var xmlhttp = new XMLHttpRequest();
var url = "http://localhost:11002/db/data/transaction/commit";
// var statement = "MATCH (n:Person) RETURN n LIMIT 25;";
var statement = "MATCH (n:Person) RETURN n LIMIT 25";

var query_com = {
    "statements": [{
        "statement": statement,
        "resutDataContents": ["graph"]
    }]
};
var query_str = JSON.stringify(query_com);
xmlhttp.open("POST", url, true);
xmlhttp.setRequestHeader("Accept", "application/json; charset=UTF-8");
xmlhttp.setRequestHeader("Content-type", "application/json");
xmlhttp.send(query_str);

xmlhttp.onreadystatechange = function () {
    if (xmlhttp.responseText != "") {
        // console.log(xmlhttp.responseText);
        var json_output = eval("(" + xmlhttp.responseText + ")");
        var results = json_output.results[0].data;
        console.log(json_output.results.data);
        // console.log(json_output.results[0].data);

        // load nodes
        for (let index = 0; index < results.length; index++) {
            const result = results[index].row[0];
            var id = result[0].id;
            var name = result[0].name;
            var state = result[0].state;
            // console.log(id);
            cy.add(
                { group: "nodes", data: { id: id, name: name, state: state } }
            );
            // console.log(id)

            // load edge and the 2nd node if exist
            if (result.length > 1) {
                var id = result[2].id;
                var name = result[2].name;
                var state = result[2].state;
                cy.add(
                    { group: "nodes", data: { id: id, name: name, state: state } }
                );

                meta = json_output.results[0].data[0].meta[0]
                var id = meta[1].id;
                var p1Id = result[0].id;
                var p2Id = result[2].id;
                var year = result[1].year;
                // console.log(p1Id)
                // console.log(p2Id)
                // console.log("=============")

                cy.add(
                    { group: "edges", data: { id: id, source: p1Id, target: p2Id, year: year } }
                );
            }
        }

        // set layout
        var layout = cy.layout({
            name: 'concentric',
            fit: true,
            padding: 30, // the padding on fit
            startAngle: 4 / 2 * Math.PI, // where nodes start in radians
            sweep: undefined, // how many radians should be between the first and last node (defaults to full circle)
            clockwise: true, // whether the layout should go clockwise (true) or counterclockwise/anticlockwise (false)
            equidistant: false, // whether levels have an equal radial distance betwen them, may cause bounding box overflow
            minNodeSpacing: 100 // min spacing between outside of nodes (used for radius adjustment)
        });
        layout.run();

    }
}


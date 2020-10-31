function sentQuery() {
    var start = performance.now();

    // define graph template
    var cy = cytoscape({
        container: document.querySelector('#cy'),

        boxSelectionEnabled: false,
        autounselectify: true,

        style: cytoscape.stylesheet()
            .selector('node')
            .css({
                'content': 'data(name)',
                // 'content': 'data(id)',
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
    // graph template end ---------------------------------------

    // load data from neo4j
    var xmlhttp = new XMLHttpRequest();
    // var url = "http://localhost:11002/db/data/transaction/commit";
    var url = "http://localhost:11006/db/data/transaction/commit";
    // var statement = "MATCH (n:Person) RETURN n LIMIT 25;";
    // var statement = "MATCH q = (p1:Person) - [:Friend] -> (p2:Person) where p1.id = 1 OR p1.id = 2 OR p1.id = 3 RETURN q ;";
    // var statement = "MATCH q = (p1:Person) - [:Friend] -> (p2:Person) where p1.id = 1 OR p1.id = 2 RETURN q ;";
    // var statement = "MATCH q = (p1:Person) - [:Friend] -> (p2:Person) where p1.id = 1 RETURN q ;";
    // var statement = "MATCH q=(p1:Person) - [:Friend] -> (p2:Person)  where p1.state = 'Nebraska'  RETURN q ;";
    var statement = document.getElementById("input").value;

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

            for (let index = 0; index < results.length; index++) {
                const result = results[index].row[0];
                if (result instanceof Array) { // result is a edge
                    // console.log(result);
                    var p1Id = result[0].id;
                    var p1Name = result[0].name;
                    var p1State = result[0].state;
                    var p2Id = result[2].id;
                    var p2Name = result[2].name;
                    var p2State = result[2].state;
                    var year = result[1].year;

                    cy.add([
                        { group: "nodes", data: { id: p1Id, name: p1Name, state: p1State } },
                        { group: "nodes", data: { id: p2Id, name: p2Name, state: p2State } },
                        { group: "edges", data: { source: p1Id, target: p2Id, year: year } }
                    ])
                    // console.log(result, p1Id, p2Id, year)
                }
                else { // result is a node
                    var id = result.id;
                    var name = result.name;
                    var state = result.state;
                    // console.log(id);
                    cy.add(
                        { group: "nodes", data: { id: id, name: name, state: state } }
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

    var end = performance.now();
    var time = end - start;
    document.getElementById("time").innerHTML = "Time: " + time / 1000 + " s";
}

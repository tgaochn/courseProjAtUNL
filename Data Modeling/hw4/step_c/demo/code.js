var cy = cytoscape({
    container: document.querySelector('#cy'),

    boxSelectionEnabled: false,
    autounselectify: true,

    style: cytoscape.stylesheet()
        .selector('node')
        .css({
            'content': 'data(name)',
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

    elements: {
        nodes: [
            { data: { id: 'j', name: 'Jerry' } },
            { data: { id: 'e', name: 'Elaine' } },
            { data: { id: 'k', name: 'Kramer' } },
            { data: { id: 'g', name: 'George' } },
            // { data: { id: 'g1', name: 'George1' } },
            // { data: { id: 'g2', name: 'George2' } }
        ],
        edges: [
            { data: { source: 'j', target: 'e' } },
            { data: { source: 'j', target: 'k' } },
            { data: { source: 'j', target: 'g' } },
            { data: { source: 'e', target: 'j' } },
            { data: { source: 'e', target: 'k' } },
            { data: { source: 'k', target: 'j' } },
            { data: { source: 'k', target: 'e' } },
            { data: { source: 'k', target: 'g' } },
            { data: { source: 'g', target: 'j' } }
        ]
    },

    layout: {
        name: 'grid',
        id: 'grid',
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

cy.add([
    { group: "nodes", data: { id: 'j1', name: 'Jerry1' } },
    // { group: "nodes", data: { id: 'j2', name: 'Jerry2' } },
    // { group: "nodes", data: { id: 'j3', name: 'Jerry3' } },
    // { group: "edges", data: { id: "e0", source: "j1", target: "j2" } }
]);

cy.add([
    { group: "nodes", data: { id: 'j11', name: 'Jerry12' } },
    // { group: "nodes", data: { id: 'j12', name: 'Jerry2' } },
    // { group: "nodes", data: { id: 'j13', name: 'Jerry3' } },
    // { group: "edges", data: { id: "e10", source: "j1", target: "j2" } }
]);

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

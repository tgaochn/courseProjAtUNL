/*
Send query to Neo4j and get the file path.
*/

// function sentQuery() {
//     // load data from neo4j
//     var xmlhttp = new XMLHttpRequest();
//     var url = "http://localhost:11009/db/data/transaction/commit";
//     var statement = "match (n:PointCloud) where n.plantId = '329_6' and n.date = '2018-08-03' return n.filePath"; // TODO: 
//     //var statement = document.getElementById("inputBox").value;

//     var query_com = {
//         "statements": [{
//             "statement": statement,
//             "resutDataContents": ["graph"]
//         }]
//     };
//     var query_str = JSON.stringify(query_com);
//     xmlhttp.open("POST", url, true);
//     xmlhttp.setRequestHeader("Accept", "application/json; charset=UTF-8");
//     xmlhttp.setRequestHeader("Content-type", "application/json");
//     xmlhttp.send(query_str);

//     xmlhttp.onreadystatechange = function () {
//         if (xmlhttp.responseText != "") {
//             var json_output = eval("(" + xmlhttp.responseText + ")");
//             var results = json_output.results[0].data;
//             //var plyPath = results[0].row[0];
//             var plyPath = './data/surface-L2.ply';
//             localStorage.setItem('plyPath', plyPath);
//             window.location.reload();
//         }
//     }
// }


/*
Return file path for demo.
*/
function sentQuery() {
    var statement = document.getElementById("inputBox").value;
    var plyPath;
    if(statement == "1"){
        plyPath = './data/moved_2.ply';
        localStorage.setItem('plyPath', plyPath);
        document.getElementById("inputBox").value = '';
        window.location.reload();
    }else if(statement == "2"){
        plyPath = './data/surface-L2.ply';
        localStorage.setItem('plyPath', plyPath);
        document.getElementById("inputBox").value = '';
        window.location.reload();
    }else if(statement == "3"){
        plyPath = './data/surface-L2-clean_denoise.ply';
        localStorage.setItem('plyPath', plyPath);
        document.getElementById("inputBox").value = '';
        window.location.reload();
    }else{
        window.alert("The data is not ready yet, try '1', '2', '3' to load different models.");
    }
}
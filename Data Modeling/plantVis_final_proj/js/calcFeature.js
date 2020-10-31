function calcSurfaceArea(selectedPointIdLis, plyFileName) {
    var loader = new THREE.PLYLoader();
    loader.load(plyFileName, function (geometry) {
        geometry.computeVertexNormals();

        var material = new THREE.MeshBasicMaterial({ vertexColors: THREE.VertexColors });
        mesh = new THREE.Mesh(geometry, material);
        mesh.position.y = 0.0;
        mesh.position.z = 0.0;
        mesh.rotation.z = -Math.PI / 2;
        mesh.scale.multiplyScalar(0.1);
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        scene.add(mesh);
        
        points = getPoints(scene.children[3].geometry.attributes.position.array);
        faces = getFaces(scene.children[3].geometry.index.array)
        // console.log(points);
        // console.log(faces);

        var p2f = {}; // build the map from point id to related face id
        for (let faceId = 0; faceId < faces.length; faceId++)
        {
            var face = faces[faceId];
            for (let i = 0; i < 3; i++)
            {
                var p = face[i];
                p in p2f || (p2f[p] = []); // p2f.setdefault(p, [])
                p2f[p].push(faceId)
            }
        }
        // console.log(p2f);

        var faceCntLis = [...Array(faces.length)].map(_ => 0); // calc how many points related to each face
        for (let pointId of selectedPointIdLis)
        {
            var faceIdLis = p2f[pointId];
            for (let faceId of faceIdLis)
            {
                faceCntLis[faceId] += 1;
            }
        }
        // console.log(faceCntLis);

        var selectedFaceId = [];
        for (let faceId = 0; faceId < faceCntLis.length; faceId++) {
            const faceCnt = faceCntLis[faceId];
            if (faceCnt == 3) {
                selectedFaceId.push(faceId);
            }
        }
        // console.log(selectedFaceId);

        var surfaceArea = 0;
        for (let faceId of selectedFaceId)
        {
            var p1, p2, p3, faceArea;
            [p1, p2, p3] = faces[faceId];
            faceArea = calcFaceArea(points[p1], points[p2], points[p3]);
            surfaceArea += faceArea;
        }
        console.log(surfaceArea);
        document.getElementById("surfaceAreaBox").value = surfaceArea; //TODO: 
    });
}

function getPoints(data) {
    var points = [];
    for (var i = 0; i < data.length; i += 3) {
        var point = [];
        point.push(data[i]);
        point.push(data[i + 1]);
        point.push(data[i + 2]);
        points.push(point);
    }
    return points;
}

function getFaces(data) {
    var faces = [];
    for (var i = 0; i < data.length; i += 3) {
        var face = [];
        face.push(data[i]);
        face.push(data[i + 1]);
        face.push(data[i + 2]);
        faces.push(face);
    }
    return faces;
}

function calcFaceArea(p1, p2, p3) {
    var p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z;
    [p1x, p1y, p1z] = p1;
    [p2x, p2y, p2z] = p2;
    [p3x, p3y, p3z] = p3;

    // Heron's formula2
    edge1_2 = Math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2 + (p1z - p2z) ** 2)
    edge1_3 = Math.sqrt((p1x - p3x) ** 2 + (p1y - p3y) ** 2 + (p1z - p3z) ** 2)
    edge2_3 = Math.sqrt((p2x - p3x) ** 2 + (p2y - p3y) ** 2 + (p2z - p3z) ** 2)
    p = (edge1_2 + edge1_3 + edge2_3) / 2
    area = Math.sqrt(p * (p - edge1_2) * (p - edge1_3) * (p - edge2_3))

    return area
}

var container, stats, mesh, points, faces;
var camera, cameraTarget, scene, renderer, geometry_clone, loader2;

function init(fileName) {

    container = document.createElement( 'div' );
    document.body.appendChild( container );
    container.setAttribute("id", "canvas");
    camera = new THREE.PerspectiveCamera( 35, window.innerWidth / window.innerHeight, 1, 200 );
    camera.position.set( -0.12, -22.3, 0.91 );   
    cameraTarget = new THREE.Vector3( 0, 0, 0 );

    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x72645b );

    // Load the .ply file into geometry.
    var loader = new THREE.PLYLoader();
    loader.load( fileName, function ( geometry ) {
        geometry.computeVertexNormals();

        var material = new THREE.MeshBasicMaterial({vertexColors: THREE.VertexColors });
        mesh = new THREE.Mesh( geometry,material);

        mesh.position.y =  0.0;
        mesh.position.z =  0.0;

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        scene.add( mesh );
        points = getPoints(scene.children[3].geometry.attributes.position.array);
        faces = getFaces(scene.children[3].geometry.index.array);
        geometry_clone = scene.children[3].geometry.clone();
    } );

    // Lights
    scene.add( new THREE.HemisphereLight( 0x443333, 0x111122 ) );
    addShadowedLight( 1, 1, 1, 0xffffff, 1.35 );
    addShadowedLight( 0.5, 1, -1, 0xffaa00, 1 );

    // renderer
    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.gammaInput = true;
    renderer.gammaOutput = true;
    renderer.shadowMap.enabled = true;

    cameraControls = new THREE.OrbitControls(camera, renderer.domElement);
    cameraControls.target.set( 0, 0, 0);
    cameraControls.maxDistance = 100;
    cameraControls.minDistance = 0;
    cameraControls.update();

    container.appendChild( renderer.domElement );

    // stats
    stats = new Stats();
    container.appendChild( stats.dom );
}

function addShadowedLight( x, y, z, color, intensity ) {

    var directionalLight = new THREE.DirectionalLight( color, intensity );
    directionalLight.position.set( x, y, z );
    scene.add( directionalLight );

    directionalLight.castShadow = true;

    var d = 1;
    directionalLight.shadow.camera.left = -d;
    directionalLight.shadow.camera.right = d;
    directionalLight.shadow.camera.top = d;
    directionalLight.shadow.camera.bottom = -d;

    directionalLight.shadow.camera.near = 1;
    directionalLight.shadow.camera.far = 4;

    directionalLight.shadow.mapSize.width = 1024;
    directionalLight.shadow.mapSize.height = 1024;

    directionalLight.shadow.bias = -0.001;
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}

function animate() {
    requestAnimationFrame( animate );
    render();
    stats.update();
}

function render() {
    camera.lookAt( cameraTarget );
    renderer.render( scene, camera );
}

function drawSquare() {
    clearDraw(); //clear the previous rectangle before drawing a new one.
    if(document.getElementById("switch").checked){
        cameraControls.enabled = false; 
        initDraw(document.getElementById('canvas'));
    }else{
        cameraControls.enabled = true;
    }
}

function initDraw(canvas) {
    function setMousePosition(e) {
        var ev = e || window.event; //Moz || IE
        if (ev.pageX) { //Moz
            mouse.x = ev.pageX + window.pageXOffset;
            mouse.y = ev.pageY + window.pageYOffset;
        } else if (ev.clientX) { //IE
            mouse.x = ev.clientX + document.body.scrollLeft;
            mouse.y = ev.clientY + document.body.scrollTop;
        }
    };

    var mouse = {
        x: 0,
        y: 0,
        startX: 0,
        startY: 0
    };
    var element = null;

    canvas.onmousemove = function (e) {
        setMousePosition(e);
        if (element !== null) {
            element.style.width = Math.abs(mouse.x - mouse.startX) + 'px';
            element.style.height = Math.abs(mouse.y - mouse.startY) + 'px';
            element.style.left = (mouse.x - mouse.startX < 0) ? mouse.x + 'px' : mouse.startX + 'px';
            element.style.top = (mouse.y - mouse.startY < 0) ? mouse.y + 'px' : mouse.startY + 'px';
        }
    }

    canvas.onclick = function (e) {
        if (element !== null) {
            element = null;
            canvas.style.cursor = "default";
            getSelectedPoint(mouse);
        } else {
            if(!cameraControls.enabled){
                clearDraw();
                mouse.startX = mouse.x;
                mouse.startY = mouse.y;
                element = document.createElement('div');
                element.className = 'rectangle'
                element.style.left = mouse.x + 'px';
                element.style.top = mouse.y + 'px';
                canvas.appendChild(element)
                canvas.style.cursor = "crosshair";
            }  
        }
    }
}

function clearDraw() {
    var elements = document.getElementsByClassName('rectangle');
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }

    var infoWindow = document.getElementById('infoWindow');
    if(infoWindow != null) infoWindow.parentNode.removeChild(infoWindow);
    localStorage.clear();
}

function allClear() {
    clearDraw();
    scene.children[3].geometry = geometry_clone;
}

function getSelectedPoint(mouse) {
    //four vertices of the rectangle
    var rec_left = Math.min(mouse.startX, mouse.x);
    var rec_right = Math.max(mouse.startX, mouse.x);
    var rec_top = Math.max(mouse.startY, mouse.y);
    var rec_bottom = Math.min(mouse.startY, mouse.y);

    pointIndices = [];
    var geometry = geometry_clone.clone();  //To successfullu change the color, a new goemetry has to be created.

    var i = 0;
    points.forEach(function(element){
 
        var p3D = new THREE.Vector3();
        p3D.x = element[0];
        p3D.y = element[1];
        p3D.z = element[2];

        p3D.project(camera);
        var x = (p3D.x + 1) * window.innerWidth / 2;
        var y = -(p3D.y - 1) * window.innerHeight / 2;

        //check whether the projection is inside the rectangle.
        if(x >= rec_left && x <= rec_right && y >= rec_bottom && y <= rec_top){

            pointIndices.push(i);
            var index = 3 * (i+1) -1;
            geometry.attributes.color.array[index] = 0;
            geometry.attributes.color.array[index-1] = 0;
            geometry.attributes.color.array[index-2] = 0.5;
        }
        
        if (i==points.length-1){

            scene.children[3].geometry = geometry;
        }
        i++;
    });

    console.log(pointIndices);
    console.log(scene);
    showSurfaceArea(mouse, pointIndices);
}

function getPoints(data) {
    var points = [];
    for (var i = 0; i < data.length; i+=3) {
        var point = [];
        point.push(data[i]);
        point.push(data[i+1]);
        point.push(data[i+2]);
        points.push(point);
    }
    return points;
}

function showSurfaceArea(mouse, pointIndices){
    var surfaceArea = 0;
    surfaceArea = calcSurfaceArea(pointIndices);
    var infoWindow = document.createElement('TEXTAREA');
    infoWindow.setAttribute("id", "infoWindow");
    infoWindow.setAttribute("rows","1");
    infoWindow.setAttribute("cols","33");
    infoWindow.style.position = "absolute";
    infoWindow.style.left = Math.max(mouse.x, mouse.startX) + 'px';
    infoWindow.style.top = Math.max(mouse.y, mouse.startY) + 'px';
    infoWindow.value = "Selected Surface Area = " + surfaceArea.toFixed(4) + ".";
    canvas.appendChild(infoWindow); 
}

function calcSurfaceArea(selectedPointIdLis) {
    var p2f = {}; // build the map from point id to related face id
    for (let faceId = 0; faceId < faces.length; faceId++) {
        var face = faces[faceId];
        for (let i = 0; i < 3; i++) {
            var p = face[i];
            p in p2f || (p2f[p] = []); // p2f.setdefault(p, [])
            p2f[p].push(faceId);
        }
    }
    // console.log(p2f);
    
    var faceCntLis = [...Array(faces.length)].map(_ => 0); // calc how many points related to each face
    for (let pointId of selectedPointIdLis) {
        if (pointId in p2f) {
            var faceIdLis = p2f[pointId];
            for (let faceId of faceIdLis) {
                faceCntLis[faceId] += 1;
            }
        }
    }
    // console.log(faceCntLis);

    var selectedFaceId = []; // consider the faces with 3 related points as valid ones
    for (let faceId = 0; faceId < faceCntLis.length; faceId++) {
        const faceCnt = faceCntLis[faceId];
        if (faceCnt == 3) {
            selectedFaceId.push(faceId);
        }
    }
    // console.log(selectedFaceId);

    var surfaceArea = 0; // calc surface area by summing face area up
    for (let faceId of selectedFaceId) {
        var p1, p2, p3, faceArea;
        [p1, p2, p3] = faces[faceId];
        faceArea = calcFaceArea(points[p1], points[p2], points[p3]);
        surfaceArea += faceArea;
    }
    return surfaceArea;
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
    edge1_2 = Math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2 + (p1z - p2z) ** 2);
    edge1_3 = Math.sqrt((p1x - p3x) ** 2 + (p1y - p3y) ** 2 + (p1z - p3z) ** 2);
    edge2_3 = Math.sqrt((p2x - p3x) ** 2 + (p2y - p3y) ** 2 + (p2z - p3z) ** 2);
    p = (edge1_2 + edge1_3 + edge2_3) / 2;
    area = Math.sqrt(p * (p - edge1_2) * (p - edge1_3) * (p - edge2_3));

    return area;
}
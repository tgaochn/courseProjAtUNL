/*
Projection: Jin 
Red: point
*/

var container, stats, mesh, points;
var camera, cameraTarget, scene, renderer, geometry_ori;


function init(fileName) {

    container = document.createElement( 'div' );
    document.body.appendChild( container );
    container.setAttribute("id", "canvas");
    camera = new THREE.PerspectiveCamera( 35, window.innerWidth / window.innerHeight, 1, 15 );
    camera.position.set( 0.0, 0.0, 1.3 );   
    cameraTarget = new THREE.Vector3( 0, 0, 0 );

    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x72645b );
    scene.fog = new THREE.Fog( 0x72645b, 2, 15 );

    // Ground
    /*
    var plane = new THREE.Mesh(
        new THREE.PlaneBufferGeometry( 40, 40 ),
        new THREE.MeshPhongMaterial( { color: 0x999999, specular: 0x101010 } )
    );
    plane.rotation.x = -Math.PI/2;
    plane.position.y = -0.5;
    scene.add( plane );
    plane.receiveShadow = true;
    */

    // PLY file
    var loader = new THREE.PLYLoader();
    loader.load( fileName, function ( geometry ) {
        geometry.computeVertexNormals();

        var material = new THREE.MeshBasicMaterial({vertexColors: THREE.VertexColors });
        mesh = new THREE.Mesh( geometry,material);

        mesh.position.y =  0.0;
        mesh.position.z =  0.0;
        mesh.rotation.z = -Math.PI / 2;
        mesh.scale.multiplyScalar( 0.1 );

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        scene.add( mesh );
        points = getPoints(geometry.attributes.position.array);
        geometry_ori = geometry;
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
    cameraControls.maxDistance = 5;
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
    clearDraw();
    if(document.getElementById("switch").checked){
        cameraControls.enabled = false; 
    }else{
        cameraControls.enabled = true;
    }
    initDraw(document.getElementById('canvas'));
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

    if(scene.children.length==5) scene.children.pop();
}

function getSelectedPoint(mouse) {
    var screenDistance = 1;
    var screenRight = Math.tan(camera.fov * Math.PI / 180 / 2) * screenDistance;
    var screenTop = screenRight / camera.aspect;

    var rec_x1 = (mouse.startX - 0.5 * window.innerWidth) * screenRight;
    var rec_x2 = (mouse.x - 0.5 * window.innerWidth) * screenRight;
    var rec_y1 = (mouse.startY - 0.5 * window.innerHeight) * screenTop;
    var rec_y2 = (mouse.y - 0.5 * window.innerHeight) * screenTop;

    var rec_left = Math.min(rec_x1, rec_x2);
    var rec_right = Math.max(rec_x1, rec_x2);
    var rec_top = Math.max(rec_y1, rec_y2);
    var rec_bottom = Math.min(rec_y1, rec_y2);

    var pointIndices = [];
    var geometry = new THREE.Geometry();

    var i = 0;
    points.forEach(function(element){
 
        var x = element[0];
        var y = element[1];
        var z = element[2];

        var projection_z = screenDistance;
        var projection_x = projection_z / z * x;
        var projection_y = Math.sqrt(Math.pow(projection_x,2) + Math.pow(projection_z,2)) 
                            / Math.sqrt(Math.pow(x,2) + Math.pow(z,2)) * y;

        if(projection_x >= rec_left && projection_x <= rec_right && 
           projection_y >= rec_bottom && projection_y <= rec_top){

            var star = new THREE.Vector3();
            pointIndices.push(i);

            var index = 3 * (i+1) -1;
            star.z=scene.children[3].geometry.attributes.position.array[index];
            star.y=scene.children[3].geometry.attributes.position.array[index-1];
            star.x=scene.children[3].geometry.attributes.position.array[index-2];

            var color=new THREE.Color(255,0,0);
            geometry.vertices.push( star );
            geometry.colors.push(color);

        }
        i++;

        if (i==points.length-1){

            var material= new THREE.PointsMaterial( {size:0.01, vertexColors: THREE.VertexColors} );
            var mesh_red = new THREE.Points(geometry, material);

            mesh_red.position.y =  0.0;
            mesh_red.position.z =  0.0;
            mesh_red.rotation.z = -Math.PI / 2;
            mesh_red.scale.multiplyScalar( 0.1 );
            mesh_red.castShadow = true;
            mesh_red.receiveShadow = true;
            scene.add( mesh_red  );
        }

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

    var infoWindow = document.createElement('TEXTAREA');
    infoWindow.setAttribute("id", "infoWindow");
    infoWindow.setAttribute("rows","2");
    infoWindow.setAttribute("cols","30");
    infoWindow.style.position = "absolute";
    infoWindow.style.left = Math.max(mouse.x, mouse.startX) + 'px';
    infoWindow.style.top = Math.max(mouse.y, mouse.startY) + 'px';
    infoWindow.value = "Selected Surface Area = " + surfaceArea + ".";
    canvas.appendChild(infoWindow);


}
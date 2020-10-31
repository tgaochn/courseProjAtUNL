{
	"metadata": {
		"version": 4.5,
		"type": "Object",
		"generator": "Object3D.toJSON"
	},
	"geometries": [{
		"uuid": "8AF8B441-D83D-4B92-9483-68126A6454BA",
		"type": "BufferGeometry",
		"data": {
			"attributes": {
				"position": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0.7370579838752747, 0.02470099925994873, 0.056919001042842865, 0.7258350253105164, 0.022958999499678612, 0.054120998829603195, 0.7325019836425781, 0.026350999251008034, 0.0661650002002716],
					"normalized": false
				},
				"color": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0.054901961237192154, 0.2705882489681244, 0.5215686559677124, 0.05098039284348488, 0.2666666805744171, 0.4941176474094391, 0.054901961237192154, 0.26274511218070984, 0.501960813999176],
					"normalized": false
				},
				"normal": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0, 0, 0, 0, 0, 0, 0, 0, 0],
					"normalized": false
				}
			},
			"index": {
				"type": "Uint32Array",
				"array": [112233, 332211, 221133]
			},
			"groups": [{
				"start": 0,
				"count": 3,
				"materialIndex": 0
			}],
			"boundingSphere": {
				"center": [0.7314465045928955, 0.024654999375343323, 0.0601429995149374],
				"radius": 0.008404142286336588
			}
		}
	}, {
		"uuid": "5A37EBF3-326E-431C-A824-8A361CC13E70",
		"type": "BufferGeometry",
		"data": {
			"attributes": {
				"position": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0.7370579838752747, 0.02470099925994873, 0.056919001042842865, 0.7258350253105164, 0.022958999499678612, 0.054120998829603195, 0.7325019836425781, 0.026350999251008034, 0.0661650002002716],
					"normalized": false
				},
				"color": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0.054901961237192154, 0.2705882489681244, 0.5215686559677124, 0.05098039284348488, 0.2666666805744171, 0.4941176474094391, 0.054901961237192154, 0.26274511218070984, 0.501960813999176],
					"normalized": false
				},
				"normal": {
					"itemSize": 3,
					"type": "Float32Array",
					"array": [0, 0, 0, 0, 0, 0, 0, 0, 0],
					"normalized": false
				}
			},
			"index": {
				"type": "Uint32Array",
				"array": [112233, 332211, 221133]
			},
			"groups": [{
				"start": 0,
				"count": 3,
				"materialIndex": 0
			}],
			"boundingSphere": {
				"center": [0.7314465045928955, 0.024654999375343323, 0.0601429995149374],
				"radius": 0.008404142286336588
			}
		}
	}],
	"materials": [{
		"uuid": "8A2F168E-90B0-449E-A18B-F80860395913",
		"type": "MeshBasicMaterial",
		"color": 16777215,
		"vertexColors": 2,
		"depthFunc": 3,
		"depthTest": true,
		"depthWrite": true
	}, {
		"uuid": "58628AC7-02DA-4FE7-83E0-ABCFBB3823E5",
		"type": "MeshBasicMaterial",
		"color": 16777215,
		"vertexColors": 2,
		"depthFunc": 3,
		"depthTest": true,
		"depthWrite": true
	}],
	"object": {
		"uuid": "F45C4A6F-86B3-461B-BA2C-D629D79CFFE2",
		"type": "Scene",
		"layers": 1,
		"matrix": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
		"children": [{
			"uuid": "681B594B-2175-49CD-B7D5-9438DFF86DDD",
			"type": "HemisphereLight",
			"layers": 1,
			"matrix": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
			"color": 4469555,
			"intensity": 1,
			"groundColor": 1118498
		}, {
			"uuid": "BAC6EF9F-F3F8-4252-AA9D-4CCE572C5504",
			"type": "DirectionalLight",
			"castShadow": true,
			"layers": 1,
			"matrix": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
			"color": 16777215,
			"intensity": 1.35,
			"shadow": {
				"bias": -0.001,
				"mapSize": [1024, 1024],
				"camera": {
					"uuid": "F9F85B5E-EC58-4690-84C7-E6B2ADFA3F9C",
					"type": "OrthographicCamera",
					"layers": 1,
					"zoom": 1,
					"left": -1,
					"right": 1,
					"top": 1,
					"bottom": -1,
					"near": 1,
					"far": 4
				}
			}
		}, {
			"uuid": "D21DD89C-9276-4AE9-9E74-6913C3C54EFF",
			"type": "DirectionalLight",
			"castShadow": true,
			"layers": 1,
			"matrix": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.5, 1, -1, 1],
			"color": 16755200,
			"intensity": 1,
			"shadow": {
				"bias": -0.001,
				"mapSize": [1024, 1024],
				"camera": {
					"uuid": "B571AA65-B985-4D5D-8815-A7D6A0119256",
					"type": "OrthographicCamera",
					"layers": 1,
					"zoom": 1,
					"left": -1,
					"right": 1,
					"top": 1,
					"bottom": -1,
					"near": 1,
					"far": 4
				}
			}
		}, {
			"uuid": "BEBCDD17-3D4F-4852-B402-B89BB763EEE7",
			"type": "Mesh",
			"castShadow": true,
			"receiveShadow": true,
			"layers": 1,
			"matrix": [-2.2204460492503132e-17, -0.10000000000000003, 0, 0, 0.10000000000000003, -2.2204460492503132e-17, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 1],
			"geometry": "8AF8B441-D83D-4B92-9483-68126A6454BA",
			"material": "8A2F168E-90B0-449E-A18B-F80860395913"
		}, {
			"uuid": "D6F1F2B6-3892-4D31-84B5-5568E221D0D7",
			"type": "Mesh",
			"castShadow": true,
			"receiveShadow": true,
			"layers": 1,
			"matrix": [-2.2204460492503132e-17, -0.10000000000000003, 0, 0, 0.10000000000000003, -2.2204460492503132e-17, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 1],
			"geometry": "5A37EBF3-326E-431C-A824-8A361CC13E70",
			"material": "58628AC7-02DA-4FE7-83E0-ABCFBB3823E5"
		}],
		"background": 7496795,
		"fog": {
			"type": "Fog",
			"color": 7496795,
			"near": 2,
			"far": 15
		}
	}
}
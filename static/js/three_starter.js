// Three.js Starter
// File: static/js/three_starter.js
// Purpose: Bootstraps a basic GLTF scene in browser.
// Load via importmap in your HTML templates.

import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const canvas   = document.createElement('canvas');
document.body.appendChild(canvas);
const renderer = new THREE.WebGLRenderer({canvas, antialias: true});
renderer.setSize(window.innerWidth, window.innerHeight);

const scene  = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.set(0,1,3);

scene.add(new THREE.HemisphereLight(0xffffff,0x444444));

new GLTFLoader().load('/static/models/model.glb', gltf => {
  scene.add(gltf.scene);
});

(function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
})();

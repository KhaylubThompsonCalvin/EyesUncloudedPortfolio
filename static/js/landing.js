import * as THREE        from 'three';
import { GLTFLoader }    from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// ——— Renderer ———
const container = document.getElementById('scene-container');
const renderer  = new THREE.WebGLRenderer({ antialias: true });
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
container.appendChild(renderer.domElement);

// ——— Scene & Camera ———
const scene  = new THREE.Scene();
scene.background = new THREE.Color(0x000000);
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(4, 5, 11);
camera.lookAt(0, 0, 0);

// ——— OrbitControls ———
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping   = true;
controls.dampingFactor   = 0.05;
controls.autoRotate      = false;
controls.autoRotateSpeed = 2.0;
controls.update();

// ——— Ground ———
const groundGeo = new THREE.PlaneGeometry(20, 20, 32, 32);
groundGeo.rotateX(-Math.PI / 2);
const groundMat = new THREE.MeshStandardMaterial({
  color: 0x555555,
  side: THREE.DoubleSide
});
scene.add(new THREE.Mesh(groundGeo, groundMat));

// ——— Lights ———
scene.add(new THREE.AmbientLight(0xffffff, 0.8));
const spotLight = new THREE.SpotLight(0xffffff, 3, 100, 0.2, 0.5);
spotLight.position.set(0, 25, 0);
scene.add(spotLight);

// ——— Load Model ———
const loader = new GLTFLoader();
loader.load(
  '/static/models/lab_scene/lab_model.gltf',
  (gltf) => {
    console.log('✅ model loaded', gltf);
    debugger;  // ← when this runs, DevTools will pause here
    const model = gltf.scene;
    model.scale.set(1.5, 1.5, 1.5);
    scene.add(model);
  },
  (xhr) => console.log(`Loading ${(xhr.loaded/xhr.total*100).toFixed(1)}%`),
  (err) => console.error('❌ GLTF load error', err)
);

// ——— Handle Resize ———
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// ——— Animate Loop ———
(function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
})();











/* particles.js — Three.js ambient particle layer */

(function () {
  const canvases = ['particleCanvas', 'contactCanvas'];

  canvases.forEach(function (id) {
    const canvas = document.getElementById(id);
    if (!canvas) return;

    let renderer, scene, camera, particles, animId;
    let mouseX = 0, mouseY = 0;
    let W = canvas.offsetWidth || window.innerWidth;
    let H = canvas.offsetHeight || window.innerHeight;

    // Lazy-load Three.js from CDN
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    script.onload = function () {
      init();
    };
    if (!window.THREE) {
      document.head.appendChild(script);
    } else {
      init();
    }

    function init() {
      const THREE = window.THREE;
      if (!THREE) return;

      renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: false });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
      renderer.setSize(W, H);
      renderer.setClearColor(0x000000, 0);

      scene = new THREE.Scene();
      camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 1000);
      camera.position.z = 80;

      const COUNT = id === 'contactCanvas' ? 120 : 260;
      const positions = new Float32Array(COUNT * 3);

      for (let i = 0; i < COUNT; i++) {
        positions[i * 3]     = (Math.random() - 0.5) * 200;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 180;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 80;
      }

      const geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

      // Glow sprite
      const tc = document.createElement('canvas');
      tc.width = 32; tc.height = 32;
      const ctx = tc.getContext('2d');
      const g = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
      g.addColorStop(0,   'rgba(208,228,255,1)');
      g.addColorStop(0.4, 'rgba(168,180,200,0.5)');
      g.addColorStop(1,   'rgba(0,0,0,0)');
      ctx.fillStyle = g;
      ctx.fillRect(0, 0, 32, 32);

      const mat = new THREE.PointsMaterial({
        size: 1.8,
        map: new THREE.CanvasTexture(tc),
        blending: THREE.AdditiveBlending,
        transparent: true,
        depthWrite: false,
        opacity: 0.5,
        sizeAttenuation: true,
      });

      particles = new THREE.Points(geo, mat);
      scene.add(particles);

      window.addEventListener('mousemove', onMouse, { passive: true });
      window.addEventListener('resize', onResize);

      let t = 0;
      (function tick() {
        animId = requestAnimationFrame(tick);
        t += 0.0005;
        const pos = particles.geometry.attributes.position.array;
        for (let i = 0; i < COUNT; i++) {
          pos[i * 3 + 1] += Math.sin(t + i * 0.55) * 0.007;
          pos[i * 3]     += Math.cos(t + i * 0.35) * 0.004;
        }
        particles.geometry.attributes.position.needsUpdate = true;
        camera.position.x += (mouseX * 7 - camera.position.x) * 0.018;
        camera.position.y += (mouseY * 4 - camera.position.y) * 0.018;
        camera.lookAt(scene.position);
        renderer.render(scene, camera);
      })();
    }

    function onMouse(e) {
      mouseX =  (e.clientX / window.innerWidth  - 0.5) * 2;
      mouseY = -(e.clientY / window.innerHeight - 0.5) * 2;
    }

    function onResize() {
      W = canvas.offsetWidth || window.innerWidth;
      H = canvas.offsetHeight || window.innerHeight;
      if (renderer && camera) {
        renderer.setSize(W, H);
        camera.aspect = W / H;
        camera.updateProjectionMatrix();
      }
    }
  });
})();

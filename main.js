/* main.js — GSAP animations, nav scroll-spy, video controls, reveal */

gsap.registerPlugin(ScrollTrigger);

/* ── HERO ENTRANCE ─────────────────────────────────── */
(function () {
  const els = [
    { el: '.hero-eyebrow',    delay: 0.3  },
    { el: '.hero-name-first', delay: 0.55 },
    { el: '.hero-name-last',  delay: 0.72 },
    { el: '.hero-tagline',    delay: 0.95 },
    { el: '.hero-ctas',       delay: 1.15 },
  ];

  els.forEach(function (item) {
    const el = document.querySelector(item.el);
    if (!el) return;
    gsap.to(el, {
      opacity: 1, y: 0, duration: 1.2,
      ease: 'expo.out', delay: item.delay,
    });
  });

  // Scroll indicator
  gsap.to('#scrollIndicator', {
    opacity: 0.6, y: 0, duration: 1,
    ease: 'power2.out', delay: 1.8,
  });
})();

/* ── SCROLL REVEAL ─────────────────────────────────── */
(function () {
  const revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    // Stagger children in same parent
    revealEls.forEach(function (el, i) {
      const siblings = el.parentElement.querySelectorAll('.reveal');
      let delay = 0;
      siblings.forEach(function (sib, si) {
        if (sib === el) delay = si * 0.08;
      });
      el.style.transitionDelay = delay + 's';
      observer.observe(el);
    });
  } else {
    // Fallback
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }
})();

/* ── NAV SCROLL ────────────────────────────────────── */
/* ── NAV SCROLL + BACK TO TOP ──────────────────────── */
(function () {
  const nav = document.getElementById('nav');
  const btn = document.getElementById('backToTop');
  const sections = ['about','experience','achievements','skills','certifications','contact'];

  window.addEventListener('scroll', function () {

    // Nav scrolled state
    if (window.scrollY > 60) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');

    // Back to top button visibility
    if (btn) {
      if (window.scrollY > 400) btn.classList.add('visible');
      else btn.classList.remove('visible');
    }

    // Active nav link
    let current = '';
    sections.forEach(function (id) {
      const el = document.getElementById(id);
      if (el && el.getBoundingClientRect().top <= 120) current = id;
    });
    document.querySelectorAll('.nav-link').forEach(function (link) {
      link.classList.remove('active');
      if (link.textContent.toLowerCase().replace(/[^a-z]/g,'').includes(current.replace(/[^a-z]/g,''))) {
        link.classList.add('active');
      }
    });

  }, { passive: true });
})();

/* ── MOBILE MENU ───────────────────────────────────── */
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  menu.classList.toggle('open');
}

/* ── VIDEO CONTROLS ────────────────────────────────── */
var isMuted = true;
var isPlaying = true;

function toggleMute() {
  const video = document.getElementById('heroVideo');
  isMuted = !isMuted;
  video.muted = isMuted;
  document.getElementById('iconMuted').style.display = isMuted  ? 'block' : 'none';
  document.getElementById('iconSound').style.display = !isMuted ? 'block' : 'none';
  document.getElementById('soundHint').style.opacity = '0';
}

function togglePlay() {
  const video = document.getElementById('heroVideo');
  if (isPlaying) {
    video.pause();
    document.getElementById('iconPause').style.display = 'none';
    document.getElementById('iconPlay').style.display  = 'block';
  } else {
    video.play();
    document.getElementById('iconPause').style.display = 'block';
    document.getElementById('iconPlay').style.display  = 'none';
  }
  isPlaying = !isPlaying;
}

/* ── SOUND HINT AUTO-HIDE ──────────────────────────── */
setTimeout(function () {
  var hint = document.getElementById('soundHint');
  if (hint) hint.style.opacity = '0';
}, 5000);

/* ── CONTACT FORM ──────────────────────────────────── */
function handleSubmit(e) {
  e.preventDefault();
  var form = e.target;
  var name    = form.elements['name'].value;
  var email   = form.elements['email'].value;
  var message = form.elements['message'].value;
  var mailto  = 'mailto:garishma.gari@gmail.com'
    + '?subject=' + encodeURIComponent('Portfolio Enquiry from ' + name)
    + '&body='    + encodeURIComponent('From: ' + name + '\nEmail: ' + email + '\n\n' + message);
  window.location.href = mailto;
}

/* ── EXPERIENCE STACK SCROLL ───────────────────────── */
(function () {
  const items = document.querySelectorAll('.stack-item');
  if (!items.length) return;

  window.addEventListener('scroll', function () {
    items.forEach(function (item, index) {
      const card = item.querySelector('.stack-card');
      if (!card) return;

      const rect = item.getBoundingClientRect();
      const nextItem = items[index + 1];

      if (!nextItem) {
        // Last card — always full
        card.style.transform = 'scale(1)';
        card.style.filter = 'brightness(1)';
        return;
      }

      const nextRect = nextItem.getBoundingClientRect();

      // How much has the next card overlapped this one (0 to 1)
      const overlap = Math.max(0, Math.min(1,
        (card.offsetHeight - nextRect.top + item.getBoundingClientRect().top) / card.offsetHeight
      ));

      // As next card slides over, scale down and darken this card
      const scale = 1 - (overlap * 0.04);
      const brightness = 1 - (overlap * 0.45);

      card.style.transition = 'transform 0.1s ease, filter 0.1s ease';
      card.style.transform = `scale(${Math.max(0.92, scale)})`;
      card.style.filter = `brightness(${Math.max(0.55, brightness)})`;
    });
  }, { passive: true });
})();

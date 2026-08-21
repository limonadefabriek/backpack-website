/* Backpack — gedeelde scripts. Eén bestand voor alle pagina's. */
(function () {
  'use strict';

  // Header krijgt achtergrond zodra je scrollt
  var header = document.getElementById('header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 20); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobiel menu
  var burger = document.getElementById('burger');
  var navlist = document.getElementById('navlist');
  if (burger && navlist) {
    burger.addEventListener('click', function () {
      var open = navlist.classList.toggle('open');
      burger.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    navlist.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navlist.classList.remove('open');
        burger.classList.remove('open');
        burger.setAttribute('aria-expanded', false);
        document.body.style.overflow = '';
      });
    });
  }

  // Submenu's: hover op desktop, uitklappen op mobiel
  document.querySelectorAll('.navbtn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (window.innerWidth > 1120) return;
      e.preventDefault();
      var open = btn.nextElementSibling.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });

  // Tabbladen (inspiratie)
  var tabs = document.querySelectorAll('.tab');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on);
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
    });
  });

  // Reviews: schuiven met de pijltjes
  var rail = document.getElementById('rev-rail');
  if (rail) {
    var knoppen = document.querySelectorAll('.rail-btn');
    var stap = function () {
      var kaart = rail.querySelector('.rev');
      return kaart ? kaart.offsetWidth + 20 : 340;
    };
    knoppen.forEach(function (b) {
      b.addEventListener('click', function () {
        rail.scrollBy({ left: b.dataset.rail === 'next' ? stap() : -stap(), behavior: 'smooth' });
      });
    });
    var stand = function () {
      var max = rail.scrollWidth - rail.clientWidth - 4;
      knoppen.forEach(function (b) {
        b.disabled = b.dataset.rail === 'prev' ? rail.scrollLeft <= 4 : rail.scrollLeft >= max;
      });
    };
    rail.addEventListener('scroll', stand, { passive: true });
    stand();
  }

  // Conversiemeting: elke klik naar een afspraaksysteem wordt geregistreerd.
  // Werkt zodra Google Analytics 4 of Tag Manager is geplaatst.
  window.dataLayer = window.dataLayer || [];
  document.querySelectorAll('a[href*="clientomgeving.nl"], a[href*="onlineafspraken.nl"]').forEach(function (a) {
    a.addEventListener('click', function () {
      var wie = a.dataset.book || (a.href.indexOf('onlineafspraken') > -1 ? 'maaike' : 'clementine');
      var blok = a.closest('section, header, footer');
      window.dataLayer.push({ event: 'afspraak_klik', behandelaar: wie, plek: (blok && blok.id) || 'overig' });
      if (typeof gtag === 'function') gtag('event', 'afspraak_klik', { behandelaar: wie });
    });
  });

  // Zachte fade-in bij scrollen.
  // Pas als we zeker weten dat het werkt, verbergen we iets — en er is een
  // noodrem die na 2,5 seconde alles alsnog toont.
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && items.length) {
    document.documentElement.classList.add('js-anim');
    var toon = function (el) { el.classList.add('in'); };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { toon(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -5% 0px' });
    items.forEach(function (el) { io.observe(el); });
    setTimeout(function () { items.forEach(toon); }, 2500);
  }
})();

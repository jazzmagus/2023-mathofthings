---
title: Studiare (con l'IA)
summary: Metodo di studio, ieri e oggi, tra internet e intelligenza artificiale
authors: [Diego Fantinelli]
tags: [organizzazione, metodo-di-studio, AI]
categories: [lesson]
date: "2026-09-06T00:00:00Z"
draft: true
slides:
  theme: mathofthings
  transition: convex
  particles: true
---

<section class="mot-hero" data-transition="zoom">
  <div class="hero-icon hero-icon-anim" style="margin: 0 auto 16px; width: 140px;">
    <svg width="140" height="50" viewBox="0 0 140 50" aria-hidden="true">
      <defs>
        <filter id="hero-goo" x="-30" y="-30" width="200" height="110" filterUnits="userSpaceOnUse">
          <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
          <feColorMatrix in="blur" mode="matrix"
            values="1 0 0 0 0
                    0 1 0 0 0
                    0 0 1 0 0
                    0 0 0 20 -9" result="goo" />
          <feComposite in="SourceGraphic" in2="goo" operator="atop" />
        </filter>
      </defs>
      <g filter="url(#hero-goo)" fill="currentColor">
        <circle cx="70" cy="25" r="16" />
        <circle id="hero-icon-ball" cx="70" cy="25" r="6.5" />
      </g>
    </svg>
  </div>
  <script>
    (function () {
      var ball = document.getElementById('hero-icon-ball');
      if (!ball) return;
      var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduceMotion) return;
      var centerX = 70, amplitude = 40, duration = 1600, start = null;
      function frame(ts) {
        if (start === null) start = ts;
        var elapsed = (ts - start) % (duration * 2);
        var t = elapsed / duration;
        var x = t < 1 ? -amplitude + amplitude * 2 * t : amplitude - amplitude * 2 * (t - 1);
        ball.setAttribute('cx', centerX + x);
        requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    })();
  </script>
  <p class="mot-kicker">metodo di studio</p>
  <h1>Studiare con<br>L'intelligenza<br><em>artificiale</em></h1>
  <p class="mot-tagline">breve storia di come si studia la matematica &mdash; da prima di internet a <em>oggi</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DI INTERNET</h1>
  <p class="mot-joke fragment">quando "cercare su Google" si chiamava "andare in biblioteca"</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Come si studiava <em>prima</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DELL'IA</h1>
  <p class="mot-joke fragment">l'era di Wikipedia, YouTube e "fidati, l'ho letto da qualche parte"</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Internet, ma senza <em>l'IA</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">OGGI</h1>
  <p class="mot-joke fragment">studiare con l'IA, senza farsi studiare dall'IA</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Studiare oggi con <em>l'IA</em></h2>
  <p class="fragment">Un approfondimento:<br><a href="/post/chi-ha-paura-ia/" target="_blank" class="mono" style="display:inline-flex; align-items:center; gap:0.4em;">
    <svg width="0.9em" height="0.9em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    Chi ha paura dell'Intelligenza Artificiale?
  </a></p>
  <p class="mot-def fragment">L'intelligenza artificiale ha cambiato, e non poco, l'approccio allo studio: porta con sé dei benefici innegabili, ma anche qualche controindicazione. Il mio punto di vista sarà quello di pesare pro e contro dell'IA come supporto allo studio della matematica &mdash; e più in generale delle materie scientifiche.</p>
</section>

<section>
  <p class="mot-kicker">i contro</p>
  <h2>Gli <em>svantaggi</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

<section>
  <p class="mot-kicker">i pro</p>
  <h2>I <em>vantaggi</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

<section>
  <p class="mot-kicker">il bilancio</p>
  <h2>Come cambia <em>(in meglio)</em> il metodo di studio</h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

---

<section class="mot-divider" data-transition="zoom" data-background-image="panic.jpg" data-background-opacity="0.2">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">le domande stupide non esistono. Le risposte, qualche volta.</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon anno scolastico</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

<style>
body.slides-mot {
  --mot-primary: #2f8fbf;
  --r-link-color: #2f8fbf;
  --r-link-color-hover: #57abd6;
  --r-selection-background-color: rgba(47, 143, 191, 0.35);
}

body.slides-mot.dark {
  --mot-primary: #63c2e8;
  --r-link-color: #63c2e8;
  --r-link-color-hover: #8ad3ee;
}
</style>

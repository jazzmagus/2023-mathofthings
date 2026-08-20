---
title: "Il Bayesian"
summary: "Un teorema, una fortuna, un naufragio — la storia di Mike Lynch e dell'inferenza bayesiana"
authors: [Diego Fantinelli]
tags: [probabilità, teorema di Bayes, storia]
categories: [lesson]
date: "2026-07-08T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
---

<section class="mot-hero" data-background-color="#5f93b3" data-background-image="bayesian_2.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.28" data-transition="zoom">
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
  <div id="particles-bl-hero" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <p class="mot-kicker" style="color: white; position: relative; z-index: 10;">matematica e vita reale</p>
  <h1 style="color: white; position: relative; z-index: 10;">Il <span class="math-word" style="color: white; font-style: italic;">Bayesian</span></h1>
  <p class="mot-tagline" style="font-family: 'Georgia', serif; color: rgba(255,255,255,0.95); font-size: 1.3em; position: relative; z-index: 10;">un <em style="font-style: italic; color: white;">teorema</em>, una <em style="font-style: italic; color: white;">fortuna</em>, un <em style="font-style: italic; color: white;">naufragio</em></p>
  <p class="mot-meta" style="color: rgba(255,255,255,0.9); position: relative; z-index: 10;">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-porticello" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">PORTICELLO, 19 AGOSTO 2024</h1>
</section>

<section>
  <p class="mot-kicker">poco prima dell'alba</p>
  <h2>Un veliero all'<em>ancora</em></h2>
  <p class="mot-def fragment">56 metri di lunghezza. L'albero in alluminio <b>più alto del mondo</b>: 72 metri.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Una tromba d'aria improvvisa lo colpisce. In <b>pochi minuti</b> si capovolge e affonda.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Sette persone non tornano a riva.</p>
  <p class="fragment" style="font-size: 0.8em; margin-top: 1.5rem; color: #666;">Il nome del veliero: <b>Bayesian</b>.</p>
</section>

---

<section class="mot-divider" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-lynch" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">CHI ERA MIKE LYNCH</h1>
</section>

<section>
  <p class="mot-kicker">"il Bill Gates britannico"</p>
  <h2>Un impero sul <em>software</em></h2>
  <p class="mot-def fragment">Fonda <b>Autonomy</b>: un software capace di <i>leggere</i> testi, email e documenti e di capirne il significato.</p>
  <p class="fragment mot-result" style="margin-top: 2rem; font-size: 1.3em;">2011: HP la compra per<br>≈ 11 miliardi di dollari</p>
</section>

<section>
  <p class="mot-kicker">tredici anni di processi</p>
  <h2>Accusa, e <em>assoluzione</em></h2>
  <p class="fragment">HP lo accusa di aver gonfiato i conti. Comincia una lunga battaglia legale tra Regno Unito e Stati Uniti.</p>
  <p class="fragment mot-result" style="margin-top: 2rem;">Giugno 2024: assolto da tutte le 15 accuse.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">La crociera in Sicilia era la festa per quella assoluzione.</p>
</section>

---

<section class="mot-divider" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-why" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">PERCHÉ "BAYESIAN"?</h1>
</section>

<section>
  <p class="mot-kicker">il cuore della tecnologia</p>
  <h2>Il nome della sua <em>fortuna</em></h2>
  <p class="mot-def fragment">Il motore di Autonomy era una vecchia idea della probabilità: l'<b>inferenza bayesiana</b>.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Lynch battezza il suo veliero <b>Bayesian</b> in omaggio a quella matematica.</p>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1.5rem; color: #666;">Un'idea del reverendo <b>Thomas Bayes</b>, pubblicata nel <b>1763</b>. Due secoli e mezzo dopo, un impero da miliardi.</p>
</section>

---

<section class="mot-divider" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-teorema" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">IL TEOREMA</h1>
</section>

<section>
  <p class="mot-kicker">in una frase</p>
  <h2>Come si <em>cambia idea</em></h2>
  <blockquote class="mot-quote fragment">
    Ho una convinzione. Arriva una nuova informazione. Di quanto devo cambiare idea?
  </blockquote>
  <p class="fragment" style="margin-top: 1.5rem;">Bayes è il meccanismo con cui <b>aggiorniamo le credenze</b> davanti alle prove.</p>
</section>

<section>
  <p class="mot-kicker">la formula</p>
  <h2>Bayes, in <em>simboli</em></h2>
  <p class="fragment mot-result">$$P(C \mid E) = \frac{P(E \mid C)\, P(C)}{P(E)}$$</p>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1.5rem;">$C$ = la <b>causa</b> (l'ipotesi) &nbsp;·&nbsp; $E$ = l'<b>evidenza</b> osservata</p>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1rem; color: #666;">Il teorema <i>capovolge</i> il ragionamento: dalla causa all'effetto, e ritorno.</p>
</section>

<section>
  <p class="mot-kicker">l'esempio che spiazza</p>
  <h2>Il <em>test</em> positivo</h2>
  <p class="mot-def fragment">Malattia rara: 1 persona su 1000. Test affidabile al 95%. Risulti <b>positivo</b>.</p>
  <p class="fragment" style="margin-top: 1.5rem; font-size: 0.9em;">Quanto devi preoccuparti? L'istinto grida <b>95%</b>.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem; font-size: 1.4em;">$$P(\text{malato} \mid \text{positivo}) \approx 2\%$$</p>
  <p class="fragment" style="font-size: 0.8em; margin-top: 1.5rem; color: #666;">La malattia è così rara che i <b>falsi positivi</b> superano i veri malati.</p>
</section>

---

<section class="mot-divider" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-ironia" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">LA CODA DELLA DISTRIBUZIONE</h1>
</section>

<section>
  <p class="mot-kicker">un teorema, e la sua ironia</p>
  <h2>Ciò che è <em>raro</em> accade</h2>
  <p class="fragment">Un veliero all'ancora, a poche centinaia di metri dalla riva: catastrofe a probabilità bassissima.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Bassissima. Non nulla.</p>
  <p class="fragment" style="margin-top: 1.5rem; font-size: 0.9em;">Il <b>Bayesian</b> porta il nome del teorema che più di ogni altro ci ricorda: gli eventi rarissimi, ogni tanto, <b>accadono</b>.</p>
</section>

<section class="mot-hero" data-background-color="#5f93b3" data-transition="zoom" style="color: white;">
  <div id="particles-bl-finale" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 style="font-size: 2.3em; color: white; position: relative; z-index: 10;">Non dimenticare mai<br>la <em style="color: white; font-style: italic;">coda</em></h1>
  <p style="font-size: 1.2em; margin-top: 1.5rem; color: white; position: relative; z-index: 10;">Il piccolo numero che non arriva mai a zero.</p>
  <p class="mot-meta" style="color: rgba(255,255,255,0.95); margin-top: 2rem; position: relative; z-index: 10;"><a href="https://mathofthings.netlify.app/" target="_blank" style="color:inherit" class="mono">The Math of Things</a></p>
</section>

<style>
.reveal { --mot-primary: #5f93b3; }

.reveal .mot-divider h1 { color: #ffffff !important; }

.mot-hero h1 em,
.mot-hero .mot-tagline em {
  color: rgba(255,255,255,0.95);
  font-style: italic;
}

.reveal section[data-background-color="#5f93b3"] svg line,
.reveal section[data-background-color="#5f93b3"] svg circle {
  stroke: rgba(255, 255, 255, 0.4) !important;
  fill: rgba(255, 255, 255, 0.2) !important;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>
<script>
(function () {
  if (typeof tsParticles === 'undefined') return;

  var config = {
    fpsLimit: 60,
    particles: {
      number: { value: 80, density: { enable: true, area: 800 } },
      color: { value: '#ffffff' },
      opacity: { value: { min: 0.2, max: 0.5 } },
      size: { value: { min: 0.5, max: 3 } },
      move: {
        enable: true,
        speed: { min: 0.2, max: 1.5 },
        direction: 'none',
        random: true,
        straight: false,
        outModes: { default: 'out' },
        spin: { enable: true, acceleration: 0 }
      }
    },
    interactivity: {
      events: { onHover: { enable: false }, onClick: { enable: false } }
    },
    detectRetina: true
  };

  var particleIds = ['particles-bl-hero', 'particles-bl-porticello', 'particles-bl-lynch', 'particles-bl-why', 'particles-bl-teorema', 'particles-bl-ironia', 'particles-bl-finale'];
  particleIds.forEach(function (id) {
    if (document.getElementById(id)) {
      tsParticles.load(id, config);
    }
  });
})();
</script>

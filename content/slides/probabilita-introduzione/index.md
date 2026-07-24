---
title: Calcolo delle Probabilità
summary: Introduzione interattiva e ludica — giochiamo con i dadi, i sondaggi e il gioco d'azzardo
authors: [Diego Fantinelli]
tags: [probabilità, gioco, dadi, sondaggi, valore atteso]
categories: [lesson]
date: "2026-07-07T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
---

<section class="mot-hero" data-background-color="#ed6f5c" data-transition="zoom">
  <div id="particles-prob-hero" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <p class="mot-kicker" style="color: white; position: relative; z-index: 10;">matematica per il triennio</p>
  <h1 style="color: white; position: relative; z-index: 10;">Calcolo delle <span class="math-word" style="color: white; font-style: italic;">Probabilità</span></h1>
  <p class="mot-tagline" style="color: rgba(255,255,255,0.95); font-size: 1.3em; position: relative; z-index: 10;">quando la <em style="font-style: italic; color: white;">fortuna</em><br>incontra la <em style="font-style: italic; color: white;">matematica</em></p>
  <p class="mot-meta" style="color: rgba(255,255,255,0.9); position: relative; z-index: 10;">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono" style="color: white;">The Math of Things</a></p>
</section>

---

<section>
  <blockquote class="mot-quote">
    "Dio non gioca a dadi con l'universo." — Albert Einstein
    <span class="quote-attr">Ma i matematici sì.</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-background-color="#ed6f5c" data-transition="zoom" style="color: white;">
  <div id="particles-quando" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10; color: white;">QUANDO ACCADE QUALCOSA?</h1>
</section>

<section>
  <p class="mot-kicker">il concetto fondamentale</p>
  <h2>Che cos'è la <em>probabilità</em>?</h2>
  <p class="mot-def fragment">La probabilità misura quanto è <b>probabile</b> che accada un evento. È un numero tra 0 e 1.</p>
  <div class="mot-cols fragment" style="margin-top: 1.5rem;">
    <div class="mot-col">
      <p style="font-size: 0.85em"><b>Evento impossibile:</b></p>
      <p class="mot-result" style="font-size: 1.2em">P = 0</p>
      <p style="font-size: 0.75em">Non accade mai</p>
    </div>
    <div class="mot-col">
      <p style="font-size: 0.85em"><b>Evento certo:</b></p>
      <p class="mot-result" style="font-size: 1.2em">P = 1</p>
      <p style="font-size: 0.75em">Accade sempre</p>
    </div>
  </div>
  <p class="fragment" style="font-size: 0.8em; margin-top: 2rem;">$0 \lt P(\text{evento}) \lt 1$ = <b>probabilità che l'evento accada</b></p>
</section>

<section>
  <p class="mot-kicker">esperimento 1: il dado</p>
  <h2>Lanciamo un <em>dado</em>!</h2>
  <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; margin: 2rem 0;">
    <div style="font-size: 4rem; cursor: pointer; user-select: none; padding: 1rem;" id="dice-visual">🎲</div>
    <div style="text-align: left; font-size: 0.85em;">
      <p><b>Spazio campionario:</b></p>
      <p>$\{1, 2, 3, 4, 5, 6\}$</p>
      <p style="margin-top: 1rem;"><b>Probabilità di un numero:</b></p>
      <p class="mot-result">$$P(\text{un numero}) = \frac{1}{6}$$</p>
    </div>
  </div>
  <button id="roll-btn" style="padding: 0.8rem 1.5rem; font-size: 1.1em; background: var(--mot-primary); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">Lancia il dado</button>
  <p id="dice-result" style="margin-top: 1.5rem; font-size: 1.2em; color: var(--mot-primary); font-weight: 600; min-height: 1.5em;"></p>
</section>

<section>
  <p class="mot-kicker">la moneta non tradisce</p>
  <h2>Testa o <em>Croce</em>?</h2>
  <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; margin: 2rem 0;">
    <div style="font-size: 4rem; cursor: pointer; user-select: none; padding: 1rem;" id="coin-visual">🪙</div>
    <div style="text-align: left; font-size: 0.9em;">
      <p><b>Due esiti equiprobabili:</b></p>
      <p class="mot-result" style="font-size: 1.1em">$$P(\text{Testa}) = P(\text{Croce}) = \frac{1}{2}$$</p>
    </div>
  </div>
  <button id="flip-btn" style="padding: 0.8rem 1.5rem; font-size: 1.1em; background: var(--mot-primary); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">Lancia la moneta</button>
  <p id="coin-result" style="margin-top: 1.5rem; font-size: 1.1em; min-height: 1.5em;"></p>
  <p class="fragment" style="font-size: 0.75em; margin-top: 1rem; color: #666;">Se la moneta è <b>equa</b>, testa e croce hanno la stessa probabilità.</p>
</section>

---

<section class="mot-divider" data-background-color="#ed6f5c" data-transition="zoom" style="color: white;">
  <div id="particles-sondaggi" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10; color: white;">SONDAGGI & STATISTICHE</h1>
</section>

<section>
  <p class="mot-kicker">proporzionalità</p>
  <h2>Il <em>sondaggio</em> della classe</h2>
  <p class="mot-def">Facciamo un rapido sondaggio: chi preferisce i dadi, chi la moneta, chi l'astrologia?</p>
  
  <div style="margin: 1.5rem auto 1rem; width: 95%; max-width: 750px;">
    <div style="margin: 0.8rem 0;">
      <div style="display: grid; grid-template-columns: 300px 1fr; align-items: center; gap: 1rem; margin-bottom: 1rem;">
        <span style="font-weight: 600; text-align: left;">Dadi</span>
        <div id="bar-dice" style="height: 35px; background: var(--mot-primary); width: 0%; border-radius: 4px; transition: width 0.3s; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; color: white; font-weight: 600; font-size: 0.95em;"></div>
      </div>
      <div style="display: grid; grid-template-columns: 300px 1fr; align-items: center; gap: 1rem; margin-bottom: 1rem;">
        <span style="font-weight: 600; text-align: left;">Moneta</span>
        <div id="bar-coin" style="height: 35px; background: #3a6b8c; width: 0%; border-radius: 4px; transition: width 0.3s; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; color: white; font-weight: 600; font-size: 0.95em;"></div>
      </div>
      <div style="display: grid; grid-template-columns: 300px 1fr; align-items: center; gap: 1rem;">
        <span style="font-weight: 600; text-align: left;">Astrologia</span>
        <div id="bar-astro" style="height: 35px; background: #999; width: 0%; border-radius: 4px; transition: width 0.3s; display: flex; align-items: center; justify-content: flex-end; padding-right: 10px; color: white; font-weight: 600; font-size: 0.95em;"></div>
      </div>
    </div>
  </div>

  <div style="display: flex; gap: 1rem; justify-content: center; margin: 1.5rem 0;">
    <button onclick="voteFor('dice')" style="padding: 0.7rem 1.3rem; background: var(--mot-primary); color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Dadi</button>
    <button onclick="voteFor('coin')" style="padding: 0.7rem 1.3rem; background: #3a6b8c; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Moneta</button>
    <button onclick="voteFor('astro')" style="padding: 0.7rem 1.3rem; background: #999; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">Astrologia</button>
  </div>
  
  <p id="poll-stats" style="margin-top: 1.5rem; font-size: 0.55em; font-family: 'JetBrains Mono', monospace; font-weight: 600; color: var(--mot-primary); min-height: 1.8em;"></p>
</section>

---

<section class="mot-divider" data-background-color="#ed6f5c" data-transition="zoom" style="color: white;">
  <div id="particles-gioco" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10; color: white;">IL GIOCO</h1>
</section>

<section>
  <p class="mot-kicker">il lotto italiano</p>
  <h2>Giocare alla <em>lotteria</em></h2>
  <div class="mot-cols fragment" style="margin-top: 1.5rem;">
    <div class="mot-col">
      <p style="font-size: 0.9em;"><b>Numero totale:</b></p>
      <p class="mot-result">90 numeri</p>
    </div>
    <div class="mot-col">
      <p style="font-size: 0.9em;"><b>Numero estratto:</b></p>
      <p class="mot-result">1 numero</p>
    </div>
  </div>
  <p class="fragment" style="font-size: 0.85em; margin-top: 2rem;"><b>Qual è la probabilità che vinca il mio numero?</b></p>
  <p class="fragment mot-result">$$P(\text{vincere}) = \frac{1}{90} \approx 1.1\%$$</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">È più probabile che il tuo cognato ti presti soldi</p>
</section>

<section>
  <p class="mot-kicker">il gioco della roulette</p>
  <h2>Una <em>roulette</em> equa?</h2>
  <p class="mot-def fragment">La roulette francese ha 37 numeri (0–36). Se punti su un numero:</p>
  <div class="fragment" style="margin: 1.5rem 0;">
    <p class="mot-result" style="font-size: 1.1em">$$P(\text{vinci}) = \frac{1}{37} \approx 2.7\%$$</p>
    <p style="font-size: 0.9em; margin-top: 0.5rem;">Ma se vinci, il casinò ti paga solo 35 volte la puntata!</p>
  </div>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1.5rem;"><b>Dovrebbe pagarti 36 volte</b> (37 − 1 per la puntata). Lui ne paga solo 35. Ecco il guadagno del casinò!</p>
  <p class="mot-joke fragment" style="margin-top: 1rem;">Il casinò non è truccato. È matematicamente sleale.</p>
</section>

<section>
  <p class="mot-kicker">value & risk</p>
  <h2>Il <em>valore atteso</em> di un gioco</h2>
  <p class="mot-def fragment">Il valore atteso è quanto <b>ci aspettiamo di guadagnare (o perdere) in media</b> da un gioco.</p>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1.5rem;">Esempio: punto 1 euro sulla roulette su un numero:</p>
  <div class="fragment" style="margin: 1.5rem 0; font-family: 'JetBrains Mono', monospace; font-size: 0.85em;">
    <p>Vinci (prob 1/37): guadagni 35 euro</p>
    <p>Perdi (prob 36/37): perdi 1 euro</p>
  </div>
  <p class="fragment mot-result">$$E = \frac{1}{37} \cdot 35 + \frac{36}{37} \cdot (-1) =$$</p>
  <p class="fragment mot-result">$$= \frac{35 - 36}{37} = -\frac{1}{37} \approx -0.027$$</p>
  <p class="fragment" style="font-size: 0.85em; margin-top: 1rem;">In media, <b>perdi 2.7 centesimi ogni volta</b> che punti 1 euro. Su 1000 scommesse: 27 euro in meno.</p>
</section>

<section>
  <p class="mot-kicker">il verdetto</p>
  <h2>Gioco <em>equo</em> vs gioco <em>truccato</em></h2>
  <div class="mot-cols fragment" style="margin-top: 1.5rem;">
    <div class="mot-col" style="border-left: 4px solid var(--mot-primary); padding-left: 1rem;">
      <p style="font-size: 0.9em; font-weight: 600; color: var(--mot-primary);">GIOCO EQUO</p>
      <p style="font-size: 0.8em; margin-top: 0.5rem;">Valore atteso = 0</p>
      <p style="font-size: 0.75em; color: #666;">Non si guadagna né si perde</p>
      <p style="font-size: 0.75em; color: #666; margin-top: 0.5rem;">Esempio: lanciare una moneta e scommettere</p>
    </div>
    <div class="mot-col" style="border-left: 4px solid #c2185b; padding-left: 1rem;">
      <p style="font-size: 0.9em; font-weight: 600; color: #c2185b;">GIOCO SLEALE</p>
      <p style="font-size: 0.8em; margin-top: 0.5rem;">Valore atteso < 0</p>
      <p style="font-size: 0.75em; color: #666;">Il banco ha vantaggio</p>
      <p style="font-size: 0.75em; color: #666; margin-top: 0.5rem;">Esempio: roulette, lotto, gratta e vinci</p>
    </div>
  </div>
</section>

---

<section class="mot-divider" data-background-color="#ed6f5c" data-transition="zoom" style="color: white;">
  <div id="particles-riassunto" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10; color: white;">IL RIASSUNTO</h1>
</section>

<section>
  <p class="mot-kicker">in breve</p>
  <h2>Tre lezioni dalla <em>probabilità</em></h2>
  <ol style="font-size: 0.95em; line-height: 1.8; text-align: left; display: inline-block;">
    <li class="fragment"><b>La probabilità misura la rarità:</b> da 0 (impossibile) a 1 (certo).</li>
    <li class="fragment"><b>I dadi e le monete sono equi:</b> tutti gli esiti hanno la stessa probabilità.</li>
    <li class="fragment"><b>Il valore atteso racconta la verità:</b> se è negativo, il gioco è contro di te. 📉</li>
  </ol>
  <p class="mot-joke fragment" style="margin-top: 2rem;">La buona notizia: la matematica non mente. La cattiva notizia: il casinò sa bene di mentire.</p>
</section>

<section class="mot-hero" data-background-color="#ed6f5c" data-transition="zoom" style="color: white;">
  <div id="particles-finale" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 style="font-size: 2.5em; color: white; position: relative; z-index: 10;">Il gioco è solo <em style="color: white; font-style: italic;">uno specchio</em></h1>
  <p style="font-size: 1.2em; margin-top: 1.5rem; color: white; position: relative; z-index: 10;">La probabilità ti insegna a <b>leggere il mondo</b>.</p>
  <p class="mot-meta" style="color: rgba(255,255,255,0.95); margin-top: 2rem; position: relative; z-index: 10;">Prossima lezione: Calcoliamo le probabilità sul serio</p>
</section>

---

<style>
@keyframes flip-coin {
  0% { transform: rotateY(0deg) rotateX(0deg); }
  50% { transform: rotateY(720deg) rotateX(180deg); }
  100% { transform: rotateY(1080deg) rotateX(360deg); }
}

@keyframes bounce-dice {
  0% { transform: translateY(0) rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
  25% { transform: translateY(-40px) rotateX(180deg) rotateY(180deg) rotateZ(90deg); }
  50% { transform: translateY(-70px) rotateX(360deg) rotateY(360deg) rotateZ(180deg); }
  75% { transform: translateY(-40px) rotateX(540deg) rotateY(540deg) rotateZ(270deg); }
  100% { transform: translateY(0) rotateX(720deg) rotateY(720deg) rotateZ(360deg); }
}

#dice-visual {
  display: inline-block;
  perspective: 1000px;
  font-weight: bold;
  font-size: 2.5em;
}

#dice-visual.rolling {
  animation: bounce-dice 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

#coin-visual {
  display: inline-block;
  perspective: 1000px;
  font-weight: bold;
  font-size: 2.8em;
}

#coin-visual.flipping {
  animation: flip-coin 0.8s ease-in-out;
}

.mot-hero h1 em,
.mot-hero .mot-tagline em {
  color: rgba(255,255,255,0.95);
  font-style: italic;
}

/* Particles bianchi su sfondo corallo */
.reveal section[data-background-color="#ed6f5c"] svg line,
.reveal section[data-background-color="#ed6f5c"] svg circle {
  stroke: rgba(255, 255, 255, 0.4) !important;
  fill: rgba(255, 255, 255, 0.2) !important;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>
<script>
// Particles bianchi su sfondo corallo
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
        outModes: { default: 'out' }
      }
    },
    interactivity: {
      events: { onHover: { enable: false }, onClick: { enable: false } }
    },
    detectRetina: true
  };
  
  // Circular trajectories
  config.particles.move.spin = { enable: true, acceleration: 0 };
  
  // Carica particles su tutti i div con sfondo corallo
  var particleIds = ['particles-prob-hero', 'particles-quando', 'particles-sondaggi', 'particles-gioco', 'particles-riassunto', 'particles-finale'];
  particleIds.forEach(function(id) {
    var elem = document.getElementById(id);
    if (elem) {
      tsParticles.load(id, config);
    }
  });
})();

// Sondaggio
let pollVotes = { dice: 0, coin: 0, astro: 0 };

function voteFor(option) {
  pollVotes[option]++;
  updatePoll();
}

function updatePoll() {
  const total = pollVotes.dice + pollVotes.coin + pollVotes.astro;
  if (total === 0) return;
  
  const pct = (val) => total > 0 ? Math.round((val / total) * 100) : 0;
  
  document.getElementById('bar-dice').style.width = (pct(pollVotes.dice) * 0.8) + '%';
  document.getElementById('bar-dice').textContent = pct(pollVotes.dice) + '%';
  
  document.getElementById('bar-coin').style.width = (pct(pollVotes.coin) * 0.8) + '%';
  document.getElementById('bar-coin').textContent = pct(pollVotes.coin) + '%';
  
  document.getElementById('bar-astro').style.width = (pct(pollVotes.astro) * 0.8) + '%';
  document.getElementById('bar-astro').textContent = pct(pollVotes.astro) + '%';
  
  const stats = `Voti totali: ${total} | Dadi: ${pollVotes.dice} (${pct(pollVotes.dice)}%) | Moneta: ${pollVotes.coin} (${pct(pollVotes.coin)}%) | Astrologia: ${pollVotes.astro} (${pct(pollVotes.astro)}%)`;
  document.getElementById('poll-stats').textContent = stats;
}

// Dado
document.getElementById('roll-btn').addEventListener('click', function() {
  const diceVisual = document.getElementById('dice-visual');
  const result = Math.floor(Math.random() * 6) + 1;
  
  diceVisual.classList.remove('rolling');
  void diceVisual.offsetWidth;
  diceVisual.classList.add('rolling');
  
  document.getElementById('dice-result').textContent = '';
  
  setTimeout(() => {
    diceVisual.classList.remove('rolling');
    document.getElementById('dice-result').textContent = 'Risultato: ' + result;
  }, 800);
});

// Moneta
document.getElementById('flip-btn').addEventListener('click', function() {
  const coinVisual = document.getElementById('coin-visual');
  const result = Math.random() > 0.5 ? 'Testa' : 'Croce';
  
  coinVisual.classList.remove('flipping');
  void coinVisual.offsetWidth;
  coinVisual.classList.add('flipping');
  
  document.getElementById('coin-result').textContent = '';
  
  setTimeout(() => {
    coinVisual.classList.remove('flipping');
    document.getElementById('coin-result').textContent = 'Risultato: ' + result;
  }, 800);
});
</script>

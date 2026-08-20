---
title: Calcolo Letterale
summary: Monomi, polinomi e prodotti notevoli — tema mathofthings
authors: [Diego Fantinelli]
tags: [algebra, monomi, polinomi]
categories: [lesson]
date: "2026-08-20T00:00:00Z"
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
  <p class="mot-kicker">matematica per il biennio</p>
  <h1>Calcolo <span class="math-word">Letterale</span></h1>
  <p class="mot-tagline">monomi, polinomi e prodotti <em>notevoli</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PERCHÉ LE LETTERE?</h1>
  <p class="mot-joke fragment">spoiler: per essere pigri in modo intelligente</p>
</section>

<section>
  <p class="mot-kicker">motivazione</p>
  <h2>Un conto che vale <em>sempre</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Se ho 3 sacchetti di mele e ne aggiungo altri 2, ho 5 sacchetti: ma quante mele ci sono in totale?</li>
    <li class="fragment" style="margin-bottom:0;">Dipende da quante mele ci sono in un sacchetto — un numero che non conosco ancora</li>
  </ul>
  <p class="mot-def fragment">Chiamando $x$ il numero di mele in un sacchetto, il totale è sempre $3x + 2x = 5x$, qualunque sia $x$.</p>
  <p class="mot-joke fragment">la lettera non è un mistero da risolvere: è un numero che aspetta solo di essere svelato</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MONOMI</h1>
</section>

<section>
  <p class="mot-kicker">definizione</p>
  <h2>Che cos'è un <em>monomio</em></h2>
  <p class="mot-def fragment">Un <b>monomio</b> è un'espressione formata dal prodotto di un numero (il <b>coefficiente</b>) e una o più lettere elevate a esponente naturale (la <b>parte letterale</b>).</p>
  <dl class="mot-rows fragment">
    <dt>esempio</dt><dd>$3x^2y$</dd>
    <dt>coefficiente</dt><dd>$3$</dd>
    <dt>parte letterale</dt><dd>$x^2y$</dd>
    <dt>grado</dt><dd>$2+1=3$</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">condizione</p>
  <h2>Monomi <em>simili</em></h2>
  <p class="mot-def fragment">Due monomi sono <b>simili</b> quando hanno la <b>stessa parte letterale</b>, indipendentemente dal coefficiente.</p>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">$5x^2y$ e $-2x^2y$ sono simili</li>
    <li class="fragment" style="margin-bottom:0;">$5x^2y$ e $5xy^2$ non lo sono: gli esponenti sono scambiati</li>
  </ul>
  <p class="mot-joke fragment">stessa maglietta, colore diverso: quello che conta è la taglia (la parte letterale)</p>
</section>

<section>
  <p class="mot-kicker">operazioni</p>
  <h2>Somma di monomi <em>simili</em></h2>
  <p class="fragment">Si sommano (o sottraggono) solo monomi simili: si sommano i coefficienti, la parte letterale resta invariata.</p>
  <p class="mot-result fragment">$4x^2 + 3x^2 = 7x^2$</p>
  <p class="fragment" style="font-size:0.8em">Monomi non simili, come $5x + 3y$, non si possono sommare in un solo termine: restano scritti come polinomio.</p>
</section>

<section>
  <p class="mot-kicker">operazioni</p>
  <h2>Prodotto e divisione tra monomi</h2>
  <p class="fragment">A differenza della somma, prodotto e divisione funzionano <b>anche tra monomi non simili</b>: si opera sui coefficienti e si sommano (o sottraggono) gli esponenti di ogni lettera.</p>
  <dl class="mot-rows fragment">
    <dt>prodotto</dt><dd>$2x^3 \cdot 3x^2 = 6x^5$</dd>
    <dt>divisione</dt><dd>$12x^5 : 4x^2 = 3x^3$</dd>
    <dt>potenza</dt><dd>$(2x^2)^3 = 8x^6$</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">POLINOMI</h1>
</section>

<section>
  <p class="mot-kicker">definizione</p>
  <h2>Che cos'è un <em>polinomio</em></h2>
  <p class="mot-def fragment">Un <b>polinomio</b> è una somma algebrica di monomi non tutti simili tra loro.</p>
  <dl class="mot-rows fragment">
    <dt>esempio</dt><dd>$3x^3 - 2x^2 + 5$</dd>
    <dt>grado del polinomio</dt><dd>il grado più alto tra i suoi monomi &mdash; qui $3$</dd>
    <dt>casi particolari</dt><dd>binomio (2 termini), trinomio (3 termini)</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">operazioni</p>
  <h2>Somma e sottrazione di <em>polinomi</em></h2>
  <p class="fragment">Si sommano (o sottraggono) i termini simili tra i due polinomi, uno per uno.</p>
  <p class="mot-result fragment">$(2x^2+3x) + (x^2-x) = 3x^2+2x$</p>
  <p class="fragment" style="font-size:0.8em">Nella sottrazione, si cambia segno a tutti i termini del secondo polinomio prima di sommare.</p>
</section>

<section>
  <p class="mot-kicker">operazioni</p>
  <h2>Prodotto tra <em>polinomi</em></h2>
  <p class="fragment">Un monomio per un polinomio: si distribuisce il monomio su ogni termine.</p>
  <p class="mot-result fragment">$2x(3x^2-4x+1) = 6x^3-8x^2+2x$</p>
  <p class="fragment">Un binomio per un binomio: ogni termine del primo moltiplica ogni termine del secondo.</p>
  <p class="mot-result fragment">$(x+2)(x+3) = x^2+5x+6$</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRODOTTI NOTEVOLI</h1>
  <p class="mot-joke fragment">scorciatoie legali per non sviluppare tutto a mano</p>
</section>

<section>
  <p class="mot-kicker">perché "notevoli"</p>
  <h2>Prodotti che si ripetono <em>sempre uguali</em></h2>
  <p class="fragment">Certi prodotti tra binomi seguono sempre lo stesso schema: impararlo a memoria fa risparmiare tempo e riduce gli errori di calcolo.</p>
  <p class="mot-joke fragment">non sono regole magiche: sono solo prodotti già svolti una volta per tutte</p>
</section>

<section>
  <p class="mot-kicker">1° prodotto notevole</p>
  <h2>Quadrato di un <em>binomio</em></h2>
  <p class="mot-result fragment">$$(a\pm b)^2 = a^2 \pm 2ab + b^2$$</p>
  <p class="fragment">Esempio: $(x+3)^2 = x^2+6x+9$.</p>
  <p class="fragment">Esempio con segno meno: $(2x-5)^2 = 4x^2-20x+25$.</p>
</section>

<section>
  <p class="mot-kicker">2° prodotto notevole</p>
  <h2>Somma per <em>differenza</em></h2>
  <p class="mot-result fragment">$$(a+b)(a-b) = a^2 - b^2$$</p>
  <p class="fragment">Esempio: $(x+4)(x-4) = x^2-16$.</p>
  <p class="mot-joke fragment">il doppio prodotto $2ab$ sparisce: si elimina da solo, cambiando segno</p>
</section>

<section>
  <p class="mot-kicker">3° prodotto notevole</p>
  <h2>Cubo di un <em>binomio</em></h2>
  <p class="mot-result fragment">$$(a\pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3$$</p>
  <p class="fragment">Esempio: $(x+1)^3 = x^3+3x^2+3x+1$.</p>
  <p class="fragment" style="font-size:0.8em">I segni si alternano quando il binomio è una differenza: $+,-,+,-$.</p>
</section>

<section>
  <p class="mot-kicker">un trucco pratico</p>
  <h2>Moltiplicare a <em>mente</em></h2>
  <p style="font-size: 2.2em; text-align: center; margin: 0.6em 0;">52 &times; 48 = <span class="mot-result">?</span></p>
  <p class="fragment">$52 \times 48 = (50+2)(50-2) = 50^2-2^2 = 2500-4 = 2496$.</p>
  <p class="mot-joke fragment">un prodotto notevole applicato bene batte una moltiplicazione a colonna</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOVE ANDIAMO</h1>
</section>

<section>
  <p class="mot-kicker">da qui in poi</p>
  <h2>Verso la <em>fattorizzazione</em></h2>
  <p class="fragment">Sviluppare un prodotto notevole è facile: il prossimo passo, più difficile, è il contrario &mdash; riconoscere un polinomio già sviluppato e riscriverlo come prodotto.</p>
  <p class="mot-joke fragment">spoiler: è la lezione dopo questa</p>
</section>

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon lavoro</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

---
title: La prima lezione di matematica
summary: Presentazione, regole del gioco e organizzazione dell'anno
authors: [Diego Fantinelli]
tags: [organizzazione, prima-lezione]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
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
  <p class="mot-kicker">inizio anno scolastico</p>
  <h1>La <em>prima</em> <span class="math-word">lezione</span> di matematica</h1>
  <p class="mot-tagline">la matematica non è imparare formule a memoria, ma collegare <em>concetti</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section id="menu" class="mot-divider" data-transition="zoom">
  <p class="mot-kicker">prima lezione dell'anno</p>
  <h1 class="r-fit-text">SCEGLI LA CLASSE</h1>
  <div class="mot-menu-cards">
    <a class="mot-menu-card" href="#/terze">
      <span class="mot-menu-card-num">3&ordf;</span>
      <span class="mot-menu-card-label">Terze</span>
    </a>
    <a class="mot-menu-card" href="#/quarte">
      <span class="mot-menu-card-num">4&ordf;</span>
      <span class="mot-menu-card-label">Quarte</span>
    </a>
    <a class="mot-menu-card" href="#/quinte">
      <span class="mot-menu-card-num">5&ordf;</span>
      <span class="mot-menu-card-label">Quinte</span>
    </a>
  </div>
</section>

---

<section id="terze" class="mot-divider" data-transition="zoom">
  <p class="mot-kicker">classe 3ª &mdash; <a href="#/menu" class="mono">torna alla scelta</a></p>
  <h1 class="r-fit-text">BENVENUTI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="fragment">Un primo giro di conoscenza: chi sono io, chi siete voi, da dove arrivate e cosa vi aspettate da quest'anno di matematica.</p>
  <p class="mot-joke fragment">niente paura, non c'è un'interrogazione nascosta in questa slide</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Il test d'<em>ingresso</em></h2>
  <p class="mot-def fragment">Si terrà nella mia ora, nelle prime settimane di lezione: verificheremo insieme il livello di partenza, senza ansie e senza voti che pesano.</p>
  <dl class="mot-rows fragment">
    <dt>argomenti</dt><dd>il programma dello scorso anno scolastico</dd>
    <dt>calcolo</dt><dd>operazioni, espressioni, proprietà delle potenze</dd>
    <dt>frazioni</dt><dd>operazioni con le frazioni</dd>
    <dt>geometria</dt><dd>nozioni di base</dd>
    <dt>proporzioni</dt><dd>proporzioni, percentuali</dd>
    <dt>problemi</dt><dd>semplici problemi applicativi</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">perché ci tengo al test d'ingresso</p>
  <h2>Statistiche sulle competenze <em>in ingresso</em></h2>
  <div class="mot-barchart">
    <div class="fragment mot-bar" style="--bar-color:#b3503f; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sotto le<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#d9a441; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">competenze<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#ed6f5c; --target:50%;">
      <div class="mot-bar-value">50%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sufficienti /<br>discrete</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#6f9e74; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">buone</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#c9a227; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">ottime /<br>eccellenti</div>
    </div>
  </div>
  <p class="mot-joke fragment" style="margin-top: 1.5rem;">un quarto della classe parte già sotto soglia — è per questo che il test non è una formalità</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti</dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">un quaderno diviso in due parti (o due quaderni): lezioni ed esercizi</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti sul testo</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <b>abilità</b> sono la capacità di applicare le conoscenze apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <b>competenze</b> sono la capacità di unire conoscenze, abilità e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>La verifica <em>scritta</em></h2>
  <ul class="fragment">
    <li class="fragment">una verifica per ogni modulo/argomento</li>
    <li class="fragment"><a href="/uploads/verifiche/LB01-insiemi.pdf" target="_blank" class="mono">esempio di verifica</a></li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> come viene calcolato il punteggio e come si trasforma nel voto finale?</p>
  <p class="mot-def fragment"><b>R:</b> è un algoritmo che tiene conto di diverse variabili.</p>
  <dl class="mot-rows fragment">
    <dt>1</dt><dd>livello di assimilazione dell'argomento</dd>
    <dt>2</dt><dd>capacità di ragionamento</dd>
    <dt>3</dt><dd>capacità di calcolo</dd>
    <dt>4</dt><dd>ordine</dd>
    <dt>5</dt><dd>etc.</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment">
    <li class="fragment">interrogazione classica: volontaria e/o a sorpresa</li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata</li>
    <li class="fragment">test su Google Moduli</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">controllo quaderni</dt><dd class="fragment">garantisce continuità di impegno anche nel lavoro autonomo; i voti raccolti nel quadrimestre confluiscono in un voto per l'orale, a fine quadrimestre</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
  </dl>
</section>

---

<section>
  <h2>Lezioni <em>private</em></h2>
  <p class="fragment">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
</section>

<section class="mot-divider" data-transition="zoom" data-background-image="panic.jpg" data-background-opacity="0.2">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">le domande stupide non esistono. Le risposte, qualche volta.</p>
</section>



---

<section id="quarte" class="mot-divider" data-transition="zoom">
  <p class="mot-kicker">classe 4ª &mdash; <a href="#/menu" class="mono">torna alla scelta</a></p>
  <h1 class="r-fit-text">BENVENUTI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="fragment">Un primo giro di conoscenza: chi sono io, chi siete voi, da dove arrivate e cosa vi aspettate da quest'anno di matematica.</p>
  <p class="mot-joke fragment">niente paura, non c'è un'interrogazione nascosta in questa slide</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Il test d'<em>ingresso</em></h2>
  <p class="mot-def fragment">Si terrà nella mia ora, nelle prime settimane di lezione: verificheremo insieme il livello di partenza, senza ansie e senza voti che pesano.</p>
  <dl class="mot-rows fragment">
    <dt>argomenti</dt><dd>il programma dello scorso anno scolastico</dd>
    <dt>calcolo</dt><dd>operazioni, espressioni, proprietà delle potenze</dd>
    <dt>frazioni</dt><dd>operazioni con le frazioni</dd>
    <dt>geometria</dt><dd>nozioni di base</dd>
    <dt>proporzioni</dt><dd>proporzioni, percentuali</dd>
    <dt>problemi</dt><dd>semplici problemi applicativi</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">perché ci tengo al test d'ingresso</p>
  <h2>Statistiche sulle competenze <em>in ingresso</em></h2>
  <div class="mot-barchart">
    <div class="fragment mot-bar" style="--bar-color:#b3503f; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sotto le<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#d9a441; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">competenze<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#ed6f5c; --target:50%;">
      <div class="mot-bar-value">50%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sufficienti /<br>discrete</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#6f9e74; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">buone</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#c9a227; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">ottime /<br>eccellenti</div>
    </div>
  </div>
  <p class="mot-joke fragment" style="margin-top: 1.5rem;">un quarto della classe parte già sotto soglia — è per questo che il test non è una formalità</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti</dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">un quaderno diviso in due parti (o due quaderni): lezioni ed esercizi</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti sul testo</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <b>abilità</b> sono la capacità di applicare le conoscenze apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <b>competenze</b> sono la capacità di unire conoscenze, abilità e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>La verifica <em>scritta</em></h2>
  <ul class="fragment">
    <li class="fragment">una verifica per ogni modulo/argomento</li>
    <li class="fragment"><a href="/uploads/verifiche/LB01-insiemi.pdf" target="_blank" class="mono">esempio di verifica</a></li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> come viene calcolato il punteggio e come si trasforma nel voto finale?</p>
  <p class="mot-def fragment"><b>R:</b> è un algoritmo che tiene conto di diverse variabili.</p>
  <dl class="mot-rows fragment">
    <dt>1</dt><dd>livello di assimilazione dell'argomento</dd>
    <dt>2</dt><dd>capacità di ragionamento</dd>
    <dt>3</dt><dd>capacità di calcolo</dd>
    <dt>4</dt><dd>ordine</dd>
    <dt>5</dt><dd>etc.</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment">
    <li class="fragment">interrogazione classica: volontaria e/o a sorpresa</li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata</li>
    <li class="fragment">test su Google Moduli</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">controllo quaderni</dt><dd class="fragment">garantisce continuità di impegno anche nel lavoro autonomo; i voti raccolti nel quadrimestre confluiscono in un voto per l'orale, a fine quadrimestre</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
  </dl>
</section>

---

<section>
  <h2>Lezioni <em>private</em></h2>
  <p class="fragment">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
</section>

<section class="mot-divider" data-transition="zoom" data-background-image="panic.jpg" data-background-opacity="0.2">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">le domande stupide non esistono. Le risposte, qualche volta.</p>
</section>



---

<section id="quinte" class="mot-divider" data-transition="zoom">
  <p class="mot-kicker">classe 5ª &mdash; <a href="#/menu" class="mono">torna alla scelta</a></p>
  <h1 class="r-fit-text">BENVENUTI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="fragment">Un primo giro di conoscenza: chi sono io, chi siete voi, da dove arrivate e cosa vi aspettate da quest'anno di matematica.</p>
  <p class="mot-joke fragment">niente paura, non c'è un'interrogazione nascosta in questa slide</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Il test d'<em>ingresso</em></h2>
  <p class="mot-def fragment">Si terrà nella mia ora, nelle prime settimane di lezione: verificheremo insieme il livello di partenza, senza ansie e senza voti che pesano.</p>
  <dl class="mot-rows fragment">
    <dt>argomenti</dt><dd>il programma dello scorso anno scolastico</dd>
    <dt>calcolo</dt><dd>operazioni, espressioni, proprietà delle potenze</dd>
    <dt>frazioni</dt><dd>operazioni con le frazioni</dd>
    <dt>geometria</dt><dd>nozioni di base</dd>
    <dt>proporzioni</dt><dd>proporzioni, percentuali</dd>
    <dt>problemi</dt><dd>semplici problemi applicativi</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">perché ci tengo al test d'ingresso</p>
  <h2>Statistiche sulle competenze <em>in ingresso</em></h2>
  <div class="mot-barchart">
    <div class="fragment mot-bar" style="--bar-color:#b3503f; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sotto le<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#d9a441; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">competenze<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#ed6f5c; --target:50%;">
      <div class="mot-bar-value">50%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sufficienti /<br>discrete</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#6f9e74; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">buone</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#c9a227; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">ottime /<br>eccellenti</div>
    </div>
  </div>
  <p class="mot-joke fragment" style="margin-top: 1.5rem;">un quarto della classe parte già sotto soglia — è per questo che il test non è una formalità</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti</dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">un quaderno diviso in due parti (o due quaderni): lezioni ed esercizi</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti sul testo</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <b>abilità</b> sono la capacità di applicare le conoscenze apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <b>competenze</b> sono la capacità di unire conoscenze, abilità e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>La verifica <em>scritta</em></h2>
  <ul class="fragment">
    <li class="fragment">una verifica per ogni modulo/argomento</li>
    <li class="fragment"><a href="/uploads/verifiche/LB01-insiemi.pdf" target="_blank" class="mono">esempio di verifica</a></li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> come viene calcolato il punteggio e come si trasforma nel voto finale?</p>
  <p class="mot-def fragment"><b>R:</b> è un algoritmo che tiene conto di diverse variabili.</p>
  <dl class="mot-rows fragment">
    <dt>1</dt><dd>livello di assimilazione dell'argomento</dd>
    <dt>2</dt><dd>capacità di ragionamento</dd>
    <dt>3</dt><dd>capacità di calcolo</dd>
    <dt>4</dt><dd>ordine</dd>
    <dt>5</dt><dd>etc.</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment">
    <li class="fragment">interrogazione classica: volontaria e/o a sorpresa</li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata</li>
    <li class="fragment">test su Google Moduli</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows">
    <dt class="fragment">controllo quaderni</dt><dd class="fragment">garantisce continuità di impegno anche nel lavoro autonomo; i voti raccolti nel quadrimestre confluiscono in un voto per l'orale, a fine quadrimestre</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
  </dl>
</section>

---

<section>
  <h2>Lezioni <em>private</em></h2>
  <p class="fragment">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
</section>

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
.mot-menu-cards {
  display: flex;
  justify-content: center;
  gap: 1.6em;
  margin-top: 2rem;
  flex-wrap: wrap;
}

.mot-menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.4em;
  width: 190px;
  height: 190px;
  border: 2px solid var(--mot-border);
  border-radius: 14px;
  text-decoration: none;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.mot-menu-card:hover {
  transform: translateY(-4px);
  border-color: var(--mot-primary);
  background: rgba(237, 111, 92, 0.06);
}

.mot-menu-card-num {
  font-family: var(--mot-display);
  font-size: 2.6em;
  color: var(--mot-primary);
  line-height: 1;
}

.mot-menu-card-label {
  font-family: var(--mot-mono);
  font-size: 0.55em;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--mot-text);
}

.mot-barchart {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 2.2em;
  height: 260px;
  margin: 2rem auto 0;
  max-width: 700px;
}

.mot-bar {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  height: 100%;
}

.mot-bar-value {
  flex: 0 0 auto;
  font-family: var(--mot-mono);
  font-size: 0.55em;
  font-weight: 700;
  color: var(--bar-color);
  margin-bottom: 0.4em;
}

.mot-bar-col {
  flex: 1 1 auto;
  width: 100%;
  max-width: 64px;
  display: flex;
  align-items: flex-end;
  border-radius: 6px 6px 0 0;
  background: rgba(128, 128, 128, 0.1);
  overflow: hidden;
}

.mot-bar-fill {
  width: 100%;
  height: 0;
  background: var(--bar-color);
  border-radius: 6px 6px 0 0;
  transition: height 1s cubic-bezier(0.22, 0.9, 0.35, 1);
}

.mot-bar.visible .mot-bar-fill {
  height: var(--target);
}

.mot-bar-label {
  flex: 0 0 auto;
  font-family: var(--mot-mono);
  font-size: 0.4em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--mot-muted);
  text-align: center;
  margin-top: 0.6em;
  max-width: 90px;
  line-height: 1.3;
}
</style>

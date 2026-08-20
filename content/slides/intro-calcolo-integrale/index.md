---
title: Il Calcolo Integrale
summary: Aneddoti, paradossi e un po' di storia per il primo incontro con gli integrali
authors: [Diego Fantinelli]
tags: [analisi, integrali, quinto-anno]
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
  <p class="mot-kicker">quinto anno · primo incontro</p>
  <h1>Il Calcolo <span class="math-word">Integrale</span></h1>
  <p class="mot-tagline">storie, paradossi e un simbolo che <em>allunga la esse</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">UN'AREA STORTA</h1>
  <p class="mot-joke fragment">spoiler: c'entra un cerchio, ovviamente</p>
</section>

<section>
  <p class="mot-kicker">un problema antichissimo</p>
  <h2>Quanto è <em>grande</em> una forma storta?</h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Rettangolo, triangolo, cerchio: le sappiamo calcolare da millenni</li>
    <li class="fragment" style="margin-bottom:0.5em;">Ma l'area sotto una curva qualsiasi, una forma senza nome e senza formula?</li>
    <li class="fragment" style="margin-bottom:0;">Quella resiste per più di duemila anni</li>
  </ul>
  <p class="mot-joke fragment">la geometria classica sapeva misurare tutto, tranne le cose davvero interessanti</p>
</section>

<section>
  <p class="mot-kicker">il primo tentativo, 250 a.C.</p>
  <h2>Archimede e il <em>metodo di esaustione</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Inscrive e circoscrive poligoni con sempre più lati: triangoli, poi esagoni, poi poligoni a 96 lati</li>
    <li class="fragment" style="margin-bottom:0.5em;">Più lati aggiunge, più il poligono "esaurisce" lo spazio dentro il cerchio</li>
    <li class="fragment" style="margin-bottom:0;">È già l'idea di oggi: <b>approssimare una forma curva con tanti pezzi dritti</b>, e vedere cosa succede quando i pezzi diventano infiniti</li>
  </ul>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DUE GENI, UNA LITE</h1>
  <p class="mot-joke fragment">la peggiore rissa accademica della storia della matematica</p>
</section>

<section>
  <p class="mot-kicker">1660 circa, due paesi diversi</p>
  <h2>Newton e <em>Leibniz</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Duemila anni dopo Archimede, due uomini — in Inghilterra e in Germania, senza sapere l'uno dell'altro</li>
    <li class="fragment" style="margin-bottom:0.5em;">Arrivano quasi insieme a un'idea rivoluzionaria: calcolare aree e calcolare pendenze (le derivate) sono <b>due facce dello stesso problema</b></li>
    <li class="fragment" style="margin-bottom:0;">Questo collegamento si chiama oggi <b>Teorema fondamentale del calcolo</b>, e lo vedremo tra poco</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">una polemica durata decenni</p>
  <h2>Chi lo ha <em>inventato</em> per primo?</h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Newton lo sviluppa prima (1666), ma lo pubblica dopo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Leibniz lo pubblica prima (1684), con una notazione più chiara</li>
    <li class="fragment" style="margin-bottom:0;">Ne segue una delle liti accademiche più feroci della storia: accuse di plagio, lettere anonime, un'intera nazione contro l'altra</li>
  </ul>
  <p class="mot-joke fragment">morale: anche i geni, a volte, litigano come bambini per un giocattolo</p>
</section>

<section>
  <p class="mot-kicker">chi ha vinto, alla fine?</p>
  <h2>Il simbolo che <em>usiamo ancora</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Sul piano storico, la disputa non ha mai avuto un vero vincitore: oggi si riconosce che entrambi arrivarono all'idea in modo indipendente</li>
    <li class="fragment" style="margin-bottom:0;">Ma sul piano pratico un vincitore c'è: la notazione che usiamo ancora oggi, <span class="math-word">$\int$</span>, è quella di Leibniz — una <b>S allungata</b>, iniziale di <i>Summa</i>, "somma" in latino</li>
  </ul>
  <p class="mot-joke fragment">la S allungata vince sempre, anche sui geni</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">UNA S CHE SOMMA</h1>
</section>

<section>
  <p class="mot-kicker">il simbolo spiegato</p>
  <h2>Perché una <em>esse</em>?</h2>
  <p class="mot-def fragment">$\int$ è una S stilizzata: sta per <b>Summa</b>, perché integrare significa <b>sommare</b> infinite quantità piccolissime — proprio come nell'idea di Archimede, portata all'estremo.</p>
  <dl class="mot-rows fragment">
    <dt>oggi diciamo</dt><dd>somma di rettangoli infinitamente sottili</dd>
    <dt>Leibniz diceva</dt><dd>somma di infinitesimi</dd>
    <dt>il simbolo</dt><dd>$\displaystyle\int_a^b f(x)\,dx$</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">un'analogia quotidiana</p>
  <h2>La <em>velocità</em> che diventa strada</h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Il tachimetro dell'auto misura la velocità istante per istante</li>
    <li class="fragment" style="margin-bottom:0.5em;">Se sommi (integri) tutte quelle velocità nel tempo, ottieni la distanza percorsa</li>
    <li class="fragment" style="margin-bottom:0;">È esattamente quello che fa il contachilometri, senza che tu te ne accorga</li>
  </ul>
  <p class="mot-joke fragment">ogni volta che guidi, il tuo cruscotto sta facendo un integrale in tempo reale</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">UN PARADOSSO CHE INQUIETA</h1>
</section>

<section>
  <p class="mot-kicker">2400 anni fa, un rompicapo mai davvero risolto</p>
  <h2>Achille e la <em>tartaruga</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Zenone di Elea immagina una gara: Achille, velocissimo, dà un vantaggio alla tartaruga, lentissima</li>
    <li class="fragment" style="margin-bottom:0.5em;">Per raggiungerla deve prima arrivare dove lei era; nel frattempo lei si è già spostata un po' più avanti. E così all'infinito</li>
    <li class="fragment" style="margin-bottom:0;">Conclusione (apparentemente logica, e assurda): Achille non raggiunge mai la tartaruga</li>
  </ul>
  <p class="mot-joke fragment">chiunque abbia corso i 100 metri sa che Achille vince facile: il problema è nella matematica, non nella gara</p>
</section>

<section>
  <p class="mot-kicker">la soluzione, arrivata secoli dopo</p>
  <h2>Infiniti passi, tempo <em>finito</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Il trucco è che infiniti intervalli di tempo, sempre più piccoli, possono comunque sommarsi a un totale <b>finito</b></li>
    <li class="fragment" style="margin-bottom:0;">È esattamente il tipo di somma infinita che il calcolo integrale sa gestire con precisione</li>
  </ul>
  <p class="mot-def fragment">Non serviva più veloce: serviva un modo nuovo di pensare all'infinito.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOVE ANDIAMO</h1>
</section>

<section>
  <p class="mot-kicker">da qui in poi</p>
  <h2>Dalla storia ai <em>conti</em></h2>
  <p class="fragment">Basta aneddoti: nella lezione che segue vediamo come si calcola davvero un integrale — dalla primitiva alle prime regole, fino all'area sotto una curva.</p>
  <p class="mot-joke fragment">niente tartarughe, promesso. O quasi.</p>
</section>

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon inizio</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

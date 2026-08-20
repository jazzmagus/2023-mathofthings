---
title: Equazioni Differenziali
summary: Come cambia nel tempo — tema mathofthings
authors: [Diego Fantinelli]
tags: [analisi, equazioni differenziali, corso pro]
categories: [lesson]
date: "2026-07-27T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
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
  <p class="mot-kicker">quinto anno · corso pro</p>
  <h1>Equazioni <span class="math-word">Differenziali</span></h1>
  <p class="mot-tagline">non "quanto vale", ma <em>quanto velocemente cambia</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <blockquote class="mot-quote">
    Le leggi della natura sono scritte nel linguaggio della matematica, e i suoi caratteri sono... equazioni differenziali.
    <span class="quote-attr">&mdash; liberamente da Galileo e Newton</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">UNA DOMANDA DIVERSA</h1>
</section>

<section>
  <p class="mot-kicker">finora</p>
  <h2>Equazioni con incognita un <em>numero</em></h2>
  <p class="mot-def fragment">In \(2x+3=7\), l'incognita \(x\) è un numero. Anche in \(x^2-4x+3=0\) cerchiamo numeri.</p>
  <p class="fragment" style="font-size:0.8em">E se l'incognita fosse una <b>funzione</b>? E se l'equazione legasse quella funzione al suo <b>ritmo di cambiamento</b>?</p>
</section>

<section>
  <p class="mot-kicker">l'idea centrale</p>
  <h2>Leggi che parlano di <em>variazione</em></h2>
  <p class="mot-def fragment">La velocità con cui una popolazione cresce dipende da quanti individui ci sono <b>già</b>. La velocità con cui un corpo si raffredda dipende da <b>quanto</b> è più caldo dell'ambiente.</p>
  <p class="mot-joke fragment">non leggi statiche, ma leggi che si "guardano allo specchio"</p>
</section>

<section>
  <p class="mot-kicker">definizione</p>
  <h2>Equazione <em>differenziale</em></h2>
  <p class="mot-def fragment">Un'equazione che lega una funzione incognita \(y(x)\) alle sue derivate:</p>
  <p class="mot-result fragment">$$y' = f(x,y)$$</p>
  <p class="fragment" style="font-size:0.76em">Risolverla non significa trovare un numero, ma <b>ritrovare l'intera funzione</b> a partire dal suo tasso di variazione.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">SEPARARE LE VARIABILI</h1>
</section>

<section>
  <p class="mot-kicker">il caso più semplice</p>
  <h2>Quando \(x\) e \(y\) si <em>separano</em></h2>
  <p class="mot-def fragment">Se l'equazione ha la forma \(y'=g(x)\,h(y)\), si può "smontare" mettendo tutte le \(y\) da un lato e tutte le \(x\) dall'altro:</p>
  <p class="mot-result fragment">$$\int\frac{dy}{h(y)} = \int g(x)\,dx$$</p>
</section>

<section>
  <p class="mot-kicker">esempio</p>
  <h2>Risolvere \(y'=xy\)</h2>
  <p class="mot-def fragment" style="font-size:0.8em">Separando: \(\dfrac{dy}{y}=x\,dx\), quindi \(\ln|y|=\dfrac{x^2}{2}+c\).</p>
  <p class="mot-result fragment">$$y(x) = C\,e^{x^2/2}$$</p>
  <p class="mot-joke fragment">infinite curve, una famiglia intera di soluzioni</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">CRESCITA E DECADIMENTO</h1>
</section>

<section>
  <p class="mot-kicker">il modello più famoso</p>
  <h2>Quando il ritmo è <em>proporzionale</em></h2>
  <p class="mot-def fragment">Se la velocità di variazione è proporzionale alla quantità stessa, \(y'=ky\), la soluzione è sempre la stessa forma:</p>
  <p class="mot-result fragment">$$y(t) = y_0\,e^{kt}$$</p>
  <p class="fragment" style="font-size:0.76em">Popolazioni che crescono (\(k>0\)), sostanze radioattive che decadono (\(k<0\)): stessa equazione, segno diverso.</p>
</section>

<section>
  <p class="mot-kicker">applicazione</p>
  <h2>Il tempo di <em>dimezzamento</em></h2>
  <p class="mot-def fragment">Per il decadimento radioattivo \(N(t)=N_0e^{-\lambda t}\), il tempo perché la quantità si dimezzi è:</p>
  <p class="mot-result fragment">$$t_{1/2} = \frac{\ln 2}{\lambda}$$</p>
  <p class="mot-joke fragment">la base della datazione al carbonio-14</p>
</section>

<section>
  <p class="mot-kicker">una legge nota</p>
  <h2>Il raffreddamento di <em>Newton</em></h2>
  <p class="mot-def fragment" style="font-size:0.85em">Un corpo si raffredda con velocità proporzionale al <b>divario</b> con la temperatura ambiente, non alla temperatura stessa:</p>
  <p class="mot-result fragment" style="font-size:0.85em">$$T(t) = T_{amb} + (T_0-T_{amb})\,e^{-kt}$$</p>
  <p class="fragment" style="font-size:0.76em">Per \(t\to\infty\), \(T(t)\to T_{amb}\): il caffè, prima o poi, raggiunge sempre la temperatura della stanza.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">IL FATTORE INTEGRANTE</h1>
</section>

<section>
  <p class="mot-kicker">un caso più generale</p>
  <h2>Equazioni <em>lineari</em> del primo ordine</h2>
  <p class="mot-def fragment">Non sempre l'equazione si separa. La forma generale lineare è:</p>
  <p class="mot-result fragment">$$y' + p(x)\,y = q(x)$$</p>
  <p class="fragment" style="font-size:0.76em">Serve un trucco: moltiplicare tutto per una funzione scelta ad arte.</p>
</section>

<section>
  <p class="mot-kicker">il trucco</p>
  <h2>Trasformare il primo membro in una <em>derivata</em></h2>
  <p class="mot-def fragment" style="font-size:0.78em">Con \(\mu(x)=e^{\int p(x)dx}\), il primo membro diventa la derivata di un prodotto:</p>
  <p class="mot-result fragment" style="font-size:0.85em">$$(\mu\,y)' = \mu\,q$$</p>
  <p class="fragment" style="font-size:0.76em">Da qui basta integrare: un'equazione difficile diventa un calcolo di primitive.</p>
</section>

<section>
  <p class="mot-kicker">sorpresa</p>
  <h2>Newton era già un caso <em>particolare</em></h2>
  <p class="mot-def fragment">Applicando il fattore integrante alla legge di raffreddamento (\(p\) e \(q\) costanti), si ritrova esattamente la stessa soluzione trovata separando le variabili.</p>
  <p class="mot-joke fragment">due strade diverse, stessa destinazione</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">IL PROBLEMA DI CAUCHY</h1>
</section>

<section>
  <p class="mot-kicker">quale curva, tra infinite?</p>
  <h2>La condizione <em>iniziale</em></h2>
  <p class="mot-def fragment">L'integrale generale contiene una costante libera: infinite soluzioni. Per sceglierne una, basta un punto:</p>
  <p class="mot-result fragment" style="font-size:0.85em">$$\begin{cases} y'=f(x,y) \\ y(x_0)=y_0 \end{cases}$$</p>
</section>

<section>
  <p class="mot-kicker">un fatto notevole</p>
  <h2>Curve che non si <em>incrociano</em> mai</h2>
  <p class="mot-def fragment">Sotto ipotesi ragionevoli su \(f\), da ogni punto del piano passa <b>una sola</b> curva integrale.</p>
  <p class="fragment" style="font-size:0.78em">Due soluzioni distinte della stessa equazione non si toccano mai: è il teorema di esistenza e unicità.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOVE VIVONO QUESTE EQUAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">elettronica</p>
  <h2>Il circuito <em>RC</em></h2>
  <p class="mot-def fragment" style="font-size:0.85em">La carica di un condensatore soddisfa \(R\dot q + q/C = V_0\): stessa struttura lineare, stessa forma di soluzione.</p>
  <p class="mot-result fragment" style="font-size:0.85em">$$q(t) = CV_0\left(1-e^{-t/RC}\right)$$</p>
</section>

<section>
  <p class="mot-kicker">meccanica</p>
  <h2>Caduta con <em>attrito</em></h2>
  <p class="mot-def fragment">Con resistenza dell'aria proporzionale alla velocità, esiste una <b>velocità limite</b>: il corpo smette di accelerare, molto prima di toccare terra.</p>
  <p class="mot-joke fragment">perché un paracadutista non accelera all'infinito</p>
</section>

<section>
  <p class="mot-kicker">il filo che le unisce</p>
  <h2>Sempre la stessa <em>forma</em></h2>
  <p class="mot-def fragment" style="font-size:0.82em">Condensatore, caduta con attrito, raffreddamento: fenomeni diversissimi, stessa equazione. Un sistema che si avvicina esponenzialmente a un equilibrio.</p>
  <p class="mot-joke fragment">riconoscere la stessa forma sotto vesti diverse: il cuore della matematica applicata</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">OLTRE QUESTA INTRODUZIONE</h1>
</section>

<section>
  <p class="mot-kicker">uno sguardo avanti</p>
  <h2>Ordini <em>superiori</em> e sistemi</h2>
  <p class="mot-def fragment" style="font-size:0.8em">L'oscillatore armonico \(y''+\omega^2y=0\), i sistemi preda-predatore, le equazioni alle derivate parziali di calore e onde: tutto nasce dalla stessa idea di partenza.</p>
</section>

<section>
  <p class="mot-kicker">per chiudere</p>
  <h2>Non leggi statiche, ma leggi di <em>cambiamento</em></h2>
  <p class="mot-def fragment">Dalla meccanica di Newton all'equazione di Schrödinger, le leggi fondamentali della fisica sono quasi sempre equazioni differenziali.</p>
  <p class="mot-joke fragment">la natura non dice "come sei", dice "come cambi"</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">se la risposta cresce esponenzialmente, va bene lo stesso</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

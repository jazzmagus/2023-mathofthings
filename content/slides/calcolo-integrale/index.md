---
title: Il Calcolo Integrale
summary: Dalla primitiva al teorema fondamentale — tema mathofthings
authors: [Diego Fantinelli]
tags: [analisi, integrali, calcolo integrale]
categories: [lesson]
date: "2026-07-10T00:00:00Z"
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
  <p class="mot-kicker">quinto anno · avanzato</p>
  <h1>Il Calcolo <span class="math-word">Integrale</span></h1>
  <p class="mot-tagline">dalla domanda inversa della derivata all'<em>area sotto una curva</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <blockquote class="mot-quote">
    Chi ignora la matematica non può conoscere le altre scienze né le cose di questo mondo.
    <span class="quote-attr">&mdash; Ruggero Bacone</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA DOMANDA INVERSA</h1>
</section>

<section>
  <p class="mot-kicker">ripartiamo dalle derivate</p>
  <h2>E se andassimo <em>all'indietro</em>?</h2>
  <p class="mot-def fragment">Sappiamo partire da \(f(x)\) e calcolare \(f'(x)\). Ma se conoscessimo \(f'(x)\) e volessimo <b>risalire</b> a \(f(x)\)?</p>
  <p class="fragment" style="font-size:0.78em">È la stessa domanda che si pone la fisica: conosco la <b>velocità</b> istante per istante, voglio ricostruire la <b>posizione</b>.</p>
</section>

<section>
  <p class="mot-kicker">definizione</p>
  <h2>La <em>primitiva</em></h2>
  <p class="mot-def fragment">\(F(x)\) è una primitiva di \(f(x)\) se, per ogni \(x\):</p>
  <p class="mot-result fragment">$$F'(x) = f(x)$$</p>
  <p class="fragment" style="font-size:0.78em">Esempio: se \(f(x)=2x\), allora \(F(x)=x^2\) è una primitiva, perché \((x^2)'=2x\).</p>
</section>

<section>
  <p class="mot-kicker">un dettaglio cruciale</p>
  <h2>Infinite <em>primitive</em></h2>
  <p class="mot-def fragment">Se \(F(x)\) è una primitiva di \(f(x)\), anche \(F(x)+c\) lo è, per <b>qualunque</b> costante \(c\).</p>
  <ul style="font-size:0.78em">
    <li class="fragment" style="margin-bottom:0.5em;">La derivata di una costante è zero: aggiungere \(c\) non cambia \(F'(x)\)</li>
    <li class="fragment" style="margin-bottom:0;">Tutte le primitive di \(f\) differiscono solo per una costante additiva</li>
  </ul>
  <p class="mot-joke fragment">infinite curve, tutte "parallele" tra loro</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">L'INTEGRALE INDEFINITO</h1>
</section>

<section>
  <p class="mot-kicker">la notazione di Leibniz</p>
  <h2>Il simbolo \(\int\)</h2>
  <p class="mot-def fragment">L'insieme di <b>tutte</b> le primitive di \(f(x)\) si chiama integrale indefinito:</p>
  <p class="mot-result fragment">$$\int f(x)\,dx = F(x)+c$$</p>
  <p class="fragment" style="font-size:0.74em">La "S" allungata di \(\int\) non è un caso: ricorda una <b>somma</b>. Lo capiremo tra poco.</p>
</section>

<section>
  <p class="mot-kicker">tabella essenziale</p>
  <h2>Integrali <em>immediati</em></h2>
  <div class="mot-cols">
    <div class="mot-col fragment" style="font-size:0.62em">
      <p>\(\displaystyle\int x^n dx = \frac{x^{n+1}}{n+1}+c\)</p>
      <p>\(\displaystyle\int \frac1x dx = \ln|x|+c\)</p>
      <p>\(\displaystyle\int e^x dx = e^x+c\)</p>
    </div>
    <div class="mot-col fragment" style="font-size:0.62em">
      <p>\(\displaystyle\int \sin x\,dx = -\cos x+c\)</p>
      <p>\(\displaystyle\int \cos x\,dx = \sin x+c\)</p>
      <p>\(\displaystyle\int \frac{1}{1+x^2}dx = \arctan x+c\)</p>
    </div>
  </div>
  <p class="mot-joke fragment">la tabella delle derivate, letta al contrario</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">TRE METODI</h1>
</section>

<section>
  <p class="mot-kicker">metodo 1</p>
  <h2>Per <em>sostituzione</em></h2>
  <p class="mot-def fragment">Cambiamo variabile: posto \(t=g(x)\), l'integrale complicato in \(x\) diventa immediato in \(t\).</p>
  <p class="mot-result fragment">$$\int f(g(x))\,g'(x)\,dx = \int f(t)\,dt$$</p>
  <p class="fragment" style="font-size:0.72em">Esempio: \(\displaystyle\int x\,e^{x^2}dx\), con \(t=x^2\), diventa \(\displaystyle\frac12\int e^t dt = \frac12 e^{x^2}+c\).</p>
</section>

<section>
  <p class="mot-kicker">metodo 2</p>
  <h2>Per <em>parti</em></h2>
  <p class="mot-def fragment">Nasce dalla derivata del prodotto: utile quando l'integrando è un prodotto di funzioni "diverse tra loro".</p>
  <p class="mot-result fragment">$$\int f\,g'\,dx = f\,g - \int f'\,g\,dx$$</p>
  <p class="fragment" style="font-size:0.72em">Esempio: \(\displaystyle\int x\,e^x dx = x e^x - \int e^x dx = (x-1)e^x + c\).</p>
</section>

<section>
  <p class="mot-kicker">metodo 3</p>
  <h2>Funzioni razionali <em>fratte</em></h2>
  <p class="mot-def fragment">Per \(\displaystyle\int \frac{N(x)}{ax^2+bx+c}dx\), tutto dipende dal discriminante del denominatore.</p>
  <dl class="mot-rows fragment" style="font-size:0.68em">
    <dt>\(\Delta>0\)</dt><dd>si scompone in fratti semplici, con logaritmi</dd>
    <dt>\(\Delta=0\)</dt><dd>radice doppia: fratti semplici con potenza al denominatore</dd>
    <dt>\(\Delta<0\)</dt><dd>si riconduce alla forma dell'arcotangente</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">L'INTEGRALE DEFINITO</h1>
</section>

<section>
  <p class="mot-kicker">cambiamo prospettiva</p>
  <h2>L'area sotto una <em>curva</em></h2>
  <p class="mot-def fragment">Vogliamo l'area tra il grafico di \(f(x)\geq0\), l'asse \(x\), e le rette \(x=a\), \(x=b\).</p>
  <p class="fragment" style="font-size:0.76em">Idea di Riemann: approssimare l'area con tanti rettangolini sottili, e vedere cosa succede quando il loro numero tende all'infinito.</p>
</section>

<section>
  <p class="mot-kicker">la somma diventa un limite</p>
  <h2>Le somme di <em>Riemann</em></h2>
  <p class="mot-def fragment" style="font-size:0.7em">Divido \([a,b]\) in \(n\) parti uguali, base \(\Delta x\), e sommo le aree dei rettangoli:</p>
  <img class="mot-frame fragment" src="riemann.png" alt="Somma di Riemann: rettangoli che approssimano l'area sotto la curva" style="max-height:15vh; margin:0.2em auto; display:block;">
  <p class="mot-result fragment" style="font-size:0.7em">$$S_n = \sum_{i=1}^{n} f(x_i)\,\Delta x \quad\longrightarrow\quad \int_a^b f(x)\,dx$$</p>
</section>

<section>
  <p class="mot-kicker">attenzione</p>
  <h2>Area con <em>segno</em></h2>
  <p class="mot-def fragment">Se \(f(x)<0\), i rettangoli contribuiscono <b>negativamente</b>.</p>
  <p class="fragment" style="font-size:0.78em">L'integrale definito non misura un'area "assoluta", ma un'area <b>con segno</b>: positiva sopra l'asse \(x\), negativa sotto.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">IL TEOREMA FONDAMENTALE</h1>
</section>

<section>
  <p class="mot-kicker">il ponte tra due mondi</p>
  <h2>Derivata e <em>integrale</em>: operazioni inverse</h2>
  <p class="mot-def fragment" style="font-size:0.7em">Il teorema fondamentale del calcolo collega l'integrale definito alle primitive.</p>
  <img class="mot-frame fragment" src="tfc.png" alt="Area sotto la curva tra a e b, pari a F(b) meno F(a)" style="max-height:15vh; margin:0.2em auto; display:block;">
  <p class="mot-result fragment" style="font-size:0.68em">$$\int_a^b f(x)\,dx = F(b)-F(a)$$</p>
</section>

<section>
  <p class="mot-kicker">perché funziona</p>
  <h2>La costante che <em>si cancella</em></h2>
  <p class="mot-def fragment">Con \(F(x)+c\) al posto di \(F(x)\): \(\big[F(b)+c\big]-\big[F(a)+c\big] = F(b)-F(a)\).</p>
  <p class="fragment" style="font-size:0.78em">La costante scompare sempre: per un integrale definito basta <b>una qualsiasi</b> primitiva.</p>
  <p class="mot-joke fragment">Torricelli e Barrow lo intuirono prima ancora di Newton e Leibniz</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">APPLICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">tra due grafici</p>
  <h2>Area tra due <em>curve</em></h2>
  <p class="mot-def fragment">Se \(f(x)\geq g(x)\) su \([a,b]\):</p>
  <p class="mot-result fragment">$$A = \int_a^b \big[f(x)-g(x)\big]\,dx$$</p>
  <p class="fragment" style="font-size:0.72em">Se le curve si incrociano, si spezza l'integrale nei punti di intersezione — altrimenti le aree si cancellerebbero a vicenda.</p>
</section>

<section>
  <p class="mot-kicker">dal piano allo spazio</p>
  <h2>Volumi di <em>rotazione</em></h2>
  <p class="mot-def fragment">Ruotando il grafico di \(f(x)\geq0\) attorno all'asse \(x\), il metodo dei dischi dà:</p>
  <p class="mot-result fragment">$$V = \pi\int_a^b \big[f(x)\big]^2\,dx$$</p>
  <p class="fragment" style="font-size:0.74em">Ogni fettina infinitesima è un cilindro di raggio \(f(x)\): sommando tutte le fettine si ottiene il volume del solido.</p>
</section>

<section>
  <p class="mot-kicker">verifica sorprendente</p>
  <h2>Il volume della <em>sfera</em></h2>
  <p class="mot-def fragment">Ruotando il quarto di cerchio \(f(x)=\sqrt{r^2-x^2}\) su \([0,r]\) si genera una semisfera.</p>
  <p class="mot-result fragment">$$V = \pi\int_0^r (r^2-x^2)\,dx = \frac23\pi r^3 \ \Rightarrow\ V_{\text{sfera}}=\frac43\pi r^3$$</p>
  <p class="mot-joke fragment">la formula che hai sempre usato a memoria, finalmente dimostrata</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">se la risposta tende a infinito, va bene lo stesso</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

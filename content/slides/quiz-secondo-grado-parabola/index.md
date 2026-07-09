---
title: Quiz — Equazioni, Disequazioni di Secondo Grado e Parabola
summary: Gioco a premi — terzo anno, corso base (Base / Avanzato / Pro)
authors: [Diego Fantinelli]
tags: [secondo-grado, parabola, quiz]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">gioco a premi — terzo anno</p>
  <h1>Chi Vuol Essere <span class="math-word">Parabolico</span>?</h1>
  <p class="mot-tagline">30 domande, 3 livelli, e una parabola che non perdona</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-background-image="start-here-bkg.jpg" data-background-opacity="0.15" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">PRONTI?</h1>
  <p class="mot-joke fragment">tre livelli affiancati: Base, Avanzato, Pro &mdash; la parabola vi guarda dall'alto</p>
</section>

---

<section class="mot-divider mot-level-base" data-transition="zoom">
  <p class="mot-kicker">livello 1</p>
  <h1 class="r-fit-text">BASE</h1>
  <p class="mot-joke fragment">radici semplici, raccoglimento e qualche prodotto notevole</p>
</section>

<section>
  <p class="mot-kicker">base — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Una differenza di quadrati, direttamente al secondo grado.</h2>
  <p class="mot-quiz-expr">$$x^2-9=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — x²=9 ha due soluzioni opposte: x=3 e x=-3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=\pm3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai dimenticato di fare la radice quadrata: x²=9 non significa x=9." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=9$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Manca la soluzione negativa: anche x=-3 soddisfa l'equazione, il quadrato cancella il segno." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Niente termine noto: basta un raccoglimento a fattor comune.</h2>
  <p class="mot-quiz-expr">$$x^2-5x=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli x: x(x-5)=0, quindi x=0 oppure x=5. Un'equazione spuria non va mai divisa per x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=0,\ x=5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai perso la soluzione x=0 dividendo tutto per x: mossa vietata, si perdono radici." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=5$ (solo)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Occhio al segno: x(x-5)=0 dà x=5, non x=-5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=0,\ x=-5$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Somma e prodotto, ma stavolta il secondo grado &egrave; dichiarato apertamente.</h2>
  <p class="mot-quiz-expr">$$x^2-4x+3=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 1+3=4 e 1·3=3: le radici sono 1 e 3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=1,\ x=3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="-4 e -3 sommati non fanno 4, e il prodotto neppure torna: coppia sbagliata." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=-1,\ x=-3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="1·4=4, non 3: il prodotto non corrisponde al termine noto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=1,\ x=4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">La caccia alla coppia perfetta continua.</h2>
  <p class="mot-quiz-expr">$$x^2-7x+12=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 3+4=7 e 3·4=12: bersaglio centrato." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=3,\ x=4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="1+12=13, non 7: la somma non torna, per quanto il prodotto sia giusto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=1,\ x=12$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Segno sbagliato: con due numeri negativi la somma sarebbe -7, non +7." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=-3,\ x=-4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Un'equazione pura: nessun termine in x, solo x al quadrato.</h2>
  <p class="mot-quiz-expr">$$x^2=16$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — la radice di 16 è 4, con doppio segno: x=4 e x=-4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=\pm4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai dimenticato di estrarre la radice quadrata: x²=16 non è x=16." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=16$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="4²=16, ma 8²=64: il numero 8 non c'entra proprio nulla qui." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=8$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Ancora un'equazione pura, con un fattore comune da togliere di mezzo.</h2>
  <p class="mot-quiz-expr">$$2x^2-8=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — dividi per 2: x²=4, quindi x=2 e x=-2." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=\pm2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai dimenticato di dividere per 2 prima di fare la radice: x²=8, non x²=16." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=\pm4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Manca la soluzione negativa: anche x=-2 soddisfa l'equazione pura." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Un quadrato di binomio nascosto: la soluzione &egrave; doppia.</h2>
  <p class="mot-quiz-expr">$$x^2+2x+1=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — è (x+1)²=0, quindi l'unica soluzione, contata due volte, è x=-1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=-1$ (doppia)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Occhio al segno: (x+1)²=0 dà x=-1, non x=1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=1$ (doppia)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Non ci sono due soluzioni distinte: il discriminante è nullo, la radice è doppia e unica." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=\pm1$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Un altro quadrato di binomio, stavolta con i segni invertiti.</h2>
  <p class="mot-quiz-expr">$$x^2-6x+9=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — è (x-3)²=0: soluzione doppia x=3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=3$ (doppia)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno è sbagliato: (x-3)²=0 dà x=3, non x=-3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=-3$ (doppia)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="9 è il quadrato di 3, non la soluzione dell'equazione: hai confuso il termine noto con la radice." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=9$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Tutti segni negativi da qualche parte: tienili d'occhio.</h2>
  <p class="mot-quiz-expr">$$x^2+5x+6=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — (-2)+(-3)=-5 e (-2)·(-3)=6: coppia giusta, il segno meno cattura sia la somma che il prodotto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=-2,\ x=-3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="2+3=5 sì, ma il termine centrale sarebbe -5x con radici positive, non +5x come nel testo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=2,\ x=3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="-1 e -6 danno prodotto 6, ma sommati fanno -7, non -5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=-1,\ x=-6$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 10 di 10</p>
  <h2 class="mot-quiz-q">Ultima del riscaldamento: un termine noto negativo.</h2>
  <p class="mot-quiz-expr">$$x^2-x-6=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 3+(-2)=1 e 3·(-2)=-6: la somma delle radici vale 1 (il coefficiente -x cambiato di segno), il prodotto vale -6." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=3,\ x=-2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Segni scambiati: verifica per sostituzione, non soddisfano l'equazione di partenza." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=-3,\ x=2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="6 e -1 hanno prodotto -6, ma sommati fanno 5, non -1: coppia sbagliata." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=6,\ x=-1$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-avanzato" data-transition="zoom">
  <p class="mot-kicker">livello 2</p>
  <h1 class="r-fit-text">AVANZATO</h1>
  <p class="mot-joke fragment">formula risolutiva, discriminante, segno della parabola e disequazioni</p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Quando i numeri interi non ti soccorrono, chiama la formula risolutiva.</h2>
  <p class="mot-quiz-expr">$$x^2-2x-3=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=4+12=16$, $\sqrt{\Delta}=4$: $x=\dfrac{2\pm4}{2}$ dà 3 e -1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=3,\ x=-1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Segni invertiti: verifica sostituendo, l'equazione non torna con queste radici." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=1,\ x=-3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il prodotto delle radici deve fare -3 (termine noto con segno cambiato): 3·1=3, non -3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=3,\ x=1$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Un coefficiente diverso da 1 davanti a $x^2$: la formula non si spaventa.</h2>
  <p class="mot-quiz-expr">$$2x^2+3x-2=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=9+16=25$: $x=\dfrac{-3\pm5}{4}$ dà $\tfrac12$ e $-2$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=\tfrac12,\ x=-2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai probabilmente dimenticato di dividere per $2a=4$ nella formula: controlla il denominatore." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=2,\ x=-\tfrac12$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il prodotto delle radici dovrebbe fare $c/a=-1$: $1 \cdot (-2)=-2$, non torna." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=1,\ x=-2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Il discriminante &egrave; un giudice severo: a volte dice di no.</h2>
  <p class="mot-quiz-expr">$$x^2-4x+5=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=16-20=-4<0$: nessuna soluzione reale, la parabola non tocca mai l'asse x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $\Delta<0$: nessuna soluzione reale</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Una soluzione doppia richiederebbe $\Delta=0$: qui invece $\Delta=-4$, negativo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=2$ (doppia)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="1 e 5 non risolvono l'equazione: prova a sostituire, il discriminante negativo esclude soluzioni reali in partenza." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=1,\ x=5$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">La parabola sale sopra l'asse x: dove esattamente?</h2>
  <p class="mot-quiz-expr">$$x^2-5x+6\gt0$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid1" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid1)"/>
    <line class="axis" x1="0" y1="151" x2="240" y2="151"/>
    <line class="axis" x1="28" y1="5" x2="28" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <line class="solution" x1="10" y1="151" x2="98" y2="151"/>
    <line class="solution" x1="133" y1="151" x2="220" y2="151"/>
    <circle class="point-open" cx="98" cy="151" r="4"/>
    <circle class="point-open" cx="133" cy="151" r="4"/>
    <text x="98" y="169" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">2</text>
    <text x="133" y="169" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">3</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — le radici sono 2 e 3, la parabola apre verso l'alto: è positiva fuori dalle radici." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x\lt2 \lor x\gt3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quello è l'intervallo dove la parabola è sotto l'asse (negativa), non sopra." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $2\lt x\lt3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Non è sempre vera: tra le radici 2 e 3 la parabola scende sotto l'asse, negativa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Sempre vera</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Stavolta cerchiamo dove la parabola sta sotto (o sopra, di striscio) l'asse.</h2>
  <p class="mot-quiz-expr">$$x^2-9\leq0$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid2" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid2)"/>
    <line class="axis" x1="0" y1="76" x2="240" y2="76"/>
    <line class="axis" x1="115" y1="5" x2="115" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <line class="solution" x1="36" y1="76" x2="194" y2="76"/>
    <circle class="point" cx="36" cy="76" r="4"/>
    <circle class="point" cx="194" cy="76" r="4"/>
    <text x="36" y="94" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">-3</text>
    <text x="194" y="94" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">3</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — radici -3 e 3, parabola verso l'alto: è ≤0 proprio tra le radici, estremi inclusi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $-3\leq x\leq3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quello è l'intervallo dove la parabola è positiva, fuori dalle radici: non è quello che cerchiamo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x\leq-3 \lor x\geq3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="È vera eccome: basta prendere x=0, e infatti 0-9=-9≤0, la disuguaglianza regge." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Mai vera</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Il punto pi&ugrave; basso (o pi&ugrave; alto) della parabola ha un nome: vertice.</h2>
  <p class="mot-quiz-expr">$$y=x^2-4x+3$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid3" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid3)"/>
    <line class="axis" x1="0" y1="133" x2="240" y2="133"/>
    <line class="axis" x1="31" y1="5" x2="31" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <circle class="point" cx="115" cy="155" r="4"/>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $x_V=-b/2a=4/2=2$, e $y_V=f(2)=4-8+3=-1$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(2,-1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Occhio al segno di $y_V$: sostituendo x=2 ottieni -1, non +1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(2,1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="La formula del vertice è $x_V=-b/2a$: con b=-4 e a=1 dà 2, non -2." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(-2,-1)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Il discriminante decide il destino delle radici: quando sono due e diverse?</h2>
  <p class="mot-quiz-expr">$$ax^2+bx+c=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — con $\Delta>0$ la formula risolutiva produce due valori distinti, grazie al $\pm\sqrt{\Delta}$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $\Delta>0$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $\Delta=0$ il $\pm\sqrt{\Delta}$ diventa $\pm0$: le due radici coincidono, non sono distinte." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $\Delta=0$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $\Delta<0$ la radice quadrata non esiste nei reali: nessuna soluzione, altro che due distinte." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $\Delta<0$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Una parabola che vola sempre sopra l'asse x, senza mai toccarlo.</h2>
  <p class="mot-quiz-expr">$$x^2+x+1\gt0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=1-4=-3<0$ e $a=1>0$: la parabola non incrocia mai l'asse ed è sempre positiva." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> Sempre vera ($\Delta<0$, $a>0$)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova x=0: $0+0+1=1>0$. È vera, altro che mai." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Mai vera</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova x=-1: $1-1+1=1>0$, comunque positiva: la disuguaglianza non dipende dal segno di x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Vera solo per $x>0$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Il segno davanti a $x^2$ decide da che parte la parabola sorride (o piange).</h2>
  <p class="mot-quiz-expr">$$y=-x^2+4$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid4" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid4)"/>
    <line class="axis" x1="0" y1="77" x2="240" y2="77"/>
    <line class="axis" x1="115" y1="5" x2="115" y2="175"/>
    <path class="curve" d="M10,155 Q115,-125 220,155"/>
    <circle class="point" cx="115" cy="15" r="4"/>
    <circle class="point-open" cx="45" cy="77" r="4"/>
    <circle class="point-open" cx="185" cy="77" r="4"/>
    <text x="45" y="95" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">-2</text>
    <text x="185" y="95" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">2</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — il coefficiente di $x^2$ è $a=-1<0$: la parabola apre verso il basso, come un sorriso capovolto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> Verso il basso ($a<0$)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $a$ negativo la concavità è verso il basso, non verso l'alto: il segno meno conta eccome." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Verso l'alto</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Ogni parabola ha una concavità, definita dal segno del coefficiente $a$: qui $a=-1$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non ha concavit&agrave;</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 10 di 10 — gran finale</p>
  <h2 class="mot-quiz-q">Una parabola che tocca l'asse in un solo punto: quanto vale la disequazione?</h2>
  <p class="mot-quiz-expr">$$-x^2+4x-4\geq0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — è $-(x-2)^2\geq0$: vale solo quando $(x-2)^2=0$, cio&egrave; $x=2$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> Solo $x=2$ ($\Delta=0$, $a<0$)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="In x=2 la disequazione è verificata: $-(2-2)^2=0\geq0$ è vera, quindi non è mai." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Mai vera</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova x=0: $-(0-2)^2=-4$, che non è $\geq0$: non è sempre vera." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Sempre vera</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-pro" data-transition="zoom">
  <p class="mot-kicker">livello 3</p>
  <h1 class="r-fit-text">PRO</h1>
  <p class="mot-joke fragment">parametri, sistemi con la retta, e una parabola che non tocca mai (o quasi) l'asse</p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Un parametro $k$ che decide se le due radici diventano una sola.</h2>
  <p class="mot-quiz-expr">$$x^2-2x+k=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=4-4k=0$ dà $k=1$: radici coincidenti, la parabola è tangente all'asse." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k=1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=-1$ il discriminante diventa $4+4=8>0$: due radici distinte, non coincidenti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k=-1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=0$ l'equazione diventa $x^2-2x=0$: radici 0 e 2, distinte, non coincidenti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $k=0$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Un prodotto di due fattori: quando &egrave; negativo?</h2>
  <p class="mot-quiz-expr">$$(x-1)(x+2)\lt0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — un prodotto è negativo quando i fattori hanno segno discorde: succede tra le radici -2 e 1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $-2\lt x\lt1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Fuori da quell'intervallo i due fattori hanno lo stesso segno: il prodotto è positivo, non negativo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x\lt-2 \lor x\gt1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Un intervallo scritto al contrario (estremo maggiore prima del minore) non ha senso: nessun numero lo soddisfa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $1\lt x\lt-2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Leggi il grafico: dove la parabola si tuffa sotto l'asse?</h2>
  <p class="mot-quiz-expr">$$x^2-2x-3$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid5" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid5)"/>
    <line class="axis" x1="0" y1="93" x2="240" y2="93"/>
    <line class="axis" x1="80" y1="5" x2="80" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <line class="solution" x1="45" y1="93" x2="185" y2="93"/>
    <circle class="point-open" cx="45" cy="93" r="4"/>
    <circle class="point-open" cx="185" cy="93" r="4"/>
    <text x="45" y="111" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">-1</text>
    <text x="185" y="111" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">3</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — le radici sono -1 e 3: tra di loro la parabola (che apre verso l'alto) è sotto l'asse, negativa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $-1\lt x\lt3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quello è l'intervallo dove la parabola è sopra l'asse (positiva), non sotto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x\lt-1 \lor x\gt3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Guarda il grafico: fuori dalle radici la parabola risale sopra l'asse, non resta negativa per sempre." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Sempre negativa</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Dal vertice al coefficiente: ricostruisci la parabola.</h2>
  <p class="mot-quiz-expr">$$V=(1,-4), \quad \text{passa per } (0,-3)$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $y=a(x-1)^2-4$; imponendo il passaggio per (0,-3): $-3=a(1)-4 \Rightarrow a=1$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $a=1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $a=-1$ otterresti $y=-3$ diventa $-3=-1-4=-5$: non torna, controlla il segno." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $a=-1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="$a=4$ darebbe $-3=4-4=0$, decisamente non -3: numero preso a caso." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $a=4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Un parametro $k$ nel termine centrale: quando il discriminante si azzera?</h2>
  <p class="mot-quiz-expr">$$x^2+kx+9=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $\Delta=k^2-36=0$ dà $k^2=36$, quindi $k=6$ oppure $k=-6$: non dimenticare mai il doppio segno." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k=\pm6$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=9$: $\Delta=81-36=45\neq0$. Hai confuso k con il termine noto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k=9$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=3$: $\Delta=9-36=-27\neq0$. Vicino nell'idea, ma il calcolo non regge." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $k=3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Coefficiente di $x^2$ diverso da uno anche nella disequazione: la sostanza non cambia.</h2>
  <p class="mot-quiz-expr">$$2x^2-3x-2\leq0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — le radici sono $-\tfrac12$ e $2$; la parabola apre verso l'alto, quindi è ≤0 tra le radici." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $-\tfrac12\leq x\leq2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quello è l'intervallo dove la parabola è positiva (fuori dalle radici), non dove è negativa o nulla." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x\leq-\tfrac12 \lor x\geq2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova x=0: $-2\leq0$ è vera. Quindi non è mai vera, anzi lo è in un intervallo preciso." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Mai vera</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Dove la parabola attraversa l'asse orizzontale: leggilo dal grafico.</h2>
  <p class="mot-quiz-expr">$$y=x^2-6x+8$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid6" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid6)"/>
    <line class="axis" x1="0" y1="144" x2="240" y2="144"/>
    <line class="axis" x1="25" y1="5" x2="25" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <circle class="point" cx="85" cy="144" r="4"/>
    <circle class="point" cx="145" cy="144" r="4"/>
    <text x="85" y="162" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">2</text>
    <text x="145" y="162" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">4</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 2+4=6 e 2·4=8: le intersezioni con l'asse x sono in x=2 e x=4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x=2,\ x=4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno è sbagliato: con radici negative la somma sarebbe -6, non +6." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x=-2,\ x=-4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="6 e 8 sono i coefficienti dell'equazione, non le sue soluzioni: non confonderli." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x=6,\ x=8$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Una retta e una parabola si incontrano: dove esattamente?</h2>
  <p class="mot-quiz-expr">$$y=x \quad \cap \quad y=x^2-2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — sostituendo: $x=x^2-2 \Rightarrow x^2-x-2=0 \Rightarrow x=2, x=-1$: i punti sono (2,2) e (-1,-1)." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(2,2)$ e $(-1,-1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Verifica per sostituzione: (1,1) darebbe $1=1-2=-1$, falso. Non sono punti di intersezione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(1,1)$ e $(-2,-2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="L'equazione risolvente $x^2-x-2=0$ ha discriminante positivo: le intersezioni esistono, e sono due." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Nessuna intersezione</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Un parametro $k$ che pu&ograve; far sparire il secondo grado stesso.</h2>
  <p class="mot-quiz-expr">$$(k-1)x^2+2x+1=0$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — se $k=1$ il coefficiente di $x^2$ si annulla: resta $2x+1=0$, un'equazione di primo grado." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k=1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=0$ resta $-x^2+2x+1=0$: il termine di secondo grado c'è ancora, eccome." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k=0$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Con $k=-1$ il coefficiente diventa $-2$, non zero: resta un'equazione di secondo grado." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $k=-1$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 10 di 10 — il boss finale</p>
  <h2 class="mot-quiz-q">Una parabola che sfiora l'asse in un solo punto, e lo esclude apposta.</h2>
  <p class="mot-quiz-expr">$$x^2-4x+4\gt0$$</p>
  <div class="mot-quiz-graph"><svg viewBox="0 0 240 180">
    <defs><pattern id="grid7" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 L0 0 0 20" fill="none" stroke="var(--mot-border)" stroke-width="1"/></pattern></defs>
    <rect width="240" height="180" fill="url(#grid7)"/>
    <line class="axis" x1="0" y1="155" x2="240" y2="155"/>
    <line class="axis" x1="31" y1="5" x2="31" y2="175"/>
    <path class="curve" d="M10,15 Q115,295 220,15"/>
    <line class="solution" x1="10" y1="155" x2="111" y2="155"/>
    <line class="solution" x1="119" y1="155" x2="220" y2="155"/>
    <circle class="point-open" cx="115" cy="155" r="4"/>
    <text x="115" y="173" style="font-family:'JetBrains Mono',monospace;font-size:9px;fill:var(--mot-muted);text-anchor:middle">2</text>
  </svg></div>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — è $(x-2)^2>0$: sempre vera tranne che in x=2, dove il quadrato si annulla. Game over con eleganza." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> Vera per ogni $x$ tranne $x=2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="In x=2 il quadrato $(x-2)^2$ vale 0, che non è $>0$: quel punto va escluso, non è sempre vera." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Sempre vera</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova x=0: $(0-2)^2=4>0$, vera. Non è mai vera, anzi lo è quasi sempre." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Mai vera</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">FINE</h1>
  <p class="mot-joke fragment">il punteggio non conta, la parabola s&igrave;</p>
</section>

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie della partecipazione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

<script>
function mot_quiz(el) {
  var section = el.closest("section");
  var box = section.querySelector(".mot-quiz-explain");
  box.textContent = el.dataset.explain;
  box.className = "mot-quiz-explain show " + (el.dataset.correct === "true" ? "ok" : "bad");
  el.classList.add("picked");
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise([box]);
  }
}
</script>

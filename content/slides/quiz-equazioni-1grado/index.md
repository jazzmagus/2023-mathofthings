---
title: Quiz — Equazioni di Primo Grado
summary: Gioco a premi — primo anno, corso base (Base / Avanzato / Pro)
authors: [Diego Fantinelli]
tags: [equazioni, quiz]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">gioco a premi — primo anno</p>
  <h1>Chi Vuol Essere <span class="math-word">Equazionista</span>?</h1>
  <p class="mot-tagline">30 domande, 3 livelli, <em>0</em> vie di scampo</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-background-image="start-here-bkg.jpg" data-background-opacity="0.15" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">PRONTI?</h1>
  <p class="mot-joke fragment">tre livelli affiancati: Base, Avanzato, Pro &mdash; scegli la freccia giusta</p>
</section>

---

<section class="mot-divider mot-level-base" data-transition="zoom">
  <p class="mot-kicker">livello 1</p>
  <h1 class="r-fit-text">BASE</h1>
  <p class="mot-joke fragment">riscaldamento: un passaggio o due, niente trucchi</p>
</section>

<section>
  <p class="mot-kicker">base — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Si parte piano: quanto vale $x$?</h2>
  <p class="mot-quiz-expr">$$3x = 12$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — dividi entrambi i membri per 3: x=4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai sommato invece di dividere: qui serve dividere per 3, non sottrarre." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 9$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="occhio: 3 per 3 fa 9, non 12. Ricontrolla la divisione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Un classico da riscaldamento.</h2>
  <p class="mot-quiz-expr">$$x + 7 = 15$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai sommato 7 invece di sottrarlo: porta il 7 dall'altra parte cambiandogli segno." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 22$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — sottrai 7 da entrambi i membri: x=8." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 8$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="quasi: controlla la sottrazione, 15-7 non fa 7." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 7$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Due passaggi, tienili in ordine.</h2>
  <p class="mot-quiz-expr">$$2x - 4 = 10$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai dimenticato di portare il -4 dall'altra parte prima di dividere." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — 2x=14, quindi x=7." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 7$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino, ma 2x=14 non 2x=12: ricontrolla il segno del -4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 6$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Un meno davanti alla $x$: non farti spaventare.</h2>
  <p class="mot-quiz-expr">$$-3x = 15$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="attenzione ai segni: negativo diviso negativo dà positivo, ma qui il dividendo è positivo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 5$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — dividi per -3: x=-5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = -5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="il segno va tenuto: 15 diviso -3 non fa -3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = -3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Le frazioni fanno paura solo se non le guardi negli occhi.</h2>
  <p class="mot-quiz-expr">$$\dfrac{x}{4} = 5$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai diviso invece di moltiplicare: qui serve moltiplicare per 4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 1{,}25$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplica entrambi i membri per 4: x=20." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 20$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="quasi, ma 4 per 5 fa 20, non 9." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 9$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">La $x$ compare da entrambe le parti: raccogliamola.</h2>
  <p class="mot-quiz-expr">$$5x + 2 = 3x + 10$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — porti 3x a sinistra e 2 a destra: 2x=8, quindi x=4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai sbagliato segno spostando i termini: ricontrolla chi va a destra e chi a sinistra." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 6$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="quasi: 2x=8 non 2x=4, ricontrolla la sottrazione 10-2." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Prima la parentesi, poi tutto il resto.</h2>
  <p class="mot-quiz-expr">$$4(x-1) = 12$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — dividi per 4: x-1=3, quindi x=4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai dimenticato di dividere anche il -1 per 4, oppure di riportarlo dopo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="12 diviso 4 fa 3, non 5: poi ricordati di aggiungere l'1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 5$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">La $x$ si nasconde a sinistra del segno meno.</h2>
  <p class="mot-quiz-expr">$$7 - x = 2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="attento al segno: isolando -x=-5, quindi x è positivo, non negativo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = -5$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — -x=-5, cambiando segno x=5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="7-2 fa 5, non 9: ricontrolla la sottrazione iniziale." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 9$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Ancora $x$ su entrambi i lati: niente panico.</h2>
  <p class="mot-quiz-expr">$$2x + 3 = x + 8$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — porti x a sinistra e 3 a destra: x=5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai sommato invece di sottrarre il 3: ricontrolla il trasporto dei termini." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 11$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino, ma 8-3 fa 5, non 3: ricontrolla la sottrazione finale." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 10 di 10</p>
  <h2 class="mot-quiz-q">Ultima del riscaldamento, poi si sale di livello.</h2>
  <p class="mot-quiz-expr">$$6x - 1 = 2x + 11$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai sbagliato a portare il -1 a destra: diventa +1, non -1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 2{,}5$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — 4x=12, quindi x=3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="quasi: 4x=12 non 4x=20, ricontrolla 11+1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 5$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-avanzato" data-transition="zoom">
  <p class="mot-kicker">livello 2</p>
  <h1 class="r-fit-text">AVANZATO</h1>
  <p class="mot-joke fragment">identità, equazioni impossibili, e qualche parentesi in più</p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Il pubblico sussurra: &laquo;&egrave; un trucco?&raquo;</h2>
  <p class="mot-quiz-expr">$$2(x+3) = 2x+6$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="sostituendo x=0 verifichi che vale, ma vale per QUALSIASI x, non solo per 0: hai trovato un caso, non la regola." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 0$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="tutt'altro, è sempre vera: distribuendo ottieni 2x+6=2x+6, i termini in x si elidono e resta 6=6." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> &Egrave; impossibile, arrenditi</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — distribuendo ottieni 2x+6=2x+6: un'identità, sempre vera, qualunque x scegli." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; un'identit&agrave;: vale per ogni $x$, sempre!</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Un matematico ti sfida: &laquo;scommetto che nasconde qualcosa&raquo;.</h2>
  <p class="mot-quiz-expr">$$3(x-1) - x = 2x - 3$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="funziona anche per x=0, ma non è l'unica soluzione: l'equazione è vera per ogni x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 0$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — sviluppando ottieni 2x-3=2x-3: un'identità, i due membri coincidono sempre." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Sorpresa: &egrave; un'identit&agrave;, vale per ogni $x$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="al contrario: i due membri collimano perfettamente, non c'è nessuna assurdità." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Impossibile, i conti non tornano</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Attenzione, equazione trabocchetto in arrivo.</h2>
  <p class="mot-quiz-expr">$$5x - 2(x+4) = 3x + 1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="sostituisci e noterai che non torna: i termini in x si cancellano prima ancora di arrivare a un valore." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 3$, facile no?</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="giusto — resta -8=1, un'assurdità: nessun valore di x la soddisfa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Boom: &egrave; impossibile, la $x$ sparisce e resta un'assurdit&agrave;</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="stesso destino di x=3: l'equazione non ammette proprio soluzione, qualunque numero provi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = -3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Frazioni all'attacco! Chi sopravvive ai calcoli?</h2>
  <p class="mot-quiz-expr">$$\dfrac{x+1}{2} = \dfrac{x-1}{3}$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplicando in croce ottieni 3(x+1)=2(x-1), cioè 3x+3=2x-2, quindi x=-5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = -5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="probabile errore di segno nel moltiplicare in croce: controlla il -2 finale, non +2." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 5$ (occhio ai segni!)</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="niente panico: la soluzione esiste, ed è pure unica." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; impossibile, niente panico</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Caso da detective: i denominatori sono le tue impronte digitali, non farti ingannare.</h2>
  <p class="mot-quiz-expr">$$\dfrac{2}{3}x - 1 = \dfrac{1}{6}x + 2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai probabilmente sbagliato a moltiplicare tutto per il minimo comune denominatore (6)." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplicando tutto per 6 ottieni 4x-6=x+12, quindi 3x=18 e x=6." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 6$, mistero risolto</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino ma non centrato: ricontrolla i denominatori prima di semplificare." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Specchio, specchio delle mie brame: illusione o realt&agrave;?</h2>
  <p class="mot-quiz-expr">$$-2(x-3) = -(2x-6)$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="funziona anche per x=3, ma non è l'unica soluzione: vale per ogni x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="anzi, i due membri sono la stessa espressione scritta in due modi diversi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Impossibile</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — sono la stessa espressione: l'equazione è sempre vera, un'identità." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Nessuna illusione: &egrave; un'identit&agrave; vera per ogni $x$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Sfida flash, tre operazioni in una: sopravviverai ai segni meno?</h2>
  <p class="mot-quiz-expr">$$4x - (3-2x) = 3(2x+1)$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="sostituisci e vedrai che i conti non tornano comunque: la x si cancella da entrambi i lati." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 0$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — resta -3=3, un'assurdità priva di soluzione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Game over: &egrave; impossibile</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="stesso destino: l'equazione non si risolve per nessun valore di x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 1$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 8 di 10 — livello boss</p>
  <h2 class="mot-quiz-q">Con un parametro misterioso $k$: per quale valore l'equazione si rifiuta di avere soluzione?</h2>
  <p class="mot-quiz-expr">$$(k-2)x = 6$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=6 l'equazione diventa 4x=6: soluzione x=3/2, tutto regolare." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k = 6$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — con k=2 il coefficiente di x si annulla e resta 0·x=6: impossibile." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k = 2$, l'equazione si blocca sul pi&ugrave; bello</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=0 diventa -2x=6: soluzione x=-3, nessun dramma." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $k = 0$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Dividiamo un'equazione come una pizza in fette: quanto tocca a $x$?</h2>
  <p class="mot-quiz-expr">$$\dfrac{x}{2} - \dfrac{x-1}{4} = 1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai probabilmente sbagliato segno distribuendo il meno davanti alla frazione (x-1)/4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 6$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplicando per 4 ottieni 2x-(x-1)=4, cioè x+1=4, quindi x=3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino, ma controlla il termine costante finale prima di isolare la x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 10 di 10 — gran finale</p>
  <h2 class="mot-quiz-q">La solita equazione o un colpo di scena?</h2>
  <p class="mot-quiz-expr">$$3(x+2) - 2(x-1) = x + 8$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="funziona anche per x=0, ma non è l'unica soluzione: vale per tutti gli x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 0$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — sviluppando ottieni x+8=x+8: un'identità, i due membri coincidono sempre." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Colpo di scena: &egrave; un'identit&agrave;, vale sempre</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="al contrario: i due membri coincidono sempre, non c'è nessuna assurdità." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Impossibile</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-pro" data-transition="zoom">
  <p class="mot-kicker">livello 3</p>
  <h1 class="r-fit-text">PRO</h1>
  <p class="mot-joke fragment">parentesi annidate, parametri, e trabocchetti travestiti da frazioni</p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Parentesi dentro parentesi: procedi dal centro verso fuori.</h2>
  <p class="mot-quiz-expr">$$2[3(x-1) - 2] = 4x - 2(x+1)$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — a sinistra ottieni 6x-10, a destra 2x-2: allora 6x-10=2x-2, cioè 4x=8, x=2." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="hai probabilmente distribuito il 2 esterno solo su una parte della parentesi quadra." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="niente paura: la soluzione esiste ed è unica, basta procedere con calma dal centro." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; impossibile</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Due parentesi che sembrano litigare: fanno pace?</h2>
  <p class="mot-quiz-expr">$$3(x+1) - 2(2x-1) = 5 - x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="funziona anche per x=1, ma l'equazione è vera per ogni x: non è l'unica soluzione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 1$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — a sinistra ottieni -x+5, uguale identico alla destra: identità, vale per ogni x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> Fanno pace per sempre: &egrave; un'identit&agrave;</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="al contrario: sviluppando i due membri diventano identici." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Litigano per sempre: impossibile</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Due frazioni, un solo minimo comune denominatore: trovalo.</h2>
  <p class="mot-quiz-expr">$$\dfrac{x-1}{3} - \dfrac{x+1}{2} = -1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplicando per 6 ottieni 2(x-1)-3(x+1)=-6, cioè -x-5=-6, quindi x=1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="controlla il segno quando distribuisci il -3 davanti a (x+1): diventa -3x-3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = -1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino, ma ricontrolla il minimo comune denominatore tra 3 e 2: è 6, non 5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 5$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 4 di 10 — trabocchetto puro</p>
  <h2 class="mot-quiz-q">Un parametro $k$ misterioso: per quale valore l'equazione ha infinite soluzioni?</h2>
  <p class="mot-quiz-expr">$$kx - 3 = 2x + k$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=2 l'equazione diventa 2x-3=2x+2, cioè -3=2: è impossibile, non ha infinite soluzioni." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k = 2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=-3 non annulli nemmeno il coefficiente di x: l'equazione resta determinata, una sola soluzione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k = -3$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — per avere infinite soluzioni servirebbe k-2=0 e -3-k=0 insieme: k=2 e k=-3 non possono coincidere, quindi nessun k funziona." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Nessun valore di $k$: il trucco non esiste</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Doppia distribuzione, doppio rischio di errore.</h2>
  <p class="mot-quiz-expr">$$5 - 2(x-3) = 3(2-x) + x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — a sinistra ottieni 11-2x, a destra 6-2x: resta 11=6, assurdo. Impossibile." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> &Egrave; impossibile</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="attenzione: i termini in x si cancellano da soli, resta un confronto solo tra numeri." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="non è un'identità: i numeri che restano (11 e 6) non coincidono." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; un'identit&agrave;</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Denominatori diversi, stesso obiettivo: isolare $x$.</h2>
  <p class="mot-quiz-expr">$$\dfrac{x+2}{3} - \dfrac{x-1}{6} = 1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — moltiplicando per 6 ottieni 2(x+2)-(x-1)=6, cioè x+5=6, quindi x=1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = 1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="occhio al segno meno davanti a (x-1): diventa -x+1, non -x-1." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = -1$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="vicino, ma ricontrolla il minimo comune denominatore tra 3 e 6: è 6, non 3." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x = 3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Un altro parametro, un'altra trappola: quando l'equazione &egrave; impossibile?</h2>
  <p class="mot-quiz-expr">$$(3-k)x = 6$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — con k=3 il coefficiente si annulla e resta 0·x=6: impossibile." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $k = 3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=6 l'equazione diventa -3x=6, soluzione x=-2, tutto regolare." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $k = 6$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="con k=0 diventa 3x=6, soluzione x=2, nessun problema." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $k = 0$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Un segno meno davanti a tutta la parentesi quadra: attento a distribuirlo bene.</h2>
  <p class="mot-quiz-expr">$$-[2(x+1) - 3] = -(x-4) + 2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — a sinistra ottieni -2x+1, a destra -x+6: allora -2x+1=-x+6, quindi -x=5, x=-5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x = -5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="controlla il segno meno davanti alla parentesi quadra: cambia il segno di ENTRAMBI i termini dentro." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 5$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="niente paura, la soluzione esiste ed è negativa: ricontrolla i segni con calma." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; impossibile</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Una frazione dentro l'altra: la matrioska delle equazioni.</h2>
  <p class="mot-quiz-expr">$$\dfrac{\;\dfrac{x+2}{2}\;}{3} = \dfrac{x-1}{6}$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — il primo membro si riduce a (x+2)/6: uguagliando i numeratori, x+2=x-1, cioè 2=-1: impossibile." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> &Egrave; impossibile</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="semplificando la frazione annidata, i denominatori diventano uguali (6): serve confrontare solo i numeratori." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = 4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="non è un'identità: i numeratori x+2 e x-1 non possono mai essere uguali." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; un'identit&agrave;</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 10 di 10 — il boss finale</p>
  <h2 class="mot-quiz-q">L'ultima prova: quattro parentesi, un solo verdetto.</h2>
  <p class="mot-quiz-expr">$$4(x-2) - (3x-1) = 2(x+1) - (x+5)$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="esatto — a sinistra resta x-7, a destra x-3: -7=-3 è assurdo. Impossibile, game over onorevole." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> &Egrave; impossibile</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="i termini in x si cancellano da entrambi i lati: resta solo un confronto tra numeri, controlla quello." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x = -4$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="non è un'identità: i numeri che restano, -7 e -3, sono diversi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> &Egrave; un'identit&agrave;</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">FINE</h1>
  <p class="mot-joke fragment">il punteggio non conta, la sopravvivenza s&igrave;</p>
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

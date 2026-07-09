---
title: Quiz — Scomposizione di Polinomi
summary: Gioco a premi — secondo anno, corso base (Base / Avanzato / Pro)
authors: [Diego Fantinelli]
tags: [polinomi, scomposizione, quiz]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">gioco a premi — secondo anno</p>
  <h1>Chi Vuol Essere <span class="math-word">Scompositore</span>?</h1>
  <p class="mot-tagline">30 domande, 3 livelli, un solo fattore comune: <em>il coraggio</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-background-image="start-here-bkg.jpg" data-background-opacity="0.15" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">PRONTI?</h1>
  <p class="mot-joke fragment">tre livelli affiancati: Base, Avanzato, Pro &mdash; il fattore comune non si nasconde da solo</p>
</section>

---

<section class="mot-divider mot-level-base" data-transition="zoom">
  <p class="mot-kicker">livello 1</p>
  <h1 class="r-fit-text">BASE</h1>
  <p class="mot-joke fragment">raccoglimento e quadrati: il minimo indispensabile per sopravvivere</p>
</section>

<section>
  <p class="mot-kicker">base — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Il fattore comune &egrave; in agguato: scovalo prima che scappi.</h2>
  <p class="mot-quiz-expr">$$6x + 9$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — il 3 divide sia 6 che 9: raccolto e portato a casa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $3(2x+3)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il 6 non divide il 9 in modo pulito: hai raccolto un numero che non c'entra, resta un pasticcio dentro la parentesi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $6(x+9)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai dimenticato di dividere anche il 9 per 3: 9 diviso 3 fa 3, non resta 9." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $3(2x+9)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Una differenza di quadrati che grida &laquo;scomponimi!&raquo;.</h2>
  <p class="mot-quiz-expr">$$x^2 - 9$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="9 non è il quadrato di 1: hai inventato dei numeri a caso, e nemmeno si moltiplicano bene." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-9)(x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — la radice di 9 è 3: differenza di quadrati da manuale, senza sorprese." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-3)(x+3)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Un quadrato di binomio avrebbe bisogno di un doppio prodotto (-6x) che qui non esiste." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-9)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Il quadrato di un binomio si riconosce dal doppio prodotto.</h2>
  <p class="mot-quiz-expr">$$x^2+6x+9$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quella è una differenza di quadrati, ma qui c'è un +6x di mezzo: non torna proprio." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+3)(x-3)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 3²=9 e 2·3·x=6x: quadrato di binomio perfetto, senza trucchi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+3)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="9 non è la radice quadrata di se stesso: hai confuso il numero con la sua radice." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x+9)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Raccogli tutto quello che i due termini hanno in comune, non solo un pezzo.</h2>
  <p class="mot-quiz-expr">$$2x^2-8x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 2x è il vero fattore comune: raccolta totale, complimenti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $2x(x-4)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="8x diviso 2x fa 4, non 8: hai raccolto bene il segno ma sbagliato il numero." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $2x(x-8)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Raccolta parziale: dentro la parentesi si nasconde ancora un altro 2, si poteva stringere di più." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x(2x-8)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Il classico dei classici: non fartelo scappare.</h2>
  <p class="mot-quiz-expr">$$x^2-4$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="4 non è il quadrato di 4: la radice di 4 è 2, non 4." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-4)(x+4)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — la radice di 4 è 2: differenza di quadrati pulita, promossi a pieni voti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-2)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quello sarebbe un quadrato di binomio, ma qui non compare nessun -4x: manca il doppio prodotto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-2)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Doppio prodotto sospetto: fiuta il quadrato di binomio.</h2>
  <p class="mot-quiz-expr">$$x^2-10x+25$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="25 è il quadrato di 5, non di 25: hai preso il numero sbagliato come base del quadrato." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-25)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 5²=25 e 2·5·x=10x: quadrato di binomio confermato, nessun dubbio." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-5)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quella sarebbe una differenza di quadrati, ma qui il termine centrale -10x non lo permette." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-5)(x+5)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Il fattore comune &egrave; talmente ovvio che quasi si offende se non lo trovi.</h2>
  <p class="mot-quiz-expr">$$5x - 5y$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 5 divide entrambi i termini: raccolta totale, gioco facile facile." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $5(x-y)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Occhio al segno meno tra x e y: non è sparito, resta dentro la parentesi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $5(x+y)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai raccolto la x invece del 5: possibile in teoria, ma resta un 5 di troppo fuori dalla parentesi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x(5-5y)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Un altro quadrato in agguato: 16 &egrave; un numero furbo.</h2>
  <p class="mot-quiz-expr">$$x^2-16$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — la radice di 16 è 4: differenza di quadrati, missione compiuta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-4)(x+4)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova a moltiplicarli: non ti restituisce x²-16, hai inventato due numeri a caso." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-8)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Manca il -8x che servirebbe per un quadrato di binomio: qui c'è solo una differenza di quadrati." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-4)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Raccogliere bene &egrave; un'arte: non fermarti a met&agrave; strada.</h2>
  <p class="mot-quiz-expr">$$3x^2+6x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="6x diviso 3x fa 2, non 6: hai raccolto il 3 ma sbagliato la divisione." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $3x(x+6)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 3x è il massimo fattore comune: raccolta totale, si vola." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $3x(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Raccolta parziale: dentro la parentesi c'è ancora un 3 tutto da raccogliere." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x(3x+6)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">base — domanda 10 di 10</p>
  <h2 class="mot-quiz-q">Ultima del riscaldamento: un quadrato di binomio in bella vista.</h2>
  <p class="mot-quiz-expr">$$x^2+4x+4$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="4² fa 16, non 4: hai preso il numero sbagliato come base del quadrato." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+4)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 2²=4 e 2·2·x=4x: quadrato di binomio perfetto, si sale di livello." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+2)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno è sbagliato: qui il polinomio ha tutti segni positivi, nessun meno in vista." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-2)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-avanzato" data-transition="zoom">
  <p class="mot-kicker">livello 2</p>
  <h1 class="r-fit-text">AVANZATO</h1>
  <p class="mot-joke fragment">gruppi, cubi e trinomi che sembrano scherzare, ma non lo fanno</p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Quattro termini, nessun fattore comune a vista: serve un trucco a gruppi.</h2>
  <p class="mot-quiz-expr">$$x^3+x^2+x+1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli x² dal primo gruppo e 1 dal secondo: (x+1) esce da entrambi, magia matematica." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+1)(x^2+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno è sbagliato: qui tutti i termini sono positivi, non compare mai un -x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)(x^2+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Si scompone eccome, basta raggruppare a coppie: non arrenderti troppo presto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Cerca due numeri che sommati diano 7 e moltiplicati diano 12.</h2>
  <p class="mot-quiz-expr">$$x^2+7x+12$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="2 e 6 si moltiplicano bene (12), ma sommati fanno 8, non 7: quasi, ma non basta quasi." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+2)(x+6)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — 3+4=7 e 3·4=12: la coppia perfetta, trovata al primo colpo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+3)(x+4)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="1 e 12 sommati fanno 13: troppo lontano dal bersaglio, ricontrolla la caccia." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x+1)(x+12)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 3 di 10</p>
  <h2 class="mot-quiz-q">Stessa caccia, segni diversi: attenzione ai meno.</h2>
  <p class="mot-quiz-expr">$$x^2-5x+6$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — (-2)+(-3)=-5 e (-2)·(-3)=6: bersaglio centrato, con i segni giusti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-2)(x-3)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="-1 e -6 si moltiplicano bene (6), ma sommati fanno -7, non -5." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)(x-6)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Segni invertiti: con due più il termine centrale sarebbe +5x, non -5x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x+2)(x+3)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Il coefficiente davanti alla $x^2$ complica la caccia: serve il trinomio speciale.</h2>
  <p class="mot-quiz-expr">$$2x^2+5x+2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Occhio: 2x+2 nasconde ancora un fattore 2 raccoglibile, la scomposizione non è pulita." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(2x+2)(x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — distribuendo ottieni 2x²+4x+x+2=2x²+5x+2: perfetto, senza resti." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(2x+1)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Stesso problema scritto al contrario: 2x+2 ha ancora un 2 tutto da raccogliere." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x+1)(2x+2)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">8 &egrave; un cubo travestito da numero innocuo: chi lo riconosce?</h2>
  <p class="mot-quiz-expr">$$x^3-8$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il cubo di binomio avrebbe termini intermedi con coefficienti diversi: qui serve un'altra formula." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-2)^3$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — differenza di cubi: (x-2) per il trinomio con i segni 'sempre più'." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-2)(x^2+2x+4)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno centrale del trinomio va cambiato rispetto al binomio: qui doveva essere +2x, non -2x." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-2)(x^2-2x+4)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">27 &egrave; il cubo di un numero che ami gi&agrave;: quale?</h2>
  <p class="mot-quiz-expr">$$x^3+27$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — somma di cubi: (x+3) per il trinomio con il segno meno al centro." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+3)(x^2-3x+9)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno centrale è sbagliato: nella somma di cubi il doppio prodotto va con il meno, non col più." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+3)(x^2+3x+9)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il cubo di binomio avrebbe quattro termini con coefficienti diversi: non è questo il caso." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x+3)^3$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 7 di 10</p>
  <h2 class="mot-quiz-q">Quattro lettere, zero panico: raggruppa a coppie e trova il fattore comune due volte.</h2>
  <p class="mot-quiz-expr">$$ax+ay+bx+by$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai mescolato lettere che non c'entrano tra loro: i gruppi giusti sono a(x+y) e b(x+y)." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(a+x)(b+y)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli a dal primo gruppo e b dal secondo: esce (x+y) da entrambi, pulito e preciso." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(a+b)(x+y)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Questo funzionerebbe solo se il polinomio fosse già un prodotto, non una somma di quattro termini." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(ab)(xy)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Un trinomio quadrato e una $y$ solitaria: uniscili con astuzia.</h2>
  <p class="mot-quiz-expr">$$x^2-6x+9-y^2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — riconosci $(x-3)^2-y^2$ come differenza di quadrati e la scomponi in due fattori." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-3-y)(x-3+y)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai trattato tutto come un quadrato unico, ma la $y^2$ ha il segno meno: è una differenza, non una somma." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-3-y)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Si scompone benissimo: basta vedere il trinomio come un quadrato nascosto, $(x-3)^2$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Due passaggi in uno: prima il fattore comune, poi il resto.</h2>
  <p class="mot-quiz-expr">$$3x^2-12$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli 3, poi riconosci $x^2-4$ come differenza di quadrati: doppietta perfetta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $3(x-2)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova a moltiplicarli: non torna $3x^2-12$, hai inventato una scomposizione che non esiste." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(3x-2)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Classico errore: la radice di 4 è 2, non 4. Ti sei dimenticato di farla, quella radice." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $3(x-4)(x+4)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">avanzato — domanda 10 di 10 — gran finale</p>
  <h2 class="mot-quiz-q">Una differenza di quadrati che nasconde un'altra differenza di quadrati: una matrioska algebrica.</h2>
  <p class="mot-quiz-expr">$$x^4-1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — prima scomponi in $(x^2-1)(x^2+1)$, poi $x^2-1$ si scompone ancora: matrioska aperta fino in fondo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-1)(x+1)(x^2+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Questo sarebbe il quadrato di $(x^2-1)$, ma qui non c'è nessun quadrato: manca il pezzo mancante." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x^2-1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai raddoppiato tutto per errore: nella scomposizione corretta ogni fattore compare una sola volta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-1)^2(x+1)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider mot-level-pro" data-transition="zoom">
  <p class="mot-kicker">livello 3</p>
  <h1 class="r-fit-text">PRO</h1>
  <p class="mot-joke fragment">parametri, trabocchetti e polinomi che a volte si rifiutano di scomporsi</p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 1 di 10</p>
  <h2 class="mot-quiz-q">Un quadrato di binomio che si scontra con una $z$ solitaria.</h2>
  <p class="mot-quiz-expr">$$x^2+2xy+y^2-z^2$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — riconosci $(x+y)^2-z^2$ come differenza di quadrati: scomposizione elegante." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+y-z)(x+y+z)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai trattato tutto come un unico quadrato, ma la $z^2$ ha il segno meno: manca il pezzo mancante." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+y-z)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Si scompone eccome: basta vedere $x^2+2xy+y^2$ come $(x+y)^2$ e il gioco è fatto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 2 di 10</p>
  <h2 class="mot-quiz-q">Quattro termini con coefficienti 1, 3, 3, 1: ti ricordano qualcosa?</h2>
  <p class="mot-quiz-expr">$$x^3-3x^2+3x-1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quella sarebbe la scomposizione di $x^3-1$, ma qui i coefficienti centrali (3 e 3) raccontano un'altra storia." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-1)(x^2+x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — i coefficienti 1,3,3,1 sono il triangolo di Tartaglia del cubo: $(x-1)$ al cubo, senza scampo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)^3$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il grado e i coefficienti non tornano: manca proprio il pattern del cubo perfetto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-1)(x^2-1)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 3 di 10 — trabocchetto puro</p>
  <h2 class="mot-quiz-q">Un trinomio che sembra scomponibile ma &egrave; una trappola vera e propria.</h2>
  <p class="mot-quiz-expr">$$x^2+x+1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Provalo: $(x+1)^2$ fa $x^2+2x+1$, non $x^2+x+1$. Il doppio prodotto non torna." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x+1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quella è $x^2-1$, tutta un'altra storia: qui manca proprio la struttura giusta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)(x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — il discriminante è negativo (1-4=-3): questo trinomio è irriducibile nei numeri reali, punto e basta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone in $\mathbb{R}$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 4 di 10</p>
  <h2 class="mot-quiz-q">Non fermarti al primo raccoglimento: c'&egrave; ancora lavoro da fare.</h2>
  <p class="mot-quiz-expr">$$2x^3-2x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli 2x, poi riconosci $x^2-1$ come differenza di quadrati: scomposizione completa." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $2x(x-1)(x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Hai raccolto solo il 2, ma dentro la parentesi c'è ancora una x tutta da tirare fuori." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $2(x^3-x)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova a moltiplicare: non ti restituisce $2x^3-2x$, la scomposizione non regge al controllo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x(2x-1)(x+1)$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 5 di 10</p>
  <h2 class="mot-quiz-q">Un quadrato di binomio travestito da grado quattro.</h2>
  <p class="mot-quiz-expr">$$x^4-2x^2+1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Corretto come primo passo, ma non è la scomposizione completa: $x^2-1$ si scompone ancora." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x^2-1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — dopo aver visto $(x^2-1)^2$, scomponi anche $x^2-1$: scomposizione fino in fondo." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)^2(x+1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Attenzione: $(x-1)^4$ non è uguale a $x^4-2x^2+1$, provalo a sviluppare e vedrai la differenza." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-1)^4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 6 di 10</p>
  <h2 class="mot-quiz-q">Una differenza di quadrati con un fattore comune nascosto sotto al tappeto.</h2>
  <p class="mot-quiz-expr">$$a^2-b^2+a-b$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Corretto per i primi due termini, ma hai dimenticato completamente l'a-b finale: scomposizione incompleta." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(a-b)(a+b)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — scomponi $a^2-b^2$ e raccogli $(a-b)$ anche dall'ultimo pezzo: $(a-b)(a+b+1)$." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(a-b)(a+b+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Si scompone benissimo: basta notare che $(a-b)$ è un fattore comune anche dell'ultimo termine." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 7 di 10 — livello boss</p>
  <h2 class="mot-quiz-q">Un parametro $k$ che gioca a nascondino tra i coefficienti.</h2>
  <p class="mot-quiz-expr">$$x^2-(k+1)x+k$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Distribuisci e controlla il segno centrale: non ottieni $-(k+1)x$, il segno di k non torna." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-k)(x+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — somma e prodotto: -1 e -k sommati danno $-(k+1)$ e moltiplicati danno k. Funziona anche con un parametro." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x-1)(x-k)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Un quadrato di binomio richiederebbe $-2kx$ come termine centrale: qui $-(k+1)x$ racconta un'altra storia." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(x-k)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 8 di 10</p>
  <h2 class="mot-quiz-q">Coefficienti tondi, ma non farti ingannare dal 9.</h2>
  <p class="mot-quiz-expr">$$9x^2-6x+1$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Il segno del termine centrale è negativo (-6x): con un +1 dentro otterresti +6x, non torna." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(3x+1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — $(3x)^2=9x^2$, $1^2=1$, e $2 \cdot 3x \cdot 1=6x$ col segno meno: quadrato di binomio perfetto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(3x-1)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="$9x$ al quadrato farebbe $81x^2$, ben oltre i $9x^2$ di partenza: hai preso il coefficiente sbagliato." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $(9x-1)^2$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 9 di 10</p>
  <h2 class="mot-quiz-q">Raccogli, scomponi, e non fermarti finch&eacute; non hai spremuto tutto.</h2>
  <p class="mot-quiz-expr">$$x^5-x$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Ottimo inizio, ma $x^4-1$ è ancora scomponibile: la caccia al fattore non è finita." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $x(x^4-1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — raccogli x, poi scomponi $x^4-1$ fino in fondo: scomposizione completa in quattro fattori." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $x(x-1)(x+1)(x^2+1)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Prova a moltiplicare: non torna affatto $x^5-x$, la scomposizione è pura fantasia." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> $x(x-1)^4$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

<section>
  <p class="mot-kicker">pro — domanda 10 di 10 — il boss finale</p>
  <h2 class="mot-quiz-q">L'ultima domanda &egrave; una trappola travestita da esercizio facile.</h2>
  <p class="mot-quiz-expr">$$x^2+4$$</p>
  <div class="mot-cards">
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Quella scomposizione vale per $x^2-4$, non per $x^2+4$: il segno cambia tutto." onclick="mot_quiz(this)"><span class="mot-quiz-letter">A</span> $(x-2)(x+2)$</div>
    <div class="mot-card mot-quiz-card" data-correct="false" data-explain="Provalo: $(x+2)^2$ fa $x^2+4x+4$, non $x^2+4$. Il doppio prodotto proprio non c'è." onclick="mot_quiz(this)"><span class="mot-quiz-letter">B</span> $(x+2)^2$</div>
    <div class="mot-card mot-quiz-card" data-correct="true" data-explain="Esatto — una somma di quadrati non si scompone nei numeri reali: game over, con eleganza." onclick="mot_quiz(this)"><span class="mot-quiz-letter">C</span> Non si scompone in $\mathbb{R}$</div>
  </div>
  <p class="mot-quiz-explain"></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">FINE</h1>
  <p class="mot-joke fragment">il punteggio non conta, il fattore comune s&igrave;</p>
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

---
title: Al Limite, Ci Arrivo Anch'io
summary: Un'introduzione (poco seria) al concetto di limite
authors: [Diego Fantinelli]
tags: [analisi, limiti, introduzione]
categories: [analisi matematica]
date: "2026-08-04T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">un'introduzione poco seria</p>
  <h1>Al <span class="math-word">Limite</span>, Ci Arrivo Anch'io</h1>
  <p class="mot-tagline">tutto quello che sai già sui limiti, senza saperlo</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <blockquote class="mot-quote">
    "Al limite, ci arrivo anch'io" — modo di dire italiano che significa "se proprio è necessario, mi adeguo". Bene: in matematica significa qualcosa di completamente diverso. E anche di più interessante.
    <span class="quote-attr">&mdash; nessun matematico ha mai detto questo, ma avrebbe potuto</span>
  </blockquote>
</section>

<section>
  <p class="mot-kicker">confessione</p>
  <h2>Il Limite Che Fa Paura</h2>
  <p class="mot-def fragment">Ogni anno, in ogni classe, arriva questo momento: il professore scrive "lim" alla lavagna e qualcuno sussurra <b>"e mo' che è?"</b></p>
  <p class="mot-def fragment">Buona notizia: il concetto lo conosci già. Malissimo, per giunta — ma lo conosci. Lo usi da quando eri piccolo.</p>
  <p class="mot-joke fragment">spoiler: la parte difficile non è capirlo, è scriverlo bene</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO I</h1>
  <p class="mot-tagline">un problema vecchio di 2500 anni</p>
</section>

<section>
  <p class="mot-kicker">Elea, 450 a.C. circa</p>
  <h2>Achille e la Tartaruga</h2>
  <p class="mot-def fragment"><b>Zenone</b> propone una sfida: Achille, il più veloce dei Greci, fa una gara con una tartaruga. Per gentilezza, le dà 100 metri di vantaggio.</p>
  <p class="fragment" style="font-size:0.8em">Achille corre. Ma quando raggiunge il punto dove partiva la tartaruga, lei si è già mossa un po' più avanti.</p>
  <p class="fragment" style="font-size:0.8em">Quando Achille raggiunge <em>quel</em> punto, la tartaruga si è mossa ancora, anche se pochissimo.</p>
  <p class="fragment" style="font-size:0.8em">E così via, <b>all'infinito</b>.</p>
</section>

<section>
  <p class="mot-kicker">la conclusione (assurda)</p>
  <h2>Achille Non Vince Mai?</h2>
  <p class="mot-def fragment">Zenone conclude: Achille non raggiungerà <b>mai</b> la tartaruga. Ci sono infiniti passi da fare, uno dopo l'altro, e non si finisce mai di farli tutti.</p>
  <p class="mot-def fragment">Il problema è che tutti sappiamo, per esperienza diretta, che nella realtà Achille la sorpassa senza nemmeno accorgersene.</p>
  <p class="mot-joke fragment">il paradosso non è nella corsa. È nella matematica che (ancora) non c'era per spiegarla</p>
</section>

<section>
  <p class="mot-kicker">2000 anni di attesa</p>
  <h2>Chi Ha Risolto Il Problema?</h2>
  <p class="mot-def fragment">Non un antico, ma tanti matematici tra il 1600 e l'800: <b>Newton</b>, <b>Leibniz</b>, poi <b>Cauchy</b> e <b>Weierstrass</b> hanno messo ordine.</p>
  <p class="mot-def fragment">L'idea che li ha salvati tutti: infiniti passi, ciascuno piccolissimo, possono <em>sommarsi</em> a una distanza finita. E possono <em>avvicinarsi</em> a un valore preciso, senza mai raggiungerlo esattamente in un numero finito di passi.</p>
  <p class="mot-result fragment" style="font-size:0.85em; text-align:center; margin-top:1em;">Questa idea si chiama <b>limite</b>.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO II</h1>
  <p class="mot-tagline">il limite lo conosci già</p>
</section>

<section>
  <p class="mot-kicker">indovina l'analogia</p>
  <h2>Tre Situazioni, Stessa Idea</h2>
  <div class="mot-cards">
    <div class="mot-card fragment">
      <h3>Il parcheggio</h3>
      <p>Ti avvicini al muro col paraurti, sempre più piano, sempre più vicino. Non lo tocchi mai (si spera), ma la distanza diventa piccola quanto vuoi.</p>
    </div>
    <div class="mot-card fragment">
      <h3>La dieta</h3>
      <p>"Mi manca sempre l'ultimo chilo." Ti avvicini al peso forma, un po' alla volta, ma il traguardo sembra sempre a un passo di distanza.</p>
    </div>
    <div class="mot-card fragment">
      <h3>La batteria al 1%</h3>
      <p>Scende, scende, scende... e sembra non morire mai del tutto. (Poi muore sempre nel momento peggiore, ma quello è un altro teorema.)</p>
    </div>
  </div>
  <p class="mot-joke fragment">in tutti e tre i casi: ti avvicini quanto vuoi, senza necessariamente arrivare</p>
</section>

<section>
  <p class="mot-kicker">ora sul serio</p>
  <h2>La Stessa Idea, in Formule</h2>
  <p class="mot-def fragment">Prendi una funzione $f(x)$ e un valore $x_0$ a cui $x$ si avvicina, senza necessariamente raggiungerlo.</p>
  <p class="mot-def fragment">Ci chiediamo: cosa succede a $f(x)$ mentre $x$ si avvicina sempre di più a $x_0$?</p>
  <p class="mot-result fragment" style="font-size:1.1em; text-align:center; margin-top:1em;">$$\lim_{x \to x_0} f(x) = L$$</p>
  <p class="fragment" style="font-size:0.7em; text-align:center;">si legge: "il limite di $f(x)$, per $x$ che tende a $x_0$, è uguale a $L$"</p>
</section>

<section>
  <p class="mot-kicker">occhio alle parole</p>
  <h2>"Tende A", Non "È Uguale A"</h2>
  <p class="mot-def fragment">La parte più fraintesa: <b>$x \to x_0$</b> non vuol dire "$x$ vale $x_0$". Vuol dire "$x$ si avvicina sempre di più a $x_0$, restando diverso da $x_0$".</p>
  <p class="mot-def fragment">A volte $f(x_0)$ esiste e coincide col limite. A volte $f(x_0)$ non esiste nemmeno — e il limite esiste comunque.</p>
  <p class="mot-joke fragment">è la differenza tra "arrivare in stazione" e "vedere il treno che si avvicina"</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO III</h1>
  <p class="mot-tagline">tre destini possibili</p>
</section>

<section>
  <p class="mot-kicker">cosa può succedere</p>
  <h2>Non Tutti i Limiti Sono Uguali</h2>
  <div class="mot-cards">
    <div class="mot-card fragment">
      <h3>Limite finito</h3>
      <p>$f(x)$ si avvicina a un numero preciso $L$. È il caso "tranquillo", quello della dieta e del parcheggio.</p>
    </div>
    <div class="mot-card fragment">
      <h3>Limite infinito</h3>
      <p>$f(x)$ non si stabilizza da nessuna parte: cresce (o scende) senza freno. È il caso dell'asintoto verticale.</p>
    </div>
    <div class="mot-card fragment">
      <h3>Limite che non esiste</h3>
      <p>Avvicinandosi da sinistra o da destra, $f(x)$ va in due posti diversi. Il limite, semplicemente, non c'è.</p>
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">verità scomoda</p>
  <h2>Achille, Rivisitato</h2>
  <p class="mot-def fragment">Il tempo che impiega Achille per fare tutti gli infiniti "mezzi passi" di Zenone non è infinito: è un <b>limite finito</b>.</p>
  <p class="mot-def fragment">Infiniti passi, ciascuno più piccolo del precedente, sommati insieme, danno un tempo preciso e finito. Dopo quel tempo, Achille ha sorpassato la tartaruga.</p>
  <p class="mot-result fragment" style="text-align:center; margin-top:1em;">Il paradosso si scioglie. Ci sono voluti solo 2000 anni.</p>
</section>

---

<section>
  <p class="mot-kicker">la lezione</p>
  <h2>Quello Che i Limiti Insegnano</h2>
  <p class="mot-def fragment">L'infinito non è un numero enorme. È un <b>processo</b> che non finisce mai.</p>
  <p class="mot-def fragment">Il limite è lo strumento che ci permette di ragionare su questi processi senza impazzire, e di dare una risposta precisa a una domanda che sembra non averla.</p>
  <blockquote class="mot-quote fragment" style="margin-top:1.5em;">
    "L'infinito matematico non è che una parola, con la quale si designa una lunga eternità di passi finiti."
    <span class="quote-attr">&mdash; parafrasando Carl Friedrich Gauss</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ORA TOCCA A TE</h1>
  <p class="mot-tagline">la definizione vera, passo per passo, nella prossima lezione</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

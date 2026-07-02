---
title: The Complex Case — Spy Story
summary: Una thriller matematica dalla scoperta dei numeri complessi
authors: [Diego Fantinelli]
tags: [storia, numeri complessi, renaissance, tradimenti]
categories: [storia matematica]
date: "2026-07-02T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
  chalkboard:
    enable: true
    draw:
      scale: 2
      color: ['rgba(255,255,255,1)', 'rgba(237,111,92,1)']
    eraser:
      src: null
    storage: local
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">una storia di tradimenti e segreti</p>
  <h1>The <span class="math-word">Complex</span> Case</h1>
  <p class="mot-tagline">dalla scoperta dei numeri complessi al 1800</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; The Math of Things</p>
</section>

---

<section data-background-image="book_bkg.jpg" data-background-opacity="0.15">
  <blockquote class="mot-quote">
    La matematica è la poesia della logica. E come la poesia, a volte rivela verità che la realtà nega.
    <span class="quote-attr">&mdash; Parafrasando David Hilbert</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO I</h1>
  <p class="mot-tagline">L'enigma</p>
</section>

<section>
  <p class="mot-kicker">Bologna, 1520</p>
  <h2>Il Segreto di Dal Ferro</h2>
  <p class="mot-def fragment">Un matematico bolognese, <b>Scipione Dal Ferro</b>, scopre come risolvere le equazioni cubiche della forma $x^3 + px = q$.</p>
  <p class="fragment" style="font-size:0.8em">I Greci hanno risolto le equazioni di secondo grado duemila anni prima. Ma le <b>cubiche</b>? Ancora un mistero.</p>
  <p class="fragment" style="font-size:0.8em">Dal Ferro scopre il metodo. Poi — e qui comincia la storia — <b>non lo pubblica</b>. Lo trasmette segretamente al suo allievo <b>Antonio Maria Fior</b>.</p>
</section>

<section>
  <p class="mot-kicker">contesto storico</p>
  <h2>L'Italia del Cinquecento</h2>
  <p class="mot-def fragment">Una vera e propria <b>scuola di algebristi</b> italiani che si sfidano pubblicamente. Non per gloria scientifica: per <b>soldi</b>.</p>
  <dl class="mot-rows fragment" style="font-size:0.75em">
    <dt>Chi vince</dt><dd>ottiene fama, cattedre prestigiose, compensi dagli astrologhi</dd>
    <dt>Il contesto</dt><dd>non esiste ancora un sistema di pubblicazione scientifico. Vale il "vincolo del segreto professionale"</dd>
    <dt>L'ironia</dt><dd>UFC mediaevale della matematica: il combattimento avviene via problemi, non via libri</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">il colpo di scena</p>
  <h2>Perché le cubiche?</h2>
  <p class="mot-def fragment">Le equazioni di terzo grado non sono un capriccio accademico.</p>
  <p class="fragment" style="font-size:0.8em">Gli eserciti le usano per <b>calcolare le traiettorie delle catapulte</b>. Nel Rinascimento, il controllo militare passa per la matematica.</p>
  <p class="fragment" style="font-size:0.8em">Chi possiede la formula ha un vantaggio strategico. Da Ferro lo sa. Per questo la protegge.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO II</h1>
  <p class="mot-tagline">La sfida</p>
</section>

<section>
  <p class="mot-kicker">Venezia, 1535</p>
  <h2>Tartaglia vs Fior</h2>
  <p class="mot-def fragment"><b>Niccolò Tartaglia</b> riceve una sfida pubblica: risolvere trenta problemi cubici proposti da Antonio Maria Fior.</p>
  
  <div class="mot-cols" style="margin-top:1.5em;">
    <div class="mot-col fragment">
      <p style="font-size:0.63em; font-family:'JetBrains Mono', monospace; color:#666; line-height:1.5; margin-bottom:1.2em;">
        Il nome significa letteralmente "chi balbetta" — una ferita ricevuta nel Sacco di Brescia del 1512.
      </p>
      <p style="font-size:0.73em; line-height:1.6;">Tartaglia scopre il metodo pochi giorni prima. Per non dimenticarlo, lo codifica in una poesia criptica.</p>
    </div>
    <div class="mot-col fragment">
      <img src="tartaglia.png" alt="Niccolò Tartaglia" style="max-width:100%; max-height:580px; display:block; margin:0 auto;">
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">il risultato</p>
  <h2>La Vittoria Assoluta</h2>
  <p class="fragment">Tartaglia vince tutte e trenta le sfide.</p>
  <p class="fragment" style="font-size:0.8em">Fior? Zero su trenta. La matematica ha il suo vincitore.</p>
  <p class="mot-joke fragment">Ma Tartaglia, con una saggezza che contrassegnerà tutta la sua vita, <b>non pubblica la formula</b>. La tiene per sé — per ora.</p>
</section>

<section>
  <p class="mot-kicker">la poesia criptica</p>
  <h2>Tartaglia Codifica la Soluzione</h2>
  <p class="fragment" style="font-size:0.75em; text-align:left; max-width:95%; margin:0.5em auto; line-height:1.5;">
    <em>"Quando che'l cubo con le cose appresso<br>
    Se agguaglia à qualche numero discreto,<br>
    Trovan dui altri differenti in esso;<br>
    Dapoi terrai questo per consueto,<br>
    Che'l loro prodotto sempre sia eguale<br>
    Al terzo cubo delle cose nette."</em>
  </p>
  <p class="fragment" style="font-size:0.7em;">Una specie di <b>SMS criptato del 1500</b>. Solo chi conosce la chiave può decodificare il metodo.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO III</h1>
  <p class="mot-tagline">Il tradimento</p>
</section>

<section>
  <p class="mot-kicker">Milano, 1545</p>
  <h2>Gerolamo Cardano e l'Ars Magna</h2>
  <p class="mot-def fragment">Gerolamo Cardano, matematico e astrologo, ottiene da Tartaglia la formula <b>con una promessa solenne</b>: non divulgarla.</p>
  
  <div class="mot-cols" style="margin-top:1.5em;">
    <div class="mot-col fragment">
      <p style="font-size:0.75em; line-height:1.6; margin-bottom:1em;">Pochi anni dopo, Cardano pubblica l'<em>Ars Magna</em> — "La Grande Arte" — e <b>include la formula</b>.</p>
      <p style="font-size:0.75em; color:#ed6f5c; font-weight:600;">Attribuisce parte del merito a Tartaglia (gratitudine relativa).</p>
      <p style="font-size:0.7em; margin-top:1em;">Tartaglia sarà ricordato come "quello che l'ha rivelata a Cardano".</p>
    </div>
    <div class="mot-col fragment">
      <img src="cardano.png" alt="Gerolamo Cardano" style="max-width:100%; max-height:500px; display:block; margin:0 auto;">
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">chi era Cardano</p>
  <h2>Un Uomo dalle Mille Facce</h2>
  <dl class="mot-rows" style="font-size:0.8em;">
    <dt class="fragment">Medico</dt><dd class="fragment">rinomato, forse il migliore d'Italia</dd>
    <dt class="fragment">Astrologo</dt><dd class="fragment">consulente pagato profumatamente</dd>
    <dt class="fragment">Matematico</dt><dd class="fragment">autore dell'Ars Magna</dd>
    <dt class="fragment">Giocatore d'azzardo</dt><dd class="fragment">usava la matematica per barare ai giochi</dd>
  </dl>
  <p class="fragment" style="font-size:0.75em; margin-top:1.5em; color:#666;">Nel 1570, il Papa lo fa arrestare per eresia. L'accusa principale? Aver scritto l'oroscopo di Gesù Cristo. Muore povero e dimenticato.</p>
</section>

<section>
  <p class="mot-kicker">la formula di Cardano</p>
  <h2>La Soluzione Esplicita</h2>
  <p class="mot-def fragment">Per un'equazione $x^3 + px + q = 0$:</p>
  <p class="mot-result fragment">$$x = \sqrt[3]{-\frac{q}{2} + \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\left(\frac{q}{2}\right)^2 + \left(\frac{p}{3}\right)^3}}$$</p>
  <p class="fragment" style="font-size:0.75em;">Ora il metodo è pubblico. Perfetto, no?</p>
  <p class="mot-joke fragment" style="font-size:0.75em;"><b>No.</b> C'è un problema molto serio che nessuno aveva ancora affrontato.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO IV</h1>
  <p class="mot-tagline">L'anomalia irriducibile</p>
</section>

<section>
  <p class="mot-kicker">il paradosso</p>
  <h2>L'Equazione Maledetta</h2>
  <p class="mot-def fragment">Considerare l'equazione: $x^3 = 15x + 4$</p>
  <p class="fragment" style="font-size:0.8em;">Si sa con <b>certezza</b> che una soluzione è $x = 4$.</p>
  <p class="fragment" style="font-size:0.75em;">(Verifica: $4^3 = 64$ e $15 \cdot 4 + 4 = 64$. Uguale.)</p>
  <p class="mot-result fragment" style="margin-top:1.5em;">$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}$$</p>
  <p class="fragment" style="font-size:0.8em; color:#e74c3c; font-weight:600;">Ma aspetta. $\sqrt{-121}$ non esiste nei numeri reali.</p>
</section>

<section>
  <p class="mot-kicker">il colpo di scena</p>
  <h2>Il Tunnel Buio</h2>
  <p class="mot-def fragment">La formula contiene <b>radici quadrate di numeri negativi</b>.</p>
  <p class="fragment" style="font-size:0.8em;">Eppure, l'equazione ha una soluzione reale: $x = 4$.</p>
  <p class="fragment" style="font-size:0.8em;">È come se la formula passasse per un tunnel buio e imperscrutabile, e ne uscisse con la risposta corretta.</p>
  <p class="mot-joke fragment" style="font-size:0.75em;">Un'anomalia nel codice della realtà.</p>
</section>

<section>
  <p class="mot-kicker">il discriminante</p>
  <h2>Il Caso Irriducibile</h2>
  <p class="mot-def fragment">Il termine critico è il <b>discriminante</b>:</p>
  <p class="mot-result fragment">$$\Delta = \frac{q^2}{4} - \frac{p^3}{27}$$</p>
  <dl class="mot-rows" style="font-size:0.8em; margin-top:1.5em;">
    <dt class="fragment">Se $\Delta > 0$</dt><dd class="fragment">tutto ok, niente strane</dd>
    <dt class="fragment">Se $\Delta < 0$</dt><dd class="fragment">il caso irriducibile — radici di numeri negativi</dd>
  </dl>
  <p class="fragment" style="font-size:0.75em; margin-top:1.5em;">Nel nostro esempio: $\Delta = 4 - 125 = -121$ (negativo). Anomalia confermata.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO V</h1>
  <p class="mot-tagline">La rivelazione</p>
</section>

<section>
  <p class="mot-kicker">Bologna, 1560</p>
  <h2>Rafael Bombelli e l'Illuminazione</h2>
  <p class="mot-def fragment">Rafael Bombelli studia il caso irriducibile con ossessione scientifica.</p>
  
  <div class="mot-cols" style="margin-top:1.5em;">
    <div class="mot-col fragment">
      <p style="font-size:0.8em; line-height:1.6;">Decide di <b>osare l'impossibile</b>: e se le radici di numeri negativi <b>esistessero davvero</b>? Non come numeri reali, ma come una nuova categoria?</p>
    </div>
    <div class="mot-col fragment">
      <img src="bombelli.png" alt="Rafael Bombelli" style="max-width:100%; max-height:500px; display:block; margin:0 auto;">
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">l'idea geniale</p>
  <h2>Più di Meno e Meno di Meno</h2>
  <p class="mot-def fragment">Bombelli introduce nuove notazioni:</p>
  <dl class="mot-rows" style="font-size:0.85em;">
    <dt class="fragment">"Più di meno"</dt><dd class="fragment">abbreviato $p.d.m$, rappresenta $+i$</dd>
    <dt class="fragment">"Meno di meno"</dt><dd class="fragment">abbreviato $m.d.m$, rappresenta $-i$</dd>
  </dl>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Dove $i$ è l'<b>unità immaginaria</b>: $i = \sqrt{-1}$</p>
  <p class="mot-joke fragment" style="font-size:0.8em;">Sembrerebbe pazzo. <b>Ma funziona.</b></p>
</section>

<section>
  <p class="mot-kicker">il calcolo miracoloso</p>
  <h2>Da Bombelli ai Numeri Complessi</h2>
  <p class="fragment" style="font-size:0.8em;">Bombelli scopre (con tentativi pazientissimi):</p>
  <p class="mot-result fragment">$$(2 + i)^3 = 2 + 11i$$</p>
  <p class="mot-result fragment">$$(2 - i)^3 = 2 - 11i$$</p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Quindi:</p>
  <p style="text-align:center; font-size:0.8em;">$\sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}} = (2+i) + (2-i) = 4$</p>
  <p class="mot-joke fragment" style="font-size:0.75em;">La risposta reale emerge dal caos immaginario.</p>
</section>

<section>
  <p class="mot-kicker">la conseguenza</p>
  <h2>Il Reale e l'Immaginario sono Intrecciati</h2>
  <p class="mot-def fragment">Bombelli riconosce una verità profonda: i numeri complessi non sono invenzioni. Sono strumenti per scoprire verità nascoste.</p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Ma il mondo scientifico rimane scettico. Cartesio chiama questi numeri "immaginari" con tono dispregiativo. Significa: "Figmenti dell'immaginazione, non veri numeri".</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO VI</h1>
  <p class="mot-tagline">Gli alleati</p>
</section>

<section>
  <p class="mot-kicker">1702 — Abraham de Moivre</p>
  <h2>Il Legame con la Trigonometria</h2>
  <p class="mot-def fragment">De Moivre scopre il legame fondamentale tra numeri complessi e trigonometria:</p>
  <p class="mot-result fragment">$$z^n = r^n (\cos(n\theta) + i\sin(n\theta))$$</p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Questa formula semplifica il calcolo delle potenze di numeri complessi e getta le basi per lo studio delle radici complesse.</p>
  <p class="mot-joke fragment" style="font-size:0.75em;">Aneddoto: De Moivre calcolò la sua data di morte stimando quanto dormiva ogni giorno. Morì il giorno previsto.</p>
</section>

<section>
  <p class="mot-kicker">1748 — Leonhard Euler</p>
  <h2>La Formula più Bella della Matematica</h2>
  <p class="mot-def fragment">Euler formalizza il legame sublime tra numeri complessi, esponenziali e trigonometria:</p>
  <p class="mot-result fragment">$$e^{ix} = \cos x + i\sin x$$</p>
  <p class="fragment" style="font-size:0.8em;">Dal caso particolare $x = \pi$:</p>
  <p class="mot-result fragment" style="font-size:1.2em;">$$e^{i\pi} + 1 = 0$$</p>
</section>

<section>
  <p class="mot-kicker">perché è bellissima</p>
  <h2>Cinque Costanti in Una Formula</h2>
  <div class="mot-cards" style="font-size:0.8em;">
    <div class="mot-card fragment">
      <h3>e</h3>
      <p>La base dei logaritmi naturali</p>
    </div>
    <div class="mot-card fragment">
      <h3>i</h3>
      <p>L'unità immaginaria</p>
    </div>
    <div class="mot-card fragment">
      <h3>π</h3>
      <p>La costante del cerchio</p>
    </div>
    <div class="mot-card fragment">
      <h3>1</h3>
      <p>L'identità moltiplicativa</p>
    </div>
    <div class="mot-card fragment">
      <h3>0</h3>
      <p>L'identità additiva</p>
    </div>
  </div>
  <p class="mot-joke fragment" style="font-size:0.75em; margin-top:1em;">Cinque delle costanti più importanti della matematica in un'unica equazione elegantissima.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ATTO VII</h1>
  <p class="mot-tagline">La conclusione</p>
</section>

<section>
  <p class="mot-kicker">1797-1799 — Carl Friedrich Gauss</p>
  <h2>Il Piano Complesso</h2>
  <div class="mot-cols">
    <div class="mot-col fragment">
      <p class="mot-def">Gauss riconosce i numeri complessi come <b>veri e propri numeri</b>. Conia il termine "numeri complessi".</p>
      <p style="font-size:0.8em; margin-top:1em;">Introduce la rappresentazione <b>geometrica</b>: il piano complesso. Parte reale sull'asse x, parte immaginaria sull'asse y.</p>
    </div>
    <div class="mot-col fragment">
      <img src="gauss.png" alt="Carl Friedrich Gauss" style="max-width:100%; max-height:420px; display:block; margin:0 auto;">
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">la geometria</p>
  <h2>Il Piano Complesso di Gauss</h2>
  <p class="mot-def fragment">Un numero complesso $z = a + bi$ è rappresentato come un punto $(a, b)$ nel piano.</p>
  <p class="mot-result fragment">$$|z| = \sqrt{a^2 + b^2}$$</p>
  <p class="fragment" style="font-size:0.8em;">Il <b>modulo</b> (o norma) è la distanza dall'origine.</p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Questa rappresentazione trasforma l'astratto in visibile e permette di applicare la geometria all'algebra.</p>
</section>

<section>
  <p class="mot-kicker">la critica</p>
  <h2>Gauss Difende i Numeri Complessi</h2>
  <p class="mot-def fragment">Gauss criticava aspramente chi chiamava i numeri complessi "impossibili".</p>
  <p class="mot-quote fragment">
    "Sono essenziali per una matematica più profonda. Chi ancora li rifiuta non ha capito nulla della struttura della realtà matematica."
  </p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">E aveva assolutamente ragione.</p>
</section>

---

<section class="mot-divider" data-background-image="numbers.gif" data-background-opacity="0.15" data-transition="zoom">
  <h1 class="r-fit-text">EPILOGO</h1>
  <p class="mot-tagline">L'eredità nel mondo reale</p>
</section>

<section>
  <p class="mot-kicker">1890s — Charles Steinmetz</p>
  <h2>L'Ingegnere che Produsse Elettricità</h2>
  <p class="mot-def fragment">Charles Steinmetz, ingegnere elettrotecnico tedesco, scopre che i numeri complessi descrivono <b>perfettamente</b> il comportamento delle correnti alternate.</p>
  <p class="fragment" style="font-size:0.8em; margin-top:1.5em;">Ingegneri e fisici iniziano a usarli per analizzare circuiti, onde, trasformatori.</p>
  <p class="mot-quote fragment">
    "Ha prodotto elettricità tramite i numeri complessi."
  </p>
  <p class="fragment" style="font-size:0.75em;">Una frase che cattura l'ironia perfetta: i "numeri impossibili" di Cardano guidano la tecnologia moderna.</p>
</section>

<section>
  <p class="mot-kicker">applicazioni moderne</p>
  <h2>Dove Vivono i Numeri Complessi Oggi</h2>
  <dl class="mot-rows" style="font-size:0.8em;">
    <dt class="fragment">Ingegneria elettrica</dt><dd class="fragment">Analisi dei circuiti AC, impedenze, trasformatori</dd>
    <dt class="fragment">Fisica</dt><dd class="fragment">Meccanica quantistica, teoria dei campi, relatività</dd>
    <dt class="fragment">Processamento del segnale</dt><dd class="fragment">Trasformate di Fourier, compressione audio e immagini</dd>
    <dt class="fragment">Grafica 3D</dt><dd class="fragment">Rotazioni, trasformazioni, animazioni</dd>
    <dt class="fragment">Aerodinamica</dt><dd class="fragment">Flusso di fluidi, profili alari</dd>
  </dl>
</section>

---

<section>
  <p class="mot-kicker">la trama completa</p>
  <h2>Dal Mistero alla Scoperta</h2>
  <div class="mot-cards" style="font-size:0.75em;">
    <div class="mot-card fragment">
      <h3>Dal Ferro (1520)</h3>
      <p>Scopre il segreto</p>
    </div>
    <div class="mot-card fragment">
      <h3>Tartaglia (1535)</h3>
      <p>Lo generalizza, lo codifica</p>
    </div>
    <div class="mot-card fragment">
      <h3>Cardano (1545)</h3>
      <p>Lo tradisce, lo pubblica</p>
    </div>
    <div class="mot-card fragment">
      <h3>Bombelli (1560)</h3>
      <p>Scopre il nemico vero: i numeri impossibili</p>
    </div>
    <div class="mot-card fragment">
      <h3>De Moivre, Euler (1700s)</h3>
      <p>Lo capiscono, lo formalizzano</p>
    </div>
    <div class="mot-card fragment">
      <h3>Gauss (1799)</h3>
      <p>Lo legittima matematicamente</p>
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">la lezione</p>
  <h2>Quello che I Numeri Complessi Insegnano</h2>
  <p class="mot-def fragment">La matematica non <b>inventa</b> nuovi numeri per capriccio.</p>
  <p class="mot-def fragment">Li <b>scopre</b> quando ha bisogno di loro.</p>
  <p class="mot-def fragment" style="margin-top:1.5em;">Spesso, quello che sembra "impossibile" è semplicemente una prospettiva che ancora non abbiamo.</p>
  <p class="mot-quote fragment" style="margin-top:2em;">
    "Non conosciamo, perché non abbiamo imparato a cercare nel posto giusto." — Carl Friedrich Gauss
  </p>
</section>

---

<section class="mot-divider" data-background-image="numbers.gif" data-background-opacity="0.25" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-tagline">la storia non è finita</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

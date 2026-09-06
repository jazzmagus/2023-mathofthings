---
title: Studiare (con l'IA)
summary: Metodo di studio, ieri e oggi, tra internet e intelligenza artificiale
authors: [Diego Fantinelli]
tags: [organizzazione, metodo-di-studio, AI]
categories: [lesson]
date: "2026-09-06T00:00:00Z"
draft: false
unlisted: true
slides:
  theme: mathofthings
  transition: convex
  particles: true
  particlesColorLight: "#2f8fbf"
  particlesColorDark: "#63c2e8"
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
  <p class="mot-kicker">metodo di studio</p>
  <h1>Studiare con<br>L'intelligenza<br><em>artificiale</em></h1>
  <p class="mot-tagline">breve storia di come si studia la matematica &mdash; da prima di internet a <em>oggi</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DI INTERNET</h1>
  <p class="mot-joke fragment">quando "cercare su Google" si chiamava "andare in biblioteca"</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Come si studiava <em>prima</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DELL'IA</h1>
  <p class="mot-joke fragment">l'era di Wikipedia, YouTube e "fidati, l'ho letto da qualche parte"</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Internet, ma senza <em>l'IA</em></h2>
  <p class="fragment">Contenuto da definire.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">OGGI</h1>
  <p class="mot-joke fragment">studiare con l'IA, senza farsi studiare dall'IA</p>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Studiare oggi con <em>l'IA</em></h2>
  <p class="fragment">Un approfondimento:<br><a href="/post/chi-ha-paura-ia/" target="_blank" class="mono" style="display:inline-flex; align-items:center; gap:0.4em;">
    <svg width="0.9em" height="0.9em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    Chi ha paura dell'Intelligenza Artificiale?
  </a></p>
  <p class="mot-def fragment">L'intelligenza artificiale ha cambiato, e non poco, l'approccio allo studio: porta con sé dei benefici innegabili, ma anche qualche controindicazione precisa. Quello che segue non è il solito discorso da "ai miei tempi si studiava meglio" &mdash; pesiamo pro e contro appoggiandoci a quello che la psicologia cognitiva sa già da tempo su come si impara davvero.</p>
</section>

<section>
  <p class="mot-kicker">i contro</p>
  <h2>Gli <em>svantaggi</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>illusione di comprensione</dt><dd>capire una spiegazione non significa saperla rifare da soli</dd>
    <dt>dipendenza dal procedimento altrui</dt><dd>se risolve l'IA, non sviluppi un tuo metodo</dd>
    <dt>errori detti con sicurezza</dt><dd>senza basi solide, non riconosci un passaggio sbagliato</dd>
    <dt>nessun controllo in tempo reale</dt><dd>in verifica, all'orale, alla lavagna, l'IA non c'è</dd>
    <dt>il tempo risparmiato si paga altrove</dt><dd>meno fatica ora, meno allenamento dopo</dd>
  </dl>
  <p class="mot-source fragment">Non è impressione: lo psicologo Robert Bjork (UCLA) la chiama "illusione di fluidità" &mdash; capire sembra facile solo perché qualcun altro l'ha spiegato bene. E Roediger &amp; Karpicke (2006) hanno mostrato che è il tentativo di ricordare, non la rilettura, a fissare davvero la conoscenza.</p>
</section>

<section>
  <p class="mot-kicker">i pro</p>
  <h2>I <em>vantaggi</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>disponibilità immediata</dt><dd>il dubbio si risolve subito, non il giorno dopo</dd>
    <dt>spiegazioni su misura</dt><dd>puoi farti spiegare la stessa cosa in modi diversi finché non "clicca"</dd>
    <dt>esercizi illimitati</dt><dd>ne generi quanti ne vuoi, sul tuo livello esatto</dd>
    <dt>verifica dei propri passaggi</dt><dd>fai controllare un tuo ragionamento senza aspettare la correzione</dd>
    <dt>nessun giudizio sulla domanda "stupida"</dt><dd>puoi chiedere la cosa più elementare senza il filtro della classe</dd>
  </dl>
  <p class="mot-source fragment">Non è solo comodità: è quella che lo psicologo Lev Vygotskij chiamava "zona di sviluppo prossimale" &mdash; il ruolo di un buon aiuto è farti fare un passo che da solo non faresti ancora, ma che presto farai senza aiuto.</p>
</section>

<section>
  <p class="mot-kicker">il bilancio</p>
  <h2>Come cambia <em>(in meglio)</em> il metodo di studio</h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>da cercare a dialogare</dt><dd>dalla ricerca passiva della risposta a una conversazione che guidi tu</dd>
    <dt>da leggere a verificare</dt><dd>il centro si sposta dal "leggere e ricordare" al "chiedere, verificare, rifare da solo"</dd>
    <dt>un allenatore, non un sostituto</dt><dd>allena quello che sai già fare, non ti regala quello che non sai fare</dd>
    <dt>il controllo tocca a te</dt><dd>un libro di testo non ti mente, un'IA a volte sì</dd>
    <dt>il tempo va reinvestito</dt><dd>meno tempo perso a cercare, più tempo vero a esercitarsi</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">L'ARTE DEL PROMPTING</h1>
  <p class="mot-joke fragment">perché "fammi il compito" non è un prompt, è una resa</p>
</section>

<section>
  <p class="mot-kicker">il principio base</p>
  <h2>Garbage in, <em>garbage out</em></h2>
  <p class="mot-def fragment">Il risultato che ottieni dipende, quasi interamente, da come formuli la domanda: un prompt vago produce nella migliore delle ipotesi una risposta generica, nella peggiore una risposta sbagliata detta con sicurezza.</p>
  <p class="fragment">Studiare con l'IA è anche imparare a farle le domande giuste — non è un dettaglio tecnico, è la competenza vera.</p>
  <p class="mot-source fragment">Lo psicologo Michelene Chi ha chiamato "self-explanation effect" il fatto che spiegare a parole proprie un ragionamento &mdash; anche solo a un'IA &mdash; produce più apprendimento che limitarsi a leggere una spiegazione già pronta.</p>
</section>

<section>
  <p class="mot-kicker">come si scrive un buon prompt</p>
  <h2>Contesto e <em>specificità</em></h2>
  <dl class="mot-rows fragment">
    <dt>cosa</dt><dd>l'argomento esatto, non "aiutami con la matematica" — quale argomento, quale esercizio, quale passaggio</dd>
    <dt>livello</dt><dd>dì che classe fai e cosa hai già studiato: una spiegazione da terza superiore non serve in quinta, e viceversa</dd>
    <dt>formato</dt><dd>chiedi passaggi, non solo il risultato finale — è quello che dovrai saper rifare da solo</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">la trappola più comune</p>
  <h2>Il procedimento, non <em>la soluzione</em></h2>
  <p class="fragment">Chiedere direttamente "qual è il risultato" produce uno studente che sa copiare, non uno studente che sa risolvere.</p>
  <ul class="fragment">
    <li class="fragment">"spiegami perché si fa così, non solo come"</li>
    <li class="fragment">"fammi una domanda per verificare se ho capito"</li>
    <li class="fragment">"correggimi solo se sbaglio un passaggio, non anticipare la soluzione"</li>
  </ul>
  <p class="mot-source fragment">Non è una mia opinione: uno studio del 2024 su studenti liceali (Bastani et al., Università della Pennsylvania) ha misurato esattamente questa differenza &mdash; un chatbot che dà la soluzione pronta peggiora i risultati alle verifiche, uno vincolato a fare da tutor socratico li migliora.</p>
</section>

<section>
  <p class="mot-kicker">esempio pratico — 1</p>
  <h2>Un'equazione, e non <em>solo</em></h2>
  <dl class="mot-rows fragment">
    <dt>prompt debole</dt><dd>"risolvimi questa equazione di secondo grado"</dd>
    <dt>prompt efficace</dt><dd>"sono in terza superiore e sto studiando le equazioni di secondo grado con la formula risolutiva: risolvi con me questo esercizio passo passo, spiegando ogni passaggio senza saltarne nessuno; poi proponimi altri due esercizi simili, e guidami passo passo nella soluzione di ciascuno, uno alla volta"</dd>
  </dl>
  <p class="mot-joke fragment">così, quando servono esercizi in più per fare pratica, non serve andarli a cercare: te li costruisci da solo</p>
</section>

<section>
  <p class="mot-kicker">esempio pratico — 2</p>
  <h2>Prima di <em>iniziare</em></h2>
  <p class="fragment">Un buon prompt non serve solo a risolvere un esercizio: può servire anche a organizzare il lavoro, prima ancora di iniziarlo.</p>
  <dl class="mot-rows fragment">
    <dt>prompt</dt><dd>"prima di affrontare questo problema, elencami quali conoscenze e abilità mi servono per risolverlo; poi fammi qualche domanda per verificare se le possiedo tutte"</dd>
  </dl>
  <p class="mot-joke fragment">scoprire di non avere un prerequisito prima di iniziare l'esercizio è utile — scoprirlo a metà, molto meno</p>
</section>

---

<section class="mot-divider" data-transition="zoom" data-background-image="doubts.jpg" data-background-opacity="0.6">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">le vostre domande fatele a me — quelle all'IA, scommetto, gliele avete già fatte</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon anno scolastico</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

<style>
body.slides-mot {
  --mot-primary: #2f8fbf;
  --r-link-color: #2f8fbf;
  --r-link-color-hover: #57abd6;
  --r-selection-background-color: rgba(47, 143, 191, 0.35);
}

body.slides-mot.dark {
  --mot-primary: #63c2e8;
  --r-link-color: #63c2e8;
  --r-link-color-hover: #8ad3ee;
}

body.slides-mot .reveal dl.mot-rows-narrow {
  grid-template-columns: 9em 1fr;
}

body.slides-mot .reveal dl.mot-rows-narrow dt {
  white-space: normal;
  line-height: 1.25;
}

.mot-source {
  font-family: var(--mot-mono);
  font-size: 0.4em;
  color: var(--mot-muted);
  font-style: normal;
  line-height: 1.5;
  margin-top: 1em;
  max-width: 85%;
  text-align: left;
  border-left: 2px solid var(--mot-primary);
  padding-left: 0.8em;
}

</style>

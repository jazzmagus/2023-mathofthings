---
title: Esponenziali e Logaritmi
summary: Introduzione con i modelli della vita reale — tema mathofthings
authors: [Diego Fantinelli]
tags: [esponenziali, logaritmi, modelli]
categories: [lesson]
date: "2026-07-06T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">matematica per il triennio</p>
  <h1>Esponenziali e <span class="math-word">Logaritmi</span></h1>
  <p class="mot-tagline">la matematica che <em>cresce</em> e quella che <em>misura</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <blockquote class="mot-quote">
    Il più grande difetto della razza umana è la nostra incapacità di comprendere la funzione esponenziale.
    <span class="quote-attr">&mdash; Albert A. Bartlett, fisico</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">CRESCITA</h1>
</section>

<section>
  <p class="mot-kicker">una leggenda</p>
  <h2>Il chicco di riso e la <em>scacchiera</em></h2>
  <p class="mot-def fragment">Un inventore chiede al re un premio: <b>un chicco</b> di riso sulla prima casella, <b>due</b> sulla seconda, <b>quattro</b> sulla terza&hellip; raddoppiando ogni volta.</p>
  <p class="fragment" style="font-size:0.8em">Sulla casella $n$ ci sono $2^{\,n-1}$ chicchi. Sull'ultima:</p>
  <p class="mot-result fragment">$$2^{63} \approx 9.2 \times 10^{18}$$</p>
  <p class="fragment" style="font-size:0.72em">Più riso di quanto il mondo intero ne produca in secoli.</p>
  <p class="mot-joke fragment">il re non aveva studiato le esponenziali</p>
</section>

<section>
  <p class="mot-kicker">definizione</p>
  <h2>La funzione <em>esponenziale</em></h2>
  <p class="mot-result fragment">$$y = a^x \qquad (a>0,\; a\neq 1)$$</p>
  <div class="mot-cols">
    <div class="mot-col fragment" style="font-size:0.68em">
      <p>se $a>1$ &rarr; la funzione <b>cresce</b></p>
      <p>se $0 \lt a \lt 1$ &rarr; la funzione <b>decresce</b></p>
      <p>passa sempre per $(0,1)$ e resta <b>positiva</b></p>
    </div>
    <div class="mot-col fragment">
      <svg viewBox="0 0 500 320" style="width:100%;max-width:540px" role="img" aria-label="funzioni esponenziali crescente e decrescente">
        <line x1="210.0" y1="50.0" x2="210.0" y2="270.0" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <line x1="50.0" y1="270.0" x2="450.0" y2="270.0" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <path d="M50.0 263.1 L54.0 262.9 L58.1 262.6 L62.1 262.4 L66.2 262.1 L70.2 261.8 L74.2 261.5 L78.3 261.2 L82.3 260.9 L86.4 260.6 L90.4 260.2 L94.4 259.9 L98.5 259.5 L102.5 259.2 L106.6 258.8 L110.6 258.4 L114.6 258.0 L118.7 257.5 L122.7 257.1 L126.8 256.6 L130.8 256.2 L134.8 255.7 L138.9 255.1 L142.9 254.6 L147.0 254.1 L151.0 253.5 L155.1 252.9 L159.1 252.3 L163.1 251.7 L167.2 251.0 L171.2 250.3 L175.3 249.6 L179.3 248.9 L183.3 248.2 L187.4 247.4 L191.4 246.6 L195.5 245.8 L199.5 244.9 L203.5 244.0 L207.6 243.1 L211.6 242.1 L215.7 241.1 L219.7 240.1 L223.7 239.0 L227.8 237.9 L231.8 236.8 L235.9 235.6 L239.9 234.4 L243.9 233.1 L248.0 231.8 L252.0 230.4 L256.1 229.0 L260.1 227.6 L264.1 226.0 L268.2 224.5 L272.2 222.9 L276.3 221.2 L280.3 219.4 L284.3 217.6 L288.4 215.8 L292.4 213.8 L296.5 211.8 L300.5 209.8 L304.5 207.6 L308.6 205.4 L312.6 203.1 L316.7 200.7 L320.7 198.2 L324.7 195.7 L328.8 193.0 L332.8 190.3 L336.9 187.4 L340.9 184.5 L344.9 181.5 L349.0 178.3 L353.0 175.0 L357.1 171.7 L361.1 168.2 L365.2 164.5 L369.2 160.8 L373.2 156.9 L377.3 152.8 L381.3 148.7 L385.4 144.3 L389.4 139.9 L393.4 135.2 L397.5 130.4 L401.5 125.5 L405.6 120.3 L409.6 115.0 L413.6 109.5 L417.7 103.7 L421.7 97.8 L425.8 91.7 L429.8 85.3 L433.8 78.7 L437.9 71.9 L441.9 64.9 L446.0 57.6 L450.0 50.0" style="fill:none;stroke:var(--mot-primary);stroke-width:3.5;stroke-linecap:round"/>
        <path d="M50.0 160.0 L54.0 163.8 L58.1 167.4 L62.1 171.0 L66.2 174.4 L70.2 177.7 L74.2 180.8 L78.3 183.9 L82.3 186.9 L86.4 189.7 L90.4 192.5 L94.4 195.2 L98.5 197.7 L102.5 200.2 L106.6 202.6 L110.6 204.9 L114.6 207.2 L118.7 209.3 L122.7 211.4 L126.8 213.4 L130.8 215.4 L134.8 217.3 L138.9 219.1 L142.9 220.8 L147.0 222.5 L151.0 224.2 L155.1 225.7 L159.1 227.3 L163.1 228.7 L167.2 230.1 L171.2 231.5 L175.3 232.8 L179.3 234.1 L183.3 235.4 L187.4 236.5 L191.4 237.7 L195.5 238.8 L199.5 239.9 L203.5 240.9 L207.6 241.9 L211.6 242.9 L215.7 243.8 L219.7 244.7 L223.7 245.6 L227.8 246.4 L231.8 247.2 L235.9 248.0 L239.9 248.8 L243.9 249.5 L248.0 250.2 L252.0 250.9 L256.1 251.5 L260.1 252.2 L264.1 252.8 L268.2 253.4 L272.2 254.0 L276.3 254.5 L280.3 255.0 L284.3 255.6 L288.4 256.1 L292.4 256.5 L296.5 257.0 L300.5 257.4 L304.5 257.9 L308.6 258.3 L312.6 258.7 L316.7 259.1 L320.7 259.5 L324.7 259.8 L328.8 260.2 L332.8 260.5 L336.9 260.8 L340.9 261.2 L344.9 261.5 L349.0 261.8 L353.0 262.0 L357.1 262.3 L361.1 262.6 L365.2 262.8 L369.2 263.1 L373.2 263.3 L377.3 263.5 L381.3 263.8 L385.4 264.0 L389.4 264.2 L393.4 264.4 L397.5 264.6 L401.5 264.8 L405.6 264.9 L409.6 265.1 L413.6 265.3 L417.7 265.5 L421.7 265.6 L425.8 265.8 L429.8 265.9 L433.8 266.0 L437.9 266.2 L441.9 266.3 L446.0 266.4 L450.0 266.6" style="fill:none;stroke:#3a6b8c;stroke-width:3;stroke-linecap:round"/>
        <circle cx="210.0" cy="242.5" r="4.5" style="fill:var(--mot-primary)"/>
        <text x="218.0" y="234.5" style="font-family:var(--mot-mono);font-size:13px;fill:var(--mot-muted)">(0,1)</text>
        <text x="420.0" y="80.0" style="font-family:var(--mot-mono);font-size:14px;fill:var(--mot-primary)">a&gt;1</text>
        <text x="420.0" y="290.0" style="font-family:var(--mot-mono);font-size:14px;fill:#3a6b8c">0&lt;a&lt;1</text>
      </svg>
    </div>
  </div>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MODELLI</h1>
  <p class="mot-tagline" style="font-family:'JetBrains Mono',monospace; font-size:0.5em">la crescita intorno a <em>noi</em></p>
</section>

<section>
  <p class="mot-kicker">economia</p>
  <h2>L'interesse <em>composto</em></h2>
  <p class="mot-def fragment">Un capitale $C_0$ a tasso annuo $i$, dopo $t$ anni, diventa:</p>
  <p class="mot-result fragment">$$C(t) = C_0\,(1+i)^{\,t}$$</p>
  <p class="fragment" style="font-size:0.74em">A un tasso del $5\%$, un capitale <b>raddoppia</b> in circa $14$ anni: gli interessi generano interessi, ed è crescita esponenziale.</p>
  <p class="mot-joke fragment">Einstein l'avrebbe chiamata l'ottava meraviglia del mondo</p>
</section>

<section>
  <p class="mot-kicker">epidemiologia</p>
  <h2>La curva del <em>contagio</em></h2>
  <div class="mot-cols">
    <div class="mot-col fragment" style="font-size:0.66em">
      <p>All'inizio di un'epidemia ogni infetto ne contagia altri: i casi <b>raddoppiano</b> a intervalli regolari.</p>
      <p class="mot-result" style="font-size:0.8em">$$I(t) = I_0\, R_0^{\,t}$$</p>
      <p>$R_0$ = contagi per infetto. Se $R_0>1$ &rarr; esplosione esponenziale.</p>
    </div>
    <div class="mot-col fragment">
      <svg viewBox="0 0 460 290" style="width:100%;max-width:440px" role="img" aria-label="curva del contagio">
        <line x1="60" y1="260" x2="440" y2="260" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <line x1="60" y1="20" x2="60" y2="270" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <path d="M60 255 C 180 252 262 244 330 208 C 382 178 414 108 436 32" style="fill:none;stroke:var(--mot-primary);stroke-width:3.5;stroke-linecap:round"/>
        <text x="24" y="40" style="font-family:var(--mot-mono);font-size:13px;fill:var(--mot-muted)" transform="rotate(-90 24 40)">casi</text>
        <text x="390" y="278" style="font-family:var(--mot-mono);font-size:13px;fill:var(--mot-muted)">tempo</text>
      </svg>
    </div>
  </div>
  <p class="mot-joke fragment">&laquo;flatten the curve&raquo; era, letteralmente, addomesticare un'esponenziale</p>
</section>

<section>
  <p class="mot-kicker">il modello SIR</p>
  <h2>Sani, Infetti, <em>Rimossi</em></h2>
  <svg viewBox="0 0 520 300" style="width:100%;max-width:640px;margin:0.2em auto 0;display:block" role="img" aria-label="diagramma del modello SIR">
    <line x1="55" y1="262" x2="500" y2="262" style="stroke:var(--mot-muted);stroke-width:1.5"/>
    <line x1="55" y1="20" x2="55" y2="272" style="stroke:var(--mot-muted);stroke-width:1.5"/>
    <path d="M55 48 C 170 54 210 95 265 165 C 320 232 410 252 500 255" style="fill:none;stroke:#3a6b8c;stroke-width:3.5;stroke-linecap:round"/>
    <path d="M55 256 C 160 254 205 92 250 92 C 295 92 340 254 500 256" style="fill:none;stroke:var(--mot-primary);stroke-width:3.5;stroke-linecap:round"/>
    <path d="M55 257 C 200 253 262 214 322 132 C 380 55 432 46 500 44" style="fill:none;stroke:#4a7c59;stroke-width:3.5;stroke-linecap:round"/>
    <text x="150" y="52" style="font-family:var(--mot-mono);font-size:15px;fill:#3a6b8c">S</text>
    <text x="242" y="82" style="font-family:var(--mot-mono);font-size:15px;fill:var(--mot-primary)">I</text>
    <text x="470" y="40" style="font-family:var(--mot-mono);font-size:15px;fill:#4a7c59">R</text>
  </svg>
  <dl class="mot-rows fragment" style="font-size:0.6em">
    <dt style="color:#3a6b8c">S &mdash; Susceptible</dt><dd>chi può ancora ammalarsi</dd>
    <dt style="color:var(--mot-primary)">I &mdash; Infected</dt><dd>chi è contagioso adesso: cresce e poi cala</dd>
    <dt style="color:#4a7c59">R &mdash; Removed</dt><dd>guariti (immuni) o deceduti</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">fisica</p>
  <h2>Il decadimento <em>radioattivo</em></h2>
  <p class="mot-def fragment">Una sostanza radioattiva si dimezza a intervalli fissi &mdash; il <b>tempo di dimezzamento</b> $T$:</p>
  <p class="mot-result fragment">$$N(t) = N_0 \left(\tfrac{1}{2}\right)^{t/T}$$</p>
  <p class="fragment" style="font-size:0.74em">È la legge del <b>carbonio-14</b>, con cui si datano reperti e fossili: un'esponenziale <em>decrescente</em>.</p>
  <p class="mot-joke fragment">il tempo, per un atomo, è solo questione di probabilità</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LOGARITMI</h1>
</section>

<section>
  <p class="mot-kicker">l'idea</p>
  <h2>La domanda <em>inversa</em></h2>
  <p class="mot-def fragment">L'esponenziale chiede: &laquo;quanto vale $a^x$?&raquo;. Il logaritmo chiede il contrario: <b>&laquo;a quale esponente devo elevare $a$ per ottenere $x$?&raquo;</b></p>
  <p class="mot-result fragment">$$\log_a x = y \iff a^y = x$$</p>
  <p class="fragment" style="font-size:0.76em">Esempio: $\log_2 8 = 3$, perché $2^3 = 8$.</p>
  <p class="mot-joke fragment">il logaritmo è l'esponenziale vista allo specchio</p>
</section>

<section>
  <p class="mot-kicker">geometricamente</p>
  <h2>Due funzioni allo <em>specchio</em></h2>
  <div class="mot-cols">
    <div class="mot-col fragment" style="font-size:0.68em">
      <p>Il grafico di $y=\log_a x$ è il riflesso di $y=a^x$ rispetto alla retta $y=x$.</p>
      <p>Sono <b>funzioni inverse</b>: una disfa ciò che l'altra fa.</p>
    </div>
    <div class="mot-col fragment">
      <svg viewBox="0 0 320 320" style="width:100%;max-width:340px" role="img" aria-label="esponenziale e logaritmo riflessi">
        <line x1="40" y1="280" x2="300" y2="280" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <line x1="40" y1="20" x2="40" y2="290" style="stroke:var(--mot-muted);stroke-width:1.5"/>
        <line x1="40" y1="280" x2="290" y2="30" style="stroke:var(--mot-muted);stroke-width:1.2;stroke-dasharray:5 5"/>
        <path d="M40 232 C 78 210 108 150 138 78 C 150 50 156 36 160 26" style="fill:none;stroke:var(--mot-primary);stroke-width:3.5;stroke-linecap:round"/>
        <path d="M88 280 C 110 242 170 212 242 182 C 270 170 284 164 294 160" style="fill:none;stroke:#3a6b8c;stroke-width:3.5;stroke-linecap:round"/>
        <circle cx="40" cy="232" r="4" style="fill:var(--mot-primary)"/>
        <circle cx="88" cy="280" r="4" style="fill:#3a6b8c"/>
        <text x="150" y="34" style="font-family:var(--mot-mono);font-size:13px;fill:var(--mot-primary)">aˣ</text>
        <text x="252" y="150" style="font-family:var(--mot-mono);font-size:13px;fill:#3a6b8c">logₐx</text>
        <text x="250" y="60" style="font-family:var(--mot-mono);font-size:12px;fill:var(--mot-muted)">y=x</text>
      </svg>
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">a cosa servono</p>
  <h2>Domare i <em>grandi numeri</em></h2>
  <p class="mot-def fragment">Il logaritmo <b>comprime</b> scale enormi in numeri maneggevoli: trasforma i prodotti in somme e le potenze in prodotti.</p>
  <p class="fragment" style="font-size:0.78em">Per questo molte scale scientifiche sono <b>logaritmiche</b>: ogni passo di $1$ significa moltiplicare per $10$.</p>
</section>

<section>
  <p class="mot-kicker">geologia</p>
  <h2>La scala <em>Richter</em></h2>
  <p class="mot-def fragment">La magnitudo di un terremoto è il <b>logaritmo</b> dell'ampiezza delle onde sismiche.</p>
  <p class="fragment" style="font-size:0.78em">Da magnitudo $5$ a $6$: l'ampiezza è <b>10 volte</b> maggiore, l'energia liberata circa <b>30 volte</b>.</p>
  <p class="mot-joke fragment">un numero piccolo che nasconde un'energia enorme</p>
</section>

<section>
  <p class="mot-kicker">chimica</p>
  <h2>Il <em>pH</em></h2>
  <p class="mot-result fragment">$$\mathrm{pH} = -\log_{10}[\mathrm{H}^+]$$</p>
  <p class="fragment" style="font-size:0.78em">Ogni unità di pH in meno = acidità <b>10 volte</b> maggiore. Il caffè (pH $5$) è <b>cento volte</b> più acido dell'acqua pura (pH $7$).</p>
</section>

<section>
  <p class="mot-kicker">acustica</p>
  <h2>I <em>decibel</em></h2>
  <p class="mot-def fragment">Il livello sonoro in decibel cresce come il logaritmo dell'energia del suono.</p>
  <p class="fragment" style="font-size:0.78em">$+10$ dB significa energia $\times 10$. Un concerto ($110$ dB) non è &laquo;poco più&raquo; di una conversazione ($60$ dB): è $10^5$ volte più intenso.</p>
  <p class="mot-joke fragment">ecco perché i tappi per le orecchie sono una buona idea</p>
</section>

---

<section>
  <p class="mot-kicker">il legame</p>
  <h2>Due facce della <em>stessa medaglia</em></h2>
  <div class="mot-cards">
    <div class="mot-card fragment">
      <h3>Esponenziale</h3>
      <p>modella ciò che <b>cresce</b> o <b>decade</b> moltiplicandosi</p>
      <p class="mono plain">$y=a^x$</p>
    </div>
    <div class="mot-card fragment">
      <h3>Logaritmo</h3>
      <p><b>misura</b> e comprime le scale enormi</p>
      <p class="mono plain">$y=\log_a x$</p>
    </div>
  </div>
  <p class="fragment" style="font-size:0.74em">Sono <b>inverse</b>: $\log_a(a^x)=x$ e $a^{\log_a x}=x$. Nella prossima lezione le studieremo a fondo.</p>
</section>

---

<section>
  <p class="mot-kicker">una storia vera (quasi)</p>
  <h2>Il problema dei <em>conigli</em></h2>
  <style>.fib-rabbits-img{display:block;margin:-1.2rem auto -0.3rem !important;max-width:448px !important;width:448px !important;height:auto !important;}
  body.dark .fib-rabbits-img{filter:invert(1);}</style>
  <img class="fib-rabbits-img" src="/img/fibonacci-rabbits/conigli-fibonacci.png" alt="Conigli">
  <p class="mot-def fragment" style="font-size:0.7em;margin-top:0">Nel 1202, nel <i>Liber Abaci</i>, Leonardo Pisano (Fibonacci) pone un problema: una coppia di conigli genera ogni mese una nuova coppia, che diventa fertile dopo un mese. Quante coppie ci sono dopo un anno?</p>
  <p class="fragment" style="font-size:0.65em">Contando mese per mese si ottiene $1, 1, 2, 3, 5, 8, 13, 21, \dots$ — ogni numero è la <b>somma dei due precedenti</b>.</p>
  <p class="mot-joke fragment" style="margin-top:0.4em">nella prossima animazione semplifichiamo un po': la popolazione raddoppia a ogni generazione</p>
</section>

---

<section>
  <p class="mot-kicker">un caso reale</p>
  <h2>I <em>conigli</em> di Fibonacci</h2>
  <p class="mot-def">Ogni generazione, la popolazione <b>raddoppia</b>. Guarda cosa succede.</p>
  <canvas id="rabbit-dots" width="640" height="150" style="display:block;margin:0.8rem auto 0;max-width:100%;background:rgba(0,0,0,0.03);border-radius:8px;"></canvas>
  <canvas id="rabbit-chart" width="640" height="180" style="display:block;margin:0.4rem auto 0;max-width:100%;"></canvas>
  <p id="rabbit-status" style="font-family:'JetBrains Mono',monospace;font-size:0.8em;text-align:center;margin-top:0.4rem;color:var(--mot-primary);font-weight:600;">generazione 0 — popolazione 1</p>
  <button id="rabbit-play-btn" style="margin-top:0.5rem;padding:0.35rem 0.9rem;font-size:0.72em;font-family:'JetBrains Mono',monospace;background:var(--mot-primary);color:white;border:none;border-radius:6px;cursor:pointer;font-weight:600;">&#9654; Avvia l'animazione</button>
</section>

<script>
(function () {
  var GENERATIONS = 8; // popolazione: 1,2,4,...,256
  var STEP_MS = 700;
  var dotsCanvas = document.getElementById('rabbit-dots');
  var chartCanvas = document.getElementById('rabbit-chart');
  var statusEl = document.getElementById('rabbit-status');
  var btn = document.getElementById('rabbit-play-btn');
  if (!dotsCanvas || !chartCanvas) return;

  var dctx = dotsCanvas.getContext('2d');
  var cctx = chartCanvas.getContext('2d');
  var W = dotsCanvas.width, H = dotsCanvas.height;
  var CW = chartCanvas.width, CH = chartCanvas.height;
  var PAD = 30;
  var maxPop = Math.pow(2, GENERATIONS);
  var primary = '#ed6f5c';

  // posizioni pre-calcolate (jitter su griglia) per i puntini, in ordine di apparizione
  var cols = 26, rows = 10, cellW = W / cols, cellH = H / rows;
  var slots = [];
  for (var r = 0; r < rows; r++) {
    for (var c = 0; c < cols; c++) {
      slots.push({
        x: c * cellW + cellW / 2 + (Math.random() - 0.5) * cellW * 0.5,
        y: r * cellH + cellH / 2 + (Math.random() - 0.5) * cellH * 0.5
      });
    }
  }
  // ordine casuale di apparizione
  for (var i = slots.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = slots[i]; slots[i] = slots[j]; slots[j] = tmp;
  }

  function drawAxes() {
    cctx.clearRect(0, 0, CW, CH);
    cctx.strokeStyle = 'rgba(0,0,0,0.25)';
    cctx.lineWidth = 1;
    cctx.beginPath();
    cctx.moveTo(PAD, 10);
    cctx.lineTo(PAD, CH - PAD);
    cctx.lineTo(CW - 10, CH - PAD);
    cctx.stroke();
    cctx.fillStyle = 'rgba(0,0,0,0.5)';
    cctx.font = '11px JetBrains Mono, monospace';
    cctx.fillText('generazione', CW - 90, CH - 8);
    cctx.save();
    cctx.translate(12, 60);
    cctx.rotate(-Math.PI / 2);
    cctx.fillText('popolazione', 0, 0);
    cctx.restore();
  }

  function chartPoint(gen, pop) {
    var x = PAD + (gen / GENERATIONS) * (CW - PAD - 20);
    var y = (CH - PAD) - (pop / maxPop) * (CH - PAD - 20);
    return { x: x, y: y };
  }

  function resetVisual() {
    dctx.clearRect(0, 0, W, H);
    drawAxes();
    statusEl.textContent = 'generazione 0 — popolazione 1';
  }

  function drawDotsUpTo(count) {
    dctx.clearRect(0, 0, W, H);
    dctx.fillStyle = primary;
    for (var k = 0; k < count && k < slots.length; k++) {
      dctx.beginPath();
      dctx.arc(slots[k].x, slots[k].y, 3.2, 0, Math.PI * 2);
      dctx.fill();
    }
  }

  function drawCurveUpTo(gen, points) {
    drawAxes();
    cctx.strokeStyle = primary;
    cctx.lineWidth = 2.5;
    cctx.beginPath();
    for (var k = 0; k <= gen; k++) {
      var p = points[k];
      if (k === 0) cctx.moveTo(p.x, p.y); else cctx.lineTo(p.x, p.y);
    }
    cctx.stroke();
    cctx.fillStyle = primary;
    for (var k2 = 0; k2 <= gen; k2++) {
      cctx.beginPath();
      cctx.arc(points[k2].x, points[k2].y, 3, 0, Math.PI * 2);
      cctx.fill();
    }
  }

  var playing = false;
  function play() {
    if (playing) return;
    playing = true;
    btn.disabled = true;
    btn.style.opacity = '0.6';

    var points = [];
    for (var g = 0; g <= GENERATIONS; g++) {
      points.push(chartPoint(g, Math.pow(2, g)));
    }

    var gen = 0;
    resetVisual();
    drawCurveUpTo(0, points);
    drawDotsUpTo(1);

    var timer = setInterval(function () {
      gen++;
      var pop = Math.pow(2, gen);
      drawDotsUpTo(pop);
      drawCurveUpTo(gen, points);
      statusEl.textContent = 'generazione ' + gen + ' — popolazione ' + pop;
      if (gen >= GENERATIONS) {
        clearInterval(timer);
        playing = false;
        btn.disabled = false;
        btn.style.opacity = '1';
        btn.textContent = '↻ Riavvia l\'animazione';
      }
    }, STEP_MS);
  }

  resetVisual();
  btn.addEventListener('click', play);
})();
</script>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">crescono in modo esponenziale, si spera</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

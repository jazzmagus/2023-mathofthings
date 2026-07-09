---
title: I Numeri Complessi
summary: Definizione, forme e teoremi fondamentali — corso Pro, Quinto Anno
authors: [Diego Fantinelli]
tags: [numeri complessi, algebra, quinto anno]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
  highlight_style: github
---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">quinto anno — corso pro</p>
  <h1>I Numeri <span class="math-word">Complessi</span></h1>
  <p class="mot-tagline">dalla necessit&agrave; algebrica alla struttura <em>geometrica</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; The Math of Things</p>
</section>

---

<section data-background-image="book_bkg.jpg" data-background-opacity="0.15">
  <blockquote class="mot-quote">
    I numeri complessi sono una benedizione per l'umanit&agrave;, incomprensibile per molti, di cui per&ograve; non si pu&ograve; fare a meno.
    <span class="quote-attr">&mdash; Parafrasando Gottfried Leibniz</span>
  </blockquote>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">IL PROBLEMA</h1>
</section>

<section>
  <p class="mot-kicker">un'equazione impossibile</p>
  <h2>$x^2 + 1 = 0$</h2>
  <p class="mot-def fragment">Nell'insieme $\mathbb{R}$ questa equazione <b>non ha soluzioni</b>: nessun quadrato reale &egrave; negativo.</p>
  <p class="fragment" style="font-size:0.8em">Ma i Greci gi&agrave; risolvevano le equazioni di secondo grado. Nel Rinascimento, con le equazioni <b>cubiche</b>, il problema diventa urgente: certe formule richiedono radici di numeri negativi anche quando la soluzione finale &egrave; reale.</p>
  <p class="mot-joke fragment">un'equazione che chiede aiuto a un numero che non esiste — ancora</p>
</section>

<section>
  <p class="mot-kicker">la soluzione</p>
  <h2>Un nuovo insieme numerico</h2>
  <p class="mot-def fragment">Si definisce l'insieme $\mathbb{C} = \mathbb{R}^2$, con due operazioni:</p>
  <p class="mot-result fragment">$(a,b)+(c,d)=(a+c,\ b+d)$</p>
  <p class="mot-result fragment">$(a,b)\cdot(c,d)=(ac-bd,\ ad+bc)$</p>
  <p class="fragment" style="font-size:0.75em">Si verifica che $(\mathbb{C},+,\cdot)$ &egrave; un <b>campo</b>: stessa struttura algebrica di $\mathbb{Q}$ e $\mathbb{R}$.</p>
</section>

<section>
  <p class="mot-kicker">l'unit&agrave; immaginaria</p>
  <h2>Il numero che serviva</h2>
  <p class="mot-def fragment">Ponendo $i=(0,1)$, si calcola: $i^2 = (0,1)\cdot(0,1) = (-1, 0)$.</p>
  <p class="mot-result fragment">$$i^2=-1$$</p>
  <p class="fragment" style="font-size:0.8em">Esattamente il numero che serviva per risolvere $x^2+1=0$: le sue soluzioni sono $x=\pm i$.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">FORMA ALGEBRICA</h1>
</section>

<section>
  <p class="mot-kicker">notazione</p>
  <h2>$z = a + bi$</h2>
  <dl class="mot-rows fragment">
    <dt>$a$</dt><dd>parte reale, $\mathrm{Re}(z)$</dd>
    <dt>$b$</dt><dd>parte immaginaria, $\mathrm{Im}(z)$</dd>
    <dt>$i$</dt><dd>unit&agrave; immaginaria, $i^2=-1$</dd>
  </dl>
  <p class="mot-joke fragment">un numero con due anime: una reale, una immaginaria</p>
</section>

<section>
  <p class="mot-kicker">operazioni</p>
  <h2>Somma e prodotto</h2>
  <p class="mot-result fragment">$(a+bi)+(c+di)=(a+c)+(b+d)i$</p>
  <p class="mot-result fragment">$(a+bi)(c+di)=(ac-bd)+(ad+bc)i$</p>
  <p class="fragment" style="font-size:0.75em">Si calcola come un prodotto di binomi, imponendo $i^2=-1$ ogni volta che compare.</p>
</section>

<section>
  <p class="mot-kicker">un dettaglio cruciale</p>
  <h2>Le potenze di $i$</h2>
  <p class="mot-def fragment">Sono <b>cicliche di periodo 4</b>:</p>
  <p class="mot-result fragment" style="font-size:0.75em">$i^0=1 \quad i^1=i \quad i^2=-1 \quad i^3=-i \quad i^4=1 \ \dots$</p>
  <p class="fragment" style="font-size:0.75em">Per calcolare $i^n$ con $n$ grande: basta il resto della divisione di $n$ per 4.</p>
  <p class="mot-joke fragment">$i^{37}$? Solo il resto conta: $37 = 4\cdot9+1 \Rightarrow i^{37}=i$</p>
</section>

<section>
  <p class="mot-kicker">strumenti</p>
  <h2>Coniugato e modulo</h2>
  <dl class="mot-rows fragment">
    <dt>coniugato</dt><dd>$\bar z = a-bi$</dd>
    <dt>modulo</dt><dd>$|z|=\sqrt{a^2+b^2}$</dd>
  </dl>
  <p class="mot-result fragment">$$z\cdot\bar z = |z|^2$$</p>
  <p class="fragment" style="font-size:0.75em">Da questa identit&agrave; nasce il reciproco: $\dfrac1z=\dfrac{\bar z}{|z|^2}$, e quindi la divisione tra complessi.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">IL PIANO COMPLESSO</h1>
</section>

<section>
  <p class="mot-kicker">Gauss, Argand, Wessel</p>
  <h2>Dall'algebra alla <em>geometria</em></h2>
  <div class="mot-cols">
    <div class="mot-col fragment">
      <p style="font-size:0.75em">Ogni $z=a+bi$ corrisponde al punto $P(a,b)$ del piano — o al vettore $\overrightarrow{OP}$.</p>
      <p style="font-size:0.7em; margin-top:1em">L'astratto diventa visibile: somma, modulo, coniugato hanno un significato geometrico immediato.</p>
    </div>
    <div class="mot-col fragment">
      <div style="background: rgba(237,111,92,0.08); border-left: 3px solid #ed6f5c; padding: 1.2em 1em; border-radius: 4px;">
        <p style="font-size:0.75em; margin:0; color:#666; line-height:1.6;">$|z|$ &egrave; la distanza di $P$ dall'origine. $\bar z$ &egrave; il simmetrico di $P$ rispetto all'asse reale. $|z-w|$ &egrave; la distanza tra due punti.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <p class="mot-kicker">un esempio geometrico</p>
  <h2>Luoghi nel piano complesso</h2>
  <p class="mot-def fragment">$|z-(2+i)|=3$ rappresenta i punti a distanza 3 da $(2,1)$:</p>
  <p class="mot-result fragment">una <b>circonferenza</b> di centro $(2,1)$, raggio 3</p>
  <p class="mot-joke fragment">l'equazione di un cerchio, travestita da numero complesso</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">FORMA TRIGONOMETRICA</h1>
</section>

<section>
  <p class="mot-kicker">coordinate polari</p>
  <h2>$z=\rho(\cos\theta+i\sin\theta)$</h2>
  <dl class="mot-rows fragment">
    <dt>modulo</dt><dd>$\rho=|z|=\sqrt{a^2+b^2}$</dd>
    <dt>argomento</dt><dd>$\theta=\arg(z)$, tenendo conto del quadrante</dd>
  </dl>
  <p class="mot-joke fragment">stesso numero, due lingue diverse: cartesiana e polare</p>
</section>

<section>
  <p class="mot-kicker">il vantaggio</p>
  <h2>Prodotto e quoziente</h2>
  <p class="mot-result fragment" style="font-size:0.7em">$z\cdot w=\rho_1\rho_2\big[\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\big]$</p>
  <p class="mot-result fragment" style="font-size:0.7em">$\dfrac{z}{w}=\dfrac{\rho_1}{\rho_2}\big[\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)\big]$</p>
  <p class="fragment" style="font-size:0.75em">I moduli si moltiplicano (o dividono), gli argomenti si sommano (o sottraggono).</p>
</section>

<section>
  <p class="mot-kicker">elevare a potenza</p>
  <h2>La formula di De Moivre</h2>
  <p class="mot-result fragment">$$z^n=\rho^n\big[\cos(n\theta)+i\sin(n\theta)\big]$$</p>
  <p class="fragment" style="font-size:0.75em">Conseguenza diretta e ripetuta della formula del prodotto: si dimostra per induzione su $n$.</p>
</section>

<section>
  <p class="mot-kicker">il colpo di scena</p>
  <h2>Radici <em>n</em>-esime</h2>
  <p class="mot-def fragment">Un numero complesso non nullo ha esattamente <b>$n$ radici $n$-esime distinte</b> — non una sola, come nei reali.</p>
  <p class="mot-result fragment" style="font-size:0.68em">$$z_k=\sqrt[n]{\rho}\left(\cos\dfrac{\theta+2k\pi}{n}+i\sin\dfrac{\theta+2k\pi}{n}\right), \ k=0,\dots,n-1$$</p>
  <p class="mot-joke fragment">$\sqrt{4}$ non &egrave; solo 2: nei complessi, ogni radice porta amici</p>
</section>

<section>
  <p class="mot-kicker">geometria delle radici</p>
  <h2>Vertici di un poligono regolare</h2>
  <p class="fragment" style="font-size:0.8em">Le $n$ radici $n$-esime hanno tutte lo stesso modulo $\sqrt[n]\rho$, e i loro argomenti differiscono di $2\pi/n$: formano i vertici di un <b>poligono regolare</b> di $n$ lati.</p>
  <p class="fragment" style="font-size:0.75em">Esempio: le radici quarte di 1 sono $1, i, -1, -i$ — i vertici di un quadrato inscritto nella circonferenza unitaria.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">FORMA ESPONENZIALE</h1>
</section>

<section data-background-image="numbers.gif" data-background-opacity="0.15">
  <p class="mot-kicker">Eulero, 1748</p>
  <h2>La formula pi&ugrave; <em>bella</em></h2>
  <p class="mot-def fragment">La prima formula di Eulero collega esponenziale e trigonometria:</p>
  <p class="mot-result fragment">$$e^{i\theta}=\cos\theta+i\sin\theta$$</p>
  <p class="fragment" style="font-size:0.7em">Ogni complesso si scrive anche come $z=\rho e^{i\theta}$ — la forma <b>esponenziale</b>.</p>
</section>

<section>
  <p class="mot-kicker">il caso $\theta=\pi$</p>
  <h2>L'identit&agrave; di Eulero</h2>
  <p class="mot-result fragment" style="font-size:1.3em">$$e^{i\pi}+1=0$$</p>
  <p class="fragment" style="font-size:0.75em">Cinque costanti fondamentali — $e$, $i$, $\pi$, $1$, $0$ — in un'unica uguaglianza.</p>
  <p class="mot-joke fragment">se la matematica avesse una hit, sarebbe questa</p>
</section>

<section>
  <p class="mot-kicker">il vantaggio</p>
  <h2>Calcolare con gli esponenti</h2>
  <p class="mot-result fragment" style="font-size:0.68em">$z\cdot w=\rho_1\rho_2\,e^{i(\theta_1+\theta_2)} \quad \dfrac{z}{w}=\dfrac{\rho_1}{\rho_2}\,e^{i(\theta_1-\theta_2)} \quad z^n=\rho^n\,e^{in\theta}$</p>
  <p class="fragment" style="font-size:0.75em">Prodotto, quoziente e potenza diventano manipolazioni di esponenti — proprio come per i numeri reali.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">EQUAZIONI IN C</h1>
</section>

<section>
  <p class="mot-kicker">il caso $\Delta &lt; 0$</p>
  <h2>Ogni equazione ha soluzione</h2>
  <p class="mot-def fragment">In $\mathbb{C}$, anche $ax^2+bx+c=0$ con $\Delta<0$ ha soluzioni:</p>
  <p class="mot-result fragment">$$x_{1,2}=\dfrac{-b\pm i\sqrt{|\Delta|}}{2a}$$</p>
  <p class="fragment" style="font-size:0.75em">Le due soluzioni sono sempre <b>complesse coniugate</b>, quando i coefficienti sono reali.</p>
</section>

<section>
  <p class="mot-kicker">il risultato pi&ugrave; profondo</p>
  <h2>Teorema fondamentale dell'algebra</h2>
  <p class="mot-def fragment">Ogni polinomio di grado $n\ge1$ a coefficienti complessi ha esattamente $n$ radici in $\mathbb{C}$ (contate con molteplicit&agrave;).</p>
  <p class="fragment" style="font-size:0.75em">$\mathbb{C}$ &egrave; <b>algebricamente chiuso</b>: non serve ampliarlo ulteriormente per risolvere equazioni polinomiali.</p>
</section>

---

<section class="mot-divider" data-background-image="numbers.gif" data-background-opacity="0.2" data-transition="zoom">
  <h1 class="r-fit-text">APPLICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">non solo algebra</p>
  <h2>Dove vivono i numeri complessi</h2>
  <div class="mot-cards">
    <div class="mot-card fragment">
      <h3>Elettrotecnica</h3>
      <p>$V(t)=V_0e^{i\omega t}$ — impedenza complessa per circuiti in corrente alternata</p>
    </div>
    <div class="mot-card fragment">
      <h3>Meccanica quantistica</h3>
      <p>la funzione d'onda $\psi(x,t)$ &egrave; a valori complessi; $|\psi|^2$ &egrave; una probabilit&agrave;</p>
    </div>
    <div class="mot-card fragment">
      <h3>Frattali</h3>
      <p>l'insieme di Mandelbrot nasce iterando $z_{n+1}=z_n^2+c$</p>
    </div>
  </div>
  <p class="mot-joke fragment">numeri nati per un'equazione impossibile, oggi ovunque nella tecnologia</p>
</section>

---

<section class="mot-divider" data-background-image="numbers.gif" data-background-opacity="0.25" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">l'unico numero che non ha bisogno di essere immaginato &egrave; quello di domande che avete</p>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">grazie dell'attenzione</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

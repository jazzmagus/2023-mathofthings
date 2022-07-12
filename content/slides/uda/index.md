---
title: capitolo6
summary: An introduction to using Wowchemy's Slides feature.
authors: [diego fantinelli]
tags: [math]
categories: [fattorizzazione]
date: "2022-05-09T00:00:00Z"
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
   theme: serif
  # Choose a code highlighting style (if highlighting enabled in `params.toml`)
  #   Light style: github. Dark style: dracula (default).
   highlight_style: dracula
---

{{< slide background-image="pingpong_bkg.jpg" background-opacity="0.6" >}}

<section data-transition="convex">
  <h2 style="color:#3B2F2F">Fattorizzazione polinomiale</h2>
  <h3 style="color:#3B2F2F"><em>esercizi e ripasso</em></h3>
  <h5 style="color:#8A4117"><em>prof. diego fantinelli</em></h5>
  <h5 style="color:#8A4117">ITIS "Enrico Fermi" - Bassano del Grappa</h5>
</section>

---

{{< slide background-image="lightbulb.jpg" background-opacity="0.6" >}}

<section data-transition="convex">
  <h3 class="fragment" style="color:#FFFFFF; font-size: 60px;">una riflessione per iniziare...</h3>
  <h3 class="fragment" style="color:#FFFFFF; font-size: 40px;"><em>“Our virtues and our failings are inseparable, like force and matter. When they separate, man is no more.”
  <br>&mdash; Nikola Tesla</em></h3>
</section>

---

{{< slide background-image="pingpong_bkg.jpg" background-opacity="0.6" >}}

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#3B2F2F">Prerequisiti</h2>

  <ul class="fragment">
  <li class="fragment"><h3 style="color:#8A4117">monomi e polinomi:</h3></li>
    <ul class="fragment">
      <li>Operazioni e proprietà</li>
      <li>Prodotti Notevoli</li>
    </ul>
  <hr class="fragment" style="height:2px;border-width:0;color:gray;background-color:gray">
  <li class="fragment"><h3 style="color:#8A4117">metodi di fattorizzazione</h3></li>
    <ul class="fragment">
      <li>raccoglimento a fattor comune totale</li>
      <li>raccoglimento a fattor comune parziale</li>
      <li>trinomio particolare di secondo grado - (somma-prodotto)</li>
      <li>prodotti notevoli</li>
      <li>Teorema e Regola di Ruffini</li>
    </ul>
</section>

---

{{< slide background-image="calm_bkg.jpg" background-opacity="0.6" >}}

<section data-transition="zoom">
<h2 class="fragment" style="color:#3B2F2F; font-size: 40pt;"><em>“Gli esercizi presenti in questa selezione hanno tutti lo stesso obiettivo: la <b>fattorizzazione</b> di un polinomio in un prodotto di fattori <b>irriducibili</b>"</em>
</h2></section>

---

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 1</h2>
  <h4 class="fragment">$8 x^{4}+12 x^{3}+6 x^{2}+x$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$\left[x(2 x+1)^{3}\right]$</h4>
</section>

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 2</h2>
  <h4 class="fragment">$4 x^{2}-12 x-40$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$[4(x-5)(x+2)]$</h4>
</section>

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 3</h2>
  <h4 class="fragment">$x^{3}+x^{2} y-9 x-9 y$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$[(x-3)(x+3)(x+y)]$</h4>
</section>

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 4</h2>
  <h4 class="fragment">$x^{3}+x^{2} y-9 x-9 y$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$[(x-3)(x+3)(x+y)]$</h4>
</section>

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 5</h2>
  <h4 class="fragment">$x^{3}+x^{2} y-9 x-9 y$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$[(x-3)(x+3)(x+y)]$</h4>
</section>

<section style="font-size:90%" data-transition="convex">
  <h2 style="color:#e28743">esercizio 6</h2>
  <h4 class="fragment">$4 x^{3}+5 x^{2}-23 x-6$</h4>
  <h3 class="fragment" style="color:#2596be; font-size: 80px;">soluzione</h3>
  <h4 style="color:#2596be"; class="fragment">$(x-2)(x+3)(4 x+1)$</h4>
</section>

---

<section data-background-color="#EDEDED">
  <img data-src="https://res.cloudinary.com/teepublic/image/private/s--TQXt20Pc--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_000000,e_outline:48/co_000000,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1588675429/production/designs/9818088_0.jpg">
</section>
---
title: monomi_polinomi-ex
summary: An introduction to using Wowchemy's Slides feature.
authors: [diego fantinelli]
tags: [math]
categories: []
date: "2022-03-05T00:00:00Z"
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
   theme: serif
  # Choose a code highlighting style (if highlighting enabled in `params.toml`)
  #   Light style: github. Dark style: dracula (default).
   highlight_style: dracula

---

## esercizi ripasso monomi e polinomi

#### Eseguiamo, se possibile, le seguenti divisioni

1. $\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)$;

---

- La divisione $\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)$ è possibile, perché ogni termine del dividendo contiene le variabili del divisore, con esponente maggiore o uguale.

> Non è necessario, invece, che i coefficienti dei termini del dividendo siano multipli del coefficiente del divisore.

--

- Dividiamo per $2 x^{2} y$ ogni termine del polinomio dividendo:
$$
\begin{aligned}
&12 x^{4} y^{3}:\left(2 x^{2} y\right)=6 x^{4-2} y^{3-1}=6 x^{2} y^{2} \\
&-3 x^{3} y^{4}:\left(2 x^{2} y\right)=-\frac{3}{2} x^{3-2} y^{4-1}=-\frac{3}{2} x y^{3} \\
&2 x^{2} y:\left(2 x^{2} y\right)=1 .
\end{aligned}
$$

--

Il risultato è quindi:
$$
\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)=6 x^{2} y^{2}-\frac{3}{2} x y^{3}+1 .
$$
<mark class="hltr-green">Verifica</mark> :
$$
\underbrace{\left(6 x^{2} y^{2}-\frac{3}{2} x y^{3}+1\right)}_{\text {quoziente}} \cdot \underbrace{2 x^{2} y}_{\text {divisore }}=\underbrace{12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y}_{\text {dividendo }} .
$$

---

### esercizio 2

$$\left(5 a b^{2}+3 a^{3} b^{3}-3 a^{4}\right):\left(2 a^{2} b^{2}\right)$$

--

- La divisione $\left(5 a b^{2}+3 a^{3} b^{3}-3 a^{4}\right): 2 a^{2} b^{2}$ non è possibile per due motivi:
- $5 a b^{2}$ ha grado rispetto ad $a$ minore di $2 a^{2} b^{2}$;
- $-3 a^{4}$ ha grado rispetto a $b$ minore di $2 a^{2} b^{2}$ (il grado rispetto a $b$ di $-3 a^{4}$ è 0 ).

### prodotti notevoli

#### Esercizi

- $(2 a-b)^{2}-(3 a+b)(a-2 b)+5 a^{2}-a b$
- $(x+y)^{2}-2 y(x-y)-(x+y)(y-x)$
- $\left(a^{2}+b^{2}\right)\left(a^{2}-b^{2}\right)-\left(a^{2}+b^{2}\right)^{2}+2 a^{2}\left(a^{2}+b^{2}\right)$
- $(x+1)^{3}+3(x+1)^{2}+3(x+1)+1$

--

- $2(y-3 x)^{2}+2(2 x+y)(y-2 x)-9 x^{2}-2 x y-(2 y-x)^{2}$
- $\left(x^{2}-3 y^{2}\right)\left(2 x^{2}+y^{2}\right)-\left(x^{2}+2 y^{2}\right)\left(x^{2}-2 y^{2}\right)-\left(x^{2}+y^{2}\right)^{2}$
- $[(2-a)(2+a)-2]^{3}-\left(2 a^{2}-b+1\right)^{2}+a^{2}\left(a^{2}+4\right)^{2}+\left(b-2 a^{2}\right)^{2}$
- $\left(-x+y^{2}\right)\left(-x-y^{2}\right)+(-2 y)^{2}(x-y)^{2}+8 x y^{3}-4 x^{2}\left(1+y^{2}\right)$

--

- $(x+2)^{2}-3(x+2)(x-2)+(x-2)^{3}-x^{2}(x-8)$
- $(x-2 y)^{3}-x(x-2 y)(x+2 y)+2 x y(3 x+4 y)-(-2 y)^{3}$
- $a\left(a^{2}-3\right)+\left(1+6 a+a^{3}\right)-(a-1)^{3}+(-a-1)^{3}$
- $\left\{\left[x^{3}-y^{3}+(x+y)^{3}+2 x^{2} y-x(2 x+3 y)(x+y)\right]^{2}-2\right\}^{3}$

--

- $[a+3+(b-1)(2 b+a+3)+b(b+2 a-1)] a-(b+a)^{3}$
- $\left(x^{2}-2 x y+3 y^{2}\right)\left(x^{2}+2 x y+3 y^{2}\right)-2\left(x y-x^{2}\right)^{2}-4 x^{3} y+x^{4}$
- $\left[(x-y)^{2}(x+y)^{2}-x^{2}\left(x^{2}-2 y^{2}\right)\right]: \dfrac{(-y)^{2}}{2} \cdot(x+y)$
- $\left[(x+3 a)^{2}+(2 x-3 a)^{2}+4\left(x-\dfrac{3}{2} a\right)(3 a+x)\right]:(-3)^{2}-(x-2)^{2}$

--

- $\left(1-2 a^{2}\right)\left(1+2 a^{2}\right)+\left(5 a^{2}-1\right)^{2}-2\left(1-4 a^{2}\right)^{2}-\left[-2 a^{4}-\left(3 a^{2}-1\right)^{2}\right]$
- $\left[(x+y)^{3}-(x+y)\left(x^{2}-x y+y^{2}\right)\right]^{2}-2 x y(-3 x y)^{2}$
- $\left[x^{2}-(x-y)(x+y)+y^{3}\right]^{3}-(1+y)^{3} \cdot\left[\left(y^{3}+1\right)\left(y^{3}-1\right)+\left(y^{2}+x^{2}\right)^{0}\right]$

---
title: 5. Monomi e Polinomi
linktitle: Capitolo 5 monomi e polinomi
abstract: "Il calcolo letterale cambia cmpletamente la prospettiva con la quale guardiamo al calcolo..."
toc: true
type: book
date: "2019-05-05T00:00:00+01:00"
draft: false
slides: "capitolo5"
menu:
  math-01:
    parent: 
    weight: 

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 50
---

☆ **scadenza**: 30 marzo 2022

---

>_On August 14, 2021, a team (DAViS) at the University of Applied Sciences of the Grisons announced completion of the computation of π to 62.8 trillion digits_

---

{{< toc >}}

![ex2_img](../sliding-rule.jpg)

Iniziamo oggi un viaggio in un mondo che ci farà vedere la matematica un po' più vicina alla realtà, in quanto <mark style="background-color: #ABF7F7A6;">punti di discontinuità</mark>

- In alcuni contesti utilizzare dei simboli per indicare generici elementi di un insieme aiuta ad esprimere delle caratteristiche di intere classi di elementi, non singoli oggetti.
- Questo è uno degli aspetti più caratteristici della matematica, occuparsi di fare scoperte e ricavare proprietà su intere categorie di oggetti, nel nostro caso numeri, piuttosto che sui singoli.
- Questo bisogno di generalizzare non è sentito solo in matematica, è simile a ciò che succede in molti contesti quotidiani.

![ex2_img](../calc_dark.svg)

><h4>esempio 1</h4>
>
>se diciamo:
>
><span style="color:orange">Un qualunque individuo minorenne trovato alla guida di un’auto sta commettendo reato.</em></span>
>
>- non ci interessa affatto sapere se tale individuo si chiama Andrea o Giovanni, se è biondo o castano, o se l’auto è una FIAT Panda o una Lamborghini.
>- Ciò che ci interessa è che il soggetto in questione è un **individuo** (cioè un elemento dell’insieme delle persone) minorenne (un elemento dell’insieme delle persone che non ha ancora raggiunto i 18 anni di età) e che si trova alla guida di un auto (un elemento dell’insieme di quei particolari mezzi di trasporto che sono le automobili).
>
><h4>esempio 2</h4>
>
>- se vogliamo rimanere in ambito matematico, pensiamo alle figure geometriche:
>
> - **Area del rettangolo**: <span style="color:orange">$A = a \times b$</span>, con $a$ e $b$, base e altezza;
>   - d'ora in poi sarà molto meglio usare il simbolo "$\cdot$" al posto di "$\times$" per indicare la moltiplicazione, proprio perché utilizzeremo spesso la lettere $x$ e si rischierebbe di confonderla.
> - **Area del quadrato**: <span style="color:orange">$A = l^2$</span>, con $l$ lato del quadrato;
> - **Area del cerchio**: <span style="color:orange">$A_c = 2\pi \cdot r^2$</span>;
>   - questo $2\pi \cdot r^2$ è proprio quello che tra poco chiameremo **monomio**

---

## introduzione

![mind map](../calcolo-letterale.png)

- Innanzitutto, <mark>che tipo di operazione compiamo quando utilizziamo il calcolo letterale?</mark>
  - Con il **calcolo letterale** si utilizzano dei **simboli** (usualmente lettere) al posto degli **elementi di un insieme** (di solito insiemi numerici), per sottolineare che non stiamo indicando nessun elemento in particolare, ma uno generico.
  - Stiamo perciò facendo un’affermazione che vale contemporaneamente per tutti gli elementi di un insieme, non di un solo elemento specifico.

## Utilità del Calcolo Letterale

- In alcune occasioni sostituire simboli ai numeri aiuta a semplificare i conti.
- Sostituire a dei numeri un'unica semplice lettera può permettere di svolgere molti calcoli simili una volta sola, oppure evitare di dover effettuare conti con numeri di molte cifre.

1. Se si devono effettuare molti calcoli dalla stessa struttura, ma con numeri diversi, è utile fare i calcoli una volta sola, sostituendo ai numeri un simbolo, e poi sostituire ai simboli i numeri, così da ottenere i risultati voluti.
2. Ma oltre a questo vantaggio, _sostituire lettere a numeri permette di compiere dei conti e arrivare a dei risultati che valgono per un’intera classe di elementi_, e non per uno solo.
3. Un particolare pregio del calcolo letterale è poi quello di non dover utilizzare la calcolatrice. Infatti, evitare di svolgere ogni possibile conto numerico immettendo i dati in un calcolatore elettronico può, in alcune occasioni, <mark> far risparmiare molto tempo, evitare errori e aiutare a comprendere a fondo la situazione che si sta trattando.</mark>
4. <b>Il calcolo letterale permette, quindi, di risolvere problemi tra loro simili, una sola volta.</b>

---

## Alcune importanti definizioni

{{% callout note %}}

**definizione**: <em>una **espressione algebrica** è una scrittura in cui compaiono sia numeri che lettere, (eventualmente parentesi), legati tra loro da simboli di operazioni matematiche.</em>

- Un’**espressione letterale** o **espressione algebrica** è uno schema di calcolo in cui compaiono numeri e lettere legati dai simboli delle operazioni.
- un'espressione algebrica si dice **razionale** quando le operazioni che compaiono sono quelle di: **addizione**, **sottrazione**, **moltiplicazione** ed **elevamento a potenza**: $$x^2 + y^3$$
- Tra le espressioni algebriche razionali abbiamo quelle **frazionarie**, in cui si ha un'espressione algebrica al numeratore e una al denominatore: $$\dfrac{3x^2}{2x^2 -3y}$$
- Quando invece compare anche la radice allora si parla di espressione algebrica **irrazionale**: $$\sqrt{\dfrac{3x^2}{2x^2 -3y}}$$

{{% /callout %}}

- Il **valore numerico** di un'espressione algebrica si ottiene semplicemente sostituendo alle lettere un numero reale: l'espressione algebrica si trasforma in un'espressione numerica, che assume quindi un valore numerico.
- In un’espressione letterale le lettere rappresentano delle **variabili**, che assumono un preciso significato ==solo== quando vengono sostituite da numeri
  - $2x^2 - 3x + 4$ è un'espressione algebrica
  - se assegnamo ad $x$ il valore $-1$, l'espressione assumerà il valore: $2 \cdot (1)^2 - 3 \dot (1) + 4 = 2 - 3 + 4 = +3 \Rightarrow 3$
  - se invece $x = -1$ otteniamo: $2 \cdot (-1)^2 - 3 \dot (-1) + 4 = 2 + 3 + 4 = +11 \Rightarrow 11$

---

## 3. Monomi

{{% callout note %}}

>**definizione**:
><span style="color:red">Un **monomio** è una espressione algebrica nella quale:</span>
>
>- compaiono soltanto operazioni di **moltiplicazione** ed **elevamento a potenza**;
>- Gli esponenti delle variabili sono **numeri naturali**, qundi $\in \mathbb{N}$
>
>- sono monomi:
>$7x^3yz^4 \qquad - \dfrac {1}{2} a^2bc^4 \qquad 3a(-2)ab^3 \qquad \sqrt{2}st^2 \qquad v = \dfrac{s}{t}$
>- non sono monomi:
>$7x^3yz^{-4} \qquad - \dfrac {1}{2} a^2bc^4 + \dfrac{5}{6}a^2c\qquad 3 \dfrac{a}{b^3} \qquad 2 \sqrt{s}$

{{% /callout %}}

### Grado complessivo di un monomio

{{% callout info %}}

>**definizione**:<br>
><span style="color:orange">Dato un monomio non nullo, si definisce **grado** (o **grado complessivo**) del monomio la somma degli esponenti di tutte le lettere che vi compaiono.</span>

{{% /callout %}}

Grado di un monomio rispetto ad una variabile

{{% callout info %}}

>**definizione**:<br>
><span style="color:orange">Dato un monomio non nullo, si definisce **grado** del monomio **rispetto ad una lettera**, l'esponente con cui compare quella lettera all'interno del monomio, una volta ridotto in **forma normale**</span>
>
>- il monomio: $7x^3yz^4$
>- è di grado $3$ rispetto a $x$, di grado $1$ rispetto a $y$ e di grado $4$ rispetto a $z$.

{{% /callout %}}

---

## Proprietà e operazioni con i monomi

>**nota**:<br><em>In una espressione algebrica il punto utilizzato per indicare l'operazione di moltiplicazione viene spesso omesso, quindi l'espressione algebrica $xyz^2$ ha il significato di $x \cdot y \cdot z^2$.</em>
>
>Un monomio si dice **ridotto in forma normale** quando è scritto come prodotto di **un solo** fattore numerico, detto **coefficiente numerico**, e di potenze letterali con basi diverse. Il complesso delle lettere che compaiono nel monomio ridotto a forma normale ne costituisce la **parte letterale**.

## Operazioni con i monomi

### Somma algebrica di monomi

>La <mark><b>somma algebrica</b></mark> di uno o più <mark><b>monomi simili</b></mark> è un monomio, simile a quelli di partenza, che ha per coefficiente la **somma algebrica** dei coefficienti.

- la **somma** di due monomi **opposti** è zero, ossia il monomio nullo
- la **differenza** di due monomi uguali è zero, ossia il monomio nullo

- <mark style="color:#C04000">i monomi devono essere **simili** per poter essere sommati algebricamente</mark>:
  - $$3xy^2 - 8xy^2 + xy^2$$
  - $$- \dfrac{1}{2}a^2b + \dfrac{2}{3}a^2b$$
  - $$- 6x + 5x^2y + 4x - 3x^2y$$

### Riduzione dei termini simili

>Una somma algebrica di più monomi può essere semplificata se tra i suoi termini vi sono dei termini simili tra loro.
>
>- Se i termini della somma sono monomi tutti simili tra loro si ottiene come risultato un monomio; in caso contrario si otterrà un polinomio.

{{% callout info %}}

#### esempi

65. $-2 a^{2} s^{2}+\dfrac{7}{6} a^{2} s^{2}-\dfrac{5}{27} a^{2} s^{2}+\dfrac{11}{15} a^{2} s^{2}+\dfrac{3}{10} a^{2} s^{2}+\dfrac{5}{27} a^{2} s^{2}-\dfrac{6}{5} a^{2} s^{2}$
66. $\left(-2 x^{2} y^{3}+\dfrac{5}{2} x^{2} y^{3}-\dfrac{1}{6} x^{2} y^{3}\right)-\left(\dfrac{13}{12} x^{2} y^{3}-\dfrac{11}{4} x^{2} y^{3}+x^{2} y^{3}\right)$
67. $\left(-\dfrac{7}{20} a+\dfrac{11}{30} a-\dfrac{7}{12} a+\dfrac{1}{15} a\right)-\left(\dfrac{3}{8} a-\dfrac{7}{20} a-\dfrac{2}{5} a\right)$
68. $-\dfrac{2}{5} a^{3}+\dfrac{15}{8} a^{2} b-\dfrac{8}{15} a^{2}-\dfrac{3}{5} a^{3}+\dfrac{8}{15} a^{2}+a^{3}-\dfrac{7}{8} a^{2} b$
69. $\dfrac{11}{10} s^{3} t-\dfrac{11}{10} s t^{3}+\dfrac{3}{5} s t^{3}-\dfrac{31}{35} s^{3} t-\dfrac{3}{5} s-\dfrac{3}{14} s^{3} t+\dfrac{3}{5} s+\dfrac{3}{2} t^{3}$
70. $-\dfrac{1}{10} x y^{2}-\dfrac{1}{9} x^{2} y+\dfrac{5}{6} x y^{2}+\dfrac{4}{3}+\dfrac{1}{9} x^{2} y-\dfrac{11}{15} x y^{2}-\dfrac{5}{6}$
71. $\dfrac{1}{6} x y+\dfrac{5}{3} x-\left[\dfrac{1}{24} x y-\left(\dfrac{1}{12} x y-\dfrac{7}{8} x y+\dfrac{1}{6} x y\right)+2 x-\dfrac{1}{3} x\right]$  

---

- ##### piccola _challenge_

  - Alla manifestazione hanno partecipato $n$ uomini;
  - le donne erano $100$ in più di metà degli uomini;
  - i bambini erano il doppio degli uomini diminuito di $31$.
- Quante persone hanno partecipato alla manifestazione?

{{% /callout %}}

### 8. Prodotto di monomi

- si sommano gli esponenti: $$(6xy^3z^2) \cdot (- \dfrac{1}{3}y^2z) = -2xy^5z^3$$

### 9. Elevamento a potenza

>È consigliato un ripasso delle **proprietà delle potenze**

{{% callout info %}}

>**definizione**: <span style="color:#8A4117">La **potenza con esponente naturale $n$ di un monomio** è un **monomio** che ha per coefficiente la potenza di esponente $n$ del coefficiente e per parte letterale la potenza di esponente $n$ della parte letterale.</span>
>
>- il monomio: $7x^3yz^4$
>- è di grado $3$ rispetto a $x$, di grado $1$ rispetto a $y$ e di grado $4$ rispetto a $z$.

{{% /callout %}}

#### esempio

- si **moltiplicano** gli esponenti, come per le potenze numeriche:
  - $$\{[(-2a^2b)^2]^3\}^2$$

## 10. Quoziente di due monomi

## 11. MCD e mcm di due o più monomi

{{% callout alert%}}

#### Massimo comune divisore (MCD)

> Il **massimo comune divisore (MCD)** di due monomi non nulli è un monomio così formato:
>
> - il **coefficiente** è il MCD dei valori assoluti dei coefficienti dei monomi daati, se tali coefficienti sono tutti interi, altrimentiè $1$;
> - la **parte letterale** è il prodotto di tutte le lettere comuni ai monomi dati, ciascuna presa una sola volta con l'esponente **minimo** con cui essa figura nei monomi dati.
>   - tale monomio risulta **divisore** di tutti i monomi dati e, tra tutti i divisori comuni dei monomi dati, è quello di grado maggiore.

{{% /callout %}}

{{% callout alert%}}

#### Minimo comune multiplo (mcm)

> Il **minimo comune multiplo (mcm)** di due monomi non nulli è un monomio così formato:
>
> - il **coefficiente** è il mcm dei valori assoluti dei coefficienti dei monomi daati, se tali coefficienti sono tutti interi, altrimentiè $1$;
> - la **parte letterale** è il prodotto di tutte le lettere, _comuni e non comuni_ ai monomi dati, ciascuna presa una sola volta con l'esponente **massimo** con cui essa figura nei monomi dati.
>   - tale monomio risulta **divisore** di tutti i monomi dati e, tra tutti i divisori comuni dei monomi dati, è quello di grado maggiore.

{{% /callout %}}

### Generalizzando

>- Se voglio comprare delle scarpe che costano $50$ euro e sono scontate del $12$%, mi interessa scoprire quanto devo pagare, non fare conti astratti.
>- Ma se sono un commerciante che ogni anno vende un certo numero di paia di scarpe, e devo calcolare quali sconti fare per avere un certo guadagno e aumentare le vendite, è piú utile che egli faccia dei conti riapplicabili in ogni occasione, anziché perdere tempo a ripetere gli stessi procedimenti ogni volta.

---

## Polinomi

{{% callout info %}}

>**definizione**: Un **polinomio** è una **somma algebrica** di **monomi**, non simili.</span>

{{% /callout %}}

**sono polinomi:** $6a + 2b; \quad 5a^2b + 3b^2; \quad 6x^2 - 5y^2x - 1; \quad 7ab - 2a^2b^3 + 4$.

_osserva che_:

- Se tra i termini di un polinomio non sono presenti monomi simili, il polinomio si dice in forma **normale** o **ridotto**;
- se al contrario si presentano dei termini simili, possiamo eseguire la riduzione del polinomio sommando i termini simili.
- Tutti i polinomi sono quindi riducibili in forma normale.
- Un polinomio in forma normale può presentare tra i suoi termini un monomio di grado $0$ che viene comunemente chiamato **termine noto**.

---

### grado di un polinomio

{{% callout alert %}}

> **definizione**: Il **grado complessivo** (o semplicemente grado) di un polinomio è il massimo dei gradi complessivi dei suoi termini. Si chiama, invece, grado di un polinomio rispetto ad una data lettera l’esponente maggiore con cui quella lettera compare nel polinomio, dopo che è stato ridotto a forma normale.
>
>- Il polinomio $2ab + 3 - 4a^2b^2$ ha grado complessivo $4$ perché il monomio con grado massimo è $- 4a^2b^2$, che è un monomio di quarto grado;
>
>- il grado del polinomio $a^3 + 3b^2a - 4ba^2$ rispetto alla lettera $a$ è $3$ perché l’esponente più grande con cui tale lettera compare è $3$.

- Un polinomio si dice **omogeneo** se tutti i termini che lo compongono sono dello _stesso grado_.

- Un polinomio si dice **ordinato secondo le potenze decrescenti (_crescenti_) di una lettera**, quando i suoi termini sono ordinati in maniera tale che gli esponenti di tale lettera decrescono (_crescono_), leggendo il polinomio da sinistra verso destra.

- Un polinomio di grado $n$ rispetto ad una data lettera si dice **completo** se contiene tutte le potenze di tale lettera di grado inferiore a $n$, compreso il termine noto.

{{% /callout %}}

---

## Proprietà dei polinomi

## Operazioni con i polinomi

## somma algebrica e "differenza"

> La somma algebrica comprende anche la "sottrazione", che nel Calcolo Letterale viene interpretata come una **somma algebrica** con l'**opposto** del polinomio da sottrarre.

## prodotto di un monomio per un polinomio

- Si esegue moltiplicando il monomio per ognuno dei termini del polinomio, sommando algebricamente i monomi risultanti
- Il prodotto tra un monomio e un polinomio è certamente un **caso particolare** del prodotto tra polinomi in quanto un monomio può essere pensato come un caso particolare di polinomio, composto di un solo termine.
- **esempio**:

## prodotto di polinomi

## quoziente di un polinomio e un monomio

## Prodotti Notevoli

I **prodotti notevoli** sono soltanto dei prodotti tra polinomi che, essendo utilizzati di frequente è conveniente imparare a ricavare facilmente per non doverli imparare a memoria - che non serve.

{{% staticref "uploads/ripasso_calc.pdf" "newtab" %}} <i class="fa-regular fa-share-from-square"></i> - Ripasso Prodotti Notevoli{{% /staticref %}}

### perché sono così utili

1. perché semplificano **notevolmente** i calcoli
2. perché sono molto utilizzati: compaiono molto spesso quindi conoscerli semplifica molto la comprensione di determinati ragionamenti
3. sono uno strumento molto potente nella **fattorizzazione polinomiale**

### ricavarli o ricordarli?

> sarà sufficiente ricavarli un paio di volte per ricordarli; eventualmente si possono ricavare facilmente.

## Divisione tra polinomi

### divisibilità tra polinomi

> il concetto di **divisibilità**

### l'algoritmo

### Regola di Ruffini

Divisione e Regola di Ruffini:

### Divisione tra polinomi

- Eseguire la seguente Divisione tra polinomi:

>$(6x^3 - 2x^2 + 3x -1) : (2x^2 + 1)$
>
>**soluzione**: $Q(x) = (3x - 1); \qquad R(x) = 0$.

- Qual è il quoziente $Q(x)$?
- Qual è il Resto $R(x)$?
- Che conclusioni puoi trarne?

![mind map](../Paolo_Ruffini.jpeg)

### Regola di Ruffini

>Eseguiamo un classico esercizio di _fattorizzazione_ utilizzando la Regola di Ruffini:

- Eseguire la divisione utilizzando la Regola di Ruffini:
$$(2x^3 - 9x + 1) : (x - 3)$$
- **soluzione**: $$Q(x) = 2x^2 + 6x + 9; \qquad R = 28$$

### esempi

# esercizi ripasso monomi e polinomi

#### Eseguiamo, se possibile, le seguenti divisioni

1. $\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)$;

---

- La divisione $\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)$ è possibile, perché ogni termine del dividendo contiene le variabili del divisore, con esponente maggiore o uguale.

> Non è necessario, invece, che i coefficienti dei termini del dividendo siano multipli del coefficiente del divisore.

---

- Dividiamo per $2 x^{2} y$ ogni termine del polinomio dividendo:
$$
\begin{aligned}
&12 x^{4} y^{3}:\left(2 x^{2} y\right)=6 x^{4-2} y^{3-1}=6 x^{2} y^{2} \\
&-3 x^{3} y^{4}:\left(2 x^{2} y\right)=-\frac{3}{2} x^{3-2} y^{4-1}=-\frac{3}{2} x y^{3} \\
&2 x^{2} y:\left(2 x^{2} y\right)=1 .
\end{aligned}
$$
Il risultato è quindi:
$$
\left(12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y\right):\left(2 x^{2} y\right)=6 x^{2} y^{2}-\frac{3}{2} x y^{3}+1 .
$$
<mark class="hltr-green">Verifica</mark> :
$$
\underbrace{\left(6 x^{2} y^{2}-\frac{3}{2} x y^{3}+1\right)}_{\text {quoziente }} \cdot \underbrace{2 x^{2} y}_{\text {divisore }}=\underbrace{12 x^{4} y^{3}-3 x^{3} y^{4}+2 x^{2} y}_{\text {dividendo }} .
$$

2. $\left(5 a b^{2}+3 a^{3} b^{3}-3 a^{4}\right):\left(2 a^{2} b^{2}\right)$.

- La divisione $\left(5 a b^{2}+3 a^{3} b^{3}-3 a^{4}\right): 2 a^{2} b^{2}$ non è possibile per due motivi:
- $5 a b^{2}$ ha grado rispetto ad $a$ minore di $2 a^{2} b^{2}$;
- $-3 a^{4}$ ha grado rispetto a $b$ minore di $2 a^{2} b^{2}$ (il grado rispetto a $b$ di $-3 a^{4}$ è 0 ).

### prodotti notevoli

#### Esercizi

- $(2 a-b)^{2}-(3 a+b)(a-2 b)+5 a^{2}-a b$
- $(x+y)^{2}-2 y(x-y)-(x+y)(y-x)$
- $\left(a^{2}+b^{2}\right)\left(a^{2}-b^{2}\right)-\left(a^{2}+b^{2}\right)^{2}+2 a^{2}\left(a^{2}+b^{2}\right)$
- $(x+1)^{3}+3(x+1)^{2}+3(x+1)+1$
- $2(y-3 x)^{2}+2(2 x+y)(y-2 x)-9 x^{2}-2 x y-(2 y-x)^{2}$
- $\left(x^{2}-3 y^{2}\right)\left(2 x^{2}+y^{2}\right)-\left(x^{2}+2 y^{2}\right)\left(x^{2}-2 y^{2}\right)-\left(x^{2}+y^{2}\right)^{2}$
- $[(2-a)(2+a)-2]^{3}-\left(2 a^{2}-b+1\right)^{2}+a^{2}\left(a^{2}+4\right)^{2}+\left(b-2 a^{2}\right)^{2}$
- $\left(-x+y^{2}\right)\left(-x-y^{2}\right)+(-2 y)^{2}(x-y)^{2}+8 x y^{3}-4 x^{2}\left(1+y^{2}\right)$
- $(x+2)^{2}-3(x+2)(x-2)+(x-2)^{3}-x^{2}(x-8)$
- $(x-2 y)^{3}-x(x-2 y)(x+2 y)+2 x y(3 x+4 y)-(-2 y)^{3}$
- $a\left(a^{2}-3\right)+\left(1+6 a+a^{3}\right)-(a-1)^{3}+(-a-1)^{3}$
- $[a+3+(b-1)(2 b+a+3)+b(b+2 a-1)] a-(b+a)^{3}$
- $\left(x^{2}-2 x y+3 y^{2}\right)\left(x^{2}+2 x y+3 y^{2}\right)-2\left(x y-x^{2}\right)^{2}-4 x^{3} y+x^{4}$
- $\left[(x-y)^{2}(x+y)^{2}-x^{2}\left(x^{2}-2 y^{2}\right)\right]: \dfrac{(-y)^{2}}{2} \cdot(x+y)$
- $\left[(x+3 a)^{2}+(2 x-3 a)^{2}+4\left(x-\dfrac{3}{2} a\right)(3 a+x)\right]:(-3)^{2}-(x-2)^{2}$
- $\left(1-2 a^{2}\right)\left(1+2 a^{2}\right)+\left(5 a^{2}-1\right)^{2}-2\left(1-4 a^{2}\right)^{2}-\left[-2 a^{4}-\left(3 a^{2}-1\right)^{2}\right]$
- $\left[(x+y)^{3}-(x+y)\left(x^{2}-x y+y^{2}\right)\right]^{2}-2 x y(-3 x y)^{2}$
- $\left[x^{2}-(x-y)(x+y)+y^{3}\right]^{3}-(1+y)^{3} \cdot\left[\left(y^{3}+1\right)\left(y^{3}-1\right)+\left(y^{2}+x^{2}\right)^{0}\right]$

## conclusioni

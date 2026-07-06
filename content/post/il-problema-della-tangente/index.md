---
title: "Le _derivate_: dal problema della tangente alla definizione formale"
subtitle: "Dalla pendenza di una retta alla velocità istantanea di variazione"
summary: "Un percorso completo dalle rette alle curve: come nasce il concetto di derivata e come si definisce rigorosamente"
authors: [diego fantinelli]
tags: [analisi, derivate, limiti, teoria]
categories: [maths]
date: "2026-06-16T10:00:00Z"
publishDate: "2026-06-16T10:00:00Z"
featured: false
draft: false
image:
  filename: featured.png
  caption: 'Fig. 1: Interpretazione grafica della derivata — dalla secante alla tangente'
  focal_point: Center
  placement: 2
  preview_only: false
---

## Il problema della tangente

### Pendenza di una retta

Per stabilire la **pendenza** di una retta — o meglio la sua inclinazione — è sufficiente fissare due punti sulla retta ed effettuare il rapporto tra l'incremento in direzione $y$ (altezza) e l'incremento in direzione $x$ (lunghezza):

$$\text{inclinazione}=\dfrac{\Delta y}{\Delta x}= \dfrac{y_q - y_p}{x_q - x_p} \tag{1}$$

Questo viene definito anche **tasso medio di cambiamento** o **variazione media**.

Facendo riferimento all'equazione della generica retta $y = mx + q$, l'inclinazione della retta è chiamato **coefficiente angolare**:

$$m =  \dfrac{y_q - y_p}{x_q - x_p}$$

### Il problema con le curve

Quando però la funzione non è una retta, bensì una **curva**, diventa molto complicato stabilire l'inclinazione. Nel momento in cui si fissano due punti su una curva, l'inclinazione — così com'è stata definita più sopra — rappresenterebbe soltanto un'approssimazione del **tasso di variazione** reale.

Serve pertanto uno strumento che permetta di calcolare l'inclinazione della curva **in ogni suo punto**. Questo strumento — anche intuitivamente — non può non essere legato al concetto di **limite**.

---

## Il rapporto incrementale

### Dalla retta secante alla retta tangente

Consideriamo due punti $P$ e $Q$ situati sul grafico di una funzione, quindi appartenenti al suo **Insieme di Definizione**:
- $P(x, f(x))$
- $Q(x+h, f(x+h))$

La pendenza della retta passante per i due punti $P$ e $Q$ — chiamata **retta secante** — è:

$$\dfrac{\Delta y}{\Delta x}=\dfrac{f(x+h)-f(x)}{h} \tag{2}$$

Dal punto di vista della curva, questo rapporto rappresenta soltanto l'inclinazione di una retta **secante** passante per due punti appartenenti alla funzione.

Però notiamo qualcosa di cruciale:

> **L'intuizione chiave:**
> 
> 1. La precisione riguardo al calcolo della pendenza aumenta all'avvicinarsi di $Q$ a $P$
> 2. Nel momento in cui i due punti coincideranno esisterà un'unica retta passante per quel punto e quella retta non potrà che essere la **tangente** alla curva nel punto $P$. La sua inclinazione $m$ — il coefficiente angolare — è proprio quello che cerchiamo.
> 3. La **secante** si trasforma in **tangente** al limite!

### La formula della retta secante

La retta passante per $P$ e $Q$ ha equazione:

$$y-y_p=(y_q-y_p) \cdot \dfrac{x-x_p}{x_q-x_p}$$

Sostituendo i nostri punti:

$$f(x) - f(x_0) = \dfrac{f(x_0 + h) - f(x_0)}{h} \cdot (x - x_0) \tag{3}$$

Il termine al numeratore della frazione rappresenta il **coefficiente angolare** della retta **secante** alla curva della funzione $f(x)$.

### Definizione del rapporto incrementale

$$\text{Rapporto incrementale}=\dfrac{f(x_0 + h) - f(x_0)}{h} \tag{RI}$$

È il rapporto tra gli **incrementi** in $y$ e in $x$.

---

## La derivata: dalla pendenza media alla pendenza puntuale

### Dal limite nasce la derivata

La **derivata** di una funzione è definita come il **limite** — ove questo esista e sia finito — del rapporto incrementale:

$$f'(x) = \dfrac{dy}{dx} = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h} \tag{D}$$

Questa definizione cattura l'idea fondamentale: quando avviciniamo infinitamente il secondo punto al primo, la retta secante diventa la retta tangente, e il suo coefficiente angolare diventa la **pendenza della curva esattamente in quel punto**.

### Significati della derivata

La derivata di una funzione ha due interpretazioni parallele:

1. **Geometricamente**: rappresenta l'inclinazione — il **coefficiente angolare** — della retta **tangente** al grafico della funzione in un punto.

2. **Analiticamente**: rappresenta il **tasso di variazione istantaneo** della funzione in esame. È la velocità con cui la funzione cambia in quel preciso istante.

### Un esempio dalla fisica

In fisica, l'**accelerazione** rappresenta il tasso di variazione della **velocità** — cioè la derivata della velocità rispetto al tempo. Allo stesso modo, la **velocità** è la derivata della posizione rispetto al tempo.

---

## Conclusione

Il viaggio dalla semplice domanda "qual è la pendenza di una curva?" ci ha portato a scoprire uno dei concetti più potenti della matematica: la **derivata**. 

Dalle rette alle curve, dai rapporti medi ai tassi istantanei, dalla geometria all'analisi — la derivata è il cuore pulsante del calcolo differenziale, uno strumento indispensabile non solo in matematica, ma in ogni disciplina dove il cambiamento è protagonista.

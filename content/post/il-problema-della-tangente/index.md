---
title: "Il _problema_ della tangente"
subtitle: "Introduzione al concetto di derivata attraverso il problema geometrico della tangente"
summary: "Dalle rette alle curve: come calcolare la pendenza di una curva in ogni suo punto"
authors: [diego fantinelli]
tags: [analisi, derivate, limiti, teoria]
categories: [maths]
date: "2026-06-16T00:00:00Z"
publishDate: "2026-06-16T00:00:00Z"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: ''
  focal_point: Center
  placement: 2
  preview_only: false
---

## Il problema della tangente

### Pendenza di una retta

Per stabilire la **pendenza** di una retta — o meglio la sua inclinazione — è sufficiente fissare due punti sulla retta ed effettuare il rapporto tra l'incremento in direzione $y$ (altezza) e l'incremento in direzione $x$ (lunghezza):

$$\text{inclinazione}=\dfrac{\Delta y}{\Delta x}= \dfrac{y_q - y_p}{x_q - x_p}$$

Questo viene definito anche **tasso medio di cambiamento** o **variazione media**.

Facendo riferimento all'equazione della generica retta $y = mx + q$, l'inclinazione della retta è chiamato **coefficiente angolare**:

$$m =  \dfrac{y_q - y_p}{x_q - x_p}$$

### Il problema con le curve

Quando però la funzione non è una retta, bensì una **curva**, diventa molto complicato stabilire l'inclinazione. Nel momento in cui si fissano due punti su una curva, l'inclinazione — così com'è stata definita più sopra — rappresenterebbe soltanto un'approssimazione del **tasso di variazione** reale.

Serve pertanto uno strumento che permetta di calcolare l'inclinazione della curva **in ogni suo punto**. Questo strumento — anche intuitivamente — non può non essere legato al concetto di **limite**.

Questo è il cuore della derivata.

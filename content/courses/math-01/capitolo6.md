---
title: 6. Fattorizzazione Polinomiale
linktitle: Capitolo 6 | Fattorizzazione polinomiale
toc: true
type: docs
date: "2019-05-05T00:00:00+01:00"
draft: false
slides: "capitolo6"
menu:
  math-01:
    parent: 
    weight: 

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 60
---

> ☆ **scadenza**: 30 ottobre 2021

![ex2_img](../ex2_img.png)

---

[Ruffini](../ruffini_vid.mp4)

[esercizi di ripasso]({{< relref "../../slides/ex_ripasso/index.md" >}})

>### *"Non esiste vento favorevole per il marinaio che non sa dove andare"*
>
>#### - Lucio Anneo Seneca

---

{{< toc >}}

## introduzione

## metodi di fattorizzazione

### raccoglimento a fattor comune totale

### raccoglimento a fattor comune parziale

### prodotti notevoli

>{{% staticref "uploads/ripasso_calc.pdf" "newtab" %}} <i class="fa-regular fa-share-from-square"></i> - Ripasso Prodotti Notevoli{{% /staticref %}}

### Trinomio Particolare di secondo grado

[esempio svolto]({{< relref "/publication/trinomio_particolare" >}})

> Si tratta semplicemente di un **trinomio di secondo grado, completo**, con una caratteristica che lo rende *particolare* - infatti viene chiamato anche **trinomio particolare**
>
> - Si presenta nella forma seguente:
> $$x^2 + sx+p$$
> - in cui le lettere $s$ e $p$, stanno ad indicare _somma_ e _prodotto_

### Divisione polinomiale

### Teorema del Resto

> **Teorema del Resto**: Nella divisione tra polinomio e un binomio del tipo $A(x) : (x - a)$, il resto è dato dal valore che assume $A(x)$ quando alla variabile $x$ si sostituisce il valore $a$: $R = A(a)$.

#### esempio:

- Cercare gli **zeri** di un polinomio
- Verificare se uno o più numeri sono **divisori** di un dato polinomio:
  - per poterlo dire è necessario sapere dove andarli a cercare

### Teorema Ruffini

Un polinomio $A(x)$ è divisibile per un binomio $(x - a)$ **se e soltanto se** $A(a)$ è uguale a $0$.

- Il teorema di Ruffini permette - in determinate condizioni - di scomporre in fattori un polinomio, o più generalmente, è un sistema più semplice per eseguire la Divisione.
- Consideriamo un polinomio $A(x)$.
- Sappiamo che, se $A(x) = 0$, allora il polinomio è divisibile per $(x - a)$;
- Eseguendo la divisione $A(x) : (x - a)$, otteniamo il polinomio quoziente $Q(x)$ e, poiché il resto è zero, scriviamo $A(x)$ come prodotto di due fattori: 
- $A(x) = (x - a) Q(x)\quad \Rightarrow \quad$ il risultato è una **fattorizzazione**!

### Regola di Ruffini

- Eseguiamo un classico esercizio di *fattorizzazione* utilizzando la Regola di Ruffini:
- >Eseguire la divisione utilizzando la Regola di Ruffini:
$(2x^3 - 9x + 1) : (x - 3)$
- >**soluzione**: $Q(x) = 2x^2 + 6x + 9; \qquad R = 28$

### Divisibilità

>**definizione**:

- Un polinomio $A(x)$ è divisibile per un polinomio $B(x)$ se esiste un polinomio $Q(x)$ che, moltiplicato per $B(x)$, dà come prodotto $A(x)$. $A(x) : B(x) = Q(x) \quad \Rightarrow \quad B(x) \cdot Q(x) = A(x)$
- Si può anche dire che un polinomio è divisibile per un monomio o per un altro polinomio **sse** il resto della divisione è $0$
- **Divisibilità** di un polinomio per un monomio:
Un polinomio è **divisibile** per un **monomio** non nullo se ogni suo termine è divisibile per tale monomio.
# esercitazioni

>**esercizi**
>
>- Fattorizza i seguenti polinomi utilizzando il metodo che ritieni più appropriato:
>
>1. $$81x^2 -36x + 4 = (9x-2)^2$$

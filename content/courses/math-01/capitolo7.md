---
title: 7. Frazioni algebriche
linktitle: Capitolo 7 | Frazioni algebriche
toc: true
type: docs
date: "2019-05-05T00:00:00+01:00"
draft: false
menu:
  math-01:
    parent: 
    weight: 

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 70
---

> ☆ **scadenza**: 20 ottobre 2021

![ex1_img](../frazioni_algebriche.jpeg)

## prerequisiti

- **Fattorizzazione polinomiale**

  - indispensabile per poter semplificare una *frazione algebrica*

- **mcm** tra polinomi

  - per potersi riportare alla **forma normale** di una *frazione algebrica*: $\frac{N(x)}{D(x)}$

---

### <font color="brown">cos'è una **frazione algebrica**</font>

> <font color="red">Si tratta di una **divisione** tra polinomi, espressa sottoforma di frazione.</font>
>
>_esempio:_ $\(x+1) : (x^2-1)$

$$\dfrac{\text{numeratore}}{\text{denominatore}} \rightarrow \dfrac{N(x)}{D(x)} \rightarrow \dfrac{x+1}{x^2 -1}$$

- Il *dividendo* prende il nome di <font color="brown">**numeratore**</font>
- Il *divisore* prende il nome di <font color="brown">**denominatore**</font>

---

## Condizioni di Esistenza

- Esiste un **condizione** indispensabile per poter lavorare con le **frazioni algebriche**:

- <font color="red">Il **denominatore** non può **mai** essere nullo</font>

## $$\dfrac{N(x)}{D(x)} \Rightarrow D(x) \neq 0$$

---

## <font color="brown">Le tre cose da fare</font>

1. Ridurla in **forma normale**, nel caso si trattasse di un'*espressione con frazioni algebriche*
   - fattorizzare tutti in denominatori
   - denominatore comune

2. Determinare le **Condizioni di Esistenza**, C.E.

3. fattorizzare il numeratore, se possibile

4. semplificare, se possibile

---

## Riduzione di frazioni algebriche allo stesso denominatore

><font color="brown">Per ridurre più frazioni allo stesso denominatore, bisogna trasformarle in frazioni **equivalenti** aventi tutte lo stesso denominatore (**M.C.D.** minimo comune denominatore).</font>

---

### Il procedimento

E' analogo a quello usato per ridurre più frazioni numeriche allo stesso denominatore:

1. si semplificano le frazioni date;
2. le frazioni così ottenute sono quelle a cui si applicano direttamente i passaggi successivi;
3. il denominatore comune cercato (*minimo comune denominatore*) è il **mcm** dei denominatori;

---

### esempio 1

- fattorizziamo e semplifichiamo:
  - $\dfrac{(x+1)}{(x^2-1)} = \dfrac{(x+1)}{(x+1)(x-1)} = \color{red}{\dfrac{1}{(x-1)}}$

- determiniamo le **condizioni di esistenza**, C.E.
  - poniamo il denominatore **uguale a zero** determinare per quali valori di $x$ il **denominatore si annulla**:
  - $D(x)=0 \rightarrow x - 1 = 0 \Rightarrow x=1$

---

### scriviamo correttamente la soluzione

- Condizioni di esistenza:
  - $C.E.: x \neq 1$

- Insieme di Definizione:
  - $IdD = \overbrace{\\{ \forall x \in \mathbb{R} : x \neq 1 \\}}^{insieme \\, di \\, definizione}$

{{% callout note %}}
l'IdD rappresenta un **insieme** in futuro l'IdD verrà chiamato anche **Dominio**
{{% /callout %}}

---

### esempi

- $$\dfrac{3x+15}{x^2 - 25}$$

- $$\dfrac{2 x^{4}-18}{(x-1)(2 x-3)-(x-2)(x-3)}$$

- $$\dfrac{x}{x+2}-\dfrac{8}{x^{2}-4}+\dfrac{2}{x-2}$$

- $$-\dfrac{10}{x-2}+\dfrac{x+2}{x}+\dfrac{2}{3 x^{2}-x}$$

---

<section>

## errori gravi

> Per evitare di commettere gravi errori devi ricordare che, in una frazione algebrica, puoi semplificare solo i fattori comuni al numeratore e al denominatore

---

- nella frazione $\dfrac{a+b}{b}$ non è possibile operare alcuna semplificazione; infatti $b$ è un fattore per il denominatore, ma è un addendo per il numeratore!
- Analogamente, nella frazione $\dfrac{a+x}{a+y}$ non è possibile semplificare per $a$: infatti il monomio $a$ è un addendo per entrambi i termini della frazione, non un fattore

$$\dfrac{3+5}{3} \neq \dfrac{\cancel{3} + 5}{\cancel{3}} \qquad  \dfrac{2x^2 -3y}{4x^4} \neq \dfrac{\cancel{2x^2} - 3y}{\cancel{4x^4}}$$


## Due regole d'oro

### 1. **fattorizzare** i **denominatori**

#### $\Rightarrow$ serve a calcolare il *minimo comun denominatore*

### 2. **sviluppare** i **numeratori**

#### $\Rightarrow$ serve a semplificare i monomi simili

</section>

---

<section>

## Uno sguardo alle equazioni lineari intere

- Sono del tipo:

$$P(x) = 0$$

- con $P(x)$ un Polinomio in $x$ di grado $n$

### $$x^2 + 5x + 6 = 0$$


### Vi sblocco un ricordo...

**Principi di equivalenza**

1. **primo principio**: afferma che **sommando algebricamente** ad entrambi i membri di una equazione, uno **stesso numero** o una **stessa espressione contenente l'incognita**, otteniamo una equazione **equivalente** a quella data.

2. **secondo principio**: moltiplicando o dividendo entrambi i membri di una uguaglianza per uno **stesso numero** *diverso da zero*, o per una **stessa espressione** che non possa annullarsi, si ottiene un'equazione **equivalente** a quella data.

## uno strumento davvero efficace

### L.A.P.: Legge di Annullamento del Prodotto

$$
P_1(x) \cdot P_2(x) \cdot P_3(x) = 0 \Rightarrow \begin{cases}
  P_1(x) = 0 \\\\
  P_2(x) = 0 \\\\
  P_3(x) = 0
\end{cases}
$$

---

## esempio

$$\underbrace{25x^2 - 20x + 4}_{quadrato \\, di \\, binomio} = 0$$

$$\Rightarrow (5x - 2)^2= 0$$

$$\Rightarrow 5x - 2 = 0$$

$$\Rightarrow x = \dfrac{2}{5}$$

</section>

#### equazioni/disequazioni mindmap

![mind](../equazioni_mindmap.png)

# Questions?

**>>** prossima puntata:

**equazioni lineari frazionarie**

![zzz](https://res.cloudinary.com/teepublic/image/private/s--TQXt20Pc--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_000000,e_outline:48/co_000000,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1588675429/production/designs/9818088_0.jpg)

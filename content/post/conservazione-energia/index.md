---
title: "La _conservazione_ dell'energia"
subtitle: "Dal principio della meccanica alla generalizzazione per forze non conservative"
summary: "Analisi completa del principio di conservazione dell'energia, dalle forze conservative all'introduzione delle forze non conservative"
authors: [diego fantinelli]
tags: [fisica, energia, lavoro, conservazione, dinamica]
categories: [physics]
date: "2026-06-16T00:00:00Z"
publishDate: "2026-06-16T00:00:00Z"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: "Conservazione dell'energia meccanica"
  focal_point: Center
  placement: 2
  preview_only: false
---

### Introduzione

Il cosiddetto **principio di conservazione dell'energia generalizzato** è, in realtà, una denominazione impropria.
Non si tratta infatti di un principio fondamentale della fisica, bensì di una **generalizzazione del principio di conservazione dell'energia meccanica**, valida anche in presenza di **forze non conservative**.

La relazione di partenza è il **teorema dell'energia cinetica**, che è sempre valido. Da esso si ricava:

$$
\Delta E_M = L_{\text{non c.}}
$$

dove l'energia meccanica totale $E_M$ è definita come

$$
E_M = E_K + U
$$

con $E_K$ energia cinetica e $U$ energia potenziale.

Questa espressione mostra che:

- l'**energia meccanica si conserva** quando agiscono **solo forze conservative** (ad esempio la forza gravitazionale o la forza elastica);

- l'**energia meccanica varia** quando sono presenti **forze non conservative**, come l'attrito, il cui lavoro è responsabile della variazione di $E_M$.


Il documento sviluppa in modo sistematico questa derivazione e si conclude con un **esempio applicativo**, in cui viene calcolato lo spazio percorso da un corpo soggetto a forza d'attrito.

---

# Principio di Conservazione dell'Energia Generalizzato

## Definizione

**Nome improprio**: non è un principio di conservazione, ma una **generalizzazione del principio di conservazione dell'energia meccanica** nel caso in cui agiscano forze non conservative.

---

## Teorema dell'Energia Cinetica

$$
\Delta E_K = L_{A \to B}^{\text{tot}}
$$

dove:

- $E_K$ = energia cinetica

- $L_{A \to B}^{\text{tot}}$ = lavoro totale compiuto da tutte le forze nel passaggio da $A$ a $B$


Questo teorema vale **sia in presenza di forze conservative che di forze non conservative**.

---

## Scomposizione del Lavoro Totale

Il lavoro totale può essere scomposto in:

$$
L_{A \to B}^{\text{tot}} = L_{A \to B}^{\text{cons}} + L_{A \to B}^{\text{non c.}}
$$

dove:

- $L_{A \to B}^{\text{cons}}$ = lavoro delle forze conservative

- $L_{A \to B}^{\text{non c.}}$ = lavoro delle forze non conservative


---

## Collegamento con l'Energia Potenziale

Per le forze conservative vale la relazione:

$$
L_{A \to B}^{\text{cons}} = -\Delta U = -(U_B - U_A) = U_A - U_B
$$

---

## Unendo Tutto

Dal teorema dell'energia cinetica:

$$
\Delta E_K = L_{A \to B}^{\text{cons}} + L_{A \to B}^{\text{non c.}}
$$

Sostituendo $L_{A \to B}^{\text{cons}} = -\Delta U$:

$$
\Delta E_K = -\Delta U + L_{A \to B}^{\text{non c.}}
$$

Riorganizzando:

$$
\Delta E_K + \Delta U = L_{A \to B}^{\text{non c.}}
$$

ovvero:

$$
\Delta (E_K + U) = L_{A \to B}^{\text{non c.}}
$$

Definendo l'energia meccanica totale $E_M = E_K + U$:

$$
\Delta E_M = L_{A \to B}^{\text{non c.}}
$$

---

## Caso Speciale: Solo Forze Conservative

Se **non agiscono forze non conservative**, cioè:

$$
L_{A \to B}^{\text{non c.}} = 0
$$

allora:

$$
\Delta E_M = 0
$$

e quindi:

$$
E_M = E_K + U = \text{costante}
$$

Questo è il **vero principio di conservazione dell'energia meccanica**.

In forma esplicita:

$$
E_{K,A} + U_A = E_{K,B} + U_B
$$

oppure, nel caso della forza peso:

$$
\frac{1}{2} m v_A^2 + m g h_A =
\frac{1}{2} m v_B^2 + m g h_B
$$

---

## Esempio: corpo con attrito

#### Dati

- velocità iniziale: $v_i = 5\,\mathrm{m/s}$
- massa: $m = 1\,\mathrm{kg}$
- coefficiente di attrito: $\mu = 0.4$
- determinare lo spazio percorso prima dell'arresto

---

### Soluzione

In presenza di attrito l'energia meccanica non si conserva. Tuttavia è sempre
valido il *teorema dell'energia cinetica*. Poiché l'unica forza che compie
lavoro lungo il moto è la forza di attrito, si ha:

$$
\Delta E_K = L_{\text{attrito}}
$$

La variazione di energia cinetica del corpo è:

$$
\Delta E_K
= E_{K,f} - E_{K,i}
= \frac{1}{2} m v_f^2 - \frac{1}{2} m v_i^2
$$

Poiché il corpo si arresta, $v_f = 0$, quindi:

$$
\Delta E_K
= 0 - \frac{1}{2}(1)(5)^2
= -12.5\,\mathrm{J}
$$

Il lavoro della forza di attrito, opposta al moto, vale:

$$
L_{\text{attrito}} = -\mu \cdot m \cdot g \cdot s
$$

Uguagliando la variazione di energia cinetica al lavoro dell'attrito:

$$
-\frac{1}{2} m v_i^2 = -\mu \cdot m \cdot g \cdot s
$$

Sostituendo i valori numerici:

$$
\frac{1}{2}(1)(5)^2 = 0.4 \cdot 1 \cdot 9.8 \cdot s
$$

$$
12.5 = 3.92\, s
$$

da cui:

$$
s = \frac{12.5}{3.92} \approx 3.19\,\mathrm{m}
$$

**Risultato**: il corpo percorre circa $3.2\,\mathrm{m}$ prima di fermarsi.

---

## Schema Riassuntivo

|Tipo di forze|Lavoro|Conseguenza sull'energia|
|---|---|---|
|Forze conservative|$L = -\Delta U$|$E_M$ costante (se agiscono da sole)|
|Forze non conservative|$L \neq -\Delta U$|$E_M$ varia|

|Caso|Relazione|
|---|---|
|Sempre valido|$\Delta E_K = L_{\text{tot}}$|
|Con attrito|$\Delta E_M = L_{\text{non c.}} \neq 0$|
|Senza attrito|$\Delta E_M = 0 \;\Rightarrow \; E_M$ costante|

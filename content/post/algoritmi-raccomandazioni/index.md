---
title: "Algoritmi e _Raccomandazioni_"
subtitle: "La Matematica Dietro lo Schermo"
summary: "Come Netflix, YouTube e Spotify sanno cosa ti piace"
authors:
  - diego fantinelli
tags:
  - algoritmi
  - probabilita
categories: [tech]
date: "2026-07-07T09:00:00Z"
featured: true
draft: false
image:
  filename: featured.jpg
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false
projects: []
---

> "I know that I am intelligent, because I know that I know nothing."
>
> Socrate

Quante volte questa settimana un algoritmo ha deciso cosa mostrarti? Il tuo feed Instagram, la serie che Netflix ti ha consigliato, quel video su YouTube che "sembrava fatto apposta per te", le notizie che leggi. Non è caso. Non è magia. **È matematica.**

E la domanda vera è: *come fa una macchina a indovinare quello che ti piace, se nemmeno tu lo sai sempre?*

---

## L'osservazione — Quello che vedi tutti i giorni

Apri Netflix. Scorri il catalogo. Stranamente, tra i miliardi di film e serie disponibili, **3-4 titoli ti saltano subito agli occhi**. Non sono gli ultimi usciti. Non sono i più visti al mondo. Sono *tuoi*.

Scrolli YouTube dopo una lezione di fisica. Il feed non solo suggerisce altri video di fisica — ma ha già intuito che probabilmente cercavi anche esperimenti, visualizzazioni, storie di scienziati.

Ieri hai ascoltato una canzone su Spotify. Oggi il tuo "Discover Weekly" ha catturato 6-7 brani che non conoscevi, ma potrebbero sembrare fatti per te.

**Come è possibile?**

La risposta non è che qualcuno dall'altra parte del mondo la pensa come te. È che migliaia di persone come te hanno lasciato tracce. Tante tracce. E le macchine contano.

---

## Il principio — Probabilità condizionata in azione

Immagina questo scenario semplice:

**100 persone** hanno guardato una combinazione di tre film:
- Film A (drammatico, intenso)
- Film B (fantascienza con elementi comici)
- Film C (thriller psicologico)

Ora arriva il Film D. È fantastico, ma nessuno lo conosce ancora.

Cosa succede? **80 di quelle 100 persone** decidono di guardarlo, e lo amano.

Tu, oggi, hai appena finito A, B, e C.

**Domanda per te:** qual è la probabilità che tu vorrai guardare il Film D?

La risposta intuitiva: **molto alta**. Probabilmente l'80%.

In linguaggio matematico, questo si chiama **probabilità condizionata**:

$$P(\text{guardi Film D} \mid \text{hai visto A, B, C}) = 0.8$$

Si legge così: "La probabilità che guardi il Film D, *dato che* hai visto A, B, C, è dell'80%."

L'algoritmo non "pensa" come te. Semplicemente **conta**: se sei entrato in un gruppo di persone che hanno fatto le stesse scelte (hai visto A, B, C), la probabilità che farai la loro prossima scelta è alta.

E Netflix lo sa.

---

## Come funziona davvero — Il modello

Il principio è semplice, ma la pratica è più sofisticata. Ecco cosa succede realmente dietro le quinte:

### Passo 1: Rappresentare il gusto

Ogni film, ogni canzone, ogni video ha **attributi**:
- Genere (drama, sci-fi, comedy, horror...)
- Cast principale (attori, registi)
- Durata
- Tema (amore, avventura, educativo...)
- Il "sentimento" (veloce, lento, emozionante, rilassante)
- Epoca (anni '80, recente...)
- Pubblico (adulti, ragazzi, famiglia...)

Tu, come spettatore, crei un **profilo** basato su quello che hai guardato, votato, condiviso. Ogni azione lascia un'impronta digitale: è un tuo voto implicito.

### Passo 2: Trovare persone "come te"

L'algoritmo calcola la **similarità** tra il tuo profilo e quello di altri milioni di utenti.

Se tu e un'altra persona avete guardato gli stessi 10 film, e avete detto "mi piace" agli stessi 15, allora siete **simili**.

Più sono simili i vostri profili, più probabile è che amate anche lo stesso film nuovo che nessuno di voi ha ancora visto.

### Passo 3: Il calcolo (la matematica vera)

Qui entra in gioco la distanza geometrica.

Immagina uno **spazio multidimensionale** dove ogni dimensione è un attributo (genere, attore, anno, etc.). Tu sei un punto in questo spazio. Così come è un punto ogni altro utente. Ogni film è un punto.

La **similarità** tra te e un altro utente si calcola usando il **prodotto scalare** tra i vostri vettori, oppure la **distanza coseno**:

$$\text{Similarità}(tu, \text{utente X}) = \cos(\theta) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$

Dove $\theta$ è l'angolo tra i vostri due vettori di gusto nello spazio.

Più l'angolo è piccolo, più siete simili. Più siete simili, più il suggerimento è affidabile.

**In parole semplici:** è come dire *"sei simile a questo gruppo di 5000 persone. Loro hanno amato questo film. Tu probabilmente lo amerai anche tu."*

---

## Perché funziona così bene (e perché è spaventoso)

### La bellezza

L'algoritmo è efficiente. Tu non devi digitare cosa ami — lui lo scopre guardando cosa fai. Non hai bisogno di compilare un sondaggio infinito. Più usi la piattaforma, più lui ti conosce.

E funziona. Dannatamente bene.

Se guardasse film a caso, Netflix perderebbe abbonati. Se Spotify ti suggerisse solo heavy metal quando ami il jazz, lo disinstalleresti. Questi algoritmi **mantengono vive le piattaforme** suggerendoti cose che probabilmente amerai.

### Il lato scuro

Ma c'è un prezzo.

**1. La bolla (filter bubble)**

Se hai visto solo film di azione negli ultimi due mesi, l'algoritmo te ne suggerirà altri. E altri ancora. E altri ancora.

Qui dentro, non vedi mai dramma psicologico raffinato. Non vedi documentari. Non vedi prospettive diverse. Sei **intrappolato in una bolla di preferenza**, e la bolla si stringe sempre di più.

Questo non accade per malvagità. Accade perché l'algoritmo ottimizza per una cosa: **mantenerti sull'app il più a lungo possibile**. E il modo più veloce è dargli quello che ama già.

**2. Il viaggio verso l'estremo**

Netflix sa che contenuti medi generano scarso engagement. Contenuti che ti fanno sentire *intensamente* — gioia, paura, rabbia, disgusto — ti mantengono incollato allo schermo.

Quindi gli algoritmi di engagement tendono a suggerire **contenuti sempre più estremi**, sempre più polarizzati. Non per ideologia — per matematica pura.

Se hai guardato un video su un argomento controverso, vedrai subito i video più polarizzati di quel tema. Non perché vogliano radicalizzarti. Ma perché i video estremi generano più commenti, più tempo schermo, più dati.

**3. La tua privacy non è un incidente — è il prodotto**

L'algoritmo sa:
- Che genere di film guardi
- A che ora li guardi (studio? relax? solitudine?)
- Con chi li condividi
- Dove vivi (dal server che usi)
- Cosa cerchi (se accedi via Google)
- Quali annunci ti interessano

Non è un errore di sicurezza. È il **modello di business**. Tu non sei il cliente di Netflix — sei il prodotto. Il cliente è chi compra gli annunci (o chi paga per non vederli).

Vuoi scoprire quanto sa Google di te? Vai su myactivity.google.com e inizia a scorrere. Ci metterai ore.

---

## Due domande che cambiano tutto

### Domanda 1: Vuoi controllare l'algoritmo, o vuoi che lui controlli te?

Non è retorica. È una scelta reale.

**Controllare l'algoritmo** significa:
- Sapere come funziona
- Capire cosa sta tracciando
- Decidere consapevolmente cosa condividere e cosa no
- Disattivare i suggerimenti personalizzati a volte
- Cercare attivamente prospettive diverse
- Non stare passivamente dentro la bolla

**Lasciare che lui ti controlli** significa:
- Accettare l'illusione che il feed sia casuale
- Credere che il suggerimento sia "solo per te" (sì, ma con un'agenda dietro)
- Restare intrappolato nella bolla di preferenza
- Credere di essere libero mentre sei tracciato

La scelta non è tra "usare la tecnologia" e "non usarla" — è tra **usarla consapevolmente** e usarla ingenuamente.

### Domanda 2: Cosa succederebbe se disattivassimo i suggerimenti personalizzati?

Prova questo esperimento:

Scegli una piattaforma (Netflix, YouTube, o il tuo social). **Disattiva i suggerimenti personalizzati per una settimana.** Puoi ancora usare il servizio, ma non ricevi "consigli algoritmici".

Cosa noti?

- Scopri meno cose nuove? (Sì, probabilmente.)
- Vedi più varietà? (Sì.)
- Ti annoii di più? (Magari.)
- Ti senti più libero di navigare? (Molti dicono di sì.)

Questa non è una risposta — è **un'osservazione su te stesso**. Perché la domanda vera è: preferisci l'efficienza dell'algoritmo, o la libertà di scegliere?

La risposta non è "giusta" o "sbagliata". Ma dovrebbe essere **consapevole**.

---

## La lezione dietro lo schermo

Abbiamo iniziato con una domanda: come fa Netflix a conoscerti così bene?

Abbiamo scoperto che non ti "conosce" — **misura ciò che fai, e calcola cosa farai dopo**.

È probabilità. È geometria. È il prodotto scalare nello spazio multidimensionale. È contare milioni di tracce di persone "come te".

Ma c'è una lezione più profonda.

**La matematica non è astratta.** Non è solo numeri su una lavagna. È il motore invisibile che decide cosa vedi, che attira la tua attenzione, che gradualmente plasma le tue preferenze. Un miliardo di volte al giorno, per miliardi di persone.

E la cosa affascinante (e preoccupante) è che **funziona troppo bene**. Funziona così bene che non te ne accorgi nemmeno.

Il vero potere della matematica non è risolvere equazioni complicate. È influenzare il comportamento umano in modi così sottili che la gente crede di essere libera mentre viene guidata da una formula.

Ecco perché capire questi algoritmi non è un esercizio di curiosità. È **un'esigenza di alfabetizzazione digitale**. Nel nostro tempo, non sapere come funziona un algoritmo è come nel 1980 non capire come leggere i media. Sei vulnerabile. Sei manovrato. Sei facile da prevedere.

Quindi la prossima volta che Netflix ti suggerisce qualcosa, ricordati: **non è magia. È matematica. E se conosci la matematica, puoi scegliere di seguire, o di ribellarti.**

La bolla esiste. Ma puoi riuscire ad uscirne. Devi solo volerlo abbastanza da notare i confini.

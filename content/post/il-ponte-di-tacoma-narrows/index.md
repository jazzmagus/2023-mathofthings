---
title: "Il ponte che imparò a _ballare_, e la matematica che (in parte) lo _spiega_"
subtitle: "Dal crollo di Tacoma Narrows alle equazioni differenziali del secondo ordine"
summary: "Il crollo del ponte di Tacoma Narrows nel 1940 è la porta d'ingresso più spettacolare verso oscillatori, risonanza e sistemi dinamici — con tutte le cautele storiche del caso."
authors: [diego fantinelli]
tags: [matematica, fisica, equazioni differenziali, divulgazione, verso l'università]
categories: [math]
date: "2026-07-27T07:00:00Z"
publishDate: "2026-07-27T07:00:00Z"
related_link: "/lezioni/equazioni-differenziali-universita/lezione.html"
related_link_label: "Approfondimento universitario"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: ''
  focal_point: Center
  placement: 2
  preview_only: false
---

### Un ponte che ballava

Il 7 novembre 1940, il ponte sospeso di Tacoma Narrows, nello stato di Washington, crollò nel giro di poche ore, sotto un vento tutto sommato modesto — circa 65 km/h, nulla che un ponte sospeso non dovesse sopportare normalmente. Il crollo fu filmato, ed è per questo che è diventato uno dei filmati più mostrati nelle aule di fisica di tutto il mondo: si vede l'impalcato torcersi e ondeggiare sempre più violentemente, come un nastro sventolato al vento, fino a spezzarsi.

Il soprannome che i cronisti dell'epoca diedero al ponte — "Galloping Gertie", Gertie la galoppante — era già stato coniato prima del crollo: la struttura era nota per ondeggiare vistosamente fin dai primi giorni di apertura, qualche mese prima. Non era un difetto nascosto: era un difetto che si vedeva a occhio nudo, e che nessuno prese abbastanza sul serio.

### La spiegazione da manuale (e perché è incompleta)

Per decenni, i libri di testo hanno raccontato questa storia come l'esempio per eccellenza della **risonanza**: il vento avrebbe soffiato a una frequenza vicina a una delle frequenze proprie di oscillazione del ponte, pompando energia nel sistema oscillante finché l'ampiezza non è diventata distruttiva. È una spiegazione elegante, facile da visualizzare, e — va detto con onestà — **non del tutto corretta**.

Gli studi di ingegneria aerodinamica successivi al crollo hanno mostrato che il meccanismo reale è più sottile e si chiama **flutter aeroelastico**: non è il vento che "spinge a tempo" come qualcuno che dondola un'altalena, ma è l'oscillazione stessa del ponte a modificare il flusso d'aria attorno a sé in un modo che alimenta ulteriormente l'oscillazione — un ciclo che si autosostiene, invece di una semplice forza esterna periodica. La differenza è importante per chi progetta ponti, ma per chi si affaccia per la prima volta alla matematica delle oscillazioni, l'intuizione di partenza — un sistema che oscilla, e che può farlo in modo incontrollato se qualcosa lo alimenta alla frequenza "giusta" — resta un ottimo punto di partenza.

### Dall'aneddoto all'equazione

Cosa hanno in comune un ponte che ondeggia, un'altalena, la corda di una chitarra, e il circuito che sintonizza una radio su una stazione? Tutti obbediscono, in prima approssimazione, alla stessa famiglia di equazioni: le **equazioni differenziali lineari del secondo ordine**.

Nel percorso del corso Pro abbiamo già incontrato le equazioni differenziali del primo ordine: crescita esponenziale, decadimento radioattivo, la legge di raffreddamento di Newton. Sono equazioni che rispondono alla domanda "quanto velocemente cambia questa grandezza?" Le equazioni del secondo ordine rispondono a una domanda leggermente diversa, ma altrettanto naturale: "quanto velocemente cambia la velocità con cui cambia?" — cioè: qual è l'accelerazione? Ed è esattamente la domanda che pone la seconda legge di Newton, \(F=ma\), ogni volta che la forza in gioco dipende dalla posizione stessa dell'oggetto: una molla che richiama, la gravità, l'elasticità di un impalcato che si flette.

Quando si risolvono per bene queste equazioni, emergono con chiarezza matematica tre cose che nella storia di Tacoma Narrows si intrecciano tutte:

- perché un sistema **oscilla** con una frequenza propria, indipendente da chi lo spinge;
- come l'attrito (o la resistenza dell'aria) fa sì che, di norma, un'oscillazione **si smorzi** nel tempo;
- e cosa succede — nel caso limite in cui qualcosa continua ad "alimentare" l'oscillazione proprio alla frequenza giusta — quando l'ampiezza smette di stabilizzarsi e **cresce senza controllo**: la risonanza.

### Continuare la storia

Nell'approfondimento universitario dedicato alle equazioni differenziali riprendiamo esattamente da qui: dall'equazione caratteristica che decide se un sistema oscilla, si smorza dolcemente o torna all'equilibrio senza mai oscillare, fino alla risonanza vera e propria — con tanto di richiamo, doverosamente accompagnato dalle cautele storiche, al ponte che ballò troppo. Si arriva anche oltre: ai sistemi di equazioni e ai loro "ritratti di fase" (spirali che convergono, orbite chiuse, equilibri instabili a forma di sella), e a un primo sguardo su due strumenti — le soluzioni per serie e la trasformata di Laplace — che l'analisi matematica costruisce sopra queste stesse basi.

Se non hai ancora seguito l'introduzione alle equazioni differenziali del corso Pro (variabili separabili, equazioni lineari del primo ordine, il problema di Cauchy), è il prerequisito naturale prima di affrontare questo approfondimento: la matematica, come i ponti ben progettati, si costruisce un piano alla volta.

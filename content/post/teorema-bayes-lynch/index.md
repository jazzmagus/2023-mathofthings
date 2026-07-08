---
title: "Il _Bayesian_: un teorema, una fortuna, un naufragio"
subtitle: "La storia di Mike Lynch, dell'inferenza bayesiana e di uno yacht che portava il nome di un teorema"
summary: "Un uomo costruì un impero da miliardi su un teorema del Settecento, chiamò il suo yacht con quel nome, e in quello stesso yacht trovò la fine. Dietro la cronaca, una delle idee più eleganti della matematica."
authors: [diego fantinelli]
tags: [probabilità, teorema di Bayes, storia, matematica applicata]
categories: [lesson]
date: "2025-09-05T00:00:00Z"
publishDate: "2025-09-05T00:00:00Z"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: "Il veliero Bayesian — un teorema diventato nome"
  focal_point: Center
  placement: 2
  preview_only: false
---

## Una notte al largo di Porticello

Il 19 agosto 2024, poco prima dell'alba, un veliero di 56 metri era all'ancora davanti a Porticello, un piccolo porto della costa siciliana, a poche centinaia di metri dalla riva. Aveva l'albero in alluminio più alto del mondo: 72 metri. Si chiamava *Bayesian*.

In pochi minuti una tromba d'aria — un *downburst*, una colonna d'aria che precipita dal cielo con violenza improvvisa — lo colpì e lo fece capovolgere. La barca affondò quasi subito. Delle persone a bordo, sette non tornarono a riva. Tra loro il proprietario, l'imprenditore britannico **Mike Lynch**, e sua figlia **Hannah**, diciotto anni.

A rendere questa storia degna di una lezione di matematica non è solo la tragedia. È il nome della barca.

## L'uomo che valeva undici miliardi

Mike Lynch non era un naufrago qualunque. Era stato definito "il Bill Gates britannico". Negli anni Novanta aveva fondato **Autonomy**, un'azienda di software capace di fare una cosa che allora sembrava magia: leggere testi, email, telefonate, documenti disordinati, e *capirne il significato* abbastanza da cercarci dentro, classificarli, collegarli.

Nel 2011 la Hewlett-Packard comprò Autonomy per circa **11 miliardi di dollari**. Poco dopo scoppiò la disputa: HP accusò Lynch di aver gonfiato i conti prima della vendita. Ne seguirono tredici anni di battaglie legali tra Regno Unito e Stati Uniti.

Poi, nel **giugno 2024**, la svolta: un tribunale di San Francisco lo **assolse** da tutte le quindici accuse di frode. Dopo più di un decennio, Lynch era di nuovo un uomo libero. La crociera nel Mediterraneo, con la famiglia e alcuni degli avvocati che lo avevano difeso, era la festa per quella assoluzione.

## Perché uno yacht si chiama "Bayesian"

Ed eccoci al punto. Il cuore tecnologico di Autonomy — il motore che permetteva al software di "capire" i testi — era una vecchia idea della teoria della probabilità: l'**inferenza bayesiana**. Quando Lynch comprò il veliero, lo ribattezzò *Bayesian* proprio in omaggio a quella matematica. Il nome della sua fortuna, dipinto sulla poppa.

L'inferenza bayesiana ha un nome perché discende da un teorema pubblicato dopo la morte del suo autore, il reverendo **Thomas Bayes**, nel 1763. Un'idea di due secoli e mezzo fa che, applicata ai computer, ha generato un impero — e ha dato il nome alla barca in cui quell'impero, in un certo senso, è finito.

## Il teorema in una frase

Il teorema di Bayes risponde a una domanda che facciamo di continuo, spesso senza accorgercene:

> *Ho una convinzione. Arriva una nuova informazione. Di quanto devo cambiare idea?*

È il meccanismo con cui aggiorniamo le nostre credenze davanti alle prove. Un medico che aggiunge il risultato di un esame alla sua diagnosi, un giudice che pesa un nuovo indizio, un software che rivede la probabilità che una email sia spam dopo aver letto la parola "vincita": tutti, senza saperlo, ragionano alla maniera di Bayes.

In forma compatta il teorema si scrive così:

$$P(C \mid E) = \frac{P(E \mid C)\, P(C)}{P(E)} \tag{B}$$

dove $C$ è una **causa** (o un'ipotesi) ed $E$ è l'**evidenza** che osserviamo. A parole: la probabilità della causa *dopo* aver visto l'evidenza si ottiene partendo da quanto la ritenevamo probabile *prima*, $P(C)$, e correggendola con quanto l'evidenza è compatibile con quella causa. Il teorema, in fondo, non fa che *capovolgere* il ragionamento: da "quanto è probabile l'effetto data la causa" a "quanto è probabile la causa dato l'effetto".

## Un esempio che spiazza tutti

La forza — e l'insidia — del ragionamento bayesiano si vede meglio con un esempio classico.

Immaginiamo una malattia rara: colpisce **una persona su mille**. Esiste un test molto affidabile: se sei malato, risulta positivo il 95% delle volte. Fai il test. È **positivo**. Quanto devi preoccuparti?

L'istinto grida "95%!". La matematica risponde diversamente. Su centomila persone, i malati sono circa cento, e il test ne individua 95. Ma tra le quasi centomila persone *sane* anche solo un piccolo tasso di errore produce **migliaia** di falsi positivi. Il tuo "positivo" si perde in mezzo a tutti quei falsi allarmi:

$$P(\text{malato} \mid \text{positivo}) \approx 2\%$$

Solo il **due per cento**. Non perché il test sia scadente, ma perché la malattia è così rara che la nostra convinzione di partenza — *quasi certamente sano* — pesa moltissimo. È questo che Bayes ci obbliga a ricordare: **una nuova prova non cancella ciò che già sapevamo, lo corregge**. Chi dimentica il punto di partenza legge male anche l'esame più preciso.

> Chi vuole vedere i conti per esteso li trova nella lezione interattiva sul [Calcolo delle Probabilità](/lezioni/la08-calcolo-probabilita/lezione.html), nel problema del test medico.

## Un teorema, e la sua ironia

Resta un'ultima cosa, che non è matematica ma la matematica aiuta a guardare senza retorica.

Mike Lynch aveva scommesso tutto su un'idea che insegna a *non fidarsi delle certezze* — a tenere sempre aperto lo spazio dell'imprevisto, a dare un peso, per quanto piccolo, anche a ciò che sembra impossibile. Un veliero all'ancora, in una notte d'estate, a poche centinaia di metri dalla riva, è un evento a probabilità di catastrofe bassissima. Bassissima, non nulla.

Il *Bayesian* porta il nome del teorema che, più di ogni altro, ci ricorda che gli eventi rarissimi, semplicemente, ogni tanto accadono. È una lezione severa e bellissima insieme: la stessa matematica che costruisce fortune è quella che ci chiede di non dimenticare mai la coda della distribuzione, il piccolo numero che non arriva mai a zero.

Forse è per questo che vale la pena studiarla.

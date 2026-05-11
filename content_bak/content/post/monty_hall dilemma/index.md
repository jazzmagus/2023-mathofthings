---
title: Il dilemma di Monty Hall
subtitle: introduzione al calcolo delle probabilità
summary: brain food
authors:
- diego fantinelli
tags: [itis, lesson, 2022]
categories: []
date: "2022-07-23T00:00:00Z"
featured: true
draft: false

# links:
#  - icon_pack: fab
#    icon: 
#    name: SLIDES
#    url: dunning_kruger_effect

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
image:
  caption: ''
  focal_point: "center"
  placement: 2
  preview_only: false

# slides: 
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

# Set captions for image gallery.
# gallery_item:
# - album: gallery
#   caption: Default
#   image: theme-default.png
# - album: gallery
#   caption: Ocean
#   image: theme-ocean.png
# - album: gallery
#   caption: Forest
#   image: theme-forest.png
# - album: gallery
#   caption: Dark
#   image: theme-dark.png
# - album: gallery
#   caption: Apogee
#   image: theme-apogee.png
# - album: gallery
#   caption: 1950s
#   image: theme-1950s.png
# - album: gallery
#   caption: Coffee theme with Playfair font
#   image: theme-coffee-playfair.png
# - album: gallery
#   caption: Strawberry
#   image: theme-strawberry.png
---

<!-- {{< toc hide_on="xl" >}} -->

><i class="fa-solid fa-quote-left"></i> The function of wisdom is to discriminate between good and evil <i class="fa-solid fa-quote-right"></i>
><br>&mdash; <cite>Cicerone</cite>

## Introduzione alla probabilità

>In un popolare show televisivo americano il presentatore mostra al concorrente tre porte chiuse. Dietro a una di esse si cela il premio in palio, un'automobile; le altre due nascondono una capra. 
>Il giocatore sceglie una delle tre porte, poi il conduttore, che **sa qual è quella vincente**, ne apre un'altra mostrando una capra. 
>A questo punto il concorrente deve fare la scelta definitiva:
>- è più conveniente confermare oppure cambiare porta per ottenere il premio?

Il quesito è noto come dilemma o paradosso di Monty Hall, dal nome del conduttore del celebre gioco a premi televisivo americano Let's Make a Deal.

Quando nel 1990 un lettore della rivista Parade scrisse alla rubrica Ask Marilyn chiedendo quale fosse la strategia vincente, il problema si trasformò in un'accesa controversia. 

- La soluzione proposta da Marilyn Vos Savant, presente nel Guinness dei Primati per il suo altissimo quoziente d'intelligenza, scatenò una valanga di lettere di contestazione, molte delle quali provenivano da matematici e accademici che accusavano Vos Savant di ignorare la teoria della probabilità. 
- Il giornale diventò l'arena di un furente botta e risposta: da una parte **Vos Savant**, secondo la quale **al giocatore conviene sempre cambiare porta**; dall'altra chi sosteneva che è indifferente scegliere l'una o l'altra delle due porte rimanenti. Il caso finì persino in prima pagina sul New York Times, acquisendo in breve tempo un'enorme popolarità. 

Chi aveva ragione?

### Esaminiamo il problema: 
- secondo la definizione classica della probabilità di un evento, data dal rapporto tra il numero di casi favorevoli e il numero di casi possibili, quando il concorrente sceglie una delle tre porte chiuse ha una probabilità pari a $\dfrac{1}{3}$ di vincere il premio.
- Dopo che il presentatore ha aperto una porta, mostrando una capra, si potrebbe pensare che la probabilità di aver indovinato la porta esatta salga da $\dfrac{1}{3}$ a $\dfrac{1}{2}$. 
	- Dopo tutto, restano due porte chiuse e una delle due nasconde l'auto. Pertanto, la probabilità che questa sia dietro l'una o dietro l'altra è identica e pari a $\dfrac{1}{2}$. 
	- A questo punto il giocatore può scegliere a piacimento, perché è indifferente cambiare o non cambiare. 
- <mark class="hltr-yellow">Risposta sbagliata</mark> !

- Infatti, il concorrente ha ancora una probabilità su tre di aver indovinato la porta esatta. 
	- La probabilità che l'automobile sia dietro una delle due porte non scelte è $\dfrac{2}{3}$ e, quando il presentatore rivela quale di queste due non nasconde il premio, la probabilità che l'automobile sia dietro l'altra porta è ancora $\dfrac{2}{3}$. 
	- Di conseguenza, se il giocatore mantiene la scelta iniziale, ha una probabilità di vincere pari a $\dfrac{1}{3}$, se cambia, pari a $\dfrac{2}{3}$.

## un approccio diverso

Si può arrivare alla stessa conclusione seguendo un'altra argomentazione, che convincerà i più scettici. 

> Partiamo dal presupposto (fondamentale!) che il conduttore conosce qual è la porta che nasconde l'automobile e apre sempre una porta con dietro una capra. 

- Ora, supponiamo che la prima porta scelta dal giocatore sia sbagliata e nasconda una capra. Il conduttore non ha scelta e aprirà l'altra porta con la capra. In questo caso, se il giocatore cambia porta, vince. 
- Se invece la prima porta scelta dal giocatore è esatta e il giocatore cambia, ovviamente perde. 
	- Possiamo concludere che, se il giocatore cambia porta, vince se e solo se la sua prima scelta era sbagliata, evento che ha probabilità pari a $\dfrac{2}{3}$.
	- Se la strategia del giocatore è di non cambiare mai, vince se e solo se la sua prima scelta è corretta, evento con probabilità $\dfrac{1}{3}$.
- Anche se apparentemente contro-intuitiva, la risposta di Vos Savant era esatta. 

Perché allora moltissime persone rimasero persuase del contrario? 
- Alla base della controversia c'è probabilmente un punto chiave del problema: **il conduttore sa qual è la porta vincente**. 
- Se il conduttore non sapesse dove si nasconde l'automobile (e quindi potesse anche aprire la porta fortunata), allora al giocatore resterebbero due porte con identica probabilità: cambiando o non cambiando, il concorrente avrebbe la stessa probabilità di vincere o perdere.

> Questo paradosso è una variante del paradosso delle tre carte del matematico americano Warren Weaver (1950), il quale, a sua volta, deriva dal paradosso delle tre scatole, formulato per la prima volta nel 1889 dal matematico francese Joseph Bertrand.

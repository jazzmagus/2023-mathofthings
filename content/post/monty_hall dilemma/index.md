---
title: Il dilemma di Monty Hall
subtitle: introduzione al calcolo delle probabilit√†
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

## Introduzione alla probabilit√†

>In un popolare show televisivo americano il presentatore mostra al concorrente tre porte chiuse. Dietro a una di esse si cela il premio in palio, un'automobile; le altre due nascondono una capra. 
>Il giocatore sceglie una delle tre porte, poi il conduttore, che **sa qual √® quella vincente**, ne apre un'altra mostrando una capra. 
>A questo punto il concorrente deve fare la scelta definitiva:
>- √® pi√Ļ conveniente confermare oppure cambiare porta per ottenere il premio?

Il quesito √® noto come dilemma o paradosso di Monty Hall, dal nome del conduttore del celebre gioco a premi televisivo americano Let's Make a Deal.

Quando nel 1990 un lettore della rivista Parade scrisse alla rubrica Ask Marilyn chiedendo quale fosse la strategia vincente, il problema si trasform√≤ in un'accesa controversia. 

- La soluzione proposta da Marilyn Vos Savant, presente nel Guinness dei Primati per il suo altissimo quoziente d'intelligenza, scaten√≤ una valanga di lettere di contestazione, molte delle quali provenivano da matematici e accademici che accusavano Vos Savant di ignorare la teoria della probabilit√†. 
- Il giornale divent√≤ l'arena di un furente botta e risposta: da una parte **Vos Savant**, secondo la quale **al giocatore conviene sempre cambiare porta**; dall'altra chi sosteneva che √® indifferente scegliere l'una o l'altra delle due porte rimanenti. Il caso fin√¨ persino in prima pagina sul New York Times, acquisendo in breve tempo un'enorme popolarit√†. 

Chi aveva ragione?

### Esaminiamo il problema: 
- secondo la definizione classica della probabilit√† di un evento, data dal rapporto tra il numero di casi favorevoli e il numero di casi possibili, quando il concorrente sceglie una delle tre porte chiuse ha una probabilit√† pari a $\dfrac{1}{3}$ di vincere il premio.
- Dopo che il presentatore ha aperto una porta, mostrando una capra, si potrebbe pensare che la probabilit√† di aver indovinato la porta esatta salga da $\dfrac{1}{3}$ a $\dfrac{1}{2}$. 
	- Dopo tutto, restano due porte chiuse e una delle due nasconde l'auto. Pertanto, la probabilit√† che questa sia dietro l'una o dietro l'altra √® identica e pari a $\dfrac{1}{2}$. 
	- A questo punto il giocatore pu√≤ scegliere a piacimento, perch√© √® indifferente cambiare o non cambiare. 
- <mark class="hltr-yellow">Risposta sbagliata</mark> !

- Infatti, il concorrente ha ancora una probabilit√† su tre di aver indovinato la porta esatta. 
	- La probabilit√† che l'automobile sia dietro una delle due porte non scelte √® $\dfrac{2}{3}$ e, quando il presentatore rivela quale di queste due non nasconde il premio, la probabilit√† che l'automobile sia dietro l'altra porta √® ancora $\dfrac{2}{3}$. 
	- Di conseguenza, se il giocatore mantiene la scelta iniziale, ha una probabilit√† di vincere pari a $\dfrac{1}{3}$, se cambia, pari a $\dfrac{2}{3}$.

## un approccio diverso

Si pu√≤ arrivare alla stessa conclusione seguendo un'altra argomentazione, che convincer√† i pi√Ļ scettici. 

> Partiamo dal presupposto (fondamentale!) che il conduttore conosce qual √® la porta che nasconde l'automobile e apre sempre una porta con dietro una capra. 

- Ora, supponiamo che la prima porta scelta dal giocatore sia sbagliata e nasconda una capra. Il conduttore non ha scelta e aprir√† l'altra porta con la capra. In questo caso, se il giocatore cambia porta, vince. 
- Se invece la prima porta scelta dal giocatore √® esatta e il giocatore cambia, ovviamente perde. 
	- Possiamo concludere che, se il giocatore cambia porta, vince se e solo se la sua prima scelta era sbagliata, evento che ha probabilit√† pari a $\dfrac{2}{3}$.
	- Se la strategia del giocatore √® di non cambiare mai, vince se e solo se la sua prima scelta √® corretta, evento con probabilit√† $\dfrac{1}{3}$.
- Anche se apparentemente contro-intuitiva, la risposta di Vos Savant era esatta. 

Perch√© allora moltissime persone rimasero persuase del contrario? 
- Alla base della controversia c'√® probabilmente un punto chiave del problema: **il conduttore sa qual √® la porta vincente**. 
- Se il conduttore non sapesse dove si nasconde l'automobile (e quindi potesse anche aprire la porta fortunata), allora al giocatore resterebbero due porte con identica probabilit√†: cambiando o non cambiando, il concorrente avrebbe la stessa probabilit√† di vincere o perdere.

> Questo paradosso √® una variante del paradosso delle tre carte del matematico americano Warren Weaver (1950), il quale, a sua volta, deriva dal paradosso delle tre scatole, formulato per la prima volta nel 1889 dal matematico francese Joseph Bertrand.
---
title: Il concetto di Modello Matematico
subtitle: _da Newton ad Heisemberg_
summary: Modello Matematico
authors:
- diego fantinelli
tags: [itis, lesson, 2022]
categories: [infos]
date: "2022-03-30T00:21:00Z"
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
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/We02LAPNpa8'
  focal_point: ""
  preview_only: false

# slides: 
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

# Set captions for image gallery.
gallery_item:
- album: gallery
  caption: Default
  image: theme-default.png
- album: gallery
  caption: Ocean
  image: theme-ocean.png
- album: gallery
  caption: Forest
  image: theme-forest.png
- album: gallery
  caption: Dark
  image: theme-dark.png
- album: gallery
  caption: Apogee
  image: theme-apogee.png
- album: gallery
  caption: 1950s
  image: theme-1950s.png
- album: gallery
  caption: Coffee theme with Playfair font
  image: theme-coffee-playfair.png
- album: gallery
  caption: Strawberry
  image: theme-strawberry.png
---

<!-- {{< toc hide_on="xl" >}} -->

# Il concetto di modello matematico

>Nei casi concreti, l'analisi e la modellizzazione di un fenomeno casuale avviene solitamente secondo le fasi sintetizzate nel seguente schema.

```mermaid
graph TD

A[Esperimento Casuale] --> B(osservazione)

B --> |statistica descrittiva| C(analisi dati)

C --> D{confronto}

A --> E(modello)

E -->|Calcolo delle Probabilità| G[Previsioni]

G --> D

D --> H[validazione o <br> correzione del modello]
```

- La costruzione del modello del fenomeno casuale consiste nel definire alcune variabili aleatorie che descrivono il fenomeno in esame e assegnare a tali variabili aleatorie una distribuzione di probabilità. 
  - Questa fase è la più delicata perché comporta un certo grado di <mark class="hltr-yellow">arbitrarietà</mark> nella scelta della distribuzione più adeguata.
- Naturalmente, nella costruzione del modello non si procede arbitrariamente, ma si cerca di descrivere nel miglior modo possibile gli aspetti di interesse del fenomeno che si sta studiando. 
- Tuttavia, dopo aver trovato un modello che, almeno a priori, sembra ragionevole, esso dovrà essere «messo alla prova", **confrontando** con i dati empirici le previsioni che consente di effettuare. 
- Nel caso si riscontrino delle significative discrepanze con i dati reali, occorre cercare di **modificare** il modello per renderlo più aderente alla realtà; nel caso in cui, invece, si abbia conferma di aver trovato un buon modello, non è tuttavia detto che esso sia necessariamente l'unico valido o che non sia ulteriormente migliorabile. 

>Si intravede così la moderna concezione di modello matematico come rappresentazione formale di un fenomeno, che non pretende di spiegarlo o di scoprime l'intima essenza, ma solo di darne un'immagine che descriva bene alcuni suoi aspetti. 

- Un modello va dunque valutato soltanto in base alla sua efficacia e un buon modello non è detto che sia l'unico possibile. 
  - Si tratta di un approccio opposto a quello della fisica classica:per Newton l'obiettivo fondamentale non era l'utilità ma la <mark class="hltr-cyan">ricerca della verità</mark>, la scoperta delle cause di un fenomeno, la loro spiegazione, fino a giungere alla causa prima. Non è un caso, quindi, che la moderna modellistica matematica e la diffusione dei modelli matematici anche nell'ambito di discipline diverse dalla fisica abbiano avuto origine proprio con la crisi di uno dei principi fondamentali della fisica classica: quello del <mark class="hltr-cyan">determinismo</mark>, secondo cui *la conoscenza della posizione e della velocità di un punto materiale, nonché della legge del suo moto, determinano in modo univoco la sua evoluzione*.

- A scardinare questo principio fu principalmente la scoperta, da parte di Werner Karl Heisenberg (1927), che <mark class="hltr-yellow">a livello microscopico la posizione e la velocità di una particella non possono essere determinate simultaneamente</mark>; si può soltanto determinare la **probabilità** che la particella si trovi in un punto anziché in un altro, oppure che abbia una velocità piuttosto che un'altra. 

>- Il comportamento della particella non può dunque essere previsto in modo certo, come normalmente accadeva nella fisica classica.

- Ne seguì una progressiva crisi della concezione puramente deterministica, che lasciò gradualmente spazio a un approccio nuovo ai problemi, di tipo <mark class="hltr-green">modellistico e probabilistico</mark>, ben sintetizzato dalle parole di uno dei massimi scienziati del novecento, John von Neumann (1903-1957):
  
>- «Le scienze non cercano di spiegare, a malapena tentano di interpretare, ma fanno soprattutto dei modelli. Per modello si intende un costrutto matematico che, con l'aggiunta di certe interpretazioni verbali, descrive dei fenomeni osservati. La giustificazione di un siffatto costrutto matematico è soltanto e precisamente che ci si aspetta che funzioni, cioè che descriva correttamente i fenomeni di un'area ragionevolmente ampia."
---
title: Trinomio Particolare di secondo grado
summary: An example of using the in-built project page.
tags:
- fattorizzazione
date: "2016-04-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/georgecushen
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: trinomio_particolare
---



> `fas:QuoteLeft` The real problem is not whether machines think but whether men do.
> &mdash; <cite>B. F. Skinner</cite>

> **references**: 
> - [[00 Maths Index]]
> - [[esercizi proposti classi prime|esercizi selezionati]]

# Scomporre il trinomio particolare di secondo grado

> un **trinomio particolare di secondo grado**, detto anche trinomio *notevole*, oppure trinomio *speciale* di secondo grado è un trinomio del tipo: 
> $$x^2+sx+p$$
> dove $s$ e $p$ hanno un significato particolare e servono per ricordare uno dei metodi utilizzati per fattorizzare questo particolare tipo di polinomio; per fare un esempio di come si presenta un trinomio particolare: $$x^2+5x+6$$ 
>Esistono diversi modi per fattorizzare un trinomio di secondo grado e qui ne esporremo solo alcuni

## scomposizione del trinomio particolare di scondo grado con il metodo *somma-prodotto*

> l'idea è quella di cercare una coppia di numeri la cui somma sia uguale a $s$ e il loro prodotto sia uguale a $p$.
> Se riusciamo a trovarli - chiamiamoli ad esempio $a$ e $b$, allora il nostro trinomio particolare si potrà fattorizzare nel modo seguente: $$(x+a)\cdot (x+b)$$
- consideriamo il seguente trinomio particolare: $$x^2+5x+6$$
### primo procedimento
- in questo caso $s=+5$ e $t=+6$
- cerchiamo due numeri $a$ e $b$ con le seguenti caratteristiche:
	1. la loro somma è uguale a $s$, cioè $a+b=s$
	2. il loro prodotto è uguale a $p$, cioè $a \cdot b=p$
- per trovare $a$ e $b$ cerchiamo quelle coppie di numeri che **moltiplicati tra loro** diano come risultato $p$; esse sono: $(6,1)$ e $(3,2)$
- ora scegliamo tra le due, quella i cui numeri sommati tra loro diano come risultato $s$: 
	- la coppia $(a, b)$ cercata sarà quindi la coppia $(3, 2)$
- a questo punto non resta che scrivere il trinomio iniziale nella forma fattorizzata: $$(x+a) \cdot   (x+b)$$
- nel nostro caso: $$(x+2)\cdot (x+3)$$
> **osservazione**: 
> - per la proprietà **commutativa** del prodotto, non ha alcuna importanza l'ordine con cui si scrivono i fattori ottenuti: $(x+2)\cdot (x+3) =  (x+3) \cdot (x+2)$
> - nel caso in cui i segni di  $s$ e $p$ siano uguali - entrambi positivi o entrambi negativi -  allora i segni di  $a$ e di $b$ saranno uguali, altrimenti avranno segno opposto.

### secondo procedimento

- una volta determinata la coppia come nel precedente esercizio, si può  anche riscrivere il polinomio iniziale nel modo seguente: $$x^2+(2x+3x)+6= x^2+2x+3x+6$$
- dove $5x$ è stato riscritto come somma dei due termini della coppia trovata $(3, 2)$
- a questo punto si può applicare un raccoglimento parziale, ottenendo: $$x(x+2)+3(x+2)$$
- ed infine, con un raccoglimento a fattor comune totale del binomio $(x+2)$, ottenendo: $$(x+3) \cdot (x+2)$$
## scomposizione del trinomio particolare di scondo grado quando il coefficiente del termine di secondo grado è diverso da 1

- a differenza del caso più generale
- la soluzione si potrà scrivere nel seguente modo: $$(ax+n_1) \cdot (x+ \dfrac{n_2}{a})$$
- oppure, in modo del tutto equivalente:  $$(ax+n_2) \cdot (x+ \dfrac{n_1}{a})$$

>Esempio: 
>
>- Il trinomio $2 x^{2}+5 x-3$ ha il coefficiente di $x^{2}$ diverso da 1. 
>- Per scomporlo occorre trovare due numeri che abbiano come somma il coefficiente di $x$, cioè $+5$, e come prodotto il prodotto del coefficiente di $x^{2}$ con il termine noto, cioè $2 \cdot(-3)=-6$.
>	- volendo, si può anche pensare che il termine noto sia diventato $-6$
>- cerchiamo $a$ e $b$ come al solito, tra le coppie di divisori di $-6$, esse sono: $(6, 1)$ e $(3, 2)$
>- teniamo la coppia $(6,-1)$
>	- abbiamo "aggiustato" i segni dato che i segni di $s$ e di $p$ sono opposti
>- a questo punto possiamo già scrivere la soluzione:
>$$2 x^{2}+5 x-3 = (2x-1) \cdot \left(x+ \dfrac{\cancel{6}}{\cancel{3}}\right)= (2x+1) \cdot (x+3)$$
<p style=" text-indent:75%; text-align:left;color:orange">&#9634</p>

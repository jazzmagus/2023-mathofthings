---
title: 1. Numeri naturali e numeri interi relativi
linktitle: Capitolo 1 numeri Naturali e Interi Relativi
toc: true
type: docs
date: "2021-09-09T00:00:00+01:00"
draft: false
diagram: true
menu:
  math-01:
    parent: 
    weight: 

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 10
---

{{< toc >}}
<!-- {{< toc hide_on="xl" >}} -->

> ☆ **scadenza**: 30 settembre 2021

![ex1_img](../majong_01.png)

---

## Conoscenze

- Proprietà degli insiemi numerici $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ e consapevolezza della necessità degli ampliamenti da $\mathbb{N}$ a $\mathbb{Z}$, da $\mathbb{Z}$ a $\mathbb{Q}$, da $\mathbb{Q}$ a $\mathbb{R}$.
Rappresentazione degli insiemi numericisu una retta orientata.
- Definizioni e proprietà delle quattro operazioni e delle potenze nei quattro insiemi numerici.

- `Divisibilità` in $\mathbb{N}$ e `numeri primi`;
 `mcm` e `MCD` di due o più numeri naturali.

- Concetto di `numero relativo` e di `valore assoluto`; *regola dei segni*.

- **Numeri razionali**: frazioni e rappresentazione decimale.
 Notazione `esponenziale` e notazione `scientifica` di un numero: ordine di grandezza.
 **Proporzioni** e **percentuali**.

- **Numeri irrazionali** e loro rappresentazione decimale.
 Concetto di `approssimazione` ed `errore` di un’approssimazione.

---

## Abilità

- Eseguire i calcoli con i numeri degli insiemi numerici  $\mathbb{N}$, $\mathbb{Z}$ e $\mathbb{Q}$
- Scomporre un numero naturale in fattoriprimi e calcolare il `mcm` e il `MCD` tra due o più numeri naturali.
Trasformare la scrittura di un numero naturale dalla base $10$ alla base $b$ e viceversa.
- Trasformare una frazione in numero decimale e viceversa;
scrivere un numero decimale finito in notazione scientifica e determinarne l’`ordine di grandezza`.
- Risolvere problemi su **proporzioni** e **percentuali**.
Calcolare l’errore relativo di un’approssimazione conoscendo l’errore assoluto e viceversa e determinare il valore abbreviato e quello arrotondato di un numero decimale.

---

## competenze

- Utilizzare le tecniche e le procedure del calcolo aritmetico ed algebrico, rappresentandole anche sottoforma grafica.
- Analizzare dati e interpretarli sviluppando deduzioni e ragionamenti sugli stessi anche con l’ausilio dirappresentazioni grafiche, usando consapevolmente gli strumenti di calcolo e le potenzialità offerte da applicazioni specifiche di tipo informatico.

{{< youtube cCJU5By_b8U>}}
## L’insieme dei numeri naturali

<!-- {{< figure src="../majong_01.png" caption="A caption" numbered="true" >}} -->

> Numeri, continuamente numeri: il numero dei giri, il numero della macchina, il distacco, il tempo trascorso, il tempo che manca, il numero sulla maglia, il punteggio...
>
> - Servono veramente tutti questi numeri?
> - Sono essenziali o se ne potrebbe fare a meno?

### 1. numeri naturali e loro ordinamento

- come si rappresentano gli insiemi numerici?

$$ \mathbb{N} = \\{ 0; 1; 2; 3; \dots \\} $$

>**osservazione**: l'inserimento dello `zero` nell'insieme $\mathbb{N}$ è ancor oggi una questione controversa, tanto che, a volte, si rende necessario distinguere i due *diversi* insiemi $\mathbb{N}$ in:

- $\mathbb{N}$: insieme dei numeri naturali, compreso lo `zero` (regalatoci dagli indiani...)

- $\mathbb{N^*}$: insieme dei numeri naturali, escluso lo `zero`

Nascono comunque dall'attività dell'uomo del `contare`, per questo vengono detti **naturali**.

## proprietà dell’insieme $N$

- L’insieme dei numeri naturali è `infinito`.
- Ogni numero naturale ha un `successivo`.
- Ogni numero naturale, eccetto lo zero, ha un `precedente`.
- Lo `zero` è l’elemento `minimo` dell’insieme dei numeri naturali.
- L’insieme dei numeri naturali `non` ha un elemento `massimo`

Per indicare che due numeri $a$ e $b$ sono uguali, useremo il simbolo $=$ e scriveremo: $$a=b$$ leggendo «*$a$ è uguale a $b$*»;

- la precedente **relazione** è `bidirezionale`, cioè deve intendersi nelle due direzioni, *sempre*.

Il termine a **sinistra** dell'uguale viene chiamato **primo membro**, mentre quello a **destra** si indica con **secondo membro**.

>ad esempio: $$17=17$$

La relazione di **uguaglianza** tra due numeri naturali gode delle seguenti proprietà:

- **riflessiva**: ogni numero è uguale a se stesso: $a=a$;
- **simmetrica**: se $a=b$ allora $b=a$;
- **transitiva**: se $a=b$ e $b=c$ allora $a=c$.

- I numeri naturali hanno un `ordine`, cioè, dati due numeri naturali, diversi tra loro, è sempre possibile confrontarli stabilendo tra essi una relazione di **disuguaglianza**:
  - se nella successione dei numeri naturali un numero $a$ precede un numero $b$, si dice che $a$ è **minore** di $b$ e si scrive: $$a<b$$
  - se invece $a$ segue $b$, si dice che $a$ è **maggiore** di $b$ e si scrive: $$a>b$$
- per indicare le relazioni d'ordine vengono utilizzati anche i simboli di **disuguaglianza**:
  - **maggiore o uguale**: si indica con il simbolo "$\geq$": $$a \geq b$$
    - **minire o uguale**: si indica con il simbolo "$\leq$": $$a \leq b$$
  >es.: proprietà transitiva della **disuguaglianza**:
  >
  >- se $a \leq b$ e $b \leq c$, allora $a \leq c$
  >
- I numeri naturali possono essere facilmente **rappresentati** graficamente attraverso una **semiretta orientata**

![semiretta numeri naturali](../semiretta_naturali.svg)

## Le quattro operazioni aritmetiche con i numeri naturali

### 2. addizione e sue proprietà

>**definizione**: la **somma** di due numeri naturali è quel numero naturale che si ottiene contando di seguito al primo tutte le unità del secondo.

1. proprietà **commutativa**:
   - cambiando l'**ordine** degli addendi il risultato non cambia: $$a+b=b+a$$
2. proprietà **associativa**:
   - la somma di tre numeri non cambia se a due addendi consecutivi si sostituisce la loro somma: $$(a+b)+c=a+(b+c)$$
3. Esiste l'**elemento neutro** dell’addizione:
   - è il `numero zero`. Ciò significa che sommando *zero* a qualsiasi numero si ottiene il numero dato

---

### 3. sottrazione e sue proprietà

- è un’operazione che si esegue tra due numeri, considerati nell’ordine, il primo detto `minuendo` e il secondo `sottraendo`. Il risultato della sottrazione si chiama `differenza`.

>**definizione**: la **differenza** tra due numeri naturali è quel numero naturale, se esiste, che addizionato al `sottraendo` dà come somma il `minuendo`.
>
>- esempio: $5-2=3$ perché $5=3+2$

- casi particolari:
- La sottrazione $4-6$ non si può eseguire in $\mathbb{N}$ perché non esiste alcun numero naturale che, sommato a $6$, dia $4$.
- La sottrazione, nell’insieme dei numeri naturali, si può eseguire solo se il minuendo è **maggiore** o **uguale** al sottraendo: $$a-b=c \rightarrow a= b+c$$ con $$a\geq c$$

- La sottrazione gode della proprietà `invariantiva`: se si somma o si sottrae uno stesso numero sia al minuendo sia al sottraendo, la differenza non cambia: $$(a-b)=(a+c)-(b+c)$$
  - Grazie alla proprietà invariantiva possiamo eseguire rapidamente alcune sottrazioni: $$(198-48)=(198+2)-(48+2)=200-50=150$$

- La sottrazione **non** gode della proprietà **commutativa**: $7- 5 =2$, ma $5-7$ non è calcolabile in $\mathbb{N}$ e non ammette elemento neutro: $2- 0 =2$, ma $0-2$ non si può eseguire in $\mathbb{N}$.
- La sottrazione **non** gode neppure della proprietà **associativa**.
  - Ad esempio per calcolare $15-4-2$ è necessario eseguire le sottrazioni `nell’ordine` indicato: $$\underbrace{(15-4)}_{11}-2=9$$

---

### 4. moltiplicazione e sue proprietà

>**definizione**: **prodotto** di due numeri naturali
>
>- è la somma di tanti addendi uguali al primo fattore quante sono le unità indicate dal secondo: $$a \cdot b= \underbrace{a+a+a+ \ldots + a}_{b \\; \text{addendi}}$$

1. proprietà **commutativa**: il prodotto tra due o più fattori non cambia se cambia il loro `ordine`: $$a \cdot b = b \cdot a$$
1. proprietà **associativa**: il prodotto di tre numeri non cambia se a due fattori consecutivi si sostituisce il loro prodotto: $$(a \cdot b)\cdot c= a \cdot (b \cdot c)$$
1. proprietà **distributiva**:
   - della moltiplicazione rispetto alla addizione: $$a \cdot (b+c)= a \cdot b + a \cdot c$$
   - della moltiplicazione rispetto alla sottrazione: $$a \cdot (b-c)= a \cdot b - a \cdot c$$
1. raccoglimento a `fattor comune`: si ottiene leggendo nell'altro verso la proprietà distributiva: se in una somma **tutti** gli addendi hanno un `fattore` in comune, esso può essere `raccolto` e `moltiplicato` per la somma degli altri termini; allo stesso modo per la differenza:
$$\underbrace{3 \cdot 7 + 3 \cdot 5}\_{21+15=36} = \underbrace{3 \cdot (7+5)}\_{3 \cdot 12 = 36} \qquad \underbrace{8 \cdot 12-8 \cdot 9}\_{96-72=24}=\underbrace{8 \cdot(12-9)}\_{8 \cdot 3=24}$$
1. esistenza dell'elemento `neutro`: moltiplicando qualsiasi numero per `uno` si ottiene il numero dato
1. esistenza dell'`elemento annullatore`: moltiplicando qualsiasi numero per `zero` si ottiene `zero`
1. **Legge di annullamento del prodotto**: se il prodotto tra due o più fattori è `zero` allora almeno uno dei fattori è `zero`

---

### 5. divisione e sue proprietà

>Il `quoziente` tra due numeri naturali, dei quali il secondo diverso da `zero`, è quel numero naturale, se esiste, che moltiplicato per il `divisore` dà il `dividendo`:
>
>- $a : b=c$, con $b \neq 0$, $\underbrace{\Longrightarrow}_{\text{implica}} a=b \cdot c$
>
>se la divisione si può eseguire in $\mathbb{N}$, allora si dice che $a$ è **divisibile** per $b$ o anche che $b$ è **multiplo** di $a$.
>
>- Ad esempio $24$ è divisibile per $6$  e $24$ è multiplo di $6$
>- La divisione $19:5$ non può essere eseguita in $\mathbb{N}$, poiché non esiste alcun numero naturale che, moltiplicato per $5$, dia $19$.
>
>**ATTENZIONE**:
>
>- Non è invece possibile eseguire la divisione di un numero naturale e lo `zero`, poiché il risultato dovrebbe essere un numero che, moltiplicato per `zero` dia il numero iniziale, ma qualsiasi numero moltiplicato per `zero` restituisce `zero`, che rappresenta infatti l'elemento **annullatore** della moltiplicazione.
>- La divisione $0:0$ invece ha infiniti risultati, poiché esistono infiniti numeri che moltiplicati per`zero` danno come risultato `zero`.
>- La divisione per `zero` quindi **non è mai definita**

- **casi particolari**:

| in generale            | esempio | osservazioni|
| ---------------------- | ------- |---|
| $a:1=a$                | $6:1=6$ |$1$ può essere considerato l'*elemento neutro* della divisione|
| $a:a=1$, con $a \neq 0$               | $6:6=1$ | se *dividendo* e *divisore*, entrambi $\in \mathbb{N}$ sono uguali, il risultato della divisione è l'**unità**
| $0:a=0$, se $a \neq 0$ | $0:6=0$ |lo $0$ al **dividendo** può essere considerato l'*elemento annullatore* della divisione|

`Q: Qual è la differenza tra divisione e quoziente?`

### proprietà invariantiva della divisione

- se si moltiplicano o si dividono sia il dividendo sia il divisore per uno stesso numero - diverso da zero -, il quoziente non cambia:

  - $a:b=(a \cdot c):(b \cdot c)$
  - **esempio**:
$$65:5=(65 \cdot 2):(5 \cdot 2)=130:10=13$$

  - $a:b=(a : c):(b : c)$

  - **esempio**:
$$72:12=(72 : 2):(12 : 2)=36:6=6$$

---

### proprietà distributiva della divisione

- rispetto alla **addizione**:
  - per dividere una `somma` per un `numero` si può dividere ciascun addendo per quel numero e quindi sommare i quozienti:
  - $$(a+b):c=a:b+a:c$$
  - $$\underbrace{(32+24)}_{56}:8=32:8+24:8=4+3=7$$

- rispetto alla **sottrazione**:
  - per `dividere` una `differenza` per un `numero` si possono dividere sia il `minuendo` sia il `sottraendo` per quel numero e quindi eseguire la `sottrazione` tra i `quozienti`:
  - $$(a-b):c=a:b-a:c$$
  - $$\underbrace{(32-24)}_{8}:8=32:8-24:8=4-3=1$$

>La proprietà distributiva della divisione può essere applicata per eseguire più rapidamente alcune divisioni:
>$$612:6=(600+12):6=600:6+12:6=100+2=102$$

- **Non** esistono proprietà distributive per dividere un numero per una somma o per una differenza.
$$a:(b+c) \neq a:b+a:c$$

---

### divisione approssimata - con resto

- Se il dividendo **non** è multiplo del divisore, la divisione esatta non si può eseguire. Si può ricorrere allora alla divisione approssimata che associa al dividendo e al divisore due numeri naturali, detti rispettivamente `quoziente` e `resto`.

- Il **quoziente** della divisione approssimata è il più grande numero naturale che, moltiplicato per il divisore, dà un prodotto minore o uguale al dividendo.
- Il **resto** è la **differenza** tra il dividendo e tale prodotto.
- Il resto risulta **sempre minore** del divisore

> se $r=0$, allora l'uguaglianza $a=b \cdot q +r$ diviene:
> $$a=b \cdot q$$
> che è la definizione di divisione che risulterà pertanto `esatta`

$$a:b=q \\; \text{con resto }r \\; \longleftrightarrow \quad a=b \cdot q +r \quad(r <b)$$

### Proprietà invariantiva della divisione approssimata

>se si moltiplicano o si dividono `sia` il dividendo `sia` il divisore per uno stesso numero diverso da zero il quoziente non cambia, mentre il resto risulta moltiplicato o diviso per il numero dato:

$$a:b=q \\; \text{con resto }r \\; \longrightarrow \\; (a \cdot c) : (b \cdot c)= q \\; \text{con resto }(r \cdot c)$$

$$a:b=q \\; \text{con resto }r \\; \longrightarrow \\; (a : c) : (b : c)= q \\; \text{con resto }(r : c)$$

---

## POTENZE in $\mathbb{N}$ e PROPRIETÀ delle POTENZE

### 6. definizione di potenza

> **DEFINIZIONE**:
> La potenza di `base` $a$ ed `esponente` $n$ si indica con $a^n$ ed è uguale al prodotto di $n$ `fattori` uguali ad $a$:
>
> $$a^n = \underbrace{a \cdot a \cdot a \cdot \ldots \cdot a}_{n \\; \text{volte}}$$

Come accade spesso in matematica per le potenze si adottano delle convenzioni:

- $a^1=a$
- $a^0=1$, per $a \neq 0$
- $0^0$ **non ha significato**

**casi particolari**:

- $1^n=1$, per ogni $n$ ($\forall n$)
- $0^n=0 \quad \forall n \neq 0$

---

### 7. proprietà delle potenze

>*approfondimento*: [La memoria umana in gigabytes]({{< relref "/memoria-umana-gigabytes" >}})

- Il **prodotto** di potenze con la stessa base è una potenza che ha per base la stessa base e per esponente la somma degli esponenti:
  - $a^m \cdot a^n = a^{m+n}$
- Il **quoziente** di due potenze con la stessa base è una potenza che ha per base la stessa base e per esponente la differenza degli esponenti:
  - $a^m : a^n = a^{m-n}$, con $(a \neq 0, \\; m \geq n)$
- La **potenza di una potenza** è una potenza che ha per base la stessa base e per esponente il prodotto degli esponenti:
  - $a^m \cdot a^n = a^{m+n}$

>**ATTENZIONE**:
>
>- $(a+b)^n \neq a^n + b^n$
>
>- $(3+4)^2=49$, mentre $3^2 + 4^2 = 25$
>
> - Rif.: MULTIMATH VERDE Vol.1 pag. 43

---

## ESPRESSIONI CON I NUMERI NATURALI

> Le espressioni numeriche sono una **sequenza** di operazioni, da eseguirsi rispettando il loro **grado di priorità**.
>
> 1. elevamenti a potenza
> 1. moltiplicazioni e divisioni
> 1. addizioni e sottrazioni

### 8. Priorità delle operazioni

**ESEMPIO**:

$$
12 - 4 \cdot 2 + 9 : 3 = 12 - 8 + 3 = 4 + 3 = 7
$$

### 9. Le parentesi

> Per indicare che le operazioni si devono eseguire in un ordine diverso da quello dato dal loro **grado di priorità**, si utilizzano le parentesi.

1. Le parentesi, in un’espressione, devono sempre comparire in **coppie**: a ogni parentesi **aperta** deve corrispondere una parentesi **chiusa**.
1. Si devono eseguire per prime le operazioni indicate nelle coppie di parentesi più **interne**, ossia in quelle coppie, formate da una parentesi aperta e una chiusa, all’interno delle quali non vi siano altre parentesi.
1. Tali coppiedi parentesi devono quindi essere **sostituite** con i risultati rispettivamente ottenuti.
1. Si prosegue in questo modo fino a quando non vi sono più parentesi.
1. Nel caso siano indicate di seguito diverse operazioni con lo stesso grado di priorità, esse vanno eseguite nell’ordine dato.

$$168 : 12 \cdot 3 : 2$$

- consideriamo la stessa espressione numerica dell'esempio precedente e riscriviamola utilizzando le parentesi
- `osservazione`: in questo caso risulta evidente che le parentesi sono *ridondanti*, ossia "*di troppo*".

$$
\left[12 - (4 \cdot 2) + (9 : 3) \right] = 12 - 8 + 3 = 4 + 3 = 7
$$

---

### 10. altre proprietà delle operazioni

- Per dividere un **prodotto** per un **numero**, si può dividere uno solo dei fattori per quel numero:
  - $$(a \cdot b \cdot c): d = a \cdot (b:d) \cdot c$$
  - $$(7 \cdot 15 \cdot 6):5 = 7 \cdot (15:5) \cdot 6 = 7 \cdot 3 \cdot 6 = 126$$
  - In particolare, per dividere un prodotto per uno dei suoi fattori, è sufficiente sopprimere quel fattore:
  - $$(a \cdot b \cdot c): b = a \cdot c$$
  - $$ (7 \cdot 15 \cdot 6): 15 = 7 \cdot 6 = 42$$

- Per dividere un **numero** per un **prodotto**, si può dividere successivamente quel numero per ciascun fattore:
  - $$a:(b \cdot c) = (a : b):c$$
  - $$48 : (2 \cdot 3) = (48 : 2) : 3 = 24 : 3 = 8$$
- Per moltiplicare un **numero** per un **quoziente**, si può moltiplicare il numero per il dividendo e poi dividere il prodotto ottenuto per il divisore, oppure dividere il numero per il divisore e successivamente moltiplicare il risultato per il dividendo:
  
$$
a \cdot (b:c)=
\begin{cases}
(a \cdot b):c \\\\
(a : c) \cdot b
\end{cases}
$$

$$
6 \cdot (12:3)=
\begin{cases}
(6 \cdot 12):3 \\\\
(6 : 3) \cdot 12
\end{cases}
$$

---

> **ESERCIZI**: *Rif.: MULTIMATH VERDE Vol.1 pag. 43, n. 67*

---

## Divisibilità e "numeri primi"

### 11. multipli e divisori

### 12. criteri di divisibilità

- **Divisibilità per 2**. Un numero è divisibile per 2 se la sua ultima cifra è **pari**.
- **Divisibilità per 3**. Un numero è divisibile per 3 se la **somma delle sue cifre è divisibile per 3**
- **Divisibilità per 4**. Un numero è divisibile per 4 se il numero formato dalle sue ultime due cifre è divisibile per 4 oppure se le sue ultime due cifre sono due zeri.
- **Divisibilità per 5**. Un numero è divisibile per 5 se la sua ultima cifra è 0 o 5.
- **Divisibilità per 9**. Un numero è divisibile per 9 se la somma delle sue cifre è divisibile per 9.
- **Divisibilità per 10**. Un numero è divisibile per 10 se la sua ultima cifra è 0.
- **Divisibilità per 11**. Un numero è divisibile per 11 se lo è la differenza tra la somma delle sue cifre di posto dispari (contandole per esempio da destra asinistra), eventualmente aumentata di un multiplo di 11, e la somma delle cifre di posto pari.
- **Divisibilità per 25**. Un numero è divisibile per 25 se le sue ultime due cifre sono 00 o 25 o 50 o 75.

### 13. scomposizione in fattori primi

> **definizione**: un numero naturale si dice primo se è **divisibile** solo per se stesso e per $1$
>
> - Il numero $1$, per convenzione, *non* si considera un numero primo.
>
> Ogni numero naturale, diverso da 0, che non sia primo si può esprimere, in un solo modo, come prodotto di fattori primi.
>
> - Scomporre in fattori primi un numero naturale significa determinare tali fattori.
> - Per scomporre un numero in fattori primi si cercano i suoi divisori utilizzando i criteri di divisibilità, partendo dal primo numero della successione dei numeri primi, cioè 2, e procedendo in ordine crescente.
> - Si esegue la divisione del numero dato per il più piccolo numero primo che risulta suo divisore.
> - Si divide il quoziente ottenuto per il suo divisore primo più piccolo e si continua, ripetendo il procedimento, finché il quoziente risulta uguale a 1.

---

## Massimo  comune  divisore  e  minimo  comune  multiplo

### 14. massimo comun divisore MCD

> DEFINIZIONE: **MASSIMO COMUNE DIVISORE**
>
> - Il massimo comune divisore (**MCD**) di due o più numeri naturali, diversi da zero, è il più grande dei loro divisori comuni.

Per determinare il MCD di due o più numeri naturali

1. si scompongono in fattori primi i numeri dati;
2. si moltiplicano fra loro tutti i fattori primi comuni ai numeri dati, presi una sola volta, ciascuno con l’esponente minore con cui figura.

> **NUMERI PRIMI TRA LORO**
>
>- Due o più numeri naturali sono primi tra loro (o coprimi) se il loro massimo comune divisore è 1

### 15. minimo comune multiplo *mcm*

> DEFINIZIONE: **MINIMO COMUNE MULTIPLO**
>
> Il minimo comune multiplo (mcm) di due o più numeri naturali, diversi dazero, è il più piccolo dei loro multipli comuni diversi da zero

Per determinare il mcm di due o più numeri naturali

1. si scompongono in fattori primi i numeri dati;
2. si moltiplicano fra loro tutti i fattori primi, **comuni e non comuni**, dei numeri dati, presi una sola volta, ciascuno con l’esponente maggiore con cui figura.

---

## Sistemi  di  numerazione

### 16. il sistema decimale

### 17. cambiamenti di base

#### dalla base $b$ alla base $10$

#### dalla base $10$ alla base $b$

>Il termine `algoritmo` deriva dal nome del matematico di cultura araba Mohammed ibn-Musa al-Khuwarizmi, che visse a Baghdad nel IX secolod.C.; egli ci tramandò non solo un importante libro di calcolo numerico, ma anche un libro di algebra sulle equazioni di primo e secondo grado che fu basilare per lo sviluppo dell’algebra stessa. La parola algoritmo indica un procedimento di calcolo. Esso consiste in una successione finita di operazioni elementari da eseguire una dopo l’altra in un ordine ben preciso e deve avere le seguenti caratteristiche:
>
>- deve essere `finito` (cioè terminare dopo un numero finito di operazioni),
>- `definito` (ossia essere conciso e non ambiguo),
>- `completo` e deve raggiungere il risultato per il quale è stato progettato.

---

## L’insieme  dei  numeri  interi  relativi $\mathbb{Z}$

### 18. I numeri interi relativi

#### valore assoluto e numeri opposti

##### DEFINIZIONI

- **VALORE ASSOLUTO DI UN NUMERO INTERO RELATIVO**: Il valore assoluto o modulo di un numero intero relativo, positivo o negativo, è il numero stesso privato del suo segno

- **NUMERI OPPOSTI**: Due numeri interi relativi con lo stesso valore assoluto e con segni diversi sono opposti

---

### 19. Rappresentazione dei numeri interi relativi su una retta orientata

## Le quattro operazioni aritmetiche con i numeri interi relativi

- ### 23. addizione

- ### 24. sottrazione

- ### 25. moltiplicazione

- ### 26. divisione

## Potenza di un numero intero relativo

### Le Potenze nell'insieme dei numeri interi relativi

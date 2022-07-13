---
title: 8. Equazioni lineari
linktitle: Capitolo 8 | Equazioni lineari
toc: true
type: docs
date: "2021-09-09T00:00:00+01:00"
draft: false
diagram: true
menu:
  math-02:
    parent: 
    weight: 10

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 10
---

> ☆ **scadenza**: 20 novembre 2021

![ex1_img](../capitolo_8.jpeg)

## obiettivi

{{% toc %}}

<br>

{{% callout note %}}

- alla fine della lezione saremo - *dovremmo essere* - in grado di risolvere le seguenti equazioni lineari:

$$\small{\left(x^{2}-2 x-2\right)^{2}-(x-2) \{(x-2)^{3}-4\left[2(x+1)-(x-1)^{2}\right] \}=11(x-1)}$$

$$\small{(3 x-1)^{3}+(3 x+1)(6 x-7)=(3 x+1)(3 x-1)^{2}}$$

$$\frac{x+3}{x-3}-\frac{2 x-1}{x^{2}-6 x+9}=\left(\frac{3}{x-3}+1\right)^{2}$$
{{% /callout %}}

---

## Concetti fondamentali sulle equazioni

### 1. Le equazioni

{{% callout note %}}
**definizione**:

Un’**equazione** è un’uguaglianza tra due espressioni che contiene una o più lettere.
{{% /callout %}}

### 2. Classificazione delle equazioni

```mermaid
flowchart TD
    id1(EQUAZIONI)

    id2([lineari intere])
    id3([lineari frazionarie])
    id4([numeriche])
    id5([letterali])
    id6([intere])
    id7([frazionarie])
  id1 --- id2
  id1 --- id3
  id1 --- id4
  id1 --- id5
  id5 --- id6
  id5 --- id7
```

---

### 3. Soluzioni e dominio di un’equazione

> <font color="brown">Sostituendo un numero al posto dell’incognita in un’equazione, essa si trasformain un’uguaglianza tra due espressioni, uguaglianza che, se ha significato, può risultare vera o falsa</font>

{{% callout alert %}}
<font color="darkblue">**definizione**: **soluzioni di un'equazione**

I numeri che, sostituiti al posto dell’incognita, trasformano un’equazione in un’uguaglianza vera si dicono **soluzioni**, o **radici**, dell’equazione data</font>

{{% /callout %}}
- Risolvere un’equazione significa determinare tutte le sue soluzioni.
  
  - L’insieme che ha per elementi tutte le soluzioni di un’equazione è l’insieme delle soluzioni e lo indicheremo sempre con $$S= ( \text{S} \subseteq \mathbb{R})$$.
  - In altre parole, risolvere un’equazione significa determinarne l’**insieme delle soluzioni**.
{{% callout warning %}}

<font color="brown">**definizione: DOMINIO DI UN’EQUAZIONE**

Si dice **dominio** di un’equazione l’insieme dei numeri reali che, sostituiti all’incognita, trasformano l’equazione in un’uguaglianza dotata di significato e che quindi è o **vera** o **falsa.**

- Indicheremo sempre con $D$ il dominio;
- poichè le soluzioni di un’equazione devono necessariamente appartenere al dominio dell’equazione stessa, risulta:

$$S \subseteq D \subseteq \mathbb{R}$$
{{% /callout %}}
</font>

<br>

>**ESEMPIO**:
> nella seguente equazione frazionaria:
> $$\dfrac{x -1}{x -2} + x = \dfrac{1}{2}$$
>
> - non è possibile assegnare a $x$ il valore $2$ perché si annullerebbe il denominatore della frazione al primo membro.
> - Per ogni altro valore di $x$ l’equazione si trasformerà in un’uguaglianza vera o falsa.
> - Quindi il dominio dell’equazione è: $$D = \mathbb{R}-\\{2\\}$$

### Equazioni **determinate**, **impossibili**, **indeterminate.**

- Nella risoluzione di un’equazione si possono presentare i seguenti casi.
  - L’insieme delle soluzioni contiene un numero finito di elementi, cioè l’**equazione ha un numero finito di soluzioni**: diremo allora che l’equazione è **determinata.**
    - L’equazione $x^2=4$ è **determinata**, perché i numeri il cui quadrato è $4$ sono $2$ e $-2$ e quindi le soluzioni sono $2$ e $-2$:
    $$S= \\{ -2; \\, 2\\}$$
  - L’insieme delle soluzioni è vuoto $S= \\{\emptyset \\}$, cioè l’equazione **non ha soluzioni**: diremo allora che l’equazione è **impossibile.**
    - L'equazione $x=x+5$ è **impossibile** $\Rightarrow S = \emptyset$
  - L’insieme delle soluzioni contiene un numero infinito di elementi, cioè l’equazione ha **infinite soluzioni**: diremo allora che l’equazione è **indeterminata.**
    - L'equazione: $$(x + 1)^2 = x^2 + 2x + 1$$ è verificata $\forall x \in \mathbb{R}$ e quindi è **indeterminata**: $S = \mathbb{R}$.
    - L'equazione è una **identità** perché è sempre verificata nel suo dominio $D$

<br>

---

### 5. Equazioni equivalenti

<br>
{{% callout alert %}}

<font color="darkblue">**definizione: EQUAZIONI EQUIVALENTI**

Due equazioni si dicono **equivalenti** se hanno lo stesso **insieme delle soluzioni**.</font>
{{% /callout %}}

---

<!-- ![zzz](https://res.cloudinary.com/teepublic/image/private/s--TQXt20Pc--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_000000,e_outline:48/co_000000,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1588675429/production/designs/9818088_0.jpg) -->

<br>

### 6. Principi di equivalenza delle equazioni

### $\star$ **primo** principio di equivalenza:

- *afferma che **sommando algebricamente** ad entrambi i membri di una equazione, uno **stesso numero** o una **stessa espressione contenente l'incognita**, otteniamo una equazione **equivalente** a quella data.*

### $\star \star$ **secondo** principio di equivalenza:

- *moltiplicando o dividendo entrambi i membri di una uguaglianza per uno **stesso numero***diverso da zero*, o per una **stessa espressione algebrica**, sempre definita e sempre diversa da zero nel dominio D dell'equazione, si ottiene un'equazione **equivalente** a quella data.*

<br>

> **ESEMPIO:**
> ![ex1_img](../mattoni.png)
> - _Un mattone pesa $1$ kg più mezzo mattone. Quanto pesa un mattone?_
>
> Il calcolo letterale e le equazioni ci permettono di sviluppare dei *procedimenti* in modo simbolico e di pervenire rapidamente alla soluzione.
>
> - Nel nostro caso, indicando con $x$ il peso di un mattone (espresso in kg), la situazione può essere espressa in forma simbolica dall’equazione:
>
> $$x = 1 + \dfrac{1}{2} x$$
>
> - utilizzando in modo opportuno i due *principi di equivalenza* possiamo semplificare l'equazione:
> $$x \textcolor{red}{- \dfrac{1}{2}x} = 1 + \cancel{\dfrac{1}{2} x} \textcolor{red}{- \cancel{\dfrac{1}{2}x}} \rightarrow x-\dfrac{1}{2} x=1 \quad \longrightarrow \quad \dfrac{1}{2} x=1$$
> $$\textcolor{red}{2 \\; \cdot} \dfrac{1}{2} x = \textcolor{red}{2 \\; \cdot} 1$$
> - semplificando otteniamo la soluzione:
> $$\textcolor{darkorange}{x=2}$$

---

### 7. Conseguenze dei principi di equivalenza

<br>

- **Regola del trasporto:** Se entrambi i membri di un'equazione sono polinomi, si può *trasportare* un termine da un membro all'altro, cambiandogli il segno;

- Se entrambi i membri di un’equazione sono polinomi e uno stesso termine compare in entrambi i membri, si può eliminare tale termine da entrambi i membri dell’equazione;

- Se entrambi i membri di un’equazione sono polinomi e i coefficienti dei loro termini sono tutti multipli di uno stesso numero, si possono dividere tutti i coefficienti per tale numero;

- Se in un’equazione intera compaiono frazioni o termini con coefficienti frazionari, è possibile ridurre entrambi i membri allo stesso denominatore e poi eliminare il denominatore comune;

- Si può cambiare il segno di entrambi i membri di un’equazione.
  - Infatti ciò equivale amoltiplicare per1 entrambi i membri dell’equazione.
  - In particolare, se entrambi i membri sono polinomi, si può cambiare il segno di tutti i termini di entrambi i membri.

---

### 8. Grado di un'equazione intera

Consideriamo un’equazione nell’incognita $x$ i cui membri siano espressioni intere, cioè polinomi.
E`sempre possibile, applicando le regole che sono conseguenze dei principi di equivalenza, scriverla nella forma:
$$P(x) = 0$$

dove il primo membro, che abbiamo indicato con $P(x) = 0$, è un polinomio nella variabile $x$ e il secondo membro è zero.

> Tale forma è anche detta <font color="brown">**forma canonica**</font> o <font color="brown">**forma normale**</font> dell’equazione.

{{% callout warning %}}

<font color="brown">**definizione: Grado di un'equazione intera**

Data un’equazione nell’incognita $x$, scritta nella forma canonica $P(x) = 0$, si dice grado dell’equazione il grado del polinomio $P(x)$ rispetto alla lettera $x$.
{{% /callout %}}
</font>

- Le equazioni di primo grado sono anche dette equazioni **lineari**.
- La forma canonica di un’equazione lineare nell’incognita $x$ è: $$mx + q = 0$$
  - dove $m$ e $q$ sono numeri reali, con $m \neq 0$

## Equazioni Numeriche

### 9. Procedimento risolutivo delle equazioni intere

Elenchiamo le operazioni da compiere per risolvere un’equazione numerica intera di primo grado (come al solito, indichiamo con $x$ l’incognita).

1. Si eseguono le eventuali operazioni indicate e, se presenti, si eliminano i denominatori.
2. Si trasportano tutti i monomi contenenti l’incognita al primo membro e tutti itermini noti al secondo membro, riducendo gli eventuali termini simili. 
3. Dopo aver eseguito tali operazioni l’equazione risulterà scritta nella forma

$$ax=b$$

- si possono verificare i seguenti casi:

1. $a \neq 0 \Rightarrow x=\dfrac{b}{a} \qquad \rightarrow$ equazione **determinata** $\Rightarrow S = \dfrac{b}{a}$ 
2. $a = 0$

   - $b=0 \qquad \rightarrow$ equazione **indeterminata** $\Rightarrow S = \mathbb{R}$
   - $b \neq 0 \qquad \rightarrow$ equazione **impossibile** $\Rightarrow S = \emptyset$

{{% callout note %}}

**esempio**:

$$\small{(3 x-1)^{3}+(3 x+1)(6 x-7)=(3 x+1)(3 x-1)^{2}}$$

{{% /callout %}}

### 10. Procedimento risolutivo delle equazioni frazionarie

#### Condizioni di accettabilità

- Poiché le soluzioni di un’equazione devono appartenere al suo dominio, in alternativa al dominio si possono indicare le condizioni a cui devono soddisfare le eventuali soluzioni.
Tali condizioni sono dettecondizioni di accettabilità. Useremo la notazione **C.A.** per indicare le **Condizioni di Accettabilità** delle soluzioni di un’equazione.

- Nel caso di equazioni frazionarie, le condizioni di accettabilità mettono in evidenza che la soluzione non può coincidere con i valori che annullano qualche denominatore al primo o al secondo membro.

#### Le fasi del procedimento risolutivo

Enunciamo ora il procedimento  per  risolvere  un’equazione  numerica  frazionaria.

1. Se è possibile, si scompongono in fattori i denominatori che figurano nell’equazione.
2. Si formulano le condizioni di accettabilità (oppure si esplicita il *dominio* dell’equazione).
3. Si riducono entrambi i membri dell’equazione allo stesso denominatore.
4. Si eliminano i denominatori, moltiplicando entrambi i membri per il denominatore comune.
5. Si risolve l’equazione intera così ottenuta.
6. Delle soluzioni ottenute si accettano solo quelle che soddisfano le condizionidi accettabilità (cioè solo quelle che appartengono al dominio).

- I passaggi indicati nei punti **5.** e **6.** sono giustificati dal secondo principio di equivalenza.

{{% callout note %}}

- **esempio 1**

$$\frac{x+2}{x-1}-\frac{x}{x+2}=\frac{3 x}{x^2+x-2}$$

- **esempio 2**

$$\frac{x+3}{x-3}-\frac{2 x-1}{x^{2}-6 x+9}=\left(\frac{3}{x-3}+1\right)^{2}$$

- **esempio 3**

$$\dfrac{x^2}{x-1} - x = \dfrac{2x-1}{x - 1}$$
{{% /callout %}}

<br>

---

## Problemi di Primo Grado

- In generale, le equazioni consentono di risolvere diverse specie di problemi.

>Le situazioni che si possono presentare sono dei tipi più svariati, perciò non è possibile formulare un metodo generale per la risoluzione di qualsiasi problema.
>Ci limitiamo quindi a fornire alcune indicazioni generali, che illustreremo con alcuni esempi.
>Per risolvere un problema occorre tradurlo in un’equazione che ne rappresenti il **modello matematico**.

- A tal fine, dopo aver analizzato attentamente il problema individuando i dati noti, conviene procedere nel modo seguente.

1. Si **individua l’incognita**, ossia una grandezza il cui valore numerico non è immediatamente deducibile, e si associa a essa una lettera (di solito la $x$) che sarà l’incognita dell’equazione.
2. Si pongono le eventuali **condizioni di accettabilità (C.A.**) della soluzione, ossia si stabiliscono quelle limitazioni al valore dell’incognita che garantiscono la possibilità di dare un significato alle soluzioni che si troveranno.
3. **Si scrive l’equazione**; a questo scopo si cerca di esprimere le relazioni tra lagrandezza rappresentata dall’incognita e le grandezze note mediante un’uguaglianza, che diventerà l’equazione da risolvere. In questa fase a volte è utile ragionare «come se» l’incognita fosse nota.
4. **Si risolve l’equazione** così trovata.
5. **Si confronta la soluzione trovata con le condizioni di accettabilità** poste, inmodo da escludere i valori che potrebbero non avere significato per il problema.
6. **Si formula la soluzione del problema**, tenendo presente che non sempre la risoluzione di un problema termina con la risoluzione di un’equazione.

**L’equazione** è il **modello matematico del problema**: la sua soluzione deve quindi essere interpretata in tale modello.

<br>

{{% callout note %}}
**Esempio 3:**

- Anna vuole acquistare un’auto che costa $13.900$€.
- Se riuscisse a raddoppiare i risparmi che ha adesso, per comprare l’auto dovrebbe comunque trovare altri $3.400$€.
- Quanti risparmi ha ora Anna?

**soluzione**:

- Chiamiamo $x$ l’importo dei risparmi che attualmente possiede Anna;
- Traduco in matematichese il testo:

$$2 \cdot x + 3.400 = 13.900 $$

- *traduzione*: il doppio dei risparmi attuali più $3.400$€ sono pari al totale di $13.900$€ che deve spendere per comprare l’auto;
- isoliamo l'incognita:

$$
\begin{align}
2 \cdot x &= 13.900 - 3.400 \\\\
x &= \dfrac{10.500}{2} \\\\
x &= 5.250
\end{align}$$

{{% /callout %}}

{{% callout note %}}
**Esempio 3:**

- La somma di due numeri è $37$. Dividendo il più grande per il più piccolo si ottiene come quoziente $3$ e come resto $1$.
- Quali sono i due numeri?

- **primo numero**: $= x$
- **secondo numero**: $= 37 - x$

**soluzione**:

- l'equazione risultante è la seguente: 
$$37-x=3x+1$$

{{% /callout %}}

> <font color=brown>
> Quando vi è solo un dato da trovare (o, come si dice, quando c’è solo una “incognita”),
> allora è sufficiente avere a disposizione una sola equazione che mette in relazione fra loro i dati del problema;</font>

---

### un modello molto famoso...

![modelli non matematici](https://i.pinimg.com/originals/8a/e0/e2/8ae0e2d1005f7c6ea9eee5ff5d908dad.jpg)

### Il modello matematico SEIR (SIR) per il monitoraggio pandemico

- $N:$ total population
- $S(t):$ number of people susceptible on day t
- $E(t):$ number of people exposed on day $t$
- $I(t):$ number of people infected on day t
- $\mathrm{R}(\mathrm{t}):$ number of people recovered on day $\mathrm{t}$
- $D(t):$ number of people dead on day $t$
- $\beta:$ expected amount of people an infected person infects per day
- $D:$ number of days an infected person has and can spread the disease
- $\gamma$ : the proportion of infected recovering per day $(\gamma=1 / \mathrm{D})$
- $R_o:$ the total number of people an infected person infects (Ro $=\beta / \gamma$ )
- $\delta:$ length of incubation period
- $a:$ fatality rate
- $\rho:$ rate at which people die $(=1 /$ days from infected until death $)$

![equazioni](https://miro.medium.com/max/2000/1*s7xR9yUz14_8zw7sKBhljQ.png)

![modello SIR](https://miro.medium.com/max/2000/1*YB71iX0vwxzZ82WI_dmqhA.png)

---

## esercizi proposti

### equazioni lineari intere

$$
\begin{aligned}
&\frac{1}{12} x+\frac{5}{8}-\frac{1}{4} x=\frac{3}{2}-\frac{1}{6} x-\frac{7}{8} \\\\
&\frac{x-14}{12}-\frac{2 x-1}{18}=\frac{2}{9}(2 x-5) \\\\
&\frac{4 x+3}{21}-\frac{6 x+11}{14}=\frac{5 x-1}{6} \\\\
&\frac{2 x-3}{10}=\frac{6 x-2}{15}-\frac{1+x}{5} \\\\
&\left(-\frac{1}{3} x+1\right)\left(\frac{3}{5} x-\frac{1}{2}\right)=\frac{1}{5} x\left(\frac{23}{6}-x\right)
\end{aligned}
$$

$$
\begin{aligned}
&\left(2 x^{2}+x\right)^{2}-\left(2 x^{2}-x-3\right)^{2}-(2 x+1)^{3}=2 \\\\
&(3 x-1)^{3}+(3 x+1)(6 x-7)=(3 x+1)(3 x-1)^{2} \\\\
&\left(x^{2}-4 x+1\right)^{2}-\left(x^{2}+7\right)^{2}=(4 x-1)^{2}-(2 x+1)^{3} \\\\
&(3 x+4)(3 x-4)-(3 x+2)^{2}=2(x+5)(2 x-3)-(2 x-3)^{2} \\\\
&(2 x+1)(2 x-1)(2 x+3)-(2 x+1)^{3}=4(2 x+3)-2(2 x-1)
\end{aligned}
$$

---

### equazioni lineari frazionarie

$$
\begin{aligned}
&\frac{1}{x-5}-\frac{2 x+1}{x^{2}-5 x}=\frac{2}{x} \\\\
&\frac{2 x+1}{x^{2}+2 x+1}+\frac{x}{x+1}=1 \\\\
&\frac{3 x-2}{2 x-1}-\frac{1}{8 x^{2}-8 x+2}=\frac{3}{2} \\\\
&\frac{3 x+1}{x^{2}}+\frac{9 x}{9 x^{2}-12 x+4}=\frac{12 x-1}{3 x^{2}-2 x} \\\\
&\frac{x+3}{x-3}-\frac{2 x-1}{x^{2}-6 x+9}=\left(\frac{3}{x-3}+1\right)^{2} \\\\
&\frac{(3 x-4)^{2}}{4 x+8}=\left(4-\frac{x}{x+2}\right)\left(x+2-\frac{x}{4}\right) \\\\
&\left(\frac{x}{x-1}-1\right)\left(\frac{x-1}{x}+1\right)-\frac{x+1}{x-1}+\frac{2 x-1}{x}=1 \\\\
&\frac{x+6}{6 x^{2}+4 x}-\frac{1}{9 x^{2}-4}=\frac{2}{3 x}-\frac{3 x+2}{6 x^{2}-4 x} \\\\
&\frac{x^{2}+2 x-4}{x^{3}-8}+\frac{1}{2}=\frac{x+2}{2 x-4}-\frac{x+2}{x^{2}+2 x+4} \\\\
&\frac{3}{4 x+2}-\frac{3}{4 x^{2}+4 x+1}=\frac{3}{4 x-2}-1
\end{aligned}
$$

# The Math of Things

Sito personale di **Diego Fantinelli**, insegnante di Matematica e Fisica al Liceo Scientifico. Raccoglie articoli divulgativi, materiali per i corsi, lezioni interattive, presentazioni e talk, con un'attenzione particolare al ragionamento passo-passo e al legame tra matematica, fisica e mondo reale.

- **Sito:** <https://mathofthings.netlify.app/>
- **Stack:** Hugo + tema Wowchemy Academic, deploy automatico su Netlify

---

## Cos'è

Un sito statico che funziona come vetrina didattica ed editoriale. L'idea guida è quella suggerita dal titolo: mostrare *la matematica delle cose*, cioè come modelli e concetti matematici emergano da problemi concreti (dalla tangente alla derivata, dall'indice di massa corporea alle probabilità del dilemma di Monty Hall).

Il pubblico di riferimento è duplice:

- **Studenti** del triennio del Liceo Scientifico, per materiali di studio e ripasso.
- **Docenti e curiosi**, per articoli divulgativi e riflessioni sulla didattica.

---

## Sezioni del sito

| Sezione | Percorso | Contenuto |
|---|---|---|
| Home | `/` | Homepage custom (layout dedicato, non widget Wowchemy) |
| Corsi | `/courses/` | Programmazioni didattiche e materiali per lezione |
| Articoli | `/post/` | Blog divulgativo su matematica, fisica e metodo di studio |
| Talks | `/event/` | Seminari, lezioni simulate e interventi pubblici |
| Slides | `/slides/` | Presentazioni Reveal.js integrate nel tema |
| Lezioni interattive | `/lezioni/` | Lezioni HTML+MathJax con versione PDF stampabile |

### Articoli (una selezione)

- Le *derivate*: dal problema della tangente alla definizione formale
- Il concetto di *Modello Matematico*
- La *conservazione* dell'energia
- Il *dilemma* di Monty Hall
- Effetto *Dunning–Kruger* e la *Memoria* umana in Gigabytes
- Il *Metodo* di studio Cornell
- A cosa *serve* la matematica?

> [!NOTE]
> Nei titoli una o due parole possono essere messe in *corsivo colore corallo* usando la sintassi `_parola_` nel campo `title:` del frontmatter. È una convenzione grafica del tema custom.

---

## Stack tecnico

| Componente | Dettaglio |
|---|---|
| Generatore | **Hugo v0.97.3** (eseguibile `~/.local/bin/hugo-0.97.3`) |
| Tema | **Wowchemy / Academic** (pinned v0.97.3) |
| Slides | Reveal.js v4.2.1 (integrato nel tema) |
| Deploy | **Netlify** — build automatica al push su `main` |
| Stile | SCSS in un unico file `assets/scss/custom.scss` |
| Font | Google Fonts via `data/fonts/my-font.toml` |
| Palette | tema `minimal-warm` in `data/themes/minimal-warm.toml` |

> [!WARNING]
> Usare **sempre** `~/.local/bin/hugo-0.97.3`, mai la versione di Homebrew: il tema è compatibile solo con questa release.

---

## Design system

Palette calda con accento corallo, pensata per leggibilità e coerenza tra light e dark mode.

### Colori (`minimal-warm`)

| Token | Light | Dark |
|---|---|---|
| Primario (corallo) | `#ed6f5c` | `#f08e7c` |
| Sfondo | `#f7f1e6` | `#1a1a1a` |
| Sfondo menu | `#ece1cc` | `#2a2a2a` |
| Testo corpo | `#1a1a1a` | `#d0d0d0` |

### Tipografia

| Ruolo | Font |
|---|---|
| Titoli | Playfair Display |
| Corpo | Georgia |
| Navbar / mono | JetBrains Mono |
| Codice | Fira Code |
| Display / impatto | Anton |

Pattern ricorrenti: titoli con `em` corallo, card con bordo sottile e hover in `translateY`, blockquote con barra corallo a sinistra, sfondo a particelle animate (`particles-bg.html`).

---

## Struttura del progetto

Solo i file custom; il resto è fornito dal tema.

```
mathofthings/
├── assets/scss/custom.scss        unico SCSS da modificare
├── data/
│   ├── fonts/my-font.toml         stack font
│   └── themes/minimal-warm.toml   palette colori
├── layouts/
│   ├── index.html                 homepage custom
│   └── partials/                  footer, particelle, JS inline
├── content/
│   ├── courses/                   corsi e programmazioni
│   ├── post/                      articoli del blog
│   ├── event/                     talks e seminari
│   ├── slides/                    presentazioni Reveal.js
│   └── authors/                   profilo autore
├── static/
│   ├── lezioni/                   lezioni interattive HTML + PDF
│   ├── cv/                        CV in PDF
│   └── uploads/                   allegati
└── config/_default/               config.yaml, params.yaml, menus.yaml
```

---

## Sviluppo in locale

```bash
cd /Users/magus_home/Documents/mathofthings
pkill -9 -f hugo; sleep 1
nohup ~/.local/bin/hugo-0.97.3 server -D > /tmp/hugo.log 2>&1 & disown
```

Il sito è raggiungibile su <http://localhost:1313>.

### Generare il PDF di una lezione interattiva

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=static/lezioni/<slug>/<slug>.pdf \
  --virtual-time-budget=15000 --no-sandbox \
  "http://localhost:1313/lezioni/<slug>/?print=1"
```

---

## Deploy

- Push su `main` → **Netlify** avvia automaticamente la build e pubblica il sito.
- Messaggi di commit in italiano per contenuti didattici/editoriali.
- Nessun deploy manuale necessario.

---

## Autore

**Diego Fantinelli** — insegnante di Matematica e Fisica, ITIS "E. Fermi" (Bassano del Grappa).
Interessi: composizione jazz, didattica della matematica, ciclismo.

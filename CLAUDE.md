# mathofthings — CLAUDE.md

Istruzioni specifiche per questo progetto. Integrano il profilo globale in `~/.claude/CLAUDE.md`.

---

## Panoramica

Sito personale di Diego Fantinelli (insegnante di Matematica e Fisica), generato con **Hugo v0.97.3**
e il tema **wowchemy/academic** (pinned `v0.97.3`).
Deploy automatico su **Netlify** dal branch `main` di `github.com/jazzmagus/mathofthings`.

---

## Stack tecnico

| Componente      | Versione / dettaglio                              |
| --------------- | ------------------------------------------------- |
| Hugo            | v0.97.3 — eseguibile: `~/.local/bin/hugo-0.97.3` |
| Tema            | wowchemy/academic v0.97.3                         |
| Slides          | Reveal.js v4.2.1 (integrato nel tema)             |
| Deploy          | Netlify (build su push a `main`)                  |
| CSS             | SCSS → `assets/scss/custom.scss` (unico file)     |
| Font            | Google Fonts via `data/fonts/my-font.toml`        |
| Tema colori     | `data/themes/minimal-warm.toml`                   |

**IMPORTANTE:** usare sempre `~/.local/bin/hugo-0.97.3`, mai `hugo` di Homebrew (versione diversa).
Il server dev va avviato dalla root del progetto (`/Users/magus_home/Documents/mathofthings`).

```bash
# Restart server dev:
cd /Users/magus_home/Documents/mathofthings
pkill -9 -f hugo; sleep 1
nohup ~/.local/bin/hugo-0.97.3 server -D > /tmp/hugo.log 2>&1 & disown
sleep 4
```

---

## Design system

### Colori (tema `minimal-warm`)

| Token                 | Light mode  | Dark mode   |
| --------------------- | ----------- | ----------- |
| `$primary` (coral)    | `#ed6f5c`   | `#f08e7c`   |
| Background            | `#f7f1e6`   | `#1a1a1a`   |
| Menu background       | `#ece1cc`   | `#2a2a2a`   |
| Testo corpo           | `#1a1a1a`   | `#d0d0d0`   |

### Font (`data/fonts/my-font.toml`)

| Ruolo              | Font                  |
| ------------------ | --------------------- |
| Headings           | Playfair Display      |
| Body               | Georgia               |
| Navbar / mono      | JetBrains Mono        |
| Codice             | Fira Code             |
| Display / impact   | Anton                 |

### Pattern CSS ricorrenti

- Titoli con `em` colorato in coral: `em { color: $primary; }`
- Span `.mono` per testo monospaziato inline (accent color)
- Quote block: `border-left: 3px solid $primary`
- Card base: `border: 1px solid rgba(21,20,15,0.1); border-radius: 8-12px`
- Card hover: `border-color: rgba($primary, 0.3); transform: translateY(-2|-4px)`
- Particelle di sfondo: partial `particles-bg.html` (parametri: `id`, `count`, `links`, `circular`, `colorLight`, `colorDark`)

---

## Struttura directory (solo file custom — il resto è del tema)

```
mathofthings/
├── assets/scss/
│   └── custom.scss          ← unico file SCSS da modificare
├── data/
│   ├── fonts/my-font.toml   ← stack font
│   └── themes/minimal-warm.toml  ← palette colori
├── layouts/
│   ├── index.html           ← homepage completamente custom
│   ├── partials/
│   │   ├── site_footer.html ← footer custom (About me, social, avatar zoom)
│   │   ├── particles-bg.html← sfondo particelle animato
│   │   └── custom_js.html   ← JS inline (zoom avatar, ecc.)
│   ├── courses/             ← layout lista corsi
│   ├── event/               ← layout lista talks (usa wowchemy)
│   ├── post/                ← layout lista post (usa wowchemy)
│   ├── lezioni-fisica/      ← pagina statica "Lezioni di Fisica"
│   └── verso-universita/    ← pagina statica "Verso l'Università"
├── content/
│   ├── courses/             ← sezioni corso (math-01…math-05, SE_math-03…)
│   ├── event/               ← voci Talks/Seminari (una cartella per talk)
│   ├── post/                ← articoli del blog
│   ├── slides/              ← presentazioni Reveal.js (una cartella per slide)
│   ├── lezioni-fisica/      ← _index.md pagina fisica
│   ├── verso-universita/    ← _index.md pagina università
│   └── authors/             ← profilo autore
├── static/
│   ├── lezioni/             ← PDF e HTML generati (es. equazioni-1-grado/)
│   ├── cv/                  ← CV in PDF
│   └── uploads/             ← allegati generici
└── config/_default/
    ├── params.yaml          ← font, tema, navbar
    └── menus.yaml           ← voci navbar
```

---

## Content type: `event` (Talks e Seminari)

Le voci della pagina `/event/` vivono in `content/event/<slug>/index.md`.
Schema frontmatter completo:

```yaml
title: 'Titolo del talk'
event: Nome dell'evento
event_url: https://...
location: Nome sede
address:
  street: ...
  city: ...
  region: ...
  postcode: '...'
  country: Italy
summary: Breve descrizione (appare nella card)
abstract: 'Descrizione estesa'
date: '2024-05-01T10:00:00Z'
date_end: '2024-05-01T11:30:00Z'
all_day: false
publishDate: '2024-04-01T00:00:00Z'
authors: [diego fantinelli]
tags: []
featured: false
image:
  caption: ''
  focal_point: Smart   # Smart | Left | Right | Top | Bottom
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: nome-cartella-in-content-slides   # linka /slides/<nome>/
projects: []
```

Miniatura: file `featured.png` o `featured.jpg` nella stessa cartella del talk.

---

## Content type: `slides` (Reveal.js)

Le presentazioni stanno in `content/slides/<nome>/index.md`.
Il frontmatter minimo:

```yaml
---
title: Titolo
summary: Sottotitolo
authors: [Diego Fantinelli]
tags: [tag]
categories: [categoria]
date: "2024-01-01T00:00:00Z"
slides:
  theme: serif   # serif | black | white | league | moon | solarized
---
```

Le slide sono sezioni separate da `---` nel body. Asset (immagini, video, PDF) nella stessa cartella.
URL di preview: `http://localhost:1313/slides/<nome>/`

Per collegare una presentazione a un talk: `slides: <nome>` nel frontmatter del talk.

---

## Talks esistenti (al 2026-06-16)

| Slug cartella                        | Slides collegate | Data       |
| ------------------------------------ | ---------------- | ---------- |
| `Concorso Straordinario Bis 2022`    | `prog_ad`        | 2022-08-25 |
| `lezione-simulata-stem-2022`         | `stem_2022`      | 2022-02-05 |
| `conference-2026`                    | —                | 2026       |
| `funzioni-trascendenti-2025`         | —                | 2025-05-01 |
| `impronta-umana-2025`                | —                | 2025       |
| `violenza-donne-2025`                | —                | 2025       |

---

## Lezioni interattive (PDF/HTML)

Le lezioni interattive vivono in `static/lezioni/<slug>/`.
Struttura tipo:

```
static/lezioni/equazioni-1-grado/
├── index.html      ← lezione interattiva (HTML+CSS+MathJax)
└── equazioni-1-grado.pdf  ← PDF statico generato con Chrome headless
```

Generazione PDF (Chrome headless):
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=static/lezioni/<slug>/<slug>.pdf \
  --virtual-time-budget=15000 --no-sandbox \
  "http://localhost:1313/lezioni/<slug>/?print=1"
```

La lezione aggiunge `?print=1` per attivare il CSS di stampa (`body.print-all` in `index.html`).

---

## Workflow git

- Commit solo su richiesta esplicita.
- Messaggio in italiano quando le modifiche riguardano contenuti didattici/editoriali.
- Formato commit:
  ```
  Breve descrizione in italiano

  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
  ```
- Push su `main` → trigger build Netlify automatico.
- `.DS_Store` è tracciato nel repo (non modificare `.gitignore`).

---

## Titoli con corsivo coral

Il partial `layouts/partials/page_header.html` è stato sovrascritto per usare `.RenderString` al posto di `.Title` grezzo. Questo permette di usare markdown inline nel campo `title:` del frontmatter.

Convenzione: usare `_parola_` per mettere una o due parole in corsivo coral nel titolo. Esempio:

```yaml
title: "Il concetto di _Modello Matematico_"
title: "Costruire un manuale con _l'AI_"
```

Il CSS `.article-container h1 em { color: $primary; font-style: italic; }` fa il resto.
Non esagerare: una o al massimo due parole per titolo.

---

## Convenzioni frontmatter — post (`content/post/`)

Ogni post deve avere nel blocco `image:`:

```yaml
image:
  filename: featured.jpg   # o featured.png
  caption: ''
  focal_point: Center      # Smart | Center | Top | Bottom | Left | Right
  placement: 2             # piena larghezza sopra il titolo (come Modello Matematico)
  preview_only: false
```

`placement: 2` è il default per tutti i nuovi post — non ometterlo.

---

## Convenzioni di stile

- Nessun commento HTML inutile nel codice generato.
- Nessuna emoji, mai.
- Il SCSS usa sempre `$primary`, `$sta-font-heading`, `$sta-font-body`, `$sta-background`, `$sta-dark-background` (variabili wowchemy) — non hardcodare i colori coral se non strettamente necessario.
- Nuovi layout in `layouts/` seguono il pattern `.content-page` + `.page-header-section`.
- Le pagine statiche extra (es. `lezioni-fisica`, `verso-universita`) hanno il layout in `layouts/<slug>/list.html` e il contenuto in `content/<slug>/_index.md`.
- Math inline: `$...$` — display: `$$...$$`.
- **Formule: no `\boxed{}`** — usa `\tag{}` per numerare le formule importanti, ma mai racchiuderle in box. Es: `$$f(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} \tag{D}$$`

---

## Standard — Pagine Corsi (Lezioni con Programmazione)

### Struttura card lezione (`.materials-card.lesson-card`)

Ogni lezione della programmazione didattica segue questo pattern:

```
[Lezione LA0X]
Titolo lezione
Descrizione breve (font piccolo, corsivo, Georgia)
├ Argomento 1: XXh
├ Argomento 2: XXh
├ ...
└─ Totale: XXh
```

### Font e colori

- **Titolo lezione**: Playfair Display, 1.1rem
- **Descrizione breve** (`.lesson-description`): Georgia, 0.85rem, corsivo, #1a1a1a / #d0d0d0
- **Argomenti** (`.content-title`): **JetBrains Mono**, 0.8rem, colore scuro (#1a1a1a / #d0d0d0), NON corallo
- **Ore** (`.content-hours`): JetBrains Mono, 0.85rem, colore corallo `$primary`, peso 600
- **Totale ore**: JetBrains Mono, 0.85rem, colore corallo, allineato a destra

### Link materiali (`.materials-links a`)

- Font: **JetBrains Mono**, 0.85rem, peso 600, colore corallo
- No underline, underline su hover
- Descrizione sotto: Georgia, 0.9rem, colore scuro

### Pulsanti verifica (`.verification-buttons`)

Per verifica e soluzioni: due pulsanti light affiancati, senza descrizione.

```html
<div class="verification-buttons">
  <a href="/path/verifica.pdf" class="btn-verification btn-simulation">Simulazione</a>
  <a href="/path/soluzioni.pdf" class="btn-verification btn-solutions">Soluzioni</a>
</div>
```

Stile: border 1px `rgba($primary, 0.3)`, background `rgba($primary, 0.06)`, padding 0.5rem 1rem, hover: border `rgba($primary, 0.5)`, transform translateY(-1px).

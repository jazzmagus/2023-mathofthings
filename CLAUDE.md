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

## Convenzioni di stile

- Nessun commento HTML inutile nel codice generato.
- Nessuna emoji, mai.
- Il SCSS usa sempre `$primary`, `$sta-font-heading`, `$sta-font-body`, `$sta-background`, `$sta-dark-background` (variabili wowchemy) — non hardcodare i colori coral se non strettamente necessario.
- Nuovi layout in `layouts/` seguono il pattern `.content-page` + `.page-header-section`.
- Le pagine statiche extra (es. `lezioni-fisica`, `verso-universita`) hanno il layout in `layouts/<slug>/list.html` e il contenuto in `content/<slug>/_index.md`.
- Math inline: `$...$` — display: `$$...$$`.

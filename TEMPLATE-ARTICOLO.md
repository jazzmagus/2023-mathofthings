---
title: "TEMPLATE — Articolo interattivo HTML"
author: "Diego Fantinelli"
date: "2026-06-22"
category: "Categoria Articolo"
template: "articolo-html"
slug: "nome-slug"
description: "Breve descrizione dell'articolo (una o due righe)"
keywords: [keyword1, keyword2, keyword3]
---

# Come usare questo template

Questo template è un **boilerplate HTML puro** per articoli scientifici/matematici con:
- ✅ Design minimalista warm (colori: `#faf7f2`, `#C2175B`, Georgia serif)
- ✅ Supporto MathJax per formule (`$...$` e `$$...$$`)
- ✅ Responsive design mobile (650px breakpoint)
- ✅ Header sticky con link home e bottoncino PDF
- ✅ Two-column layout per contenuti estesi

---

## Workflow

### Step 1: Scrivi il contenuto qui in Obsidian

Organizza il tuo articolo in sezioni markdown standard:

```markdown
## Titolo sezione 1

Paragrafo con formule inline: $y = f(x)$ oppure display:

$$f(x) = \int_a^b g(x) dx$$

### Sottosezione

Continua con testo...
```

### Step 2: Copia il template

```bash
cp /static/lezioni/template-articolo/index.html /static/lezioni/nome-articolo/index.html
cp /static/lezioni/template-articolo/ecg.png /static/lezioni/nome-articolo/  # se serve immagine
```

### Step 3: Modifica il contenuto nel file HTML

1. **Header metadata** (righe ~280-295):
   - Cambia `<span class="author">Diego Fantinelli</span>`
   - Cambia `<span class="date">Giugno 2026</span>`
   - Cambia `<span class="category">Categoria</span>`

2. **Titolo principale** (righe ~286):
   ```html
   <h1>Studio di una <span class="accent">Funzione</span> Reale di <span class="accent">Variabile</span> Reale</h1>
   ```
   Usa `<span class="accent">parola</span>` per parole in corsivo coral

3. **Abstract** (righe ~301-303):
   ```html
   <div class="abstract">
     <span class="abstract-title">Abstract</span>
     <p>Il tuo abstract qui...</p>
   </div>
   ```

4. **Contenuto principale** (righe ~306+):
   Sostituisci il contenuto mantenendo la struttura HTML

5. **Formule MathJax**:
   - Inline: `$x^2$` diventa $x^2$
   - Display: `$$E = mc^2$$` diventa $$E = mc^2$$

6. **Frase finale in Jet Brains Mono** (righe ~560):
   ```html
   <p style="margin-top: 60px; padding-top: 40px; border-top: 1px solid #e0e0e0; color: #999; font-size: 12px; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.3px; line-height: 1.5;">
     Il tuo credito / nota finale qui.
   </p>
   ```

---

## Struttura HTML — Sezioni principali

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- MathJax config -->
  <script>
    window.MathJax = { ... }
  </script>
  <script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js"></script>
  
  <!-- CSS: fonts, colors, layout -->
  <style>
    /* Design minimalista warm */
    /* Responsive mobile (@media 640px) */
    /* Two-column layout */
  </style>
</head>

<body>
  <!-- Header sticky: link home + PDF button -->
  <div class="doc-header">
    <a href="/">← home</a>
    <button onclick="window.print()">⬇ PDF</button>
  </div>

  <!-- Main content -->
  <main class="doc">
    <!-- Title section (2 columns) -->
    <!-- Abstract box -->
    <!-- Two-column content -->
    <!-- Final note -->
  </main>
</body>
</html>
```

---

## Colori tema (immutabili)

| Elemento | Colore | Hex |
| --- | --- | --- |
| Background | Warm beige | `#faf7f2` |
| Testo corpo | Scuro | `#2c2c2c` |
| Accent (titoli, corsivi) | Coral | `#C2175B` |
| Bordi | Grigio chiaro | `#e4ddd4` |

---

## Font (immutabili)

- **Titoli (h1, h2)**: Georgia serif
- **Corpo testo**: Georgia serif
- **Etichette / metadata**: JetBrains Mono
- **Links / navigazione**: JetBrains Mono

---

## Checklist prima del push

- [ ] Metadata aggiornato (author, date, category)
- [ ] Titolo principale modificato
- [ ] Abstract compilato
- [ ] Contenuto principale inserito
- [ ] Formule MathJax compilate e testate
- [ ] Frase finale personalizzata
- [ ] Responsive testato su mobile (Safari)
- [ ] Link home funzionante
- [ ] PDF funzionante (print)

---

## File da copiare ogni volta

```
/static/lezioni/template-articolo/
├── index.html      ← template base (copia e personalizza)
├── support.js      ← se hai immagini embedded (opzionale)
└── assets/         ← se hai immagini/PDF (opzionale)
```

---

## Note

- **Niente Cloud Design**: il template è HTML puro, zero dipendenze
- **Autonomo**: non richiede `support.js` a meno che non usi immagini embedded
- **Mobile-first**: responsive di default, testato su iPhone Safari
- **MathJax**: funziona su tutti i browser moderni
- **Lightweight**: ~50KB per articolo (vs 563KB del bundled)

---

**Ultimo aggiornamento**: 2026-06-22
**Basato su**: Studio di Funzione Razionale (lezione matematica)
**Destinazione**: `/static/lezioni/<nome-articolo>/index.html`

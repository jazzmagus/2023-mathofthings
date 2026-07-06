---
title: "Bitcoin: la _belle illusion_ della crittografia"
subtitle: "Come la matematica affascinante nasconde una realtà devastante"
summary: "La crittografia che c'è dietro il Bitcoin è bellissima. Il resto è un casinò progettato per farvi perdere denaro — e il pianeta."
authors:
  - diego fantinelli
tags:
  - bitcoin
  - criptovalute
  - matematica
  - crittografia
  - finanza
categories: [infos]
date: "2026-07-06T00:00:00Z"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: ''
  focal_point: "Center"
  placement: 2
  preview_only: false
projects: []
---

> **Nota sulla lettura.** Se avete studenti che giocherellano con i Bitcoin, leggete questo con loro. Non per proibirlo — per capire davvero cosa stanno facendo.

## Atto 1: La magia della crittografia

Prendiamo la parte vera, quella bella. **SHA-256** è una funzione di hash crittografica che trasforma qualunque input (100 caratteri o 100 gigabyte) in una stringa di 64 caratteri esadecimali. E qui sta il colpo di genio: è **irrevocabile** — non esiste algoritmo al mondo che vi restituisce l'input a partire dall'output.

Una transazione Bitcoin viene firmata digitalmente usando **curva ellittica** (ECDSA). L'idea: hai una chiave privata (il tuo segreto) e una chiave pubblica (quello che condividi). La matematica garantisce che nessuno può firmare con la tua chiave privata senza averla. È crittografia *vera*.

Il **blockchain** è un libro mastro distribuito, replicato su migliaia di nodi. Se qualcuno tenta di cambiare una transazione passata, l'hash di quel blocco cambia, e tutti i blocchi successivi diventano invalidi. È il concetto di **integrità attraverso la trasparenza**.

**Perfetto, no?**

Sì. Puramente dal punto di vista crittografico. Il resto — tutto il resto — è un disastro.

## Atto 2: La doccia fredda

### 1. Volatilità che non ha logica

Guardate il grafico qui sotto. Non è economia, è rumore puro.

<div class="bt-chart">
  <h3 class="bt-chart-title">Volatilità annuale: Bitcoin vs S&P 500 vs Oro</h3>
  <div class="bt-chart-canvas"><canvas id="btChart1"></canvas></div>
  <p class="bt-chart-desc">La volatilità del Bitcoin è 3-5 volte quella del mercato azionario. L'oro (bene rifugio) è 20 volte meno volatile.</p>
</div>

Bitcoin nel 2022 ha perso il 65% in 12 mesi. S&P 500 ha perso il 19%. L'oro ha perso il 2%. Non c'è "fondamentale economico" dietro questa differenza: è emozione, FOMO (Fear of Missing Out), manipolazione.

Se uno dei vostri studenti ha messo 1.000€ nel Bitcoin nel gennaio 2017:

- **2017 (boom):** 1.000€ → ~6 BTC → fine anno: ~24.000€ (utile: +2.300%)
- **2018 (crollo):** ~24.000€ → ~3.600€ (perdita: -85%)
- **2021 (boom di nuovo):** ~3.600€ → ~200.000€ (recuperato, e di più)
- **2022 (crimine collettivo):** ~200.000€ → ~20.000€ (perdita: -90%)
- **Oggi (2025):** ~38.000€ (recuperato un po', ma non tutto)

<div class="bt-chart">
  <h3 class="bt-chart-title">Se avessi investito 1.000€ nel 2017...</h3>
  <div class="bt-chart-canvas"><canvas id="btChart2"></canvas></div>
  <p class="bt-chart-desc">Una timeline reale: da 1.000€ a 24.000€ a 3.600€ a 200.000€ a 20.000€ a 38.000€ oggi. Domanda: quanti mesi di sonno è valso?</p>
</div>

**Domanda:** Quanta energia mentale è costato stare a guardare? Quanti mesi di sonno perso?

### 2. La truffa che la matematica non previene

**FTX, novembre 2022.**

Sam Bankman-Fried (CEO) e Gary Wang (CTO) hanno rubato **8 miliardi di dollari** ai clienti attraverso una Ponzi scheme classica: ogni nuovo investitore pagava i precedenti. La crittografia non ha fermato nulla. La firma digitale non ha fatto nulla. Perché? **Perché la truffa era all'interno del sistema, non fuori.**

Il modello matematico di una Ponzi:

$$N(t) = N_0 \times r^t$$

Se $r \leq 1$ (ogni nuovo ciclo porta meno denaro), il sistema crolla. Quando? **Sempre.** Ma nessuno sa quando.

<div class="bt-chart">
  <h3 class="bt-chart-title">Il modello matematico di una Ponzi scheme</h3>
  <div class="bt-chart-canvas"><canvas id="btChart3"></canvas></div>
  <p class="bt-chart-desc">La formula: N(t) = N₀ × r&#7511;. Se r ≤ 1, il sistema crolla. FTX è crollato in 48 ore. 8 miliardi di dollari evaporati. Zero recuperati.</p>
</div>

FTX è crollata nel giro di **48 ore**. 8 miliardi evaporati. Migliaia di persone — molte giovani — hanno perso risparmi di una vita. Alla fine del processo, Bankman-Fried è stato condannato a **25 anni di carcere**. Ma ai clienti i soldi non sono tornati.

E sapete qual è il bello? **Non è stata l'unica.** Mt. Gox (2014), QuadrigaCX (2019), Celsius (2022)... la lista continua.

### 3. Il 95% delle persone perde denaro

Studi della **ESMA** (Autorità bancaria europea) e della **CFTC** (Commodity Futures Trading Commission) americana sono chiari: **il 90-95% dei trader retail perde denaro**.

Se uno studente vi dice "conosco qualcuno che ha guadagnato", è **survivorship bias** puro. I vincitori urlano, i perdenti tacciono.

<div class="bt-chart">
  <h3 class="bt-chart-title">Distribuzione dei risultati: chi guadagna vs chi perde</h3>
  <div class="bt-chart-canvas"><canvas id="btChart4"></canvas></div>
  <p class="bt-chart-desc">Il 95% dei trader retail perde denaro. Il 5% che guadagna fa il rumore, gli altri tacciono (survivorship bias).</p>
</div>

La matematica sottostante: una distribuzione log-normale con coda sinistra pesante. Tecnicamente parlando, il "valore atteso" di entrare nel mercato crypto è **negativo**.

### 4. Il costo energetico che fa paura

Una singola transazione Bitcoin richiede **~2.500 kWh di energia** (considerate il Proof-of-Work, non la singola transazione isolata, ma il costo totale della rete per confermarla).

Per mettere in prospettiva: **è l'equivalente energetico di una casa che consuma per una settimana**. O di un volo intercontinentale.

<div class="bt-chart">
  <h3 class="bt-chart-title">Costo energetico per transazione: Bitcoin vs Visa vs Apple Pay</h3>
  <div class="bt-chart-canvas"><canvas id="btChart5"></canvas></div>
  <p class="bt-chart-desc">Una transazione Bitcoin consuma l'energia equivalente di una casa per una settimana. Visa: lo 0,0005% di quella energia. La scelta di design conta.</p>
</div>

La rete Bitcoin consuma **~150 TWh all'anno**. È più dell'intero consumo energetico della Svezia.

<div class="bt-chart bt-chart-wide">
  <h3 class="bt-chart-title">Consumo energetico annuale della rete Bitcoin</h3>
  <div class="bt-chart-canvas"><canvas id="btChart6"></canvas></div>
  <p class="bt-chart-desc">~150 TWh/anno = consumo energetico della Svezia. CO₂ emessa: ~60 milioni di tonnellate all'anno. Ogni transazione: ~730 kg di CO₂. Visa: 0,004 kg per transazione.</p>
</div>

E la CO₂? Una transazione Bitcoin emette circa **730 kg di CO₂**. Una transazione Visa: **0,004 kg**.

**Domanda finale:** Vi sembra matematica intelligente, o autolesionismo su scala industriale?

## Atto 3: Perché la gente continua a crederci

**Teoria del prospetto** di Kahneman e Tversky: gli umani temono la perdita il **doppio** della gioia del guadagno. Questo significa che se perdete 1.000€, avete bisogno di guadagnare 2.000€ per sentirvi di nuovo "neutrali".

Il Bitcoin sfrutta questa distorsione psicologica in modo letale:

- Se perdete il 50%, l'unica via per recuperare è... aspettare il prossimo boom.
- Ogni boom alimenta FOMO: "Se non compro ora, perderò il treno."
- Ogni crollo alimenta la speranza: "È il momento di comprare al ribasso."

È un ciclo che non finisce. La matematica della mente umana è più forte della matematica della crittografia.

## La vera lezione

La crittografia che c'è dietro il Bitcoin è bellissima. È scienza reale, ingegneria corretta, matematica elegante.

Ma la crittografia non risponde a queste domande:

- **Come mai il prezzo sale da 100 a 70.000 e torna a 20.000?** (No, non è "volatilità di mercato sano" — è casinò)
- **Perché la rete consuma come un paese intero?** (No, non è "necessario per la sicurezza" — è una scelta di design)
- **Perché il 95% delle persone perde denaro?** (No, non è "incompetenza" — è architettura)

L'unica cosa che la crittografia **fa davvero** è rendervi impossibile **riprendere i vostri soldi una volta che li avete persi**.

Se uno studente vuole giocare ai Bitcoin, va bene. Ma che lo faccia **consapevole**:

1. **Non è un investimento.** È una scommessa a zero-sum con probabilità note a favore dei big player e degli exchange.
2. **Non è libertà finanziaria.** È la massima libertà di perdere denaro senza protezioni.
3. **Non è il futuro della finanza.** È un casinò energivoro.

La matematica è neutrale. Come la usiamo, no.

| Metrica | Valore | Prospettiva |
|---|---|---|
| Volatilità annua Bitcoin (2015-2025) | ~50-80% | S&P 500: ~15% |
| Probabilità di perdere denaro (trader retail) | 90-95% | Quasi certa |
| Transazioni Bitcoin perse a truffe (annuali) | ~$14 miliardi | 2023 |
| Consumo energetico Bitcoin (TWh/anno) | ~150 | Equivalente: Svezia |
| CO₂ per transazione Bitcoin | ~730 kg | Visa: 0,004 kg |
| Clienti FTX che hanno recuperato i soldi | ~$0 miliardi | Su 8 miliardi persi |

---

*Fonti: ESMA — "Leverage and Margin Lending Study" (2023); CFTC — "Retail Trader Losses in Commodity Futures Markets" (2022); Digiconomist — Bitcoin Energy Consumption Index; Bankman-Fried prosecution documents (U.S. District Court, SDNY, 2023); Kahneman, Tversky — "Prospect Theory: An Analysis of Decision under Risk" (1979); IEA — "Electricity 2024".*

> Questo articolo contiene calcoli verificabili e dati pubblici. Se qualcuno vi discute con "ma il Bitcoin salirà", ricordate: non è un'argomentazione. È speranza. La speranza non è strategia finanziaria.

**Per i vostri studenti:** Se state già dentro ai Bitcoin, non vi sto dicendo di uscire (anche se sì, dovreste). Vi sto dicendo di aprire gli occhi su quello che state facendo. Se state pensando di entrarci, chiedetevi perché — e ascoltate la risposta con onestà.

<style>
.bt-chart {
  background: #fbf6ec;
  border: 1px solid rgba(21,20,15,0.1);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 2rem 0;
  box-shadow: 0 4px 20px rgba(21,20,15,0.06);
}
.dark .bt-chart {
  background: #242424;
  border-color: rgba(255,255,255,0.08);
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.bt-chart-title {
  font-size: 1.15rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid #ed6f5c;
}
.dark .bt-chart-title {
  color: #d0d0d0;
  border-bottom-color: #f08e7c;
}
.bt-chart-canvas {
  position: relative;
  height: 340px;
}
.bt-chart-desc {
  font-size: 0.9rem;
  color: #6b6459;
  line-height: 1.6;
  font-style: italic;
  margin: 1rem 0 0 0;
}
.dark .bt-chart-desc { color: #a8a29a; }
@media (max-width: 768px) {
  .bt-chart-canvas { height: 280px; }
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
(function () {
  var instances = [];

  function isDark() { return document.body.classList.contains('dark'); }

  function theme() {
    var dark = isDark();
    return {
      // Palette coerente col design del sito (warm / coral)
      bitcoin: dark ? '#f08e7c' : '#ed6f5c',   // coral primario
      sage:    dark ? '#8db38a' : '#6f9e74',   // verde salvia (positivo / sostenibile)
      ochre:   dark ? '#e0b45a' : '#d9a441',   // ocra calda (oro)
      loss:    dark ? '#c85a42' : '#a83f2b',   // terracotta (perdita / Ponzi)
      taupe:   dark ? '#c39a72' : '#a17a52',   // taupe caldo (neutro)
      slate:   dark ? '#93a1b3' : '#7a8ba3',   // grigio-azzurro tenue (comparazioni)
      text:    dark ? '#b8b2a8' : '#6b6459',
      grid:    dark ? 'rgba(255,255,255,0.08)' : 'rgba(21,20,15,0.08)',
      cardBg:  dark ? '#242424' : '#fbf6ec',
      fill:    dark ? 'rgba(240,142,124,0.12)' : 'rgba(237,111,92,0.1)',
      lossFill:dark ? 'rgba(200,90,66,0.12)' : 'rgba(168,63,43,0.1)'
    };
  }

  function build() {
    instances.forEach(function (c) { c.destroy(); });
    instances = [];
    var t = theme();
    var baseOpts = {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { labels: { color: t.text, font: { size: 12 } } } }
    };
    function scale(extra) {
      return Object.assign({ ticks: { color: t.text }, grid: { color: t.grid } }, extra || {});
    }

    instances.push(new Chart(document.getElementById('btChart1'), {
      type: 'bar',
      data: {
        labels: ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024'],
        datasets: [
          { label: 'Bitcoin', data: [74,45,120,73,56,78,65,64,98,53], backgroundColor: t.bitcoin, borderRadius: 6 },
          { label: 'S&P 500', data: [15,8,19,18,14,16,12,19,16,18], backgroundColor: t.sage, borderRadius: 6 },
          { label: 'Oro', data: [6,2,4,5,3,3,2,4,3,2], backgroundColor: t.ochre, borderRadius: 6 }
        ]
      },
      options: Object.assign({}, baseOpts, {
        scales: {
          y: Object.assign(scale(), { title: { display: true, text: 'Volatilità (%)', color: t.text } }),
          x: { ticks: { color: t.text }, grid: { display: false } }
        }
      })
    }));

    instances.push(new Chart(document.getElementById('btChart2'), {
      type: 'line',
      data: {
        labels: ['Gen 2017','Dic 2017','Dic 2018','Dic 2019','Dic 2020','Dic 2021','Dic 2022','Dic 2023','Lug 2025'],
        datasets: [{
          label: "Valore dell'investimento (€)",
          data: [1000,24000,3600,8500,35000,200000,20000,42000,38000],
          borderColor: t.bitcoin, backgroundColor: t.fill,
          borderWidth: 3, fill: true, tension: 0.4, pointRadius: 6,
          pointBackgroundColor: t.bitcoin, pointBorderColor: t.cardBg, pointBorderWidth: 2
        }]
      },
      options: Object.assign({}, baseOpts, {
        scales: {
          y: scale({ ticks: { color: t.text, callback: function (v) { return '€' + v.toLocaleString(); } } }),
          x: { ticks: { color: t.text }, grid: { display: false } }
        }
      })
    }));

    var ponziData = [], ponziTime = [];
    for (var i = 0; i <= 50; i++) { ponziTime.push('Mese ' + i); ponziData.push(1000 * Math.pow(1.15, i) * Math.exp(-i / 20)); }
    instances.push(new Chart(document.getElementById('btChart3'), {
      type: 'line',
      data: { labels: ponziTime, datasets: [{
        label: 'Valore totale del fondo (Ponzi)', data: ponziData,
        borderColor: t.loss, backgroundColor: t.lossFill,
        borderWidth: 3, fill: true, tension: 0.4, pointRadius: 2, pointBackgroundColor: t.loss
      }]},
      options: Object.assign({}, baseOpts, {
        scales: {
          y: scale(),
          x: { ticks: { color: t.text, maxTicksLimit: 5 }, grid: { display: false } }
        }
      })
    }));

    instances.push(new Chart(document.getElementById('btChart4'), {
      type: 'doughnut',
      data: { labels: ['Perde denaro','Guadagna denaro'], datasets: [{
        data: [95,5], backgroundColor: [t.loss, t.sage], borderColor: t.cardBg, borderWidth: 3
      }]},
      options: Object.assign({}, baseOpts, {
        plugins: { legend: { labels: { color: t.text, font: { size: 12 }, padding: 20 } } }
      })
    }));

    instances.push(new Chart(document.getElementById('btChart5'), {
      type: 'bar',
      data: { labels: ['Bitcoin','Visa','Apple Pay','Bancomat'], datasets: [{
        label: 'kWh per transazione', data: [2500,0.002,0.001,0.0015],
        backgroundColor: [t.bitcoin, t.sage, t.ochre, t.slate], borderRadius: 6
      }]},
      options: Object.assign({}, baseOpts, {
        indexAxis: 'y',
        scales: {
          x: scale({ type: 'logarithmic' }),
          y: { ticks: { color: t.text }, grid: { display: false } }
        }
      })
    }));

    instances.push(new Chart(document.getElementById('btChart6'), {
      type: 'bar',
      data: { labels: ['Bitcoin','Svezia','Italia','Egitto'], datasets: [{
        label: 'TWh/anno', data: [150,147,220,190],
        backgroundColor: [t.bitcoin, t.slate, t.sage, t.ochre], borderRadius: 6
      }]},
      options: Object.assign({}, baseOpts, {
        scales: {
          y: scale(),
          x: { ticks: { color: t.text }, grid: { display: false } }
        }
      })
    }));
  }

  function start() {
    if (typeof Chart === 'undefined') { setTimeout(start, 100); return; }
    if (window.__btChartsDrawn) return;
    window.__btChartsDrawn = true;
    build();
    // Ridisegna al cambio tema (light/dark)
    var pending;
    new MutationObserver(function () {
      clearTimeout(pending);
      pending = setTimeout(build, 60);
    }).observe(document.body, { attributes: true, attributeFilter: ['class'] });
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', start); }
  else { start(); }
})();
</script>

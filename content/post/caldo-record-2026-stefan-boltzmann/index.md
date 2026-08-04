---
title: "L'estate 2026 e la _quarta potenza_ che spiega tutto"
subtitle: "Perché il pianeta non si scalda in modo lineare, e cosa c'entra Stefan-Boltzmann"
summary: "I dati Copernicus sull'estate 2026 raccontano un pianeta che si scalda sempre più in fretta. La legge di Stefan-Boltzmann spiega perché l'irraggiamento non è mai una questione lineare."
authors: [diego fantinelli]
tags: [fisica, termodinamica, irraggiamento, clima, divulgazione]
categories: [physics]
date: "2026-08-03T07:00:00Z"
publishDate: "2026-08-03T07:00:00Z"
featured: false
draft: false
image:
  filename: featured.jpg
  caption: ''
  focal_point: Center
  placement: 2
  preview_only: false
---

### Un giugno che ha riscritto i registri

Secondo il bollettino del Copernicus Climate Change Service (C3S), il servizio europeo che monitora il clima globale attraverso satelliti e stazioni a terra, giugno 2026 è stato il secondo giugno più caldo mai registrato a livello globale, con una temperatura media dell'aria in superficie di 16,54 °C — 0,56 °C sopra la media 1991-2020 e 1,39 °C sopra il livello preindustriale (1850-1900). Per l'Europa occidentale è stato invece il giugno più caldo di sempre in assoluto: 20,74 °C di media, 3,05 °C sopra la norma, con punte di anomalia fino a +9 °C in Francia e Germania, e un bilancio umano stimato in oltre 14.000 morti in più nel continente secondo le prime analisi diffuse a luglio.

Ma il dato che mi ha colpito di più, leggendo il bollettino, è un altro: la temperatura superficiale degli oceani, tra i 60° Sud e i 60° Nord, ha raggiunto i 20,86 °C, il valore più alto mai misurato per un mese di giugno, superando i record già altissimi del 2023 e del 2024. Non è la prima estate calda della storia recente. È l'ennesima che batte le precedenti — e qui la matematica ha qualcosa da dire su *perché* la faccenda tende ad accelerare, invece di procedere con calma.

### Il pianeta non è un termosifone

L'intuizione comune sul riscaldamento è quella di un corpo che assorbe calore e si scalda "in proporzione": il doppio dell'energia in ingresso, il doppio dell'aumento di temperatura. Se fosse davvero così, la faccenda sarebbe lineare, prevedibile, quasi rassicurante. Non è così, e il motivo è una legge di fisica che si studia nell'ultimo anno di liceo insieme all'elettromagnetismo: la **legge di Stefan-Boltzmann**.

Ogni corpo con una temperatura sopra lo zero assoluto emette energia sotto forma di radiazione elettromagnetica — è il fenomeno dell'irraggiamento, lo stesso per cui un tizzone ardente brilla di rosso e il Sole di bianco-giallo. La potenza irradiata per unità di superficie non cresce in proporzione alla temperatura, ma alla sua **quarta potenza**:

$$P = \sigma \, A \, T^4 \tag{SB}$$

dove $T$ è la temperatura assoluta (in kelvin), $A$ la superficie del corpo, e $\sigma$ è la costante di Stefan-Boltzmann, $\sigma \approx 5{,}67 \times 10^{-8} \; \text{W}/(\text{m}^2 \text{K}^4)$.

### Perché la quarta potenza cambia tutto

Una potenza quarta ha un comportamento che l'intuizione fatica ad afferrare. Se la temperatura assoluta di un corpo raddoppia, l'energia che irradia non raddoppia: diventa $2^4 = 16$ volte maggiore. Un aumento apparentemente piccolo di temperatura corrisponde a una variazione enorme di energia scambiata.

<div class="sb-chart">
  <h3 class="sb-chart-title">Potenza irradiata al variare della temperatura assoluta</h3>
  <div class="sb-chart-canvas"><canvas id="sbChart1"></canvas></div>
  <p class="sb-chart-desc">Confronto tra una crescita lineare (dashed) e la crescita reale $P \propto T^4$ (curva), entrambe normalizzate a 1 per $T/T_0=1$. Raddoppiando la temperatura assoluta, la potenza irradiata non raddoppia: diventa 16 volte maggiore.</p>
</div>

Questo vale anche al contrario, ed è il punto cruciale per il clima: la Terra si mantiene in equilibrio termico quando l'energia solare assorbita è pari all'energia che il pianeta re-irradia verso lo spazio, secondo esattamente questa legge. Se qualcosa — come l'aumento dei gas serra in atmosfera — riduce anche di poco l'efficienza con cui il pianeta riesce a re-irradiare calore, il sistema non si riequilibra con un piccolo aggiustamento lineare. Serve una variazione di temperatura sproporzionatamente più significativa perché l'equazione torni a bilanciarsi, perché è $T^4$ a dover compensare, non $T$.

È la stessa ragione per cui, guardando i dati Copernicus di anno in anno, i record non si susseguono a intervalli regolari e con incrementi costanti: un sistema retto da una legge di potenza quarta non risponde in modo lineare alle piccole spinte che riceve, e può restare apparentemente stabile per un tratto, per poi mostrare salti che sembrano bruschi ma sono la conseguenza matematica, coerente, di uno squilibrio che si accumula.

<div class="sb-chart">
  <h3 class="sb-chart-title">Le anomalie di giugno 2026, tradotte in energia irradiata</h3>
  <div class="sb-chart-canvas"><canvas id="sbChart2"></canvas></div>
  <p class="sb-chart-desc">Applicando $P \propto T^4$ con $T_0 = 288\,\text{K}$ (temperatura media terrestre), le anomalie di giugno 2026 riportate da Copernicus corrispondono a questi aumenti percentuali nella potenza che un corpo alla nuova temperatura irradierebbe. Piccoli gradi di anomalia pesano più di quanto l'intuizione lineare suggerisca.</p>
</div>

### Un modello, non una spiegazione completa

Va detto con onestà, come sempre quando la fisica di base incontra un sistema complesso come il clima terrestre: la Terra non è un corpo nero ideale, e il bilancio radiativo reale coinvolge l'atmosfera, gli oceani, le nubi, i ghiacci, in un sistema di retroazioni che nessuna singola equazione riassume per intero. La legge di Stefan-Boltzmann non "spiega il clima" da sola. Ma è il mattone fisico di base — lo stesso che si usa per stimare la temperatura di una stella dal suo colore — su cui si costruisce ogni modello più sofisticato di bilancio energetico planetario. E aiuta a capire una cosa semplice ma spesso fraintesa nel dibattito pubblico: un pianeta che si scalda "poco" secondo l'intuizione lineare può star accumulando uno squilibrio energetico enorme, perché il termometro dell'universo, letteralmente, lavora a potenza quarta.

Sources:
- [Copernicus Climate Change Service — Bollettino climatico giugno 2026](https://climate.copernicus.eu/)
- [Copernicus: giugno 2026 il più caldo mai registrato per l'Europa occidentale — Sanità Informazione](https://www.sanitainformazione.it/caldo-record-copernicus-giugno-2026-riscrive-la-storia-del-clima/)
- [Giugno 2026, mese più caldo di sempre per l'Europa — Geopop](https://www.geopop.it/giugno-2026-e-stato-il-mese-piu-caldo-di-sempre-per-leuropa-e-il-secondo-nel-mondo-dati-copernicus/)
- [Caldo record, 14 mila morti in più in Europa — Vatican News](https://www.vaticannews.va/it/mondo/news/2026-07/caldo-europa-vittime-fragili.html)

---

<p style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:300;line-height:1.3;color:#8a827a;">Questo articolo è stato scritto con l'indispensabile contributo di Claude <svg viewBox="0 0 24 24" fill="currentColor" width="17" height="17" style="display:inline-block;vertical-align:-3px;margin:0 2px;color:#ed6f5c;"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2.5C16 2.5 19 6 19 11C19 16 16.5 21 12 21C7.5 21 5 16 5 11C5 6 8 2.5 12 2.5ZM8.7 6.6C10.4 6.6 11.6 8.2 11.6 10.2C11.6 12.2 10.4 13.4 8.7 13.4C7 13.4 6 12 6 10.2C6 8.2 7 6.6 8.7 6.6ZM15.3 6.6C17 6.6 18 8.2 18 10.2C18 12 17 13.4 15.3 13.4C13.6 13.4 12.4 12.2 12.4 10.2C12.4 8.2 13.6 6.6 15.3 6.6Z"/></svg> — la quale, va detto, non ha chiesto nulla in cambio. Per ora.</p>

<style>
.sb-chart {
  background: #fbf6ec;
  border: 1px solid rgba(21,20,15,0.1);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 2rem 0;
  box-shadow: 0 4px 20px rgba(21,20,15,0.06);
}
.dark .sb-chart {
  background: #242424;
  border-color: rgba(255,255,255,0.08);
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.sb-chart-title {
  font-size: 1.15rem;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0 0 1rem 0;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid #ed6f5c;
}
.dark .sb-chart-title {
  color: #d0d0d0;
  border-bottom-color: #f08e7c;
}
.sb-chart-canvas {
  position: relative;
  height: 320px;
}
.sb-chart-desc {
  font-size: 0.9rem;
  color: #6b6459;
  line-height: 1.6;
  font-style: italic;
  margin: 1rem 0 0 0;
}
.dark .sb-chart-desc { color: #a8a29a; }
@media (max-width: 768px) {
  .sb-chart-canvas { height: 260px; }
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
      coral:  dark ? '#f08e7c' : '#ed6f5c',
      sage:   dark ? '#8db38a' : '#6f9e74',
      ochre:  dark ? '#e0b45a' : '#d9a441',
      slate:  dark ? '#93a1b3' : '#7a8ba3',
      text:   dark ? '#b8b2a8' : '#6b6459',
      grid:   dark ? 'rgba(255,255,255,0.08)' : 'rgba(21,20,15,0.08)',
      cardBg: dark ? '#242424' : '#fbf6ec',
      fill:   dark ? 'rgba(240,142,124,0.15)' : 'rgba(237,111,92,0.12)'
    };
  }

  function build() {
    instances.forEach(function (c) { c.destroy(); });
    instances = [];
    var t = theme();
    var baseOpts = {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } }
    };
    function scale(extra) {
      return Object.assign({ ticks: { color: t.text }, grid: { color: t.grid } }, extra || {});
    }

    // 1 — Crescita T^4 vs crescita lineare, normalizzate a T/T0 = 1..2
    var ratios = [];
    var quartic = [];
    var linear = [];
    for (var i = 0; i <= 10; i++) {
      var r = 1 + i * 0.1;
      ratios.push(r.toFixed(1));
      quartic.push(Math.pow(r, 4));
      linear.push(r);
    }
    instances.push(new Chart(document.getElementById('sbChart1'), {
      type: 'line',
      data: {
        labels: ratios,
        datasets: [
          {
            label: 'P ∝ T⁴',
            data: quartic,
            borderColor: t.coral,
            backgroundColor: t.fill,
            borderWidth: 3, fill: true, tension: 0.25,
            pointRadius: 0
          },
          {
            label: 'crescita lineare',
            data: linear,
            borderColor: t.slate,
            borderDash: [6, 4],
            borderWidth: 2, fill: false, tension: 0,
            pointRadius: 0
          }
        ]
      },
      options: Object.assign({}, baseOpts, {
        plugins: { legend: { display: true, position: 'top', labels: { color: t.text } } },
        scales: {
          y: Object.assign(scale({ beginAtZero: true, max: 16 }), {
            title: { display: true, text: 'Potenza relativa (P/P₀)', color: t.text }
          }),
          x: Object.assign(scale(), {
            title: { display: true, text: 'Temperatura relativa (T/T₀)', color: t.text }
          })
        }
      })
    }));

    // 2 — Anomalie giugno 2026 tradotte in % di potenza irradiata in più (T0 = 288 K)
    instances.push(new Chart(document.getElementById('sbChart2'), {
      type: 'bar',
      data: {
        labels: ['vs media 1991-2020\n(+0,56°C)', 'vs preindustriale\n(+1,39°C)', 'anomalia Europa occ.\n(+3,05°C)'],
        datasets: [{
          data: [0.78, 1.94, 4.30],
          backgroundColor: [t.ochre, t.slate, t.coral],
          borderRadius: 6
        }]
      },
      options: Object.assign({}, baseOpts, {
        scales: {
          y: Object.assign(scale({ beginAtZero: true, max: 5 }), {
            ticks: { color: t.text, callback: function (v) { return v + '%'; } },
            title: { display: true, text: 'Energia irradiata in più', color: t.text }
          }),
          x: { ticks: { color: t.text }, grid: { display: false } }
        }
      })
    }));
  }

  function start() {
    if (typeof Chart === 'undefined') { setTimeout(start, 100); return; }
    if (window.__sbChartsDrawn) return;
    window.__sbChartsDrawn = true;
    build();
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

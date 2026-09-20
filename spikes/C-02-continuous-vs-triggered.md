# Spike C-02 — Continuous vs State-Triggered Transition

**Stato:** `aperto`
**Data:** 2026-09-20
**Predecessore:** `C-CONDITION-01` (verdetto: forma di `C` già coperta; nucleo
ipotetico = semantica forward-looking)
**Origine:** revisione avversariale esterna — la domanda più difficile emersa.

## Domanda

> Esistono evidenze sperimentali che le transizioni intra-gesto nel movimento
> umano richiedano un meccanismo di **switching discreto**, oppure possono
> essere spiegate da **controllo continuo con feedback**?

Formulazione rigorosa: quando osserviamo un cambiamento qualitativo nella
coordinazione durante un gesto, esiste evidenza che sia generato da una
condizione di switching discreta, oppure è spiegabile da un controllo
continuo dello stato?

## Modelli da confrontare

| Modello | Meccanismo | Fonte concettuale |
|---|---|---|
| **Continuous** | controllo continuo dello stato; le "fasi" emergono | OFC (Todorov & Jordan 2002); intermittency da feedback con ritardi |
| **Switching** | guardia/frontiera → cambio di politica | automata ibridi; guard conditions |
| **Hybrid** | controllo continuo + eventi di switching | sistemi ibridi |
| **Hierarchical** | option A → condizione → option B | options framework (Sutton et al. 1999) |

**Problema di identificabilità:** dalla sola cinematica i quattro modelli
possono produrre traiettorie indistinguibili. Serve evidenza che vada oltre
il "quando parte B".

## Regola dello spike

> **Non assumere che una decomposizione analitica del movimento dimostri
> un'architettura discreta del controllo motorio.**

Precedenti che rendono la regola necessaria:

- submovements nel reaching: decomposizione analitica, non prova di
  rappresentazione discreta nel sistema nervoso;
- movement intermittency: discreto apparente da feedback continuo + ritardi.

## Cosa cercherebbe il test empirico

Non "quando parte B", ma se esiste una **frontiera predittiva**:

```
s₁ → B inizia a t₁
s₂ → B inizia a t₂
s₃ → B inizia a t₃
...
```

- Se la posizione/tempo della transizione è predetta da variabili di stato
  *prima* che B inizi, e le esecuzioni si separano lungo una frontiera → `C`
  acquista contenuto empirico.
- Se il tempo di transizione è una funzione continua dello stato senza
  separazione → la guardia è una discretizzazione descrittiva di un controllo
  continuo.

## Domande operative per lo spike

1. Quali variabili osservate distinguono i modelli? (perturbazioni, variabilità
   trial-by-trial, correlazioni stato→timing della transizione)
2. Quale spazio conta: articolare / configurazioni / **variabili di task**
   (ipotesi UCM — `C` come frontiera nello spazio delle variabili rilevanti)?
3. Che scala temporale serve? (17 fps ≈ 59 ms probabilmente insufficiente per
   distinguere i modelli → dichiararlo, non interpolare)
4. Quali perturbazioni sperimentali segnano la differenza?
5. Cosa resta **non identificabile** anche con dati migliori?

## Conseguenza per l'editor

L'editor non deve dimostrare "come il cervello controlla il pugno", ma
rappresentare **ipotesi concorrenti sugli stessi dati OSS**:

```
             STESSI DATI OSS
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  modello continuo    modello a
                      transizioni
        │                   │
        └─────────┬─────────┘
                  ▼
            PREDIZIONI
                  ▼
               MISURA
                  ▼
             CONFRONTO
```

Lo schema deve quindi permettere più di un'interpretazione IPO sullo stesso
sottoinsieme di osservazioni, ciascuna con le proprie predizioni.

## Output richiesto

- [ ] rassegna dell'evidenza sperimentale (perturbation studies, trial
  variability, sequencing/chunking vs continuous control);
- [ ] tabella "quale osservazione distingue quale modello";
- [ ] valutazione: cosa è osservabile con i dati che abbiamo (17 fps, 5 rep)
  e cosa richiede cattura diversa;
- [ ] verdetto: `C` come livello descrittivo utile sempre / come meccanismo
  solo se X.

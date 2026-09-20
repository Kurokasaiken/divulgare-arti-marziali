# 06 — Lo strumento visuale ("Motion Mechanics Lab")

> Nome provvisorio. Se mai lo teniamo, è il nome del **tool**, non del progetto.

## Perché serve

Serve poter dire a una persona — o a un'AI — esattamente:

> "Il gomito parte qui, arriva qui, segue questa traiettoria; la supinazione
> inizia qui; la mano resta aperta fino a questo punto; poi si chiude; questo
> vettore deve essere coerente con quest'altro; qui compare il vincolo."

È una **lavagna biomeccanica interattiva**: rende esplicito il modello, non
interpreta il movimento.

## Cosa deve rappresentare

- punti, segmenti, articolazioni (scheletro semplificato);
- archi e traiettorie funzionali (es. arco del gomito);
- vettori e direzioni (es. V₁ gomito ≈ V₂ pugno);
- rotazioni;
- intervalli temporali ed eventi (supinazione, chiusura mano, LOCK);
- configurazioni e vincoli;
- keyframe e transizioni;
- viste diverse (frontale, laterale, zenitale...).

Esempio del linguaggio visuale cercato:

```
GUARD                  LOCK
  ● spalla               gomito ●
   \                      ╲
    ● gomito    →          ╲──────●
     \                       arco
      ● mano

SUPINAZIONE      |────────────|
CHIUSURA MANO           |────|
VECTOR GOMITO    ←────────
VECTOR PUGNO     ←────────
```

## Stack minimo pensato

scheletro semplificato + SVG + keyframe + timeline + vettori + archi +
annotazioni + viste. Nient'altro per la prima versione.

## Cosa NON è

- Non è il progetto: è subordinato alla ricerca.
- Non è motion capture, né avatar realistico, né animazione.
- Non è un'AI che interpreta automaticamente la tecnica.
- Non è una simulazione fisica completa.
- Non deve crescere oltre il necessario: se una feature non serve a rendere
  esplicito il modello, non entra.

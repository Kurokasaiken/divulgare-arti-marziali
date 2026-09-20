# 06 — Lo strumento visuale ("Motion Mechanics Lab")

> Nome provvisorio. Se mai lo teniamo, è il nome del **tool**, non del progetto.

## Perché serve

Serve poter dire a una persona — o a un'AI — esattamente:

> "Il gomito parte qui, arriva qui, segue questa traiettoria; la supinazione
> inizia qui; la mano resta aperta fino a questo punto; poi si chiude; questo
> vettore deve essere coerente con quest'altro; qui compare il vincolo."

È una **lavagna biomeccanica interattiva**: rende esplicito il modello, non
interpreta il movimento.

Il dato canonico (JSON) è l'unica fonte; la UI è una delle sue viste:

```
              CANONICAL DATA
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
    HUMAN VIEW             AI VIEW
     (diagramma)        (JSON/grafo)
        │                     │
        └──────────┬──────────┘
                   ▼
              SAME MODEL
```

L'"AI view" non è solo descrizione: il modello porta con sé intenzione,
evidenza, incertezza e **predizione** — così chi lo legge (umano o AI) può
contestarlo, non solo rappresentarlo.

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

## Prototipo v0 — `tools/biomech-editor.html`

Esiste già un primo prototipo: [`tools/biomech-editor.html`](../tools/biomech-editor.html)
(file HTML singolo, zero dipendenze, prodotto da Claude e importato il
2026-09-20). Si apre direttamente nel browser.

Cosa fa già:

- catena **spalla → gomito → polso → mano** con proporzioni umane fisse
  (100 : 90 : 50);
- **keyframe di posa** su timeline: giunti trascinabili, keyframe spostabili nel
  tempo, doppio clic per aggiungerne;
- **rotazioni assiali** come annotazioni sulla timeline (barra viola con
  inizio/fine modificabili) — es. SUPINAZIONE 120→360 ms; scelta deliberata:
  un overlay 2D non mostra la rotazione assiale reale, quindi è annotazione
  indipendente dalla posa;
- riproduzione della sequenza (Play);
- traiettorie dei giunti come tratteggio;
- export/import **JSON canonico** (schemaVersion 2): il documento esportato è il
  modello, non un dump della UI — contiene `task`, `skeleton` (segmenti e
  lunghezze), `keyframes` con ID stabili (`KF1…`) ed `epistemic`, `events`
  (rotazioni → `E1…` tipo `axial_rotation`), e contenitori vuoti pronti per le
  slice successive (`states`, `movements`, `conditions`, `transitions`,
  `constraints`, `vectors`, `annotations`, `sources`). Import accetta anche il
  formato legacy (`{keyframes, rotations}` / `{keyframes, annotations}`) e lo
  migra. Round-trip verificato: export → import → export identico (epsilon
  float sulle posizioni ricalcolate);
- salvataggio locale (localStorage) nello stesso formato canonico;
- tema chiaro/scuro.

Cosa manca rispetto al modello (gap noti, non richieste approvate):

- vettori espliciti tra configurazioni (V₁ gomito ≈ V₂ pugno);
- condizioni sufficienti / marker di transizione come oggetti propri;
- LOCK/vincoli funzionali come eventi;
- viste multiple e segmenti oltre l'arto superiore (bacino, gambe);
- editing delle etichette OSS/INT/IPO (presenti nello schema, non ancora
  editabili in UI).

## Cosa NON è

- Non è il progetto: è subordinato alla ricerca.
- Non è motion capture, né avatar realistico, né animazione.
- Non è un'AI che interpreta automaticamente la tecnica.
- Non è una simulazione fisica completa.
- Non deve crescere oltre il necessario: se una feature non serve a rendere
  esplicito il modello, non entra.

# Desiderata — Divulgare Arti Marziali

Formato: ogni versione ha `Status` (DRAFT/FROZEN), `Date`, `Authorized by`,
`Reason`, e la formulazione approvata. Una FROZEN non si modifica: una nuova
versione si appende sotto.

---

## v1

**Status:** FROZEN
**Date:** 2026-09-20
**Authorized by:** Fausto
**Reason:** approvazione esplicita in sessione — Director ha riproposto la
candidata v3 verbatim e ordinato "passa al protocollo multi AI web per questo
plan".

**Intento del Director:**
Tool che indichi precisamente le cose e che possa dare informazioni precise a
un agente AI per poterne discutere, per studiare la teoria biomeccanica.
Multi-angolazioni interessanti. Corpo intero fase per fase, partendo dal
progetto mocap esistente (camera-fighter). UI divulgativa secondaria —
potrebbe essere un altro tool, ci pensiamo dopo.

*User-stated:*
"Intanto per studiare la teoria biomeccanica dobbiamo fare un tool che indichi
precisamente le cose e che possa anche dare informazioni precise a un agente AI
per poterne discutere. L'idea di mostrarlo da più angolazioni contemporaneamente
è interessante. […] poco alla volta dovremo fare un modello di tutto il corpo,
separatamente (fase per fase), ma per quello completo potremmo partire dal mio
progetto con motion capture. […] una UI abbastanza bella e interessante da usare
nel video divulgativo è secondaria attualmente. Potremmo usare un altro tool,
ci pensiamo dopo."

*AI inference:*
- Evolvere `tools/biomech-editor.html` (non ripartire da zero) verso una lavagna
  che esprime il modello `S→M→C→S`: stati/configurazioni, vincoli
  funzionali/LOCK, eventi temporali, condizioni di transizione, vettori,
  etichette OSS/INT/IPO.
- L'export JSON è il prodotto: deve bastare a un'AI per ragionare sul modello
  senza vedere l'immagine.
- Multi-vista ortografica con store di giunti condiviso (una posa, N proiezioni).
- Capability import: convertitore `captures/*.msgpack` → keyframe OSS
  nell'editor (i 33 landmark MediaPipe esistono già in camera-fighter).
- Annotazioni INT/IPO sopra i keyframe OSS importati.
- Lean: una capability alla volta; niente animazione/estetica divulgativa in
  questo tool.

*Still unresolved:*
- Quale slice prima: import-dati o authoring-semantico (vettori/LOCK/
  transizioni)?
- Il sampling ~17fps resta un limite per i timing rapidi — vale una nuova
  cattura più densa per le transizioni critiche?
- Se/quando serve un secondo tool per la divulgazione video.

**Formulazione approvata (FROZEN):**
|<!-- REQ:v1-tool-preciso --> Evolvere tools/biomech-editor.html in una lavagna
che esprime il modello S→M→C→S con informazioni precise e non ambigue per un
agente AI.<!-- REQ:v1-json-prodotto --> L'export JSON è il prodotto: sufficiente
a un'AI per ragionare sul modello senza vedere l'immagine.<!-- REQ:v1-multivista
--> Multi-vista ortografica con store di giunti condiviso.<!-- REQ:v1-import-
mocap --> Import dei landmark mocap (camera-fighter, msgpack 33 lm) come
keyframe OSS, con annotazioni INT/IPO sopra.<!-- REQ:v1-lean --> Una capability
alla volta; niente animazione né estetica divulgativa in questo tool.<!--
REQ:v1-corpo-fasi --> Modello corpo intero fase per fase, riusando il pipeline
mocap esistente.

---

## v2

**Status:** FROZEN
**Date:** 2026-09-20
**Authorized by:** Fausto
**Reason:** riprioritizzazione esplicita in sessione — "assolutamente è più che
secondario. Mi interessa prima di tutto fare slice dei movimenti singoli, senza
mostrare tutto il corpo e lavorare su quelli, il movimento intero sarà alla
fine." Drift log: `.mw/runs/2026-09-20-drift/desiderata-drift.md`.
**Sostituisce:** v1 resta valida su tutto tranne l'ordine: il corpo intero
passa da capability in roadmap a obiettivo finale.

**Intento del Director:**
Lavorare prima sui **movimenti singoli** (slice di movimento, es. la catena del
pugno) senza mostrare tutto il corpo; il movimento intero/corpo completo arriva
alla fine.

*User-stated:*
"assolutamente è più che secondario. Mi interessa prima di tutto fare slice dei
movimenti singoli, senza mostrare tutto il corpo e lavorare su quelli, il
movimento intero sarà alla fine."

*AI inference:*
- Il lavoro primario è sul modello semantico `S→M→C→S` applicato a movimenti
  singoli (la catena già presente nell'editor), non sul corpo intero.
- L'import mocap resta rilevante ma riscoped: si possono importare solo i
  landmark del movimento singolo (es. braccio) dai captures esistenti.
- La multi-vista resta utile ma applicata alla catena singola, con store
  condiviso.
- Full body = ultimo passo.

*Still unresolved:*
- Import dei soli landmark del movimento singolo: utile subito o dopo
  l'authoring semantico?

**Formulazione approvata (FROZEN):**
|<!-- REQ:v2-movimenti-singoli --> Prima i movimenti singoli: slice semantiche
S→M→C→S su catene parziali (es. braccio del pugno), senza mostrare il corpo
intero.<!-- REQ:v2-corpo-alla-fine --> Il modello corpo intero è l'ultimo
passo, non un prerequisito.<!-- REQ:v2-import-riscoped --> L'import mocap, se
fatto, è riscoped ai landmark del movimento singolo.

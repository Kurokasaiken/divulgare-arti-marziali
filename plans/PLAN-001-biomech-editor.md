# PLAN-001 — Evoluzione biomech-editor verso il modello S→M→C→S

**Stato:** `approvato` (Director, 2026-09-20 — "approvo il plan")
**Data:** 2026-09-20
**Desiderata:**
- `.mw/desiderata.md` **v1 FROZEN** — capability complessive del tool
- `.mw/desiderata.md` **v2 FROZEN** — ordine/priorità aggiornato (movimenti
  singoli prima; corpo intero alla fine; import riscoped)
**Provenienza:** deliberazione multi-AI web (`mw-iterative-deliberate --phase plan`,
transport web via sessioni personali Chrome CDP). Run 1 (`plan-v1-tool/`): panel
A=chatgpt + B=gemini-web — il testo sotto è `final.md` di quella run.
Run 2 (`plan-v1-tool-web4/`): ri-raccolta a 4 modelli — A=chatgpt, B=gemini-web,
C=deepseek, D=claude (grok escluso: rate-limit/upsell). Nota sul protocollo:
`--phase plan` usa solo gli slot A+B; le risposte di deepseek e claude sono state
raccolte come piani indipendenti sullo stesso prompt (file `cycle-01/C.md`,
`cycle-01/D.md` nella run, gitignored).
**Nota epistemica:** questo è il piano prodotto dal protocollo, non una decisione.
Diventa operativo solo dopo approvazione del Director.

---

## Confronto multi-modello sul nodo aperto (ordine capability)

Sul primo nodo — *import-dati vs authoring-semantico* — il panel si è **diviso 2-2**,
non convergente come appariva dalla sola run 1:

| Modello | Posizione |
|---|---|
| chatgpt (A, piano finale run 1) | semantica prima |
| gemini-web (B) | nella sua sintesi comparativa: **import prima** (dopo lo store canonico) |
| deepseek (C, indipendente) | **import prima** |
| claude (D, indipendente) | semantica prima |

**Argomento "semantica prima" (chatgpt, claude):** l'importer deve sapere in quale
modello scrivere; importare mocap senza contenitori S/M/C produce un visualizzatore
di tracce grezze e costringe a riadattare il modello dati dopo.

**Argomento "import prima" (gemini sintesi, deepseek):** lo store di giunti 3D
condiviso è prerequisito della multi-vista, e l'import mocap lo forza subito —
l'authoring semantico sul modello 2D attuale consoliderebbe un'astrazione
sbagliata; inoltre formalizzare la semantica senza dati reali rischia DSL
prematuro, mentre con le 5 rep OSS importate si può verificare se una C candidata
è esprimibile. I dati esistono già e il costo di import è basso.

**Punto di accordo unanime:** la Slice 1 è in ogni caso il contratto JSON canonico
con store unico — il fork reale è solo sulla Slice 2. DeepSeek propone S1 = schema
con contenitori semantici *vuoti* + import; la minoranza propone S1 = schema +
popolamento manuale della semantica.

**Decisione aperta per il Director** — entrambe le posizioni sono difendibili;
la differenza pratica è se le prime transizioni reali guidano la semantica
(import prima) o la semantica guida l'import (semantica prima).

### Risoluzione del fork (2026-09-20, desiderata v2)

Il Director ha riprioritizzato: *"Mi interessa prima di tutto fare slice dei
movimenti singoli, senza mostrare tutto il corpo e lavorare su quelli, il
movimento intero sarà alla fine."*

Con il corpo intero deprioritizzato, l'argomento portante di "import prima"
(lo store 3D full-body come prerequisito della multi-vista) perde forza:
l'import non serve più a forzare il modello 3D. Il fork si risolve verso
**semantica prima**, con import **riscoped** ai soli landmark del movimento
singolo — e come supporto all'authoring, non come prerequisito architetturale.

Sequenza rivista:

```
S1  Contratto JSON canonico + store unico (invariato — accordo unanime)  ✔ FATTA
S2  Authoring semantico sul movimento singolo: S→M→C→S, vettori, LOCK,
    eventi, OSS/INT/IPO   ✔ FATTA (minimale: C=unformalized, no DSL)
S3  Multi-vista ortografica sulla catena singola (store condiviso)     ✔ FATTA — anticipata dal Director (2026-09-20)
S4  Import mocap riscoped: landmark del solo movimento (es. braccio)
    → keyframe OSS, come materiale per INT/IPO
S5a Spike scientifico: definizione candidata di C   ← GATE, non opzionale
S5b Formalizzazione implementabile (schema predicati)
S5c Verifica sui dati OSS
S6  Diagnostica limite 17fps / eventuale cattura più densa
S7  Corpo intero — ultimo passo
```

**Gate esplicito su S5:** S5b non inizia prima che lo spike `C-CONDITION-01`
(`spikes/C-CONDITION-01.md`) abbia prodotto una definizione candidata di `C`
confrontata con la letteratura. Altrimenti si rischia di implementare
`C = threshold(...)` prima di sapere se `C` è rappresentabile come predicato —
cioè di trasformare una questione scientifica aperta in una feature software.

**Regola trasversale (livello ricerca vs livello rappresentazione):** la UI non
deve determinare la teoria. Se una condizione reale non è rappresentabile bene
nel JSON attuale, si cambia il modello dati — non si semplifica la teoria per
adattarla all'editor.

---

1. Ordine delle capability

Ordine raccomandato:

Contratto JSON canonico + modello S→M→C→S minimo

Authoring semantico minimo: vettori, LOCK, transizioni, eventi, OSS/INT/IPO

Multi-vista ortografica con store di posa condiviso

Import camera-fighter MsgPack → keyframe OSS

Corpo intero fase per fase

Rafforzamento di C, timing e qualità del dato mocap

La scelta importante è quindi:

Authoring-semantico prima dell'import-dati, ma solo come schema minimo e strumenti di editing. Non costruire prima una DSL.

Il motivo è strutturale: l'import MsgPack deve sapere in quale modello semantico inserire i dati. Se si importa prima, si rischia di costruire un buon convertitore per una rappresentazione che poi cambia quando vengono introdotti S, M, C, LOCK, vettori ed epistemicità.

Viceversa, non conviene implementare subito un editor completo del modello teorico: il contratto JSON deve essere abbastanza piccolo da poter essere validato e popolato sia manualmente sia dal mocap.

2. Slice 1 — Contratto JSON canonico + conservazione dell'editor attuale
Scopo

Trasformare l'attuale JSON da semplice serializzazione dell'editor in formato canonico del modello biomeccanico.

La UI può rimanere quasi invariata. Il risultato della slice è che una sequenza oggi rappresentata come keyframe/annotazioni diventa esplicitamente interrogabile come modello.

Schema JSON introdotto

Struttura iniziale indicativa:

JSON
{
  "schemaVersion": 1,
  "task": {
    "id": "right-punch",
    "desiredOutput": "...",
    "targetInteraction": "...",
    "temporalConstraints": {},
    "postActionState": {},
    "allowablePerturbation": {}
  },
  "joints": {},
  "states": [],
  "movements": [],
  "conditions": [],
  "transitions": [],
  "events": [],
  "annotations": []
}

Ogni oggetto semantico deve avere almeno:

JSON
{
  "id": "C1",
  "epistemic": "OSS"
}

con:

OSS = osservato
INT = interpretato
IPO = ipotesi

Importante: non introdurre ancora una sintassi generica per esprimere formule arbitrarie.

Componenti toccati

tools/biomech-editor.html

modello dati interno;

import/export JSON;

migrazione del formato attuale.

eventualmente un piccolo schema/validator incorporato nel file, senza dipendenze esterne.

Verifica

Dato un progetto creato nell'editor:

export;

cancellazione dello stato locale;

re-import;

confronto semantico del JSON;

nessuna informazione della posa/timeline deve andare persa.

Gate: l'export deve essere autonomamente interpretabile senza dipendere da localStorage o dallo stato implicito della UI.

3. Slice 2 — Authoring semantico minimo: S → M → C → S
Scopo

Rendere editabile il modello teorico senza ancora importare il mocap.

L'utente deve poter prendere una sequenza manuale e dichiarare:

S0
 ↓
M1
 ↓
C1
 ↓
S1

con sovrapposizione temporale tra movimenti.

Questa è la slice che risolve il nodo semantico prima dell'import.

Schema JSON esteso
JSON
{
  "states": [
    {
      "id": "S0",
      "time": 0,
      "configuration": {},
      "epistemic": "OSS"
    }
  ],
  "movements": [
    {
      "id": "M1",
      "start": 120,
      "end": 420,
      "vectors": [],
      "epistemic": "INT"
    }
  ],
  "conditions": [
    {
      "id": "C1",
      "afterMovement": "M1",
      "predicates": [],
      "epistemic": "IPO"
    }
  ],
  "transitions": [
    {
      "from": "S0",
      "movement": "M1",
      "condition": "C1",
      "to": "S1"
    }
  ]
}

**Estensione epistemico-causale (review esterna 2026-09-20):** il modello deve
comunicare non solo *cosa* succede ma *perché* si propone. Ogni transizione/
condizione può portare campi opzionali:

```json
{
  "id": "T1",
  "from": "S0", "movement": "M1", "condition": "C1", "to": "S1",
  "intendedEffect": ["constrain_left_side", "prepare_trunk_rotation"],
  "hypothesis": "Raggiungere questa configurazione fornisce un vincolo utile per la rotazione del tronco",
  "evidence": ["practitioner_observation", "video:5rep"],
  "status": "HYPOTHESIS",
  "prediction": "Ritardare/rimuovere il LOCK dovrebbe alterare il timing della rotazione del tronco"
}
```

Tre linguaggi sovrapposti sullo stesso modello: **geometrico** (traiettorie,
vettori), **temporale** (eventi, sovrapposizioni), **epistemico-causale**
(OSS/INT/IPO, ipotesi, evidenza, predizione). La predizione è ciò che rende il
modello *contestabile* da un'AI — non solo descrivibile. Le predizioni si
collegano al registro ipotesi (`wiki/03`) tramite ID (`H1`, …).

**Requisito emerso da spike C-CONDITION-01 (rev. avversariale):** lo schema
deve permettere **ipotesi concorrenti sullo stesso sottoinsieme di OSS** —
es. "modello continuo" vs "modello a transizioni" sullo stesso movimento,
ciascuna con le proprie predizioni. La funzione scientifica dell'editor è il
confronto predizione→misura, non la dimostrazione di una teoria unica.

Per i vettori, inizialmente basta una rappresentazione esplicita:

JSON
{
  "id": "V1",
  "from": "elbow",
  "to": "wrist",
  "startTime": 120,
  "endTime": 300,
  "direction": {
    "x": 0.82,
    "y": -0.57
  },
  "epistemic": "INT"
}
LOCK

LOCK deve essere un oggetto semantico, non una proprietà booleana del joint:

JSON
{
  "id": "L1",
  "type": "functional-lock",
  "target": "elbow",
  "start": 320,
  "end": 480,
  "epistemic": "INT"
}

Il nome functional-lock evita di suggerire che l'articolazione sia fisicamente immobilizzata.

Condizioni

Qui va mantenuta deliberatamente una distinzione:

la UI può creare condizioni, ma non deve ancora pretendere di aver definito la teoria matematica di C.

Per esempio:

JSON
{
  "id": "C1",
  "predicates": [
    {
      "type": "position-region",
      "target": "wrist",
      "region": "R1"
    }
  ]
}

oppure:

JSON
{
  "id": "C1",
  "status": "unformalized",
  "notes": "mano sufficientemente avanzata per iniziare M2"
}

Questo è preferibile a inventare ora un DSL del tipo:

velocity(shoulder) > 1.2 AND ...
Componenti toccati

timeline;

modello dati;

pannello/controlli semantici;

rendering di:

M;

C;

LOCK;

vettori;

transizioni;

epistemicità.

Verifica

Creare manualmente una sequenza con:

almeno 3 stati;

2 movimenti sovrapposti;

1 condizione;

1 LOCK;

2 vettori;

almeno una annotazione OSS, INT e IPO.

Export → re-import → stessa struttura semantica.

Gate: un AI che riceve solo il JSON deve poter ricostruire la catena causale dichiarata senza vedere la timeline.

4. Slice 3 — Multi-vista ortografica con store di giunti condiviso
Scopo

Passare da:

una posa → una vista

a:

una posa
 ├── frontale
 ├── laterale
 └── zenitale

senza duplicare lo stato biomeccanico.

Schema JSON

Il dato articolare deve essere indipendente dalla vista:

JSON
{
  "joints": {
    "shoulder_r": {
      "position": {
        "x": 123,
        "y": 210,
        "z": 84
      }
    }
  },
  "views": [
    {
      "id": "front",
      "projection": "orthographic"
    },
    {
      "id": "side",
      "projection": "orthographic"
    }
  ]
}

Le coordinate 3D diventano la sorgente; la vista contiene soltanto la proiezione/configurazione di visualizzazione.

Componenti toccati

renderer SVG;

store centrale della posa;

gestione drag dei joint;

proiezioni;

timeline/keyframe.

Verifica

Trascinare un joint nella vista A.

Gate obbligatorio:

la stessa posa cambia coerentemente in tutte le viste;

export contiene una sola configurazione articolare, non tre configurazioni indipendenti;

nessuna vista può diventare accidentalmente la fonte canonica rispetto alle altre.

Questo è uno dei gate architetturali più importanti dell'intero progetto.

5. Slice 4 — Import camera-fighter MsgPack → keyframe OSS
Scopo

Collegare finalmente il tool al dato reale già esistente.

Pipeline:

captures/*.msgpack
        ↓
parser
        ↓
33 MediaPipe landmarks
        ↓
normalizzazione
        ↓
keyframe OSS
        ↓
editor
        ↓
JSON canonico

Il dato importato deve rimanere distinguibile da ciò che viene interpretato dall'autore.

Schema JSON

Esempio:

JSON
{
  "source": {
    "type": "camera-fighter",
    "format": "msgpack",
    "landmarks": "MediaPipe-33",
    "samplingHz": 17
  },
  "keyframes": [
    {
      "id": "kf-001",
      "time": 0,
      "source": "capture-001",
      "epistemic": "OSS",
      "landmarks": {
        "right_shoulder": {},
        "right_elbow": {},
        "right_wrist": {}
      }
    }
  ]
}

Le interpretazioni successive non devono sovrascrivere il dato OSS.

Per esempio:

OSS: wrist = posizione osservata
INT: vettore del pugno = ...
IPO: condizione C1 = ...

sono tre livelli diversi.

Componenti toccati

importer MsgPack;

mapping MediaPipe → joint model;

normalizzazione coordinate;

keyframe store;

provenance/source metadata;

renderer.

Verifica

Usare una delle catture reali delle 5 ripetizioni.

Gate:

tutti i 33 landmark sono importabili;

timestamp preservati;

ordine temporale preservato;

keyframe risultano OSS;

nessun INT/IPO viene creato automaticamente;

export → reimport mantiene il dato.

La conversione non deve "capire" il pugno.

6. Slice 5 — Corpo intero fase per fase
Scopo

Generalizzare il modello dall'arto superiore all'intero corpo senza trasformare l'editor in un avatar sofisticato.

Skeleton minimo:

testa
  │
torace
  │
bacino
├── spalla → gomito → polso → mano
├── anca → ginocchio → caviglia → piede
└── ...

Il principio è:

modello completo, rendering minimale.

Non serve accuratezza estetica o anatomia 3D completa.

Schema JSON

Il modello dei joint diventa gerarchico:

JSON
{
  "bodyModel": {
    "version": 1,
    "joints": {
      "pelvis": {},
      "spine": {},
      "shoulder_r": {},
      "elbow_r": {},
      "wrist_r": {},
      "hip_r": {},
      "knee_r": {},
      "ankle_r": {}
    }
  }
}

Le fasi restano espresse come stati/transizioni, non come semplice array:

JSON
{
  "states": [
    "guard",
    "preparation",
    "delivery",
    "post_action"
  ]
}

ma ogni stato deve avere configurazione e provenance.

Componenti toccati

joint registry;

skeleton renderer;

multi-view;

keyframe;

importer mapping;

timeline.

Verifica

Importare una cattura e poterla rappresentare almeno nelle viste:

frontale;

laterale;

con una singola posa condivisa e corpo intero.

Gate: nessuna nuova logica semantica deve essere richiesta per aggiungere una parte del corpo.

7. Slice 6 — Condizioni di transizione verificabili
Scopo

Affrontare il debito esplicitamente dichiarato nella wiki: C non deve restare indefinitamente una metafora.

Questa slice viene dopo che il tool possiede dati reali, timeline, vettori e stati.

La ragione è importante: prima di avere esempi reali si rischia di progettare una formalizzazione delle condizioni completamente astratta.

Evoluzione dello schema

Da:

JSON
{
  "id": "C1",
  "notes": "mano sufficientemente avanti"
}

a:

JSON
{
  "id": "C1",
  "predicates": [
    {
      "type": "threshold",
      "variable": "wrist.distanceToTarget",
      "operator": "<=",
      "value": 0.08,
      "unit": "normalized"
    },
    {
      "type": "range",
      "variable": "trunk.angle",
      "min": 15,
      "max": 25,
      "unit": "deg"
    }
  ],
  "epistemic": "IPO"
}

Ma il formato esatto dei predicate va deciso solo dopo aver raccolto casi concreti.

Verifica

Per ogni C:

esiste una definizione esplicita;

è possibile calcolare se è vera/falsa su una sequenza;

il risultato è riproducibile;

l'export conserva sia condizione sia risultato.

8. Slice 7 — Analisi del limite temporale del mocap
Scopo

Non "risolvere" arbitrariamente il problema dei 17 fps, ma rendere esplicito quando il dato OSS è insufficiente per sostenere un'interpretazione.

A ~17 fps il passo temporale è circa:

1 / 17 ≈ 59 ms

Una transizione che avviene in pochi frame può quindi essere osservata con risoluzione temporale grossolana.

Schema

Metadata obbligatori:

JSON
{
  "sampling": {
    "nominalHz": 17,
    "temporalResolutionMs": 58.8
  }
}

Eventi e condizioni possono dichiarare precisione:

JSON
{
  "timingConfidence": "limited"
}
Verifica

Prendere almeno una transizione rapida e classificare esplicitamente:

OSS sufficientemente risolta
OSS temporalmente ambigua
INT derivata da dato insufficiente

Non interpolare per trasformare un'osservazione a 17 fps in un'osservazione ad alta frequenza.

Se il caso critico non è risolvibile, quello diventa l'input per una nuova cattura più densa.

9. Rischi principali e mitigazioni
Rischio	Conseguenza	Mitigazione
Incoerenza multi-vista	ogni vista evolve verso una posa diversa	store unico dei joint; view = proiezione
DSL prematuro	si cristallizza una teoria ancora inesplorata	predicate minimi + unformalized; nessun linguaggio generale
Import prima dello schema	pipeline mocap costruita sul modello sbagliato	contratto JSON prima, import dopo
17 fps insufficiente	timing rapido apparentemente preciso ma non osservato	provenance + risoluzione temporale + flag di ambiguità
Confusione OSS/INT/IPO	inferenze presentate come dati	epistemicità obbligatoria sugli oggetti semantici
LOCK interpretato come articolazione bloccata	modello biomeccanico scorretto	functional-lock come vincolo configurazionale
C ridotta a una soglia arbitraria	il modello teorico viene falsificato dall'implementazione	inizialmente condizioni dichiarative; formalizzazione successiva
JSON dipendente dalla UI	AI incapace di ragionare senza editor	JSON come source of truth, UI come vista
Crescita verso un avatar/animazione	perdita del focus	rendering solo funzionale al modello
Corpo intero troppo presto	grande lavoro infrastrutturale prima della validazione	prima arto superiore + semantica + multi-view + mocap
10. Confini espliciti del piano
Dentro

JSON canonico;

stati/configurazioni;

movimenti;

transizioni;

condizioni;

LOCK funzionali;

vettori;

eventi temporali;

OSS/INT/IPO;

keyframe;

multi-view ortografico;

import MediaPipe 33 landmark;

corpo intero fase per fase;

provenance e qualità temporale.

Fuori

avatar realistico;

IK;

simulazione fisica;

riconoscimento automatico della tecnica;

inferenza automatica di C;

AI integrata nell'editor;

animazione divulgativa;

rendering 3D sofisticato;

sistema generico di scripting biomeccanico;

estetica da prodotto/video.

11. Sequenza operativa finale

La roadmap minima diventa:

S1  JSON canonico
 ↓
S2  S→M→C→S + vettori + LOCK + epistemicità
 ↓
S3  multi-view con store condiviso
 ↓
S4  MsgPack → OSS keyframes
 ↓
S5  corpo intero
 ↓
S6  C verificabili
 ↓
S7  validazione timing / eventuale cattura >17 fps

Il punto architetturale centrale è che S1–S2 definiscono il linguaggio dei dati, S3 definisce la loro geometria, S4 porta dentro l'evidenza osservata e S6 prova a rendere operativa la teoria.

Questo evita due errori opposti: costruire prima un importer mocap senza sapere quale modello debba produrre, oppure costruire prima una sofisticata DSL teorica senza avere dati reali con cui verificarla.
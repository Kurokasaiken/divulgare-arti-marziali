---
title: Session Handoff
type: state
updated: 2026-09-20
---

# Session Handoff

## Stato aggiunto 2026-09-20 (terza revisione + spike C-CONDITION-01)

- **R-008 applicata**: R-003 duplicato → R-007; PLAN-001 desiderata v1+v2 e
  gate S5a (spike prima dei predicati); regola "UI non determina la teoria" in
  AGENTS; `02` — supinazione come rappresentazione, piede/tronco come INT.
- **`spikes/C-CONDITION-01.md` aperto e avviato**: Fuchs 2018 (abstract)
  compilato → SSM copre "inizio non seriale", NON "innesco da condizione
  sufficiente" → novità non chiusa; mappatura preliminare motor-control
  (priors); nota: `C` ≈ guard condition in sistemi ibridi (forma esiste, il
  contenuto è la questione aperta).
- Direzione: completare lo spike (letture fonti primarie Q2/Q3) prima di S2/S5b.

## Stato aggiunto 2026-09-20 (desiderata v1 FROZEN + PLAN-001 da deliberazione web)

- **`.mw/desiderata.md` v1 FROZEN** — tool che esprime S→M→C→S, JSON come
  prodotto, multi-vista condivisa, import mocap, lean.
- **PLAN-001** (`plans/PLAN-001-biomech-editor.md`, stato `proposta`): prodotto
  da deliberazione multi-AI web (chatgpt + gemini-web, convergenti). Roadmap:
  S1 contratto JSON canonico → S2 authoring semantico (vettori/LOCK/OSS-INT-IPO)
  → S3 multi-vista store condiviso → S4 import msgpack → S5 corpo intero →
  S6 condizioni C verificabili → S7 diagnostica limite 17fps.
  Decisione chiave: **schema semantico prima dell'import** (l'importer deve
  sapere in quale modello scrivere); niente DSL prematura.
- **Desiderata v2 FROZEN** (riprioritizzazione Director): movimenti singoli
  prima, senza corpo intero; corpo intero = ultimo passo; import mocap riscoped
  ai landmark del singolo movimento. Drift log in `.mw/runs/2026-09-20-drift/`.
- PLAN-001 aggiornato: il fork multi-AI "import vs semantica" si risolve verso
  semantica prima (lo store 3D full-body non è più prerequisito); sequenza
  rivista con corpo intero in S7.
- PLAN-001 **approvato** dal Director → **S1 implementata** (JSON canonico
  schemaVersion 2 in biomech-editor: task, skeleton, keyframes con ID stabili +
  epistemic, events, contenitori S/M/C/transizioni/vincoli/vettori vuoti;
  migrazione legacy; round-trip verificato in browser). Prossima slice: S2
  authoring semantico (S→M→C→S, vettori, LOCK, editing OSS/INT/IPO).

## Stato aggiunto 2026-09-20 (revisione R-003 + install MW + desiderata candidata)

- **Mind Weaver installato** (`install.sh --with-runtime`): skill, runtime
  proxy, pointer IDE. `.env`/providers/sessions gitignored; repo pubblico pulito.
- **R-003 applicata** (seconda revisione Director, 15 punti):
  - `08` — "nessuna fonte" → stato ricerca non conclusione; **questione teorica
    centrale** (Cᵢ nuovo vs rappresentazione di noti); corpus motor-control da
    mappare; **spike Fuchs 2018** come tabella confronto.
  - `09` — CONOSCIAMO con una fonte per claim; effective mass come costrutto
    dibattuto; OSS diviso `[video]`/`[empirico]`; prossima domanda = "cosa è
    noto / combinazione / nuovo"; collo di bottiglia = scientifico.
  - `01` — `C` come congiunzione di predicati misurabili o switching boundary.
  - `02` — anelli → rete di transizioni (direzione futura); ultimo momento
    utile come frontiera possibile.
- **Dati mocap verificati** in camera-fighter: `mac/captures/pugno_destro/`,
  5 rep msgpack, 33 landmark MediaPipe, ~17fps misurato, ~4s/rep — importabile
  come keyframe OSS (`07` aggiornato).
- **Desiderata v3 candidata** (tool + modello corpo intero via mocap): in attesa
  di approvazione Director → poi freeze in `.mw/desiderata.md` e R-XXX.
- **Direzione corrente:** il progetto è entrato nella fase "confronto
  dell'intuizione con la letteratura". Prossimo passo = spike Fuchs 2018 +
  mapping motor-control, NON altro software.

## Stato aggiunto 2026-09-20 (revisione R-002: mapping scientifico + formalizzazione)

- Applicata la critica in 15 punti del Director:
  - **Nuova `wiki/08-letteratura-biomeccanica.md`**: le 4 categorie esplicative
    (meccanica/biomeccanica/motor control/modello), tabella di mapping concetti
    nostri ↔ esistenti, fonti reali raccolte (Fuchs 2018 CSM/SSM come riferimento
    più vicino alla sovrapposizione; studi effective mass MDPI 2024/2025;
    Walilko 2005; Turner 2015 controverso; Bernstein/Newell/Todorov-Jordan/
    Latash da mappare).
  - **Nuova `wiki/09-stato-della-ricerca.md`**: conosciamo / osservato /
    interpretato / ipotizziamo / non sappiamo / da verificare / prossima domanda.
  - `01-modello-movimento.md`: "principio dei gradi di libertà" declassato a
    **working principle** finché il mapping non è completo; aggiunta notazione
    minima S→M→C→S con debito esplicito sulla definizione operativa di
    "condizione sufficiente"; nuove sezioni **TASK** (struttura del compito) e
    **stato post-azione** come output del modello.
  - `02-anatomia-del-pugno.md`: disclaimer rafforzato (decomposizione di lavoro,
    non biomeccanica stabilita; anello = unità analitica); "ultimo momento
    utile" con debito di formalizzazione e variabili candidate.
  - `05-glossario.md`: compito, stato post-azione, principio di lavoro, anello
    come unità analitica, 4 categorie.
- **Prossima attività indicata dal Director:** portare il progetto dalla
  formulazione concettuale alla mappatura rigorosa con biomeccanica e motor
  control — capire cosa è già noto con altro nome, cosa è combinazione di
  noti, cosa è eventualmente nuovo. Primo passo concreto: leggere Fuchs 2018.

## Stato aggiunto 2026-09-20 (strumento visuale v0)

- **`tools/biomech-editor.html`** importato (prototipo fatto da Claude, da
  `~/Downloads`). Editor keyframe self-contained: catena spalla→gomito→polso→
  mano, proporzioni fisse, rotazioni assiali come annotazioni timeline, export
  JSON, localStorage. Gap rispetto al modello annotati in
  `wiki/06-strumento-visuale.md` (vettori, condizioni sufficienti, LOCK, viste,
  segmenti oltre l'arto superiore).

## Stato aggiunto 2026-09-20 (bootstrap del progetto)

- **Progetto creato** (R-001): struttura lean — README, AGENTS.md, CLAUDE.md,
  CANON.md, RICHIESTE.md, wiki/ (7 pagine).
- **Contenuto:** distillato della discussione Director↔ChatGPT sulla
  formalizzazione biomeccanica del pugno: modello stato→movimento→condizione→
  configurazione/vincolo, sovrapposizione temporale, principio dei gradi di
  libertà, scomposizione in anelli 0–6, ipotesi H1–H6, 7 fasi del metodo,
  glossario, ruolo subordinato dello strumento visuale, limiti del video 15fps.
- **Scelte interpretative da confermare:**
  - "modalità lean" = niente `plans/`, `execution/`, skill, runtime finché non
    serve; conoscenza in `wiki/`, decisioni in `CANON.md`, richieste in
    `RICHIESTE.md`.
  - Nome directory: `divulgare-arti-marziali` in `progetti_personali/`.
  - Progetto inizializzato come repo git standalone.
- **Prossimi step candidati (non approvati):**
  - FASE 1 del metodo: definizione precisa di "pugno ottimale" e dei vincoli.
  - FASE 2: consolidare il glossario in definizioni formali.
  - Verifica terminologica contro letteratura (motor control, biomeccanica del
    colpo) prima di adottare i termini candidati.
  - Prima sessione su un anello specifico (es. anello 2, il più analizzato).

## Aggiunta (2026-09-20, tarda sessione)

- **R-009**: integrata proposta epistemico-causale (why-layer) in PLAN-001 S2,
  wiki/06 (doppia vista canonical data) e spike (test di contestabilità).

## Aggiunta (2026-09-20, spike C-CONDITION-01 — primo risultato)

- Spike avanzato su fonti verificate: **la forma di `C` esiste già** —
  initiation set / termination condition (options framework, Sutton-Precup-
  Singh 1999, AIJ); guard condition (automata ibridi); entry-state transition
  conditions (grafi di motion primitives, arXiv:2106.10310, robotica).
- Nucleo distintivo residuo (ipotetico): applicazione alla coordinazione
  intra-gesto umano + semantica forward-looking su stato post-azione.
- OFC (Todorov-Jordan 2002) verificato: minimal intervention copre "preserva
  DOF finché utile", ma è feedback continuo — non trigger discreto. APA copre
  il principio t−Δt. Fuchs 2018: sovrapposizione parziale (no innesco da
  condizione).
- wiki/08 (mapping aggiornato) e wiki/09 (NON SAPPIAMO + PROSSIMA DOMANDA
  aggiornate) riflettono il risultato. Restano priors da verificare su fonti
  primarie (Bernstein, Newell, Latash).

## Aggiunta (2026-09-20, revisione avversariale → spike C-02)

- Review esterna sul verdetto di C-01: regge, ma il problema vero è
  l'**identificabilità** — continuo / continuo+switching / gerarchico
  producono la stessa cinematica. Regola: decomposizione analitica ≠
  architettura discreta (submovements, intermittency).
- Nuova direzione: `C` forse frontiera nello **spazio delle variabili di
  task** (UCM/Latash), non articolare. Domanda chiave: "il modello C aggiunge
  capacità esplicativa rispetto a un continuo equivalente?" → test della
  frontiera predittiva.
- Creato `spikes/C-02-continuous-vs-triggered.md` (aperto). Aggiornati
  wiki/08, wiki/09, PLAN-001 (ipotesi concorrenti sugli stessi OSS).
- Prossimo passo: eseguire lo spike C-02 (rassegna evidenza sperimentale).

## Aggiunta (2026-09-20, chiarimento obiettivo — R-011)

- Il Director ha chiarito: obiettivo = **spiegazione scientifica rigorosa
  della tecnica**, fase per fase (τ = r×F, impulso, DOF...), non nuova
  teoria. Gerarchia: spiegare → noto → lacune → novità residua.
- `wiki/00` (gerarchia obiettivi), `wiki/04` (scheda analisi per fase/anello),
  `wiki/09` (nota direzione) aggiornati. Spike C-02 resta aperto ma
  subordinato: serve per scrivere affermazioni causali corrette.

## Aggiunta (2026-09-20, scheda Anello 2 compilata)

- Prima applicazione della scheda di analisi (FASE 3): Anello 2, retrazione +
  LOCK braccio sinistro, in `wiki/02`. Risultato utile: separa nettamente OSS
  (4 items con provenienza), INT/IPO meccaniche (5 candidati funzione, nessuno
  scelto a priori), e 4 cose "non dimostrate".
- Due predizioni registrate in `wiki/03`: P-A2.1 (LOCK → timing rotazione,
  serve cattura densa) e **P-A2.2 (I stimato da landmark+antropometria —
  calcolabile SUBITO** — primo test quantitativo possibile senza strumenti).
- Per S2: la scheda mostra che il JSON deve sostenere campi `cost`,
  `alternatives`, `predictions` con ID — oltre a forces/moments.

## Aggiunta (2026-09-20, S3 multi-vista — fatta)

- Director ha anticipato S3 su S2/schede. Implementata: giunti 3D, 3 viste
  ortografiche su store condiviso, schema v3 + campo `views`, migrazione
  v2/legacy. Verificata in browser (gate S3: stessa posa in tutte le viste,
  export con una sola configurazione). Schema keyframe ora `[x,y,z]`.
- Prossimi candidati: S2 authoring semantico / schede anelli restanti /
  P-A2.2 (stima I da landmark) / S4 import mocap.

## Aggiunta (2026-09-20, S2 semantico minimale — fatta)

- R-013: wiki/06 allineato a S3; S2 implementata (pannello semantico,
  S/M/C/T/LOCK/V/A con epistemic+provenance, transizioni per ID,
  C=unformalized di default). Gate: catena ricostruibile da solo JSON.
- Avvertenza review: attenzione a catene di spiegazioni derivate dalla stessa
  ipotesi non verificata (LOCK→vincolo→rotazione→coppia→trasferimento).
- Prossimi candidati: schede anelli restanti; P-A2.2 (I stimato, calcolabile
  subito); S4 import mocap (porta provenance:measured); spike C-02.

## Aggiunta (2026-09-20, bozza Anello 2 in S2 — R-014)

- `tools/examples/anello-2-retrazione.json`: primo caso d'uso completo del
  linguaggio S2 (S1→M1→C1→S2→M2→C2→S3 + LOCK + V1/V2 displacement +
  supinazione). Bozza autoriale, non formalizzazione scientifica.
- Aggiunto vector mode 'displacement' (spostamento giunto tra due tempi) —
  necessario per rappresentare V1 retrazione.
- Limite noto: stato↔keyframe legati solo per time implicito.
- Criterio di riuscita dichiarato dal Director: JSON+visualizzazione devono
  bastare a un lettore esterno — il test umano resta da fare.

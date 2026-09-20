---
title: Session Handoff
type: state
updated: 2026-09-20
---

# Session Handoff

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
- In attesa: approvazione PLAN-001 prima di implementare S1.

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

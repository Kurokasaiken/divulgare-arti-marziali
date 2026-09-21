---
title: Richieste esplicite
type: intent-ledger
updated: 2026-09-20
---

# Richieste esplicite

**Questo file è la bussola operativa. Contiene ciò che Fausto ha chiesto, con le sue parole.**

L'AI può mettere in discussione una richiesta. Non può ignorarla, riformularla in
silenzio, ridurla, o rinviarla. Gli stati `ridotta`, `rinviata`, `ritirata` richiedono
approvazione esplicita. Il testo fra virgolette è verbatim e non si riscrive.

## Stati

`da chiarire` · `aperta` · `in corso` · `fatta` · `ridotta` · `rinviata` · `ritirata`

---

## R-001 — Creare il progetto con wiki e documentazione

**Richiesta:** *"Crea un nuovo progetto: Divulgare Arti Marziali. Ti passo la mia
discussione con chatGPT, poi passa in modalità lean, crea un wiki, una
documentazione adeguata, ecc"*
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:** creata struttura lean — `README.md`, `AGENTS.md`, `CANON.md`,
`RICHIESTE.md`, `SESSION_HANDOFF.md` e `wiki/` con 7 pagine che distillano la
discussione sulla formalizzazione biomeccanica del pugno (progetto, modello del
movimento, scomposizione per anelli, registro ipotesi, metodo/fasi, glossario,
strumento visuale). "Modalità lean" interpretata come: nessun apparato
(`plans/`, `execution/`, skill, runtime) finché non serve.

---

## R-002 — Revisione della wiki: mapping scientifico, formalizzazione, stato della ricerca

**Richiesta:** *"Manca ancora la parte scientifica che stavamo iniziando a
costruire [...] il repository adesso è una buona memoria esterna del progetto, ma
non è ancora la conclusione della ricerca. È il punto di partenza formalizzato."*
(critica in 15 punti, sessione 2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:** create `wiki/08-letteratura-biomeccanica.md` (4 categorie,
mapping, fonti reali) e `wiki/09-stato-della-ricerca.md`; aggiornati
`01-modello-movimento.md` (working principle, notazione S→M→C, TASK, stato
post-azione), `02-anatomia-del-pugno.md` (decomposizione di lavoro, formalizzazione
"ultimo momento utile"), `05-glossario.md`, `INDEX.md`, `SESSION_HANDOFF.md`.
Pushato su GitHub (pubblico).
**Punti della richiesta:**
1. Aggiungere il mapping concetti nostri ↔ letteratura (tabella concetto/relazione/stato).
2. Il "principio dei gradi di libertà" non va trattato come principio scientifico:
   rinominato **principio di lavoro** finché il mapping non è fatto.
3. Dare una definizione minima formale alla sequenza S→M→C→S (stato/movimento/
   condizione sufficiente) — altrimenti resta metafora.
4. "Ultimo momento utile" da formalizzare (posizione, velocità, traiettoria
   desiderata, errore dal target, costi).
5. La scomposizione del pugno va marcata ancora più chiaramente come *nostra
   decomposizione di lavoro*, non biomeccanica stabilita.
6. "Anello": esplicitare che è unità analitica del modello, non categoria
   anatomica standard.
7. Nuova pagina letteratura: cosa è noto, controverso, pertinente, adiacente,
   non-supportante (effective mass, impulso, force-time, boxers, momentum
   transfer).
8. Separare 4 categorie: meccanica / biomeccanica / motor control / modello del
   progetto.
9. Rendere esplicito il concetto di **compito** (TASK: output desiderato,
   interazione, vincoli temporali, stato post-azione, perturbazione ammissibile).
10. Sviluppare lo **stato post-azione** come parte del modello.
11. Non ripartire da zero con lo strumento visuale: il prototipo esiste.
12–14. CANON vuoto va bene: non canonizzare per riempire; la conoscenza cresce
   nella wiki.
15. Nuova pagina **Stato della ricerca**: conosciamo / osservato / interpretato /
    ipotizziamo / non sappiamo / dobbiamo verificare / prossima domanda.

---

## R-003 — Seconda revisione: mapping motor-control, C operativa, provenienza osservazioni

**Richiesta:** *"prima di continuare: [...] il prossimo passo NON dovrebbe essere
costruire altro software [...] il collo di bottiglia è scientifico"*
(critica in 15 punti nn. 5–15, sessione 2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- `08`: "nessuna fonte trovata" riformulato come *stato della ricerca*, non
  conclusione; aggiunta **questione teorica centrale** (`Cᵢ` nuovo o
  rappresentazione di concetti esistenti?) con corpus motor-control da mappare;
  aggiunto **spike Fuchs 2018 vs nostro modello** come tabella di confronto.
- `09`: CONOSCIAMO riscritto con una fonte per affermazione; effective mass
  riformulato come costrutto dibattuto (Turner 2015), non fatto semplice;
  ABBIAMO OSSERVATO diviso per provenienza `[video]`/`[empirico]`; "poca
  attività muscolare" marcata come percepito, non misurato; PROSSIMA DOMANDA
  riformulata sulla domanda centrale della fase; dichiarato che il collo di
  bottiglia è scientifico, non software.
- `01`: debito su `C` esteso — forma candidata come congiunzione di predicati
  misurabili + possibilità che `C` sia una frontiera (switching boundary), non
  una soglia.
- `02`: nota "anelli → rete di transizioni" come prossima rappresentazione;
  "ultimo momento utile" con ipotesi switching-boundary.

---

## R-004 — Desiderata v1 FROZEN + deliberazione multi-AI web per il piano tool

**Richiesta:** *"Approvi la v3 come FROZEN? […] passa al protocollo multi AI web
per questo plan"* (sessione 2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- Desiderata congelata come **v1 FROZEN** in `.mw/desiderata.md` (verbatim
  user-stated + AI inference: evolve biomech-editor → modello S→M→C→S, JSON
  come prodotto, multi-vista con store condiviso, import mocap msgpack, lean).
- Lanciata deliberazione `--phase plan` via transport web (Chrome CDP, sessioni
  personali): panel A=chatgpt + B=gemini-web (config `deliberation-config-web.yaml`).
  Smoke test OK su entrambi; deepseek/claude/grok con sessioni rotte (login page
  / rate limit) — restano solo come fallback.
- Artefatti in `.mw/runs/plan-v1-tool/` (prompt.txt, context.txt, output).
- Deliberazione convergente in 1 ciclo → `plans/PLAN-001-biomech-editor.md`
  (stato `proposta`, in attesa di approvazione Director prima dell'esecuzione).

---

## R-005 — Riprioritizzazione: movimenti singoli prima, corpo intero alla fine

**Richiesta:** *"assolutamente è più che secondario. Mi interessa prima di
tutto fare slice dei movimenti singoli, senza mostrare tutto il corpo e
lavorare su quelli, il movimento intero sarà alla fine"* (2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- Drift vs desiderata v1 registrato in `.mw/runs/2026-09-20-drift/`.
- Desiderata **v2 FROZEN** in `.mw/desiderata.md`: movimenti singoli prima,
  corpo intero alla fine, import mocap riscoped ai landmark del movimento.
- PLAN-001 aggiornato: fork "import vs semantica" risolto → semantica prima;
  sequenza rivista S1–S7 con corpo intero ultimo.

---

## R-006 — Approvazione PLAN-001 + implementazione Slice 1

**Richiesta:** *"approvo il plan […] dobbiamo passare all'implementazione"*
(2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta` (S1), `in corso` (roadmap)
**Cosa è successo:**
- PLAN-001 marcato `approvato`.
- **S1 implementata** in `tools/biomech-editor.html`: export/import JSON
  canonico `schemaVersion: 2` (task, skeleton, keyframes con ID stabili +
  epistemic, events, contenitori semantici vuoti), migrazione legacy,
  textarea editabile + pulsante Importa, save/load/auto-persist in formato
  canonico.
- Verificato in browser (puppeteer): round-trip export→import→export
  semanticamente identico; migrazione legacy OK; UI integra (3 ossa, 4 giunti,
  3 kf, 1 rotazione).

---

## R-007 — Evolvere biomech-editor verso la lavagna del modello

*(originariamente registrata come secondo "R-003" — rinumerata R-007 il
2026-09-20 perché l'ID collidevano con R-003 "Seconda revisione")*

**Richiesta:** *"Intanto per studiare la teoria biomeccanica dobbiamo fare un
tool che indichi precisamente le cose e che possa anche dare informazioni precise
ad un agente AI per poterne discutere. L'idea di mostrarlo da più angolazioni
contemporaneamente è interessante. [...] poco alla volta dovremo fare un modello
di tutto il corpo, separatamente (fase per fase), ma per quello completo
potremmo partire dal mio progetto con motion capture."*
**Data:** 2026-09-20
**Stato:** `in corso` (PLAN-001 approvato, S1 fatta)
**Desiderata:** v1+v2 FROZEN — `.mw/desiderata.md` (v2 riprioritizza: movimenti
singoli prima, corpo intero alla fine)

---

## R-008 — Terza revisione: fix governance + spike scientifico C-CONDITION-01

**Richiesta:** revisione esterna del repository (sessione 2026-09-20): duplicato
R-003, desiderata v1→v2 in PLAN-001, gate scientifico prima di S5, regola "la UI
non determina la teoria", formulazioni INT troppo assertive in `02`, supinazione
come rappresentazione non ontologia, e *"il prossimo lavoro dovrebbe essere
SPIKE SCIENTIFICO 01 — What exactly is C?"*.
**Data:** 2026-09-20
**Stato:** `in corso`
**Cosa è successo:**
- Fix: R-003 duplicato rinumerato R-007; PLAN-001 dichiara desiderata v1+v2;
  S5 spezzata in S5a (spike) / S5b (schema) / S5c (verifica) con gate esplicito.
- Regola "la UI non determina la teoria" aggiunta ad `AGENTS.md`.
- `02`: supinazione = scelta di rappresentazione; piede e tronco riformulati
  come INT del progetto con funzioni candidate esplicite.
- Spike `spikes/C-CONDITION-01.md` creato e avviato: tabella Fuchs 2018
  compilata (abstract) → sovrapposizione parziale, novità non chiusa;
  mappatura preliminare motor-control (priors da verificare); nota Q3 su
  guard condition in sistemi ibridi.

---

## R-009 — Estensione epistemico-causale del modello (input AI esterno)

**Richiesta:** proposta via review esterna (ChatGPT, 2026-09-20): il JSON del
modello deve comunicare non solo *cosa* succede ma *perché* — campi
intendedEffect/hypothesis/evidence/status/prediction; tre linguaggi sovrapposti
(geometrico / temporale / epistemico-causale); canonical data come unica fonte
con viste umana e AI.
**Data:** 2026-09-20
**Stato:** `fatta` (integrazione documentale; implementazione in S2)
**Cosa è successo:**
- PLAN-001 S2: schema transizioni esteso con campi epistemico-causali;
  predizioni collegate al registro ipotesi via ID (`H1`, …).
- `wiki/06`: diagramma "canonical data → human view + AI view → same model".
- Spike C-CONDITION-01: aggiunto test di contestabilità (l'AI deve poter
  obiettare dipendenza causale vs semplice sovrapposizione temporale).

---

## R-010 — Revisione avversariale dello spike C-01 + spike C-02 (continuo vs triggered)

**Richiesta:** revisione esterna del verdetto di C-CONDITION-01 (sessione
2026-09-20): *"il prossimo spike dovrebbe essere molto piccolo: C-2 Continuous
vs State-Triggered Transition"*; tre modelli concorrenti indistinguibili dalla
sola cinematica; regola "decomposizione analitica ≠ architettura discreta";
`C` possibilmente come frontiera nello spazio delle variabili di task (UCM);
ipotesi di lavoro riformulata in modo difendibile; editor come strumento di
confronto tra ipotesi concorrenti sugli stessi dati.
**Data:** 2026-09-20
**Stato:** `in corso`
**Cosa è successo:**
- `spikes/C-CONDITION-01.md`: sezione "Revisione avversariale" — tre modelli
  (continuo / continuo+switching / gerarchico), identificabilità, precedenti
  submovements+intermittency, ipotesi riformulata, `C` nello spazio delle
  variabili di task, domanda "C aggiunge capacità esplicativa vs continuo?".
- Creato `spikes/C-02-continuous-vs-triggered.md` (domanda, tabella modelli,
  regola, test della frontiera predittiva, domande operative, output).
- `wiki/08`: due righe nuove nel mapping (UCM task-space; discreto apparente).
- `wiki/09`: NON SAPPIAMO + PROSSIMA DOMANDA aggiornate alla domanda empirica.
- `PLAN-001` S2: requisito "ipotesi concorrenti sugli stessi OSS" nello schema.

---

## R-011 — Chiarimento dell'obiettivo primario: spiegazione rigorosa, non nuova teoria

**Richiesta:** *"Il mio obiettivo principale è poter spiegare, punto per punto,
fase x fase, cosa intendo x 'ottimale' e spiegare la mia tecnica nel modo +
preciso, scientifico, usando fisica e biomeccanica. nn da maestro di arti
marziali, ma da 'scenziato'. Parlare di momento, le definizioni corrette,
momento torcente, ecc. Voglio che chiunque faccia uno sport da combattimento
possa capirne la teoria 'del movimento' e se ha dubbi sia già stato
esplicitato e sviscerato in modo esaustivo."* (2026-09-20) — con revisione
esterna che propone la gerarchia: spiegare → identificare il noto → lacune →
novità residua.
**Data:** 2026-09-20
**Stato:** `fatta` (integrazione documentale)
**Cosa è successo:**
- `wiki/00`: nuova sezione "Gerarchia degli obiettivi" — spiegazione rigorosa
  prima; novità di `C` come possibile sottoprodotto, non motore; i precedenti
  in letteratura sono il funzionamento previsto, non un danno.
- `wiki/04`: "Scheda di analisi per fase/anello" — catena OSS → cinematica →
  forze/momenti (τ = r×F) → funzione meccanica → costo → perché → effetto
  sulla fase successiva → alternative → letteratura → ipotesi → misura.
- `wiki/09`: nota di direzione — C-02 subordinato alla correttezza delle
  affermazioni causali, non a una rivendicazione di teoria.
- Valutazione esterna registrata: ~4/10 oggi come risultato scientifico,
  potenziale 7–8/10 se verificato — il valore è nella formalizzazione
  rigorosa e falsificabile, non nella scoperta già avvenuta.

---

## R-012 — Priorità Director: multi-vista prima (S3 anticipata)

**Richiesta:** alla domanda "cosa preparo per primo — schede testuali / S2
semantico / S3 multi-vista" il Director ha scelto **S3 multi-vista**
(2026-09-20): *"dovremmo avere anche un modo di rappresentare scena x scena
da + punti d vista, dovremmo prepararli."*
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- `tools/biomech-editor.html`: store giunti → 3D `[x,y,z]`; tre viste
  ortografiche (frontale x-y, laterale z-y, zenitale x-z) sullo stesso store;
  drag in una vista modifica solo i due assi proiettati; schema → v3 con
  campo `views`; migrazione v2 (2D→z=0) e legacy.
- Gate S3 verificato in browser (puppeteer): drag nella vista laterale →
  tutte le viste aggiornate dalla stessa posa; export = una sola
  configurazione articolare, nessuna copia per-vista; round-trip
  export→import→export; migrazioni OK.

---

## R-013 — Quarta revisione: allinea wiki/06 a S3, poi S2 semantico minimale

**Richiesta:** revisione esterna post-S3 (sessione 2026-09-20): wiki/06 ancora
indietro rispetto al codice (v2, multi-vista come "manca"); raccomandazione
*"a questo punto io farei S2"* come authoring semantico minimale — `C` non
matematico subito (`unformalized` + predicati opzionali dopo); provenance
authored/measured; attenzione a catene di spiegazioni tutte derivate dalla
stessa ipotesi non verificata.
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- `wiki/06` allineato: store 3D + tre proiezioni + schema v3 spostati in
  "implementato"; limite "coordinate autoriali ≠ misura" dichiarato.
- `tools/biomech-editor.html` S2 minimale: pannello semantico con oggetti
  S/M/C/T/LOCK/vettori/annotazioni — epistemic editabile, provenance
  `authored`, transizioni collegate per ID con campi
  intendedEffect/hypothesis/prediction; condizioni `unformalized` di default;
  LOCK evidenzia il segmento, vettori disegnati come frecce nelle tre viste;
  fix: keyframe creati da dblclick/+Keyframe ora hanno ID stabile.
- Gate S2 verificato (puppeteer): catena S1→M1→C1→S2 ricostruibile dal solo
  JSON; round-trip semantico OK; render vettori/LOCK attivi/inattivi OK.

---

## R-014 — Bozza Anello 2 come primo caso d'uso di S2

**Richiesta:** *"preferisco che lo prepari tu come bozza nell'editor [...] non
consideriamola ancora una 'formalizzazione scientifica' dell'Anello 2. Deve
essere il primo caso di studio completo del nuovo linguaggio S2."* Struttura
S1→M1→C1→S2→M2→T1→S3; C1 `unformalized`; vettori solo geometricamente
descrivibili; hypothesis/prediction/esistemic separati. Criterio di riuscita:
*"un'altra persona, leggendo soltanto il JSON + visualizzazione, riesce a
ricostruire esattamente cosa stiamo dicendo?"* (2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- Aggiunto `mode:'displacement'` ai vettori (V1 = spostamento del gomito nel
  tempo, non giunto→giunto — necessario per V₁≈V₂).
- Creato `tools/examples/anello-2-retrazione.json`: 3 keyframe autoriali,
  S1–S3, M1–M2, C1–C2 unformalized, T1–T2 con intendedEffect/hypothesis/
  prediction (P-A2.1), L1 LOCK funzionale, V1–V2 displacement, 2 annotazioni.
- Import verificato in browser: tutti gli oggetti caricati, vettori+LOCK+
  supinazione renderizzati nelle 3 viste.
- Limite emerso (registrato in wiki/02): legame stato↔keyframe implicito via
  `time` — `state.keyframeId` esplicito sarebbe meno ambiguo.

---

## R-015 — Correzioni S2 dalla lettura a freddo (3 fix, poi stop)

**Richiesta:** revisione esterna della bozza Anello 2 (sessione 2026-09-20):
tre ambiguità strutturali da correggere — (A) `state.keyframeId` esplicito;
(B) `M2.representationStatus: not_available` + reason (non inventare il
tronco); (C) LOCK: start/end = validità del vincolo + `associatedState`/`role`.
Poi: *"fermerei S2"* — il test ha trovato ambiguità reali senza inventare
teoria; prossimo passo = test esterno a freddo del JSON.
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- Editor: select `keyframeId` sugli stati, `representationStatus` sui
  movimenti, `associatedState`/`role` sui vincoli — tutto passa nel canonico.
- `anello-2-retrazione.json` v2: S1→KF1, S2→KF2, S3→KF3; M2 dichiarato fuori
  scope skeleton; L1 con associatedState S2 + role constrain-next-transition.
- Verificato: campi preservati nel round-trip export→import.

---

## R-016 — Lettura a freddo esterna del JSON (test semantico di S2)

**Richiesta:** protocollo rigido — *"consegnare solo il JSON; non spiegare
S, M, C, T, LOCK, V; chiedere all'esterno di ricostruire la sequenza
semantica, osservazioni, interpretazioni, ipotesi, elementi rappresentati
cinematicamente, elementi fuori scope, significato del LOCK, predizioni;
confrontare con il significato intenzionale."* Classificazione:
CORRETTO / AMBIGUO / ERRATO. *"La cosa più importante è non correggere il
lettore durante il test. Se interpreta male qualcosa, è evidenza che il
modello semantico non comunica abbastanza."* (2026-09-20)
**Data:** 2026-09-20
**Stato:** `fatta`
**Cosa è successo:**
- Tre lettori esterni via mw-ask (groq gpt-oss-120b, gemini-3.8-flash,
  openrouter/free; codex al usage-limit): solo JSON + domande, zero
  contesto, zero correzioni.
- Esiti documentati in `spikes/S2-COLD-READ-01.md`: nucleo semantico
  CORRETTO (sequenza, epistemica, ipotesi, LOCK, fuori-scope, predizioni).
- 8 ambiguità emerse — 4 sotto-specificazioni reali (unità/calibrazione,
  E1 supinazione non rappresentabile, KF2≡KF3 statico-vs-solidale, legenda
  epistemica assente), 2 aperture da mantenere (ruolo logico di C,
  relazione attesa V1~V2).
- S2 resta chiusa: nessuna modifica allo schema finché il Director non
  decide quali ambiguità meritano un campo.

---

## R-017 — Unità e calibrazione dichiarate in `meta`

**Richiesta:** *"aggiungerei in `meta` qualcosa del tipo `units:
{position:'px', time:'ms', calibration:'not-calibrated'}`. Non aggiungerei
ancora velocityUnit/accelerationUnit — sarebbero conseguenze, non proprietà
primitive. Non trasformerei px in una pseudo-unità fisica."* (2026-09-21,
decisione su esito cold-read)
**Data:** 2026-09-21
**Stato:** `fatta`
**Cosa è successo:**
- `buildCanonical()` emette `meta.units` di default; `meta` importato è
  preservato nel round-trip (merge shallow, `exportedAt` sempre aggiornato).
- Esempio Anello 2 aggiornato; verificato in browser.

## R-018 — Legenda epistemica e di provenance in `meta`

**Richiesta:** *"`epistemicLegend` + `provenanceLegend` in `meta`, non dentro
ogni oggetto. `authored` non significa `OSS`: epistemic e provenance sono due
assi diversi."* Motivazione: 1 lettore su 3 ha espanso IPO come "Initial
Proposal" e classificato i keyframe authored come OSS. (2026-09-21)
**Data:** 2026-09-21
**Stato:** `fatta`
**Cosa è successo:**
- `meta.epistemicLegend` (OSS/INT/IPO espansi) e `meta.provenanceLegend`
  (authored/measured) emessi di default e preservati in import.
- Esempio Anello 2 aggiornato; verificato in browser.

## R-019 — `representationStatus` esteso agli eventi

**Richiesta:** *"non inventerei un secondo meccanismo specifico per gli
eventi. Estenderei il concetto a proprietà semantica generale [...] Una cosa
può esistere nel modello semantico senza essere rappresentata
cinematicamente."* Caso trovato dal cold-read: E1 supinazione — OSS
dichiarato, non rappresentabile su aste punto-punto. Cautela: *"il test ha
trovato il buco, non ci ha ancora detto come riempirlo"* — niente tassonomia
traslazione/rotazione/orientamento ora. (2026-09-21)
**Data:** 2026-09-21
**Stato:** `fatta`
**Cosa è successo:**
- Eventi: `representationStatus` + `representationReason` passano nel
  canonico (export/import), emessi solo se presenti — niente UI dedicata.
- E1 nel JSON d'esempio: `not_available` +
  `axial-rotation-not-represented`. Round-trip verificato.
- **Restano aperti per design** (decisione Director): KF2≡KF3 (stessa
  configurazione ≠ nessun movimento), ruolo logico di C, relazione V1~V2,
  onset L1 dentro M1, terminologia LOCK nel meta.

---

## R-020 — P-A2.2 standalone con data-gate, S4 rinviato

**Richiesta:** *"Procedere con A, ma preceduta da una micro-fase di
estrazione/validazione dei landmark. Non farei subito S4 completo."*
Sequenza: capture msgpack → estrazione landmark braccio → validazione
qualità → P-A2.2 standalone → risultato INT + incertezza → solo dopo,
eventuale S4. Riformulazione della domanda: *"nel capture disponibile, il
modello segmentale adottato stima un momento d'inerzia diverso tra la
configurazione retratta e quella di riferimento?"* — `I_estimated`, non
`I_measured`. Richiesta stima Monte Carlo della sensibilità agli errori
landmark. Primo gate: spike `P-A2.2-DATA-01` (quali landmark/frame/fps/
coordinate/unità/confidence/missing; identificazione riproducibile della
configurazione retratta). C parallelo non-gate; C-02 deferito. P-A2.2 non
dimostra la funzione del LOCK: `I_retracted < I_ref` è circoscritto al
modello adottato. (2026-09-21)
**Data:** 2026-09-21
**Stato:** `in corso`
**Cosa è successo:**
- Spike `P-A2.2-DATA-01` completato (`spikes/P-A2.2-DATA-01.md`):
  capture = 33 landmark ML Kit x,y normalizzati + inFrameLikelihood
  (**nessuna profondità reale**), ~17fps, 5 reps senza gap.
- Configurazione retratta riproducibile (gomito sx <80° + oltre mediana,
  finestre ~0-10 guardia / ~30-45 retratta) su tutte le reps.
- Gate SUPERATO con caveat: stima planare di I con bias di proiezione
  dichiarato; `I_estimated` INT, non misura.
- P-A2.2 eseguito (`analysis/pa2_inertia.py`): mediana robusta su finestre
  rilevate da regola, Monte Carlo (N=2000) con sigma stimato dal jitter in
  guardia. Risultato (INT): I_braccio planare ~-50% in retratta, IC95%>0
  in tutte le reps; rep_003 conteneva un frame con landmark esploso —
  risolto passando da media a mediana.
- Esito registrato in wiki/03 con ambito dichiarato (I_estimated nel
  modello, non dimostra funzione LOCK).

---

## R-021 — Scheda Anelli 0+1 con OSS quantitativi dai capture

**Richiesta:** *"possiamo cominciare a lavorare sul primo anello della
catena cinetica?"* (2026-09-21) — ramo C della sequenza R-020, eseguito
perché i capture contengono già i landmark della parte bassa.
**Data:** 2026-09-21
**Stato:** `fatta`
**Cosa è successo:**
- Scheda 12-passi compilata in `wiki/02` per Anelli 0+1 con OSS da capture:
  sollevamento piede (~2% frame), salita bacino (~1-1.7%), flip del proxy
  pelvico `hips_dx` in tutte le reps.
- **Risultato nuovo:** flip pelvico e retrazione braccio sincroni a ±1
  frame in 5/5 reps — a 17fps l'ordine bacino↔braccio non è risolvibile.
  Registrato come predizione **P-A0.1** in `wiki/03` (richiede ≥100fps).
- Limite dichiarato: carico tallone→avampiede NON osservabile nei landmark
  (serve pressione/GRF).

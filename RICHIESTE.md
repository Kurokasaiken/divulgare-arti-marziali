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

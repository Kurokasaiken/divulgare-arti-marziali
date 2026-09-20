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

## R-003 — Evolvere biomech-editor verso la lavagna del modello

**Richiesta:** *"Intanto per studiare la teoria biomeccanica dobbiamo fare un
tool che indichi precisamente le cose e che possa anche dare informazioni precise
ad un agente AI per poterne discutere. L'idea di mostrarlo da più angolazioni
contemporaneamente è interessante. [...] poco alla volta dovremo fare un modello
di tutto il corpo, separatamente (fase per fase), ma per quello completo
potremmo partire dal mio progetto con motion capture."*
**Data:** 2026-09-20
**Stato:** `aperta`
**Desiderata:** v1 FROZEN — `.mw/desiderata.md`
**Cosa manca:** scelta della prima slice (import-dati vs authoring-semantico) e
piano di implementazione.

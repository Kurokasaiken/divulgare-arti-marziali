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

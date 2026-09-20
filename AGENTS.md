# Mind Weaver — Divulgare Arti Marziali

At the start of every session: read `CANON.md`, `RICHIESTE.md` and
`SESSION_HANDOFF.md` (if they exist). Then read `wiki/INDEX.md` and load only the
pages relevant to the task.

`RICHIESTE.md` holds the user's explicit requests, in their own words. Entries marked
`aperta` or `in corso` are committed work, not suggestions. You may challenge a
request and argue against it — you should, if you have reasons — but you may not
ignore it, silently reframe it, narrow it, or defer it. Changing an entry to
`ridotta`/`rinviata`/`ritirata` requires explicit human approval, same as `CANON.md`.

Before responding to anything consequential — architecture, dependencies, research
direction — read `CANON.md`. If a proposal contradicts a decision, say so before
proceeding.

Write to `CANON.md` only after explicit human approval ("approvato" or unambiguous
equivalent). After writing, report exactly what was added.

## Regola epistemica centrale

Ogni affermazione sul movimento porta un'etichetta:

- **OSS** — osservazione: ciò che si vede/misura (es. "il gomito si sposta
  posteriormente").
- **INT** — interpretazione: funzione meccanica attribuita all'osservazione.
- **IPO** — ipotesi: affermazione falsificabile da verificare con misure.

Mai presentare un'INT o un'IPO come OSS. Il dettaglio in
[`wiki/03-registro-ipotesi.md`](wiki/03-registro-ipotesi.md).

## Gerarchia del progetto

Il progetto è la **ricerca/formalizzazione del movimento**. Lo strumento visuale
("Motion Mechanics Lab") è ausiliario: serve a rendere il modello leggibile, non è
il progetto. Vedi [`wiki/06-strumento-visuale.md`](wiki/06-strumento-visuale.md).

**La UI non determina la teoria.** Se una condizione o relazione reale non è
rappresentabile bene nel formato dati attuale, si cambia il modello dati — non si
semplifica la teoria per adattarla all'editor. Livello ricerca (cosa è `C`) e
livello rappresentazione (come serializziamo `C`) non si invertono.

## Modalità lean

Struttura minima: niente `plans/`, `execution/`, skill o runtime finché un'esigenza
reale non li richiede. La conoscenza vive in `wiki/`; le decisioni in `CANON.md`;
le richieste in `RICHIESTE.md`.

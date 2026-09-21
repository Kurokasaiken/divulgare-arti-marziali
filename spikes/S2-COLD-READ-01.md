# S2-COLD-READ-01 — Lettura a freddo del JSON Anello 2

**Data:** 2026-09-20 · **Stato:** completata · **Tipo:** test di usabilità semantica (R-016)

## Protocollo

- Oggetto del test: `tools/examples/anello-2-retrazione.json` (versione post R-015).
- Ai lettori è stato consegnato **solo** il JSON + le domande di ricostruzione.
  Nessuna spiegazione di `S/M/C/T/LOCK/V`, nessun codice, nessuna conversazione
  precedente, nessuna correzione durante il test.
- Domande: (1) sequenza semantica; (2) osservazioni; (3) interpretazioni;
  (4) ipotesi; (5) elementi rappresentati cinematicamente vs dichiarati fuori
  scope; (6) significato del LOCK; (7) predizioni; (8) ambiguità.
- Lettori esterni (via `mw-ask`, contesto pulito):
  - **groq** `openai/gpt-oss-120b` — risposta completa;
  - **gemini** `gemini-3.8-flash` — completa (in due tranche, la prima troncata
    per limite token);
  - **openrouter** `openrouter/free` — quasi completa (troncata sul punto 8);
  - **codex** — non disponibile (usage limit fino al 2026-10-10).
- Risposte verbatim: `.mw/runs/cold-read-s2/{prompt,groq,gemini,gemini-2,openrouter}.txt`.

## Esiti per domanda

| # | Domanda | Esito | Note |
|---|---------|-------|------|
| 1 | Sequenza semantica | **CORRETTO** (3/3) | Tutti hanno ricostruito `S1→M1→C1→S2→M2→C2→S3` con i tempi corretti. |
| 2 | Osservazioni | **CORRETTO** (2/3) | groq e gemini: S1, S2, E1, A1. openrouter: **ERRATO** — ha classificato KF1–KF3 come OSS ignorando `epistemic:INT`+`provenance:authored`, e ha espanso `IPO` come "Initial Proposal". |
| 3 | Interpretazioni | **CORRETTO** (3/3) | Pose autoriali, M1, L1, V1 riconosciuti come scelte dell'autore. |
| 4 | Ipotesi | **CORRETTO** (3/3) | Tutti hanno letto T1/T2 come ipotesi, inclusa la distinzione "abilita ≠ causa". |
| 5 | Rappresentato vs fuori scope | **CORRETTO** (2/3) | groq/gemini: tronco/M2 correttamente letti come fuori scope. openrouter: **AMBIGUO** — ha elencato M2 sia come rappresentato sia come fuori scope (autocontraddizione). |
| 6 | Significato del LOCK | **CORRETTO** (3/3, con sfumatura) | Tutti: vincolo funzionale, non blocco articolare, prepara la transizione. openrouter ha aggiunto semantica di gate ("deve rimanere bloccato *prima* che avvenga T2") — leggero eccesso. |
| 7 | Predizioni | **CORRETTO** (3/3) | P-A2.1 e la predizione di T1 ricostruite come falsificabili da tutti. |

## Ambiguità emerse (il risultato utile del test)

1. **Unità e calibrazione** (groq + gemini) — `px` senza scala metrica, `ms`
   impliciti. Impedisce di derivare velocità/accelerazioni fisiche.
   *Sotto-specificazione reale.*
2. **E1 supinazione non rappresentabile geometricamente** (gemini) — i
   segmenti sono aste punto-punto: la rotazione assiale (rollio) non è
   esprimibile. E1 è un evento OSS **dichiarato ma non rappresentabile** —
   lo stesso buco che `representationStatus` ha chiuso per i movimenti, ma
   gli eventi non hanno quel campo. *Gap strutturale reale.*
3. **KF2 ≡ KF3** (gemini) — il braccio è identico a 300 e 600 ms: fermo nel
   mondo o solidale a un tronco in rotazione non modellato? Il modello non
   distingue le due letture. *Ambiguità reale.*
4. **Ruolo logico di C** (openrouter) — condizione necessaria? sufficiente?
   guardia o trigger? Il JSON non lo dice. *Coerente con C-02; da non
   risolvere prematuramente, ma da registrare.*
5. **Relazione attesa in V1~V2** (gemini, groq) — il confronto è ipotizzato
   ma non si dice quale relazione ci si aspetta (parallelismo, rapporto di
   magnitudo, fase). *Ipotesi sotto-specificata.*
6. **Onset di L1 a 200 ms < S2 a 300 ms** (groq) — il LOCK inizia dentro M1,
   prima dello stato a cui è `associatedState`. La nota dice che il vincolo
   può attraversare le transizioni, ma il lettore si aspettava l'attivazione
   a S2. Semantica dell'onset sotto-specificata (intenzionale nel modello:
   il vincolo emerge nella coda di M1).
7. **Legenda epistemica assente** (openrouter) — `IPO` letto come "Initial
   Proposal". groq e gemini l'hanno inferita dal contesto; un lettore su tre
   ha sbagliato. *Gap di auto-documentazione del formato.*
8. **"LOCK" nel meta vs `type: functional-lock`** (groq, openrouter) —
   terminologia colloquiale nel meta non legata formalmente all'oggetto L1.

## Errori del lettore (non difetti del modello)

- openrouter: KF1–KF3 classificati OSS (campi `epistemic`/`provenance`
  presenti ed espliciti); "KF3 = fine di M1" (KF3 appartiene a S3); M2
  elencato come rappresentato e come fuori scope.
- groq: "V2 non calcolabile senza ulteriori dati" — V2 è calcolabile dai
  keyframe come V1; resta però vero che la *relazione attesa* non è
  specificata (punto 5 sopra).

## Verdetto

Il nucleo semantico **comunica**: sequenza, struttura epistemica, ipotesi,
LOCK funzionale, fuori-scope e predizioni sono stati ricostruiti
correttamente dalla maggioranza dei lettori a freddo.

Il test ha prodotto **8 ambiguità**, di cui almeno 4 sono sotto-specificazioni
reali del linguaggio (unità/calibrazione, E1 non rappresentabile, KF2≡KF3,
legenda epistemica) e 2 sono aperture già note da mantenere aperte (ruolo
logico di C, V1~V2 come ipotesi da specificare solo quando si testa).

**Decisione sospesa:** nessuna modifica allo schema finché il Director non
decide quali ambiguità meritano un campo e quali restano "aperte per
design". S2 resta chiusa.

## Appendice — decisione del Director (2026-09-21)

| Ambiguità | Decisione | Implementazione |
|-----------|-----------|-----------------|
| unità/calibrazione | **CHIUSO** | `meta.units` + `calibration:'not-calibrated'` (R-017) |
| legenda epistemica | **CHIUSO** | `meta.epistemicLegend` + `provenanceLegend` (R-018) |
| E1 non rappresentabile | **CHIUSO** | `representationStatus`/`representationReason` esteso agli eventi (R-019) — senza tassonomia traslazione/rotazione/orientamento |
| KF2 ≡ KF3 | APERTO per design | stessa configurazione ≠ nessun movimento intervenuto |
| ruolo logico di C | APERTO per design | è la domanda scientifica di C-02 |
| relazione V1~V2 | APERTO per design | `≈` richiede una metrica da ricerca, non da schema |
| onset L1 dentro M1 | APERTO/documentato | il vincolo emerge nella coda di M1 — intenzionale |
| LOCK meta vs functional-lock | APERTO/documentato | terminologia colloquiale, non ambiguità bloccante |

S2 resta il benchmark congelato: queste sono richieste nuove generate dal
test, non correzioni retroattive del caso di studio.

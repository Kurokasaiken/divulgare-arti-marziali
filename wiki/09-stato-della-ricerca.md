# 09 — Stato della ricerca

> Pagina di orientamento: impedisce che il progetto diventi un accumulo di
> documentazione. Aggiornarla quando cambia ciò che sappiamo.
> Ultimo aggiornamento: 2026-09-20 (bootstrap).

## CONOSCIAMO (consolidato in letteratura — una fonte per affermazione)

- Il choku-zuki studiato da Martins et al. si completa in ~400 ms con pattern
  cinematici/EMG specifici dell'arto superiore (karateka portoghesi).
  *[choku-zuki EMG study — vedi `08`]*
- Il sequenziamento prossimale-distale dei segmenti in azioni di striking è
  documentato nella letteratura generale. *[letteratura striking — vedi `08`]*
- In pugni studiati con force plate, le GRF degli arti inferiori sono misurabili
  e correlano con le caratteristiche del colpo. *[Frontiers Physiol. 2022 — vedi `08`]*
- Sequenziamento simultaneo vs consecutivo dei segmenti è già studiato (Fuchs
  2018, Wing Chun): nessuno dei due universalmente superiore. *[Fuchs 2018]*
- Meccanica di base: impulso `J = ∫F dt = Δp`, momento d'inerzia dipendente dalla
  distribuzione della massa, coppie di forze. *[meccanica classica]*

### Effective mass — trattare con cautela

Costrutto quantitativo usato nella letteratura sullo striking (misurato come
forza-picco / accelerazione del pugno all'impatto), **ma la sua definizione e
interpretazione dipendono dal metodo di misura ed è stata oggetto di discussione**
(Turner 2015). Non è "X kg di massa nel pugno". Non costruire la teoria su
questa variabile come se fosse concettualmente semplice.

## ABBIAMO OSSERVATO

Provenienza dichiarata per ogni osservazione: `[video]` = pose-estimation
(~17fps, landmark), `[empirico]` = prove/pratica del Director (percepito, non
misurato).

- `[video]` L'estensione dell'arto superiore inizia prima che la configurazione
  della parte inferiore sia completa → sovrapposizione temporale (cinematica).
- `[video]` La parte inferiore continua a modificarsi mentre l'arto superiore è
  già in movimento.
- `[video]` Retrazione + supinazione del braccio sinistro come evento combinato,
  non sequenziale.
- `[video]` Mano sinistra: aperta → chiusura rapida quando la traiettoria è
  stabile.
- `[video]` Vettore finale del pugno ≈ direzione del vettore di retrazione del
  gomito (V₁ ≈ V₂ — osservazione geometrica, da verificare su dati).
- `[empirico]` Configurazione finale del braccio che trasmette carico con **poca
  attività muscolare percepita** (prova contro parete — sensazione, non misura).

## ABBIAMO INTERPRETATO

- Il piede sinistro come vincolo attivo che abilita la rotazione, non semplice
  appoggio.
- Il tronco come struttura dinamicamente organizzata (né rigida né rilassata).
- "LOCK" come configurazione terminale funzionale, non blocco articolare.
- "Ultimo momento utile" come condizione geometrica (conservare il DOF allontana
  dalla traiettoria) — formulazione ancora intuitiva, da formalizzare.
- Destabilizzazione come possibile costo sullo stato post-azione (caso lastra).

## IPOTIZZIAMO (registro completo in `03-registro-ipotesi.md`)

- H1–H6 + force couple contralaterale sul bacino + V₁≈V₂ + configurazione
  strutturale finale.

## NON SAPPIAMO

- **Se `Cᵢ` è nuovo o una rappresentazione di qualcosa che la letteratura chiama
  già in altro modo** — *risposta preliminare dello spike `C-CONDITION-01`:*
  la **forma** esiste già (initiation set / termination condition, Sutton et
  al. 1999; guard condition; entry-state conditions nei grafi di motion
  primitives). Resta aperto il **contenuto** (quali variabili misurabili
  definiscono la regione nel gesto umano) e la semantica forward-looking
  (utilità rispetto allo stato post-azione).
- Quali variabili devono assumere quali valori perché `C` sia vera — `C` resta
  "quando è pronto" finché non diventa un predicato su quantità misurabili.
- Quale variabile determina il cambio di strategia ("ultimo momento utile") —
  potrebbe non essere una singola variabile ma una **frontiera**, e forse non
  nello spazio articolare ma nello **spazio delle variabili di task**
  (ipotesi UCM — `spikes/C-CONDITION-01.md`, rev. avversariale §4).
- **Se le transizioni intra-gesto siano eventi discreti o emergano da
  controllo continuo** — problema di identificabilità: continuo / continuo+
  switching / gerarchico possono produrre la stessa cinematica. Discreto
  apparente ≠ discreto nel controller (submovements, intermittency).
  → `spikes/C-02-continuous-vs-triggered.md`
- Quanto il braccio compatto contribuisca causalmente alla velocità di rotazione
  (momento d'inerzia ridotto ≠ rotazione accelerata dimostrata).
- Se la forza del force couple contralaterale esiste e quanto contribuisce.

## DOBBIAMO VERIFICARE

- Mapping completo dei nostri concetti su letteratura motor control
  (Bernstein, Newell, Todorov & Jordan, Latash) — iniziato, non finito.
- Fuchs 2018 in dettaglio: la nostra sovrapposizione coincide con SSM o è
  qualcosa di più generale?
- Video ad alta frequenza per i timing rapidi (chiusura mano, supinazione).
- GRF + cinematica 3D per force couple e contributo arti inferiori.
- Misura di effective mass / impulso su varianti della tecnica.

## PROSSIMA DOMANDA

> **La forma di `C` è nota (initiation set / guard condition). Le domande
> aperte ora sono due: (a) quali variabili misurabili definiscono la regione
> di commutazione — e in quale spazio (articolare o variabili di task)?;
> (b) il modello `C` aggiunge capacità esplicativa rispetto a un modello
> continuo equivalente — esiste una frontiera predittiva nel gesto reale?**

Ipotesi di lavoro (formulazione difendibile, da rev. avversariale): *una
rappresentazione tramite transizioni condizionate dallo stato può essere
utile come livello descrittivo; resta da determinare se corrispondano a
meccanismi discreti o emergano da controllo continuo.*

Spike: `C-CONDITION-01` (verdetto in) → `C-02` (continuo vs triggered,
**aperto** — la domanda empirica centrale). Restano da verificare le priors
motor-control sulle fonti primarie (Bernstein, Newell, Latash).

**Il collo di bottiglia ora è scientifico, non software.** Non aggiungere pagine
o feature: la prossima attività è lo spike C-02.

> Nota di direzione (R-011, 2026-09-20): l'obiettivo primario è la
> **spiegazione rigorosa della tecnica** (scheda di analisi in `04`), non la
> novità di `C`. La questione discreto/continuo resta aperta ma subordinata:
> serve a scrivere correttamente le affermazioni causali, non a rivendicare
> una teoria.

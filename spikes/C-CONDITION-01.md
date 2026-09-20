# SPIKE C-CONDITION-01 — What exactly is C?

**Stato:** `in corso`
**Data apertura:** 2026-09-20
**Origine:** revisione esterna sul repository (punto 17 + raccomandazione
finale): *"il prossimo lavoro non dovrebbe essere aggiungere S2 al tool.
Dovrebbe essere SPIKE SCIENTIFICO 01 — What exactly is C?"*

## Perché questo spike

Il modello `S --M--> C --> S` ha un debito dichiarato: `C` ("condizione
sufficiente") non ha ancora una definizione operativa misurabile. Prima di
implementare predicati nel JSON (PLAN-001 S5b), bisogna capire **se** `C` è
rappresentabile come predicato — e se il concetto esiste già in letteratura
sotto un altro nome.

## Le tre domande

### Q1 — Fuchs 2018 / simultaneous motion sequencing

*Quanto del nostro modello è già contenuto nella simultaneous motion
sequencing?*

Fonte: Fuchs, Lindinger, Schwameder — *"Kinematic analysis of proximal-to-distal
and simultaneous motion sequencing of straight punches"* (Journal of Sports
Sciences, 2018; DOI 10.1080/14763141.2017.1365928). 4 praticanti esperti di
Practical Wing Chun, 20 pugni per concetto, Vicon 8 camere a 250 fps, Visual3D.
**Nota:** compilato dall'abstract/risultati pubblici — la lettura del full text
può raffinare le celle `?`.

Fatti rilevanti (OSS dalla fonte):

- CSM e SSM sono due **concetti di coordinazione osservati**: entrambi mostrano
  sequenziamento prossimale-distale delle velocità articolari massime; in SSM è
  accoppiato a **iniziazione simultanea** dei segmenti.
- Differenze misurate: momento del bacino e backswing di spalla/gomito (CSM);
  ruolo della spalla (SSM); ROM, timing, velocità angolari → differenze
  significative (p<0.05) in velocità del pugno al contatto, tempo di
  esecuzione, distanza, spostamento orizzontale del CoM.
- Gli autori stessi concludono che l'applicazione appropriata dei due concetti
  **dipende da setting ambientale, requisiti situazionali e stile individuale**
  — cioè il risultato è task-dipendente (coerente col nostro TASK).

Tabella di confronto:

| Domanda | Fuchs 2018 (SSM/CSM) | Nostro modello |
|---|---|---|
| Quando parte il segmento successivo? | SSM: simultaneamente; CSM: dopo il precedente | quando C è soddisfatta |
| Serve completamento del precedente? | SSM: no; CSM: sì (consecutivo) | no — ma serve C |
| Timing fisso? | pattern cinematico osservato, descritto statisticamente | dovrebbe essere stato-dipendente |
| Condizione geometrica esplicita? | **no** — descrizione cinematica, nessuna condizione di innesco | centrale |
| Stato successivo nel modello? | non modellato (misurano spostamento CoM, ma non come vincolo di task) | centrale |
| Adattamento a perturbazioni? | non trattato | centrale |
| Formalizzazione come transizione? | no — i concetti sono *pattern di coordinazione*, non transizioni con innesco | centrale |

**Primo risultato:** la sovrapposizione è reale ma parziale. SSM copre
"l'inizio non è seriale", ma **non** "l'inizio è condizionato da una condizione
sufficiente sullo stato". Fuchs caratterizza *come* i due pattern differiscono
cinematicamente; non modella *quando* una transizione debba iniziare in funzione
dello stato corrente. La questione novità su `C` **non è chiusa** da Fuchs —
resta aperta, con sovrapposizione parziale documentata.

### Q2 — Motor control

*`C` corrisponde a un concetto già esistente sotto un altro nome?*

Candidati da confrontare (in `wiki/08-letteratura-biomeccanica.md`):

- Bernstein — DOF problem
- Newell — task constraints
- Todorov & Jordan — optimal feedback control, minimal intervention
- Latash — motor abundance, uncontrolled manifold
- movement primitives
- anticipatory postural adjustments (APA)

Per ciascuno: il concetto copre l'innesco della transizione? la condizione
sufficiente? lo stato post-azione nella funzione obiettivo?

**Mappatura preliminare** (priors da verificare contro le fonti primarie —
non letture complete):

| Concetto | Copre | Relazione candidata con `C` | Stato |
|---|---|---|---|
| Bernstein (DOF problem) | strategia di gestione dei gradi di libertà | parente del working principle (freeze/free DOF), non dell'innesco | da verificare |
| Newell (constraints) | vincoli organismo/task/ambiente | inquadra il nostro TASK, non `C` | da verificare |
| Todorov & Jordan (OFC) | correzioni solo quando task-rilevanti | feedback continuo su costo — `C` potrebbe mappare sulla legge di feedback, non su condizione discreta | da verificare |
| Latash (UCM/motor abundance) | variabilità nelle direzioni non rilevanti | spiega "preservare DOF utili", non l'innesco di transizione | da verificare |
| Movement primitives | transizioni spesso basate su tempo/fase | alcuni modelli ammettono trigger di fase — vicino a `C` | da verificare |
| APA | preparazione anticipata dello stato | copre il nostro principio `t−Δt` (preparazione della configurazione successiva), più che `C` | da verificare |

Osservazione preliminare: **nessun candidato noto combina da solo** "innesco
stato-dipendente" + "condizione geometrica sufficiente" + "stato post-azione
nell'obiettivo". Ma ogni componente ha un parente — `C` potrebbe risultare una
*combinazione* di concetti noti, che è già una risposta utile alla domanda
centrale.

### Q3 — Optimal / hybrid control

*Una switching boundary è una formalizzazione appropriata di `C`, oppure stiamo
importando una metafora matematica che non descrive il controllo umano?`

Forme candidate per `C`:

- **Predicato**: congiunzione di condizioni misurabili
  (`posizione ∈ regione AND velocità > soglia AND ...`)
- **Switching boundary**: superficie nello spazio degli stati che separa
  "continuare la transizione A è utile" da "iniziare B è utile" —
  `f(stato, velocità, target, vincoli, tempo) = 0`

La seconda è più vicina a controllo/ottimizzazione, ma non abbiamo ancora
dimostrato che il sistema motorio umano funzioni così. È una struttura
ipotetica.

**Nota preliminare Q3:** in letteratura di controllo ibrido esiste già il
formalismo della **guard condition** (automata ibridi: una transizione di modo
scatta quando lo stato entra in un insieme guardia). `C` mapperebbe quasi
esattamente su quel concetto — il che risponderebbe parzialmente a Q2: `C` come
*forma* esiste già (guardia di modo in sistemi ibridi). La questione aperta non
è la forma ma il **contenuto**: quali variabili/stati definiscono la guardia nel
controllo motorio umano, e se l'evidenza supporta switch discreti invece di
feedback continuo (OFC suggerirebbe il secondo per correzioni intra-movimento;
eventi discreti come il contatto giustificano invece cambi di modo).

## Regola dello spike

La risposta a "cosa è C" viene dalla letteratura e dai dati, non dal formato
JSON dell'editor. L'output di questo spike è una **definizione candidata** di
`C` con: forma (predicato / frontiera / altro), variabili coinvolte,
provenienza epistemica di ogni componente, e confronto esplicito con i nomi
esistenti in letteratura.

## Output

- [x] tabella Fuchs compilata con citazioni (abstract; full-text può raffinare)
- [ ] mapping `C` ↔ concetti motor-control (stato per ciascuno)
- [ ] giudizio su predicato vs switching boundary
- [ ] definizione candidata di `C` (se emerge) → aggiorna `wiki/01`, `wiki/09`
- [ ] esito: `C` nuovo / combinazione di noti / già coperto → aggiorna `wiki/08`

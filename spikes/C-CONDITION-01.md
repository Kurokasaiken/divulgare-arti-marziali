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

**Mappatura** (primi due riquadri verificati su fonte; gli altri restano priors
da leggere nelle fonti primarie):

| Concetto | Copre | Relazione con `C` | Stato |
|---|---|---|---|
| **Options framework** — Sutton, Precup, Singh 1999 (*"Between MDPs and semi-MDPs"*, AIJ; anche Sutton et al. 1998 *"Improved Switching among Temporally Abstract Actions"*) | azioni temporalmente estese con `⟨I, π, β⟩`: initiation set `I ⊆ S`, policy π, termination condition β(s) | **`C` mappa quasi esattamente**: l'opzione successiva è disponibile quando `s ∈ I`; il movimento corrente termina quando `β(s)` scatta. `S→M→C→S` ≈ catena di opzioni | **verificato su fonte** |
| **Transition conditions tra motion primitives** — arXiv:2106.10310 (*dynamic-state-aware transitions*, robotica) | formalizza transizioni A→B tra primitive dinamiche: la transizione è disponibile quando il flusso di A raggiunge l'insieme d'ingresso `S_B` di B; Class 1 (sempre) vs Class 2 (solo in certi tempi/stati) | la "Class 2 transition" è quasi letteralmente la nostra `C`: transitabile solo quando lo stato entra nella regione giusta | **verificato su fonte** |
| Todorov & Jordan 2002 — OFC, minimal intervention (Nature Neurosci.) | feedback continuo `u=L(x)`; correzioni solo quando rilevanti al task; "discrete coordination modes emerge naturally" | OFC **non** usa condizioni discrete: il controllo è una legge continua sullo stato. `C` come trigger discreto non è il formalismo OFC — ma il minimal-intervention copre bene il nostro "preserva DOF finché utile" | **verificato su fonte** |
| Bernstein (DOF problem) | strategia di gestione dei gradi di libertà (freeze/free) | parente del working principle, non dell'innesco | prior |
| Newell (constraints) | vincoli organismo/task/ambiente | inquadra TASK, non `C` | prior |
| Latash (UCM/motor abundance) | variabilità nelle direzioni non rilevanti al task | spiega "preserva DOF utili", non l'innesco | prior |
| APA (Belen'kii 1967; Latash; ASAs) | preparazione feedforward dello stato posturale prima dell'azione | copre il nostro principio `t−Δt` (la configurazione successiva si prepara prima), non `C` come trigger | **verificato su fonte** (concetto; applicazione al pugno da verificare) |

**Risultato Q2:** la *forma* di `C` **esiste già con nomi precisi**:
*initiation set* / *termination condition* (options framework), *guard
condition* (automata ibridi), *entry-state/transition conditions* (grafi di
motion primitives). Quello che non risulta dalla prima mappatura è una fonte
che applichi questa forma **alla coordinazione intra-movimento nel gesto
umano** (i lavori su transizioni tra primitive sono in robotica/controllo, non
in motor control sperimentale dello striking).

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

**Risultato Q3 (preliminare ma fondato):** la switching boundary **non è una
metafora importata a caso** — è la forma standard con cui la letteratura
formalizza esattamente questo tipo di condizione:

- automata ibridi → *guard set*;
- options framework → *initiation set* `I ⊆ S` e *termination condition* `β(s)`;
- grafi di motion primitives → *entry-state conditions* (transizione Class 2).

Quindi `C` va rappresentata come **regione/frontiera nello spazio degli stati**
(la forma B della sezione precedente), coerente con tutti i formalismi
esistenti. La questione che resta scientificamente aperta non è la forma ma il
**contenuto e l'evidenza**:

1. quali variabili misurabili definiscono la regione in un gesto reale;
2. se le transizioni intra-gesto nel sistema motorio umano siano davvero
   guard-triggered (switch discreti) o emergano da feedback continuo (OFC
   suggerirebbe il secondo; la letteratura su sequencing/chunking il primo);
3. se il nostro "utile per la transizione successiva" (forward-looking, include
   lo stato post-azione) sia coperto da `I`/`β` standard o richieda qualcosa di
   più (i formalismi esistenti definiscono *quando* si può transitare, non
   *perché è utile farlo* — la funzione obiettivo con post-action state resta
   il candidato distintivo).

**Test di contestabilità (da review esterna):** il formato JSON del modello è
sufficiente se un'AI che lo legge può obiettare *"C1 è descritta come
sufficiente per M2, ma dai dati non risulta dipendenza causale — potrebbe
essere semplice sovrapposizione temporale"*. Se il documento permette solo di
descrivere e non di contestare, manca lo strato epistemico-causale
(intended_effect / hypothesis / evidence / status / prediction).

## Regola dello spike

La risposta a "cosa è C" viene dalla letteratura e dai dati, non dal formato
JSON dell'editor. L'output di questo spike è una **definizione candidata** di
`C` con: forma (predicato / frontiera / altro), variabili coinvolte,
provenienza epistemica di ogni componente, e confronto esplicito con i nomi
esistenti in letteratura.

## Verdetto provvisorio (2026-09-20)

> **`C` come forma è già coperto dalla letteratura** — initiation set /
> termination condition (options framework), guard condition (sistemi ibridi),
> entry-state condition (grafi di motion primitives). Dichiararlo "nuovo" sarebbe
> sbagliato.
>
> **Cosa resta potenzialmente distintivo** (da verificare, non da rivendicare):
>
> 1. l'applicazione di questa forma alla **coordinazione intra-gesto nel
>    movimento umano** — le formalizzazioni trovate sono in RL/robotica, non in
>    motor control sperimentale sullo striking;
> 2. la semantica **forward-looking**: `C` non è solo "quando posso passare" ma
>    "quando passare è utile *in funzione dello stato successivo e dello stato
>    post-azione*". I formalismi esistenti definiscono disponibilità, non
>    utilità rispetto al seguito — questo potrebbe essere il contributo del
>    modello, se regge.
>
> La risposta onesta alla domanda centrale è quindi: **combinazione di concetti
> noti, con un possibile nucleo distintivo piccolo e ancora da dimostrare** —
> esattamente l'esito che il progetto cercava di verificare.

## Output

- [x] tabella Fuchs compilata con citazioni (abstract; full-text può raffinare)
- [x] mapping `C` ↔ concetti motor-control (stato per ciascuno) — vedi tabella
- [x] giudizio su predicato vs switching boundary → **regione/frontiera nello
  spazio degli stati** (forma standard: guard set / initiation set)
- [ ] definizione candidata di `C` (forma ora chiara; mancano le **variabili**
  — contenuto della regione) → da aggiornare `wiki/01`, `wiki/09`
- [x] esito: `C` nuovo / combinazione di noti / già coperto → **combinazione di
  noti + nucleo distintivo ipotetico** (semantica forward-looking su
  post-action state) → aggiornare `wiki/08`

## Revisione avversariale (esterna, 2026-09-20)

Il verdetto regge ma va raffinato su cinque punti.

### 1. Tre modelli concorrenti, stessa cinematica

```
MODELLO A — controllo continuo
───────────────────────────────>   la "fase" emerge; non esiste switch

MODELLO B — controllo continuo + switching
─────────────────────┐
                     └──────────>   C(s) innesca il cambio di politica

MODELLO C — politica gerarchica (options)
─── option A ─── C ─── option B ───
```

**Dal solo video cinematico A, B e C possono apparire identici.** Questo è il
problema di identificabilità — probabilmente la difficoltà scientifica
centrale del progetto in questa fase.

### 2. Discreto apparente ≠ discreto nel controller

- Letteratura sui **submovements** nel reaching: il movimento come somma di
  componenti sovrapposte, con nuove componenti innescate da informazioni
  cinematiche del movimento in corso — vicino alla nostra osservazione
  "A continua + B inizia". Ma gli stessi autori sottolineano che la
  decomposizione è un modello *analitico*, non la prova che il sistema
  nervoso rappresenti il movimento come submovements.
- Letteratura sulla **movement intermittency**: fenomeni apparentemente
  discreti possono emergere da feedback continuo con ritardi, senza eventi
  discreti nel controller.

**Regola (da mantenere):** non assumere che una decomposizione analitica del
movimento dimostri un'architettura discreta del controllo motorio.

### 3. Formulazione difendibile dell'ipotesi

Non: *"il movimento umano è composto da transizioni guard-triggered"*
(troppo forte). Ma:

> Una rappresentazione del movimento umano tramite transizioni condizionate
> dallo stato può essere utile come livello descrittivo; resta da determinare
> se tali transizioni corrispondano a meccanismi discreti di controllo oppure
> emergano da dinamiche di controllo continuo.

Questo rende il progetto **testabile**, non più debole.

### 4. `C` nello spazio delle variabili di task (UCM / Latash)

`C` potrebbe non essere una frontiera nello spazio degli stati corporei, ma
nello **spazio delle variabili rilevanti per il compito**:

```
spazio articolare → spazio configurazioni → spazio variabili di task → C?
```

Si collega a UCM / motor abundance: conta non la configurazione articolare
specifica, ma se una variazione modifica una variabile di performance
rilevante. Direzione potenzialmente più promettente della soglia geometrica
— da includere nel mapping Latash.

### 5. La domanda scientifica principale emersa

> **Il modello `C` aggiunge capacità esplicativa rispetto a un modello
> continuo equivalente?**

Test sperimentale candidato: su molte esecuzioni con condizioni iniziali
diverse (`s₁→t₁`, `s₂→t₂`, …), esiste una **frontiera predittiva** — la
posizione della transizione è predetta da variabili di stato *prima* che B
inizi? Se il tempo di transizione è solo una funzione continua dello stato
senza separazione significativa, la guardia è una discretizzazione utile, non
un meccanismo. **Entrambi gli esiti sarebbero scientificamente interessanti.**

→ Spike successivo: `spikes/C-02-continuous-vs-triggered.md`.

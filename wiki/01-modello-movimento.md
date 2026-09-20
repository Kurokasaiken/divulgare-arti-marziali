# 01 — Il modello del movimento

## Unità di analisi: la transizione condizionata

Non la "fase" classica. Il modello non è:

```
fase 1 → finisce → fase 2 → finisce → fase 3
```

ma:

```
STATO
  ↓
MOVIMENTO
  ↓
CONDIZIONE SUFFICIENTE raggiunta
  ↓
NUOVA CONFIGURAZIONE / VINCOLO
  ↓
MOVIMENTO SUCCESSIVO
  ↓
NUOVA CONFIGURAZIONE
```

con **sovrapposizione temporale**:

```
Movimento A ────────────────
              └── Movimento B ─────────
                         └── Movimento C ─────
```

Una nuova transizione può iniziare quando è stata raggiunta la **condizione
sufficiente** che la rende utile, anche se il movimento precedente è ancora in
corso. Questo è il cardine del modello.

### Notazione minima

```
S₀ ──M₁──▶ C₁ ──▶ S₁ ──M₂──▶ C₂ ──▶ S₂ ──M₃──▶ ...
```

- `Sᵢ` = stato del sistema (postura, configurazione, equilibrio)
- `Mᵢ` = movimento in corso
- `Cᵢ` = condizione sufficiente: lo stato minimo che rende utile avviare la
  transizione successiva

**Debito aperto:** "condizione sufficiente raggiunta" non ha ancora una
definizione operativa misurabile. Finché non la diamo, lo schema è una metafora
utile, non un modello.

Il salto necessario: `C` vera quando quali **proprietà misurabili** soddisfano
quali **condizioni**? Forma candidata (esempio, non la formula corretta):

```
C₁ = posizione_mano ∈ regione X
     AND errore_traiettoria < ε
     AND velocità_spalla > soglia
     AND configurazione_tronco ∈ regione R
```

E attenzione: `C` potrebbe non essere una soglia singola ma una **frontiera
nello spazio degli stati** (switching boundary) — una superficie che separa
"continuare questa transizione è utile" da "passare alla successiva è utile".
Vale la pena esplorare questa forma prima di cercare una variabile scalare.
La definizione va confrontata prima con la letteratura (switching conditions in
optimal control?) — vedi `08-letteratura-biomeccanica.md`.

## Il principio di lavoro sui gradi di libertà

> **Stato: working principle, non principio scientifico.** È una nostra
> formulazione concettuale. Potrebbe essere una buona sintesi di concetti già
> presenti (Bernstein DOF problem, motor abundance, optimal control, minimal
> intervention) oppure contenere qualcosa di distintivo — **non lo sappiamo
> ancora**. Non promuoverlo a "principio" prima del mapping in
> `08-letteratura-biomeccanica.md`.

Formulazione corrente:

> Ogni configurazione organizza il sistema in modo da massimizzare il contributo
> utile alla transizione successiva, rispettando i vincoli del compito e
> preservando i gradi di libertà finché rimangono utili.

In forma operativa:

> **Mantieni un grado di libertà finché produce vantaggio. Quando continuare a
> usarlo diventa controproducente, transita rapidamente verso la configurazione
> successiva.**

## Il principio temporale (anticipazione)

> Se una configurazione deve essere pronta al tempo `t` e richiede `Δt` per
> essere costruita, il suo inizio deve avvenire a `t − Δt`.

Conseguenza: azioni apparentemente "anticipate" non sono errori di
sincronizzazione, ma **preparazione temporale necessaria** della configurazione
successiva. È il motivo per cui si analizzano le transizioni, non i fotogrammi
finali.

## Il vincolo è funzionale, non articolare

"LOCK" non significa articolazione fisicamente bloccata. Significa
**configurazione terminale funzionale**: il sistema ha raggiunto uno stato in cui
continuare a usare quel grado di libertà non produce più il vantaggio precedente.
Quella configurazione diventa un **vincolo funzionale** per la transizione
successiva.

## Il compito (TASK) è parte del modello

Non esiste un pugno ottimale in assoluto: dipende dal compito. Ogni analisi va
ancorata a una struttura esplicita:

```
TASK
 ├── desired output          (es. trasferire impulso, raggiungere posizione)
 ├── target interaction      (percussione breve / spinta prolungata / ...)
 ├── temporal constraints    (tempo disponibile, sequenza richiesta dopo)
 ├── post-action state       (configurazione richiesta dopo l'interazione)
 └── allowable perturbation  (quanta destabilizzazione è accettabile)
```

Questo rende rigorosa la definizione "output utile sotto vincoli": i vincoli
non sono solo meccanici, includono il compito.

## Il movimento modifica lo stato successivo

Modello ingenuo:

```
input → movimento → output
```

Modello del progetto:

```
STATO → MOVIMENTO → NUOVO STATO → VINCOLO → NUOVO MOVIMENTO → NUOVO STATO
```

Il risultato di un movimento **modifica le condizioni** in cui avverrà il
movimento successivo. La configurazione finale di una fase è parte del problema,
non semplicemente la fine della fase.

### Lo stato post-azione è un output del modello

Non `movimento → risultato`, ma:

```
movimento → interazione → risultato + stato post-azione
```

Due strategie possono produrre **lo stesso output immediato** lasciando il corpo
in configurazioni diverse — e quella differenza è parte di ciò che il modello
deve valutare (es. il caso lastra: "cadere" nel colpo vs conservare la postura).
Lo stato post-azione è quindi un argomento della funzione obiettivo, non un
dettaglio.

## La "catena" ridefinita

Non semplicemente `gambe → bacino → tronco → spalla → braccio → pugno`, ma:

> una successione coordinata di configurazioni e trasferimenti in cui ogni
> elemento modifica le condizioni del successivo.

Questo spiega perché un segmento può iniziare prima che il precedente abbia
terminato, perché un segmento può diventare temporaneamente un vincolo, e perché
una parte può conservare un grado di libertà mentre un'altra cambia
configurazione.

## Output utile sotto vincoli, non massima forza

L'output desiderato va massimizzato **sotto vincoli** sullo stato del sistema e
sullo stato richiesto dopo l'interazione.

### Massa efficace

La *effective mass* è un concetto biomeccanico reale: la **massa equivalente
associata alla risposta dinamica del sistema** nell'interazione — non "quanta
massa del corpo viene trasferita nel bersaglio". Si collega a impulso e quantità
di moto:

```
J = ∫ F(t) dt = Δp
```

Forza, durata, profilo forza-tempo e variazione di quantità di moto sono legati.
La durata da sola non definisce un colpo: la differenza tra percussione rapida e
spinta prolungata va descritta attraverso l'interazione forza-tempo completa e il
comportamento del sistema.

### Stabilità come variabile, non come massimo

La destabilizzazione può essere risorsa o costo, a seconda del compito.

**Caso lastra (esempio del Director):** si può aumentare la massa efficace
"cadendo" nel colpo — ma si perde la configurazione posturale. Ottenere lo stesso
risultato senza perdere la postura è una soluzione con una proprietà diversa e
più interessante: conserva lo stato successivo.

Formulazioni candidate di ricerca (non termini stabiliti):
*stability-preserving transfer*, *postural cost of transfer* → **output sotto
vincolo dello stato posturale**, invece di semplice massimizzazione della forza.

## Modello ideale vs esecuzione reale

Il modello ideale definisce vincoli, relazioni, condizioni, traiettorie e timing.
L'esecuzione reale — un gesto allenato migliaia di volte — può partire da
configurazioni non perfette e trovare una soluzione compatibile: il modello non è
una traiettoria rigida, ma un **programma motorio che generalizza**.

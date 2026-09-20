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

## Il principio dei gradi di libertà

Formulazione corrente (da verificare contro la letteratura, non ancora un nome
scientifico stabilito):

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

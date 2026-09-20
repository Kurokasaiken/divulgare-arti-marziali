# 02 — Anatomia del pugno: scomposizione per anelli

> **Attenzione epistemica.** Questa è **la decomposizione proposta dal progetto
> per poter studiare il pugno** — non "la biomeccanica del pugno". È la nostra
> ipotesi corrente di organizzazione del movimento, da verificare. Un lettore
> esterno non deve interpretarla come descrizione biomeccanica stabilita.
>
> "Anello" è la **nostra unità analitica** — un segmento della catena di
> configurazioni scelto per comodità di studio. Non è una categoria anatomica o
> biomeccanica riconosciuta.
>
> Ogni affermazione porta il suo livello: **OSS** osservazione, **INT**
> interpretazione, **IPO** ipotesi.

Struttura di lavoro (gli "anelli" non sono rigidamente sequenziali — vedi
`01-modello-movimento.md`):

> **Nota di rappresentazione:** la lista 0–6 rischia di essere *letta* come
> sequenza anatomica anche se non lo è. Alla prossima revisione valutare di
> trasformare la rappresentazione principale da "anelli del pugno" a **rete di
> transizioni del pugno** (nodi = configurazioni, archi = movimenti condizionati
> che possono sovrapporsi), con gli anelli come viste analitiche sulla rete.
> Non urgente — è il passo concettuale successivo già segnato.

```
0. regolazione distanza / spostamento del baricentro
1. ancoraggio piede sinistro
2. retrazione braccio sinistro → configurazione terminale
3. organizzazione bacino e tronco
4. avanzamento della spalla destra
5. rilascio/accelerazione finale della mano destra
6. configurazione strutturale finale / interazione
```

Per ogni anello si descrive: stato iniziale · movimento · traiettoria · gradi di
libertà · evento di transizione · configurazione finale · vincolo prodotto ·
relazione con l'anello successivo.

---

## Anello 0 — Distanza / spostamento

Quando la distanza lo permette, un piccolo passo — più precisamente **una modifica
della configurazione e dell'equilibrio del sistema** per portarsi nella condizione
spaziale necessaria al movimento successivo. Non necessariamente un "passo
avanti". (INT)

Elementi osservati nell'esecuzione (OSS):

- il piede sinistro si solleva;
- atterra con il tallone;
- il carico passa fortemente verso l'avampiede;
- la gamba si estende leggermente;
- il bacino sale;
- la parte sinistra del bacino viene spinta posteriormente.

La funzione meccanica di ciascun elemento va ancora separata tra osservazione,
funzione ipotizzata e verifica.

## Anello 1 — Piede sinistro / base

Il movimento del braccio sinistro **non è indipendente** dall'ancoraggio della
parte anteriore del corpo. (INT)

```
piede sinistro → gamba → bacino → tronco → arto superiore
```

Il piede non è semplicemente "appoggiato": diventa parte del sistema che permette
di generare forze, vincolare il corpo, controllare il movimento del bacino e
fornire una base alla transizione successiva. (INT)

La quantificazione del contributo alla rotazione richiede GRF e cinematica 3D.
(IPO, non verificata con i dati attuali)

## Anello 2 — Braccio sinistro

### Traiettoria del gomito

Partenza da guardia; il braccio viene portato posteriormente. Il gomito segue una
traiettoria approssimativamente **arcuata** (OSS — da rappresentare come arco
punto-iniziale → punto-finale; la funzione esatta dell'arco è INT).

### Retrazione + supinazione: evento combinato

Non `retraggo → poi supino`, ma **retrarre + supinare nella stessa finestra
temporale** (OSS). La supinazione è un **evento temporale**, non uno stato finale:

```
inizio supinazione → progressione → fine supinazione
```

### Mano sinistra: aperta → chiusa

La mano non si chiude immediatamente: resta aperta finché quella configurazione
conserva un'utilità (INT). La chiusura **comincia** nel primo momento in cui la
traiettoria è sufficientemente stabile per consentire la configurazione
successiva, ed è **molto rapida** — il paragone del Director: *"come afferrare
qualcosa che arriva velocemente"*.

```
OPEN ───────┐
            │ chiusura (evento temporale rapido)
            ↓
           FIST
```

### LOCK del braccio sinistro

Configurazione terminale funzionale: continuare a usare quel grado di libertà non
produce più il vantaggio precedente → diventa vincolo funzionale per la
transizione successiva. Non "articolazione bloccata". (INT — vedi
`05-glossario.md`)

### Relazione gomito → mano

OSS da verificare: il vettore finale della mano/pugno può essere uguale o molto
simile, come direzione, al vettore con cui il gomito si muove posteriormente.

```
gomito  ←──── V₁
mano    ←──── V₂
V₁ ≈ V₂        (relazione geometrica del modello, IPO — non legge biomeccanica)
```

## Anello 3 — Bacino

Quando il braccio sinistro raggiunge la configurazione terminale, nella
descrizione del Director comincia la parte importante della rotazione
tronco/bacino:

- il piede sinistro fornisce un vincolo;
- il lato sinistro del bacino viene spinto posteriormente;
- il piede destro comincia a spingere anteriormente;
- l'interazione delle due azioni potrebbe generare una **coppia sul bacino**
  (*force couple* contralaterale). (IPO — non dimostrata; servono GRF, direzione
  delle forze, momenti, cinematica 3D)

### Contributo del braccio compatto alla rotazione

Formulazione corretta: ridurre la distribuzione della massa lontano dall'asse
**può ridurre il momento d'inerzia** rispetto a quell'asse (principio fisico
stabilito). La relazione con la velocità angolare dipende dalla dinamica
complessiva e dalle coppie applicate — quindi "il braccio compatto accelera la
rotazione" è IPO, non conclusione.

## Anello 4 — Tronco

Né completamente rigido né completamente rilassato: **struttura dinamicamente
organizzata** che consente trasferimento e coordinamento tra parte inferiore e
superiore (INT). Deve simultaneamente: consentire la rotazione, trasferire
movimento/forze, mantenere una configurazione utile, non produrre perturbazione
posturale inutile.

## Anello 5 — Spalla destra e mano destra

La mano destra non inizia necessariamente subito la sua corsa finale. Può restare
relativamente raccolta mentre:

```
tronco ruota → spalla destra avanza → mano conserva un grado di libertà
```

### "L'ultimo momento utile"

Non un numero fisso di millisecondi, ma una condizione geometrica: finché
l'ulteriore rotazione della spalla porta la mano verso una configurazione più
favorevole, il movimento può continuare. Quando continuare quella libertà
inizierebbe ad **allontanare** la mano dalla traiettoria desiderata, la mano deve
passare rapidamente alla propria traiettoria finale:

```
spalla continua → raggiunge condizione utile → mano accelera → traiettoria finale
```

Transizione **geometrica + temporale**, non una semplice "fase del pugno". (INT/IPO)

**Debito di formalizzazione:** la condizione di cambio va resa operativa.
Candidati per la variabile che determina il cambio di strategia: posizione e
velocità della mano, traiettoria desiderata, errore dalla configurazione target,
costo temporale, costo energetico, stato post-azione richiesto. Non
necessariamente tutti — e **potrebbe non essere una singola variabile**: la
commutazione potrebbe vivere su una **frontiera nello spazio degli stati**
(switching boundary), una superficie che separa "continuare è utile" da
"transitare è utile". Esplorare questa forma prima di cercare una soglia
scalare. Possibile parente in letteratura: switching condition in optimal
control — da mappare (`08-letteratura-biomeccanica.md`).

### Traiettoria della mano

Principio: **minimo movimento non utile** — non "sempre linea retta", ma evitare
deviazioni che non contribuiscono all'obiettivo. Da rappresentare: punto
iniziale, punto finale, traiettoria, vettore, deviazioni, momento di transizione.

## Anello 6 — Configurazione strutturale finale

OSS (prove di allineamento e spinta contro una parete): esiste una configurazione
del braccio in cui l'allineamento scheletrico è favorevole, la struttura si
mantiene/carica con relativamente poca attività muscolare, e la geometria sembra
permettere una trasmissione efficace del carico.

Formulazione più scientifica di "posizione corretta":

> configurazione strutturale favorevole alla trasmissione del carico attraverso
> arto superiore → spalla → tronco → bacino → arti inferiori.

La metafora della "lancia" è utile didatticamente, ma non è una dimostrazione
biomeccanica. (INT)

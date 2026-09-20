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

Il progetto interpreta il piede come parte del sistema che *può* contribuire a
generare forze, vincolare il corpo, controllare il movimento del bacino e
preparare la transizione successiva. (INT)

Quale di queste funzioni sia effettivamente necessaria — e in che misura — è
IPO. La quantificazione del contributo alla rotazione richiede GRF e cinematica
3D. (IPO, non verificata con i dati attuali)

## Anello 2 — Braccio sinistro

### Traiettoria del gomito

Partenza da guardia; il braccio viene portato posteriormente. Il gomito segue una
traiettoria approssimativamente **arcuata** (OSS — da rappresentare come arco
punto-iniziale → punto-finale; la funzione esatta dell'arco è INT).

### Retrazione + supinazione: evento combinato

Non `retraggo → poi supino`, ma **retrarre + supinare nella stessa finestra
temporale** (OSS). *Nel nostro modello* la supinazione viene rappresentata come
**evento temporale**, anziché come proprietà della configurazione finale —
questa è una scelta di rappresentazione, non una proprietà biomeccanica:

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

### Scheda di analisi compilata — Anello 2 (prima applicazione del formato `04`)

> Prima compilazione della scheda di analisi per fase/anello (FASE 3, `04`).
> Serve a verificare quali campi il modello/JSON deve sostenere — e a separare
> ciò che sappiamo da ciò che la spiegazione pretende.

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[video]` il gomito percorre una traiettoria posteriore approssimativamente
  arcuata, da guardia a configurazione terminale.
- `[video]` retrazione e supinazione avvengono nella stessa finestra
  temporale (evento combinato, non sequenziale).
- `[video]` la mano resta aperta, poi si chiude rapidamente quando la
  traiettoria è stabile.
- `[empirico]` la configurazione finale trasmette carico con poca attività
  muscolare *percepita* (prova contro parete — sensazione, non EMG).

**2. CINEMATICA**

- Posizioni: gomito da avanti → posteriore; polso segue il gomito; mano
  aperta → pugno chiuso.
- Traiettoria del gomito: arcuata (forma esatta da verificare sui dati).
- Relazione temporale: la fine della retrazione è ~contemporanea all'inizio
  della rotazione tronco/bacino (sovrapposizione da quantificare).
- **Limite dichiarato:** a ~17 fps (Δt ≈ 59 ms) la chiusura rapida della mano
  e la transizione retrazione→rotazione sono *temporalmente ambigue* —
  velocità e ω di quegli eventi non sono misurabili sui dati attuali.

**3. FORZE/MOMENTI COINVOLTI** — *interamente INT/IPO: nessuna misura di forza.*

- τ = r × F rispetto all'asse verticale di rotazione tronco/bacino: la
  retrazione del braccio possiede momento angolare proprio attorno a
  quell'asse.
- Domande fisiche aperte: la retrazione **trasferisce** momento angolare al
  tronco (conservazione/trasferimento di L in catena)? Serve un modello
  segmentale con masse e inertie — i soli landmark non bastano.
- Compattezza: braccio retratto vicino all'asse → può ridurre il momento
  d'inerzia `I` del sistema tronco+braccio → a parità di τ, ω potenzialmente
  maggiore (IPO — dipende dalla dinamica complessiva, non dalla sola I).
- A fine corsa la configurazione diventa parte della struttura che trasmette
  carico (vincolo, non più generatore di moto).

**4. FUNZIONE MECCANICA — candidati (non scelta a priori)**

- produrre momento angolare controrotatorio sul tronco;
- limitare un DOF → configurazione-vincolo per la rotazione successiva;
- ridurre `I` rispetto all'asse di rotazione;
- stabilizzare il lato sinistro mentre il destro accelera;
- preparare la configurazione strutturale finale (Anello 6).

**5. COSTO**

- Tempo dedicato alla retrazione vs anticipazione del pugno (costo temporale).
- Energia muscolare per retrazione + tenuta della configurazione.
- Il LOCK consuma un DOF: quel grado non contribuisce più al moto.
- Eventuale perturbazione posturale se la retrazione sbilancia il sistema.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché arcuata e non rettilinea? (INT: l'arco forse combina retrazione e
  rotazione — da verificare).
- Perché mano aperta fino a traiettoria stabile? (INT del progetto: la
  chiusura come evento rapido differito).
- Perché il LOCK coincide ~con l'inizio della rotazione, non dopo?

**7. EFFETTO SULLA FASE SUCCESSIVA**

- Configura il lato sinistro come riferimento/vincolo durante la rotazione
  del bacino (INT).
- Alimenta l'ipotesi della coppia contralaterale sul bacino (piede sx
  posteriore + piede dx anteriore — IPO, serve GRF).
- V₁ ≈ V₂: la direzione della retrazione anticipa quella finale del pugno
  (relazione geometrica, IPO).

**8. ALTERNATIVE**

- Retratta poi ruota (seriale, ~CSM) vs sovrapposta (~SSM) — Fuchs 2018:
  entrambe documentate, nessuna universalmente superiore.
- Rotazione con braccio non retratto → `I` più alto (previsione calcolabile).
- Mano sempre chiusa o sempre aperta vs chiusura differita.
- Nessuna retrazione (pugno "singolo").

**9. COSA SA LA LETTERATURA?**

- Fuchs 2018: in CSM esiste il *backswing* di spalla/gomito — la nostra
  "retrazione" ha un parente documentato in letteratura sullo striking.
- Martins et al. (choku-zuki): *bracing* dell'estremità prossimale — affine
  al nostro LOCK funzionale.
- APA/feedforward: la retrazione potrebbe essere preparazione posturale
  anticipata alla rotazione.
- Trasferimento di momento angolare nella catena cinetica: concetto noto in
  biomeccanica dello striking (mapping da completare in `08`).

**10. COSA STIAMO IPOTIZZANDO? (IPO + predizioni)**

- H1, H3 + "il LOCK facilita la rotazione del tronco" (registro `03`).
- **Predizione P-A2.1:** ritardare o eliminare il LOCK/retrazione dovrebbe
  alterare il timing o la velocità della rotazione del tronco — falsificabile
  con confronto di varianti a cattura densa.
- **Predizione P-A2.2:** un modello segmentale con tabelle antropometriche +
  posizioni landmark dovrebbe stimare `I_tronco+braccio` più basso con
  retrazione completa — **calcolabile subito**, senza nuova strumentazione.

**11. COME POTREMMO MISURARLO?**

- Subito: stima di `I` da landmark + tabelle antropometriche (P-A2.2).
- Serve: cattura ≥100–240 fps per chiusura mano e transizione LOCK→rotazione;
  cinematica 3D; GRF per la coppia contralaterale; EMG per "poca attività
  muscolare".

**12. COSA NON DIMOSTRIAMO ANCORA**

- Che il LOCK sia *causalmente* necessario alla rotazione (vs semplice
  sovrapposizione temporale).
- Che la retrazione trasferisca momento utile al tronco.
- Che "poca attività muscolare" sia vera (percepito ≠ EMG).
- Quale delle funzioni candidate (punto 4) sia quella reale.

### Bozza nel tool — primo caso d'uso del linguaggio S2

`tools/examples/anello-2-retrazione.json` (importabile nell'editor via
pannello JSON). Codifica:

```
S1 GUARDIA ──M1 retrazione──C1 (unformalized)──> S2 POST-RETRAZIONE
S2 ──M2 transizione verso rotazione tronco──C2──> S3 CONFIG. SUCCESSIVA
```

con LOCK funzionale (L1, avambraccio 200–600 ms), vettori di spostamento
V1 (gomito) e V2 (mano), evento SUPINAZIONE, annotazione sulla chiusura
rapida della mano. È una **bozza autoriale** (pose e tempi scelti a mano,
`provenance: authored`), non una formalizzazione scientifica: il test è che
il JSON da solo basti a ricostruire il modello.

Limite noto del linguaggio emerso dalla bozza: il legame stato↔keyframe è
solo per `time` (implicito); un riferimento esplicito `state.keyframeId`
renderebbe la catena meno ambigua.

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

Il progetto interpreta il tronco come **struttura dinamicamente organizzata** —
né completamente rigida né completamente rilassata — che consentirebbe
trasferimento e coordinamento tra parte inferiore e superiore (INT del
progetto, non operazionalizzata). Funzioni candidate da verificare: consentire
la rotazione, trasferire movimento/forze, mantenere una configurazione utile,
non produrre perturbazione posturale inutile.

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

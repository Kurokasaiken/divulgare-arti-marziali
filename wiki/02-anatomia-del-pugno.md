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

### Scheda di analisi compilata — Anelli 0+1 (base e spostamento)

> Seconda applicazione del formato `04`. A differenza di Anello 2, qui il
> capture 2D vede la parte bassa del corpo (landmark 23–32, confidence ~1.0)
> ma **non** la distribuzione del carico tallone/avampiede — quella resta
> osservazione empirica non misurabile sui dati attuali.

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[video]` il piede sinistro si solleva, atterra con il tallone, il carico
  passa verso l'avampiede, la gamba si estende leggermente.
- `[capture]` `L_foot_index.y` e `L_ankle.y` mostrano un sollevamento del
  piede di ~2% dell'altezza di frame (dy ≈ −0.02 unità normalizzate),
  consistente in 5/5 reps.
- `[capture]` `L_hip.y` scende di ~1–1.7% frame durante l'azione → il bacino
  **sale**, come già osservato a video (ora confermato su dato).
- `[capture]` `R_hip.x − L_hip.x` **cambia segno** in tutte le reps
  (−0.05 → +0.02/0.04): proxy planare di rotazione/scivolamento dell'asse
  pelvico. Interpretazione come "rotazione" è INT (dipende dall'azimut
  camera); come evento cinematico è OSS.
- `[empirico]` la parte sinistra del bacino viene spinta posteriormente
  (sensazione dell'esecutore — non separabile come OSS su dati 2D).

**2. CINEMATICA**

- Sequenza osservabile: sollevamento piede → spostamento → appoggio →
  salita bacino; le finestre esatte variano tra reps (foot-lift max a
  f26–f52, hip-rise max a f26–f46).
- **Sincronia critica:** il flip di `hips_dx` e il primo frame con
  `gomito_sx < 80°` coincidono entro ±1 frame in tutte le reps
  (f11/f11, f15/f15, f16/f16, f19/f19, f28/f27). A Δt ≈ 59 ms l'ordine
  bacino↔braccio **non è risolvibile**.
- Limite dichiarato: a 17 fps non si può distinguere anticipazione
  posturale (bacino prima) da drive comune (sincroni) da risposta
  (bacino dopo).

**3. FORZE/MOMENTI COINVOLTI** — *interamente INT/IPO: nessuna misura GRF.*

- Appoggio tallone → carico avampiede: ridistribuzione della reazione
  vincolare normale; l'attrito al suolo è la sola fonte possibile di forza
  orizzontale esterna sul sistema (vincolo meccanico, non misurato).
- Estensione gamba + salita bacino: lavoro contro gravità sul CoM —
  energia spesa verticalmente, candidata a preload o a riposizionamento.
- Spinta posteriore del bacino sx: se reale, implica momento sul bacino
  attorno all'asse verticale — coerente con il flip `hips_dx` (IPO di
  lettura congiunta).

**4. FUNZIONE MECCANICA — candidati (non scelta a priori)**

- ancoraggio: fissare il lato anteriore come fulcro per le fasi
  successive;
- impulso: contribuire forza orizzontale via attrito al moto del sistema;
- riposizionamento: portare il sistema nella configurazione spaziale utile
  alla rotazione (distanza/offset del bacino);
- preload/postura: estensione gamba + bacino alto come condizione
  energetica o geometrica preparatoria;
- nessuna funzione attiva: semplice conseguenza dello spostamento (ipotesi
  nulla da non scartare).

**5. COSTO**

- Tempo del passo vs partenza diretta del colpo.
- Impegno posturale: il passo vincola la base fino all'atterraggio.
- Shock all'appoggio del tallone (dissipazione, non recuperabile).
- Energia spesa nel sollevamento del CoM.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché tallone prima? (INT: appoggio stabile rapido / rotolamento
  controllato — da verificare).
- Perché poi carico su avampiede? (INT: prepara la rotazione sul
  avampiede come pivot — serve GRF o vista laterale).
- Perché il bacino sale? (INT candidati: estensione gamba per pivotare;
  aggiustamento altezza CoM; artefatto della rotazione pelvica in
  proiezione).
- Perché spinta posteriore del lato sx? (INT: contro-rotazione pelvica che
  accompagna/prepara la rotazione del tronco).

**7. EFFETTO SULLA FASE SUCCESSIVA**

- Fornisce l'ancoraggio sinistro durante la retrazione del braccio
  (Anello 2) e la rotazione del tronco — la sincronia bacino↔braccio a
  ±1 frame è **compatibile** con accoppiamento causale, non lo dimostra.
- Se il piede sx funge da pivot, la configurazione finale del passo
  determina l'asse attorno a cui la rotazione può svilupparsi (INT).

**8. ALTERNATIVE**

- Nessun passo (colpo da fermo) — confronto diretto possibile in cattura.
- Appoggio diretto su avampiede senza fase tallone.
- Passo più ampio/più corto — trade-off distanza vs tempo.
- Bacino senza salita (estensione diversa della gamba).

**9. COSA SA LA LETTERATURA?**

- APA (anticipatory postural adjustments): l'attività posturale di
  gambe/bacino *precede* tipicamente il gesto rapido dell'arto — la nostra
  sincronia ±1 frame non la esclude né la conferma (risoluzione).
- GRF nei colpi: la letteratura sullo striking documenta il contributo
  della spinta al suolo alla potenza del pugno (mapping in `08` da
  completare); il ruolo del piede pivot in gyaku-zuki è discusso.
- Nessuna fonte consultata ancora sul segnale specifico tallone→avampiede
  nel passo d'ingresso.

**10. COSA STIAMO IPOTIZZANDO? (IPO + predizioni)**

- Il piede sx contribuisce causalmente (ancoraggio/impulso) e non è solo
  spettatore — IPO.
- **Predizione P-A0.1 (nuova):** se il bacino guida il gesto (modello
  APA), l'inizio del flip `hips_dx` precede la retrazione del braccio di
  almeno un intervallo risolvibile; se il drive è comune o il braccio guida,
  no. **Non falsificabile a 17fps — richiede cattura ≥100fps o EMG.**
- La salita del bacino dovrebbe comparire anche in esecuzioni senza impatto
  reale se è funzionale alla configurazione (vs artefatto del contatto).

**11. COME POTREMMO MISURARLO?**

- Subito (dati attuali): timing dei proxy cinematici (foot lift, hip rise,
  hips_dx) — fatto; confronto varianti con/senza passo.
- Serve: cattura ≥100–240 fps per l'ordine bacino↔braccio; pedana di forza
  o solette a pressione per tallone→avampiede; vista laterale o 3D per la
  componente in profondità del bacino; EMG arti inferiori.

**12. COSA NON DIMOSTRIAMO ANCORA**

- Che il passo/base sia *causalmente* necessario (vs risposta
  accompagnatoria).
- Che il carico tallone→avampiede avvenga davvero come descritto
  (non osservabile nei landmark).
- L'ordine temporale bacino↔braccio (sincroni a 17 fps).
- La quota di forza orizzontale effettivamente prodotta al suolo.

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

Tre correzioni applicate dopo la prima lettura a freddo (rev. esterna):

- **stato↔keyframe esplicito**: `S2.keyframeId = "KF2"` — prima il legame era
  solo implicito via `time` (fragile: più stati possono condividere un
  istante, e uno stato semantico non è una posa);
- **`M2.representationStatus: 'not_available'`** (`reason: skeleton_scope`) —
  la rotazione del tronco è dichiarata fuori scope dello skeleton, non una
  traiettoria dimenticata. La differenza tra "movimento rappresentato" e
  "movimento semanticamente dichiarato" è ora leggibile nel JSON;
- **LOCK con semantica temporale esplicita**: `L1.associatedState: 'S2'` +
  `role: 'constrain-next-transition'` — `start`/`end` sono la *finestra di
  validità del vincolo* (può attraversare le transizioni), non la durata di
  uno stato.

Regola confermata dal test: se la teoria richiede una distinzione che il
modello dati non sa esprimere, si corregge il modello dati (es. vettori
`displacement` per V₁≈V₂ — uno spostamento nel tempo non è un vettore
giunto→giunto).

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

### Scheda di analisi compilata — Anello 3 (bacino)

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[capture]` `hips_dx = R_hip.x − L_hip.x` cambia segno in 5/5 reps
  (−0.05 → +0.02/0.06) — evento cinematico OSS; lettura come "rotazione
  pelvica" è INT (proxy dipendente da azimut camera).
- `[capture]` il flip avviene allo **stesso frame** del flip della linea
  delle spalle (`sdx`) e a ±1 frame dalla retrazione del braccio
  (`gomito_sx < 80°`): f11, f15, f16, f19, f28 nelle cinque reps.
- `[capture]` il bacino sale (OSS già registrato in Anelli 0+1).
- `[video/empirico]` piede sx come vincolo, lato sx del bacino spinto
  posteriormente, piede dx che spinge anteriormente.

**2. CINEMATICA**

- Flip pelvico osservabile come inversione dell'ordine x delle anche in
  proiezione — la finestra di transizione è breve (~pochi frame).
- Il bacino precede di alcuni frame il picco di salita e accompagna la
  retrazione del braccio (sincronia ±1 frame — vedi P-A0.1).
- Nessuna cinematica 3D: la rotazione vera attorno all'asse verticale non
  è misurabile, solo il proxy planare.

**3. FORZE/MOMENTI COINVOLTI** — *INT/IPO, nessuna misura.*

- Coppia contralaterale candidata: piede sx vincolato + spinta posteriore
  bacino sx + spinta anteriore piede dx → possibile `τ` sul bacino attorno
  all'asse verticale. (IPO — serve GRF.)
- Il momento torcente risultante, se esiste, è ciò che accelera la
  rotazione del segmento tronco+bacino.

**4. FUNZIONE MECCANICA — candidati**

- generatore di momento torcente (coppia contralaterale);
- fulcro/pivot attorno a cui la rotazione si organizza;
- riposizionatore del CoM e della configurazione per lo strike;
- trasmettitore: il bacino come giunzione tra spinta dal suolo e tronco.

**5. COSTO**

- La rotazione pelvica impegna la base: se il piede non è ancorato la
  coppia non si sviluppa (dipendenza dal ring precedente).
- Energia dei muscoli del core e degli arti inferiori.
- Richiede timing stretto con braccio e tronco.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché la rotazione parte dal bacino e non dal tronco da solo?
  (INT: il bacino è il segmento con massa maggiore — momento torcente
  più efficace; e collega la catena al suolo.)
- Perché sincrono con la retrazione? (IPO: accoppiamento funzionale —
  oppure drive comune, o risposta — non risolvibile a 17fps.)

**7. EFFETTO SULLA FASE SUCCESSIVA**

- Determina l'asse e il momento disponibile per la rotazione del tronco
  (Anello 4) e per l'avanzamento della spalla destra (Anello 5).
- Se la coppia contralaterale esiste, il LOCK del braccio sx (Anello 2)
  potrebbe chiuderne il lato destro — IPO di sistema.

**8. ALTERNATIVE**

- Rotazione solo del tronco senza contributo pelvico (possibile ma
  meccanicamente meno efficace — IPO).
- Sequenza bacino→tronco strettamente seriale vs sovrapposta (come CSM/SSM
  per l'arto — stessa distinzione a livello inferiore).
- Senza coppia contralaterale: solo spinta del piede posteriore.

**9. COSA SA LA LETTERATURA?**

- La rotazione pelvica come contributo primario alla potenza dello striking
  è documentata (kinematic sequence, proximal-to-distal).
- Force couple e contributo GRF nel pugno: presente in letteratura boxing/
  karate — mapping in `08` da completare.

**10. COSA STIAMO IPOTIZZANDO? (IPO + predizioni)**

- Che esista una coppia contralaterale misurabile (serve GRF).
- Che la sincronia bacino↔braccio non sia casuale ma coordinata
  (P-A0.1 copre il caso discriminante).

**11. COME POTREMMO MISURARLO?**

- Proxy attuali: timing e ampiezza del flip `hips_dx` — fatto.
- Serve: vista zenitale o 3D per angolo pelvico vero; GRF per la coppia;
  ≥100fps per l'ordine relativo agli altri anelli.

**12. COSA NON DIMOSTRIAMO ANCORA**

- Che il flip `hips_dx` sia rotazione pelvica e non artefatto di
  traslazione/perspettiva.
- Che la coppia contralaterale esista.
- La quota di momento torcente fornita dal bacino vs dal tronco.

## Anello 4 — Tronco

Il progetto interpreta il tronco come **struttura dinamicamente organizzata** —
né completamente rigida né completamente rilassata — che consentirebbe
trasferimento e coordinamento tra parte inferiore e superiore (INT del
progetto, non operazionalizzata). Funzioni candidate da verificare: consentire
la rotazione, trasferire movimento/forze, mantenere una configurazione utile,
non produrre perturbazione posturale inutile.

### Scheda di analisi compilata — Anello 4 (tronco)

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[capture]` `sdx = R_shoulder.x − L_shoulder.x` cambia segno allo stesso
  frame del flip pelvico in 5/5 reps — proxy planare della rotazione del
  cingolo scapolare (INT la lettura come rotazione; OSS l'evento).
- `[capture]` all'estensione massima del pugno il tronco resta impilato:
  `lean = midshoulder.x − midhip.x ≈ 0` (−0.00 → +0.02) in tutte le reps.
- `[video]` il tronco ruota e trasferisce il moto dal basso verso il
  braccio che colpisce.

**2. CINEMATICA**

- Onset della rotazione scapolare sincrono col flip pelvico (±0 frame) —
  **nessun ritardo misurabile** bacino→cingolo a 17fps: coerente con
  rotazione "a blocco" del segmento tronco-bacino in questa finestra, o con
  risoluzione insufficiente a vedere il ritardo.
- Rotazione prosegue mentre il pugno estende (finestra f~24–30 in rep_001)
  e si stabilizza nel plateau.

**3. FORZE/MOMENTI COINVOLTI** — *INT/IPO.*

- Se bacino e cingolo ruotano insieme, il tronco trasmette il momento
  generato sotto verso il braccio: funzione di **trasmissione** più che di
  generazione in questa finestra (INT).
- Rigidezza variabile ("struttura dinamicamente organizzata") è IPO non
  operazionalizzata: un tronco troppo cedevole dissiperebbe il momento,
  troppo rigido impedirebbe il sequenziamento — nessuna misura attuale
  distingue.

**4. FUNZIONE MECCANICA — candidati**

- trasmettere momento torcente dal bacino alla spalla destra;
- mantenere impilamento posturale (lean ≈ 0 osservato);
- permettere differenziale di rotazione in una fase successiva (se esiste
  un ritardo fine non risolto a 17fps).

**5. COSTO**

- Co-contrazione del core per la rigidità funzionale (energia).
- Un tronco rigido rende tutto il sistema un unico corpo inerziale —
  riduce i DOF disponibili per correzioni.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché impilato (lean ≈ 0) e non inclinato? (INT: minimizza momento
  destabilizzante e mantiene l'asse di rotazione vicino al CoM — da
  verificare.)

**7. EFFETTO SULLA FASE SUCCESSIVA**

- Porta la spalla destra nella regione da cui la mano può partire verso la
  traiettoria finale (Anello 5) — è l'anello che rende possibile
  "l'ultimo momento utile".

**8. ALTERNATIVE**

- Tronco inclinato in avanti (lean > 0): più massa dietro il colpo ma
  meno stabilità di recupero.
- Rotazione differenziata bacino→cingolo (whip più marcato): non osservata
  nei dati a questa risoluzione.

**9. COSA SA LA LETTERATURA?**

- Kinematic sequence / proximal-to-distal sequencing è il modello standard
  dello striking; il nostro dato (sincronia bacino↔cingolo a 17fps) non la
  conferma né la smentisce — la sequenza fine non è risolta.

**10. COSA STIAMO IPOTIZZANDO?**

- Che il tronco si comporti da trasmettitore organizzato e non da massa
  passiva; che il lean ≈ 0 sia funzionale e non casuale.

**11. COME POTREMMO MISURARLO?**

- Angolo relativo cingolo–bacino in 3D (vista zenitale o mocap con z);
  ≥100fps per l'eventuale ritardo fine; EMG core per "organizzato vs
  rigido vs rilassato".

**12. COSA NON DIMOSTRIAMO ANCORA**

- L'esistenza di un ritardo bacino→cingolo (risoluzione insufficiente).
- Che il tronco trasferisca momento e non lo dissipa.
- Che il lean ≈ 0 sia causale alla trasmissione.

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

### Scheda di analisi compilata — Anello 5 (spalla e mano destra)

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[capture]` durante la fase di rotazione il gomito destro **flette
  ulteriormente** prima di estendere: R_elb scende a ~25–50° mentre il
  bacino ruota, poi estende a ~165–178° — la mano resta "raccolta" come
  descritto (conferma su dato della qualifica nel testo sopra).
- `[capture]` il polso dx resta ~stazionario in x (~0.34–0.45) durante il
  flip, poi avanza rapidamente a ~0.56 nella finestra di estensione
  (rep_001: f24→f30).
- `[capture]` la traiettoria del polso durante l'estensione è circa
  monotona in x — coerente con "minimo movimento non utile" (INT la
  qualifica di "non utile"; OSS la monotonia).
- `[capture]` **artefatto noto:** durante il transito rapido i landmark del
  polso mostrano salti (~0.17 unità/frame, es. rep_001 f18–f21) pur con
  confidence 1.0 — motion blur/occlusione. La velocità di punta del pugno
  NON è misurabile su questi dati; i picchi apparenti sono spurî.

**2. CINEMATICA**

- Sequenza: raccolta (flessione ulteriore durante la rotazione) →
  estensione rapida (~5–10 frame) → plateau a pugno esteso (~15 frame) →
  rientro.
- L'estensione completa **~10–15 frame dopo** il flip pelvico/scapolare in
  tutte le reps — la mano parte dopo che la rotazione è iniziata
  (OSS sui tempi; il criterio "ultimo momento utile" resta IPO).

**3. FORZE/MOMENTI COINVOLTI** — *INT/IPO.*

- L'avanzamento della mano eredita la velocità del cingolo rotante più
  l'estensione del gomito — composizione dei due contributi non
  scomponibile senza 3D e dinamica.
- Il mantenere la mano raccolta riduce `I` del lato destro durante la
  rotazione (stesso principio di P-A2.2, lato opposto — IPO simmetrica).

**4. FUNZIONE MECCANICA — candidati**

- ritardare l'estensione per massimizzare il contributo della rotazione
  prima della traiettoria finale;
- preservare un DOF correttivo fino all'ultimo momento (robustezza contro
  errori di mira — candidato forte);
- ridurre I durante la fase di accelerazione rotatoria.

**5. COSTO**

- Tempo di raccolta: la mano parte dopo → il colpo arriva più tardi (se
  non compensato dalla rotazione).
- La finestra di decisione è stretta: transizione tardiva → colpo corto;
  precoce → perde il contributo rotatorio.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché flettere *di più* durante la rotazione invece di restare fermi?
  (IPO: compattare il lato destro riduce I e preserva il DOF.)
- Perché l'estensione parte a rotazione avviata e non prima? (IPO: la
  commutazione avviene quando continuare la raccolta non è più utile —
  "ultimo momento utile", debito di formalizzazione dichiarato sopra.)

**7. EFFETTO SULLA FASE SUCCESSIVA**

- Determina la configurazione all'impatto (Anello 6): allineamento
  polso-gomito-spalla e stato del sistema post-contatto.

**8. ALTERNATIVE**

- Estensione simultanea alla rotazione (colpo "a spinta") vs estensione
  differita — documentato nella pratica di stili diversi.
- Mano raccolta ma gomito meno flesso (raccolta parziale).

**9. COSA SA LA LETTERATURA?**

- Il sequenziamento prossimale→distale (spalla prima, mano dopo) è il
  modello canonico — i nostri dati sono coerenti (estensione completa dopo
  il flip), ma non dimostrano il meccanismo.
- Switching boundary / optimal control: candidati per la formalizzazione
  dell'"ultimo momento utile" (già notato nel testo; spike C-02).

**10. COSA STIAMO IPOTIZZANDO? (IPO + predizioni)**

- **Predizione P-A5.1 (nuova):** in esecuzioni corrette l'onset
  dell'estensione (R_elb che supera ~90°) segue il flip pelvico/scapolare
  di un margine risolvibile; una variante "a spinta" (estensione anticipata)
  dovrebbe mostrare velocità finale del polso diversa — verificabile con
  confronto di varianti a parità di capture.
- L'ultimo momento utile come frontiera nello spazio degli stati (IPO —
  debito di formalizzazione esplicito).

**11. COME POTREMMO MISURARLO?**

- Subito: timing onset estensione vs flip (fatto — margine ~10–15 frame).
- Serve: ≥100fps e/o camera ad alta risoluzione temporale per la velocità
  reale del polso (i picchi attuali sono artefatti); 3D per la
  traiettoria vera; parametrizzazione dell'errore dalla traiettoria
  desiderata per operazionalizzare la commutazione.

**12. COSA NON DIMOSTRIAMO ANCORA**

- Che il ritardo dell'estensione sia una strategia (vs semplice ritardo
  muscolare).
- La velocità finale del pugno (dati inaffidabili nel transito rapido).
- Quale variabile commuta la mano (posizione/velocità/errore/tempo).

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
### Scheda di analisi compilata — Anello 6 (configurazione finale)

**1. COSA SUCCEDE? (OSS, con provenienza)**

- `[capture]` al plateau di estensione (rep_001: f30–f45) il gomito destro
  sta a ~165–178° — **quasi esteso ma non in iperestensione**; il polso è
  stazionario (x ~0.56, varianza piccola) per ~15 frame: esiste una fase di
  **tenuta** della configurazione, non solo un istante di picco.
- `[capture]` al massimo dell'estensione il tronco resta impilato
  (lean ≈ 0) — la configurazione finale conserva l'allineamento
  spalle-bacino in proiezione.
- `[empirico]` prova contro parete: la configurazione trasmette carico con
  poca attività muscolare *percepita* (sensazione, non EMG).
- `[video]` allineamento polso–gomito–spalla visibile in proiezione.

**2. CINEMATICA**

- Finestra di tenuta osservabile: ~0.9 s a 17fps (plateau f30–f45) — il
  sistema mantiene la configurazione oltre l'istante di estensione
  massima.
- Gomito quasi-esteso: ~165–178° — il margine residuo rispetto ai 180° è
  OSS, la sua funzione (riserva di corsa / evitare il blocco articolare /
  tolleranza del landmark) è INT.

**3. FORZE/MOMENTI COINVOLTI** — *INT/IPO, nessuna misura di carico.*

- Se la trasmissione è strutturale, il carico dovrebbe passare per
  compressioni articolari allineate piuttosto che per momenti muscolari —
  l'allineamento osservato è *necessario ma non sufficiente* a
  dimostrarlo.
- La tenuta prolungata (0.9 s) suggerisce basso costo di mantenimento —
  compatibile con "poca attività muscolare" ma non la dimostra (serve EMG).

**4. FUNZIONE MECCANICA — candidati**

- trasmissione del carico dall'impatto al suolo attraverso la catena
  (funzione primaria candidata);
- stabilità post-contatto: la tenuta permette assorbimento controllato;
- configurazione di riferimento per il rientro/ritorno in guardia.

**5. COSTO**

- La configurazione strutturale è rigida: poca capacità di correzione
  durante il contatto; un impatto fuori asse scaricherebbe sulle
  articolazioni.
- Il tempo di tenuta è tempo non disponibile al colpo successivo.

**6. PERCHÉ QUESTA CONFIGURAZIONE?**

- Perché ~170° e non estensione completa? (IPO: margine anti-iperestensione
  e capacità di assorbimento; alternativa: semplice limite di tracking.)
- Perché tenuta e non rimbalzo immediato? (INT: verifica della trasmissione
  / abitudine alla prova contro parete — il soggetto è l'autore del
  modello.)

**7. EFFETTO SULLA FASE SUCCESSIVA**

- La configurazione di tenuta è lo stato da cui parte il rientro in
  guardia (ritorno osservabile f45–f60: polso rientra, gomito riflette).

**8. ALTERNATIVE**

- Contatto e rimbalzo immediato (snap) vs tenuta: i dati mostrano tenuta
  — la scelta è autoriale/stilistica finché non si confrontano varianti.
- Iperestensione completa vs margine: il margine osservato è consistente
  con l'evitamento del blocco articolare passivo.

**9. COSA SA LA LETTERATURA?**

- Il concetto di *effective mass* all'impatto e di allineamento strutturale
  è documentato nella biomeccanica dello striking — la nostra
  configurazione ne è un'istanza candidata; effective mass reale richiede
  dinamica dell'impatto, non posa statica.
- "Trasmissione a basso costo muscolare" — affine a concetti di stiffness/
  impedance control; serve EMG per verificarla.

**10. COSA STIAMO IPOTIZZANDO?**

- Che la tenuta osservata corrisponda alla configurazione a basso costo
  percepita (empirico); che il margine ~170° sia funzionale e non artefatto.

**11. COME POTREMMO MISURARLO?**

- Impatto su bersaglio strumentato (forza) + EMG del braccio durante la
  tenuta; confronto angolo gomito vs forza trasmessa; angolo 3D vero per
  l'allineamento (2D proietta).

**12. COSA NON DIMOSTRIAMO ANCORA**

- Che la configurazione trasmetta meglio di alternative (nessuna misura di
  carico).
- Che "poca attività muscolare" sia vera (percepito ≠ EMG).
- Che l'allineamento in proiezione 2D sia allineamento 3D reale.

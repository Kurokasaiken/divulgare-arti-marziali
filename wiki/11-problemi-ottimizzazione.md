# Problemi di ottimizzazione per anello

> Seconda fase del metodo: le schede di `02` descrivono il gesto
> **osservato** nelle catture reali. Questa pagina lo trasforma in una
> serie di problemi meccanici: per ogni anello, quale configurazione
> sarebbe preferibile *per la funzione attribuita* — non quale sia la
> tecnica "ideale" a priori.
>
> Schema per anello: osservato → problema meccanico → vincoli del compito
> → alternative → **candidato ottimizzato (aperto)** → cosa dovrebbe
> produrre → come verificarlo.
>
> La colonna "candidato" è ora riempita con **proposte IPO derivate dal
> problema meccanico** (prima revisione teorica, R-024 → 2026-09-21):
> ogni candidato porta *perché*, *Δ rispetto al gesto osservato* e *stato*
> (letteratura vs IPO). Candidato ≠ tecnica dimostrata: è la proposta che
> la cattura densa dovrà confrontare con la baseline osservata.

## Quadro

```
CATTURE REALI → ricostruzione gesto osservato → ANALISI PER ANELLO
    → per ogni anello: problema meccanico esplicito
    → candidato ottimizzato derivato dal problema
    → "questa è la tecnica che proponiamo" + perché + cosa produce + come verificarlo
    → nuova cattura della versione MODIFICATA → confronto col gesto precedente
```

La cattura densa (requisiti in `10`) diventa così un esperimento di
confronto modello-contro-modello, non una semplice registrazione migliore.

## Anello 0 — Distanza / spostamento

| | |
|---|---|
| **Osservato** | passo/riposizionamento con sollevamento piede ~2% frame, atterraggio tallone, carico verso avampiede, bacino che sale (OSS capture) |
| **Problema meccanico** | portare il sistema nella configurazione spaziale necessaria all'anello successivo, nel minor tempo compatibile con la stabilità della base |
| **Vincoli del compito** | distanza residua al bersaglio; nessuna telegrafatura; base che deve già supportare la coppia di Anello 3 |
| **Alternative** | nessun passo / passo corto / passo lungo; atterraggio tallone vs avampiede; timing precoce vs tardivo |
| **Candidato ottimizzato** | spostamento **minimo sufficiente** a chiudere la distanza; atterraggio tallone→avampiede solo perché prepara il pivot di Anello 1; salita del bacino accettata come sottoprodotto dell'estensione gamba, non come obiettivo (IPO) |
| **Cosa dovrebbe produrre** | tempo minimo a parità di output del colpo; base pronta alla rotazione |
| **Verifica** | confronto varianti ampiezza passo a parità di bersaglio (VAR+VD) |

*Perché:* tempo e costo crescono con l'ampiezza dello spostamento; energia
spesa a sollevare il CoM non torna. *Δ vs osservato:* coerente — il passo
osservato è già piccolo; il punto aperto è se la salita del bacino sia
funzionale o spesa inutile. *Stato:* IPO — la funzione della salita non è
dimostrata.

## Anello 1 — Piede sinistro / base

| | |
|---|---|
| **Osservato** | piede sx come vincolo durante la retrazione e la rotazione (OSS cinematico: stabile durante il flip pelvico) |
| **Problema meccanico** | fornire un vincolo al suolo capace di scambiare forza orizzontale (dentro il cono d'attrito) senza slittare, posizionato per consentire la rotazione pelvica |
| **Vincoli del compito** | attrito disponibile; orientamento del piede rispetto all'asse di rotazione voluto; transizione tallone→avampiede se serve pivot |
| **Alternative** | piede piatto fisso vs pivot su avampiede; orientamento più aperto/chiuso; posizione più avanti/indietro |
| **Candidato ottimizzato** | ancoraggio che migra da tallone (assorbimento all'appoggio) ad **avampiede** prima dell'onset della rotazione pelvica: il pivot su contatto piccolo riduce il τ d'attrito che il suolo oppone alla rotazione; orientamento del piede compatibile con la direzione del flip (IPO) |
| **Cosa dovrebbe produrre** | shear GRF utile senza slittamento; rotazione pelvica non impedita |
| **Verifica** | GRF (direzione shear) + confronto orientamenti piede (VAR) |

*Perché:* il momento resistente d'attrito attorno all'asse verticale scala
con la dimensione dell'area di contatto — ruotare su avampiede costa meno
momento che ruotare su pianta intera; ma il pivot riduce la stabilità
antero-posteriore, quindi la migrazione deve avvenire **dopo** l'appoggio
stabile e **prima** del flip. *Δ vs osservato:* coerente con la sequenza
tallone→avampiede osservata; il timing esatto vs flip non è risolvibile a
17fps. *Stato:* IPO — principio d'attrito solido, applicazione non misurata.

## Anello 2 — Braccio sinistro / retrazione + LOCK

| | |
|---|---|
| **Osservato** | retrazione+supinazione combinata, mano aperta→chiusa differita, LOCK funzionale, I planare −50% (OSS+INT) |
| **Problema meccanico** | raggiungere la configurazione terminale nel tempo giusto, minimizzando `I` rispetto all'asse di rotazione senza costi eccessivi altrove |
| **Vincoli del compito** | finestra temporale (sincronia col flip pelvico); la configurazione terminale deve servire da vincolo per la fase successiva; non telegrafare |
| **Alternative** | retrazione più/meno completa; traiettoria arcuata vs retta; mano sempre chiusa; LOCK più precoce/tardivo; nessuna retrazione |
| **Candidato ottimizzato** | configurazione terminale a **I minimo compatibile col vincolo**: gomito massimamente flesso e vicino all'asse di rotazione, mano chiusa solo a traiettoria stabilizzata, LOCK attivo entro l'onset della rotazione (IPO — dipende dalla funzione vera del LOCK) |
| **Cosa dovrebbe produrre** | ΔI massimo utile; LOCK che effettivamente altera la rotazione (P-A2.1) |
| **Verifica** | P-A2.1 con varianti di LOCK; P-A2.2 in 3D su geometrie candidate |

*Perché:* se la funzione del LOCK è vincolo per la fase successiva (non
generatore di momento), allora minore I = minore resistenza inerziale alla
rotazione del sistema. *Trade-off dichiarato:* minimizzare I riduce anche
il momento angolare proprio del braccio — se la funzione fosse invece
"trasferire L al tronco", il candidato sarebbe diverso (massa più lontana
= più L a parità di ω). La scelta del candidato dipende dalla funzione —
questa dipendenza è esplicita, non nascosta. *Δ vs osservato:* la
configurazione osservata è già vicina al minimo I (−50% misurato);
l'ottimo potrebbe coincidere con l'osservato oppure differire nel margine
(mano più vicina al corpo?). *Stato:* IPO — P-A2.2 è planare, la funzione
del LOCK non è stabilita.

## Anello 3 — Bacino

| | |
|---|---|
| **Osservato** | flip `hips_dx` sincrono con spalle e retrazione (±0/1 frame), salita bacino (OSS capture) |
| **Problema meccanico** | generare/trasmettere il momento torcente attorno all'asse verticale con l'ampiezza e il timing che la catena richiede |
| **Vincoli del compito** | dipende dall'ancoraggio di Anello 1; deve coordinarsi con il LOCK di Anello 2; coppia contralaterale è IPO |
| **Alternative** | rotazione pelvica ampia vs ridotta; anticipata vs sincrona; con/senza coppia contralaterale |
| **Candidato ottimizzato** | rotazione pelvica con **lead prossimale**: onset che precede la rotazione scapolare di un margine piccolo ma risolvibile; se la coppia contralaterale esiste, le spinte dei due piedi simultanee e massime entro il cono d'attrito (IPO forte — il lead NON è osservato nei dati a 17fps) |
| **Cosa dovrebbe produrre** | momento torcente sufficiente; nessuna perdita di base |
| **Verifica** | ordine temporale a ≥100fps (P-A0.1); GRF per la coppia; confronto ampiezze (VAR) |

*Perché:* la sequenza prossimale→distale sfrutta il segmento più massivo
per primo e consente accumulo/preattivazione nel segmento successivo
(meccanismo documentato nel lancio e nello striking); la coppia richiede
due forze opposte simultanee — sfasate, dissipano momento. *Δ vs
osservato:* **prima divergenza potenziale candidato/osservato** — i dati
mostrano sincronia bacino↔cingolo↔braccio, non lead; il candidato potrebbe
differire dal gesto attuale, o il lead esistere già sotto la risoluzione.
*Stato:* IPO — meccanismo whip documentato in letteratura, applicazione
qui non verificata.

## Anello 4 — Tronco

| | |
|---|---|
| **Osservato** | flip scapolare sincrono col bacino; lean ≈ 0 all'impatto (OSS capture) |
| **Problema meccanico** | trasmettere il momento dal basso al braccio senza dissiparlo: il tronco come elemento a rigidezza controllata |
| **Vincoli del compito** | troppo cedevole → dissipa; troppo rigido → un solo corpo inerziale, niente correzioni |
| **Alternative** | rigidità alta/bassa/variabile nella fase; lean positivo/nullo |
| **Candidato ottimizzato** | rigidità tronco **modulata**: alta durante la finestra di trasmissione (non dissipare momento), con lean ≈ 0 mantenuto; differenziale cingolo–bacino presente solo se il whip di Anello 3 esiste (IPO) |
| **Cosa dovrebbe produrre** | trasmissione del momento con minima perdita |
| **Verifica** | ritardo fine bacino→cingolo a ≥100fps; EMG core per rigidità reale |

*Perché:* un mezzo cedevole dissipa il momento in deformazione invece di
trasmetterlo; lean ≈ 0 mantiene l'asse di rotazione vicino al CoM ed
elimina il momento destabilizzante della massa del tronco sbilanciata.
*Δ vs osservato:* coerente — lean ≈ 0 e sincronia bacino↔cingolo sono già
negli OSS; la modulazione temporale della rigidità non è osservabile nei
landmark. *Stato:* IPO — coerente con impedance/stiffness control in
letteratura motoria, mai misurata qui.

## Anello 5 — Spalla e mano destra

| | |
|---|---|
| **Osservato** | gomito dx flette ulteriormente durante la rotazione (mano raccolta), poi estende; estensione completa ~10–15 frame dopo il flip (OSS capture) |
| **Problema meccanico** | scegliere **quando** rilasciare il DOF della mano: troppo presto perde il contributo rotatorio, troppo tardi accorcia il colpo |
| **Vincoli del compito** | la commutazione dipende da stato (posizione/velocità/errore), non da tempo fisso — "ultimo momento utile" come frontiera nello spazio degli stati |
| **Alternative** | estensione anticipata ("a spinta") / sincrona / differita; raccolta parziale vs completa |
| **Candidato ottimizzato** | commutazione raccolta→estensione quando la rotazione prossimale **smette di portare la mano verso il bersaglio**: estendere nel punto in cui la velocità indotta dalla rotazione e quella dell'estensione si sommano lungo la linea d'attacco; gomito flesso fino a quel momento per tenere I basso e il DOF disponibile (IPO — criterio geometrico, non temporale) |
| **Cosa dovrebbe produrre** | massima velocità utile della mano all'impatto |
| **Verifica** | P-A5.1 + varianti "a spinta" con bersaglio strumentato (VAR+VD+IMP) |

*Perché:* le velocità dei segmenti si sommano al punto distale — estendere
mentre la rotazione contribuisce alla direzione utile massimizza la
velocità lungo la linea d'attacco; il DOF trattenuto è un margine
correttivo contro errori di mira finché dura. *Δ vs osservato:* coerente
— l'estensione segue il flip di ~10–15 frame e la mano resta raccolta
durante la rotazione; il criterio esatto di commutazione resta da
formalizzare (frontiera di stato, spike C-02). *Stato:* IPO — parente
documentato (release timing nel lancio), mai operazionalizzato qui.

## Anello 6 — Configurazione strutturale finale

| | |
|---|---|
| **Osservato** | tenuta ~0.9s a gomito ~165–178°, lean ≈ 0, allineamento in proiezione (OSS capture); bassa attività muscolare percepita (empirico) |
| **Problema meccanico** | trasmettere il carico dell'impatto attraverso la catena con minimo costo muscolare e senza cedimento articolare |
| **Vincoli del compito** | margine anti-iperestensione; capacità di assorbire direzioni fuori asse; recupero post-contatto |
| **Alternative** | angolo gomito più/meno aperto; tenuta vs rimbalzo immediato; allineamenti diversi |
| **Candidato ottimizzato** | allineamento pugno→avambraccio→spalla tale che la forza d'impatto passi per **compressioni articolari** e punti verso la base; gomito a ~165–175° (margine anti-iperestensione e assorbimento); tenuta o rimbalzo a seconda dello scopo — push vs snap (IPO) |
| **Cosa dovrebbe produrre** | forza trasmessa massima a parità di EMG |
| **Verifica** | IMP + EMG: forza vs attivazione al variare dell'angolo |

*Perché:* quando la linea di forza passa attraverso i centri articolari i
carichi sono compressivi e i momenti muscolari necessari crollano — è il
meccanico dietro "poca attività percepita"; il margine angolare evita che
l'impatto scarichi sull'iperestensione passiva del gomito. *Δ vs
osservato:* coerente — ~165–178° e lean ≈ 0 già osservati; la tenuta
lunga è probabilmente artefatto del gesto senza bersaglio reale. *Stato:*
IPO — effective mass e allineamento hanno letteratura (da mappare in
`08`); "poca attività muscolare" resta percepito fino a EMG.

## Nota metodologica

I candidati sono formulati come IPO: derivati dal problema meccanico di
ciascun anello, non assunti dalla pratica. Tre pattern emergono:

- **Δ nullo** (Anelli 0,1,4,6): il candidato teorico coincide ~con il
  gesto osservato — la tecnica praticata è già vicina a ciò che il
  modello proporrebbe; la verifica serve a *confermare*, non a correggere.
- **Δ possibile** (Anello 3): il lead pelvico proposto dalla sequenza
  prossimale→distale **non è osservato** nei dati a 17fps — la prima
  divergenza candidato/osservato; se la cattura densa lo smentisse, il
  modello va corretto, non il gesto.
- **Δ da formalizzare** (Anelli 2,5): il candidato dipende da scelte
  funzionali non ancora stabilite (ruolo del LOCK; criterio di
  commutazione della mano) — il "candidato" è condizionale finché la
  funzione non è decisa.

La cattura densa, quando avverrà, confronterà baseline osservata vs
configurazioni candidate: le varianti controllate di `wiki/10` diventano
esperimenti tra modelli, non solo misure.

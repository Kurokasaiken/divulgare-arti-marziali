# Formalizzazione teorica degli anelli candidati

> Per ciascun anello: il problema meccanico, l'obiettivo ottimizzato, i
> vincoli, i trade-off, perché il candidato è preferibile alle alternative,
> l'effetto sull'anello successivo, cosa è già in letteratura e cosa resta
> IPO. I candidati **non** sono la tecnica dimostrata: sono proposte
> teoriche la cui giustificazione è esplicita e contestabile.
>
> Avvertenze del Director (2026-09-21): Δ=0 non significa "già ottimale",
> significa "il candidato attuale non propone modifiche"; nessun Δ implica
> automaticamente una cattura — prima va capita l'affermazione teorica.

## Anello 0 — Distanza / spostamento

**Problema meccanico.** Portare il sistema nella condizione spaziale
necessaria al gesto, con il minimo costo in tempo e stabilità.

**Obiettivo ottimizzato.** Tempo a disposizione del gesto: ogni unità di
spostamento in più consuma tempo senza aggiungere nulla alla catena.

**Vincoli.** Distanza residua al bersaglio; base di appoggio che deve
reggere la coppia di Anello 3; non telegrafare l'intenzione.

**Trade-off.** Il passo costa tempo ma permette di scegliere la
configurazione della base; la salita del bacino (osservata) spende energia
verticale — accettabile solo se è sottoprodotto dell'estensione utile,
spreco se è movimento gratuito.

**Perché il candidato.** "Minimo sufficiente" perché l'anello non produce
output — produce *condizione*. Tallone→avampiede perché il tallone dà
contatto stabile immediato all'atterraggio (area grande, assorbimento
passivo) e il rollio verso l'avampiede prepara il pivot senza secondo
appoggio. La salita del bacino è accettata ma non promossa a feature:
resta da capire se serve a liberare la rotazione (estensione che sgombra
l'anca) o è solo costo.

**Effetto sul successivo.** Definisce posizione e orientamento iniziale
del piede sinistro — l'input geometrico di Anello 1.

**Letteratura / IPO.** Footwork e step-in nello striking: letteratura
descrittiva presente, trattazione come problema di ottimo rara. IPO: la
funzione della salita del bacino; l'ampiezza esatta ottimale.

## Anello 1 — Piede sinistro / base

**Problema meccanico.** Scambiare forza orizzontale col suolo dentro il
cono d'attrito, senza slittare, permettendo (non impedendo) la rotazione
pelvica quando arriva.

**Obiettivo ottimizzato.** Massimizzare l'impulso orizzontale
trasmissibile minimizzando il momento resistente alla rotazione verticale
nel momento in cui serve ruotare.

**Vincoli.** `F_t ≤ μN` (cono d'attrito); la posizione del piede fissa dove
può stare l'asse di rotazione del corpo; la migrazione tallone→avampiede
deve completarsi prima del flip pelvico.

**Trade-off.** Contatto piccolo (avampiede): momento d'attrito resistente
alla rotazione `τ_f ∝ μN·r` piccolo → il bacino ruota con poca
resistenza, ma la base è meno stabile in avanti-indietro. Contatto grande
(pianta): stabile ma oppone momento alla rotazione. La candidata paga
stabilità per ottenere libertà rotazionale — scelta sensata solo se la
fase successiva richiede davvero rotazione sul piede.

**Perché il candidato.** Il τ resistente d'attrito scala col raggio
efficace del contatto: ruotare su avampiede costa molto meno momento che
ruotare su pianta intera. Se la tecnica richiede flip pelvico sul piede
sinistro, scaricare il tallone prima del flip è la configurazione che non
si auto-impedisce.

**Effetto sul successivo.** Determina quanto della forza spesa per
ruotare finisce in rotazione e quanto in attrito superfluo — imposta il
"rendimento" di Anello 3.

**Letteratura / IPO.** Cono d'attrito e pivot su avampiede: fisica
elementare + pratica documentata nello striking (pivot foot). IPO: che la
migrazione osservata avvenga davvero prima del flip (irrisolvibile a
17fps); il contributo effettivo dello shear (serve GRF).

## Anello 2 — Braccio sinistro / retrazione + LOCK

**Problema meccanico.** Portare l'arto nella configurazione terminale in
tempo utile, senza lasciare massa lontana dall'asse a resistere alla
rotazione del sistema.

**Obiettivo ottimizzato.** *Condizionale alla funzione*:
(a) se la funzione è vincolo per la rotazione → minimizzare `I` del braccio
rispetto all'asse tronco;
(b) se la funzione fosse trasferire momento angolare al tronco → servirebbe
massa *lontana* e in moto — candidato opposto.
La proposta adotta (a) perché la massa del braccio (~5% M) rende il
contributo di L trasferibile piccolo rispetto a quello di gambe+bacino;
ma la scelta resta aperta finché la funzione non è dimostrata.

**Vincoli.** Completare entro l'onset della rotazione (sincronia osservata);
la configurazione finale deve poter funzionare da vincolo; non telegrafare.

**Trade-off.** Tempo dedicato alla retrazione vs disponibilità del braccio
per altro; il LOCK consuma un DOF (non corregge più); mano aperta→chiusa
differita conserva un'opzione ma aggiunge un evento rapido da coordinare.

**Perché il candidato.** I planare osservato −50%: la configurazione
retratta ha già la proprietà geometrica cercata — il candidato non
modifica la geometria, modifica la *giustificazione*: il LOCK diventa il
punto in cui l'arto smette di essere massa libera e diventa struttura.

**Effetto sul successivo.** Il lato sinistro vincolato è il contrappeso
meccanico dentro cui Anello 3/4 sviluppano la rotazione del lato destro.

**Letteratura / IPO.** Backswing in CSM (Fuchs 2018), bracing prossimale
(Martins): parenti documentati. IPO: causalità del LOCK (P-A2.1),
scelta (a) vs (b), rilevanza reale del ΔI sulla dinamica completa.

## Anello 3 — Bacino

**Problema meccanico.** Generare e immettere nella catena il momento
torcente attorno all'asse verticale con ampiezza e timing utili.

**Obiettivo ottimizzato.** Momento angolare consegnato al tronco per unità
di tempo e di disturbo alla base.

**Vincoli.** Attrito disponibile ai piedi (Anello 1); coordinazione col
LOCK (Anello 2); la rotazione non deve sbilanciare la base.

**Trade-off — il punto della domanda del Director.** Tre opzioni a
confronto:

- **Lead pelvico** (bacino prima, cingolo dopo): se il cingolo resta
  indietro di un margine, la rotazione relativa pre-tende i tessuti del
  tronco e può sfruttare il ciclo allungamento-accorciamento; inoltre il
  bacino (massa maggiore) accelera quando il sistema è ancora compatto.
  *Costo:* richiede rotazione differenziale (taglio nel tronco), timing
  più difficile, e se il margine è troppo lungo il bacino decelera prima
  che il tronco raccolga — il momento si perde.
- **Simultaneo (blocco rigido):** bacino+tronco come un corpo solo.
  *Vantaggio:* nessun timing interno da sbagliare, nessuna dissipazione
  in taglio. *Costo:* l'inerzia è massima (tutto insieme), nessun effetto
  elastico.
- **Inverso (cingolo prima):** accelera la parte leggera senza impulso
  prossimale; il tronco in anticipo trascina il bacino — meccanicamente
  il più debole: momento angolare piccolo e generato dove le forze al
  suolo non possono contribuire direttamente.

**Perché il candidato (lead).** La letteratura sul lancio/striking
documenta il sequenziamento prossimale→distale come meccanismo che
massimizza la velocità distale; per il pugno, il lead pelvico è il primo
anello di quella catena. **Però** — nota onesta: per un colpo corto e
rapido il guadagno del whip può non ripagare il costo temporale; la
sincronia osservata potrebbe essere *la* soluzione corretta per questa
tecnica, non un deficit. Il candidato "lead" è quindi una congettura da
giustificare, non una correzione certa.

**Effetto sul successivo.** Determina se Anello 4 trasmette un blocco
rigido o una coppia in sequenza — cambia il problema di Anello 4.

**Letteratura / IPO.** Sequenza prossimale→distale, SSC, kinematic
sequence: documentati. IPO: che il lead esista o convenga in questo
gesto; la coppia contralaterale (serve GRF); l'ampiezza ottimale.

## Anello 4 — Tronco

**Problema meccanico.** Trasmettere il momento dal basso al braccio senza
dissiparlo in deformazione.

**Obiettivo ottimizzato.** Rigidità funzionale: abbastanza alta da non
assorbire il momento, abbastanza bassa da non eliminare i DOF correttivi
e (se il whip esiste) da permettere la rotazione differenziale.

**Vincoli.** Postura impilata (lean ≈ 0 osservato): il CoM del tronco
sbilanciato aggiungerebbe un momento gravitario che la muscolatura deve
contrastare — budget di coppia sottratto alla rotazione.

**Trade-off.** Rigido = trasmissione efficiente ma nessuna correzione e
stress da taglio interno; cedevole = distribuisce errori ma disperde il
momento. Il candidato propone rigidità **modulata nel tempo** — alta solo
nella finestra di trasmissione.

**Perché il candidato.** Il momento attraversa il tronco solo se il tronco
non lo assorbe; la modulazione risolve il trade-off perché la rigidità non
deve essere costante — deve esserci quando serve. Lean ≈ 0 perché tiene
l'asse verticale vicino al CoM: la rotazione non spende momento contro la
gravità.

**Effetto sul successivo.** Consegna alla spalla destra la rotazione con
la minima perdita — e la rigidità residua determina quanta libertà ha la
mano in Anello 5.

**Letteratura / IPO.** Trunk stiffness, proximal stability for distal
mobility, impedance control: documentati come principi. IPO: la
modulazione temporale reale (serve EMG core); se esiste differenziale
fine cingolo-bacino sotto i 17fps.

## Anello 5 — Spalla destra e mano destra

**Problema meccanico.** Scegliere *quando* rilasciare il DOF della mano:
la commutazione raccolta→estensione.

**Obiettivo ottimizzato.** Velocità della mano lungo la linea d'attacco
all'impatto = somma vettoriale dei contributi: traslazione della spalla +
velocità indotta dalla rotazione + velocità di estensione del gomito.

**Vincoli.** La corsa utile dell'estensione è finita — rilasciare tardi
lascia il pugno corto; la raccolta tiene basso `I` durante la rotazione.

**Trade-off.** Ogni frame di raccolta in più conserva correzioni di mira
ma consuma la finestra di accelerazione; ogni frame di estensione in
anticipo rinuncia al contributo rotatorio ancora disponibile.

**Perché il candidato.** Il punto di commutazione proposto è *geometrico*,
non temporale: quando la rotazione smette di portare la mano verso il
bersaglio (la componente utile della velocità indotta cala), estendere
aggiunge velocità esattamente lungo la linea d'attacco. La flessione
ulteriore osservata durante la rotazione è coerente: compatta il lato
destro e tiene il DOF di estensione integro fino al rilascio.

**Effetto sul successivo.** Fissa la geometria e la velocità con cui il
sistema arriva alla configurazione finale — input diretto di Anello 6.

**Letteratura / IPO.** Release timing nel lancio, proximal-distal
sequencing: documentati; la formalizzazione come frontiera di stato è il
nostro debito (spike C-02). IPO: la variabile che commuta davvero; che il
rilascio osservato sia a quella frontiera.

## Anello 6 — Configurazione strutturale finale

**Problema meccanico.** Trasmettere il carico d'impatto attraverso la
catena col minimo momento articolare da sostenere muscolarmente.

**Obiettivo ottimizzato.** Forza trasmessa per unità di attivazione
muscolare; sicurezza articolare sotto carico.

**Vincoli.** La linea di forza deve passare vicino ai centri articolari;
il gomito non deve arrivare a iperestensione sotto impatto; il sistema
deve poter assorbire direzioni fuori asse.

**Trade-off.** Rigidità totale = trasmissione massima ma ritorno di shock
e rischio articolare; cedevolezza = protezione ma dispersione. Il margine
~165–175° compra assorbimento rinunciando a un minimo di rigidità.

**Perché il candidato.** Quando la forza passa per i centri articolari il
momento articolare `τ_j = F·d` si riduce a ~zero: la struttura porta il
carico per compressione ossea, non per contrazione — è il meccanico dietro
"poca attività muscolare percepita". Il margine angolare evita che
l'impatto scarichi sull'arresto passivo del gomito.

**Effetto sul successivo.** È l'anello terminale; la tenuta vs rimbalzo
decide lo stato da cui parte il rientro.

**Letteratura / IPO.** Effective mass e allineamento strutturale nello
striking: documentati (mapping in `08` da completare). IPO: che la
configurazione trasmessa sia davvero a basso EMG; tenuta vs snap come
scelta funzionale e non artefatto del gesto senza bersaglio.

## Stato della formalizzazione

| Anello | Candidato | Giustificazione teorica | Δ vs osservato | Debito principale |
|---|---|---|---|---|
| 0 | minimo sufficiente + rollio tallone→avampiede | costo ∝ ampiezza; condizione, non output | ~0 | funzione della salita del bacino |
| 1 | pivot su avampiede prima del flip | τ_attrito ∝ raggio contatto | ~0 | timing reale vs flip (17fps) |
| 2 | minimo I + LOCK come vincolo | scelta (a) vs (b) dipende dalla funzione | ~0 | funzione del LOCK non stabilita |
| 3 | lead pelvico prossimale→distale | SSC/sequenza pross-dist; massa grossa prima | **possibile** | lead non osservato; whip vs blocco |
| 4 | rigidità modulata + lean≈0 | trasmissione senza dissipazione | ~0 | modulazione non osservabile |
| 5 | commutazione su frontiera geometrica | somma velocità lungo linea d'attacco | ~0 (criterio da formalizzare) | variabile di commutazione ignota |
| 6 | allineamento compressivo + margine 165-175° | τ_articolare → 0 | ~0 | EMG e IMP mai misurati |

**Il nodo teorico più carico è Anello 3:** il lead pelvico è l'unico
candidato che potrebbe divergere dal gesto reale — e l'unico la cui
giustificazione (whip) potrebbe non applicarsi a un colpo corto. Prima di
testarlo va risposto: quale variabile dovrebbe migliorare (ω_tronco?
v_mano? impulso?) e a quale costo misurabile (tempo? stabilità?).

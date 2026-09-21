---
title: Anello 2 — analisi meccanica fase per fase
type: analysis
updated: 2026-09-21
---

# Anello 2 — analisi meccanica fase per fase

Banco di prova: `tools/examples/anello-2-dettaglio.json` (7 keyframe autoriali,
INT/authored). Il file è il **modello manipolabile** del gesto osservato, non la
tecnica ottimale: è il materiale su cui applicare il ciclo
osservato → analisi → alternative → candidato → predizioni.

Metodo: per ogni transizione quattro domande — **A** cosa vuole ottenere,
**B** perché questa geometria, **C** alternative possibili, **D** candidato
attuale e domande aperte.

---

## M1 · GUARDIA → SCIVOLAMENTO (0–140 ms)

**A.** Avviare la retrazione della mano con costo minimo e senza aprire la
guardia prima del necessario.

**B.** Il polso guida la flessione del gomito (T1, IPO). Candidati meccanici:

- il segmento più leggero si muove per primo: minima coppia richiesta a
  pari accelerazione;
- l'angolo del gomito resta quasi costante (~110→100°): il braccio conserva
  estensione = capacità di parata/schermo più a lungo;
- il lead distale può servire a "prendere velocità" sul componente che dovrà
  chiudersi ultimo (la mano ha la finestra di chiusura più tardiva).

**C.** Alternative: lead prossimale (gomito prima) — retrazione di massa più
rapida ma telegrafata e guardia che cade prima; simultaneo — controllo più
semplice, nessun vantaggio di sequenziamento.

**D.** Candidato: lead distale com'è. Domanda aperta: il vantaggio è inerziale
(massa piccola prima) o funzionale (schermo più a lungo)?

## M2 · SCIVOLAMENTO → ARCO MEDIO (140–300 ms)

**A.** Portare il gomito sull'arco posteriore mentre l'avambraccio supina.

**B.** Distinzione da tenere esplicita: **M2 = movimento spaziale del segmento**,
**E1 = rotazione assiale**. Sono due DOF coordinati nella stessa finestra, non
"il braccio ruota". Perché sovrapposti:

- supinare durante la traslazione distribuisce la coppia di rollio su ~240 ms
  invece di concentrarla in una sotto-fase;
- il palmo arriva orientato correttamente *al momento del LOCK*, non dopo;
- meccanismo candidato del tipo "usa il DOF mentre è libero, fissalo quando
  serve" — la stessa idea della chiusura ritardata della mano.

L'arco (non la retta) mantiene il gomito lontano dal torace durante la
discesa e evita la collisione con le costole in ingresso hikite.

**C.** Alternativa sequenziale (retrazione poi supinazione): durata maggiore,
due accelerazioni separate. Alternativa inversa: supinazione completa a guardia
alta — palmo esposto, posizione innaturale in guardia.

**D.** Candidato: combinato com'è. Domanda aperta: la forma esatta dell'arco
(A2, IPO) e se il timing di E1 influisce sul profilo della traiettoria.

## M3 · ARCO MEDIO → TRAIETTORIA STABILE (300–400 ms)

**A.** Stabilizzare la traiettoria e chiudere la mano.

**B.** C3 è il punto teoricamente più ricco dell'anello: la mano resta aperta
fino a traiettoria stabile, poi chiusura rapida. Perché mai? Ipotesi candidate
(ipo, non ancora teoria):

1. **Impedenza**: mano aperta = meno co-contrazione dell'avambraccio →
   impedenza del segmento più bassa → le correzioni di traiettoria costano
   meno e perturbano meno il resto della catena;
2. **Accoppiamento**: chiudere il pugno attiva flessori dell'avambraccio che
   condividono l'innervazione con muscoli del polso/gomito — la chiusura
   anticipata potrebbe perturbare la traiettoria (cross-talk muscolare);
3. **Preparazione terminale**: la chiusura serve solo alla configurazione
   finale (pugno contro il fianco); anticiparla non dà vantaggio e costa;
4. **Residuo appreso**: la mano aperta potrebbe non avere funzione meccanica —
   solo strategia motoria ereditata.

**La variabile del gate non è nota.** Candidati: velocità angolare del gomito
sotto soglia; direzione del vettore polso convergente; distanza residua dalla
configurazione LOCK; previsione della configurazione terminale (feedforward).

**C.** Alternative: chiusura immediata (a t=0), chiusura nel LOCK, chiusura
graduale proporzionale all'avanzamento.

**D.** Candidato: chiusura gated (open 0.6→0 su 300→400). Il file esplicita il
gate ma non la variabile: questa è la domanda teorica prioritaria.

## M4 · TRAIETTORIA STABILE → LOCK (400–480 ms)

**A.** Assestamento nella configurazione di vincolo (gomito ~45°, pugno al
fianco).

**B.** ~45° minimizza il braccio di leva della massa della mano rispetto alla
spalla → contributo inerziale del braccio alla rotazione del tronco piccolo;
posa il pugno vicino alle costole = possibile appoggio geometrico. La chiusura
è già completata prima del LOCK: il vincolo riceve un terminale già rigido.

**C.** Alternative: LOCK più aperto (60–70°, più pronto a rilasciare ma meno
compatto); più chiuso (<30°, massima compattezza ma rischio co-contrazione e
difficoltà di rilascio rapido).

**D.** ~45° com'è. Da verificare: quanto del valore è appoggio geometrico e
quanto minimo inerziale.

## M5 · LOCK → TENUTA DURANTE ROTAZIONE (480–900 ms)

**A.** Mantenere la configurazione mentre il tronco ruota (evento esterno allo
scheletro del braccio).

**B.** Il LOCK è un vincolo funzionale con finestra di validità
(L1, `constrain-next-transition`), non un'articolazione bloccata. **La domanda
fondamentale ancora aperta: che cosa viene vincolato?** Candidati:

- l'angolo del gomito (posizione);
- la relazione spaziale mano↔tronco (il pugno "ancorato" al fianco rende il
  braccio parte del frame del tronco);
- la libertà di sbandamento inerziale: durante la rotazione un braccio libero
  ritarderebbe/sbanderebbe — il LOCK impedisce il flail passivo;
- il ponte contralaterale (IPO esistente): il lato bloccato partecipa al
  bilanciamento della rotazione.

**C.** Alternativa: nessun LOCK (braccio libero) — costo zero ma flail;
frenata muscolare attiva senza contatto geometrico.

**D.** LOCK com'è. La funzione resta IPO finché non si dice *quale* variabile
deve restare ferma.

## M6 · TENUTA → RITORNO A GUARDIA (900–1250 ms)

**A.** Ritorno alla guardia: riapertura + estensione + supinazione inversa.

**B.** Speculare in senso lato all'andata; nessuna pretesa di simmetria —
il ritorno avviene a gesto concluso, con vincoli diversi.

---

## Domande teoriche aperte dell'anello (priorità)

1. **C3 — variabile del gate**: quale misura decide che la traiettoria è
   "sufficientemente stabile" da rendere la chiusura sicura? È il caso
   concreto dell'idea "tieni libero un DOF finché serve, fissalo quando
   diventa controproducente".
2. **L1 — bersaglio del LOCK**: quale variabile il LOCK tiene ferma (angolo,
   relazione mano-tronco, flail inerziale, ponte contralaterale)?
3. **V1≈V2 — razionale**: perché la configurazione ideale dovrebbe produrre
   vettori di retrazione gomito/mano simili? Candidato: semplicità di
   controllo (un solo template di direzione per due giunti) o conseguenza
   geometrica del LOCK? Sulle pose attuali divergono ~21° — non è un difetto
   da correggere, è una domanda.
4. **T1 — lead distale**: inerziale o funzionale?

## Nota epistemica sul file

- `hand.sup` e `hand.open` sono **parametri autoriali della ricostruzione**:
  l'evento di supinazione è osservato (OSS), gli angoli assegnati no.
- Le pose sono INT guidate dagli angoli osservati nel capture — non misure.
- T2: la sovrapposizione temporale retrazione/supinazione è OSS; "evento
  combinato funzionale" è INT/IPO.

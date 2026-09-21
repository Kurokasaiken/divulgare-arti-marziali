# Matrice di falsificazione

> Documento operativo post-schede: per ogni ipotesi/predizione attiva,
> quale misura la discrimina, quale risultato la supporta e quale la
> indebolisce o falsifica. Guida il design della prossima cattura densa.
> Regola: una predizione è utile solo se esiste un risultato osservabile
> che la renderebbe falsa.

Legenda strumentazione: **VD** = video/capture densa (≥100 fps);
**3D** = multi-vista o mocap con profondità reale; **GRF** = pedana di
forza / solette a pressione; **EMG** = elettromiografia;
**IMP** = bersaglio strumentato (forza d'impatto); **VAR** = confronto tra
varianti controllate del gesto.

## Predizioni attive

### P-A0.1 — ordine bacino↔braccio

*Se il bacino guida il gesto (schema APA), il flip `hips_dx` precede la
retrazione del braccio di un intervallo risolvibile; se il drive è comune
o il braccio guida, no.*

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Onset pelvico vs onset retrazione braccio | VD | Bacino precede di ≥1 frame a 100+ fps, consistente tra reps | Sincronia perfetta a 100 fps (drive comune) o braccio prima (bacino = risposta) |
| EMG core/gambe vs EMG braccio | EMG | Attivazione posturale precede quella focale (firma APA) | Ordine invertito o simultaneo |

### P-A2.1 — il LOCK influenza la rotazione del tronco

*Ritardare o eliminare il LOCK/retrazione dovrebbe alterare timing o
velocità della rotazione del tronco.*

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Confronto varianti: retrazione normale / ritardata / assente | VAR + VD | Rotazione tronco ritardata o più lenta quando il LOCK manca | Rotazione identica senza LOCK → LOCK non causale per la rotazione (possibile pura sovrapposizione temporale) |
| Velocità angolare tronco durante M2 | 3D + VD | ω maggiore quando LOCK presente e completo | ω indipendente dallo stato del LOCK |

### P-A2.2 — I stimato (ESEGUITA, INT)

*Nel modello segmentale planare, I_braccio è ~50% più basso in
configurazione retratta (5/5 reps, IC95%>0).*

| Misura | Serve | Rafforza | Indebolisce |
|---|---|---|---|
| Stessa stima su dati 3D veri | 3D | ΔI di segno e magnitudine compatibile con la stima planare | ΔI che scompare in 3D → la riduzione era artefatto di proiezione |
| Stima su esecuzioni di altri soggetti | VAR | ΔI replicabile | ΔI dipendente dal soggetto/stile |

### P-A5.1 — l'estensione segue il flip (mano raccolta)

*L'onset dell'estensione del braccio destro segue il flip pelvico/scapolare
di un margine risolvibile; variante "a spinta" con estensione anticipata
dovrebbe mostrare dinamica finale diversa.*

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Timing onset estensione vs flip pelvico | VD | Margine positivo consistente tra reps e varianti corrette | Estensione simultanea o precedente il flip |
| Confronto variante "a spinta" (estensione anticipata) | VAR + IMP | Dinamica finale diversa (velocità/forza/timing) | Nessuna differenza → il ritardo non è funzionale |
| Velocità reale del polso nel transito | VD (≥120fps) | Profilo velocità pulito | Landmark instabili anche a fps alto → problema non risolvibile così |

## Ipotesi H del registro (03) — cosa le distinguerebbe

### H1 — la base crea condizione favorevole per l'arto superiore

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Confronto con/senza passo (variante) | VAR + VD + IMP | Colpo da fermo: timing o output diverso | Nessuna differenza misurabile → il passo non contribuisce |
| GRF durante il passo | GRF | Shear/impulso orizzontale misurabile | GRF puramente verticale → nessun contributo orizzontale |

### H2 — sovrapposizione temporale riduce il tempo

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Confronto esecuzione naturale vs seriale forzata | VAR + VD | Seriale più lenta o meno efficace | Seriale equivalente → la sovrapposizione non è funzionale |

### H3 — la raccolta preserva un DOF utile

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Perturbazione durante la raccolta (target mobile) | VAR | La mano corregge la traiettoria — il DOF è usato | La mano non corregge → il DOF preservato non serve |
| Formalizzazione della condizione di commutazione | VD + modello | Esiste una regione di stato da cui il cambio è predittibile | Nessuna regolarità rilevabile → la "frontiera" non esiste nei dati |

### H4 — accelerazione terminale nell'estensione

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Profilo velocità polso nella fase finale | VD (≥120fps) o IMU | Picco accelerazione nel tratto terminale | Profilo piatto/decelerante → la componente non esiste |

### H5 — postura = compromesso output/stato successivo

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Tempo e qualità del rientro in guardia | VD | Chi colpisce con postura "compromessa" rientra peggio/più tardi | Nessuna correlazione postura↔rientro |

### H6 — condizioni sufficienti > fasi rigide (quadro teorico)

| Misura | Serve | Supporta | Falsifica/indebolisce |
|---|---|---|---|
| Variabilità tra reps nello spazio degli stati | 3D + VD | Le transizioni avvengono in una *regione* di configurazioni compatibili (UCM-like) | Transizioni legate a un unico valore soglia stretto → modello a fasi basta |
| Stessa cinematica, contesti diversi | VAR | La transizione avviene solo se il contesto lo richiede | Transizione sempre allo stesso punto → non condizionale |

## IPO residue dalle schede (non ancora predizioni formalizzate)

| IPO | Misura discriminante | Serve |
|---|---|---|
| Coppia contralaterale sul bacino (Anello 3) | Direzione e magnitudo delle shear force ai due piedi durante il flip | GRF + VD |
| "Poca attività muscolare" nella tenuta (Anello 6) | EMG braccio/spalla durante il plateau di tenuta | EMG |
| Effective mass / trasmissione strutturale (Anello 6) | Forza d'impatto e spettro al variare della configurazione | IMP + EMG |
| Trasferimento di momento braccio→tronco (Anello 2/3) | Bilancio di momento angolare segmentale durante M1→M2 | 3D + VD |
| V1 ≈ V2 (direzione retrazione ~ direzione finale pugno) | Angolo tra i due vettori di spostamento | 3D (già misurabile in 2D come proxy) |

## Requisiti minimi della cattura densa (derivati dalla matrice)

| Requisito | Sblocca |
|---|---|
| ≥100 fps (meglio 120–240) | P-A0.1, P-A5.1, H2, H4, velocità polso |
| Vista multipla / 3D reale | P-A2.2 in 3D, H6 (regione di stato), bias planare |
| Molte ripetizioni stesso gesto | variabilità, regioni di stato (H6), potenza statistica |
| Varianti controllate (senza LOCK, a spinta, senza passo, target mobile) | P-A2.1, P-A5.1, H1, H2, H3 — unica via per separare correlazione da funzione |
| GRF (pedana/solette) | coppia contralaterale, carico tallone→avampiede, H1 |
| EMG | "poca attività muscolare", APA, organizzazione del tronco |
| Bersaglio strumentato | effective mass, trasmissione |
| Conservazione dati grezzi (non solo skeleton) | ri-analisi future, stima rumore, audit |

**Nota di metodo:** le varianti controllate sono il singolo elemento che
trasforma osservazioni in esperimenti — senza di esse la matrice resta al
livello "coerente con", mai "distingue".

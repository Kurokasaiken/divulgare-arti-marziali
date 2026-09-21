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
> La colonna "candidato" resta deliberatamente vuota finché il problema
> non è formulato rigorosamente: riempirla con supposizioni sarebbe
> tornare all'intuizione. (R-024, 2026-09-21)

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
| **Candidato ottimizzato** | **APERTO** — quale ampiezza/direzione/timing dello spostamento minimizza tempo e costo posturale preservando la base utile? |
| **Cosa dovrebbe produrre** | tempo minimo a parità di output del colpo; base pronta alla rotazione |
| **Verifica** | confronto varianti ampiezza passo a parità di bersaglio (VAR+VD) |

## Anello 1 — Piede sinistro / base

| | |
|---|---|
| **Osservato** | piede sx come vincolo durante la retrazione e la rotazione (OSS cinematico: stabile durante il flip pelvico) |
| **Problema meccanico** | fornire un vincolo al suolo capace di scambiare forza orizzontale (dentro il cono d'attrito) senza slittare, posizionato per consentire la rotazione pelvica |
| **Vincoli del compito** | attrito disponibile; orientamento del piede rispetto all'asse di rotazione voluto; transizione tallone→avampiede se serve pivot |
| **Alternative** | piede piatto fisso vs pivot su avampiede; orientamento più aperto/chiuso; posizione più avanti/indietro |
| **Candidato ottimizzato** | **APERTO** — quale posizione/orientamento del piede massimizza il momento trasmissibile senza slittamento né costo articolare? |
| **Cosa dovrebbe produrre** | shear GRF utile senza slittamento; rotazione pelvica non impedita |
| **Verifica** | GRF (direzione shear) + confronto orientamenti piede (VAR) |

## Anello 2 — Braccio sinistro / retrazione + LOCK

| | |
|---|---|
| **Osservato** | retrazione+supinazione combinata, mano aperta→chiusa differita, LOCK funzionale, I planare −50% (OSS+INT) |
| **Problema meccanico** | raggiungere la configurazione terminale nel tempo giusto, minimizzando `I` rispetto all'asse di rotazione senza costi eccessivi altrove |
| **Vincoli del compito** | finestra temporale (sincronia col flip pelvico); la configurazione terminale deve servire da vincolo per la fase successiva; non telegrafare |
| **Alternative** | retrazione più/meno completa; traiettoria arcuata vs retta; mano sempre chiusa; LOCK più precoce/tardivo; nessuna retrazione |
| **Candidato ottimizzato** | **APERTO** — quale geometria terminale minimizza I (o massimizza la funzione vincolo) senza aumentare il tempo né peggiorare lo stato post-azione? Nota: la configurazione osservata **non è necessariamente** l'ottimo. |
| **Cosa dovrebbe produrre** | ΔI massimo utile; LOCK che effettivamente altera la rotazione (P-A2.1) |
| **Verifica** | P-A2.1 con varianti di LOCK; P-A2.2 in 3D su geometrie candidate |

## Anello 3 — Bacino

| | |
|---|---|
| **Osservato** | flip `hips_dx` sincrono con spalle e retrazione (±0/1 frame), salita bacino (OSS capture) |
| **Problema meccanico** | generare/trasmettere il momento torcente attorno all'asse verticale con l'ampiezza e il timing che la catena richiede |
| **Vincoli del compito** | dipende dall'ancoraggio di Anello 1; deve coordinarsi con il LOCK di Anello 2; coppia contralaterale è IPO |
| **Alternative** | rotazione pelvica ampia vs ridotta; anticipata vs sincrona; con/senza coppia contralaterale |
| **Candidato ottimizzato** | **APERTO** — quale ampiezza/timing della rotazione pelvica dà il momento necessario al costo minimo? |
| **Cosa dovrebbe produrre** | momento torcente sufficiente; nessuna perdita di base |
| **Verifica** | ordine temporale a ≥100fps (P-A0.1); GRF per la coppia; confronto ampiezze (VAR) |

## Anello 4 — Tronco

| | |
|---|---|
| **Osservato** | flip scapolare sincrono col bacino; lean ≈ 0 all'impatto (OSS capture) |
| **Problema meccanico** | trasmettere il momento dal basso al braccio senza dissiparlo: il tronco come elemento a rigidezza controllata |
| **Vincoli del compito** | troppo cedevole → dissipa; troppo rigido → un solo corpo inerziale, niente correzioni |
| **Alternative** | rigidità alta/bassa/variabile nella fase; lean positivo/nullo |
| **Candidato ottimizzato** | **APERTO** — quale livello di accoppiamento bacino↔cingolo massimizza la trasmissione? Il "dinamicamente organizzato" va operazionalizzato. |
| **Cosa dovrebbe produrre** | trasmissione del momento con minima perdita |
| **Verifica** | ritardo fine bacino→cingolo a ≥100fps; EMG core per rigidità reale |

## Anello 5 — Spalla e mano destra

| | |
|---|---|
| **Osservato** | gomito dx flette ulteriormente durante la rotazione (mano raccolta), poi estende; estensione completa ~10–15 frame dopo il flip (OSS capture) |
| **Problema meccanico** | scegliere **quando** rilasciare il DOF della mano: troppo presto perde il contributo rotatorio, troppo tardi accorcia il colpo |
| **Vincoli del compito** | la commutazione dipende da stato (posizione/velocità/errore), non da tempo fisso — "ultimo momento utile" come frontiera nello spazio degli stati |
| **Alternative** | estensione anticipata ("a spinta") / sincrona / differita; raccolta parziale vs completa |
| **Candidato ottimizzato** | **APERTO** — quale condizione di stato (non quale istante) rende ottimale la commutazione raccolta→estensione? |
| **Cosa dovrebbe produrre** | massima velocità utile della mano all'impatto |
| **Verifica** | P-A5.1 + varianti "a spinta" con bersaglio strumentato (VAR+VD+IMP) |

## Anello 6 — Configurazione strutturale finale

| | |
|---|---|
| **Osservato** | tenuta ~0.9s a gomito ~165–178°, lean ≈ 0, allineamento in proiezione (OSS capture); bassa attività muscolare percepita (empirico) |
| **Problema meccanico** | trasmettere il carico dell'impatto attraverso la catena con minimo costo muscolare e senza cedimento articolare |
| **Vincoli del compito** | margine anti-iperestensione; capacità di assorbire direzioni fuori asse; recupero post-contatto |
| **Alternative** | angolo gomito più/meno aperto; tenuta vs rimbalzo immediato; allineamenti diversi |
| **Candidato ottimizzato** | **APERTO** — quale geometria terminale massimizza la trasmissione di carico per unità di costo muscolare? |
| **Cosa dovrebbe produrre** | forza trasmessa massima a parità di EMG |
| **Verifica** | IMP + EMG: forza vs attivazione al variare dell'angolo |

## Nota metodologica

La colonna "candidato ottimizzato" è la coda di lavoro teorico del
progetto. Riempirla richiede, per ciascun anello: formulazione esplicita
del funzionale da ottimizzare, dei vincoli, e della metrica di costo —
non intuizione. Solo dopo che un candidato è formulato, la cattura densa
diventa un esperimento di confronto: gesto osservato vs gesto candidato.

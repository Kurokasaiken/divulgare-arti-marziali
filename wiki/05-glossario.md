# 05 — Glossario

Terminologia di lavoro del progetto. I termini marcati *(candidato)* non sono
ancora verificati contro la letteratura biomeccanica.

## Livelli epistemici

- **OSS** — osservazione: ciò che il video/dato mostra direttamente.
- **INT** — interpretazione: funzione attribuita a un'osservazione.
- **IPO** — ipotesi: affermazione falsificabile da sottoporre a misura.

## Struttura del modello

- **Stato** — la condizione del sistema (postura, equilibrio, configurazione
  articolare) in un istante.
- **Configurazione** — un'organizzazione del sistema che abilita o vincola i
  movimenti successivi.
- **Grado di libertà (DOF)** — un modo in cui un segmento può ancora muoversi
  utilmente.
- **Vincolo funzionale** — una configurazione che limita selettivamente i DOF
  per servire la transizione successiva. Funzionale, non necessariamente
  articolare.
- **Condizione sufficiente** — lo stato minimo che rende utile avviare la
  transizione successiva. *(candidato)*
- **Transizione condizionata** — il passaggio a una nuova configurazione
  innescato dal raggiungimento di una condizione sufficiente, non dal completamento
  del movimento precedente. *(candidato)*
- **LOCK** — configurazione terminale funzionale: continuare a usare quel DOF non
  produce più vantaggio. **Non** significa articolazione bloccata.
- **Evento temporale** — qualcosa con inizio/progressione/fine (es. supinazione,
  chiusura della mano), da non ridurre a stato finale.
- **Anello** — un segmento della catena di configurazioni (distanza, piede,
  braccio, bacino, tronco, spalla, mano). **Unità analitica del modello**, scelta
  per comodità di studio — NON una categoria anatomica o biomeccanica standard.
- **Compito (TASK)** — la struttura che definisce cosa si ottimizza: output
  desiderato, interazione target, vincoli temporali, stato post-azione richiesto,
  perturbazione ammissibile. Non esiste pugno ottimale in assoluto: esiste
  ottimo **per un compito**.
- **Stato post-azione** — la configurazione in cui il sistema si trova dopo
  l'interazione. Output del modello al pari del risultato: due strategie con lo
  stesso output immediato possono differire nello stato post-azione.
- **Principio di lavoro sui gradi di libertà** — la nostra formulazione
  operativa ("mantieni un DOF finché produce vantaggio"). **Working principle,
  non principio scientifico**: non promosso finché il mapping su letteratura
  non è completato.

## Principi

- **Minimo movimento non utile** — evitare deviazioni che non contribuiscono
  all'obiettivo; non equivale a "sempre linea retta".
- **Ultimo momento utile** — la condizione geometrica oltre la quale conservare
  un DOF allontana dalla traiettoria desiderata invece di avvicinare.
- **Anticipazione temporale** — una configurazione richiesta al tempo `t` che
  costa `Δt` va iniziata a `t − Δt`.
- **Output utile sotto vincoli** — l'obiettivo da massimizzare, vincolato dallo
  stato del sistema e dallo stato richiesto dopo l'azione.

## Biomeccanica

- **Effective mass** — massa equivalente associata alla risposta dinamica del
  sistema nell'interazione. Non "quanta massa del corpo va nel bersaglio".
- **Impulso** — `J = ∫ F(t) dt = Δp`; collega forza, durata e variazione di
  quantità di moto.
- **Momento d'inerzia** — dipende dalla distribuzione della massa rispetto
  all'asse; riducibile rendendo il sistema più compatto. La relazione con la
  velocità angolare dipende dalle coppie applicate.
- **Force couple** — coppia di forze che produce rotazione; ipotesi corrente per
  il bacino (spinta posteriore sx + anteriore dx).
- **GRF** — ground reaction force; necessaria per verificare le ipotesi di
  spinta/coppia.
- **COM** — centro di massa; non ricavabile dal solo video di pose.
- **Stability-preserving transfer** — trasferimento che conserva lo stato
  posturale utile dopo l'interazione. *(candidato)*
- **Postural cost of transfer** — costo posturale di una soluzione che ottiene
  l'output destabilizzando il sistema. *(candidato)*

## Concetti vicini in letteratura (da mappare)

kinetic chain · proximal-to-distal sequencing · summation of speed · induced
acceleration · degrees of freedom (Bernstein) · task constraints (Newell) ·
optimal feedback control (Todorov & Jordan) · motor abundance / uncontrolled
manifold (Latash) · anticipatory postural adjustments

Il mapping dettagliato vive in `08-letteratura-biomeccanica.md`.

## Le quattro categorie esplicative

Non mescolare i livelli: **meccanica** (fenomeni fisici) ≠ **biomeccanica**
(organizzazione corporea) ≠ **motor control** (decisione/coordinamento) ≠
**modello del progetto** (la nostra formalizzazione). Dettaglio in
`08-letteratura-biomeccanica.md`.

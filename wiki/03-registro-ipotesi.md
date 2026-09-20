# 03 — Registro delle ipotesi e metodo epistemico

## La regola dei tre livelli

Ogni affermazione sul movimento dichiara il suo livello:

| Livello | Signato | Esempio |
|---|---|---|
| **OSS** | Osservazione: ciò che si vede o si misura | "Il gomito si sposta posteriormente." |
| **INT** | Interpretazione: funzione meccanica attribuita | "Questa configurazione può costituire la condizione per la rotazione successiva." |
| **IPO** | Ipotesi falsificabile | "La retrazione compatta riduce il momento d'inerzia e favorisce la velocità di rotazione." |

Sono tre affermazioni completamente diverse. Il progetto fallisce se le mescola:
diventerebbe una razionalizzazione della tecnica già conosciuta.

## Ipotesi attuali

| id | Ipotesi | Stato | Cosa serve per verificarla |
|---|---|---|---|
| H1 | La configurazione della parte inferiore può creare una condizione favorevole per l'azione dell'arto superiore. | aperta | cinematica 3D + GRF; confronto con varianti |
| H2 | La sovrapposizione temporale delle azioni può ridurre il tempo complessivo senza una sequenza rigidamente seriale. | supportata cinematicamente (video: estensione arto sup. inizia prima che la parte inf. sia completa) — la causalità resta da dimostrare | timing ad alta frequenza; confronto seriale vs sovrapposto |
| H3 | Mantenere una configurazione raccolta finché utile preserva un grado di libertà funzionale per la transizione successiva. | aperta | definizione operativa di "utile"; misura della traiettoria mano |
| H4 | La fase finale dell'estensione può contenere una componente di accelerazione terminale. | aperta | video ad alta frequenza o IMU; il video a 15fps non basta |
| H5 | La postura è un compromesso tra output immediato e conservazione di una configurazione utile per lo stato successivo. | aperta | definizione di "stato successivo utile"; misura del costo posturale |
| H6 | Il movimento si descrive meglio attraverso condizioni sufficienti per le transizioni che attraverso fasi rigidamente delimitate. | quadro teorico — guida tutto il resto | coerenza del modello vs dati; confronto con modelli a fasi |

## Ipotesi specifiche emerse nella scomposizione

- **Force couple contralaterale sul bacino** (piede sx posteriore + piede dx
  anteriore → coppia). Serve: GRF, momenti, cinematica 3D.
- **V₁ ≈ V₂** — vettore finale del pugno simile in direzione al vettore di
  retrazione del gomito. Relazione geometrica del modello, da verificare, non
  legge.
- **Configurazione strutturale finale** — trasmissione del carico con poca
  attività muscolare, verificata finora solo empiricamente (spinta contro parete).

## Errori già corretti nella discussione

- ~~"il braccio compatto aumenta il momento angolare"~~ → improprio se il sistema
  è sottoposto a coppie. Forma corretta: la retrazione può ridurre il momento
  d'inerzia; la relazione con la velocità angolare dipende dalla dinamica
  complessiva.
- ~~"massimizzare la massa efficace"~~ → la massa efficace non è l'obiettivo
  universale; è una variabile che dipende dall'interazione e dal risultato
  desiderato.
- ~~"fasi sequenziali"~~ → le transizioni si sovrappongono; l'unità è la
  transizione condizionata.

## Terminologia candidata (non ancora stabilita)

- *stability-preserving transfer*
- *postural cost of transfer*
- transizione condizionata / condizione sufficiente
- configurazione terminale funzionale (invece di "lock" articolare)

Prima di adottare un termine: verificare che la letteratura (motor control,
biomeccanica del colpo) non copra già il concetto con un nome esistente.

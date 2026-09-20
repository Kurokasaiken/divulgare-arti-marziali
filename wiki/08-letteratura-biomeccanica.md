# 08 — Letteratura e mapping scientifico

> Scopo di questa pagina: evitare di reinventare terminologia esistente e capire
> quali parti del nostro modello sono (a) già note con altro nome, (b)
> combinazioni di concetti noti, (c) eventualmente formulazioni nuove.
> **Stato: parziale — mapping avviato, non completato.**

## Le quattro categorie (non sono la stessa cosa)

| Categoria | Cosa descrive | Esempi |
|---|---|---|
| **Meccanica** | Cosa succede fisicamente | quantità di moto, impulso, momento d'inerzia, coppia, GRF, effective mass |
| **Biomeccanica** | Come il corpo organizza quei fenomeni | segmentazione, joint coordination, kinetic chain, stiffness, proximal-distal sequencing, postura |
| **Motor control** | Come il sistema decide/coordina le transizioni | degrees of freedom, task constraints, coordination, anticipazione, adattamento, variabilità |
| **Modello del progetto** | La nostra formalizzazione | stato → movimento → condizione sufficiente → configurazione → vincolo → transizione |

Una confusione tipica da evitare: usare un risultato di *meccanica* (es. momento
d'inerzia) come se fosse un risultato di *motor control* (es. "il sistema sceglie
di compattarsi per accelerare"). Sono livelli diversi di spiegazione.

## Mapping concetti nostri ↔ concetti esistenti

| Concetto nostro | Concetto esistente | Relazione | Stato |
|---|---|---|---|
| Transizione condizionata | — (non trovato equivalente diretto) | possibile contributo distintivo | **da verificare** |
| Configurazione terminale funzionale ("LOCK") | constraint / endpoint configuration | parziale / sovrapposta | da verificare |
| Preservazione dei DOF | Bernstein's degrees-of-freedom problem; motor abundance | possibile relazione forte | da studiare |
| Ultimo momento utile | ? — forse descritto in optimal control / switching | possibile equivalenza con switching condition | **aperto** |
| Output utile sotto vincoli | task constraints (Newell); optimal feedback control | forte relazione | da formalizzare |
| Stabilità vs output | postural control / whole-body dynamics | da mappare | aperto |
| Sovrapposizione temporale | simultaneous vs consecutive motion sequencing (Fuchs 2018) | relazione diretta | **mappato parzialmente** |
| Anticipazione `t − Δt` | anticipatory postural adjustments / feedforward | probabile parente | da verificare |
| Stato post-azione | task-dependent terminal state / recovery posture | da mappare | aperto |

## Cosa è già noto

- **Sequenziamento del pugno.** Il pattern proximal-to-distal nel pugno diretto
  è documentato (pelvi → tronco → braccio → avambraccio → mano), con EMG e
  cinematica 3D. Choku-zuki: sequenza di attivazione con bracing dell'estremità
  prossimale, completamento in ~400 ms (Martins et al., karate portoghese).
- **Sequenziamento simultaneo vs consecutivo.** Fuchs, Lindinger & Schwameder
  (2018, *Journal of Sports Sciences*) hanno confrontato CSM e SSM nei pugni
  Wing Chun: entrambi mostrano picchi di velocità proximal-to-distal, ma in SSM
  l'**inizio** dei movimenti è simultaneo. **Questo è il riferimento più vicino
  alla nostra "sovrapposizione temporale"** — va studiato per primo.
- **Effective mass.** Misurata come rapporto forza-picco / accelerazione del
  pugno all'impatto. Studi su boxeur: cross ~31 kg, jab ~30 kg (Piorkowski/
  Lenetsky-style, MDPI Appl. Sci. 2025); jab e cross ~19 kg (~21% massa corporea)
  in studio 2024. La tecnica conta più della massa corporea assoluta.
- **Contributo degli arti inferiori.** GRF della gamba posteriore correla con
  la forza del colpo; elite vs junior boxers differiscono significativamente in
  impulso e RFD degli arti inferiori (Frontiers Physiol. 2022, lead punch).
- **Pugni su boxeur olimpici.** Walilko, Viano & Bir (2005, BJSM): biomeccanica
  dei pugni al volto in olimpionici — riferimento storico su forza e dinamica
  dell'impatto.

## Cosa è controverso / discusso

- **Effective mass come costrutto.** Turner et al. (2015, *Human Movement
  Science*, "Is effective mass in combat sports punching above its weight?")
  discutono se la effective mass sia misurata e interpretata correttamente —
  il concetto è utile ma la sua operazionalizzazione è dibattuta.
- **Sequenziale vs simultaneo.** La letteratura sportiva tende a trattare il
  proximal-to-distal come ottimo "per velocità", ma Fuchs 2018 mostra che la
  scelta dipende da contesto, requisiti situazionali e stile — **nessuna delle
  due è universalmente superiore**. Coerente con il nostro "output utile sotto
  vincoli".

## Direttamente pertinente al nostro modello

- Fuchs 2018 (CSM/SSM): la sovrapposizione temporale esiste in letteratura come
  *simultaneous initiation* — il nostro modello potrebbe essere una
  generalizzazione parametrica (non solo "tutto insieme" o "tutto in fila", ma
  condizioni sufficienti che innescano transizioni parziali). **Da verificare.**
- Task constraints (Newell 1986) e optimal feedback control (Todorov & Jordan
  2002): il nostro "output utile sotto vincoli + stato post-azione" è affine a
  *task-dependent optimization*. Il *minimal intervention principle* potrebbe
  essere parente del nostro "mantieni il DOF finché utile".
- Bernstein (1967) e motor abundance / uncontrolled manifold (Latash): il nostro
  "preserva i DOF finché utili" è probabilmente un caso particolare del problema
  dei gradi di libertà visto dal lato temporale — da studiare prima di dichiarare
  novità.

## Solo adiacente

- GRF e lower-limb kinetics: confermano che gli arti inferiori contribuiscono,
  ma non parlano di *transizioni condizionate*.
- EMG sul pugno: descrive l'attivazione muscolare, non la logica delle
  configurazioni.

## Cosa NON supporta il nostro modello (finora)

- Nessuna fonte trovata descrive la transizione come evento innescato da una
  "condizione sufficiente" geometrica/funzionale invece che da tempo o da
  completamento di fase. Potrebbe essere il punto distintivo — **oppure è già
  coperto da optimal control/switching e non l'abbiamo ancora trovato.**

## Fonti raccolte (prime letture)

- Fuchs PX, Lindinger SJ, Schwameder H (2018). *Kinematic analysis of
  proximal-to-distal and simultaneous motion sequencing of straight punches*.
  J Sports Sci. doi:10.1080/14763141.2017.1365928
- *Biomechanics of Punching — The Impact of Effective Mass and Force Transfer
  on Strike Performance*. Appl. Sci. 2025, 15(7):4008. doi:10.3390/app15074008
- *The Influence of Effective Mass on the Striking Force of Lead Jab and Rear
  Cross Punches of Boxers*. Appl. Sci. 2024, 14(17):7785.
- Walilko T, Viano DC, Bir C (2005). *Biomechanics of the head for Olympic
  boxer punches to the face*. BJSM 39(10):710-719.
- Turner AN et al. (2015). *Is effective mass in combat sports punching above
  its weight?* Hum Mov Sci. doi:10.1016/j.humov.2014.11.016
- Pinto Neto O, Magini M, Saba MMF (2007). *The Role of Effective Mass and Hand
  Speed in Kung Fu Athletes*. J Appl Biomech 23(2):139-148.
- *Biomechanics of the lead straight punch of different level boxers*.
  Front Physiol 2022. doi:10.3389/fphys.2022.1015154
- Classici da mappare: Bernstein (1967); Newell (1986) task constraints;
  Todorov & Jordan (2002) optimal feedback control; Latash, uncontrolled
  manifold / motor abundance.

## Prossimo passo su questa pagina

Leggere Fuchs 2018 per primo: se la nostra "transizione condizionata" si riduce
a SSM parametrico, il mapping chiude la questione novità; se no, la differenza
va enunciata con precisione.

# 07 — Fonti e limiti

## Provenienza del materiale

Il contenuto di questo wiki deriva da una discussione di formalizzazione
(diretta Director ↔ ChatGPT) sulla tecnica del pugno, distillata il 2026-09-20.
Non è una revisione di letteratura: dove il testo afferma qualcosa di
biomeccanico, il livello è dichiarato (OSS/INT/IPO) e la verifica è rimandata.

## I dati landmark esistono (verificato 2026-09-20)

In `camera-fighter/mac/captures/pugno_destro/`:

- **5 reps** (`rep_001`–`rep_005`), formato `.msgpack` + meta `.json`.
- Ogni rep: **67 frame** su ~4 s. Ogni frame: `{ts (ms), seq, landmarks}`.
- **33 landmark** MediaPipe-pose per frame, coordinate **normalizzate 0..1**
  nell'immagine, terzo valore = confidence (`inFrameLikelihood`).
- **Sampling effettivo misurato: mediana 59 ms → ~17 fps** (corregge la stima
  "≈15 fps" della discussione originale; stesso ordine, stesso limite).
- Corpo intero già presente nel dato (33 landmark), anche se il lavoro finora ha
  guardato soprattutto il braccio.
- Esiste anche `stats.json` e, in `mac/`, `freeze.json`, `calibration.json` e la
  pipeline `body_model.py`/`features.py`/`combo_engine.py` che consuma questi
  frame.
- Esiste una **registrazione schermo** del replay scheletro (`.mov`, ~36fps
  container, 45.7s) — utile come visualizzazione, ma il dato vero è il msgpack.

Implicazione per lo strumento visuale: **l'import di landmark reali come
keyframe OSS è fattibile** — convertitore msgpack→JSON, poi annotazioni
INT/IPO sopra. Vedi `06-strumento-visuale.md`.

## Il video attuale

Registrazione di **pose estimation** (scheletro), non una registrazione
biomeccanica completa, a circa **17 fps** (mediana misurata sui dati).

### Cosa può mostrare

- posizioni articolari;
- traiettorie 2D;
- sequenza temporale grossolana;
- sovrapposizione di movimenti;
- configurazioni relative.

### Cosa NON può mostrare

- forza, impulso, massa efficace;
- GRF;
- spostamento reale del COM;
- causalità biomeccanica;
- trasferimento energetico;
- impatto reale.

### Limite temporale

~17 fps (1 frame ≈ 59 ms) è troppo poco per transizioni rapide. Non si possono
stabilire con sicurezza: istante della chiusura della mano, micro-transizioni,
accelerazioni terminali, timing esatto della supinazione, eventi nell'ordine di
poche decine di millisecondi.

### Osservazione utile già estratta

L'estensione dell'arto superiore inizia prima che la configurazione della parte
inferiore sia completa, e la parte inferiore continua a modificarsi mentre
l'arto superiore è già in movimento → supporta la **sovrapposizione temporale**
(cinematicamente). Non dimostra che "il movimento A causa il movimento B".

## Cosa servirebbe per andare oltre

- video ad alta frequenza (≥120–240 fps) per i timing;
- più viste o 3D per la cinematica completa;
- GRF/pedana per le ipotesi su spinte e coppie;
- forza d'impatto/impulso per le ipotesi su effective mass;
- misura del costo posturale per H5.

Ogni misura entra quando risponde a una domanda già formulata — non prima
(`04-metodo-e-fasi.md`, FASE 7).

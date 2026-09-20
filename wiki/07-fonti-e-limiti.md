# 07 — Fonti e limiti

## Provenienza del materiale

Il contenuto di questo wiki deriva da una discussione di formalizzazione
(diretta Director ↔ ChatGPT) sulla tecnica del pugno, distillata il 2026-09-20.
Non è una revisione di letteratura: dove il testo afferma qualcosa di
biomeccanico, il livello è dichiarato (OSS/INT/IPO) e la verifica è rimandata.

## Il video attuale

Registrazione di **pose estimation** (scheletro), non una registrazione
biomeccanica completa, a circa **15 fps** → 1 frame ≈ 66,7 ms.

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

15 fps è troppo poco per transizioni rapide. Non si possono stabilire con
sicurezza: istante della chiusura della mano, micro-transizioni, accelerazioni
terminali, timing esatto della supinazione, eventi nell'ordine di poche decine
di millisecondi.

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

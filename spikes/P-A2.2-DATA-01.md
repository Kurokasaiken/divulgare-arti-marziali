# P-A2.2-DATA-01 — Qualità e sufficienza dei capture per la stima di I

**Data:** 2026-09-21 · **Stato:** completato (gate superato con caveat) · **Tipo:** data-gate per P-A2.2 (R-020)

## Domanda del gate

> Il capture contiene dati sufficienti per tentare P-A2.2?

## Inventario dei dati

Sorgente: `camera-fighter/mac/captures/pugno_destro/rep_001…005.msgpack`
(stream msgpack; oggetti `{landmarks, seq, ts}` alternati a marker `int 0`).

| Proprietà | Valore |
|---|---|
| Repetizioni | 5 (66–67 frame ciascuna, ~4 s) |
| Landmark | 33 per frame (topologia ML Kit Pose), sempre presenti |
| Coordinate | `x, y` **normalizzate** [0,1] + **inFrameLikelihood** come 3° elemento |
| Profondità | **ASSENTE** — il terzo valore è confidence (~0.99–1.0), non z. Confermato in `camera-fighter/mac/body_model.py` |
| Frequenza | ~17 fps effettivi (Δts ≈ 59 ms, mediana) |
| Continuità | `seq` senza gap in tutte le reps |
| Sistema di riferimento | piano immagine, non calibrato (nessuna metrica) |
| Confidenza | alta e uniforme sui landmark del braccio |

## Identificabilità della configurazione retratta — SÌ, riproducibile

Cinematica del braccio sinistro (landmarks ML Kit 11/13/15) consistente in
tutte le 5 reps:

| Fase | Frame ~ | Segnale sinistro |
|---|---|---|
| Guardia (S1) | 0–10 | angolo gomito ~110–130°, d(polso,spalla) ~0.09, gomito laterale alla linea mediana (+0.09) |
| Retrazione (M1) | 15–30 | angolo scende a ~45–65°, d(polso,spalla) dimezza (~0.03–0.05), gomito supera la mediana (−0.06/−0.08) |
| Post-retrazione / LOCK (S2) | 30–45 | configurazione retratta stabile mentre il destro è esteso (R_ang ~165–177°) |
| Ritorno | 45–55 | angolo risale |
| Guardia | 55–66 | configurazione iniziale ripristinata |

La finestra retratta (frame ~30–45) è identificabile con una regola semplice
(es. `angolo_gomito_sx < 80° AND gomito_sx oltre mediana`) — riproducibile
senza intervento manuale su tutte le reps.

## Cosa si può stimare — e cosa no

**SÌ:** `I` planare proiettata. Per l'asse verticale del tronco serve la
distanza radiale orizzontale `r = √(x²+z²)` dal baricentro/asse; il dato 2D
fornisce solo la componente immagine `x`. Si può calcolare
`I_planar = Σ mᵢ·(xᵢ − x_asse)²` in unità immagine²·massa, scalabile tramite
larghezza spalle come riferimento di scala.

**Caveat strutturale (bias, non solo rumore):** la retrazione ha componente
in profondità. Il pugno esteso punta verso la camera → `x_img` piccolo ma `r`
reale grande → `I_extended` sottostimata in proiezione planare. Direzione del
bias non verificabile senza conoscere l'azimut camera↔piano del movimento.
**P-A2.2 sarà quindi una stima planare dichiarata INT con bias documentato**,
non una stima della I orizzontale completa.

**NO:** z/profondità, velocità angolari affidabili a 17 fps sulle transizioni
rapide, calibrazione metrica assoluta (servirebbe un riferimento noto
nell'inquadratura o altezza del soggetto).

## Verdetto del gate

**SUPERATO con caveat.** I dati bastano per P-A2.2 in forma planare:

> *"Nel capture disponibile, il modello segmentale planare adottato stima un
> momento d'inerzia diverso tra la configurazione retratta (frame 30–45) e la
> configurazione di riferimento (guardia, frame 0–10)?"* — con Monte Carlo sui
> landmark e bias di proiezione dichiarato.

Non serve S4 per scoprirlo: la scoperta decisiva (2D-only) è arrivata da
questo spike, non da un'integrazione nell'editor.

## Note per P-A2.2

- Finestre suggerite per rep: guardia `0–10`, retratta `30–45` (verificabili
  con la regola sopra, non hardcodate).
- Modello segmentale minimo: avambraccio+mano e braccio come masse puntuali/
  aste ai landmark 11/13/15 (+ tronco opzionale 11/12/23/24). Pesi da tabelle
  antropometriche (de Leva 1996) — dato esterno da introdurre come IPO di
  proporzione.
- Monte Carlo: perturbare x,y dei landmark con σ stimato da jitter
  inter-frame durante le finestre statiche (la guardia iniziale fornisce un
  estimatore di rumore in-dataset).
- Risultato atteso e dichiarato: `I_estimated`, classe INT. Non dimostra la
  funzione del LOCK né che "la retrazione serve a ridurre I".

## Aperto

- Vista camera (frontale/obliqua) non documentata nel capture — incide sulla
  lettura del bias. Se serve una stima 3D vera: nuova cattura laterale o
  stereo, o upgrade pipeline a landmark con z reale.
- ~17 fps: sufficiente per configurazioni quasi-statiche (S1, S2), marginale
  per la dinamica di M1 — la desiderata v1 aveva già questo punto aperto.

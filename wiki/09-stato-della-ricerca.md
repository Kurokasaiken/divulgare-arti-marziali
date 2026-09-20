# 09 — Stato della ricerca

> Pagina di orientamento: impedisce che il progetto diventi un accumulo di
> documentazione. Aggiornarla quando cambia ciò che sappiamo.
> Ultimo aggiornamento: 2026-09-20 (bootstrap).

## CONOSCIAMO (consolidato in letteratura)

- Il pugno diretto ha un sequenziamento documentato (pelvi → tronco → arto),
  ~400 ms di completamento, contributo misurabile degli arti inferiori (GRF).
- Effective mass misurabile (forza-picco / accelerazione del pugno all'impatto);
  tecnica > massa corporea.
- Sequenziamento simultaneo vs consecutivo dei segmenti è già studiato (Fuchs
  2018, Wing Chun): nessuno dei due universalmente superiore.
- Meccanica di base: impulso `J = ∫F dt = Δp`, momento d'inerzia dipendente dalla
  distribuzione della massa, coppie di forze.

## ABBIAMO OSSERVATO (nel video / nelle prove del Director)

- L'estensione dell'arto superiore inizia prima che la configurazione della
  parte inferiore sia completa → sovrapposizione temporale (cinematica, 15fps).
- La parte inferiore continua a modificarsi mentre l'arto superiore è già in
  movimento.
- Retrazione + supinazione del braccio sinistro come evento combinato, non
  sequenziale.
- Mano sinistra: aperta → chiusura rapida quando la traiettoria è stabile.
- Configurazione finale del braccio che trasmette carico con poca attività
  muscolare (prova empirica contro parete).
- Vettore finale del pugno ≈ direzione del vettore di retrazione del gomito
  (V₁ ≈ V₂, osservazione geometrica).

## ABBIAMO INTERPRETATO

- Il piede sinistro come vincolo attivo che abilita la rotazione, non semplice
  appoggio.
- Il tronco come struttura dinamicamente organizzata (né rigida né rilassata).
- "LOCK" come configurazione terminale funzionale, non blocco articolare.
- "Ultimo momento utile" come condizione geometrica (conservare il DOF allontana
  dalla traiettoria) — formulazione ancora intuitiva, da formalizzare.
- Destabilizzazione come possibile costo sullo stato post-azione (caso lastra).

## IPOTIZZIAMO (registro completo in `03-registro-ipotesi.md`)

- H1–H6 + force couple contralaterale sul bacino + V₁≈V₂ + configurazione
  strutturale finale.

## NON SAPPIAMO

- Se "transizione condizionata" ha già un nome in letteratura (optimal control /
  switching conditions?) — mapping in `08-letteratura-biomeccanica.md`.
- Quale variabile determina esattamente il cambio di strategia ("ultimo momento
  utile"): errore geometrico? costo temporale? energetico? stato post-azione?
- Quanto il braccio compatto contribuisca causalmente alla velocità di rotazione
  (momento d'inerzia ridotto ≠ rotazione accelerata dimostrata).
- Se la forza del force couple contralaterale esiste e quanto contribuisce.
- Cosa conta come "condizione sufficiente" in termini misurabili.

## DOBBIAMO VERIFICARE

- Mapping completo dei nostri concetti su letteratura motor control
  (Bernstein, Newell, Todorov & Jordan, Latash) — iniziato, non finito.
- Fuchs 2018 in dettaglio: la nostra sovrapposizione coincide con SSM o è
  qualcosa di più generale?
- Video ad alta frequenza per i timing rapidi (chiusura mano, supinazione).
- GRF + cinematica 3D per force couple e contributo arti inferiori.
- Misura di effective mass / impulso su varianti della tecnica.

## PROSSIMA DOMANDA

> **La "condizione sufficiente" che innesca una transizione è esprimibile come
> variabile misurabile (geometrica, temporale, dinamica) — e se sì, qual è?**

Prerequisito: completare il mapping letteratura per non riformulare con parole
nostre ciò che ha già un nome.

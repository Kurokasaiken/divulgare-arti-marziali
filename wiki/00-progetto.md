# 00 — Il progetto

## Origine

Circa 30 anni di pratica nelle arti marziali e 15 di insegnamento. Il progetto
nasce dal tentativo di rispondere a una domanda che l'esperienza risolve
corporalmente ma non verbalmente: **perché** un movimento organizzato in un certo
modo funziona meglio di un altro.

## Cosa NON è

- Non è la dimostrazione che una particolare tecnica di karate è "quella corretta".
- Non è un confronto tra scuole o stili.
- Non è "studiare il mio pugno": il pugno è il **caso di studio**, non il limite
  della teoria.
- Non è motion capture: l'obiettivo non è registrare una persona e trasformarla
  in un avatar.

## Cosa è

Trasformare una **competenza motoria tacita** in un **modello esplicito** che sia:

- descrivibile;
- visualizzabile;
- misurabile;
- confrontabile;
- falsificabile;
- eventualmente generalizzabile ad altri gesti.

L'esperienza pratica è il **generatore di ipotesi**, non la prova. Ogni
affermazione dichiara il suo livello: osservazione, interpretazione o ipotesi
(regola in `AGENTS.md`, registro in `03-registro-ipotesi.md`).

## Domanda di ricerca

> È possibile formalizzare in termini biomeccanici misurabili la strategia con cui
> un movimento efficace viene costruito — come successione di configurazioni e
> transizioni condizionate — e verificare se le condizioni individuate producono
> effettivamente un vantaggio rispetto ad altre strategie motorie?

La formulazione più generale del modello (vedi `01-modello-movimento.md`):

> Il movimento come **successione temporale di configurazioni e transizioni**,
> nella quale ogni configurazione preserva o limita selettivamente i gradi di
> libertà disponibili in funzione del risultato desiderato e della configurazione
> successiva, minimizzando il movimento non utile e rispettando i vincoli
> meccanici, posturali e temporali del compito.

## Gerarchia degli obiettivi (direzione del Director, 2026-09-20)

L'obiettivo primario **non** è scoprire una nuova teoria del controllo motorio.
È costruire una **descrizione scientificamente rigorosa della tecnica**, fase
per fase, usando fisica e biomeccanica con la terminologia corretta (momento,
momento torcente `τ = r × F`, impulso, quantità di moto) — non da maestro di
arti marziali, ma "da scienziato": chiunque pratichi uno sport da combattimento
deve poterne capire la teoria del movimento, con i dubbi già sviscerati.

Ordine:

1. **Spiegare rigorosamente la tecnica** — ogni scelta definita fisicamente,
   descritta biomeccanicamente, motivata rispetto all'obiettivo, distinta
   dalle alternative, falsificabile quando è causale.
2. Identificare ciò che la letteratura già sa (usare i termini esistenti
   invece di inventarne).
3. Identificare le lacune della spiegazione.
4. Solo alla fine: valutare se resta qualcosa di realmente nuovo.

Conseguenza: scoprire che `C` ha precedenti in letteratura **non danneggia**
il progetto — è il funzionamento previsto. La novità è un possibile
sottoprodotto, non il motore.

## Definizione di "ottimale"

Non: massima forza, massima velocità, massima massa efficace, massima stabilità
— sono variabili che possono entrare in conflitto.

Sì: **massimizzare l'output utile compatibilmente con i vincoli** meccanici,
posturali, temporali e geometrici, **e con lo stato richiesto dopo l'azione**.
"Ottimale" = efficace + efficiente rispetto al compito.

## Gerarchia progetto / strumento

```
PROGETTO: ricerca / formalizzazione della tecnica del pugno
  ├── modello biomeccanico
  ├── analisi video
  ├── teoria delle configurazioni e dei vincoli
  └── strumento visuale di supporto ("Motion Mechanics Lab")
        ├── linee, archi, vettori
        ├── rotazioni, keyframe
        └── viste diverse
```

Lo strumento visuale è **al servizio** della ricerca: rende il modello leggibile
a una persona o a un'AI. Non è il progetto (dettagli in `06-strumento-visuale.md`).

## Rapporto con la letteratura

Esistono concetti vicini — *kinetic chain*, *proximal-to-distal sequencing*,
*summation of speed*, *effective mass*, *induced acceleration*, *degrees of
freedom*, *task constraints*, *motor control* — ma nessuno, preso singolarmente,
descrive la **logica temporale** delle transizioni che questo progetto cerca di
formalizzare. La terminologia candidata va verificata contro la letteratura prima
di essere adottata: non inventare termini che la letteratura già copre.

Il mapping concetto-per-concetto e le fonti raccolte sono in
`08-letteratura-biomeccanica.md`. Lì sono separate anche le **quattro categorie
esplicative** — meccanica, biomeccanica, motor control, modello del progetto —
che non vanno confuse tra loro.

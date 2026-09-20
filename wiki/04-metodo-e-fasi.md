# 04 — Metodo e fasi del progetto

## Struttura scientifica complessiva

```
ESPERIENZA PRATICA
      ↓
OSSERVAZIONE
      ↓
MODELLO CINEMATICO
      ↓
RELAZIONI TRA CONFIGURAZIONI
      ↓
IPOTESI MECCANICHE
      ↓
PREDIZIONI MISURABILI
      ↓
MISURAZIONE
      ↓
VERIFICA / FALSIFICAZIONE
      ↓
MODELLO RIVISTO
```

Il video entra soprattutto nel passaggio OSSERVAZIONE → MODELLO CINEMATICO.
Strumenti più avanzati (GRF, 3D, IMU) entrano **dopo**, quando sappiamo cosa
dobbiamo misurare.

## Le sette fasi

### FASE 1 — Definizione del problema

Definire precisamente: cosa significa "pugno ottimale"; quale risultato si
ottimizza; quali vincoli si considerano; cosa significano efficacia ed
efficienza. **Nessuna simulazione in questa fase.**

### FASE 2 — Definizione del linguaggio

Definire formalmente: stato, configurazione, grado di libertà, vincolo,
condizione sufficiente, transizione, traiettoria, evento, timing, output, stato
successivo. Fondamentale per evitare di usare "fase" per descrivere cose
diverse. → `05-glossario.md` è il suo artefatto vivente.

### FASE 3 — Scomposizione del pugno

Anello per anello (vedi `02-anatomia-del-pugno.md`): per ciascuno, stato
iniziale, movimento, traiettoria, gradi di libertà, evento di transizione,
configurazione finale, vincolo prodotto, relazione con l'anello successivo.

### FASE 4 — Separazione dei livelli

Per ogni affermazione: OSS / INT / IPO. È il filtro che impedisce al progetto di
diventare razionalizzazione della tecnica già nota. → `03-registro-ipotesi.md`.

### FASE 5 — Modello visuale

Rappresentazione **manuale** del modello: mostrare esattamente cosa si intende
quando si dice "il gomito raggiunge questa condizione e allora parte la
transizione successiva". Non serve riconoscimento automatico.
→ `06-strumento-visuale.md`.

### FASE 6 — Video

Solo dopo aver definito cosa si cerca. Il video verifica traiettorie, ordine
relativo, sovrapposizione, timing, configurazioni. Non inventa la teoria.
Limiti del video attuale in `07-fonti-e-limiti.md`.

### FASE 7 — Misurazioni

Quando le ipotesi sono abbastanza precise, si decide quali dati servono: alta
frequenza temporale, 3D, GRF, velocità/accelerazioni segmentali, COM, pressione,
forza d'impatto, impulso, effective mass, costo posturale. **La misura viene
scelta perché risponde a una domanda**, non perché possiamo misurare qualcosa.

## Cosa NON fare (ancora)

- Non fare mocap complesso, 3D realistico, AI che interpreta automaticamente la
  tecnica, simulazione fisica completa.
- Non cercare una singola "traiettoria perfetta" immutabile — il modello deve
  funzionare partendo da stati leggermente diversi.
- Non assumere le fasi come seriali.
- Non trattare la massa efficace né la stabilità come obiettivi universali.
- Non usare il video per dimostrare dinamica, forza o causalità — fornisce
  soprattutto informazione cinematica.

#!/usr/bin/env python3
"""P-A2.2 standalone — stima planare del momento d'inerzia del braccio
sinistro attorno all'asse verticale del tronco, confronto tra configurazione
di guardia e configurazione retratta.

Domanda (R-020): nel capture disponibile, il modello segmentale planare
adottato stima un I diverso tra configurazione retratta e di riferimento?

LIMITI DICHIARATI (classe INT, non misura):
- dati 2D: i landmark ML Kit portano x,y normalizzati + inFrameLikelihood;
  la profondita' non esiste -> I e' una PROIEZIONE planare, con bias
  dipendente dall'azimut camera rispetto al piano del movimento
  (spike P-A2.2-DATA-01);
- masse segmentali = frazioni de Leva 1996 della massa corporea: il
  risultato e' espresso come I/M_corpo [m^2] — serve la massa del soggetto
  per valori assoluti; il contributo del tronco e' escluso (approssimato
  costante tra le configurazioni rispetto al proprio asse);
- scala metrica da larghezza biacromiale assunta 0.40 m (IPO antropometrica);
- asse di rotazione = linea verticale per il punto medio delle spalle
  (approssimazione dell'asse tronco);
- segmenti modellati come aste omogenee tra landmark: I = m(r_com^2+L^2/12);
  mano come massa puntiforme al polso (approx. conservativa).
"""
import msgpack, math, glob, random, statistics

CAP_DIR = '/Users/faustoboni/progetti_personali/camera-fighter/mac/captures/pugno_destro'
BIACROMIAL_M = 0.40          # IPO: larghezza spalle assunta [m]
SEG = {'upper_arm': 0.0271, 'forearm': 0.0162, 'hand': 0.0061}  # de Leva 1996, frazioni M_corpo
N_MC = 2000

# indici landmark (topologia ML Kit / MediaPipe)
LS, LE, LW, RS = 11, 13, 15, 12

def ang2d(a, b, c):
    v1 = (a[0]-b[0], a[1]-b[1]); v2 = (c[0]-b[0], c[1]-b[1])
    den = math.hypot(*v1) * math.hypot(*v2) or 1
    return math.degrees(math.acos(max(-1, min(1, (v1[0]*v2[0]+v1[1]*v2[1]) / den))))

def shoulder_scale(lm):
    """metri per unita' immagine, dalla larghezza biacromiale assunta."""
    return BIACROMIAL_M / max(1e-6, abs(lm[LS][0] - lm[RS][0]))

def planar_I(lm, scale):
    """I/M_corpo [m^2] del braccio sinistro attorno all'asse verticale per
    il punto medio spalle."""
    ax = (lm[LS][0] + lm[RS][0]) / 2
    def rod(a, b, frac):
        comx = (lm[a][0] + lm[b][0]) / 2
        L = math.hypot(lm[b][0]-lm[a][0], lm[b][1]-lm[a][1]) * scale
        r = (comx - ax) * scale
        return frac * (r*r + L*L/12)
    hand_r = (lm[LW][0] - ax) * scale
    return (rod(LS, LE, SEG['upper_arm'])
            + rod(LE, LW, SEG['forearm'])
            + SEG['hand'] * hand_r * hand_r)

def windows(frames):
    """guardia = primi 10 frame; retratta = angolo gomito sx < 80 deg e
    gomito oltre la mediana delle spalle."""
    guard = list(range(10))
    retr = [i for i, o in enumerate(frames)
            if ang2d(o['landmarks'][LS], o['landmarks'][LE], o['landmarks'][LW]) < 80
            and o['landmarks'][LE][0] < (o['landmarks'][LS][0] + o['landmarks'][RS][0]) / 2]
    return guard, retr

def jitter_sigma(frames):
    """sigma del rumore landmark stimato dal jitter frame-to-frame nella
    finestra di guardia quasi statica (diff consecutive ~ N(0, 2*sigma^2))."""
    g, _ = windows(frames)
    diffs = []
    for a, b in zip(g, g[1:]):
        for idx in (LS, LE, LW, RS):
            la, lb = frames[a]['landmarks'][idx], frames[b]['landmarks'][idx]
            diffs += [lb[0]-la[0], lb[1]-la[1]]
    return statistics.stdev(diffs) / math.sqrt(2) if len(diffs) > 2 else 0.001

def med_I(frames, idxs, perturb=None):
    """mediana di I sulla finestra — robusta ai frame con landmark
    misdetectati (es. scala biacromiale che esplode)."""
    vals = []
    for i in idxs:
        lm = frames[i]['landmarks']
        if perturb:
            lm = [[p[0]+perturb(), p[1]+perturb(), p[2]] for p in lm]
        vals.append(planar_I(lm, shoulder_scale(lm)))
    return statistics.median(vals)

def run(path):
    frames = [o for o in msgpack.Unpacker(open(path, 'rb'), raw=False)
              if isinstance(o, dict)]
    g, r = windows(frames)
    if not r:
        return None
    Ig, Ir = med_I(frames, g), med_I(frames, r)
    sigma = jitter_sigma(frames)
    rng = random.Random(42)
    dI = []
    for _ in range(N_MC):
        pert = lambda: rng.gauss(0, sigma)
        dI.append(med_I(frames, g, pert) - med_I(frames, r, pert))
    dI.sort()
    return dict(n=len(frames), win=(r[0], r[-1], len(r)), Ig=Ig, Ir=Ir,
                dI=Ig-Ir, lo=dI[int(.025*N_MC)], hi=dI[int(.975*N_MC)],
                mid=statistics.mean(dI), sigma=sigma)

if __name__ == '__main__':
    results = []
    print(f"{'rep':<12} {'finestra retr':>14} {'I_guard':>10} {'I_retr':>10} {'dI':>10} {'IC95% dI':>22} {'sigma':>7}")
    for p in sorted(glob.glob(CAP_DIR + '/*.msgpack')):
        res = run(p)
        if not res:
            print(f"{p.split('/')[-1]:<12} NESSUNA finestra retratta"); continue
        results.append(res)
        w = f"{res['win'][0]}-{res['win'][1]} ({res['win'][2]}fr)"
        print(f"{p.split('/')[-1]:<12} {w:>14} {res['Ig']*1e4:9.3f}e-4 {res['Ir']*1e4:9.3f}e-4 "
              f"{res['dI']*1e4:9.3f}e-4 [{res['lo']*1e4:.3f},{res['hi']*1e4:.3f}]e-4 {res['sigma']:.4f}")
    if results:
        mg = statistics.median(r['Ig'] for r in results)
        md = statistics.median(r['dI'] for r in results)
        print(f"\npooled (mediane): I_guard={mg*1e4:.3f}e-4 I_retr={statistics.median(r['Ir'] for r in results)*1e4:.3f}e-4 "
              f"dI={md*1e4:.3f}e-4 m^2 ({md/mg*100:.0f}% di I_guard)")
        print("unita': I/M_corpo [m^2]. I assoluto = valore x massa soggetto.")

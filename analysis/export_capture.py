"""Export dei capture msgpack di camera-fighter in JSON per il viewer.

Uso (dal venv di camera-fighter, che ha msgpack):
    cd /Users/faustoboni/progetti_personali/camera-fighter
    mac/venv/bin/python \\
        /Users/faustoboni/progetti_personali/divulgare-arti-marziali/analysis/export_capture.py

Scrive tools/captures/rep_NNN.json nel repo divulgare-arti-marziali.
Ogni frame: {t_ms, landmarks: [[x,y,vis] x33]} con t_ms relativo al primo frame.
"""
import glob
import json
import math
import os
import msgpack

CAPTURES = os.path.join(os.path.dirname(__file__),
                        "..", "..", "camera-fighter", "mac", "captures", "pugno_destro")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "tools", "captures")


def frames(path):
    un = msgpack.Unpacker(raw=False)
    un.feed(open(path, "rb").read())
    return [f for f in un if isinstance(f, dict) and "landmarks" in f]


def angle(a, b, c):
    v1 = (a[0] - b[0], a[1] - b[1])
    v2 = (c[0] - b[0], c[1] - b[1])
    d = math.hypot(*v1) * math.hypot(*v2)
    if d < 1e-9:
        return 180.0
    return math.degrees(math.acos(max(-1.0, min(1.0, (v1[0]*v2[0] + v1[1]*v2[1]) / d))))


def detect_events(fs):
    """Marker degli anelli, seminati dai dati (INT: rilevamento euristico,
    raffinabile trascinando nel viewer)."""
    ev = {}
    # retrazione sx: primo frame in cui il gomito sx scende sotto 80 deg
    for i, f in enumerate(fs):
        l = f["landmarks"]
        if angle(l[11], l[13], l[15]) < 80:
            ev["retract_start"] = i
            break
    # LOCK: polso sx al minimo x nella finestra di retrazione
    if "retract_start" in ev:
        seg = fs[ev["retract_start"]:ev["retract_start"] + 20]
        best = min(range(len(seg)), key=lambda j: seg[j]["landmarks"][15][0])
        ev["lock"] = ev["retract_start"] + best
    # flip pelvico: primo frame con hips_dx positivo per >=3 frame consecutivi
    for i in range(len(fs) - 3):
        if all(fs[i + k]["landmarks"][24][0] > fs[i + k]["landmarks"][23][0]
               for k in range(3)):
            ev["pelvis_flip"] = i
            break
    # inizio estensione dx: gomito dx risale dopo il minimo nella fase flip
    ang_r = [angle(f["landmarks"][12], f["landmarks"][14], f["landmarks"][16])
             for f in fs]
    lo = ev.get("pelvis_flip", 0)
    mn = min(range(lo, min(lo + 15, len(fs))), key=lambda j: ang_r[j])
    for i in range(mn + 1, len(fs)):
        if ang_r[i] > ang_r[i - 1] + 10:
            ev["ext_start"] = i
            break
    # impatto: primo frame con gomito dx > 165
    for i, a in enumerate(ang_r):
        if a > 165:
            ev["impact"] = i
            break
    # rientro: gomito dx torna sotto 160 dopo l'impatto
    if "impact" in ev:
        for i in range(ev["impact"], len(fs)):
            if ang_r[i] < 160:
                ev["return_start"] = i
                break
    return ev


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(CAPTURES, "rep_*.msgpack"))):
        fs = frames(path)
        t0 = fs[0]["ts"]
        data = {
            "meta": {
                "source": os.path.basename(path),
                "fps_note": "stream ML Kit ~17fps, monocular",
                "units": {"position": "normalized", "time": "ms"},
                "epistemic": {"landmarks": "OSS", "events": "INT (euristico, raffinabile)"},
            },
            "events": detect_events(fs),
            "frames": [
                {"t": round(f["ts"] - t0), "lm": [[round(p[0], 4), round(p[1], 4)]
                                                  for p in f["landmarks"]]}
                for f in fs
            ],
        }
        out = os.path.join(OUT_DIR, os.path.basename(path).replace(".msgpack", ".json"))
        json.dump(data, open(out, "w"))
        print(out, len(fs), "frames", data["events"])


if __name__ == "__main__":
    main()

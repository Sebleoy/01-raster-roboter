# 01 – Raster-Roboter

Erste Übung aus Phase 1 meines Robotik-Lernplans.

Ein simulierter Roboter fährt auf einem 10×10-Raster herum, dreht sich,
weicht Hindernissen aus und zeigt seine Position an.

## Aufgabe

Öffne `roboter.py` und fülle alle Stellen mit `TODO` aus.

| Stufe | Was | Neu gelernt |
|---|---|---|
| 1 | `drehe_links()`, `drehe_rechts()` | Listen, Modulo `%` |
| 2 | `vorwaerts()` mit Rand-Prüfung | Bedingungen, Koordinaten |
| 3 | `fahre("VVRVVL")` | Schleifen über Strings |
| 4 | `zeichne()` – Raster im Terminal ausgeben | verschachtelte Schleifen |
| 5 | Hindernisse: Roboter bleibt davor stehen | Mengen (`set`) |

Koordinaten: `(0, 0)` ist **unten links**, `x` nach rechts, `y` nach oben.
Richtungen: `"N"`, `"O"`, `"S"`, `"W"`.

## Testen

```bash
python3 test_roboter.py
```

Am Anfang schlagen alle Tests fehl – das ist richtig so. Ziel: alle grün.

## Ausführen

```bash
python3 roboter.py
```

"""Raster-Roboter – Übung 01.

Fülle alle Stellen mit TODO aus. Teste mit:  python3 test_roboter.py
"""

RICHTUNGEN = ["N", "O", "S", "W"]  # im Uhrzeigersinn

# Wie verändert sich (x, y), wenn der Roboter einen Schritt fährt?
SCHRITT = {
    "N": (0, 1),
    "O": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


class Roboter:
    def __init__(self, x=0, y=0, richtung="N", breite=10, hoehe=10, hindernisse=None):
        self.x = x
        self.y = y
        self.richtung = richtung
        self.breite = breite
        self.hoehe = hoehe
        # Menge von (x, y)-Tupeln, z. B. {(2, 3), (5, 5)}
        self.hindernisse = set(hindernisse or [])

    # --- Stufe 1 -----------------------------------------------------------
    def drehe_rechts(self):
        """Um 90° im Uhrzeigersinn drehen: N -> O -> S -> W -> N."""
        # TODO: Tipp: RICHTUNGEN.index(...) und der Modulo-Operator %
        self.richtung = RICHTUNGEN[(RICHTUNGEN.index(self.richtung) + 1) % 4]
        

    def drehe_links(self):
        """Um 90° gegen den Uhrzeigersinn drehen: N -> W -> S -> O -> N."""
        self.richtung = RICHTUNGEN[(RICHTUNGEN.index(self.richtung) - 1) % 4]


    # --- Stufe 2 + 5 -------------------------------------------------------
    def vorwaerts(self):
        """Einen Schritt in Blickrichtung fahren.

        Gibt True zurück, wenn der Schritt geklappt hat.
        Gibt False zurück (und bleibt stehen), wenn das Ziel
        - außerhalb des Rasters liegt (Stufe 2) oder
        - ein Hindernis ist (Stufe 5).
        """
        dx, dy = SCHRITT[self.richtung]

        pos_x =dx + self.x
        pos_y = dy + self.y

        if pos_x >= self.breite or pos_x < 0 or pos_y >= self.hoehe or pos_y < 0:
            return False

        self.x = pos_x
        self.y = pos_y
        return True

    
    # --- Stufe 3 -----------------------------------------------------------
    def fahre(self, befehle):
        """Befehlsfolge ausführen, z. B. "VVRVL".

        V = vorwärts, L = links drehen, R = rechts drehen.
        Unbekannte Zeichen ignorieren.
        """
        # TODO
        pass

    # --- Stufe 4 -----------------------------------------------------------
    def zeichne(self):
        """Raster als String zurückgeben.

        '.' = frei, '#' = Hindernis, Roboter je nach Richtung: ^ > v <
        Die oberste Zeile ist y = hoehe-1, die unterste y = 0.
        Zeilen mit "\\n" verbinden, Zeichen in einer Zeile ohne Leerzeichen.
        """
        # TODO
        return ""

    def __repr__(self):
        return f"Roboter(x={self.x}, y={self.y}, richtung={self.richtung!r})"


if __name__ == "__main__":
    r = Roboter(hindernisse={(2, 3), (4, 4)})
    r.fahre("VVVRVV")
    print(r)
    print(r.zeichne())

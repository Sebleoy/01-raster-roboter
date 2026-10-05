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

SYMBOL = {
    "N": "^",
    "O": ">",
    "S": "v",
    "W": "<",
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
        self.richtung = RICHTUNGEN[(RICHTUNGEN.index(self.richtung) + 1) % len(RICHTUNGEN)]
        

    def drehe_links(self):
        """Um 90° gegen den Uhrzeigersinn drehen: N -> W -> S -> O -> N."""
        self.richtung = RICHTUNGEN[(RICHTUNGEN.index(self.richtung) - 1) % len(RICHTUNGEN)]


    # --- Stufe 2 + 5 -------------------------------------------------------
    def vorwaerts(self):
        """Einen Schritt in Blickrichtung fahren.

        Gibt True zurück, wenn der Schritt geklappt hat.
        Gibt False zurück (und bleibt stehen), wenn das Ziel
        - außerhalb des Rasters liegt (Stufe 2) oder
        - ein Hindernis ist (Stufe 5).
        """
        dx, dy = SCHRITT[self.richtung]

        pos_x = dx + self.x
        pos_y = dy + self.y

        if not (0 <= pos_x < self.breite and 0 <= pos_y < self.hoehe):
            return False
        if (pos_x, pos_y) in self.hindernisse:
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
        for befehl in befehle:
            if befehl == "V":
                self.vorwaerts()
            elif befehl == "L":
                self.drehe_links()
            elif befehl == "R":
                self.drehe_rechts()
        

    # --- Stufe 4 -----------------------------------------------------------
    def zeichne(self):
        """Raster als String zurückgeben.

        '.' = frei, '#' = Hindernis, Roboter je nach Richtung: ^ > v <
        Die oberste Zeile ist y = hoehe-1, die unterste y = 0.
        Zeilen mit "\\n" verbinden, Zeichen in einer Zeile ohne Leerzeichen.
        """
        zeilen = []

        for y in range(self.hoehe - 1, -1, -1):
            zeile = ""
            for x in range(self.breite):
                if y == self.y and x == self.x:
                    zeile = zeile + SYMBOL[self.richtung]
                elif (x, y) in self.hindernisse:
                    zeile = zeile + "#"
                else:
                    zeile = zeile + "."
            zeilen.append(zeile)

            


        return "\n".join(zeilen)

    def __repr__(self):
        return f"Roboter(x={self.x}, y={self.y}, richtung={self.richtung!r})"


if __name__ == "__main__":
    r = Roboter(hindernisse={(2, 3), (4, 4)})
    r.fahre("VVVRVV")
    print(r)
    print(r.zeichne())

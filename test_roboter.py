"""Tests für den Raster-Roboter.  Ausführen:  python3 test_roboter.py"""

import unittest

from roboter import Roboter


class Stufe1Drehen(unittest.TestCase):
    def test_rechts_einmal(self):
        r = Roboter()
        r.drehe_rechts()
        self.assertEqual(r.richtung, "O")

    def test_rechts_rundherum(self):
        r = Roboter()
        for _ in range(4):
            r.drehe_rechts()
        self.assertEqual(r.richtung, "N")

    def test_links_von_nord(self):
        r = Roboter()
        r.drehe_links()
        self.assertEqual(r.richtung, "W")


class Stufe2Vorwaerts(unittest.TestCase):
    def test_nach_norden(self):
        r = Roboter()
        self.assertTrue(r.vorwaerts())
        self.assertEqual((r.x, r.y), (0, 1))

    def test_rand_unten(self):
        r = Roboter(richtung="S")
        self.assertFalse(r.vorwaerts())
        self.assertEqual((r.x, r.y), (0, 0))

    def test_rand_rechts(self):
        r = Roboter(x=9, richtung="O")
        self.assertFalse(r.vorwaerts())
        self.assertEqual((r.x, r.y), (9, 0))


class Stufe3Befehle(unittest.TestCase):
    def test_befehlsfolge(self):
        r = Roboter()
        r.fahre("VVRVV")
        self.assertEqual((r.x, r.y, r.richtung), (2, 2, "O"))

    def test_unbekannte_zeichen(self):
        r = Roboter()
        r.fahre("V?xV")
        self.assertEqual((r.x, r.y), (0, 2))


class Stufe4Zeichnen(unittest.TestCase):
    def test_kleines_raster(self):
        r = Roboter(x=1, y=0, richtung="O", breite=3, hoehe=2, hindernisse={(2, 1)})
        self.assertEqual(r.zeichne(), "..#\n.>.")


class Stufe5Hindernisse(unittest.TestCase):
    def test_bleibt_vor_hindernis(self):
        r = Roboter(hindernisse={(0, 2)})
        r.fahre("VVV")
        self.assertEqual((r.x, r.y), (0, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)

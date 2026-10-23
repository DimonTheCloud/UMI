"""
Ukol 6: Kontrola rodneho cisla
=========================================================
Vytvorte GUI, ktere zkontroluje spravnost rodneho cisla (bez lomitka,
10 znaku: RRMMDD/XXXX).

Pravidla:
- pole musi byt vyplnene
- RC musi mit 10 znaku
- RC se sklada pouze z cislic
- RC musi byt delitelne 11
- hodnota mesice (znaky na pozici 2-3) musi byt 01-12 nebo 51-62
- hodnota dne (znaky na pozici 4-5) musi byt 01-31
"""

from tkinter import Tk
from tkinter import ttk

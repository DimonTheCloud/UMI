"""
Ukol 5: Vypocet kvadraticke rovnice
=========================================================
Vytvorte GUI pro vypocet korenu kvadraticke rovnice a*x^2 + b*x + c = 0.
Uzivatel zada koeficienty a, b, c a po stisknuti tlacitka "Spocitej"
se zobrazi vysledek zaokrouhleny na 2 desetinna mista. Pokud je
diskriminant zaporny, zobrazi se hlaska "Rovnice nema reseni".

Vsechny widgety umistete pomoci grid()
"""

from tkinter import Tk
from tkinter import ttk

# TODO 1: vytvorte okno, nastavte titulek a velikost (cca 420x160)
window = ...

# TODO 2: vytvorte objekt stylu a nadefinujte jeden styl
#  "Koeficient.TLabel" (napr. tucne pismo a vlastni barva textu),
#  ktery pak pouzijete pro vsechny 3 popisky a, b, c
style = ...

# TODO 3: vytvorte popisky pro "a:", "b:" a "c:", vsem nastavte
#  style="Koeficient.TLabel" a umistete je
label_a = ...
label_b = ...
label_c = ...

# TODO 4: vytvorte 3 Entry (pro a, b, c) o sirce 10 znaku a
#  umistete je
entry_a = ...
entry_b = ...
entry_c = ...


# TODO 5: napiste funkci calculate(), ktera:
#  - precte a prevede na float hodnoty z entry_a, entry_b, entry_c
#  - spocita diskriminant D = b^2 - 4*a*c
#  - pokud D >= 0, spocita oba koreny (zaokrouhlene na 2 des. mista)
#  a zobrazi je v label_vysledek
#  - pokud D < 0, zobrazi v label_vysledek text "Rovnice nema reseni"
def calculate():
    ...


# TODO 6: vytvorte tlacitko s textem "Spocitej", ktery zavola
#  calculate(), widget umistete
button_vysledek = ...

# TODO 7: vytvorte prazdny label_vysledek pro zobrazeni vysledku,
#  widget umistete
label_vysledek = ...

window.mainloop()

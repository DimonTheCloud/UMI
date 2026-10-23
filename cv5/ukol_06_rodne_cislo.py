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

from tkinter import Tk
from tkinter import ttk

window = Tk()
window.title("Kontrola rodneho cisla")
window.geometry("420x180")

label_rc = ttk.Label(window, text="Rodne cislo bez lomitka:")
label_rc.grid(row=0, column=0, padx=10, pady=15)

entry_rc = ttk.Entry(window, width=20)
entry_rc.grid(row=0, column=1, padx=10)


def kontrola():
    rc = entry_rc.get()

    if rc == "":
        vysledek = "Vyplnte rodne cislo"

    elif len(rc) != 10:
        vysledek = "Rodne cislo musi mit 10 znaku"

    elif not all(znak in "0123456789" for znak in rc):
        vysledek = "Rodne cislo musi obsahovat pouze cislice"

    else:
        mesic = int(rc[2:4])
        den = int(rc[4:6])

        if int(rc) % 11 != 0:
            vysledek = "Rodne cislo neni delitelne 11"

        elif not (1 <= mesic <= 12 or 51 <= mesic <= 62):
            vysledek = "Neplatny mesic"

        elif not (1 <= den <= 31):
            vysledek = "Neplatny den"

        else:
            vysledek = "Rodne cislo je platne podle zadanych pravidel"

    label_vysledek.config(text=vysledek)


button = ttk.Button(window, text="Zkontrolovat", command=kontrola)
button.grid(row=1, column=0, columnspan=2, pady=10)

label_vysledek = ttk.Label(window, text="")
label_vysledek.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
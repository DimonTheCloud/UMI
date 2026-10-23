"""
Ukol 2: Jednoduchy formular
=========================================================
Vytvorte GUI s jednim widgetem Label, jednim Entry a jednim Button.
Po stisknuti tlacitka se v popisku zobrazi text napsany do pole ve
formatu "Napsal jsi: text_z_entry". Pokud uzivatel nic nenapise,
zobrazi se "Nic jsi nenapsal". Widgety umistete pomoci grid()
(kazdy do vlastniho radku, sloupec 0).
"""

from tkinter import Tk
from tkinter import ttk

window = Tk()
window.title("GUI")
window.geometry("300x120")

# TODO 1: vytvorte Label s textem "Tady se zobrazi tvuj napsany
#  text" a umistete ho
label = ...

# TODO 2: vytvorte Entry o sirce 30 znaku a umistete ho
entry = ...

# TODO 3: napiste funkci zobraz_text(), ktera:
#  - precte text z entry
#  - pokud je prazdny, nastavi labelu text "Nic jsi nenapsal"
#  - jinak nastavi labelu text "Napsal jsi: " + precteny text
...

# TODO 4: vytvorte Button s textem "Zobraz text", ktery po
#  stisknuti zavola funkci zobraz_text, widget umistete
button = ...

# spusteni GUI

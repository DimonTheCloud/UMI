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

from tkinter import Tk
from tkinter import ttk

window = Tk()
window.title("Vypocet kvadraticke rovnice")
window.geometry("420x160")

style = ttk.Style()
style.configure("Koeficient.TLabel",
                foreground="blue", font=("Arial", 10, "bold"))

label_a = ttk.Label(window, text="a:", style="Koeficient.TLabel")
label_b = ttk.Label(window, text="b:", style="Koeficient.TLabel")
label_c = ttk.Label(window, text="c:", style="Koeficient.TLabel")

label_a.grid(row=0, column=0, padx=5, pady=5)
label_b.grid(row=1, column=0, padx=5, pady=5)
label_c.grid(row=2, column=0, padx=5, pady=5)

entry_a = ttk.Entry(window, width=10)
entry_b = ttk.Entry(window, width=10)
entry_c = ttk.Entry(window, width=10)

entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)


def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        label_vysledek.config(text="Zadejte platna cisla")
        return

    if a == 0:
        label_vysledek.config(text="Koeficient a nesmi byt 0")
        return

    D = b**2 - 4*a*c

    if D >= 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        label_vysledek.config(text=f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        label_vysledek.config(text="Rovnice nema reseni")


button_vysledek = ttk.Button(window, text="Spocitej", command=calculate)
button_vysledek.grid(row=3, column=0, padx=10)

label_vysledek = ttk.Label(window, text="")
label_vysledek.grid(row=3, column=1, padx=10)

window.mainloop()

# TODO 6: vytvorte tlacitko s textem "Spocitej", ktery zavola
#  calculate(), widget umistete
button_vysledek = ...

# TODO 7: vytvorte prazdny label_vysledek pro zobrazeni vysledku,
#  widget umistete
label_vysledek = ...

window.mainloop()

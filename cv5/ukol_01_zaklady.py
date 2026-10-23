"""
Ukol 1: Prvni GUI - zakladni widgety
=========================================================
Vytvorte jednoduche okno a postupne ho rozsirte o ruzne widgety
z knihovny ttk. Widgety umistete pomoci pack().
"""

from tkinter import Tk, Listbox, Label, Button
from tkinter import ttk

# TODO 1: vytvorte hlavni okno (Tk), nastavte titulek a velikost okna
window = Tk("Appka")
window.title('Moje GUI')
window.geometry('400x600')

# TODO 2: vytvorte Label s textem "Hello world!"
label = ttk.Label(window, text="Hello World", font=("Arial", 25))
label.pack(pady=10)

# TODO 3: vytvorte Entry o sirce 25 znaku
button_entry = ttk.Entry(window, width=25, font=("Arial", 15))
button_entry.pack(pady=10)
# TODO 4: vytvorte Combobox se 3 polozkami podle vlastniho vyberu
combobox = ttk.Combobox(window, values=["Hello", "no helo"])
combobox.pack(pady=10)

# TODO 5: vytvorte Checkbutton s textem "Zaskrtni me"
checkbutton = ttk.Checkbutton(window, text="pin me")
checkbutton.pack(pady=10)

# TODO 6: vytvorte Radiobutton s textem "Vyber me"
radiobutton = ttk.Radiobutton(window, text="pin me")
radiobutton.pack(pady=10)

# TODO 7: vytvorte Listbox (pozor, v ttk neexistuje - pouzijte verzi
#  z tkinter) a vlozte do nej 3 polozky pomoci .insert()
listbox = Listbox(window, height=5, width=50)
listbox.insert(0, "Hello World")
listbox.insert(1, "no helo")
listbox.pack(pady=10)

# TODO 8: vytvorte funkci close_window(), ktera zavre okno
#  a tlacitko s textem "Zavřít", ktery ji zavola

def close_window():
    window.destroy()

close_button = ttk.Button(window, text="Close", command=close_window)
close_button.pack(pady=10)


button_2 = ttk.Button(window, text="close", command=close_window)
button_2.pack(pady=10)


# spusteni GUI
window.mainloop()

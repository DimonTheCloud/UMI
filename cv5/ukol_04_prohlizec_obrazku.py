"""
Ukol 4: Prohlizec obrazku
=========================================================
Vytvorte GUI pro prohlizeni obrazku. Pri spusteni se zobrazi
"picture01.jpg". Tlacitko "Zmenit obrazek" otevre dialog pro vyber
noveho souboru, tlacitko "Zavrit" zavre okno. Vsechny widgety
umistete pomoci place().

pip install Pillow
"""

from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

window = Tk()
window.title("Prohlizec obrazku")
window.geometry("700x500")

# TODO 1: nactete "picture01.jpg" pomoci Image.open(), zmente
#  velikost pomoci resize() a prevedte na ImageTk.PhotoImage
image = ImageTk.PhotoImage(Image.open("picture01.jpg").resize((400,400)))

# TODO 2: vytvorte Label, do ktereho vlozite obrazek
#  a umistete na souradnice x=150, y=50
label = ttk.Label(window, image=image)
label.place(x=150,y=50)


# TODO 3: napiste funkci change_image(), ktera:
#  - otevre dialog pro vyber souboru (fd.askopenfilename())
#  - nacte vybrany obrazek, zmeni velikost na (400, 400) a prevede
#  na ImageTk.PhotoImage
#  - nastavi novy obrazek do labelu
#  - DULEZITE: musite si novy obrazek ulozit i do label.image
def change_image():
    path_to_image = fd.askopenfilename()
    image_new = ImageTk.PhotoImage(Image.open(path_to_image).resize((400,400)))
    label.configure(image=image_new)
    label.image = image_new



# TODO 4: vytvorte tlacitko "Zmenit obrazek", ktere zmeni obrazek
#  a tlacitko "Zavrit" pro zavreni okna, oba umistete pomoci place()
button_change = ttk.Button(window, text="Change image", command=change_image)
button_close = ttk.Button(window, text="Close", command=window.quit)

button_change.place(x=200,y=460)
button_close.place(x=450,y=460)
window.mainloop()

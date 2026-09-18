"""
Ukol 2: Cislene soustavy
==========================
Doplnte funkci prevod_do_soustavy, ktera prevede DESITKOVE (dekadicke)
cislo do zvolene cilove soustavy (2 = binarni, 8 = oktalni, 16 = hexadecimalni).
"""


def prevod_do_soustavy(cislo, soustava):
    cislice = "0123456789ABCDEF"

    # TODO 1: osetrete, ze soustava je podporovana (2, 8 nebo 16) -
    # pokud ne, vratte retezec "Pozor: nepodporovana soustava"
    ...

    if cislo == 0:
        return "0"

    vysledek = ""
    # TODO 2: doplnte prevod cisla do zvolene soustavy - funkce ma vratit
    # presne to, co bude ulozene v promenne vysledek
    ...


print("175 -> binarne: ", prevod_do_soustavy(175, 2))
print("175 -> hexa:    ", prevod_do_soustavy(175, 16))
print("143 -> oktalne: ", prevod_do_soustavy(175, 8))

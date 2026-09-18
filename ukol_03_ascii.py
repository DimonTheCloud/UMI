"""
Ukol 3: ASCII a znakove sady
===============================
Zdravotnicky system potrebuje jednoduse "zakodovat" jmeno pacienta do
cisel (napr. pro pseudonymizovany prenos dat) a pak ho zase spravne
dekodovat zpet na text.

TODO 1: doplnte funkci text_na_kody, ktera z retezce vytvori seznam
        ASCII kodu jednotlivych znaku (pouzijte vestavenou funkci ord()).
TODO 2: doplnte funkci kody_na_text, ktera ze seznamu ASCII kodu
        zrekonstruuje puvodni text (pouzijte vestavenou funkci chr()).
"""


def text_na_kody(text):
    # TODO 1
    ...


def kody_na_text(kody):
    # TODO 2
    ...


jmeno = "Novak"

kody = text_na_kody(jmeno)
print("Kody:", kody)

zpet = kody_na_text(kody)
print("Dekodovano zpet:", zpet)
print("Sedi to s puvodnim jmenem?", zpet == jmeno)

# Pokud posledni radek vypise False, vystup NENI totozny se vstupem -
# upravte svuj kod, dokud nebude "Sedi to s puvodnim jmenem?" vracet True.

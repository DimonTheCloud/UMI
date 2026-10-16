"""
Ukol 4: Najdete chyby v kodu
===============================
Kod analyzuje data o pacientech - pocita prumernou klidovou tepovou
frekvenci senioru, prumerny vek pacientu, BMI a pocet mladsich
pacientu. Najdete chyby.

Senior je pacient ve veku 65 let a vice, mladsi pacient je ten,
komu je mene nez 65 let.
"""

pacienti = [
    {"jmeno": "Adam", "vek": 72, "tf": 68},
    {"jmeno": "Bara", "vek": 45, "tf": 58},
    {"jmeno": "Cyril", "vek": 68, "tf": 82},
    {"jmeno": "Dana", "vek": 30, "tf": 62},
    {"jmeno": "Emil", "vek": 81, "tf": 90},
    {"jmeno": "Fila", "vek": 55, "tf": 65},
    {"jmeno": "Gita", "vek": 90, "tf": 76},
    {"jmeno": "Hugo", "vek": 40, "tf": 60},
    {"jmeno": "Ivo", "vek": 65, "tf": 88},
]


def je_senior(pacient, hranice_veku=65):
    return pacient["vek"] >= hranice_veku


def prumerna_tf_seniori(pacienti, hranice_veku=65):
    soucet = 0
    for pacient in pacienti:
        if je_senior(pacient, hranice_veku):
            soucet += pacient["tf"]
    pocet = 0
    for pacient in pacienti:
        if je_senior(pacient, hranice_veku):
            pocet += 1

    return soucet / pocet


def prumerny_vek_pacientu(pacienti):
    soucet = 0
    for pacient in pacienti:
        soucet += pacient["vek"]
    return soucet / len(pacienti)


def bmi(vaha_kg, vyska_cm):
    return vaha_kg / ((vyska_cm/100) ** 2)



def je_mladsi(pacient, hranice_veku=65):
    return pacient["vek"] < hranice_veku


def pocet_mladych_pacientu(pacienti, hranice_veku=65):
    mladi = []
    for pacient in pacienti:
        if je_mladsi(pacient, hranice_veku):
            mladi.append(pacient)
    return len(mladi)


print("Prumerna klidova tf senioru:", prumerna_tf_seniori(pacienti))
print("Prumerny vek pacientu:", prumerny_vek_pacientu(pacienti))
print("BMI (70 kg, 170 cm):", bmi(70, 170))
print("Pocet pacientu mladsich 65 let:", pocet_mladych_pacientu(pacienti))

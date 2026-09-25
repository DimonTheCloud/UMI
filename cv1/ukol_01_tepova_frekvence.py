"""
Ukol 1: Seznamy a cykly
========================
V nemocnicnim informacnim systemu mate ulozene namerene klidove tepove
frekvence (BPM) skupiny pacientu. Vasim ukolem je najit vsechny hodnoty,
ktere jsou MIMO fyziologicky normalni rozsah klidove tepove frekvence
dospeleho cloveka: 60-100 tepu/min (VCETNE hranicnich hodnot 60 a 100).

Postup: nejdrive napiste odhad do `moje_predikce`, pak teprve doplnte
TODO a spustte (podrobne kroky viz prezentace ke cviceni).
"""

tepova_frekvence = [58, 72, 101, 65, 88, 110, 45, 76, 99, 130, 60, 100]

# TODO 1: vase predikce - kolik hodnot bude mimo rozsah 60-100 (vcetne)?
moje_predikce = 4

# TODO 2: doplnte inicializaci promenne
mimo_rozsah = []

for hodnota in tepova_frekvence:
    # TODO 3: doplnte podminku - hodnota je MIMO klidovy rozsah 60-100 (vcetne)
    if 60 <= hodnota <= 100:
        mimo_rozsah.append(hodnota)

print(f"Vase predikce: {moje_predikce}")
print(f"Skutecny pocet mimo rozsah: {len(mimo_rozsah)}")
print("Hodnoty mimo rozsah:", mimo_rozsah)

# TODO 4: doplnte, kolik procent pacientu ma hodnotu mimo rozsah
# a vypiste zaokrouhlene na 1 desetinne misto.
podil = len(mimo_rozsah) * 100/len(tepova_frekvence)
print(f"Podil mimo rozsah: {podil:.1f} %")

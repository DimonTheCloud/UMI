"""
Ukol 4: Prace se soubory GenBank
=========================================================
Genom bakterie Staphylococcus aureus subsp. aureus NCTC 8325
(pristupove cislo NZ_LS483365), stazeny z databaze NCBI Nucleotide
ve formatu GenBank.
"""

from Bio import SeqIO
from pyexpat import features

# TODO 1: nactete GenBank soubor, ktery jste stahli z NCBI
record = SeqIO.read("sequence.gb", "genbank")


# TODO 2: vypiste jednotlive atributy - id, popis (.description) a delku sekvence
print(record.id)
print(record.annotations)
print(record.features[:2])
print(record.description)


# TODO 3: v record.features najdete CDS jehoz produkt je "staphylococcal protein A".
# Vysledek ulozte do promenne "cds"
hledany_produkt = "staphylococcal protein A"

for feature in record.features:
    if feature.type == "CDS" and feature.qualifiers["product"][0] == hledany_produkt:
        print(feature)

# TODO 4: u nalezeneho CDS vypiste jeho polohu (.location) a prelozeny protein (qualifiers["translation"])
...

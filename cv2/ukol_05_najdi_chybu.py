"""
Ukol 5: Najdete chyby v kodu
=========================================================
Funkce get_ORF ma pro zadanou nukleotidovou sekvenci najit vsech 6
cteci ramcu (3 na primem vlaknu, 3 na reverznim komplementu), kazdy
prelozit do aminokyselin (bakterialni geneticky kod) a spocitat, kolik
obsahuje stop kodonu (*). Ramec s prave jednim stop kodonem (na konci)
je platny cteci ramec - ten se ulozi do noveho FASTA souboru.
"""

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def get_ORF(sequence):
    rcomplement = sequence.reverse_complement()

    translate_sequence = []
    num_of_stop = []

    for start in range(0, 2):
        translate_sequence.append(sequence[start:].translate(table=2))
        num_of_stop.append(sequence[start:].translate(table=2).count("*"))
        translate_sequence.append(rcomplement[start:].translate(table=2))
        num_of_stop.append(sequence[start:].translate(table=2).count("*"))

    for i in range(0, len(num_of_stop)):
        if num_of_stop[i] == 1:
            filename = f"coding_ORF_{i}.fasta"
            SeqIO.write(SeqRecord(translate_sequence[i], "coding ORF"), filename, "fasta")


get_ORF(Seq("CATGAAAGTAGCGTGA"))

# TODO: spustte kod. Kolik souboru coding_ORF_*.fasta byste cekali, ze
# se ulozi? Kolik se jich skutecne ulozilo? V kodu jsou 3 chyby -
# najdete vsechny a opravte je.

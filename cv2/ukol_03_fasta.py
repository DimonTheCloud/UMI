"""
Ukol 3: Prace se soubory FASTA
=========================================================
Sekvence genomu bakterie Streptococcus pyogenes MGAS8232, stazena
z databaze NCBI Nucleotide ve formatu FASTA.
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# TODO 1: nactete FASTA soubor, ktery jste stahli z NCBI
record = SeqIO.read("streptocok.fasta", format="fasta")

# TODO 2: vypiste jednotlive atributy - id, popis (.description) a delku sekvence
print(record.id)
print(record.description)
print(len(record.seq))

# TODO 3: vyindexujte prvnich 50 nukleotidu sekvence do promenne
# "novy_uryvek"
novy_uryvek = record.seq[0:50]
print(novy_uryvek)

# TODO 4: vytvorte novy SeqRecord z "novy_uryvek" s id "Streptococcus_50NT"
novy_record = SeqRecord(novy_uryvek,id="novy_uryvek228")

# TODO 5: ulozte novy_record do souboru "streptococcus_50nt.fasta"
SeqIO.write(novy_uryvek, record, format="fasta")

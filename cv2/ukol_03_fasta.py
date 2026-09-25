"""
Ukol 3: Prace se soubory FASTA
=========================================================
Sekvence genomu bakterie Streptococcus pyogenes MGAS8232, stazena
z databaze NCBI Nucleotide ve formatu FASTA.
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# TODO 1: nactete FASTA soubor, ktery jste stahli z NCBI
record = ...

# TODO 2: vypiste jednotlive atributy - id, popis (.description) a delku sekvence
...

# TODO 3: vyindexujte prvnich 50 nukleotidu sekvence do promenne
# "novy_uryvek"
novy_uryvek = ...

# TODO 4: vytvorte novy SeqRecord z "novy_uryvek" s id "Streptococcus_50NT"
novy_record = ...

# TODO 5: ulozte novy_record do souboru "streptococcus_50nt.fasta"
...

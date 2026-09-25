"""
Ukol 2: BioPython - trida Seq
=========================================================
Biopython umi pracovat s biologickymi sekvencemi - trida Seq umoznuje
pocitat komplement, transkripci a translaci primo v Pythonu.
"""

from Bio.Seq import Seq
import Bio.Data.CodonTable
# TODO 1: vytvorte sekvenci "ATGCGTAAATGA" (trida Seq)
sequence = Seq("ATGCGTAAATGA")

# TODO 2: vypiste delku sekvence
seq_len = len(sequence)
print(seq_len)
# TODO 3: vypiste komplement a reverzni komplement sekvence
complement_seq = sequence.complement()
print(complement_seq)
reverse_complement = complement_seq.reverse_complement()
print(reverse_complement)
# TODO 4: prepiste sekvenci do mRNA (transkripce)
transcripted_seq = sequence.transcribe()
print(transcripted_seq)

# TODO 5: prelozte sekvenci do aminokyselin - nejdrive standardnim
# genetickym kodem, pak genetickym kodem pro bakterie (table=11)

seq_bacterium = sequence.translate(table="11")
print(seq_bacterium)

# TODO 6: pomoci Bio.Data.CodonTable zjistete, jake jsou START a STOP
# kodony standardniho genetickeho kodu

seq_stst = Bio.Data.CodonTable.IUPAC.transcribe(seq_bacterium)


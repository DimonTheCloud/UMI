"""
Ukol 2: BioPython - trida Seq
=========================================================
Biopython umi pracovat s biologickymi sekvencemi - trida Seq umoznuje
pocitat komplement, transkripci a translaci primo v Pythonu.
"""

from Bio.Seq import Seq

# TODO 1: vytvorte sekvenci "ATGCGTAAATGA" (trida Seq)
sequence = ...

# TODO 2: vypiste delku sekvence
...

# TODO 3: vypiste komplement a reverzni komplement sekvence
...

# TODO 4: prepiste sekvenci do mRNA (transkripce)
...

# TODO 5: prelozte sekvenci do aminokyselin - nejdrive standardnim
# genetickym kodem, pak genetickym kodem pro bakterie (table=11)
...

# TODO 6: pomoci Bio.Data.CodonTable zjistete, jake jsou START a STOP
# kodony standardniho genetickeho kodu
import Bio.Data.CodonTable

...

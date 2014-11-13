
from Bio import SeqIO 

for record in SeqIO.parse("genome.fasta", "fasta"):
    print record.id

    print record.seq
    print len(record.seq)

    print record.description
    break

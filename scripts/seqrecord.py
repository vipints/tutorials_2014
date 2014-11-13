# importing modules 
import re 
from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord

# doing an operation 
rna = "AUG"
dna = re.sub(r'U', r'T', rna)

# making seqrecods
dna = Seq(dna)
fas_rec = SeqRecord(dna, id="codon_1", description="start  codon")

# writing to a fasta file 
fh = open("codon.fa", "w")
fh.write(fas_rec.format("fasta"))
fh.close() 

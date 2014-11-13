
from Bio.Seq import Seq 

# working with sequences 
my_seq = Seq("AGTACACTGGT") 

print my_seq 

print "complement: " + my_seq.complement() 
print "reverse complement: " + my_seq.reverse_complement()
print "transcribe: " + my_seq.transcribe() 
print "my_seq[2:4]: " + my_seq[2:4]

my_rna = my_seq.transcribe()
my_dna = my_rna.back_transcribe() 

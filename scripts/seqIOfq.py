
for record in SeqIO.parse("reads.fq", "fastq"):
    print record.id

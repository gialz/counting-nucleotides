# counting_dna_nucleotides.py
def count_nucleotides(dna):
    return dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')

# Example input
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_nucleotides(dna))


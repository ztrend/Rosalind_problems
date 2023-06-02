"""
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols.
Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s
 corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by
"""
#Create a dictionary with the RNA codon table
codon = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

# Read the text file containing the RNA sequence
file_path = "/root/code/data_science/Rosalind_problems/rosalind_prot.txt"  # Replace with the actual file path
with open(file_path, "r") as file:
    rna = file.read().strip()
#Break the RNA string into a list of 3 codons
rna =[rna[i:i+3] for i in range(0,len(rna),3)]
# Create an empty list to append each protein name
protein = []
# With a for loop append to the protein list, each protein found in rna list
for cod in rna:
    if cod in codon:
        protein.append(codon[cod])
# Drop the , and join all letters except the last one, which is the stop codon
proteins = ''.join(map(str, protein[:-1]))
print(proteins)


#Alternative one liner with list comprehension
#proteins = ''.join(codon.get(rna[i:i+3], '') for i in range(0, len(rna), 3) if i + 3 <= len(rna) and codon[rna[i:i+3]] != "Stop"))

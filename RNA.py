'''
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
'''
import sys

def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python RNA.py <dna_string>")
        sys.exit(1)

    dna_string = sys.argv[1]
    rna_string = dna_to_rna(dna_string)
    print(rna_string)

# t = str(input())

# print(t.replace("T","U"))

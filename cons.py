"""Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n
 matrix has m
 rows and n
 columns. Given a matrix A
, we write Ai,j
 to indicate the value found at the intersection of row i
 and column j
.

Say that we have a collection of DNA strings, all having the same length n
. Their profile matrix is a 4×n
 matrix P
 in which P1,j
 represents the number of times that 'A' occurs in the j
th position of one of the strings, P2,j
 represents the number of times that C occurs in the j
th position, and so on (see below).

A consensus string c
 is a string of length n
 formed from our collection by taking the most common symbol at each position; the j
th symbol of c
 therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings."""

#Input 10 strings size n
#Output a dictionary of A,C,G,T with values a list of n numbers that count the key at that position and the consensus string
# We are using numpy as we will work with matrices
import numpy as np

#Input DNA strings
# DNA1 = "ATCCAGCT"
# DNA2 = "GGGCAACT"

# matrix = np.concatenate(DNA1+DNA2)


# consensus = max()


def profile_matrix_and_consensus_string(dna_strings):
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for key in profile_matrix:
        profile_matrix[key] = [0]*len(dna_strings[0])

    for dna_string in dna_strings:
        for i, nucleotide in enumerate(dna_string):
            profile_matrix[nucleotide][i] += 1

    consensus_string = ''
    for i in range(len(dna_strings[0])):
        max_nucleotide = 'A'
        for nucleotide in 'ACGT':
            if profile_matrix[nucleotide][i] > profile_matrix[max_nucleotide][i]:
                max_nucleotide = nucleotide
        consensus_string += max_nucleotide

    return profile_matrix, consensus_string


# Reading from input file
with open("input.txt", "r") as file:
    lines = file.readlines()
    dna_strings = [line.strip() for line in lines if not line.startswith(">")]

# Processing the DNA strings
profile_matrix, consensus_string = profile_matrix_and_consensus_string(dna_strings)

# Writing to output file
with open("output.txt", "w") as file:
    file.write(consensus_string + "\n")
    for nucleotide in 'ACGT':
        file.write(nucleotide + ": " + " ".join(map(str, profile_matrix[nucleotide])) + "\n")

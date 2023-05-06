#Counting DNA Nucleotides
'''
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
'''
# s = str(input("Provide a string of DNA nucleobases: "))
# a = 0
# g = 0
# c = 0
# t = 0
# for letter in s:
#     if letter == "A":
#         a += 1
#     if letter == "C":
#         c += 1
#     if letter == "G":
#         g += 1
#     if letter == "T":
#         t +=1

# print(a,c,g,t)
import sys

def count_bases(s):
    a_count = s.count('A')
    c_count = s.count('C')
    g_count = s.count('G')
    t_count = s.count('T')

    return a_count, c_count, g_count, t_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        s = sys.argv[1]
        a_count, c_count, g_count, t_count = count_bases(s)
        print(f"{a_count} {c_count} {g_count} {t_count}")
    else:
        print("Usage: python DNA.py <dna_string>")

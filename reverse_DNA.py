'''In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc of s
'''
import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def reverse_dna(dna_string):
    trans_dict = {'A':'T','T':'A','C':'G','G':'C'}
    map = dna_string.maketrans(trans_dict)
    translated = dna_string.translate(map)
    reversed_dna_string = translated[::-1]
    return reversed_dna_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python reverse_DNA.py <dna_string>")
        sys.exit(1)

    dna_string = sys.argv[1]
    reversed_dna_string = reverse_dna(dna_string)
    #Instead of printing the resutls we open a txt file
    with open('reverse_dna_string.txt', 'w') as output_file:
        output_file.write(reversed_dna_string)

if __name__=="__main__":
    main()

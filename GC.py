'''
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG

# s = str(input("Input fasta file:"))
# # First I apply sting modifications by a) removing spaces, b) spliting the string at the > position and c) removing the empty item 0
# # Next I have a list to work on with a for loop where I will apply calculations

# s = s.replace(" ", "")
# s = s.split(">")
# s.pop(0)

# # Now we have a clean list to iterate in. But the output will be based on a calculation, so we need a dictionary for this.
# dict = {}
# for index,i in enumerate(s):
#     string_id = i[:13]   # Create a key with the name of the DNA id
#     dna = i[13:]        # Create a value with the DNA string
#     g = dna.count("G")  # Count the Gs
#     c = dna.count("C")   # Count the Cs
#     gc = ((g + c)/len(dna))*100  # Calculate the GC percentage
#     dict[string_id] = gc     # Add the DNA id and the GC percentage in the dictionary

# max_value = max(dict.values())    # Get the max value from the dictionary
# max_key = max(dict, key=dict.get)  # Get the max key from the dictionary
# print(f"{max_key}\n{max_value}")   # Print the correct value


def calculate_gc_content(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    dna_dict = {}
    current_key = ''

    for line in lines:
        if line.startswith('>'):
            current_key = line[1:]  # Remove '>'
        else:
            if current_key not in dna_dict:
                dna_dict[current_key] = line
            else:
                dna_dict[current_key] += line

    gc_content_dict = {}
    for key, dna in dna_dict.items():
        gc_content = (dna.count('G') + dna.count('C')) / len(dna) * 100
        gc_content_dict[key] = gc_content

    max_key = max(gc_content_dict, key=gc_content_dict.get)
    max_value = gc_content_dict[max_key]

    print(f"{max_key}\n{max_value}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        calculate_gc_content(filename)

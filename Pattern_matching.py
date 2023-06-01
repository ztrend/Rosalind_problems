"""Write a function PatternMatching that solves the Pattern Matching Problem.
Pattern Matching Problem: Find all occurrences of a pattern in a string.
     Input: Strings Pattern and Genome.
     Output: All starting positions in Genome where Pattern appears as a substring.
Sample Input:
ATAT
GATATATGCATATACTT

Sample Output:
1 3 9
"""
import sys

def PatternMatching(Pattern, Genome):
    positions = []
    pat = len(Pattern)
    for i in range(len(Genome) - pat + 1):  # +1 to include the end
        if Genome[i:i+pat] == Pattern:  # Slice Genome to get a substring of the same length as Pattern
            positions.append(i)
    return positions




#This function has quadratic time complexity because find will be iterated over the whole sequence multiple times.
# def PatternMatching(Pattern, Genome):
#     positions = [] # output variable
#     a =0
#     for i in range(len(Genome)):
#         #This will find the first occurence of the pattern starting from the position a+i. the first attempt will start from 0.
#         # Why a+i? x tells us where the first occurence starts. So in the next iteration we don't care to go over all the letters. we just want to go one step after the first occurence.
#         # That will be i + a (which will equal to x)
#         x = Genome.find(Pattern, a+i, len(Genome))
#         if x != -1:
#             positions.append(x)
#             a = x  #
#     return positions

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <pattern> <genome>")
        sys.exit(1)

    Pattern = sys.argv[1]
    Genome = sys.argv[2]

    positions = PatternMatching(Pattern, Genome)
    print(positions)

if __name__ == "__main__":
    main()
# if __name__ == '__main__':
#     Pattern = "CTTGATCAT"
#     Genome = "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT"
#     PatternMatching(Pattern, Genome)

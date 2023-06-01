"""Write a function PatternMatching that solves the Pattern Matching Problem. Then add PatternMatching to Replication.py.
Sample Input:
ATAT
GATATATGCATATACTT

Sample Output:
1 3 9
"""
import sys

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    a =0
    for i in range(len(Genome)):
        #This will find the first occurence of the pattern starting from the position a+i. the first attempt will start from 0.
        # Why a+i? x tells us where the first occurence starts. So in the next iteration we don't care to go over all the letters. we just want to go one step after the first occurence.
        # That will be i + a (which will equal to x)
        x = Genome.find(Pattern, a+i, len(Genome))
        if x != -1:
            positions.append(x)
            a = x  #
    return positions

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

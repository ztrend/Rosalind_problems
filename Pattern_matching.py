"""Write a function PatternMatching that solves the Pattern Matching Problem. Then add PatternMatching to Replication.py.

Pattern Matching Problem: Find all occurrences of a pattern in a string.
     Input: Strings Pattern and Genome.
     Output: All starting positions in Genome where Pattern appears as a substring."""

     # fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    a =0
    for i in range(len(Genome)):
        x = Genome.find(Pattern, i+a, len(Genome))
        if x != -1:
            positions.append(x)
            a+=x
    return positions

"""Write a function PatternMatching that solves the Pattern Matching Problem. Then add PatternMatching to Replication.py.
Sample Input:
ATAT
GATATATGCATATACTT

Sample Output:
1 3 9
"""

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

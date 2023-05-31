
"""To keep multiple tasks separate and allow us to work on one task at a time, we will employ top-down programming,
in which we start at the highest level of our program and divide the work into subsequently smaller pieces. """

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

#Write a function Reverse() that takes a string Pattern and returns a string formed by reversing all the letters of Pattern.
# Recall that for strings x, y, and z, the notation z=x+y concatenates x and y together into the variable z.
def Reverse(Pattern):
    rev = ""
    for letter in Pattern:
        rev = letter + rev
    return rev

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement)."""
def Complement(Pattern):
    rev = ""
    for letter in Pattern:
        rev = letter + rev
    return rev

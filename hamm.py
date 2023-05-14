"""
Problem

Given two strings s and t of equal length,
the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s  and t

Given: Two DNA strings s  and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
"""
s = input("Input DNA string:")
t = input("Input DNA string:")

if len(s) != len(t):
    print("Input same length DNA strings")
hamming_distance = 0

if len(s) != len(t):
    print("Input same length DNA strings")
hamming_distance = 0
for index, l in enumerate(s):
    if l == t[index]:
        hamming_distance = hamming_distance
    else:
        hamming_distance += 1
print(hamming_distance)

"""We are now just about ready to solve the Frequent Words Problem.
All that remains is to append any keys to our list words if the key's corresponding value in freq is equal to m.
We leave this to you in the FrequentWords() function below."""

from frequency_map import FrequencyMap

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)# add each key to words whose corresponding frequency value is equal to m
    return words

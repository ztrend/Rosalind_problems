"""Fill in the missing part of the FrequencyMap() function below so that it computes
the frequency map of a given string Text and integer k."""

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0

    return freq

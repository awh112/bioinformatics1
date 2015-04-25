def CountNucleotides(input):
    a = input.count('A')
    c = input.count('C')
    g = input.count('G')
    t = input.count('T')

    return "a: " + str(a) + " c: " + str(c) + " g: " + str(g) + " t: " + str(t)

def PatternStartIndices(text, pattern):
    count = 0
    indexes = ""

    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            indexes += str(i) + " "
            count += 1

    return indexes

def FrequentWords(text, k):
    frequentPatterns = []
    count = []

    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(PatternCount(text, pattern))
    maxCount = max(count)
    for j in range(len(text) - k):
        if count[j] == maxCount:
            frequentPatterns.append(text[j:j+k])

    return list(set(frequentPatterns))

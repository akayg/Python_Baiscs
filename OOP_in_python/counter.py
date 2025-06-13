from collections import Counter

sentence = "test test automation python test case automation python"

# Split the sentence into words
words = sentence.split()

# Count the occurrences of each word
count = Counter(words)
print(count)
print(count.most_common(2))
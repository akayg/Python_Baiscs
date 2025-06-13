from collections import defaultdict

words = ["apple", "axe", "banana", "bat", "cat"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))

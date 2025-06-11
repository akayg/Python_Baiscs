# with open("file_handling/userdata.txt", "r") as f:
#     data = f.read()
#     counting = data.split()
#     for word in counting:
#         print(f"{word}: {counting.count(word)}")

with open("file_handling/userdata.txt", "r") as f:
    data = f.read()
    words = data.split()
    word_count = {}

    for word in words:
        word = word.lower()  # Optional: normalize casing
        word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        print(f"{word}: {count}")

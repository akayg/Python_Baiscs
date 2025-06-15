fs = frozenset([1, 2, 3])

try:
    fs.add(4)
except AttributeError:
    print("❌ Cannot modify a frozenset!")

print("Current frozenset:", fs)

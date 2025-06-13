from collections import namedtuple

Book=namedtuple("Book",["title","author","Price"])

b1 = Book("Rich dad poor dad","Rober kiyosaki","399")
b2 =Book("Bhagwat Geeta","Sri Krishna","9999")
print(b1.author)
print(b2.Price)
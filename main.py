# main.py

from models import Book, Member, Magazine, DVD


# Create library items
book = Book("Python 101", 1, "A. Rao")
book2 = Book("The Alchemist", 101, "Paulo Coelho")

magazine = Magazine("Times", 201, 99)
magazine2 = Magazine("NYT", 202, 99)

dvd = DVD("Titanic", 301, 120)


# Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=3)


# 1. Borrow items
bob.borrow(book2)
bob.borrow(magazine)
bob.borrow(dvd)

print("Bob has borrowed:", bob.borrowed_titles())


# 2. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

    bob.borrow(book)  # Already borrowed by Alice

except ValueError as e:
    print("Could not borrow:", e)


# 3. Trigger borrowing limit error
try:
    bob.borrow(magazine2)  # Bob has reached his limit

except ValueError as e:
    print("Could not borrow:", e)


# 4. Trigger item-not-borrowed error
try:
    bob.return_item(magazine2)

except ValueError as e:
    print("Could not return:", e)


# 5. Polymorphism: calculate late fees for different item types
items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 6. Display total number of items created
print("Total items created:", Book.total_items)

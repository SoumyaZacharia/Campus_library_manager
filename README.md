### Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because there are items in the class that have to be defined inside every child class. The class itself is a blueprint for DVDs, magazines, books. The @abstractmethod enforces late_fee() is implemented in every child class.
If late_fee() is not defined in DVD, it will raise TypeError and connot instantiate the class

### What happens when you read item.\_\_available from outside the class, and why do we use is_available() instead?

item.\_\_available is a private object inside the class and it cannot be accessed outise the class. We use a method of the class is_available so that it is safely accessed ensuring encapsulation

### What is the difference between LibraryItem.total_items and self.title?

total_items is a class attribute, shared by all LibraryItem objects, whereas title is an instance attribute, unique to each object.
eg. title "Alchemist", "Da Vinci Code" etc is unique to each object, whereas total_items in class will be 10 if two books have been added in library

#Create a class Book that stores details like the title, author, and price of a book
#Add methods to display the details of the book and apply a discount to the price.
#(a) Create two objects for different books and display their details. 
#(b) Apply a 10% discount to one of the books and display the updated price.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Price : ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount


# --- (a) Create two Book objects and display their details ---
book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("Data Structures", "Alice Brown", 650)

print("Before Discount:")
book1.display_details()
book2.display_details()

# --- (b) Apply 10% discount to one of the books ---
book2.apply_discount(10)

print("After 10% Discount on Book 2:")
book2.display_details()

# ============================================================
# Practical Task 1. Student Class
# ============================================================

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

student1 = Student("Asel", 19, 3.8)
student2 = Student("Timur", 21, 3.5)
student3 = Student("Dina", 20, 3.9)

for student in [student1, student2, student3]:
    print(f"Student name: {student.name}")
    print(f"Age: {student.age}")
    print(f"GPA: {student.gpa}")
    print()


# ============================================================
# Practical Task 2. Method Inside a Class
# ============================================================

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

car1 = Car("Toyota", "Camry", 2020)
car1.show_info()

car2 = Car("BMW", "X5", 2022)
car2.show_info()
print()


# ============================================================
# Practical Task 3. Constructor __init__()
# ============================================================

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print(f'"{self.title}" by {self.author}, {self.year}')

book1 = Book("Python Basics", "John Smith", 2022)
book2 = Book("OOP in Python", "Anna Brown", 2023)

book1.show_info()
book2.show_info()
print()


# ============================================================
# Practical Task 4. BankAccount Class
# ============================================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}")
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}")
            print(f"New balance: {self.balance}")

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

account = BankAccount("Asel", 5000)
account.show_balance()
account.deposit(2000)
account.withdraw(3000)
account.withdraw(10000)  # Not enough money
print()


# ============================================================
# Practical Task 5. Point Class and __str__() Method
# ============================================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
print(p1)          # (2, 3)
p1.translate(5, -1)
print(p1)          # (7, 2)

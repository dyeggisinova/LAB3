"""
class MyString:
    def getString(self):
        self.user_input = input("Enter a string: ")

    def printString(self):
        print(self.user_input.upper())

my_string = MyString()

my_string.getString()
my_string.printString()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length ** 2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

length_square = float(input("Enter the length of the square: "))  # Convert input to float for decimals
square = Square(length_square)

length_rectangle = float(input("Enter the length of the rectangle: "))
width_rectangle = float(input("Enter the width of rectangle: "))
rectangle = Rectangle(length_rectangle, width_rectangle)

print(f"Area of square: {square.area()}")
print(f"Area of rectangle: {rectangle.area()}")
    
import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x},{self.y})")

    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)** 2 +(self.y-other_point.y))
    

class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance:{self.balance}")
        else:
            print("Insufficient funds!")

account = Account("Daniya", 100)

account.deposit(50)
account.withdraw(30)
account.withdraw(150)

"""
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

numbers = [10,13,15,23,42,59,63]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)

print("Taking Input and Displaying Messages")
# Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))
# Alternative way to format a string
print("nHello %s" % myname)

print("\n Variables and Their Types")
#Python Variables


i = 138
print(f"Variable i has the value {i}")
f = 1.893
print(f"Variable f has the value {f} and its type is {type(f)}")
b = True
print(f"Variable b has the value {b}")
n = None
print(f"Variable n has the value of {n}")

# tuples
print("\n Tuples")
c = (10,20,30)
print(f"\n c[0] has the value {c[0]} and is of type: {type(c)}")
# lists
print("\n Lists")
l = ["Anna", "Tom", "John"]
l = [10,20,30]
print(f"\n l[0] has the value {l[0]} and is of type: {type(l)}")

print("\n Sets")
# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)

print("")

# Dictionary
grades = {"Yohannes" : "A", "Berhane": "B-"}
grades["Yohannes"]
grades["Asfaw"] = "D"
#create an empty Dictionary

mydictionary = dict()

#Conditionals
print("\n Conditionals")
x=10
if (x > 0):
    print("The number x is positive")
elif (x<0):
    print("The number x is negative")
else:
    print("The number x is zero")

#Loops
print("\n Loops")
for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

#Functions
print("\n Functions")
def is_even(x):
if (x % 2) == 0:
    return True
else:
    return False

#Classes
print("\n Functions")
class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)

#Using a module
#This would be a file in the same folder that would hold the functions for example
print("\n Using a Module")
def square(x):
    return x*x
# method to execute file is run from command line.
def main():
    pass

if __name__ == "__main__":
main()

#Using imports we can import the functions we want and call them whenever match_parent

from mymodule.helper_utils import square
print(square(100))

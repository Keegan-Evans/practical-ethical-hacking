#!/bin/python3
#Variables and Methods
quote = "All is fair in love and war."
print(quote)

#methods
print(quote.upper())
print(quote.lower())
print(quote.title())
print(len(quote))

# bring in math

name = "Keegan"
age = 30 #int
gpa = 3.73 #float

print(int(age))
print(int(30.1)) # int on float DOES NOT ROUND, just takes the int part

print("My name is " + name + " and I am " + str(age) + " years old")

age += 1
print(age)

birthday = 1
age += birthday
print(age)
print("\n")


# Functions Video
# mini programs

def who_am_i():
    name = "keegan"
    age = 30 
    print("My name is " + name + " and I am " + str(age) + " years old")

who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

#multiple parameters
def add(x,y):
    print(x + y)
add(5,7)

def multiply(x,y):
    return x*y

print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(16)

def nl():
    print('\n')

#Boolean expressions
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1)) 

nl()

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) # True

test_not = not True # False

nl()
#Conditional statements

def drink(money):
    if money >= 2:
        return "you got yourself a drinnk"
    else:
        return "you don't have enough money"

print(drink(3)) 
print(drink(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "we are getting a drink"
    elif (age >= 21) and (money < 5):
        return "come back with more money"
    elif (age < 21) and (money >= 5):
        return "nice try kid"
    else:
        return "you're too poor and too young"

print(alcohol (21, 5))
print(alcohol (21, 4))
print(alcohol (20, 5))
print(alcohol (11, 3))

nl()
#Lists - changeable, reorderable data structures. Each thing in the list
# is an item. Lives in brackets

movies = ["george of the jungle", 
        "apocalypse now", 
        "eternal sunshine of the spotless mind", 
        "the revenge of the sith"]

print(movies[1]) # index starts on 0 rather than 1
print(movies[0]) # prints first item on list
print(movies[1:3]) # output stops "right before" last number
print(movies[1:]) #outputs everything starting from index

'''Chapter 2 Materials
#TESTING METHODS
name = 'Paul Riggs'
print(name.upper())
print(name.lower())
greet = 'Hello!'
greeting = f"{greet} {name}"
print(greeting.upper())
print("\tYour boy is testing the tab\n\tAND the new line in strings.")'''

#Testing Stripping Methods
strip_test1 = ' some value '
strip_test2 = 'somevalue'

#This case returns false because the values have whitespace.
def testing_strip():
    if strip_test1 == strip_test2:
        print(True)
    else:
        print(False)

testing_strip()

#This will still print false because the strip method doesn't
#affect the center.
strip_test3 = strip_test1.strip()
def testing_strip1():
    if strip_test3 == strip_test2:
        print(True)
    else:
        print(False)

print(strip_test3)
print(strip_test2)
testing_strip1()

#This will print true now that it matches.
strip_test4 = ' somevalue '
def testing_strip2():
    if strip_test4.strip() == strip_test2:
        print(True)
    else:
        print(False)

testing_strip2()

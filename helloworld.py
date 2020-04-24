def add_1(x, y, z=10):
    assert type(x) == int, 'Get your shit together, thats not a number!'
    x = x + 1
    y = y + 1
    z = z + 1
    return(x, y, z)

x = int(input('Enter value for x: '))
y = int(input('Enter value for y: '))
add = add_1(x,y)
print(add)
print(add_1)
print("we've made a change to the document")

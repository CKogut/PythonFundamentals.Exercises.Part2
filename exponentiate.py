# raise x to the power of y
def exponentiate(x, y):
    return x**y

# raise x to the 4th power, calling exponentiate
def raise_to_fourth_power(x):
    return exponentiate(x, 4)

# square number, calling exponentiate
square = lambda x : exponentiate(x, 2)

# cube number, calling exponentiate
cube = lambda x : exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
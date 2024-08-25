# List comprehension is a concise way to create lists in Python. 
# I'll be comparing traditional methods of creating lists and then doind the same thing using list comprehension.

# Example 1: Creating a list of squares
# Traditional method
squares = []
for x in range(10):
    squares.append(x**2)

# Using list comprehension
squares = [x**2 for x in range(10)]

print(squares)  

# Example 2: Filtering a list
# Traditional method
even_numbers = []
for x in range(20):
    if x % 2 == 0:
        even_numbers.append(x)

# Using list comprehension
even_numbers = [x for x in range(20) if x % 2 == 0]

print(even_numbers)  

# Example 3: Creating a list of tuples
# Traditional method
coordinates = []
for x in range(3):
    for y in range(3):
        coordinates.append((x, y))

# Using list comprehension
coordinates = [(x, y) for x in range(3) for y in range(3)]

print(coordinates)  

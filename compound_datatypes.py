# A compound datatype in Python is a datatype that can contain multiple elements or values. 
# These datatypes allow you to group related data together. 
# Below I'll be going over three common examples of compound datatypes in Python:

# 1.Lists:Lists are ordered, mutable sequences of elements enclosed in square brackets.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)  
print(fruits[1])  
fruits.append("elderberry")
print(fruits)  

# 2.Tuples: Tuples are ordered, immutable sequences of elements enclosed in parentheses.
numbers = (10, 20)
print(numbers)  
print(numbers[0])  

# 3. Dictionaries: Dictionaries are unordered collections of key-value pairs enclosed in curly braces.
person = {
    "name": "Dave",
    "age": 23,
    "city": "Nairobi"
}
print(person)  
print(person["name"])  
person["occupation"] = "Engineer"
print(person)  
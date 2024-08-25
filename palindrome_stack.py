# Palindromes are words or phrases that read the same forwards and backwards lik "racecar" or "madam"
# I'll create a Python program that can determine if a given string is a palindrome. 
# For the assignment requirements, I'll use a stack data structure to keep track of characters.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Create a stack
    stack = Stack()
    
    # Push first half of the string onto the stack
    for char in cleaned_string[:len(cleaned_string)//2]:
        stack.push(char)
    
    # Determine the starting point for the second half
    start_index = len(cleaned_string)//2 + len(cleaned_string) % 2
    
    # Compare the second half with the characters in the stack
    for char in cleaned_string[start_index:]:
        if char != stack.pop():
            return False
    
    return True

# Testing the function to see if it works
test_strings = [
    "A man a plan a canal Panama",
    "race a car",
    "racecar"
    "hello",
    "madam"
    "Python"
]

for string in test_strings:
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")
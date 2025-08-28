# Day 1 - Python Basics

# List
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("First number:", numbers[4])

# Dictionary
person = {"name": "Gigieh", "role": "DBA"}
print("Dictionary:", person)
print("Name:", person["role"])

# Loop
for n in numbers:
    print("Loop item:", n)

# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Gigieh"))

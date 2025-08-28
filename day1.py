# Day 1 - Python Basics

# List
numbers = [1, 2, 3, 4, 5, 6]
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

# Function untuk hitung rata-rata
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

print("Average:", average(numbers))

# Dictionary of people
people = [
    {"name": "Andi", "age": 25},
    {"name": "Budi", "age": 30},
    {"name": "Cici", "age": 22}
]

# Loop untuk print nama dan umur
for p in people:
    print(f"{p['name']} is {p['age']} years old")

# Function untuk hitung rata-rata
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

print("Average:", average(numbers))

# Function untuk mendapatkan nilai max
def find_max(numbers):
    max_number = numbers[0]   # mulai dari elemen pertama
    for n in numbers:         # loop semua angka di list
        if n > max_number:    # kalau lebih besar dari max saat ini
            max_number = n    # ganti max_number
    return max_number

print(find_max([3, 9, 1, 7]))

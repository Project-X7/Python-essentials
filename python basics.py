# Basic types
name = "Alice"          # str (string)
age = 30                # int (integer)
score = 95.5            # float (decimal)
is_active = True        # bool (True/False)
nothing = None          # NoneType (absence of value)

# Check type
print(type(name))       # <class 'str'>


## Strings

name = "Alice"

# Common operations
print(name.upper())         # ALICE
print(name.lower())         # alice
print(len(name))            # 5
print(name.replace("A", "E"))  # Elice

# f-strings (most common way to format)
age = 30
print(f"My name is {name} and I am {age} years old")


## lists 

fruits = ["apple", "banana", "cherry"]

# Access
print(fruits[0])        # apple (first)
print(fruits[-1])       # cherry (last)

# Modify
fruits.append("mango")         # add to end
fruits.remove("banana")        # remove item
fruits.insert(1, "grape")      # insert at index

# Slice
print(fruits[0:2])      # first two items

# Loop
for fruit in fruits:
    print(fruit)

# Length
print(len(fruits))      # 4


# Key-value pairs — very common in AI (JSON responses, configs)
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "ML"]
}

# Access
print(person["name"])           # Alice
print(person.get("age"))        # 30 (safer way)

# Modify
person["age"] = 31
person["city"] = "Amsterdam"    # add new key

# Loop
for key, value in person.items():
    print(f"{key}: {value}")


age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# One-liner (ternary)
status = "Adult" if age >= 18 else "Minor"


### Data types and structures

# Basic types
name = "Maggie"          # str (string)
age = 3               # int (integer)
weight =  70.5          # float (decimal)
isActive = True        # bool (True/False)
emptyValue = None          # NoneType null value
names = ["Mohan", "Priya", "Maggie"]  # list (ordered collection)

# Check type
print(type(emptyValue))       # type of variable


# ## Strings operations

# Common operations
print(name.upper())         # uppercase
print(name.lower())         # lowerscase
print(len(name))            # length of string

# f-strings (most common way to format)
age = 30
print(f"My name is {name} and I am {age} years old")


## lists operations - names

## Access
print(names[0])        # first value in the list
print(names[-1])       # last value in the list

names.append("mango")         # add to end
names.remove("Mohan")        # remove item
print(len(names))        # length of list
## print(names)           # print list
names.insert(1, "grape")      # insert at index
print(names[0:2])      # first two items

## Loop
for n in names:
    print(n)

## Length
print(len(fruits)) 


# # Key-value pairs — very common in AI (JSON responses, configs)
# person = {
#     "name": "Alice",
#     "age": 30,
#     "skills": ["Python", "ML"]
# }

# # Access
# print(person["name"])           # Alice
# print(person.get("age"))        # 30 (safer way)

# # Modify
# person["age"] = 31
# person["city"] = "Amsterdam"    # add new key

# # Loop
# for key, value in person.items():
#     print(f"{key}: {value}")


# age = 20

# if age < 18:
#     print("Minor")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

# # One-liner (ternary)
# status = "Adult" if age >= 18 else "Minor"


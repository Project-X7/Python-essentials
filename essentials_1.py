## Data types and structures

## Basic types
name = "Maggie"          # str (string)
age = 3               # int (integer)
weight =  25.5          # float (decimal)
isActive = True        # bool (True/False)
emptyValue = None          # NoneType null value
names = ["Mohan", "Priya", "Maggie"]  # list (ordered collection)

## Check type
print(type(emptyValue))       # type of variable


## Strings operations

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


## Key-value pairs — very common in AI (JSON responses, configs)
# person = {
#     "name": "Alice",
#     "age": 30,
#     "skills": ["Python", "ML"]
# }

## Access
# print(person["name"])           # Alice
# print(person.get("age"))        # 30 (safer way)

# # Modify
# person["age"] = 31
# person["city"] = "Amsterdam"    # add new key

## Loops
# for key, value in person.items():
#     print(f"{key}: {value}")


# age = 20

# if age < 18:
#     print("Minor")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")

## One-liner (ternary)
# status = "Adult" if age >= 18 else "Minor"

## Import libraries like numpy and use them for operations

# import pandas as pd

# df = pd.read_csv("data.csv")
# df.head()               # preview
# df.describe()           # stats
# df.dropna()             # remove nulls
# df["label"].value_counts()  # class distribution

## numpy library for numerical operations

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)        # (2, 3)
# print(arr.mean())       # 3.5

# # Broadcasting — no loops needed
# arr * 2                 # [[2, 4, 6], [8, 10, 12]]
# arr[arr > 3]            # array([4, 5, 6])


## Functions and classes and example of doc strings and type hints

# from typing import Optional
 
 
# class AIModel:
#     """A simple AI model with a name, temperature, and message history.
 
#     Args:
#         name:        A label for this model.
#         temperature: Controls creativity — 0.0 (focused) to 1.0 (creative).
#     """
 
#     def __init__(self, name: str, temperature: float = 0.7) -> None:
#         self.name: str = name
#         self.temperature: float = temperature
#         self.history: list[str] = []
 
#     def send(self, message: str) -> None:
#         """Add a message to the conversation history.
 
#         Args:
#             message: The text to add.
#         """
#         self.history.append(message)
 
#     def last_message(self) -> Optional[str]:
#         """Return the most recent message, or None if history is empty."""
#         return self.history[-1] if self.history else None
 
#     def reset(self) -> None:
#         """Clear the conversation history."""
#         self.history.clear()
 
#     def __str__(self) -> str:
#         return f"AIModel(name={self.name}, messages={len(self.history)})"
 
 
##   Instantiation and usage
 
# if __name__ == "__main__":
#     model = AIModel(name="Demo", temperature=0.5)
 
#     model.send("Hello!")
#     model.send("What is AI?")
 
#     print(model)                        # AIModel(name=Demo, messages=2)
#     print(model.last_message())         # What is AI?
 
#     model.reset()
#     print(f"After reset: {len(model.history)} messages")



## example of multiple line text for building prompts

task = f"""
Please process the document at {image_path} using ocr and extract the following information in human readable format:
- Total amount
- Tax amount
- method of payment

also, check if total is correct.

"""
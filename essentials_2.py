class Dog:
    def __init__(self, name, age):  # contructor method run when Dog class is instatiated
        self.name = name
        self.age = age
    def bark(self, breed):
        if breed == "labrador":
            return "Woof! I'm a labrador!"
        elif breed == "poodle":
            return "Woof! I'm a poodle!"
        elif breed == "goldenretriever":
            return "Woof! I'm a golden retriever!"
        else:
            return "Woof! I'm a dog of unknown breed!"

dog_1 = Dog("Maggie", 3)  # create an instance of the Dog class

print(f"dog name is {dog_1.name} and dog's age is {dog_1.age}")
print(dog_1.bark("goldenretriever"))  # call the bark method on the dog instance

## abstract class example ( has some conrete methods and some abstract methods that must be implemneted by the subclass)

## Interface (contracts for classes to implement - only must implement methods for the subclass)






    

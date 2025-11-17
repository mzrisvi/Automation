# This is for Object-Oriented Programming Studies (OOPS)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Dog is making a sound")
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        print("Cat is making a sound")
        return "Meow!"
    
# Example usage
if __name__ == "__main__":
    dog = Dog(name="Dog type Buddy", breed="Golden Retriever")
    cat = Cat(name="Cat type Whiskers", color="Tabby")

    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")
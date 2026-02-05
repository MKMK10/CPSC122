class Animal():
    """
    Docstring for Animal
    """
    def __init__(self, species: str = "default species", age: int = 0) -> None:
        self._species = species
        self._age = age

    def __str__(self) -> str:
        return f"a {self._age}-year old {self._species}"

class Pet(Animal):
    """
    Docstring for Pet
    """
    def __init__(self, species: str, age: int, name: str = "default name") -> None: 
        super().__init__(species, age)
        self._name = name
    
    def __str__(self) -> None:
        str_rep = super().__str__()
        str_rep += " named " + self._name
        return str_rep

class WildAnimal(Animal):
    """
    Docstring for WildAnimal
    """
    def __init__(self, species: str, age: int, noise: str = "default noise") -> None: 
        super().__init__(species, age)
        self._ferocious_noise = noise
    
    def __str__(self) -> None:
        str_rep = super().__str__()
        str_rep += " that goes " + self._ferocious_noise
        return str_rep
    
def main():
    a1 = Animal()
    print(a1)
    a2 = Animal("cat",2)
    print(a2)

    p1 = Pet("dog", 5, "Spike")
    print(p1)

    w1 = WildAnimal("lion", 10, "Roar")
    print(w1)

    animals = [a1, a2, p1, w1] # List of animal references.
    for animal in animals:
        print(animal) # Same code, different behavior.

main()
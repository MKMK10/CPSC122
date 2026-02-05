class Animal():
    """
    Docstring for Animal
    """
    def __init__(self, species: str = "default species", age: int = 0) -> None:
        self._species = species
        self._age = age

    def __str__(self) -> str:
        return f"a {self._age}-year old {self._species}"
    
def main():
    a1 = Animal()
    print(a1)
    a2 = Animal("cat",2)
    print(a2)
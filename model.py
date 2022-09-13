#@total_ordering
class Person:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool) -> None:
        # milyen értéket ad vissza a metódus (None,Str,Bool,Int)
        self.id = id
        self.name = name
        self.age = age
        self.male = male

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    def __ne__(self, other) -> bool:
        # de ezt nem kell, __eq__ alapján automatikusan csinálja
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented  # Persont nem lehet Car-ral összehasonlitani

        return self.id < o.id

    def __gt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented
        return self.id > o.id


# class Person2:
#     def __init__(self, id: str, name: str, age: int, male: bool) -> None:
#         self._id = id  # privátság (_) miatt nem kell konstruktor előtt megadni a tipusokat
#         self._name = name
#         self._age = age
#         self._male = male


if __name__ == "__main__":
    Person.id = "ID1"
    print(Person.__dict__)
    p1 = Person("P1", "Aladár", 18, True)
    print(p1.__dict__)
    p2 = Person("P1", "Aladár", 18, True)

    # egyenlőek-e?
    print(p1 == p2)
    print(p1.__eq__(p2))
    print(Person.__eq__(p1, p2))

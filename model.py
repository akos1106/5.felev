#https://unidebhu-my.sharepoint.com/personal/olah_norbert_inf_unideb_hu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Folah%5Fnorbert%5Finf%5Funideb%5Fhu%2FDocuments%2Fkali%2Dlinux%2D2021%2E3%2Dvirtualbox%2Damd64%2Eova&parent=%2Fpersonal%2Folah%5Fnorbert%5Finf%5Funideb%5Fhu%2FDocuments&ga=1
# #@total_ordering
# class Person:
#     id: str
#     name: str
#     age: int
#     male: bool
#     def __init__(self, id: str, name: str, age: int, male: bool) -> None:
#         # milyen értéket ad vissza a metódus (None,Str,Bool,Int)
#         self.id = id
#         self.name = name
#         self.age = age
#         self.male = male
#
#     def __str__(self) -> str:
#         return "#{0}: {1} ({2}, {3})".format(self.id, self.name, self.age, self.male)
#
#     def __eq__(self, o: object) -> bool:
#         return isinstance(o, Person) and self.id == o.id
#
#     def __ne__(self, other) -> bool:
#         # de ezt nem kell, __eq__ alapján automatikusan csinálja
#         return not self.__eq__(other)
#
#     def __hash__(self) -> int:
#         return id.__hash__()
#
#     def __lt__(self, o: object) -> bool:
#         if not isinstance(o, Person):
#             return NotImplemented  # Persont nem lehet Car-ral összehasonlitani
#
#         return self.id < o.id
#
#     def __gt__(self, o: object) -> bool:
#         if not isinstance(o, Person):
#             return NotImplemented
#         return self.id > o.id
#
#
# # class Person2:
# #     def __init__(self, id: str, name: str, age: int, male: bool) -> None:
# #         self._id = id  # privátság (_) miatt nem kell konstruktor előtt megadni a tipusokat
# #         self._name = name
# #         self._age = age
# #         self._male = male
#
#
# if __name__ == "__main__":
#     Person.id = "ID1"
#     print(Person.__dict__)
#     p1 = Person("P1", "Aladár", 18, True)
#     print(p1.__dict__)
#     p2 = Person("P1", "Aladár", 18, True)
#
#     # egyenlőek-e?
#     print(p1 == p2)
#     print(p1.__eq__(p2))
#     print(Person.__eq__(p1, p2))


#tanáré

from functools import total_ordering


@total_ordering
class Person:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.male = male

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    def __str__(self) -> str:
        return "#{0}: {1} ({2}, {3})".format(self.id, self.name, self.age, self.male)

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id


@total_ordering #az összes hátralévő nem definiált operátort csináljon meg a python
class Car:
    plate: str
    type: str
    year: int
    automatic: bool

    def __init__(self, plate: str, type: str, year: int, automatic=True) -> None:
        self.plate = plate
        self.type = type
        self.year = year
        self.automatic = automatic

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Car) and self.plate == o.plate

    def __str__(self) -> str:
        return "{0} ({1}, {2}): {3}".format(self.plate, self.type, self.year, self.automatic)

    def __hash__(self) -> int:
        return self.plate.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Car):
            return NotImplemented

        return self.plate < o.plate


@total_ordering
class Airport:
    code: str
    name: str
    city: str
    state: str
    country: str

    def __init__(self, code: str, name: str, city: str, state: str, country: str) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Airport) and self.code == o.code

    def __str__(self) -> str:
        return "{code} ({name}): {city}, {state}, {country}".format(
            code=self.code, name=self.name, city=self.city,
            state=self.state, country=self.country)

    def __hash__(self) -> int:
        return self.code.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Airport):
            return NotImplemented

        return self.code < o.code

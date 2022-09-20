from data.basic.model import Person
from faker import Faker
import random


def generate_people(n: int, male_ratio: float = 0.5,
                    locale: str = "en_US", unique: bool =False) -> list[Person]:
    fake = Faker(locale)
    if unique:
        fake=fake.unique


    people = []
    for i in range(1, n + 1):
        male = random.random() < male_ratio  # igaz vagy hamis

        person = Person(
            f"P{str(i).zfill(6)}",  # id
            fake.name_male() if male else fake.name_female(),  # név
            random.randint(18, 100),  # kor
            male  # nem (boolean)
        )
        people.append(person)

    return people  # vagy ez vagy a következő 9 sor

    """return [    #listás comprihention(?)
        Person(
            f"P{str(i).zfill(6)}",      # id
            fake.name(),                # név
            random.randint(18, 100),    # kor
            random.randint(0, 1) == 1   # nem (boolean)
        )
        for i in range(1,n+1)
    ]"""


def main() -> None:
    people = generate_people(10, 0.7, locale="hu_HU")
    for person in people:
        print(person)


if __name__ == "__main__":
    main()

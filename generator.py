# from data.basic.model import Person
# from faker import Faker
# import random
#
#
# def generate_people(n: int, male_ratio: float = 0.5,
#                     locale: str = "en_US", unique: bool =False) -> list[Person]:
#     fake = Faker(locale)
#     if unique:
#         fake=fake.unique
#
#
#     people = []
#     for i in range(1, n + 1):
#         male = random.random() < male_ratio  # igaz vagy hamis
#
#         person = Person(
#             f"P{str(i).zfill(6)}",  # id
#             fake.name_male() if male else fake.name_female(),  # név
#             random.randint(18, 100),  # kor
#             male  # nem (boolean)
#         )
#         people.append(person)
#
#     return people  # vagy ez vagy a következő 9 sor
#
#     """return [    #listás comprihention(?)
#         Person(
#             f"P{str(i).zfill(6)}",      # id
#             fake.name(),                # név
#             random.randint(18, 100),    # kor
#             random.randint(0, 1) == 1   # nem (boolean)
#         )
#         for i in range(1,n+1)
#     ]"""
#
#
# def main() -> None:
#     people = generate_people(10, 0.7, locale="hu_HU")
#     for person in people:
#         print(person)
#
#
# if __name__ == "__main__":
#     main()


# tanáré
import random
from faker import Faker
from data.basic.model import Person, Car, Airport
from faker_vehicle import VehicleProvider
from faker_airtravel import AirTravelProvider


def generate_people(n: int, male_ratio: float = 0.5, locale: str = "en_US",
                    unique: bool = False, min_age: int = 0, max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    fake = Faker(locale)
    people = []
    for i in range(n):
        male = random.random() < male_ratio
        generator = fake if not unique else fake.unique
        people.append(Person(
            "P-" + (str(i).zfill(6)),
            generator.name_male() if male else generator.name_female(),
            random.randint(min_age, max_age),
            male))

    return people


def generate_cars(n: int,
                  automatic_ratio: float = 0.2,
                  locale: str = "hu_HU",
                  unique: bool = False,
                  min_year: int = 1950,
                  max_year: int = 2022) -> list[Car]:
    assert n >= 1
    assert 0 <= automatic_ratio <= 1
    assert min_year >= 1950
    assert min_year <= max_year <= 2022

    fake_plate = Faker(locale)
    fake_plate.add_provider(VehicleProvider)  # ha community providert használsz

    fake_type = Faker(locale)
    fake_type.add_provider(VehicleProvider)

    if unique:
        fake_plate = fake_plate.unique

    cars = []
    for i in range(n):
        car = Car(
            fake_plate.license_plate(),
            fake_type.vehicle_make(),
            random.randint(min_year, max_year),
            random.random() < automatic_ratio
        )

        cars.append(car)

    return cars


if __name__ == "__main__":
    cars = generate_cars(20, unique=True)  # 50 különböző rendszámú
    # for car in cars:
    #     print(car)


def generate_airports(n: int,
                      country: str = None,
                      unique: bool = False,
                      attempts: int = None) -> list[Airport]:
    fake = Faker()
    fake.add_provider(AirTravelProvider)

    airports = []

    for i in range(n if attempts is None else attempts):

        values = fake.airport_object()
        if values["icao"] == "":
            continue

        if country is not None and values["country"] != country:
            continue

        if len(airports) == n:
            break

        airport = Airport(
            values["icao"],
            values["airport"],
            values["city"],
            values["state"],
            values["country"]
        )


        if airport not in airports or not unique:
            airports.append(airport)
    return airports


if __name__ == "__main__":
    airports = generate_airports(5, attempts=10000, country="Germany", unique=True)
    for air in airports:
        print(air)

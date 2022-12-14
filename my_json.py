import json

from data.basic.model_dataclasses import Person
from data.basic.generator import generate_people
import os


def write_people(peolpe: list[Person], path: str, file_name: str = "people", extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [person.__dict__ for person in peolpe],
            file,
            indent=2 if pretty else None
        )


def read_people(path: str, file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            Person(person["id"], person["name"], person["age"], person["male"])
            for person in json.load(file)
        ]
        """
        return json.load(file,object_hook=lambda d: Person(**d))


if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, "C:/Users/hallgato/")

    for person in read_people("C:/Users/hallgato/"):
        print(person)

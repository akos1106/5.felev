import csv
import os
from data.basic.generator import generate_people

from data.basic.model_dataclasses import Person

def write_people(people: list[Person],
                 path: str,
                 delimiter: str =";",
                 file_name:str="people",
                 extension: str=".csv") ->None:

    with open(os.path.join(path,file_name+extension), "w", newline="") as file: #csv-t iró objektum
        writer = csv.DictWriter(file,delimiter=delimiter,
                                fieldnames=["id","name","age","male"])
        writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)

def read_people(path: str,file_name:str="people",
                extension:str=".csv",
                delimiter:str=";")->list[Person]:

    with open(os.path.join(path, file_name+extension)) as file:
        rows=csv.DictReader(file,delimiter=delimiter)
        people=[]
        for row in rows:
            people.append(Person(
                row["id"],
                row["name"],
                int(row["age"]),
                bool(row["male"])
            ))
        return people


if __name__=="__main__":
    people=generate_people(10)
    write_people(people,"C:/Users/hallgato/")

    people=read_people("C:/Users/hallgato/")
    for person in people:
        print(person)
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
        writer = csv.writer(file,delimiter=delimiter)
        for person in people:
            writer.writerow([
                person.id,
                person.name,
                person.age,
                person.male
            ])

def read_people(path: str,file_name:str="people",
                extension:str=".csv",
                delimiter:str=";")->list[Person]:

    with open(os.path.join(path, file_name+extension)) as file:
        rows=csv.reader(file,delimiter=delimiter)
        people=[]
        for row in rows:
            people.append(Person(
                row[0],
                row[1],
                int(row[2]),
                bool(row[3])
            ))
        return people

if __name__=="__main__":
    people=generate_people(10)
    #write_people(people,r"C:/Users/hallgato/",file_name="people",delimiter="\t",extension=".tsv")
    write_people(people, r"C:/Users/hallgato/") #alapertelmezett parameterekkel
    people=read_people(r"C:/Users/hallgato/",file_name="people",extension=".csv",delimiter=";")
    for person in people:
        print(person)
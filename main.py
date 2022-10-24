class student:
    def __init__(self, name="No name"):
        self.name = name
class Aspirant:
    def __init__(self, brand):
        self.brand = brand
        self.kids = []

    def add_kids(self, student):
        self.kids.append(student)

    def print_kids_names(self):
        if self.kids != []:
            print(f"Names, surname, age:{self.brand} kids:")
            for kids in self.kids:
                print(kids.name)
        else:
            print(f"There are no kids in {self.brand}!")


child = Aspirant("")

child.add_kids(student("Fojder Denys вік 12 "))
child.add_kids(student("Fojder Roma вік 14"))
child.add_kids(student("Fojder Oleg вік 22"))
child.add_kids(student("Fojder Maxim вік 13"))
child.add_kids(student("готуються до захисту дипломної роботи!"))

child.print_kids_names()

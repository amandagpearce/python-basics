from abc import ABC, abstractmethod


class Institute(ABC):
    def __init__(self):
        print(type(self).__name__, " details :")

    def courseOffered(self):
        print("Courses offered: C, Python, .NET")

    @abstractmethod
    def address(self): pass


class TechnoAcademy(Institute):
    def courseOffered(self):
        print("Courses offered: Javascript")

    def address(self):
        print("Address @ Brazil")


class OnlineAcademy(Institute):
    def address(self):
        print("Address @ Brazil")


ta = TechnoAcademy()
ta.courseOffered()
ta.address()

olt = TechnoAcademy()
olt.courseOffered()
olt.address()

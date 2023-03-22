class Name:
    def __init__(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName


class Student:
    def __init__(self, sId, sName, course):
        self.sId = sId
        self.sName = sName
        self.course = course


student1 = Student(101, Name("Clara", "Banana", "Prato"), "OOP With Python")
student2 = Student(102, Name("Marcelo", "Cigarro", "Paiva"), "OOP With Node")

students = [student1, student2]

for student in students:
    print("Id: {}\n Student Name: {} {} {}\n Course: {}\n".format(
        student.sId,
        student.sName.firstName,
        student.sName.middleName,
        student.sName.lastName,
        student.course))

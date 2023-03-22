class Grandparents:
    def PropertyLand(seld):
        print("Property land for farming given by grandparents")


class Parents(Grandparents):
    def PropertyHome(self):
        print("Property home constructed by Parents")


class Child(Parents):
    def PropertyVehicle(self):
        print("Property car purchased by child")


c1 = Child()
c1.PropertyLand()
c1.PropertyHome()
c1.PropertyVehicle()

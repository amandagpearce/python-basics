class Father:
    def FatherProperty(self):
        print('Fathers property')


class Mother:
    def MotherProperty(self):
        print('Mothers property')


class Child(Father, Mother):
    def Property(self):
        print("Child inherits:")
        super().FatherProperty()
        super().MotherProperty()


c1 = Child()
c1.Property()

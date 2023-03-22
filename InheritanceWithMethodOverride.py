class Employee:

    def __init__(self, empno, ename, salary, deptno):
        self.Empno = empno
        self.Ename = ename
        self.Salary = salary
        self.Deptno = deptno

    def showEmployee(self):
        print(" Employee #: {}\n Emp Name: {}\n Salary: {}\n Department: {}".
              format(self.Empno, self.Ename,
                     self.Salary, self.Deptno))


class Salesman(Employee):
    def __init__(self, empno, ename, salary, deptno, commission):
        self.Commisssion = commission
        super().__init__(empno, ename, salary, deptno)

    def showEmployee(self):
        super().showEmployee()
        print(" Commission: ", self.Commisssion)


emp = Salesman(101, 'Name Here', 5400, 10, 500)
emp.showEmployee()

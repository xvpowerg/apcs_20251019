class Employee:
    def __init__(self,name,salary=25000):
        print("__init__:",self)
        self.name = name
        self.salary = salary

emp1 = Employee("Ken",50000)
emp2 = Employee("Iris",28000)
emp3 = Employee("Joy")
emp4 = Employee(salary=35000,name= "Lucy")
print(emp1.name,emp1.salary)
print(emp2.name,emp2.salary)
print(emp3.name,emp3.salary)
print(emp4.name,emp4.salary)

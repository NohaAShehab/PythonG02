class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, email="iti@iti.com", salary=1000):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        self.id = Employee.count_emp

    def speak(self):
        print(f"I am {self.name}, You can reach me at {self.email}")

    @classmethod  # decorator
    def mymethod(cls):
        print(cls.makefaults)
        return cls("Mona", "mona@gmail.com", 4555)

    @classmethod
    def addEmployee(cls, emp1, emp2):
        cls.newvar = 10  # new class variable
        return cls(f'{emp1.name} {emp2.name}', "mergedmail@gmail.com", emp1.salary + emp2.salary)

    # static method can be called using Classname or object
    # create utility functions
    @staticmethod
    def netsal(sal):  # cannot change the structure of the class
        return sal * .89





print("==========================obj 1========================")
e1 = Employee("Ali", "a@gmail.com", 1000)
# e1_net_sal=netsal(e1.salary)
# print(e1_net_sal)
e1_net_sal=Employee.netsal(e1.salary)
print(e1_net_sal)
print("==========================obj 2=========================")
e2 = Employee("Ahmed", "Ahmed@gmail.com")  # name ,mail
e2_net_sal=e2.netsal(e2.salary)
print(e2_net_sal)

print("=======================obj 3============================")
# e = Employee("Esraa")
# e_net_sal=netsal(e.salary)
# print(e_net_sal)

print(Employee.netsal(5000))
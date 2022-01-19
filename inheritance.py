# single inhirtance
class Person:
    def __init__(self, name, bdate):
        print("==== parent constructor called ====")
        self.name = name
        self.bdate = bdate
        print("==== parent constructor finished ====")

    # instance method
    def speak(self):
        print("------ Parent Speek called------")
        print(f"I am {self.name}")
        print("------ Parent Speek Ended------")

        # overloading , overriding
        'overloading ---> the same function with same name but with different param calls' \
        'in the same class'


class Employee(Person):
    def __init__(self, name, bdate, salary, email):
        print("===========Employee constructor called=======")
        super().__init__(name=name, bdate=bdate)
        self.salary = salary
        self.email = email

    # overriding
    def speak(self, id=100):
        super().speak()
        print("bla bla bla ")


e = Employee("ali", "ssdfs", 20000, "dasssd@fdgf.com")
# print(e.name)
e.speak()
e.speak(999)
print("test")

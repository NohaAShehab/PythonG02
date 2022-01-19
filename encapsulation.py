class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, email="iti@iti.com", salary=1000):
        # instance variables of the class have public modifire
        # ### act like public variable
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        # # variable name starts with _ ----> proptected variable
        # can be accessed in the class and child classed
        self._id = Employee.count_emp
        self._protected= "iti"
        # private member ---> can be accessed only inside the class
        self.__commission = 10

    def speak(self):
        print(f"I am {self.name}, You can reach me at {self.email}, {self._id}, {self.__commission}")

    def __repr__(self):
        return f"Employee({self.name},{self.email},{self.salary})"


class B(Employee):
    def __init__(self, name):
        super().__init__(name)

    def test(self):
        # proteced member in the chlid class
        print(self._protected, self.__commission)


# encapuslation
e = Employee("noha", "nshehab@iti.gov.eg", 2000)
print(e)
e.name = "Noha Shehab"
e.speak()
# e.__newval = "abc"  # consider it as proptected
# print(e.__newval)

# print(e.__commission) # AttributeError: 'Employee' object has no attribute '__commission'

# print(e)
# print(e.salary)
# loosly typed , dynmaically lang
# e.dept = "Open source"  #
# print(e.dept)
# e.dept ="Python"
# print(e.dept)
print("---------------------------")
# e3 = Employee("Ahmed", "Ahmed@iti.gov.eg", 2000)
# print("---------------------------")

b = B("iiiii")
# b.test()
print("---------------------")
# print(b._protected)
# print(b.__commission)
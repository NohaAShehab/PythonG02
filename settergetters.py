class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, email="iti@iti.com", salary=1000):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        self.comm = 10
        self._id = Employee.count_emp
        self._protected = "iti"
        self.__commission = 10

    def speak(self):
        print(f"I am {self.name}, You can reach me at {self.email}, {self._id}, {self.__commission}")

    def __repr__(self):
        return f"Employee({self.name},{self.email},{self.salary})"

    # setter and getter for variable ---> apply certain conditions
    def setCommission(self, commission):
        try:
            self.__commission = abs(commission)
        except:
            # exception handling
            self.__commission = 0

    def getCommission(self):
        return self.__commission*.89


# encapuslation
e = Employee("noha", "nshehab@iti.gov.eg", 2000)

print(e.getCommission())
# e.__commission= 100
e.setCommission("mdd")

print("--------------------------")

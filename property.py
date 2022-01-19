class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, commission, email="iti@iti.com", salary=1000,data ="uuuu"):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        self.comm = 10
        self._id = Employee.count_emp
        self._protected = "iti"
        self.commission = commission  # access private property --->
        # self.commission = commission
        # property --> instance variable
        ###
        self.__data = data  # private

    def speak(self):
        print(f"I am {self.name}, You can reach me at {self.email}, {self._id}")

    def __repr__(self):
        return f"Employee({self.name},{self.email},{self.salary})"

    @property  # print property value
    def commission(self):
        print("Property getter called ")
        return self.__commission

    @commission.setter
    def commission(self, commissionval):
        try:
            self.__commission = abs(commissionval)
        except:
            self.__commission = 0

    #property only --> private
    @property
    def data(self):
        return self.__data

    # def getdata(self):
    #     return self.__data
    # # setter and getter for variable ---> apply certain conditions, operation on the property __commission
    # def setCommission(self, commission):
    #     try:
    #         self.__commission = abs(commission)
    #     except:
    #         # exception handling
    #         self.__commission = 0
    #
    # def getCommission(self):
    #     return self.__commission*.89


# encapuslation
e = Employee("noha", -10, "nshehab@iti.gov.eg", 2000)
# print(e.__commission) # access private member
# print(e.commission) # -10
e.commission = -90
print("--------------------------")
print(e.data)

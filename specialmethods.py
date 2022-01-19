class Employee:
    makefaults = True
    count_emp = 0

    def __init__(self, name, email="iti@iti.com", salary=1000):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count_emp += 1
        self.id = Employee.count_emp
    '--------------------------override------------------------------------'
    def __str__(self):
        # return string
        # return f"name = {self.name}, email={self.email}, salary={self.salary}"
        return self.name

    def __repr__(self):
        # in debugging
        return f"Employee({self.name},{self.email},{self.salary})"
    '----------------------------------------------------------------------'
    def __len__(self):
        # retrun int
        return 4

    def __call__(self):
        print(f"calling Employee({self.name},{self.email},{self.salary}) object")




###
e = Employee("Ali", "ali@iti.com", 3000)
print(e)
print(e.__repr__()) #debuging your code

print(len(e))
print(e.__len__())

e()  # call object e
# l = [44,66,77]
# print(len(l))
# print(l.__len__())


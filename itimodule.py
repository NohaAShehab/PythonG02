# print("Inside the iti module")
name = "Israa"


def greeting(fname, lname):
    print(f"Nice to meet you {fname} {lname}")


def introduceself():
    name = input("Plz enter your name ")
    work = input("Where are you working")
    print(f"you said that your name is {name} and works at {work}")


def validateInput(typee):
    while True:
        name = input(f"Plz enter {typee} ")  #a--z
        if name.isalpha() and not name.isspace():
            return name


# n = validateInput("first name")
#
# n = validateInput("last name")
# print(n)
# greeting("Mohamed", "Ahmed")
# introduceself()
#
#
# introduceself()
#
#
# introduceself()
#
#
# introduceself()


def validateFullname():
    while True:
        fname = input(f"Plz enter firstname ")  #a--z
        if fname.isalpha() and not fname.isspace():
            break

    while True:
        lname = input(f"Plz enter lname ")  # a--z
        if lname.isalpha() and not lname.isspace():
            break

    return fname, lname


# m = validateFullname()
# print(type(m))

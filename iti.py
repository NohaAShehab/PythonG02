

def greeting(fname, lname):
    print(f"Hello   {fname} {lname}")


def introduceself():
    name = input("Plz enter your name ")
    work = input("Where are you working")
    print(f"you said that your name is {name} and works at {work}")
    return name,work
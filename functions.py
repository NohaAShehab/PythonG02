### loosly dynamically typed lang.
def goodmorning(fname, lname):
    print(f"Good morning, My name is {fname} {lname}")
    # retrun with None
    return f"{fname} {lname}"
#
#
# x = goodmorning("Noha", "Shehab")
# print(x)
# print(goodmorning("Ahmed", "Ali"))


# python support default arguments
# def summ(x=10, y=10):
#     print(f"x = {x}, y = {y}")
#     return x + y
#
#
# z = summ(5, 6)
# print(z)
# print("==================================")
# m = summ()
# print(m)
# print("==================================")
# n = summ(y=3)
# print(n)
####################### function argument , parameter
def summ(z, x=10, y=10):
    print(f"x = {x}, y = {y}, z={z}")
    return x + y * z


#
#
# # s = summ(2)
# # print(s)
#
# # s = summ(3, x=2)
# # print(s)
# # z,x,y
# m = summ(5, 6, 7)
# print(m)
# ########3 change paramter order
#
# n = summ(y=5,z=3,x=8)
# print(n)

##################3 number of arguments

def calsum(*args):  # * allow you to send zero or more paramters
    # unknown number of arguments
    print(type(args))  # in form of tuple
    print(f"function called and the arguments passed to it are {args}")
    summ_ = 0
    for i in args:
        summ_ +=i
    return summ_
#
#
# calsum()
# m =calsum(2, 4, 6, 7, 9)
# print(m)
# # n= calsum("Good"," Morning", "Team")
# # print(n)

############################33 Kwargs

def getInfo(**abbass):  #kwargs  #unkwoun number or argyments, keywords
    print(abbass)
    print(type(abbass))
    for key in abbass:
        print(f"{key} = {abbass[key]}")

    print("=======================================")
    pass


getInfo(year=2022)
getInfo(fname="Noha", lname="Shehab", track="Python")
getInfo(fullname="Mariam Ahmed", country="Egypt", age=25, email="m@gmail.com")
getInfo(salary=1000)

m = "My name is {hhhh} I graduated from {fii} and I works at {work}"
print(m.format(hhhh="Noha", fii="Engineering", work="ITI"))

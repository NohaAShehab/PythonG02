# scoping ---> lexical scope

#### Global scope of the module ,script
iti = "Information Technology Institue"
print(iti)  # read the value


# iti = "ITI"  # modification on the value
# print(iti)

def greet1():
    # you can read the values of the global scope variable
    print(iti)


# def greeting():
#     # local scope ---> once you create function, new local scope created
#     # create local scope for the function
#     print("=========I am in the local scope of the greeting function========")
#     # create new varable inside a function ---> add it to the local scope of the function
#     iti = "Python track"  #
#     print(iti)
#     print("============ End of the local scope of the greeting function =======")
#
#
# greeting()
# print(iti)




# def greeting():
#     # local scope ---> once you create function, new local scope created
#     # create local scope for the function
#     print("=========I am in the local scope of the greeting function========")
#     # create new varable inside a function ---> add it to the local scope of the function
#     global iti
#     iti = "Python track"  #
#     print(iti)
#     print("============ End of the local scope of the greeting function =======")
#
#
# greeting()
# print(iti)

countt = 0

def myfunction():
    global countt
    countt +=1
    print("My function called")



myfunction()
myfunction()
myfunction()
myfunction()
myfunction()
print(countt)
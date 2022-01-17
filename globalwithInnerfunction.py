name = "python"


#
# def outerfun():
#     print(name)
#
#
# outerfun()


# def outerfun():
#     name = "test"  # local variable test --->
#     print(name)


# outerfun()


# def outerfun():
#     global name
#     name = "test"  # modify the global variable
#     print(name)


# def myfun():
#     print('================inside my function===============')
#
#     def innerfun():
#         print(name)
#
#     innerfun()
#
#
# myfun()
############################################

# def myfun():
#     print('================inside my function===============')
#
#     def innerfun():
#         name = "abc"  # define local variable inside the innerfun scope
#         print(name)
#
#     innerfun()
#
#
# myfun()

###################################3
print(name)
def myfun():
    print('================inside my function===============')

    def innerfun():
        global name
        name = "abc"  # define local variable inside the innerfun scope
        print(name)

    innerfun()


myfun()
print(name)
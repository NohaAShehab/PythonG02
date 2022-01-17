

# def outerfunc():
#     x = 10
#     print(x)
#
#
# outerfunc()

##################
# def outerfunc():
#     x = 10
#
#     def innerfunction():
#         print(f"from the inner function {x}")
#
#     innerfunction()
#     print(f"from the outer function {x}")
#
#
#
# outerfunc()



# def outerfunc():
#     x = 10
#
#     def innerfunction():
#         x = "python"
#         print(f"from the inner function {x}")
#
#     innerfunction()
#     print(f"from the outer function {x}")
#
#
# outerfunc()




# def outerfunc():
#     x = 10
#
#     def innerfunction():
#         nonlocal x
#         x = "python"
#         print(f"from the inner function {x}")
#
#     innerfunction()
#     print(f"from the outer function {x}")
#
#
# outerfunc()

m = 100

def outerfunc():
    x = 10
    def innerfunction():
        x = "Mahinour"
        def test():
            nonlocal x
            print(f"============={x}")
            x = "python updated"
            print(f"from the test function {x}")
            global m
            m = 2022
        test()
        print(f" changing mahinoor value to be {x}")

    innerfunction()
    print(f"from the outer function {x}")


outerfunc()

print(m)
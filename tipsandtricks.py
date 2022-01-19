# def num_mul_four(x):
#     return x*4
#
# print(num_mul_four(10))
# print("rrrrrr")
# lambda expressions

myfun = lambda x, y: x * 4 + y
print(myfun)  # can be called
z = myfun(100, 30)
print(z)
l = [4, 67, 8, 9, 9, "fff_"]


# myl= []
# for item in l:
#     # print(item*4)
#     myl.append(item*4)
#
# print(myl)
# map apply logic on all items
# l= [10,40,60,50]
# myl=map(lambda x:x*4, {1,3,5,6})
# print(myl)
# print(list(myl))

# filter certain values
# l=[x for x in range(0,11)]
# print(l)
#
# myl= filter(lambda x:x%2==0, l)
# print(myl)  # filter object
# print(list(myl))
#
# ########################## iterators
#
# # l1= ["python", "Django", "Flask"]
# # # for item in l1:
# # #     print(item)
# #
# # # for i in range(len(l1)):
# # #     print(l1[i])
# #
# # # iter function
# # myiter = iter(l1)
# # print(type(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # try:
# #     next(myiter)
# # except:
# #     print("End of iterator ")
# # print(next(myiter))
#
#
# ###################### generator
# # inside a function
#
# def gen():
#     for i in range(2000000000000000000000000000000):
#         yield i
#
#
# # l=(x for in range(100000000000000000000000))
# # print(nongen())
# # print(nongen())
# s = gen()
# print(s)  # can be iterated
# # print(next(s))
# # print(next(s))
# # print(next(s))
#
# while True:
#     try:
#         # print(type(next(s)))
#         x = next(s)  # 100
#         if next(s) == 101:
#             print("--------------------------")
#             break
#         print(x)
#     except:
#         break
#

class Test:
    class B:
        def __init__(self):
            print("class b called")

    def __init__(self):
        self.b = Test.B()




test = Test()
print("-----------------")
a=test.B()
print("---------------------")
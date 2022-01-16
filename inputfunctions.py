
# input --->
x = input("plz enter raduis ")
# open new prompt ---> accept value from user
print(x, type(x))

if x.isdigit():
    x = int(x)


## check if the value inside string is float or not ...

########## range
# loop ---> 5 item
# i = 0
# while i <5:
#     i+=1
#     print("hiii")


# for item in [1, 2, 3, 4, 5]:
#     print("hii")

# generate something can be iterated ---> 0, 4
# x = range(100, 10, -2)
# print(type(x))  # range object ---> can be iterated from start to end-1
# for abbass in x:
# #     print(abbass)
#
#
# for i in range(10):
#     if i == 4:
#         break
#     print(i)
# else:
#     # lines are executed after the loop completed --->
#     print("loop ended")
#
# '''
# if(x==4){
# }
# '''
#
# # if x==4:
# #     pass


for i in range(0,10):
    if i == 4:
        continue
    print(i)

print("xxx")
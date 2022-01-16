myl = ["Python", "Django", "Postgres"]
l = [1, 2, "test", "Ahmed", True, 55.6, myl]
print(l)
# access list elements =--> index
print(l[4])
# get list len
print(len(l))
# list are mutable data types , change items of list in the run time
l[3]="iti"
print(l)
### add new item in the list (add the end of the list)
l.append("new item added")
print(l)
# insert item at certain position
l.insert(4, "inserted values")
print(l)
### pop value --> remove value
l.pop() # remove last item
print(l)
###
l.pop(2) ### 2 is the index
print(l)
### remove =--> item
l.remove(55.6) ### accept item
print(l)
###
print(l.count(1))
########## list extend
myl2 = ["js", "Linux", "ShellScript"]
l.extend(myl2)  # affect the same variable l
print(l)
# l.append(myl2)
# print(l)
####### concatination
# l3 = l + myl2   # create new list with the all items
# print(l3)
# ########### min , max
# ll =[2,4,6.888,7777.6]  # valid if all items in the list are numbers float or int
# print(max(ll), min(ll))

########## sort , reverse
# myl2 = ["js", "Linux","aa","bbb","ShellScript"]
# print(myl2)
# myl2.sort() #sort asencding
# # # myl2.sort(reverse=True) # sort decending
# print(myl2)
# # myl2.reverse() # reverse items as they are
# # print(myl2)


######## membership
myl2 = ["js", "Linux","aa","bbb","ShellScript"]
print("ShellScrip" in myl2)

### looping over the list
for item in myl2:
    print(f"item = {item}")

ll2 = None  # falsy values
import sys
print(sys.getsizeof(ll2))
if ll2:
    print("List found")
else:
    print("not found")



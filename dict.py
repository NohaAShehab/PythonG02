# info = {"name": "Noha", "email": "nshehab@iti.gov.eg",
#         "track": "python",
#         "myl": [3, 4, 6, 666]}
# print(type(info))
# print(info["name"])
# #mutable ===>
# info["name"] ="Noha Shehab"
# print(info)
# info["work"] = "ITI"
# print(info)
#
# # get len of the dic
# print(len(info))
#
# data =info.pop("work")  # accept the key
# print(data)
# print(info)
#
# ### get keys of dictionary
# # for abbass in info:
# #         print(abbass)   # abbass ---> keys
#
#
# # for abbass in info:  #get keys
# #         print(f"key = {abbass} and value = {info[abbass]}")   # abbass ---> keys
# #
# # info_keys = info.keys()  # retrun with the keys of the dictionary
# # print(type(info_keys), info_keys)
# # # print(info_keys[0])
# # for m in info_keys:
# #         print(m)
# # #
# # # # you can cast the info_keys to list or tuple
# # info_keys=tuple(info_keys)
# # print(info_keys)
#
# # #######################3 get values of dictionary
# # info_values = info.values()
# # print(type(info_values), info_values)
# # for val in info_values:
# #         print(val)
# #
# # info_values = list(info_values)
# # print(info_values)
# ################## casting dictionary into list
# # list_dic = list(info)
# # print(list_dic)
# #
# # list_dic = list(info.values())
# # print(list_dic)
# # tup_dic = tuple(info.values())
# # print(tup_dic)
#
# ################
# myinfo = info.items()
# print(myinfo)
# myinfo = list(myinfo)
# print(myinfo)
# #
# # for k,v in info.items():  # ("name", "nohasheba")
# #         print(f"{k} = {v}")
# #


info = {"name": "Noha", "email": "nshehab@iti.gov.eg",
        "track": "python",
        "myl": [3, 4, 6, 666]}

education = {"faculty": "Engineering", "Masters": "Engineering",
             "PHD":"Student", "track":"open source"}
print(info)
info.update(education)
print(info)

info.clear()
print(info)

del info


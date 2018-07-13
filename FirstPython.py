import re
# name="sagar"
# print(name)
# test=input("enter the name yo want :")
# print(test)
# saglist=[25,255,36,89]
# print(saglist)
# print(saglist[1])
# for i in range(saglist.__len__()):
#     if(saglist[i]==255):
#         print("duplicate")
#     else:
#         print(saglist[i])
def add(a,b):
     return a+b
line='pet:cat i love you'
sa='i love pet:dog'
resu=re.match(r'pet:\w\w\w',line)
print(resu.group(0))
#checks the entire line
res=re.search(r'pet:\w\w\w',sa)
print(res.group(0))

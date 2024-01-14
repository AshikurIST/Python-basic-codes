'''set do not maintain order
and do not repeat any item
and set are like tuple
 that's means we can't change the value'''

s={90,33,"ashikur",1,3,6,3,"ashikur",6,7,85,3}
print(s)

ashik=set()
print(type(ashik))
for value in s:
    print(value)

# Operation of set

s1={1,3,4,5}
s2={4,5,6,7,9}
set_union=s1.union(s2)
print("union result is:",set_union)
set_inter=s1.intersection(s2)
print("intersection result is:",set_inter)
s1.update(s2)
print("updated s1 is:\n",s1)

print("\n---dictionary----\n")

dic={
    "ashikur": "human",
    "roll": 21071,
    "computer": "Object"
}
print(dic["computer"])
print(dic["roll"])
print(dic.keys())
for key in dic.keys():
    print(key)
print(dic.values())
for value in dic.values():
    print(value)

print("\n --dictionary method---\n")

students={1:23,2:33,3:58,5:94}
students2={6:94,7:99,8:92,9:94}
students.update(students2)
print(students)

students2.clear()
print(students2)

students.pop(1)
print(students)

students.popitem()
print(students)



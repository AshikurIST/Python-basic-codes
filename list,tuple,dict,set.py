print("____List____\n")
letters=["a","b","c","d",25]
matrix=[[1,3],[4,5]]
message=["i don't love code "] * 3
print( message)
print(matrix)
print(letters)
print(letters[3])
print(letters[-3])    # negative index
print(letters[len(letters)-3])         # positive index
print(letters[5-3])     # positive index

print("\n----search in list------\n")
if "Z" in letters:
    print("Yes")
else:
    print("No")

if 25 in letters:
    print("Yes")
else:
    print("No")

print("\n ----indexin ----\n")

marks=[1,2,3,4,5,6,"ashik","A"]
print(len(marks))
print(marks)
print(marks[:])
print(marks[2:-1])
print(marks[2:7])
print(marks[:7:2])

print("\n---list comprehension and unpacking ----\n")
lst=[i for i in range(8)]
print(lst)
first=lst[0]
second=lst[1]
third=lst[2]
print(first,second,third)
st,nd, *other=lst
print(nd)
print(st)
print(other)

print("\n --adding and removing---\n")
newlist=[1,3,4,5,6,7]
newlist.append(10)
newlist.insert(2,"ashikur")
print(newlist)

# removing

ist=[2,5,6,1,2,3,4,5,6,6,7,8,9]
print(ist)
ist.pop()
print(ist)
ist.pop(2)
print(ist)
ist.remove(6)
print(ist)
del ist[0:3]
print(ist)
ist.clear()
print(ist)

# list methods
ist1=[2,5,6,1,2,3,4,5,6,6,7,8,9]
ist1.sort()
print(ist1)
ist1.sort(reverse=True)
print(ist1)
(ist1.reverse())
print(ist1)
print(ist1.index(4))
print(ist1.count(6))
ist1.insert(3,"ashikur")
print(ist1)
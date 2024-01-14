# for loop
x="Ashikur"

for i in x :
    print(i)

    if(i=="h"):
        print("letter H")

colors=["red","blue","green","yellow"]
for color in colors:
   print(color)
   for c in color:
       print(c)

''' 1st parameter is start
    2nd parameter is stop
    3rd parameter is steps'''

for k in range(5):
    print(k+4)

for k in range(2,9):  # 9 is n and,,9 equal to n-1
    print(k)

for i in range(1,16,3):  # 3 is steps
    print(i)



print("\n   _______while loop-------\n ")
i=1
while(i<5):
    print(i)
    i=i+1

print("\n")
count=5
while(count>0):
    print(count)
    count=count-1



print("\n -----continue and break----- \n ")

for a in range(12):
    if(a==10):
        break
    print("5 X", a, "=",5*a)
print("get out from the loop")

for a in range(15):
    if(a==10):
        print("skip the iteration")
        continue
    print("5 X", a, "=", 5 * a)
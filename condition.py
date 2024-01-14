age=int(input("Enter your age:"))
print("age is:",age)
print(age==18)
print(age!=18)
print(age<18)
print(age>18)
print(age<=18)
print(age>=18)

if(age>=18):
    print("You can drive")
else:
    print("You can't drive")

num=int(input("Enter any number:"))

if(num<0):
    if(num<=-1 and num>-10):
        print("Number is between -1 to -10")
    elif(num<=-11 and num>=-20):
        print("Number is between -11 to -20")
    else:
        print("Number is less than -21")

elif(num>0):
    if(num>=1 and num<=10):
        print("Number is between 1 to 10")
    elif(num>=11 and num<=20):
        print("Number is between 11 to 20")
    else:
        print("Number is greater than 21")

else :
    print("Number is zero")


# Match case statement
print("\n------ Match case statement------- \n")

num=int(input("Enter any number:"))
match num:
    case 0:
        print("number is 0")
    case 1:
        print("number is 1")

    case 3:
        print("number is 3")

    case 2:
        print("number is 2")

    case 5:
        print("number is 5")

    case _:
        print(num)
#num1,num2=map(int,input("Enter two integer number separated by space:").split())
#print("Number 1 is:",num1,"\nNumber 2 is:",num2)


def greet():
    print("assalamuaikur!")
    print("welcome bangladesh")

greet()

def greet(first_name,sec_name):
    print(f"hi {first_name} {sec_name}")
    print("Welcome aboard")

greet("Ashikur","Rahman")
greet("Ayman","Abdullah")

def sum(a,b):
    return a+b
print(sum(a=3,b=4))

def sum2(a,b=4):
    return a+b
print(sum2(4))

def sum2(a,b=8):
    print(a+b)

sum2(1,2)

print("\n---number of argument----\n")

'''In the given code, the asterisk * before the parameter 
numbers is used to indicate that the function can accept 
an arbitrary number of positional arguments.'''

def multiply(*numbers):
    total = 1
    for number in numbers:
        print(number)

        total *= number
    print("Total is:",total)

multiply(1,2,3,4,5,3)

def save_user(**user):
    print(user)
    print(user["age"])

save_user(roll=71,name="Ashikur Rahman",age=22,semestar="3rd")

print("\n___fizbuzz problem_____\n")

num=int(input("Enter any number:"))
def fiz_buzz(num):
    #return num
    if (num % 3 == 0 and num % 5 == 0):
        print("Fiz_Buz")

    elif(num % 5 == 0):
        print("Buz")

    elif (num % 3 == 0):
        print("Fiz")
    else:
        print(num)

fiz_buzz(num)

print("\n===recursion function===\n")
def facctorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * facctorial(n-1)

print(facctorial(4))
print(facctorial(5))

print("===fibonacci sequence---")
def fibo (n1,n2):
    if (n1==0 and n2==1)
        return 1
    else:
        n1=n2
        n2=n1
        fib=n1+n2
        print(fib)
fibo(2,3)

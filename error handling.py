mul=input("enter any int number:")
print(f"multiplication table is of {mul} is:")


try:
    for i in range(1,11):
     print(f"{int(mul)} X {i} = {int(mul)*i}")

# except Exception as a:
except:
    print("Invalid input")

print("\n rest of the code")
print("end of the program")


try:
    num= int (input("enter an integer:"))
    a=[2,6]
    print(a[num])
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("index error")

# finally will always executed

finally:
    print("\ni will always executed")

def func1():
    try:
        l=[1,2,6,4]
        i=int(input("enter an index:"))
        print(l[i])
        return 323
    except:
        print("wrong index,an error occurred")
        return 404


    finally:
        print("always executed")

x=func1()
print(x)
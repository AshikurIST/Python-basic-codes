x=5
print(x)
name="ashikur rahman"

def hello():
    global name
    name="sujon"
    x=9
    print(f"the local variable x is {x}")
    print("hello ashikur")

hello()

print(f"the global variable x is:{x}")
print(name)
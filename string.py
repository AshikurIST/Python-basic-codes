name="My name is Ashikur rahman"
print(name.lower())
print((name.upper().isupper()))
print(name.isupper())
print(len(name))
print(name[0])
print(name.index("r"))
print(name.replace("rahman","Rahman Sujon"))

print("\n----f string -----\n")
name="My name is {} rahman i'm from {}"
nam="Ashikur"
country="Bangladesh"
print(name.format(nam,country))
country="germany"
print(f"my name is {nam} and i wanna go to {country} with scholarship")


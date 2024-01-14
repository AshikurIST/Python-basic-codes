marks=[34,64,94,75,88,55,55,65,84]

index=0

for mark in marks:
    print(mark)

    if (index==2):
        print("Well done!\n")
    index +=1

marks = [34, 64, 94, 75, 88, 55, 55, 65, 84]
for index,mark in enumerate(marks):
    print(mark)
    if (index==4):
        print("Nice!")

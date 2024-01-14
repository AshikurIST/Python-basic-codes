import os

#print(dir(os))

print(os.getcwd())  # current working directory
#os.chdir("E:\python Code")      #change directory
#print(os.getcwd())

#print(os.listdir())     # all files in the folder
print(os.listdir("F://"))

#os.mkdir("new")    # make new folder
#os.makedirs("folder1/folder2")  #make folder into a folder
#os.rename("list,tuple,dic,set.py","list,tuple,dict,set.py")    # os.rename(source,destination)
print(os.path.exists("E:\python Code\code_with_harry"))

#for i in range(1,100):
    #os.makedirs(f"new directory/name{i}")   # make new folder or directory
    #os.rename(f"new directory/day{i}",f"new directory/day {i}")


#os.mkdir("day 15/file.p")
folders= os.listdir("new directory")
#print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"new directory/{folder}"))



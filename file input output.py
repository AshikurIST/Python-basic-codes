#file=open('Pre Document.txt','r')   # read mode is default

#text=file.read()
#print(text)
#file.close()

'''
# w-write mode open file creat a file if doesn't exist and delete previous data and
# a-append mode do not delete data only add data creat file if doesn't exist
# x-creat mode creat a file,if file exist give error
# t-default value,text mode
# b-binary mode,,images
'''
# f=open('Pre Document.txt','a')
# f.write("\n hello world")
# f.close()

with open('Pre Document.txt','r') as f:
    for line in f:
       print(line,end=" ")


with open('Pre Document.txt','r') as file:
    content=file.read(150)
    print("\n",content)

    content = file.read(100)
    print("\n", content)
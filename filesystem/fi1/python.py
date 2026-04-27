# file handling ek important part hai files ko handle karne ke 
# file system me ham log files ko read write create delete kara sakte hai

#pythong has the open function 

# r operation is use for read
# a operation use for append
# w operation use for write
# x operatror is user for create

# t is use for text
# b is use for binary format


# use to read the file text 
# f = open("file.txt", "rt")
# print(f.read())
# f.close()

# f=open("file.txt","rt")
# print(f.read())

f=open("file.txt","w")
f.write("My name is mohit sankhyan")

f=open("file.txt","rt")
print(f.read())
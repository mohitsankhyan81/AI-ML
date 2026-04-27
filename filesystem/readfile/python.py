#read fucntion is use for 
#read is use for the data data is entered in the fuction

# f=open("file.txt","rt")
# print(f.read())

# f=open("file.txt","rt")
# print(f.readline())

# with is also use for the opening a file

# with open("file.txt") as f:
#     print(f.read())

#read only the part of file
# with open("file.txt") as f:
#     print(f.read(5))

#using loop read file

with open("file.txt") as f:
    for x in f:
        print(x)
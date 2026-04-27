# to delete the file we use the os model 

# import os
# os.remove("file.txt")


#check file is exists or not
import os
if(os.path.exists("file.txt")):
    os.remove("file.txt")
else:
    print("this file does not found")


# for remove the folder we use 
# rmdir
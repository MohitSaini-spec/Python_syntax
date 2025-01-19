f=open("text1.txt","w")
f.write("Written by python in this file ")
f.close
f=open("text1.txt","r") #"x"  create a new empty file
                        #"a" add contant to file
data=f.read() #.read(5) read first 5 characters
                #f.readline() to read one line
print(data)
f.close

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")     #remove file
# else:
#   print("The file does not exist")

# os.rmdir("myfolder")            #remove folder
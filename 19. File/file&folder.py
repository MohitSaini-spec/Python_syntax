# Reading a file line by line
print('{:-^50s}'.format("Reading a file"))
with open('myfile.txt', 'r') as fp:
 for line in fp:
  print("With loop: ",line)

with open("myfile.txt", "r") as fp:
  lines = fp.readlines()
  for i in range(len(lines)):
    print("Line " + str(i) + ": " , line)
 

with open('myfile.txt', 'r') as fp:
 while True:
  cur_line = fp.readline()
  if cur_line == '':
 # We have reached the end of the file
    break
  print("Readline with loop :",cur_line)


# Getting full content
#.read ( CLOSE AUTOMATICALLY )
print('{:-^50s}'.format("Getting full content"))
with open('myfile.txt') as in_file:
 content = in_file.read()
print(".read() :\n"+content)


# Without with ( CLOSE MANUALLY )
in_file = open('myfile.txt', 'r')
content = in_file.read()
print("\n.read():\n"+content)
in_file.close()

# WRITTING FILE
print("\nWritting a file")

# With encoding type
with open('myfile.txt', 'w+', encoding='utf-8') as f:
 f.write("Written by .write method\n")
 s = "I'm Not Dead Yet!"
 s1 = "\nGood to go"
 print(s,s1, file = f)

# Checking whether a file or path exist
#import os
#os.path.isfile('user\Desktop\New folder\Python')
#if os.path.exists(path):
# print("it's exist")


import fileinput
replacements = {'Search1': 'Replace1',
 'Search2': 'Replace2'}
for line in fileinput.input('text2.txt', inplace=True):
 for search_for in replacements:
  replace_with = replacements[search_for]
  line = line.replace(search_for, replace_with)
 print(line, end='')



'''import pathlib
path = pathlib.Path('C:/Users/user/Desktop/New folder/Python/file.txt')
print("hi")
if path.is_file():
 print("its here")
# Random access file using mmap
import mmap
with open('text2.txt', 'r') as fd:
 # 0: map the whole file
 mm = mmap.mmap(fd.fileno(), 0)
 # print characters at indices 5 through 10
 print(mm[5:10])
 # print the line starting from mm's current position
 print(mm.readline())
 # write a character to the 5th index
 mm[5] = 'a'
 # return mm's position to the beginning of the file
 mm.seek(0)
 # close the mmap object
 mm.close()'''

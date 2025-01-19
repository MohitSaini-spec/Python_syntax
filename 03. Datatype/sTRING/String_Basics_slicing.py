# SLICING
add_string="hey! "+"everyone" 
join_string="hello","world"
# SYNTAX :var_name[starting index*include : ending index*exclude : Jumping gap*optional]
print("SLICING OF VARIABLE HAVING SINGLE STRING")
print("Slicing [0:3]      :",add_string[0:3])                   # hey
print("Slicing [:3]       :",add_string[:4] )                   # hey!
print("Slicing [5:len()]  :",add_string[5:len(add_string)])     # everyone
print("Slicing [5:]       :",add_string[5:] )                   # everyone
print("slicing [0::2]     :",add_string[0::3])                  # h!vye        #jump 2
print("Slicing [-10:len()]:",add_string[-10:len(add_string)])   # ! everyone 
print("Slicing [-10:]     :",add_string[-10:])                  # ! everyone
print("Slicing [-5:]      :",add_string[-5:])                   # ryone

print("SLICING OF VARIABLE HAVING MULTIPLE STRING")
print("Slicing [:]        :",join_string[:])                    # ('hello','world')
print("Slicing [:len()]   :",join_string[:len(join_string)])    # ('hello','world')
print("Slicing [:1]       :",join_string[:1])                   # ('hello',)
print("Slicing [1:]       :",join_string[1:])                   # ('world',)
print("Slicing [:][-1]    :",join_string[:][-2])                # hello
print("Slicing [:1][-1]   :",join_string[1:][-1])               # world
print("Slicing [-1][0:3]  :",join_string[-1][0:3])              #wor


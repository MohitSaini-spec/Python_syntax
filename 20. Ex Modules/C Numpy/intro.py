
# not arranged after reshaping and before seraching


import numpy as np
print(f'{"Detail":~^50}')
print("Version :",np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print("Type :",type(arr))

print(f'{"Creating":~^50}')
print("Direct printing array :",arr)

print(f'{"Indexing":~^50}')
# Dimension in array& indexing
a = np.array(42)                                                # 0 D
b = np.array([1, 2, 3, 4, 5])                                   # 1 D
c = np.array([[1, 2, 3], [4, 5, 6]])                            # 2 D
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # 3 D

print("Depth :",a.ndim)       # no index 

print("Depth :",b.ndim)       # 1 index []
# print(b[-3] + b[-2])
# print(b[1:5],"\n")

print("Depth :",c.ndim)       # 2 index [] []
# print(c[-2,-1])
# print(c[1, 1:4])
# print(c[0:2, 1:2],"\n")

print("Depth :",d.ndim)       # 3 index [] [] []
# print(d[0, 1, 2])
# print(d[1,0, 1:],"\n")
 

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('dimensions\depth manual :', arr.ndim)

# Datatytpe--------------------------------------------------------------
print(f'{" DataType ":~^50}')

arr = np.array([1, 2, 3, 4])
print("Automatic :",arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')
print("DataType with S:",arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='i4') #4byte integer
print("DataType with i4:",arr.dtype)

# Typecasting-------------------------------------
print(f'{" Typecasting ":~^50}')

arr = np.array([1.1, 2.1, 3.1])
print("Before Typecasting :",arr)
newarr = arr.astype('i')
print("After Typecasting :",newarr)
print("Type :",newarr.dtype)

# Copy & View-------------------------------------
print(f'{" Copy & View ":~^50}')

rr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()
view =arr.view()
arr[0] = 42
view[1] = 43

print("Original :",arr)
print("Copy :",copy)       # Copy
print("View  :",view)       # Change original

print("Base of copy :",copy.base)   # Duplicated
print("Base of view :",view.base)   # Owns data

# Array shape-------------------------------------------
print(f'{" Shape ":~^50}')

arr = np.array([1, 2, 3, 4] , ndmin=5)

print("Note:No of result represent depth and \n    digit reprenent no of element on that depth")
print('Shape of array  :', arr.shape)   # NO. of result shows dimension and value shows no. of element 
 
# Array reshapeing--------------------------------------
print(f'{" Reshaping ":~^50}')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)          # Multiplication of value = no. of element (4 array of 3 element)----
type = newarr.base
print("Base:",type)                         # View
print("Array:",newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)      # -1 automatically dectect no.------
print("Reshaping with -1 :",newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)            # Multidimensional array to 1 d array------
print("Reshaping to 1D:",newarr)

# Array iteration

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)                  # Don't triverse each elemet seperately

for x in arr:
  for y in x:
    for z in y:             # for 3d array
      print(z)

for x in np.nditer(arr):    # Iterate each element with single loop--------- 
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):  # Chanmge datatype in buffer not in original
  print(x)

arr = np.array([[1, 2, 3, 4, 5 ], [ 6, 7, 8, 9 ,0]])
for x in np.nditer(arr[:, ::2]):                # with Jumping steps 
  print(x)

for idx, x in np.ndenumerate(arr):              # Using ndenumate
  print("iteration with indexing :",idx, x)

# Joining array-----------------------------------------------
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)       # With axis 1 join 1st array with first arry of another array
arr3 = np.concatenate((arr1, arr2))              # **conbine arrays**
print("With axis 1 :",arr,
      "\nWithout axis para",arr3)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)            # STACK **combine elements** with the same index no.
print("Stack(axis =1)",arr)

arr = np.hstack((arr1, arr2))                   # hstak in sequence
print("Hstack",arr)

arr = np.concatenate((arr1, arr2))
print("Concatenate :",arr)

arr = np.vstack((arr1, arr2))                   # put array of same index as a sub element
print(arr)

arr = np.dstack((arr1, arr2))
print(arr)

# Spliting----------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])    # Indexing

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)     # alternate of hsplit
print(newarr)

ewarr = np.hsplit(arr, 3)                   # alternate of array_split(axis=1)
print(newarr)

#Searching-------------------------------------------------------------------
print(f'{" Seaching ":~^50}')


arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)                # where ===========
y = np.where(arr%2 == 0)              # seraching even
print(x,y)
#search sorted

x = np.searchsorted(arr, 7)           # return index form left
y = np.searchsorted(arr, 7, side='right') #return indexz from right
z = np.searchsorted(arr, [2, 4, 6])
print("Index from left:",x,"\nIndex from right",y,"\nIndex of given element",z)


# Sort -------------------------------------------------------------------
print(f'{" Sort ":~^50}')

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))      # sort false first in boolean

# Filter ------------------------------------------------------------------------
print(f'{" Filter ":~^50}')

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print("Manual :",filter_arr)
print("Manual :",newarr)



array = np.array([41, 42, 43, 44])
filter_array = array > 42
newarray = array[filter_array]
print("Automatically :",filter_array)
print("Automatically :",newarray)
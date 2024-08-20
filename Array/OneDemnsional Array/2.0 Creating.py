'''
 When we create an array ,we 
  -Assign  it to a variable
  -Define the type of elements that it will 
  -Define its size ( the maximum  numbers of elements)
'''

#  Creating an array (Array Module)

from array import *
# arrayName=array(typecode,[initializers])
array1=array('i',[1,2,3,4,5])
array2=array('d',[1.3,1.5,1.6])
print(array1)
print(array2)

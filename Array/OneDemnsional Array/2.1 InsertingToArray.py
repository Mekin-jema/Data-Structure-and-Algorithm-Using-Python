# Insertion

from array import *

myArray1=array('i',[1,2,3,4,5,6,7])
myArray2=array('d',[1,2,3,4,5,6,7])


myArray2.insert(7,8)
print(myArray2)


# Time Complexity 
'''
    -insertion at the beginning of the array=O(n)
    -insertion at the end of the array O(1)
    -insertion at  the full array to the end is O(n)
'''
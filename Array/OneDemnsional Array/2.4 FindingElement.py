from array import *
myArray2=array('d',[1,2,3,4,5,6,7])

def searchingArray(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return " The element does not exist in this array"

print(searchingArray(myArray2,7))
print(searchingArray(myArray2,5))
print(searchingArray(myArray2,10))

#  Time Complexity and Space  Complexity
#   -space complexity=)(n)
    

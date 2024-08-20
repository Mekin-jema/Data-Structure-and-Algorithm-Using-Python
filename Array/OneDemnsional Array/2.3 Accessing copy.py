from array import *
myArray2=array('d',[1,2,3,4,5,6,7])


def accessElement(array,index):
    if index >=len(array):
        print("There is not any element in this index")
    else:
        print(array[index])
        
accessElement(myArray2,6)
# Time and Space Complexity
'''
  Both time and space is constant
'''
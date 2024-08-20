import numpy as np

myTwoD=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,1],[2,4,6,8]])
print(myTwoD)

# myTwoD=np.insert(myTwoD,0,[[4,5,7,3]],axis=0)
# print(myTwoD)

def accessing(array,row,colum):
    if row>=len(array) and colum>=len(array[0]):
        print("row or column can not be greater than length of array")
    else:
        print(array[row][colum])

accessing(myTwoD,4,3)
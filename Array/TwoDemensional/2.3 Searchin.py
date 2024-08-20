import numpy as np

myTwoD=np.array([[1,2,3,4],[6,5,7,7],[7,8,9,1],[2,4,6,8]])
mybreak=False
for i in range(4):
    for j in range(4):
        if myTwoD[i][j]==6:
            mybreak=True
            break
    if mybreak:
        break
    
    

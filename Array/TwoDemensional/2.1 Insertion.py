import numpy as np

twoDArray=np.array([[11,15,10,16],[33,32,24,43],[34,35,63,23],[22,33,41,55]])
# print(twoDArray)

#  Adding column   see  Adding column image
#  adding Row  # see adding row image
# In Both time complexity is O(M*N)


newTwoDArray=np.insert(twoDArray,3,[[1,2,3,4]],axis=1)
print(newTwoDArray) 


# #  Using append
# newTwoDArray=np.append(twoDArray,1,[[1,2,3,4]],axis=1)
# print(newTwoDArray)  

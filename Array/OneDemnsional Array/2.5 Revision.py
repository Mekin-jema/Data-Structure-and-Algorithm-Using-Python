from array import *
#  1. Crete an array and traverse.

my_array=array('i',[1,2,3,4,5,6,7])

for i in my_array:
    print(i)
 
#  2. Access individual elements through  indexes
print(my_array[6])

#  3. Append  any value  to the array using append method()
my_array.append(19)
print(my_array)

#  4. Insert value in an array using insert() method
my_array.insert(0,44)
print(my_array)
 
# 5. Extend  python array using extend () method
my_array1=array('i',[10,11,12,13,14,15])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list inot array using fromList() method
tempList=[20,21,22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove  ay array element using remove()
my_array.remove(44)
print(my_array)

# 8. Remove Lst array element using  pop()
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print(my_array.index(6))  # it will tell you the index of the given value

# 10. Reverse a python array using reverse() method
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print(my_array.buffer_info())

# 12. Check for number of occurrence of  an element using count() method
my_array.append(20)  #  i am adding another 20 number for checking counting 
print(my_array.count(20))

# 13.Converting array  to string using toString() method
    # strTemp=my_array.tostring()
    # print(strTemp)

# 14. Convert array to a python list with same elements using tolist( ) method
print(my_array.tolist())

# 15. Append a string  to char array using fromstring() method

# 16 . Slice Elements from an array
print( my_array[1:5])

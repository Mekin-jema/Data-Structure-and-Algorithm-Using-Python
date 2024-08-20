myList=[1,2,3,4,5,6,7]

#  LIst Methods
#    -insert()   
myList.insert(0,11) #Time complexity at the beginning oof the list is BIG of N
#    -append()
myList.append(45)  # Efficient  way of inserting at the end of the list
#    -extend()
newList=[3,4,6,6]
myList.extend(newList) # it is looping to the new list and add it  to the oldest one so it is big of ON  

print(myList) 
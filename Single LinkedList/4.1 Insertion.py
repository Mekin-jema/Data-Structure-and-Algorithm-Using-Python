class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head ==None:  # If the list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # Insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert in the middle
                index = 0
                tempNode = self.head
                while index < location - 1 : #and tempNode.next is not None :
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode
                # if newNode.next is None:
                #     self.tail = newNode

    def print(self):
         if self.head is None:
            print("The list is empty")
         else:
            temp = self.head
            items = []
            while temp:
                items.append(str(temp.value))
                temp = temp.next
            print("-->".join(items))

# Testing the linked list
singleLinkedList = SLinkedList()
singleLinkedList.insert(1, 0)
singleLinkedList.insert(2, 1)
singleLinkedList.insert(3, 2)
singleLinkedList.insert(4, 3)
singleLinkedList.insert(5, 4)
singleLinkedList.print()

# Alternatively, you can iterate using:
# for node in singleLinkedList:
#      print(node.value)

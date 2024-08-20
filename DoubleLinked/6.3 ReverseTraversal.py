class Node:
    def __init__(self,value=None):
        self.next=None
        self.prev=None
        self.value=value
    
class doubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    # def __iter__(self):
    #     node=self.head
    #     while node:
    #         yield node 
    #         node=node.next
    # Creation of Doubly linked List
    def CreateDLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=None
        node.prev=None
        self.tail=node
        self.head=node
        return" The double linked List is created"
    
    
    def Insert(self,value,location):
        newNode=Node(value)
        # newNode.next=None
        # newNode.prev=None
    
        if self.head is None:
            print( " LInked list is empty")
            
        else:
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index <location-1 :
                    tempNode=tempNode.next 
                    index+=1
                newNode.next=tempNode.next
                newNode.prev= tempNode
                newNode.next.prev= newNode
                tempNode.next=newNode
#  Traversal Method in Doubly linked list
    def print(self):
        tempNode=self.head
        while tempNode :
             print(tempNode.value)
             tempNode=tempNode.next
#  Reverse Traversal Method in Doubly linked list
    def ReverseTraversal(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.value)
            tempNode=tempNode.prev  
doubleLL=doubleLinkedList()
doubleLL.CreateDLL(2)
doubleLL.Insert(1,0)
doubleLL.Insert(2,2)
doubleLL.Insert(3,3)
doubleLL.Insert(4,4)
doubleLL.print()
doubleLL.ReverseTraversal()
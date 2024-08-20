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
    
    
    def CreateDoubleLinkedLIst(self,value,location):
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
                while index <location-1 and tempNode is not None:
                    tempNode=tempNode.next 
                    index+=1
                newNode.next=tempNode.next
                newNode.prev= tempNode
                newNode.next.prev= newNode
                tempNode.next=newNode
#  Traversal Method in Doubly linked list
    def print(self):
        tempNode=self.head
        while tempNode != self.tail:
             print(tempNode.value)
             tempNode=tempNode.next
#  Reverse traversal doubly linkedlist   
    def ReverseTraversal(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.value)
            tempNode=tempNode.prev  
    def deleteNode(self,location):
        if self.head is None:
            print("There si not any element in DLL")
        else:
            if location==0:
                if self.head.next is None:
                    self.head =None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                if self.head.next is None:
                    self.head =None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                index=0
                tempNode=self.head
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                tempNode.next=tempNode.next.next 
                tempNode.next.prev=tempNode
            
doubleLL=doubleLinkedList()
doubleLL.CreateDLL(0)
doubleLL.CreateDoubleLinkedLIst(1,0)
doubleLL.CreateDoubleLinkedLIst(2,1)
doubleLL.CreateDoubleLinkedLIst(3,2)
doubleLL.CreateDoubleLinkedLIst(4,3)
doubleLL.print()
# doubleLL.ReverseTraversal()
print("================")
doubleLL.deleteNode(0)
doubleLL.print()
print("================")
doubleLL.deleteNode(0)
doubleLL.print()
# doubleLL.ReverseTraversal()
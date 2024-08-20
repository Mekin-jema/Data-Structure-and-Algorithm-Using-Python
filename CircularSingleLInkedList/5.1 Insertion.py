#  Circular Singly Linked list -Insertion
#    Insert at the beginning of linked list
#    insert at the specified location of linked list
#    insert at the end of linked ist

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node =self.head
        while node:
            yield node
            if node.next==self.tail.next:
                break
            node=node.next
#  Creation of circular singly linked list
    def  createCSLL(self,nodeValue):  # The time  and space complexity is big of one
        node =Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return " The Circular linked list has been created "
    #  Insertion of a node in circular singly linked list
    def InsertiCSLL(self,value,location):  
        if self.head is None: # big of one
            return " The head reference is None"
        else:                  # big of one
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:  # big of one 
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:             # big of N 
                index=0
                tempNode=self.head
                while index< location-1:  
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            return "The Node has been successfully created"

        
        
circularSLL=CircularSinglyLinkedList()
circularSLL.createCSLL(12)
circularSLL.createCSLL(11)
circularSLL.InsertiCSLL(1,0)
circularSLL.InsertiCSLL(2,1)
circularSLL.InsertiCSLL(3,2)
circularSLL.InsertiCSLL(4,3)
print([node.value for node in circularSLL])


  
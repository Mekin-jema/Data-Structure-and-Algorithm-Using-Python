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
            if node.next==self.head:
                break
            node=node.next
#  Creation of circular singly linked list
    def  createCSLL(self,nodeValue):  # The time  and space complexity is big of one
        node =Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return " The Circular linked list has been created "
circularSLL=CircularSinglyLinkedList()
circularSLL.createCSLL(12)
circularSLL.createCSLL(11)
print([node.value for node in circularSLL])
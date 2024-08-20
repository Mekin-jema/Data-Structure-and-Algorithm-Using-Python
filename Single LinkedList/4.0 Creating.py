class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

     

singleLinkedList=SLinkedList()
Node1=Node(3)
Node2=Node(5)
singleLinkedList.head=Node1
singleLinkedList.head.next=Node2
singleLinkedList.tail=Node2
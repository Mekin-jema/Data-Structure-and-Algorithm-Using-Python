
class Node:
    def __init__(self,value=None):
        self.next=None
        self.value=value
    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        tempNode=self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next

class Queue:
    def __init__(self):
        self.linkedList=LinkedList()
    
    def __str__(self):
        values=[str(x) for x in self.linkedList ]
        return "-->".join(values)
    
    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedList.head is None:
            self.linkedList.head=newNode
            self.linkedList.tail=newNode
        else:
            self.linkedList.tail.next=newNode
            self.linkedList.tail=newNode
            
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    
    def dequeue(self):
        if self.isEmpty():
            return " We don't have any node to be dequeued"
        else:
            tempNode=self.linkedList.head
            if self.linkedList.head==self.linkedList.tail:
                self.linkedList.head=None
                self.linkedList.tail=None
            else:
                self.linkedList.head=self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return " The queue is empty"
        return self.linkedList.head
    
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None
        

custQueue=Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
# print(custQueue.dequeue())
print(custQueue.dequeue())
print(custQueue.dequeue())
print("              ")
print(custQueue.peek())
custQueue.delete()
print(custQueue)
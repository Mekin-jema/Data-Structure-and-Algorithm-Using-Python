class Queue:
    def __init__(self):
        self.Items=[]
        
    def __str__(self):
        values=[str(x) for x in self.Items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.Items==[]:
            return True
        return False
    
    def enqueue(self,value):
        self.Items.append(value)
        return " The elements is inserted at the end of queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the queue"
        return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the queue"
        return self.Items[0]
    
    def delete(self):
        self.Items=None
            
customQueue=Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
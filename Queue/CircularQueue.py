class CircularQueue:
    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1
        
    def __str__(self):
        values=[str(x) for x in self.items]
        return "-->".join(values)   
    def isFull(self):
        if self.start-1==self.top:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        return False
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    def enqueue(self,value):
        if self.isFull():
            print("The list full can not be inseted")
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
    
    def dequeue(self):
        if self.isEmpty():
            return " The list is empty ,can not be deleted"
        else:
          firstElement=self.items[self.start]
          start=self.start
          if self.start==self.top:
              self.start=0
              self.top=0
          elif self.start +1==self.maxSize:
              self.start=0
          else:
              self.start+=1
          self.items[start]=None
          return firstElement
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        return self.items[self.start]
    def delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1
    
            
CQueue=CircularQueue(6)
CQueue.enqueue(1)
CQueue.enqueue(2)
CQueue.enqueue(3)
CQueue.delete()
print(CQueue.isEmpty())
print(CQueue)
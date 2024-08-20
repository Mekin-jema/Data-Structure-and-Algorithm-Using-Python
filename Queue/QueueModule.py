import queue as q
custQueue=q.Queue(maxsize=3)
print(custQueue.empty())
custQueue.put(1)
custQueue.put(2)
custQueue.put(3)
# custQueue.put(4)
print(custQueue.get())
print(custQueue.full())
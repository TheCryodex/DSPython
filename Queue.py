class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.insert(0, data)
        
    def dequeue(self):
        if not self.isempty():
            return self.pop()
            
    def isempty(self):
        return(self.queue == [])
    
    def __len__(self):
        return (len(self.queue))
        
    def view(self):
        if not self.isempty():
            return(self.queue[-1])

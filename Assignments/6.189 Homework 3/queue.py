# Name: Tyler Brown
# Section:
# queue.py

# **********  Exercise 3.6 **********

class Queue:
    # A class the represents a queue
    
    def __init__(self, line = 0):
        #initialization method 

        #Make 2 object methods 
        self.line = line = []
        
    def insert(self, line):
        print self.line.append(line)
        
    def remove(self):
        
        if self.line == []: #if queue empty
            print 'Empty dude'
        
        else: #remove
            print self.line[0]
            self.line.remove(self.line[0])
      
# Test Cases for Exercise 3.6 

queue = Queue()  
queue.insert(5)
queue.insert(6)
print queue.remove()
print queue.remove()
print queue.remove()

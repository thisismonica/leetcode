class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        ss = []
        while self.stack:
            ss.append( (self.stack.pop()) )
        self.stack.append(x)
        while ss:
            self.stack.append( (ss.pop()) )

# @return nothing
def pop(self):
    self.stack.pop()
    
    # @return an integer
    def peek(self):
        return self.stack[-1]
    
    # @return an boolean
    def empty(self):
        return self.stack==[]
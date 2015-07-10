class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.list = []
        self.head = -1
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.head += 1
        if len(self.list) == self.head:
            self.list.append( x )
        else:
            self.list[self.head] = x

# @return nothing
def pop(self):
    self.head -= 1
    
    # @return an integer
    def top(self):
        return self.list[self.head]
    
    # @return an boolean
    def empty(self):
        return self.head == -1
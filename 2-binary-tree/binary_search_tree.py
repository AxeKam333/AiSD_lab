class Node():
    def __init__(self, value=None):
        self.L = None
        self.R = None
        self.value = value
    
    def insert(self, v):
        if self.value == None:
            self.value = v
            return
        
        if v < self.value:
            if self.L != None:
                self.L.insert(v)
                return
            self.L = Node(v)
            return
        
        if v > self.value:
            if self.R != None:
                self.R.insert(v)
                return
            self.R = Node(v)
            return
    
    def find(self, v):
        if self.value == v:
            return True
        
        if v < self.value:
            if self.L == None:
                return False
            return self.L.find(v)
        
        if v > self.value:
            if self.R == None:
                return False
            return self.R.find(v)
        
    def height(self):
        if self.L == None:
            left = 0
        else:
            left = self.L.height()
        
        if self.R == None:
            right = 0
        else:
            right = self.R.height()
        
        return max(left,right) + 1
            

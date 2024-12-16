class Node:
    def __init__(self,key,value,bin=None,parent=None,):
        self.key=key
        self.value=value
        self.right=None 
        self.left=None
        self.parent=parent 
        self.height=1
        self.duplicates=None
        self.bin=bin
        pass
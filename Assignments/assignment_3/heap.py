class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        '''
        self.init_array = init_array[:]
        self.comparison_function = comparison_function
        if len(self.init_array) > 1:
            self.heapify()
    
    def parent(self, j):
        return (j-1)//2
    
    def left_child(self, j):
        return 2*j + 1
    
    def right_child(self, j):
        return 2*j + 2
    
    def swap(self, i, j):
        self.init_array[i], self.init_array[j] = self.init_array[j], self.init_array[i]
    
    def downheap(self, j):
        minindex = j
        size = len(self.init_array)
        left = self.left_child(j)
        if left < size and self.comparison_function(self.init_array[left], self.init_array[minindex]):  # Fixed: pass values not indices
            minindex = left
        right = self.right_child(j)
        if right < size and self.comparison_function(self.init_array[right], self.init_array[minindex]):  # Fixed: pass values not indices
            minindex = right
        if minindex != j:
            self.swap(j, minindex)
            self.downheap(minindex)
    
    def upheap(self, j):
        while j > 0 and self.comparison_function(self.init_array[j], self.init_array[self.parent(j)]):  # Fixed: pass values not indices
            self.swap(j, self.parent(j))
            j = self.parent(j)
    
    def heapify(self):
        start = self.parent(len(self.init_array)-1)  # Fixed: len(self) to len(self.init_array)
        for j in range(start, -1, -1):
            self.downheap(j)
    
    def insert(self, value):
        self.init_array.append(value)
        self.upheap(len(self.init_array)-1)
    
    def extract(self):
        if not self.init_array:  # Added check for empty heap
            raise IndexError("Heap is empty")
        self.swap(0, len(self.init_array)-1)
        min_val = self.init_array.pop()
        if self.init_array:  # Only downheap if heap isn't empty after pop
            self.downheap(0)
        return min_val
    
    def top(self):
        if len(self.init_array) == 0:
            raise IndexError("Heap is empty")  # Fixed: specify the error type
        return self.init_array[0]
    

    def is_empty(self):
        
        return len(self.init_array) == 0

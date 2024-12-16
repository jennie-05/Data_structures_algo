from hash_table import HashSet, HashMap
from prime_generator import get_next_size


class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        
        new_table_size = get_next_size()
        
        
        prev_table = self.table.copy()
        
        
        self.table = [None] * new_table_size

        old_size = self.table_size

        self.table_size = new_table_size


        self.count = 0  

        
        if self.collision_type == "Chain":
            for slot in prev_table:




                if slot is not None:
                    for item in slot:
                        super().insert(item)  
        else:
            for item in prev_table:
                if item is not None:
                    super().insert(item)  
    def __str__(self):

        return super()._str_()   
    def insert(self, x):

        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        
        new_table_size = get_next_size()
        
        
        prev_table = self.table.copy()
        
        
        self.table = [None] * new_table_size


        old_size = self.table_size
        self.table_size = new_table_size
        self.count = 0  

        
        if self.collision_type == "Chain":
            for slot in prev_table:
                if slot is not None:


                    
                    for key_value in slot:
                        super().insert(key_value) 
        else:
            for key_value in prev_table:
                if key_value is not None:
                    super().insert(key_value) 
    def __str__(self):

        return super()._str_()  
    def insert(self, key):

        super().insert(key)
        
        if self.get_load() >= 0.5:

            self.rehash()
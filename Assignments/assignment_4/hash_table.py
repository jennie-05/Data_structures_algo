from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        self.collision_type=collision_type
        self.params=params
        # alag alag type of coliision k liye alag alag init function define kara hai
        if collision_type=="Chain":
            self.z=params[0]
            self.table_size=params[1]
            self.table=[None]*self.table_size
            #count is the parametehr which counts jab bhi ek element add hota hai

            self.count=0
        if collision_type=="Linear":
            self.z=params[0]
            self.table_size=params[1]
            #initializing the initial array as none
            self.table=[None]*self.table_size
            self.count=0
        if collision_type=="Double":
            self.z1=params[0]
            self.z2=params[1]
            self.c2=params[2]
            self.table_size=params[3]
            self.table=[None]*self.table_size
            self.count=0

        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        pass
    def hash_code(self, key, mult_factor):

        result = 0

        position_value = 1
        
        for letter in key:

            if letter.islower():
                
                result += (ord(letter) - 97) * position_value

            elif letter.isupper():
                
                result += (ord(letter) - 65 + 26) * position_value
                
            position_value *= mult_factor
            
        return result
   
        
    
    def insert(self, x):

        #get the inialise slot using get slot
        hash_key = self.get_slot(x)
        if type(x)==tuple:


            key=x[0]
        else:
            key=x
        #process for chain
        if self.collision_type == "Chain":

            if self.table[hash_key] is None:

                self.table[hash_key] = []
            if x not in self.table[hash_key]:  
                self.table[hash_key].append(x)
                self.count += 1
        #process for linear    
        elif self.collision_type == "Linear":


            slot = hash_key
            i = 0
            
            current_slot = slot
            while self.table[current_slot] is not None:
                if self.table[current_slot] == x:  
                    return
                current_slot = (hash_key + i) % self.table_size
                i += 1
                if current_slot == slot: 
                    break
                    
            
            slot = hash_key
            i = 0
            while self.table[slot] is not None and i<self.table_size:
                slot = (hash_key + i) % self.table_size
                i += 1
            if self.table[slot] is None:
                self.table[slot] = x
                self.count += 1
        #process for double       
        elif self.collision_type == "Double":
            slot = hash_key
            step_size = self.c2 - (self.hash_code(x, self.z2) % self.c2)
            i = 1
            
            current_slot = slot
            while self.table[current_slot] is not None and i<self.table_size:


                if self.table[current_slot] == x:  
                    return
                current_slot = (hash_key + i * step_size) % self.table_size
                i += 1
                if current_slot == slot:  
                    break
                    
            
            slot = hash_key
            i = 0
            while self.table[slot] is not None and i<self.table_size:
                slot = (hash_key + i * step_size) % self.table_size




                i += 1
            if self.table[slot] is None:
                self.table[slot] = x
                self.count += 1

    
   
    def find(self, key):
        hash_key = self.get_slot(key)

        if self.collision_type == "Chain":
            
            chain = self.table[hash_key]
            if chain is None:
                return False
            
            for item in chain:
                if item == key:
                    return True
            return False

        elif self.collision_type == "Linear":
            # Linear probing
            slot = hash_key
            i = 0
            while self.table[slot] is not None and i<self.table_size:
                if self.table[slot] == key:
                    return True
                slot = (hash_key + i) % self.table_size
                i += 1
            return False

        elif self.collision_type == "Double":
            # Double hashing
            slot = hash_key
            step_size = self.c2 - (self.hash_code(key, self.z2) % self.c2)
            i = 0
            while self.table[slot] is not None and i<self.table_size:
                if self.table[slot] == key:
                    return True
                slot = (hash_key + i * step_size) % self.table_size
                i += 1
            return False

    
   
    
    def get_slot(self, key):

        if self.collision_type=="Chain":
            return self.hash_code(key,self.z) % self.table_size
        
        elif self.collision_type=="Linear":
            return self.hash_code(key,self.z) % self.table_size
        
        elif self.collision_type=="Double":
            return self.hash_code(key,self.z1) % self.table_size
        
    
    def get_load(self):
        load=self.count/self.table_size
        return load
        
    
    
    def _str_(self):
       
        
        result = []
        for item in self.table:
            if item is None:
                
                result.append("<EMPTY>")
            elif isinstance(item, list):
               
                chain_entries = []

                for entry in item:

                    if isinstance(entry, tuple):  

                        chain_entries.append(f"({entry[0]}, {entry[1]})")


                    else: 

                        chain_entries.append(str(entry))
                result.append(" ; ".join(chain_entries))
            else:
                
                if isinstance(item, tuple):  
                    result.append(f"({item[0]}, {item[1]})")

                else:  

                    result.append(str(item))

        
        return " | ".join(result)


        
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    # def rehash(self):
         
    #     # Store old table and its size
    #     old_table = self.table
    #     old_size = self.table_size
        
    #     # Get new size (next prime number > 2 * old_size)
    #     new_size = get_next_size(old_size)
        
    #     # Reset table with new size
    #     self.table_size = new_size
    #     self.table = [None] * new_size
    #     rehashed_table=HashTable(self.collision_type,self.params)
    #     self.count = 0  # Reset count as we'll increment during insertions
        
    #     # Rehash elements based on collision type
    #     if self.collision_type == "Chain":
    #         # For chaining, iterate through each slot and its chain
    #         for slot in old_table:
    #             if slot is not None:
    #                 for element in slot:
    #                     rehashed_table.insert(element)
                        
    #     else:  # For Linear and Double probing
    #         # Iterate through each slot
    #         for slot in old_table:
    #             if slot is not None:
    #                 rehashed_table.insert(slot)
    #     return rehashed_table
    #     pass
    def rehash(self):
        new_table_size = get_next_size(self.table_size)
        prev_table = [i for i in self.table]
        self.table = [None] * new_table_size
        self.table_size = new_table_size
        self.count = 0  
        if self.collision_type == "Chain":
            for slot in prev_table:
                if slot is not None:
                    for item in slot:
                        self.insert(item)
        else:
            for item in prev_table:
                if item is not None:
                    self.insert(item)
    
        
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    

class HashSet(HashTable):
    def _init_(self, collision_type, params):
        
        super()._init_(collision_type, params)

    def insert(self, key):
        
        super().insert(key)

    def find(self, key):
        
        return super().find(key)
    def get_slot(self, key):
        return super().get_slot(key)
        pass
    
    def get_load(self):
        return super().get_load()
        pass
    

    def _str_(self):
        
        return super()._str_()

class HashMap(HashTable):
    def _init_(self, collision_type, params):
        
        super()._init_(collision_type, params)

    def insert(self, x):
        
        key=x[0]

    
        slot = self.get_slot(key)
        
        if self.collision_type == "Chain":


            
            if self.find(key)==None or self.find(key)==False:
                if self.table[slot] is None:
                    self.table[slot] = [x]
            
            # for i, item in enumerate(self.table[slot]):
            #     if item[0] == key:  # Update the value for an existing key
            #         self.table[slot][i] = (key, value)
            #         return
            # If key not found, add (key, value) to the chain
                else:
                    self.table[slot].append(x)
            self.count += 1

        elif self.collision_type == "Linear":
            i = 0
            while self.table[slot] is not None and self.table[slot][0] != key:
                slot = (slot + 1) % self.table_size
                i += 1
            if self.table[slot] is None:
                self.count += 1  
            self.table[slot] = x  

        elif self.collision_type == "Double":
            step_size = self.c2 - (self.hash_code(key, self.z2) % self.c2)
            i = 0
            while self.table[slot] is not None and self.table[slot][0] != key:
                slot = (slot + i * step_size) % self.table_size
                i += 1
            if self.table[slot] is None:
                self.count += 1  # Increment count only if it's a new insertion
            self.table[slot] = x  # Insert or update (key, value)

    def find(self, key):
        
        slot = self.get_slot(key)

        if self.collision_type == "Chain":
            chain = self.table[slot]

            if chain is None:

                return None
            
            for item in chain:

                if item[0] == key:

                    return item[1]
            return None

        elif self.collision_type == "Linear":
            i = 0

            while self.table[slot] is not None:
                if self.table[slot][0] == key:

                    return self.table[slot][1]
                
                slot = (slot + 1) % self.table_size
                i += 1
            return None

        elif self.collision_type == "Double":
            step_size = self.c2 - (self.hash_code(key, self.z2) % self.c2)


            i = 0
            while self.table[slot] is not None:
                if self.table[slot][0] == key:



                    return self.table[slot][1]
                slot = (slot + i * step_size) % self.table_size

                i += 1
            return None
    def get_slot(self, key):
        
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()

    def _str_(self):
        # Use the base class _str_, which will handle HashMap formatting
        return super()._str_()
    

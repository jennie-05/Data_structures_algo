from hash_table import HashSet,HashMap 

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        #creating a new list for appending book titles 
        self.book_titles =[]
        for i in book_titles:
            self.book_titles.append(i)
        #creating a new list for appending texts 
        self.texts = []
        for i in texts:
            self.texts.append(i)
        #creating a new list which stores the index of the book of the old list  and book titles as a list and appending it
        booksind = []
        for i in range(len(book_titles)):
            x = [i, book_titles[i]]
            booksind.append(x)
        #merge sorting the bookind on the basis of book alphabetically 

        self.booksind = self.merge_sort_books(booksind)  
        for j in range(len(texts)):
            word_pairs = [[word, ''] for word in self.texts[j]]  
            #merge sorting the texts for each book
            self.texts[j] = [pair[0] for pair in self.merge_sort(word_pairs)]  

    def merge_books(self, left, right):
        sorted_unique = []
        i = j = 0
        #modifying merge sort for a list 
    
        while i < len(left) and j < len(right):
            
            if left[i][1] < right[j][1]:
                if not sorted_unique or sorted_unique[-1][1] != left[i][1]:
                    sorted_unique.append(left[i])
                i += 1
            elif left[i][1] > right[j][1]:
                if not sorted_unique or sorted_unique[-1][1] != right[j][1]:
                    sorted_unique.append(right[j])
                j += 1
            else:  
                if not sorted_unique or sorted_unique[-1][1] != left[i][1]:
                    sorted_unique.append(left[i])
                i += 1
                j += 1
        
        while i < len(left):
            if not sorted_unique or sorted_unique[-1][1] != left[i][1]:
                sorted_unique.append(left[i])
            i += 1
    
        while j < len(right):
            if not sorted_unique or sorted_unique[-1][1] != right[j][1]:
                sorted_unique.append(right[j])
            j += 1
        
        return sorted_unique

    def merge_sort_books(self, arr):
    
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort_books(arr[:mid])
        right_half = self.merge_sort_books(arr[mid:])
        
        return self.merge_books(left_half, right_half)
    def merge(self, left, right):
        sorted_unique = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                if not sorted_unique or sorted_unique[-1] != left[i]:
                    sorted_unique.append(left[i])
                i += 1
            elif left[i] > right[j]:
                if not sorted_unique or sorted_unique[-1] != right[j]:
                    sorted_unique.append(right[j])
                j += 1
            else:
                if not sorted_unique or sorted_unique[-1] != left[i]:
                    sorted_unique.append(left[i])
                i += 1
                j += 1
        
        while i < len(left):
            if not sorted_unique or sorted_unique[-1] != left[i]:
                sorted_unique.append(left[i])
            i += 1
        
        while j < len(right):
            if not sorted_unique or sorted_unique[-1] != right[j]:
                sorted_unique.append(right[j])
            j += 1
        
        return sorted_unique

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])

        right_half = self.merge_sort(arr[mid:])
        
        return self.merge(left_half, right_half)
     
    def binary_search(self,arr, x):
     # normal binary serach
        low = 0
        high = len(arr) - 1
        
        
        def binary_search_helper(low, high):
            
            if high >= low:
                mid = (high + low) // 2
                
                
                if arr[mid] == x:
                    return mid
                    
                

                elif arr[mid] > x:
                    return binary_search_helper(low, mid - 1)
                    
            
                else:
                    return binary_search_helper(mid + 1, high)
                    
            else:
            
                return -1
                
        return binary_search_helper(low, high)
    
    def distinct_words(self, book_title):
        for item in self.booksind:
            if item[1] == book_title:  
                index = item[0] 
                return self.texts[index]
        pass
    
    def count_distinct_words(self, book_title):
        for item in self.booksind:
            if item[1] == book_title: 
                index = item[0]  
                return len(self.texts[index])

        pass
    
    def search_keyword(self, keyword):
        key_books = []
        for i in range(len(self.booksind)):  
            y=self.booksind[i][0]
            x = self.binary_search(self.texts[y], keyword)
            if x != -1:
                key_books.append(self.booksind[i][1])
        return key_books
        
    
    def print_books(self):
        for i in self.booksind:
            book_title = i[1]
            book_index = i[0]
            words = self.texts[book_index]
        
            book_title_str = f"{book_title}: "
            
            words_str = " | ".join(word.strip() for word in words)
            print(book_title_str + words_str)
    
    


        pass
class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        if name == "Jobs":
            self.collision_type = "Chain"
            z, initial_table_size = params
            self.hashmap = HashMap(self.collision_type, [z, initial_table_size])
        elif name == "Gates":
            self.collision_type = "Linear"
            z, initial_table_size = params
            self.hashmap = HashMap(self.collision_type, [z, initial_table_size])
        elif name == "Bezos":
            self.collision_type = "Double"
            z1, z2, c2, initial_table_size = params
            self.hashmap = HashMap(self.collision_type, [z1, z2, c2, initial_table_size])
    
    def add_book(self, book_title, text):
        if self.name == "Jobs":
            self.collision_type = "Chain"
            z, initial_table_size = self.params
            self.hashset = HashSet(self.collision_type, [z, initial_table_size])
        elif self.name == "Gates":
            self.collision_type = "Linear"
            z, initial_table_size = self.params
            self.hashset = HashSet(self.collision_type, [z, initial_table_size])
        elif self.name == "Bezos":
            self.collision_type = "Double"
            z1, z2, c2, initial_table_size = self.params
            self.hashset = HashSet(self.collision_type, [z1, z2, c2, initial_table_size])
            
        for word in text:
            self.hashset.insert(word)
        tuple = [book_title, self.hashset]
        self.hashmap.insert(tuple)

    def distinct_words(self, book_title):
        hashset = self.hashmap.find(book_title)
        if hashset is None:
            return []
        
        
        words = []
        if self.collision_type == "Chain":

            for chain in hashset.table:
                if chain is not None:
                    for j in chain:
                        words.append(j)
        else:
            
            for item in hashset.table:
                if item is not None:
                    words.append(item)
        
        return words

    def count_distinct_words(self, book_title):
        hashset = self.hashmap.find(book_title)
        if hashset is None:
            return 0
        
        count = 0
        if self.collision_type == "Chain":
            
            for chain in hashset.table:
                if chain is not None:
                    if isinstance(chain, list):
                        count += len(chain)
                    else:
                        count += 1
        else:
            
            for item in hashset.table:
                if item is not None:
                    count += 1
        return count

    def search_keyword(self, keyword):
        books_keywords = []
        if self.collision_type == "Chain":
            for slot in self.hashmap.table:
                if slot is not None:
                    for book_title, hashset in slot:
                        if hashset.find(keyword):
                            books_keywords.append(book_title)
        else:
            for item in self.hashmap.table:
                if item is not None:
                    book_title, hashset = item
                    if hashset.find(keyword):
                        books_keywords.append(book_title)
        
        return sorted(books_keywords)

    
    
   
    def print_books(self):
    
        if self.collision_type == "Chain":
            # For Chaining
            for lfa_slot in self.hashmap.table:
                if lfa_slot is None:
                    continue
                
                if isinstance(lfa_slot, list):  
                    
                    for item in lfa_slot:
                        if isinstance(item, list) and len(item) == 2:

                            lfa_book_title, lfa_book_hashset = item
                            lfa_words = []
                            
                            for lfa_word in lfa_book_hashset.table:

                                if lfa_word is None:
                                    lfa_words.append("<EMPTY>")
                                elif isinstance(lfa_word, list): 

                                    lfa_words.append(" ; ".join([w for w in lfa_word if w is not None]))
                                else:
                                    lfa_words.append(lfa_word)
                            print(f"{lfa_book_title}: {' | '.join(lfa_words)}")
                        

        elif self.collision_type == "Linear":
            # For Linear Probing
            for lfa_slot in self.hashmap.table:
                if lfa_slot is not None:
                    if isinstance(lfa_slot, list) and len(lfa_slot) == 2:

                        lfa_book_title, lfa_book_hashset = lfa_slot
                        lfa_words = []

                        for lfa_word in lfa_book_hashset.table:
                            if lfa_word is None:
                                lfa_words.append("<EMPTY>")

                            elif isinstance(lfa_word, list):
                                lfa_words.append(" ; ".join([w for w in lfa_word if w is not None]))
                            else:
                                lfa_words.append(lfa_word)


                        print(f"{lfa_book_title}: {' | '.join(lfa_words)}")
                    

        elif self.collision_type == "Double":
            # For Double Hashing
            for lfa_slot in self.hashmap.table:
                if lfa_slot is not None:
                    if isinstance(lfa_slot, list) and len(lfa_slot) == 2:

                        lfa_book_title, lfa_book_hashset = lfa_slot
                        lfa_words = []
                        for lfa_word in lfa_book_hashset.table:

                            if lfa_word is None:
                                lfa_words.append("<EMPTY>")

                            elif isinstance(lfa_word, list):
                                lfa_words.append(" ; ".join([w for w in lfa_word if w is not None]))


                            else:
                                lfa_words.append(lfa_word)
                        print(f"{lfa_book_title}: {' | '.join(lfa_words)}")
                    





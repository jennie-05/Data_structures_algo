from object import Object
from node import Node
from exceptions import NoBinFoundException
def comp(node, key, value):
    # Compare the key first
    if key < node.key:
        return -1  # Go to the left
    elif key > node.key:
        return 1  # Go to the right
    else:  # Keys are equal, compare the values
        if value < node.value:
            return -1  # Insert in the left subtree
        elif value > node.value:
            return 1  # Insert in the right subtree
        else:
            return 0  # The exact same key-value pair (no insertion needed)



class AVLTree:
    def __init__(self, compare_function=comp):
        self.root = None
        self.comp=comp
        self.comparator = compare_function
    def is_empty(self):
        return self.root is None
    def minValue(self,root):
        current = root
        while current is not None:
            if current.left is None:
                return current
            current = current.left
        return current
    def height(self,node):
        if not node:
            return 0
        return node.height
    def after(self,root, n):
        if n.right is not None:
            return self.minValue(n.right)

        succ = None
        while root is not None:
            if root.key < n.key:
                root = root.right
            elif root.key > n.key:
                succ = root
                root = root.left
            else:
                break

        return succ
    def find_ge(self,root, target):
        result = None
    
        while root is not None:
            if root.key == target:
                return root  # If we find an exact match, return the node immediately
            
            elif root.key > target:
                # Current node is a candidate, but there might be a closer one on the left
                result = root
                root = root.left
            
            else:
                # Current node is smaller, so we move to the right subtree
                root = root.right
    
    # Return the closest node greater than or equal to the target, or None if not found
        return result

    # def find_ge(self,root,k):
   
    #     if self.is_empty():
    #         return None
        
    #     else:
    #         p = self.find_position(root,k)  # may not find exact match
    #         if p is None :
    #             return None
    #         if p.key < k:  # p’s key is too small
    #             p = self.after(p)
    #     return p if p is not None else None
    # def inorder_successor(self, node, n):
    #     if n.right is not None: return self.minValue(n.right)
    #     succ = None
    #     while node:
    #         comp = n-node.key
    #         if comp < 0:
    #             succ = node
    #             node = node.left
    #         elif comp > 0: node = node.right
    #         else: break
    #     return succ    

    # def subtreesearch(self,p,k):
 
    #     if k==p.key():

    #         return p
    #     elif k<p.key(): 
    #         if self.left(p)is not None:
    #             return self.subtreesearch(self.p.left,k)
    #     else: 
    #         if self.right(p)is not None:
    #             return self.subtreesearch(self.p.right,k)
    #     return p
    
 
    # def subtreemaxposition(self,p):

    #     walk=p
    #     while self.right(walk)is not None: #keepwalkingright
    #         walk=self.right(walk)
    #     return walk
    
    
            
    def find_position(self, root, q):
    
        if root is None:
            return None
        if root.key is None:
            return None
    
    # If the current node's value matches the search value, return the node
        if q == root.key:
            return root
    
    # If the value is smaller, search the left subtree
        elif q < root.key:
            return self.find_position(root.left,q)
    
    # If the value is larger, search the right subtree
        else:
            return self.find_position(root.right,q)

    
    
        
    
    def getbalance(self,root):
        # print("getbalance")
        if root is None:
            return 0
        return self.height(root.left)-self.height(root.right)
    def leftrotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rightrotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    
    def find_parent(self, root, node):
        if root is None or root == node:
            return None
        if root.left == node or root.right == node:
            return root
        if node.key < root.key:
            return self.find_parent(root.left, node)
        else:
            return self.find_parent(root.right, node)
    # def insert_node(self,root,key,value): # key-cap, value-id
    #     if root is None:
    #         return Node(key,None)
    #     if root.duplicates is None:
    #             root.duplicates=AVLTree()
    #     if key==root.key :
    #         root.duplicates.root=root.duplicates.insert_node(root.duplicates.root,value,key)
    #         return root
    #     elif key < root.key:
    #         root.left = self.insert_node(root.left, key,value)
    #     elif key >root.key:
    #         root.right = self.insert_node(root.right, key,value)
    #     root.height = 1 + max(self.height(root.left), self.height(root.right))
    #     balance = self.getbalance(root)
    #     if balance > 1 and key < root.left.key:
    #         return self.rightrotate(root)
    #     if balance < -1 and key >root.right.key:
    #         return self.leftrotate(root)
    #     if balance > 1 and key >root.left.key:
    #         root.left = self.leftrotate(root.left)
    #         return self.rightrotate(root)
    #     if balance < -1 and key <root.right.key:
    #         root.right = self.rightrotate(root.right)
    #         return self.leftrotate(root)
    #     return root
    # def update_height(self,node):
    #     if not node: return 0
    #     else: return node.height
    # def return_height(self,node):
    #     if node: node.height= 1+max(self.update_height(node.left),self.update_height(node.right))
    # def return_height(self,node):
    #     if not node: return 0
    #     else: return node.height
    # def update_height(self,node):
    #     if node and node.left and node.right: node.height= 1+max(self.return_height(node.left),self.return_height(node.right))
    def insert(self, root,node_id=None,value,bin=None):
        if not root:
            return Node(value, node_id,bin)
        
        # Insert based on value, then by id if values are equal
        if value < root.value.capacity or (value == root.value.capacity and node_id < root.value.bin_id):
            root.left = self.insert(root.left, value, node_id,bin)
        else:
            root.right = self.insert(root.right, value, node_id,bin)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.getbalance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rightrotate(root)

        # Right rotation
        if balance < -1 and self.getbalance(root.right) <= 0:
            return self.leftrotate(root)

        # Left-Right rotation
        if balance > 1 and self.getbalance(root.left) < 0:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        # Right-Left rotation
        if balance < -1 and self.getbalance(root.right) > 0:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)


        return root
    def insert_node(self,root, key,value):
        # print("p")
    # Perform the normal BST insertion
        if root is None:
            
            # print(key,1)
            return Node(key,value)
        # print(root)
        comp1=self.comp(root,key,value)
        if comp1 < 0:  # Go left
            root.left = self.insert_node(root.left, key, value)
        elif comp1 > 0:  # Go right
            root.right = self.insert_node(root.right, key, value)
        # else:
        # # If comp returns 0, do nothing (we assume it's an exact duplicate)
        #     return root
        # print(key,3)
        # Update height of this ancestor node
        # print(root)
        root.height= 1+max(self.height(root.left),self.height(root.right))
        # Get the balance factor of this ancestor node
        balance = self.getbalance(root)

        # If this node becomes unbalanced, 
        # then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.key:
            
            return self.rightrotate(root)

        # Right Right Case
        if balance < -1 and key >root.right.key:
            
            return self.leftrotate(root)

        # Left Right Case
        if balance > 1 and key >root.left.key:
            
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        # Right Left Case
        if balance < -1 and key <root.right.key:
            
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)

        # Return the (unchanged) node pointer
        # e=root.key
        # print(e)
        # print(self.root.key)
        return root

    # def return_height(self,node):
    #     if node: node.height= 1+max(self.update_height(node.left),self.update_height(node.right))
    # def insert_node(self,node,key,value):
    #     if not node: return Node(key,value)
    #     comp =key-node.key
    #     if comp < 0: node.left = self.insert_node(node.left,key,value)
    #     else: node.right = self.insert_node(node.right,key,value)
    #     self.return_height(node)
    #     balance = self.getbalance(node)
    #     print(key)
    #     if balance > 1:
    #         if key-node.left.key < 0: return self.rightrotate(node)
    #         else:
    #             node.left = self.leftrotate(node.left)
    #             return self.rightrotate(node)
    #     if balance < -1:
    #         if key-node.right.key > 0: return self.leftrotate(node)
    #         else:
    #             node.right = self.rightrotate(node.right)
    #             return self.leftrotate(node)
    #     return node
    
    def getminvaluenode(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    def find_max(self,root):
        if self.is_empty():
            return None
        current = root
        
        #loop down to find the rightmost leaf
        while(current.right is not None and current is not None):
            current = current.right
        return current
    def delete(self, root, value, node_id=None):
        if not root:
            return root

        # Delete based on value, then by id if values are equal
        if value < root.value.capacity or (value == root.value and node_id < root.id):
            root.left = self.delete(root.left, value, node_id)
        elif value > root.value.capacity or (value == root.value and node_id > root.id):
            root.right = self.delete(root.right, value, node_id)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.id = temp.id
            root.bin=temp.bin
            root.right = self.delete(root.right, temp.value, temp.id)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.getbalance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rightrotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.leftrotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)

        # Right-Left rotation
        if balance < -1 and self.getbalance(root.right) > 0:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)

        return root
    def delete_object(self, root, value):
        if not root:
            return root

        # Delete based on value, then by id if values are equal
        if value < root.value :
            root.left = self.delete_object(root.left, value)
        elif value > root.value:
            root.right = self.delete_object(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.id = temp.id
            root.bin=temp.bin
            root.right = self.delete_object(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    # def delete(self, root, value, node_id=None):
    #     if not root:
    #         return root

    #     # Delete based on value, then by id if values are equal
    #     if value < root.value or (value == root.value and node_id < root.id):
    #         root.left = self.delete(root.left, value, node_id)
    #     elif value > root.value or (value == root.value and node_id > root.id):
    #         root.right = self.delete(root.right, value, node_id)
    #     else:
    #         if not root.left:
    #             temp = root.right
    #             root = None
    #             return temp
    #         elif not root.right:
    #             temp = root.left
    #             root = None
    #             return temp

    #         temp = self.min_value_node(root.right)
    #         root.value = temp.value
    #         root.id = temp.id
    #         root.bin=temp.bin
    #         root.right = self.delete(root.right, temp.value, temp.id)

    #     if not root:
    #         return root

    #     root.height = 1 + max(self.height(root.left), self.height(root.right))
    #     balance = self.balance(root)

    #     # Left rotation
    #     if balance > 1 and self.balance(root.left) >= 0:
    #         return self.right_rotate(root)

    #     # Right rotation
    #     if balance < -1 and self.balance(root.right) <= 0:
    #         return self.left_rotate(root)

    #     # Left-Right rotation
    #     if balance > 1 and self.balance(root.left) < 0:
    #         root.left = self.left_rotate(root.left)
    #         return self.right_rotate(root)

    #     # Right-Left rotation
    #     if balance < -1 and self.balance(root.right) > 0:
    #         root.right = self.right_rotate(root.right)
    #         return self.left_rotate(root)

    #     return root
    def delete_node(self,node,key,value):
        # print(key)
        if not node: return None
        
        comp=key-node.key
        if comp < 0: node.left = self.delete_node(node.left,key,value)
        elif comp > 0: node.right = self.delete_node(node.right,key,value)
        else:
            if not node.left or not node.right: return node.left if node.left else node.right
            successor = node.right
            while successor.left: successor = successor.left
            node.key = successor.key
            node.right = self.delete_node(node.right,successor.key,successor.value)
        node.height= 1+max(self.height(node.left),self.height(node.right))
        balance = self.getbalance(node)
        if balance > 1:
            if self.getbalance(node.left) < 0: node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        if balance < -1:
            if self.getbalance(node.right) > 0: node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
        return node

    # def delete_node(self,node2,key,value):
    #     if not node2: return None
    #     comp=key-node2.key
    #     if comp < 0: node2.left = self.delete_node(node2.left,key,value=None)
    #     elif comp > 0: node2.right = self.delete_node(node2.right,key,value=None)
    #     else:
    #         if not node2.left or not node2.right: return node2.left if node2.left else node2.right
    #         successor = node2.right
    #         while successor.left: successor = successor.left
    #         node2.key = successor.key
    #         node2.right = self.delete_node(successor.key,node2.right)
    #     self.return_height(node2)
    #     balance = self.getbalance(node2)
    #     if balance > 1:
    #         if self.getbalance(node2.left) < 0: node2.left = self.leftrotate(node2.left)
    #         return self.rightrotate(node2)
    #     if balance < -1:
    #         if self.getbalance(node2.right) > 0: node2.right = self.rightrotate(node2.right)
    #         return self.leftrotate(node2)
    #     return node2
    # def delete_node(self, root, key, value,size=0):
        # if not root:
        #     return None
        # # If the value matches, compare the id
        # elif key == root.key:
        #     #if root.id == id:
        #     # If there are duplicates, delete from duplicates tree first
        #     if root.duplicates is not None:
        #         root.duplicates.root = root.duplicates.delete_node(root.duplicates.root,value,key)
        #         temp=root.duplicates.root
        #         root.key=temp.value
        #         root.value=temp.key
        #         #print("value-",root.duplicates.root.value)
        #         if temp.left is None and temp.right is None:
        #             root.duplicates=None
        #         return root
            
        #     else:
        #         # No duplicates left, proceed with regular node deletion
        #         if not root.left:
        #             temp = root.right
        #             root = None
        #             return temp
        #         elif not root.right:
        #             temp = root.left
        #             root = None
        #             return temp

        #         temp = self.minValue(root.right)
        #         root.key = temp.key
        #         root.value = temp.value
        #         root.right = self.delete_node(root.right, temp.key, temp.value)
        # #         return root
        #     """else:
        #     # Delete from the duplicates tree if it's a duplicate node
        #         if root.duplicates:
        #             root.duplicates.root = root.duplicates.delete(root.duplicates.root, value, id)
        #         return root"""

    #     elif key < root.key:
    #         root.left = self.delete_node(root.left, key,value)
    #     else:
    #         root.right = self.delete_node(root.right, key,value)

    #     if not root:
    #         return root

    # # Update height of the current node
    #     root.height = 1 + max(self.height(root.left), self.height(root.right))

    # # Get the balance factor of this node to check if it became unbalanced
    #     balance = self.getbalance(root)

    # # If the node becomes unbalanced, then there are 4 cases:

    # # Left Left Case
    #     if balance > 1 and self.getbalance(root.left) >= 0:
    #         return self.rightrotate(root)

    # # Right Right Case
    #     if balance < -1 and self.getbalance(root.right) <= 0:
    #         return self.leftrotate(root)

    # # Left Right Case
    #     if balance > 1 and self.getbalance(root.left) < 0:
    #         root.left = self.leftrotate(root.left)
    #         return self.rightrotate(root)

    # # Right Left Case
    #     if balance < -1 and self.getbalance(root.right) > 0:
    #         root.right = self.rightrotate(root.right)
    #         return self.leftrotate(root)

    #     return root
    # def bluecargo(self,root,size):
    #     while root.left.key is not None:
    #         if root.left.key>=size:
    #             temp=root
    #             root=root.left
    #         if root.left.key<size or root.left is None:
    #             return temp


    # def yellowcargo(self,root, size):
    #     y=self.bluecargo(size)
    #     while 
        
    #      # If no duplicates, return the value of l itself

    # def redcargo(self,root,size):
    #     # print("redcargo")
    #     l = self.find_max(root)
    #     if l is None:
    #         raise NoBinFoundException
        
    #     if l.duplicates is not None and l.duplicates.root is not None:
    #         y = self.minValue(l.duplicates.root)
    #         return y
    #     return l  # If no duplicates, return the value of l itself

    # def greencargo(self,root, size):
    #     l = self.find_max(root)
    #     if l is None:
    #         raise NoBinFoundException
        
    #     if l.duplicates is not None and l.duplicates.root is not None:
    #         p = self.subtreemaxposition(l.duplicates.root)
    #         return p
    #     return l  # If no duplicates, return the value of l itself
    
    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)  # Store as tuple
            self.inorder_traversal(node.right, result) 
    def get_inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        # print(result)
        return result   
    # def compact_value(self, root, node, key):
    #     if root is None :
    #         return node  # Return the last valid node found (instead of None)
        
    #     if key == root.key:
    #         node=root
    #         #return self.get_compact_value(root, node, node.value)
    #         return node
        
    #     elif key < root.key:
    #         if node.left is not None:
    #              return self.get_compact_value_node(root.left, root, key)
    #         # Recursively search in the left subtree, update node reference
           
        
    #     else:
    #         # Recursively search in the right subtree, update node reference
    #         return self.get_compact_value_node(root.right,node,key)
    def inOrderSuccessor(self,root, n):
    
    # Step 1 of the above algorithm
        if n.right is not None:
            return self.minValue(n.right)

        # Step 2 of the above algorithm
        succ=None
        
        
        while( root):
            if(root.key<n.key):
                root=root.right
            elif(root.key>n.key):
                succ=root
                root=root.left
            else:
                break
        return succ
    def compact_fit_cap(self,node,size):
        if size==None:
            return None
        if node==None: 
            return None
        if node.key==size: 
            return node
        elif size < node.key:
            if node.left: return (self.compact_fit_cap(node.left,size))
            else: return node
        else: 
            if node.right: return (self.compact_fit_cap(node.right,size))
            else:
                temp_node=self.inOrderSuccessor(self.root,node)
                if temp_node:
                    return temp_node
                else:
                    return None
    def largest_fit_cap(self,node,size):
        if node==None: return None
        while node.right: node=node.right
        if node.key<size: return None
        else: return node
    # def largest_fit_cap(self,node,size):
    #     if node is None:
    #         return None
    #     if node.right==None:
    #         return node
    #     while node.right is not None: 
    #         node=node.right
    #     if node.key<size: 
    #         return None
        
    #     else: 
    #         return node

    def smallest_id(self,node,cap):
        a=None
        if node==None or cap==None: return a
        if node.key==cap:
            a=node
            temp_node=self.smallest_id(node.left,cap)
            if temp_node: a=temp_node
        elif node.key>cap:
            if node.left: a=self.smallest_id(node.left,cap)
        else: 
            if node.right: a=self.smallest_id(node.right,cap)
        # print(a.key)
        return a
    
    def largest_id(self,node,cap):
        a=None
        if not node: return a
        if node.key==cap:
            a=node
            temp_node=self.largest_id(node.right,cap)
            if temp_node: a=temp_node
        elif node.key>cap:
            if node.left: a=self.largest_id(node.left,cap)
        else: 
            if node.right: a=self.largest_id(node.right,cap)
        return a
    
    def bluecargo(self,node,size):
        if not node: return None
        chose=self.compact_fit_cap(node,size)
        # print(chose.value)
        a=self.smallest_id(node,chose.key)
        # print(a.value)
        return a
    
    def yellowcargo(self,node,size):
        if not node: return None
        chose=self.compact_fit_cap(node,size)
        a=self.largest_id(node,chose.key)
        return a
    
    def redcargo(self,node,size):
        if not node: return None
        chose=self.largest_fit_cap(node,size)
        # print(chose.key)
        a=self.smallest_id(node,chose.key)
        # print(a.key)
        
        return a
    
    def greencargo(self,node,size):
        if not node: return None
        chose=self.largest_fit_cap(node,size)
        a=self.largest_id(node,chose.key)
        return a
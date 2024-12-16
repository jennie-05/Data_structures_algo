from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node
class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bincapacity=AVLTree()
        self.objects=AVLTree()
        self.binidtree=AVLTree()
        
        pass 
   
    
    def add_bin(self, bin_id, capacity):
        bin=Bin(bin_id,capacity)
        self.bincapacity.root=self.bincapacity.insert_node(self.bincapacity.root,capacity,bin)

        self.binidtree.root=self.binidtree.insert_node(self.binidtree.root,bin_id,bin)
        # print(self.binidtree.root.key, self.bincapacity.root.key,2)
        # print()
        pass

    def add_object(self, object_id, size, color):
        object2=Object(object_id, size, color)
        if color==Color.BLUE:
            y=self.insertblue( object2)
              
        elif color==Color.YELLOW:
            self.insertyellow( object2)
               
        elif color==Color.RED:
            y=self.insertred(object2)      
            
        elif color==Color.GREEN:
            self.insertgreen( object2)
              
        elif self.bincapacity.find_max(size).capacity<size:
        
            raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        k=self.objects.find_position(self.objects.root,object_id)
        self.objects.root=self.objects.delete_node(self.objects.root,object_id,k.value)
        x=self.binidtree.find_position(self.binidtree.root,k.value)
        self.bincapacity.root=self.bincapacity.delete_node(self.bincapacity.root,x.value.capacity,x.value.bin_id)
        x.value.remove_object(object_id)
        self.bincapacity.root=self.bincapacity.insert_node(self.bincapacity.root,x.value.capacity,x.value.bin_id)
    
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        q=self.binidtree.find_position(self.binidtree.root,bin_id)
        if q is not None:
            if q.value is not None:
                l=q.value.bin_objects.get_inorder()
        return (q.value.capacity,l)
        

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        x=self.objects.find_position(self.objects.root,object_id)
        return x.value
    
    def insertred(self,obj):
            y=self.bincapacity.redcargo(self.bincapacity.root,obj.size)
            c= self.binidtree.find_position(self.binidtree.root,y.value) 
            obj.bin_id=c.key
            # if y.value==c.key: print(7)
            
            self.bincapacity.root=self.bincapacity.delete_node(self.bincapacity.root,c.value.capacity, c.key)
            c.value.add_object(obj)
            y.key=y.key-obj.size
            self.bincapacity.root=self.bincapacity.insert_node(self.bincapacity.root,y.key,c.key)
            # print(y.value,c.value.bin_objects.get_inorder(),c.value.bin_id,y.key,c.value.capacity)
            self.objects.root=self.objects.insert_node(self.objects.root,obj.object_id,y.value)
    def insertyellow(self,obj):
            y=self.bincapacity.yellowcargo(self.bincapacity.root,obj.size)
            
            c= self.binidtree.find_position(self.binidtree.root,y.value) 
            obj.bin_id=c.key
            # if y.value==c.key: print(7)
            
            self.bincapacity.root=self.bincapacity.delete_node(self.bincapacity.root,c.value.capacity,c.key)
            c.value.add_object(obj)
            y.key=y.key-obj.size
            self.bincapacity.root=self.bincapacity.insert_node(self.bincapacity.root,y.key,c.key)

            # print(y.value,c.value.bin_objects.get_inorder(),c.value.bin_id,y.key,c.value.capacity)
            self.objects.root=self.objects.insert_node(self.objects.root,obj.object_id,y.value)
    def insertblue(self,obj):
            y=self.bincapacity.bluecargo(self.bincapacity.root,obj.size)
            obj.bin_id=y.value.bin_id
            self.objects.root=self.objects.insert(self.objects.root,obj.object_id,obj.bin_id)
            temp1=y.key#ye bin capacity hai
            temp2=y.value#ye bin hai
            newobject=Object(obj.object_id,obj.size,obj.color)
            temp2.add_object(newobject)
            self.bincapacity.delete(self.bincapacity.root,y.key,y.value)
            newbinnode=Node(temp1-obj.size,temp2)
            self.bincapacity.insert(self.bincapacity.root,newbinnode.key,newbinnode.value)
            
            
    def insertgreen(self,obj):
            y=self.bincapacity.greencargo(self.bincapacity.root,obj.size)
            c= self.binidtree.find_position(self.binidtree.root,y.value) 
            obj.bin_id=c.key
            
            self.bincapacity.root=self.bincapacity.delete_node(self.bincapacity.root,c.value.capacity, c.key)
            c.value.add_object(obj)
            y.key=y.key-obj.size
            self.bincapacity.root=self.bincapacity.insert_node(self.bincapacity.root,y.key,y.value)

            # print(y.value,c.value.bin_objects.get_inorder(),c.value.bin_id,y.key,c.value.capacity)
            self.objects.root=self.objects.insert_node(self.objects.root,obj.object_id,y.value)
    
    
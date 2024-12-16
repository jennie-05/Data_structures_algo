from avl import AVLTree
from object import Object
from node import Node
from exceptions import NoBinFoundException 
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.bin_objects=AVLTree()
        pass

    def add_object(self, obj):
        # Implement logic to add an object to this bin
        
        if obj.size>self.capacity:
            raise NoBinFoundException
        else:
            self.bin_objects.root=self.bin_objects.insert_node(self.bin_objects.root,obj.object_id,obj.size)
            self.capacity=self.capacity-obj.size
    def remove_object(self,object_id):
        object1=self.bin_objects.find_position(self.bin_objects.root,object_id)
        self.bin_objects.root=self.bin_objects.delete_node(self.bin_objects.root,object_id,object1.value)
        # Implement logic to remove an object by ID
        self.capacity=self.capacity+object1.value
        pass

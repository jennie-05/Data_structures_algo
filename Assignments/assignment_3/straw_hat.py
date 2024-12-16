'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
#here x and y are the instances of crewmate class
def comp1(x, y):
    # If either crew member hasn't received any treasure yet
    if not x.crewtreasure:
        return True  # x should be considered as having less load
    if not y.crewtreasure:
        return False  # y should be considered as having less load
    
    current_time = max(x.latesttime, y.latesttime)
    
    load_x = max(x.latestload - (current_time - x.latesttime), 0)
    load_y = max(y.latestload - (current_time - y.latesttime), 0)
    
    return load_x < load_y
# def comp1(x,y):
#     realloadx=x.latestload-(-x.latesttime) if x.latestload>0 else 0
#     realloady=y.latestload-(-y.latesttime) if y.latestload>0 else 0
#     return realloadx<realloady
#here x and y are instances of treasure
def comp2(x,y):

    priorityx= x[1].size+x[1].arrival_time
    priorityy=y[1].size+y[1].arrival_time
    if priorityx!=priorityy:
        return priorityx<priorityy
    else:
        return x[1].id<y[1].id

    


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):

        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        self.crewmatearray=[]
        for i in range(m):
            crew=CrewMate()
            self.crewmatearray.append(crew)
       
        # Write your code here
        self.crewmatesheap=Heap(comp1,self.crewmatearray)
        self.crewmatesnumber=m
        self.activecrewmates=[]
        pass
    def add_treasure(self, treasure):
    # Getting the top of the heap
        topcrewmate = self.crewmatesheap.extract()
        
        # Error is in this line: len(topcrewmate.crewtreasure==0)
        # Should be: len(topcrewmate.crewtreasure) == 0
        if topcrewmate.latestload == 0 or (topcrewmate.latestload - (treasure.arrival_time - topcrewmate.latesttime))<=0:
            topcrewmate.latesttime = treasure.arrival_time
            topcrewmate.latestload = treasure.size
        else:
            # Calculate remaining load considering time passed
            topcrewmate.latestload+=treasure.size
            
        # Adding treasure into that top element

        topcrewmate.add_treasure(treasure)
        
        # Heapifying the crewmatesheap again
        self.crewmatesheap.insert(topcrewmate)
        if topcrewmate not in self.activecrewmates:
            self.activecrewmates.append(topcrewmate)
  
        
       
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        pass
    def get_completion_time(self):
        all_treasures = []
        if len(self.activecrewmates)<self.crewmatesnumber:
            for crew in self.activecrewmates:
                for treasure in crew.crewtreasure:
                    treasure_copy = Treasure(treasure.id, treasure.size, treasure.arrival_time)
                    # Set completion time as arrival time + size
                    treasure_copy.completion_time = treasure_copy.arrival_time + treasure_copy.size
                    all_treasures.append(treasure_copy)
            return sorted(all_treasures, key=lambda x: x.id)


        for j in range(len(self.crewmatesheap.init_array)):
            crew1 = self.crewmatesheap.init_array[j]
            crewmatestreasurecopy = []
            for k in self.crewmatesheap.init_array[j].crewtreasure:
                crewmatestreasurecopy.append(Treasure(k.id, k.size, k.arrival_time))
            crew_treasure_array = []
            crew_treasure_heap = Heap(comp2, crew_treasure_array)
            tprev = 0
            tnow = 0
            
            for i in range(len(crewmatestreasurecopy)):
                treasure1 = crewmatestreasurecopy[i]
                tupleadded = [treasure1.size + treasure1.arrival_time, treasure1]
                tnow = treasure1.arrival_time
                
                while not crew_treasure_heap.is_empty():
                    top_crew1 = crew_treasure_heap.top()
                    time_diff = tnow - tprev
                    if top_crew1[1].size <= time_diff:
                        completed = crew_treasure_heap.extract()
                        completed[1].completion_time = tprev + completed[1].size
                        all_treasures.append(completed[1])
                        tprev += completed[1].size
                    else:
                        top_crew1[1].size -= time_diff
                        break
                
                crew_treasure_heap.insert(tupleadded)
                tprev = treasure1.arrival_time
            
            while not crew_treasure_heap.is_empty():
                completed = crew_treasure_heap.extract()
                completed[1].completion_time = tprev + completed[1].size
                all_treasures.append(completed[1])
                tprev = completed[1].completion_time

        sorted_treasures = sorted(all_treasures, key=lambda x: x.id)
        return sorted_treasures
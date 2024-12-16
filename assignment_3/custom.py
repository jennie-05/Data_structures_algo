# You can add any additional function and class you want to implement in this file
'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
from treasure import Treasure
#here x and y are the instances of crewmate class
def comp1(x,y):
    realloadx=x.latestload-(-x.latesttime) if x.latestload>0 else 0
    realloady=y.latestload-(-y.latesttime) if y.latestload>0 else 0
    return realloadx<realloady
#here x and y are instances of treasure
def comp2(x,y):

    priorityx= x[1].size+x[1].arrival_time
    priorityy=y[1].size+x[1].arrival_time
    if priorityx!=priorityy:
        return priorityx<priorityy
    else:
        return x[1].id<y[1].id

    


class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def _init_(self, m):

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
        pass
    
    def add_treasure(self, treasure):
        #getting the top of the heap
        
        topcrewmate=self.crewmatesheap.top()
        #adding treasure into that top element
        topcrewmate.add_treasure(treasure)
        #changing the latestload
        topcrewmate.latestload+=treasure.size
        #changing the lastesttime to the arrival time of the latest load
        topcrewmate.latesttime=treasure.arrival_time
        #heapifying the crewmatesheap again 
        self.crewmatesheap.downheap(0)
       
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
        all_treasures=[]
        for j in range (len(self.crewmatesheap.init_array)):
            #crewmatesheap k jth element ko lena
            crew1=self.crewmatesheap.init_array[j]
            #crew k reasure ki empty array
            
        crewmatestreasurecopy = []
        for k in self.crewmatesheap.init_array[j].crewtreasure:
            crewmatestreasurecopy.append(Treasure(k.id, k.size, k.arrival_time))
            crew_treasure_array=[]
            # crewmate ka heap construction
            crew_treasure_heap=Heap(comp2,crew_treasure_array)
            tprev=0
            tnow=0
            #top wale crewmate ke pehle treasure ko access karna
            
            for i in range (len(crew1.crewmatestreasurecopy)-1):
               
                treasure1=crew1.crewmatestreasurecopy[i]
                # remaining size dynamically change nahi ho raha that is the problem
                tupleadded=[treasure1.size+treasure1.arrival_time,treasure1]
                #updating the tnow 
                tnow=treasure1.arrival_time
                #updating size of the top element
                
                if not crew_treasure_heap.is_empty(): 
                    top_crew1=crew_treasure_heap.top()
                    
                    top_crew1[1].size-=(tnow-tprev)
                    if top_crew1[1].size==0:
                        top_crew=crew_treasure_heap.top()
                        top_crew[1].completion_time=tnow
                        all_treasures.append(top_crew[1])
                        crew_treasure_heap.extract()
                    if top_crew1[1].size<0:
                        top_crew=crew_treasure_heap.top()
                        top_crew[1].completion_time=tprev+top_crew1[1].size+tnow-tprev
                        all_treasures.append(top_crew[1])
                        top2=crew_treasure_heap.top()
                        time1=top2[1].completion_time
                        tprev=time1
                        crew_treasure_heap.extract()

                #changing priority of the treasure
                    treasure1.priority=top_crew1[1].size+treasure1.arrival_time
                
                crew_treasure_heap.insert(tupleadded)
                #updating the tprev to the arrival time of the just added treasure
                tprev=treasure1.arrival_time
            for i in range (len( crew_treasure_heap.init_array)):
                completed = crew_treasure_heap.extract()
                completed[1].completion_time = tprev + completed[1].size
                all_treasures.append(completed[1])
                tprev = completed[1].completion_time


            sorted_treasures = sorted(all_treasures, key=lambda x: x.id)
    
    # Extract only the completion times from the sorted list
            
    
        return sorted_treasures
    # def get_completion_time(self):
    #     all_treasures = []
    #     for crew in self.crewmatesheap.init_array:
    #         current_time = 0
    #         crew_treasures = sorted(crew.crewtreasure, key=lambda t: t.arrival_time)
            
    #         for treasure in crew_treasures:
    #             current_time = max(current_time, treasure.arrival_time)
    #             wait_time = current_time - treasure.arrival_time
    #             priority = wait_time - treasure.size
                
    #             treasure_heap = Heap(comp2, [(priority, t) for t in crew_treasures if t.completion_time is None])
                
    #             while not treasure_heap.is_empty():
    #                 _, current_treasure = treasure_heap.extract()
    #                 current_treasure.completion_time = current_time + current_treasure.size
    #                 current_time = current_treasure.completion_time
    #                 all_treasures.append(current_treasure)
                    
    #                 # Update priorities for remaining treasures
    #                 for i in range(len(treasure_heap.init_array)):
    #                     _, t = treasure_heap.init_array[i]
    #                     new_priority = (current_time - t.arrival_time) - t.size
    #                     treasure_heap.init_array[i] = (new_priority, t)
    #                 treasure_heap.heapify()

    #     return sorted(all_treasures, key=lambda x: x.id)
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        pass
    
    # You can add more methods if required
    def get_completion_time(self):
        all_treasures = []
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
                tprev = tnow
            
            while not crew_treasure_heap.is_empty():
                completed = crew_treasure_heap.extract()
                completed[1].completion_time = tprev + completed[1].size
                all_treasures.append(completed[1])
                tprev = completed[1].completion_time

        sorted_treasures = sorted(all_treasures, key=lambda x: x.id)
        return sorted_treasures
    def get_completion_time(self):
        all_treasures = []
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
      # def add_treasure(self, treasure):
        

    #     #getting the top of the heap
        
    #     topcrewmate=self.crewmatesheap.top()
    #     if len(topcrewmate.crewtreasure==0):
    #         topcrewmate.latesttime = treasure.arrival_time
    #         topcrewmate.latestload = treasure.size
    #     #adding treasure into that top element
    #     else:
    #     # Calculate remaining load considering time passed
    #         topcrewmate.latestload = max(topcrewmate.latestload - (treasure.arrival_time - topcrewmate.latesttime),0) + treasure.size
    #         topcrewmate.latesttime = treasure.arrival_time
    #     topcrewmate.add_treasure(treasure)

    #     #changing the latestload
        
    #     #changing the lastesttime to the arrival time of the latest load
        
    #     #heapifying the crewmatesheap again 
    #     self.crewmatesheap.downheap(0)
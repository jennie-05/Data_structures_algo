from heap import Heap
from treasure import Treasure
'''
    Python file to implement the class CrewMate
'''

class CrewMate:

    '''
    Class to implement a crewmate
    '''
    def __init__(self,latestload=0,latesttime=0,t=0):
        self.crewtreasure=[]
        #this is the latest treasure jab tumne add kara hai uss samay kya load tha wo hai
        self.latestload=latestload
        #this is the var which was in the algo it is the arrival time of the last treasure which was added in the crewmate
        self.latesttime=latesttime
        #this is the time t which is the current time it is the time which is teh arrival time of the latest treasure whcih is added to the crewmates
        self.t=t
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
    def add_treasure(self,treasureadded):
        self.crewtreasure.append(treasureadded)  
       
        # Write your code here
        pass
    
    # Add more methods if required
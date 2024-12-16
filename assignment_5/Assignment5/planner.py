from flight import Flight

class Planner:
    def __init__(self, flights):
        self.flights = flights
        self.No_flight = len(flights)
        
        
        max_flight_no = self.find_max_flight_no(flights)
        self.flight_graph = self.Graph(max_flight_no + 1) 
        
      
        max_city =self.find_max_city(flights)
        flightsbystart = []  
        for i in range(max_city + 1):  
            flightsbystart.append([])  

        
     
        for flight in flights:
            flightsbystart[flight.start_city].append(flight)
            self.flight_graph.add_edge(flight.flight_no, flight)
        x=self.add_flight_connections(self.flight_graph, flights, flightsbystart)

    #adding flight connections i.e. adding teh flight edges 
    def add_flight_connections(self,flight_graph, flights, flights_by_start):
    
        for current_flight in flights:

            connecting_flights = flights_by_start[current_flight.end_city]
            
            for candidate_flight in connecting_flights:
                
                if current_flight.flight_no != candidate_flight.flight_no:
                    flight_graph.add_edge(current_flight.flight_no, candidate_flight)
#for finding the maximummmmmmmmmm flight numberrrrrrrrrrrr


    def find_max_flight_no(self,flights):
        max_no = -float('inf')  
        for flight in flights:
            if flight.flight_no > max_no:
                max_no = flight.flight_no
        return max_no
    #finddd maximummm cityyyyyyyyyy
    def find_max_city(self,flights):
        max_city = -float('inf')  

        for flight in flights:
            
            if max_city is None or flight.start_city > max_city:
                
                
                
                
                max_city = flight.start_city
            if flight.end_city > max_city:
                
                
                max_city = flight.end_city
        return max_city
    

    # def least_flights_earliest_route(self, start_city, end_city, t1, t2):
    #     if start_city==end_city:
    #         return []
    #     shortest_route = None
    #     earliest_arrival = float('inf')
    #     min_flights = float('inf')
       
        
       
    #     for flight in self.flights:
    #         if flight.start_city == start_city:
    #             if flight.departure_time>t1:
    #                 route = self.bfs_find_route(flight, end_city, t2)
    #                 if route:
    #                     route_length = len(route)
    #                     last_flight = route[route_length - 1]  # Access the last flight using route_length
    #                     last_flight_arrival = last_flight.arrival_time  # Arrival time of the final flight

                       
    #                     if (route_length < min_flights) or (route_length == min_flights and last_flight_arrival < earliest_arrival):
    #                         shortest_route = route
    #                         min_flights = route_length
    #                         earliest_arrival =last_flight_arrival
        
    #     if shortest_route is not None:
    #         return shortest_route
    #     else:
    #         return []
    def least_flights_ealiest_route(self, start_city, end_city, t1, t2):

        if start_city==end_city:
            return []
        

        shortest_route = None
        earliest_arrival = float('inf')
        
        min_flights = float('inf')

        #traversing through the entire flight ki list and then running bfs in each of the specific flight then update the the least flight wala route and then if same toh check least arrival time wala
        
        for flight in self.flights:
            if flight.start_city == start_city and flight.departure_time >= t1:
                route = self.find_bfs_route(flight, end_city, t2)

                if route:
                    route_length = len(route)

                    last_flight = route[route_length - 1] 

                    last_flight_arrival = last_flight.arrival_time 

                    
                    if (route_length < min_flights) or (route_length == min_flights and last_flight_arrival < earliest_arrival):


                        shortest_route = route


                        min_flights = route_length

                        earliest_arrival = last_flight_arrival
        
        if shortest_route is not None:

            return shortest_route
        else:

            return []

    # def bfs_find_route(self, start_flight, end_city, t2):
    #     queue = self.Queue()
        
    #     # Initialize visited array with size max_flight_no + 1
    #     max_flight_no = max(flight.flight_no for flight in self.flights)
    #     visited = [False] * (max_flight_no + 1)
        
    #     # Store (flight, path) tuples in the queue
    #     queue.enqueue((start_flight, [start_flight]))
    #     visited[start_flight.flight_no] = True

    #     while not queue.is_empty():
    #         current_flight, current_path = queue.dequeue()

    #         if current_flight.arrival_time > t2:
    #             continue  # Skip paths that exceed arrival window

    #         if current_flight.end_city == end_city:
    #             return current_path  # Found a valid path to end city

    #         # Check next flights that connect from current_flight
    #         for next_flight in self.flight_graph.get_adjacent(current_flight):
    #             if not visited[next_flight.flight_no] and current_flight.arrival_time + 20 <= next_flight.departure_time:
    #                 visited[next_flight.flight_no] = True
    #                 # Create new path by extending current path
    #                 new_path = current_path.copy()
    #                 new_path.append(next_flight)
    #                 queue.enqueue((next_flight, new_path))

    #     return []

    def find_bfs_route(self, start_flight, end_city, t2):
        flight_queue = self.Queue()
        
        flight_no_max = self.find_max_flight_no(self.flights)

        visited_flights = [False] * (flight_no_max + 1)
        
        flight_queue.enqueue([start_flight, [start_flight]])
        visited_flights[start_flight.flight_no] = True

        while not flight_queue.is_empty():
            current_flight, current_path = flight_queue.dequeue()

            if current_flight.arrival_time > t2:
                continue

            if current_flight.end_city == end_city:
                return current_path

            for next_flight in self.flight_graph.get_adjacent(current_flight):
                if not visited_flights[next_flight.flight_no]:

                    if current_flight.arrival_time + 20 <= next_flight.departure_time:

                        visited_flights[next_flight.flight_no] = True

                        extended_path = []

                        for item in current_path:

                            extended_path.append(item)

                        extended_path.append(next_flight)
                        flight_queue.enqueue([next_flight, extended_path])

        return []

    def cheapest_route(self, start_city, end_city, t1, t2):
        
        if start_city==end_city:
            return []
        


        max_flight_no =self.find_max_flight_no(self.flights)
        min_fare = [float('inf')] * (max_flight_no + 1)







        predecessor = [-1] * (max_flight_no + 1)
        heap_list=[]
        heap = self.Heap(self.comparator1, heap_list)
        
        
        for flight in self.flights:

            if flight.start_city == start_city:

                if flight.departure_time>=t1:

                    min_fare[flight.flight_no] = flight.fare

                    heap.insert((flight.flight_no, flight.fare))
        
        
        while not heap.is_empty():

            current_flight_no, current_fare = heap.extract()

            current_flight = None
            
            
            for flight in self.flights:


                if flight.flight_no == current_flight_no:



                    current_flight = flight
                    break
            
            if current_flight is None:
                continue
                
           
            if current_flight.end_city == end_city and current_flight.arrival_time <= t2:


                route = []
                flightnotemp = current_flight_no
                while flightnotemp != -1:
                    # Find the flight object corresponding to this number
                    for flight in self.flights:
                        if flight.flight_no == flightnotemp:
                            route.insert(0, flight)
                            break

                    flightnotemp = predecessor[flightnotemp]

                return route
            
            
            for next_flight in self.flight_graph.get_adjacent(current_flight):
               
                if current_flight.arrival_time + 20 <= next_flight.departure_time:
                    new_fare = current_fare + next_flight.fare
                    
                
                    if new_fare < min_fare[next_flight.flight_no]:
                        min_fare[next_flight.flight_no] = new_fare

                        predecessor[next_flight.flight_no] = current_flight_no

                        heap.insert((next_flight.flight_no, new_fare))

        
        return []  # No valid route found
    # def cheapest_route(self, start_city, end_city, t1, t2):
    #     if start_city==end_city:
    #         return []
    #     min_fare = [float('inf')] * self.No_flight
    #     predecessor = [-1] * self.No_flight
    #     queue = self.Heap(lambda x, y: x[1] < y[1], [])

    #     for flight in self.flights:
    #         if flight.start_city == start_city and flight.departure_time >= t1:
    #             min_fare[flight.flight_no] = flight.fare
    #             queue.insert((flight.flight_no, flight.fare))

    #     while not queue.is_empty():
    #         current_flight_no, current_fare = queue.extract()
    #         current_flight = self.flights[current_flight_no]

    #         if current_flight.end_city == end_city and current_flight.arrival_time <= t2:
    #             route = []
    #             while current_flight_no != -1:
    #                 route.insert(0, self.flights[current_flight_no])
    #                 current_flight_no = predecessor[current_flight_no]
    #             return route

    #         for next_flight in self.flight_graph.get_adjacent(current_flight):
    #             if current_flight.arrival_time + 20 <= next_flight.departure_time:
    #                 new_fare = current_fare + next_flight.fare

    #                 if new_fare < min_fare[next_flight.flight_no]:
    #                     min_fare[next_flight.flight_no] = new_fare
    #                     predecessor[next_flight.flight_no] = current_flight.flight_no
    #                     queue.insert((next_flight.flight_no, new_fare))

    #     return []
   


    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
    
        if start_city==end_city:
            return []
        
        max_flight_no = self.find_max_flight_no(self.flights)

        min_fare = [float('inf')] * (max_flight_no + 1) 

        min_flights = [float('inf')] * (max_flight_no + 1) 

        predecessor = [-1] * (max_flight_no + 1)

       
        heap1_list=[]
        heap1 = self.Heap(self.comparator2, heap1_list)
        
        
        for flight in self.flights:
            if flight.start_city == start_city and flight.departure_time >= t1:

                min_fare[flight.flight_no] = flight.fare

                min_flights[flight.flight_no] = 1

                heap1.insert((flight.flight_no, flight.fare, 1))  
        
       
        while not heap1.is_empty():

            flight_no, total_fare, total_flights = heap1.extract()

            current_flight = None
            
           
            for flight in self.flights:
                if flight.flight_no == flight_no:
                    current_flight = flight
                    break
            
            if current_flight is None:
                continue
                
           
            if current_flight.end_city == end_city and current_flight.arrival_time <= t2:
                route = []

                temp_flight_no = flight_no

                while temp_flight_no != -1:
                   
                    for flight in self.flights:
                        if flight.flight_no == temp_flight_no:

                            route.insert(0, flight)
                            break

                    temp_flight_no = predecessor[temp_flight_no]

                return route
            
            
            for next_flight in self.flight_graph.get_adjacent(current_flight):
              
                if current_flight.arrival_time + 20 <= next_flight.departure_time:
                    new_fare = total_fare + next_flight.fare
                    new_flights = total_flights + 1
                    
                    
                    if (new_flights < min_flights[next_flight.flight_no]) or (new_flights == min_flights[next_flight.flight_no] and new_fare < min_fare[next_flight.flight_no]):
                        min_fare[next_flight.flight_no] = new_fare



                        min_flights[next_flight.flight_no] = new_flights



                        predecessor[next_flight.flight_no] = flight_no


                        heap1.insert((next_flight.flight_no, new_fare, new_flights))
        
        return []  
    # def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
    #     if start_city==end_city:
    #         return []
    #     min_fare = [float('inf')] * self.No_flight
    #     min_flights = [float('inf')] * self.No_flight
    #     predecessor = [-1] * self.No_flight
    #     queue = self.Heap(lambda x, y: (x[2] < y[2]) or (x[2] == y[2] and x[1] < y[1]), [])

    #     for flight in self.flights:
    #         if flight.start_city == start_city and flight.departure_time >= t1:
    #             min_fare[flight.flight_no] = flight.fare
    #             min_flights[flight.flight_no] = 1
    #             queue.insert((flight.flight_no, flight.fare, 1))

    #     while not queue.is_empty():
    #         flight_no, total_fare, total_flights = queue.extract()
    #         current_flight = self.flights[flight_no]

    #         if current_flight.end_city == end_city and current_flight.arrival_time <= t2:
    #             route = []
    #             while flight_no != -1:
    #                 route.insert(0, self.flights[flight_no])
    #                 flight_no = predecessor[flight_no]
    #             return route

    #         for next_flight in self.flight_graph.get_adjacent(current_flight):
    #             if current_flight.arrival_time + 20 <= next_flight.departure_time:
    #                 new_fare = total_fare + next_flight.fare
    #                 new_flights = total_flights + 1

    #                 if (new_flights < min_flights[next_flight.flight_no]) or (new_flights == min_flights[next_flight.flight_no] and new_fare < min_fare[next_flight.flight_no]):
    #                     min_fare[next_flight.flight_no] = new_fare
    #                     min_flights[next_flight.flight_no] = new_flights
    #                     predecessor[next_flight.flight_no] = flight_no
    #                     queue.insert((next_flight.flight_no, new_fare, new_flights))

    #     return []    # Changed from None to []
    
    #yaha pe flight number bhi 1,2,3,4 hai toh flight number would teh index in which the flight has been stored.
    class Graph:
        def __init__(self, num_vertices):
            # Initialize an empty adjacency list with num_vertices empty lists
            self.adj_list = [[] for _ in range(num_vertices)]
        
        def add_edge(self, src, dest):
            self.adj_list[src].append(dest)
            
        def remove_edge(self, src, dest):
            if dest in self.adj_list[src]:
                self.adj_list[src].remove(dest)
            
        
        def get_adj_list(self):
            
            return self.adj_list
        def get_adjacent(self, flight):
    
            if 0 <= flight.flight_no < len(self.adj_list):
                return self.adj_list[flight.flight_no]
            return []
            


    class Queue:
        def __init__(self):
            self.queue = []

        def is_empty(self):
            return len(self.queue) == 0

        def enqueue(self, item):
            self.queue.append(item)

        def dequeue(self):
            if self.is_empty():
                raise IndexError("Dequeue from an empty queue")
            return self.queue.pop(0)

        def peek(self):
            if self.is_empty():
                raise IndexError("Dequeue from an empty queue")
            return self.queue[0]

        def size(self):
            return len(self.queue)

    def comparator1(self,x, y):
        return x[1] < y[1]
    def comparator2(self,x, y):
        if x[2] < y[2]:
            return True
        elif x[2] == y[2] and x[1] < y[1]:
            return True
        return False

    class Heap:
   
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
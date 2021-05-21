# Defines agent class to encapsulate agents' properties and behavour.     

import random 

class Agent:


    def __init__ (self, agents, y, x, environment, store):
        """
        Defines object method using the contructor __init__

        Parameters
        ----------
        agents : List
            A reference to a list of all the agents.
        y : List
            y coordinate.
        x : List
            x coordinate.
        environment : List of lists
            Raster data (read in as x, y, z from text file).
        store : Integer
            Agents' store.

        Returns
        -------
        None.
        """
        self.agents = agents 
        self._y = y
        self._x = x
        self.environment = environment 
        self.store = store
        
        
    def getx(self):
        '''
        Function for getting the attribute value.

        Returns
        -------
        x   List
            get function for x coordinate.

        '''
        return self._x 
    
    def setx(self, x):
        '''
        Function for setting the attribute value.
        ----------
        x : List
            set function for x coordinate.

        Returns
        -------
        None.

        '''
        self._x = x
    
    def delx(self):
        '''
        Function for deleting the attribute value (x).

        Returns
        -------
        None.

        '''

        del self._x
    x = property(getx, setx, delx)
    
    
    def gety(self):
        '''
        Function for getting the attribute value.

        Returns
        -------
        TYPE
            delete function for x coordinate..

        '''
        return self._y
    
    def sety(self, y):
        '''
        Function for setting the attribute value.

        Parameters
        ----------
        y : List
            set function for y coordinate..

        Returns
        -------
        None.

        '''
        self._y = y
        
    def dely(self):
        '''
        Function for delting the attribute value.

        Returns
        -------
        None.

        '''

        del self._y
    y = property(gety, sety, dely)
    
    
    
    def __str__(self):
        '''
        Converts Python objects to strings (helpful to print output and check functions).

        Returns
        -------
        String
            Information about location and agent store.

        '''
        return "x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)
    

    def move(self):
        """
        Moves agents within existing environment, using torus to keep 
        agents within 0-99 square.
        """
        print("Before move", self) # Print out to test.
        if (random.random() < 0.5):
            self._y = (self._y + 1) % 300
        # Changed to modulus 300 to account for environment
        else:
            self._y = (self._y - 1) % 300
        if (random.random() < 0.5):
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
        print("After move", self) # Print out to test.
        
    
    def eat(self): 
        '''
        Eat function which allows agents to nibble environment.
        Adjusts self-store accordingly.

        Returns
        -------
        None.

        '''
        print("Before eat", self) # Print out to test.
        
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            print("After eat", self) # Print out to test.
        else:      
           self.environment[self._y][self._x] -= self.environment[self._y][self._x]
           self.store += self.environment[self._y][self._x]   
        print("After eat", self) # Print out to test.
        
        
            
    def share_with_neighbours(self, neighbourhood):
        '''
        Allows agents to share environment with neighbours.
        ----------
        neighbourhood : Integer
            Distance value detailing agents' local environment.

        Returns
        -------
        None.
        
        '''
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))
                
       
    def distance_between(self, agent):
        
        '''
        Calculates distance between agents.
        ----------
        agent : List
            List of agents.

        Returns
        -------
        Integer
            Straight line distance between agents.

        '''

        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


            
  
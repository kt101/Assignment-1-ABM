# Defines agent class to encapsulate agents' properties and behavour.     

import random 

class Agent:


    def __init__ (self, agents, y, x, environment, store): #Would need to set to x, y=None as default.
        """
        Defines object method using the contructor __init__

        Parameters
        ----------
        agents : List
            A reference to a list of all the agents.
        y : TYPE
            y coordinate of agent.
        x : TYPE
            x coordinate of agent.
        environment : List of lists
            The bounded location that the agents operate in.
        store : TYPE
            Amount stored by each agent.

        Returns
        -------
        None.
        """
        
        self.agents = agents # Agent ID
        self._y = y
        self._x = x
        self.environment = environment 
        self.store = store
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (x == None):
            self._y = random.randint(0,100)
        else:
            self._y = x
        
        
        
        
    """
    Using property() method to ensure data encapsulation.
    Getting the values

    """

    def getx(self):
        return self._x 
    def setx(self, x):
        self._x = x
    
    def delx(self):
        del self._x
    x = property(getx, setx, delx)
    
    
    def gety(self):
        return self._y
    
    def sety(self, y):
        self._y = y
        
    def dely(self):
        del self._y
    y = property(gety, sety, dely)
    
    def __str__(self):
        '''
        Converts numbers to string variable which are printed to test model.

        Returns
        -------
        TYPE
            Concatenates x, y coordinates and agents' store in a string list.

        '''
        return "x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)

    def move(self):
        """
        Moves agents within existing environment, using torus to keep 
        agents within 0-99 square.
        """
       # print("Before move", self) # Print out to test.
        if (random.random() < 0.5):
            self._y = (self._y + 1) % 299
        # Changed to modulus 300 to account for environment
        else:
            self._y = (self._y - 1) % 299
        if (random.random() < 0.5):
            self._x = (self._x + 1) % 299
        else:
            self._x = (self._x - 1) % 299
       #print("After move", self) # Print out to test.
        
    
    def eat(self): 
        """
        Allows agents to nibble environment.
        Adjusts self-store accordingly.
        """
      #  print("Before eat", self) # Print out to test.
        
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.environment[self._y][self._x] -= self.environment[self._y][self._x]
            self.store += self.environment[self._y][self._x]
       #     print("After eat", self) # Print out to test.
            
    def share_with_neighbours(self, neighbourhood):
        """
        Allows agents to share environment with neighbours.
        """
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
                
       
    def distance_between(self, agent):
        """
        Calculates distance between agents.
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


            
  
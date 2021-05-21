# Uses Python inheritance to define a class that inherits all the methods and 
#properties from another class.

# Parent class = Agent
# Child classes = Wolves and sheep

import random 

class Agent:
    
    def __init__ (self, y, x):
        
        '''
        Defines object method using the contructor __init__
        ----------
        y : List
            y coordinate.
        x : List
            x coordinate.

        Returns
        -------
        None.

        '''
        self._y = y
        self._x = x
        
        
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
    
     
    
    def move(self, distance):
        '''
        Moves agents within existing environment, using torus to keep 
        agents within 300 square.

        Returns
        -------
        None.

        '''
        print("Before move", self) # Print out to test.
        if (random.random() < 0.5):
            self._y = (self._y + distance) % 300
        # Changed to modulus 299 to account for environment
        else:
            self._y = (self._y - distance) % 300
        if (random.random() < 0.5):
            self._x = (self._x + distance) % 300
        else:
            self._x = (self._x - distance) % 300
        print("After move", self) # Print out to test.


class Sheep(Agent):


    def __init__ (self, i, sheep, y, x, environment, store):
        """
        Defines object method using the contructor __init__

        Parameters
        ----------
        sheep : List
            A reference to a list of all the sheep.
        y : TYPE
            y coordinate of Sheep.
        x : TYPE
            x coordinate of Sheep.
        environment : List of lists
            The bounded location that the sheep operate in.
        store : TYPE
            Amount stored by each Sheep.

        Returns
        -------
        None.
        """
        Agent.__init__(self, y, x)
        self.i = i
        self.sheep = sheep # Sheep ID
        self.environment = environment 
        self.store = store
    
    # Removed getx, setx, delx as duplicated following inheritance.  
        
        
        
    def __str__(self):
        '''
        Converts numbers to string variable which are printed to test model.

        Returns
        -------
        TYPE
            Concatenates x, y coordinates and store and prints out to check code.

        '''
        return "SHEEP" + str(self.i) + ": x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)
    
    # Removed move as duplicated following inheritance. 

    
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

# Sheep don't share, so 'share_with_neighbour removed.



# Defines Wolves class to encapsulate wolves' properties and behavour.     

class Wolves(Agent):


    def __init__ (self, wolves, sheep, y, x, store):
        """
        Defines object method using the contructor __init__

        Parameters
        ----------
        sheep : List
            A reference to a list of all the wolves.
        y : Interger
            y coordinate of Wolvess.
        x : Interger
            x coordinate of Wolves.
        store : TYPE
            Amount stored by each Wolves.

        Returns
        -------
        None.
        """
        Agent.__init__(self, y, x)
        self.wolves = wolves #Wolves ID
        self.sheep = sheep # Sheep ID included to link wolves and sheep
        #self._y = y
        #self._x = x
        self.store = store
        
        
    # Removed getx, setx, delx as duplicated following inheritance.    
        
    
    def __str__(self):
        '''
        Converts numbers to string variable which are printed to test model.

        Returns
        -------
        String
            Concatenates x, y coordinates and store for wolves and prints out to check code.

        '''
        return "WOLF: x=" + str(self._x) + ", y=" + str(self._y) + ", store=" + str(self.store)

    # def move(self) removed for wolves as was duplicated following inheritance.
    

    def eat_sheep(self, sheep, wolfneighbourhood):
        '''
        Calculates (and then) eats sheep within wolf neighbourhood
        ----------
        sheep : List
            List of sheep.
        wolfneighbourhood : Integer
            
        Returns
        -------
        None.

        '''
        """
        
        """
        print("Before eat sheep", self, "wolfneighbourhood=" + str(wolfneighbourhood)) # Print out to test.
        
        sheep_eaten = []
        print("Number of Sheep", len(self.sheep))
        for sheep in self.sheep:
            print("Does sheep", sheep, "get eaten?")
            dist = self.distance_between_species(sheep)
            if dist <= wolfneighbourhood: #If True, will remove sheep 
                index = self.sheep.index(sheep) 
                # Index used to print i of sheep in wolf neighbourhood.
                # Help gratefully received from A. Tunrner.
                sheep_eaten.append(index) # Appends element to the end of a list.
                self.store += 200 # Adds wolf store by 200
                print("Eating sheep", sheep)
                print("After eat sheep", self) # Print out to test.
        print("number of sheep eaten", len(sheep_eaten))   
        print(sheep_eaten)
        sheep_eaten.reverse() # Reverse sheep eaten list as we remove from the start.
        print(sheep_eaten)
        print("number of sheep", len(self.sheep))
        for i in sheep_eaten:
            self.sheep.pop(i) # Remove (the now reveresed) first element in list.
        print("number of sheep after eat", len(self.sheep)) # Print all reaining sheep
        for i in self.sheep:
            print(i)
            
            
    def distance_between_species(self, sheep):
        '''
        Calculates distance between sheep and wolves.
        ----------
        agent : List
            List of wolves.

        Returns
        -------
        Integer
            Straight line distance between sheep and wolves.

        '''
        return (((self.x - sheep.x)**2) + ((self.y - sheep.y)**2))**0.5

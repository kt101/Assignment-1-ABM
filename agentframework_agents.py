# Defines agent class to encapsulate agents' properties and behavour.     

import random

class Agent:
    
    def __init__ (self, y, x):
        '''
        Defines object method using the contructor __init__

        Parameters
        ----------
        y : Integer
            y coordinate.
        x : Integer
            x coordinate.

        Returns
        -------
        None.

        '''
        self.y = 0 #random.randint(0,99)
        self.x = 0 #random.randint(0,99)
        
        
        
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
            delete function for y coordinate..

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
   

 
        
        
    def move(self):
        
        """
        Moves agents within existing environment, using torus to keep 
        agents within 0-99 square.
        """
        if (random.random() < 0.5):
            self._y = (self._y + 1) % 100
        # Changed to modulus 300 to account for environment
        else:
            self._y = (self._y - 1) % 100
        if (random.random() < 0.5):
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
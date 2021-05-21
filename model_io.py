print("Start")

# Should remove all variables - this ensures environment has no legacy variables.
from IPython import get_ipython
get_ipython().magic('reset -sf')

# Import modules
import csv
import operator
import matplotlib.pyplot
from datetime import datetime
import os
import agentframework_io as af #Uniquely labelled for Input Output practical. 
import random

# Sets function to calculate Pythagoras to calculate distance between agents.

def distance_between(a, b):
    '''
    Calculates distance between two agents.

    Parameters
    ----------
    a : Integer
        First agent
    b : TYPE
        Second agent.

    Returns
    -------
    Integer
        Straight line distance between two points (using Pythagoras).

    '''
    return (((a.x - b.x)**2) +    ((a.y - b.y)**2))**0.5


# =============================================================================
# 
# User input allowed here to change No. of agents and No. of interations. 
# 
# =============================================================================
num_of_agents = 10
num_of_iterations = 2

# Set the random seed for reproducibility (for testing purposes)
# Used to initialise the random number generator. Using the same random number ensures you will get the same random number each time.
random.seed(0)

# Load the environment
# Import csv
# Good practise to check what txt file looks like in Notepad or Excel to ensure data is as expected.
f = open("in.txt", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


##########################
# Set environment
##########################

environment = []
for row in reader: 
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
f.close() # Alwayys ensure text file is closed after use

# Always importanht to test load - only required on initial load of data (or else new data files).

# Used as a quick check to ensure data is importing correcting.
#matplotlib.pyplot.show()
#matplotlib.pyplot.imshow(environment) 

# To confirm our environment is a square, a simple test will be run to check the rows equal the length of the environment.
nrows = len(environment)
print("nrows", nrows) # Answer 300
for i in range(nrows): # Tests whether cols == rows
    ncols = len(environment)
    if (ncols != 300):
        print("Not square - re-check source file") # Test to see if all rows have the same number of columns
print("ncols", ncols)

# Returns nrows 300, ncols 300 so square and can proceed.


##########################
# Creates agents i.e. adds values to y and x
# Checks distance function 
##########################

agents = [] # Create empty list which will be populated.

# Make the agents.
# Uses for loop to create agents using 6 input parameters
# 1. Agents variable, (2) and (3) random integer between 0 and 299 (length of environment-1), (4) environment and (5) store set to random integer between 0 and 10.

for i in range(num_of_agents):
    # Sets up initial agents with 
    agents.append(af.Agent(agents, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          environment,
                                          random.randint(0,10)))
    

# Prints all the agents to ensure setting up agents worked.
for i in range(len(agents)): 
    print(agents[i])
 # Correctly uses __str__ set up in agentframework - prints all agents locations and stores.  Looks as expected.   


# Test to ensure distance function works (creates two extra agents as positions 11 and 12)
# By setting x and y values to (0,0) and (3, 4) we know the distance answer should equal 5.

agents.append(af.Agent(agents, 
                                          0,
                                          0, 
                                          environment,
                                          random.randint(0,10)))
agents.append(af.Agent(agents, 
                                          3,
                                          4, 
                                          environment,
                                          random.randint(0,10)))

print(distance_between(agents[10], agents[11]))
# Printed answer is 5, so distance code works.

#Checks new num_of_agents
num_of_agents = len(agents) # Checks new number of agents using length. 
print(num_of_agents) # Check as expected (10 + 2 = 12)



##########################
# Plots agents
##########################


matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents): 
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show() # Check scatterplot to ensure all agents are displayed.

##########################
# Sums stores to check 'eat' function working.
##########################


def sum_stores():
    """
    Adds up the store in all the agents

    Returns
    -------
    total_store : Number
        Total store in all the agents.

    """
    # Sum up all the stores
    total_store = 0
    for i in range(num_of_agents):
        #print("agent store", agents[i].store)
        total_store = total_store + agents[i].store
    #print("total_store", total_store)
    return total_store

print("total_store", sum_stores()) # Check as expected.

type(sum_stores())

##########################
# Stimulate agents behaviour (move, eat)
##########################


# Set agents to move and eat (as detailed in Agentframework).
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
# Check move function works
# Compare before and after move. Ensure x and y move by +/- 1 each time. Correct
# Compare before and after eat. Ensure stores change by +/- 10 each time. Correct

# Check extra eat function
# Spatially restricted environment considerably to ensure agents had to eat small environment.
# x, y set to between 0 and 3.
# Increased agents and iterations and monitored print out.
# Before and after store print function remained same so agents have have eaten environment.
# Sucessful test.

#for i in range(20):
    # Sets up initial agents with 
    #agents.append(af.Agent(agents, 
                                          #random.randint(0,3),
                                          #random.randint(0,3), 
                                          #environment,
                                          #random.randint(0,10)))
    
#for j in range(1000):
    #for i in range(num_of_agents):
        #agents[i].move()
        #agents[i].eat()

       
  
# Sum up all the stores to monitor how much agents are storing.
total_store = 0
for i in range(num_of_agents):
    print("agent store", agents[i].store)
    total_store = total_store + agents[i].store
print("total_store", total_store)


"""
Extra practice

Using the lecture notes, can you write out the environment as a file at the 
end?
"""

#Export csv
f2 = open("dataout.txt", 'w', newline='')
writer = csv.writer(f2, delimiter=' ')

for row in environment: 
    writer.writerow(row)
        
f2.close() #Close text file after use

# This was tested by checking the directory in which my model_IO.py was saved.
# Directory had data file labelled 'dataout.txt' so test successful.

"""
Can you make a second file that writes out the total amount stored by all the 
agents on a line? Can you get the model to append the data to the file, 
rather than clearing it each time it runs?



Can you override __str__(self) in the agents, as mentioned in the lecture on 
classes, so that they display this information about their 
location and stores when printed?

# Complete. See agentframework


Can you get the agents to wander around the full environment by finding out 
the size of environment inside the agents, and using the size when you 
randomize their starting locations and deal with the boundary conditions?

Have used length of the environment when creating the agents (in model). 
Would need to work out length of enviornment in agentframework but I'm unsure 
how to implement this.


At the moment, the agents only eat 10 units at a time. This will leave a few 
#units in each area, even if intensly grazed. Can you get them to eat the last 
few bits, if there's less than 10 left, without leaving negative values?


# Complete. See agentframework


Can you get the agents to sick up their store in a location if they've been 
greedy guts and eaten more than 100 units? (note that when you add or 
subtract from the map, the colours will re-scale).

Not working: Tested and failed so have rejected.   

def sick(self): 
#Allows agents to be sick if eaten > 100 units.
#Adjusts self-store accordingly.
    print("Before sick", self) # Print out to test.
          if self.store > 100:
             self.environment[self._y][self._x] += self.store
             self.store == 0
             print("After sick", self) # Print out to test.
         print("Not sick", self) # Print out to test.

"""
print("Finish")
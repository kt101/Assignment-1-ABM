print("Start")

# Should remove all variables - this ensures environment has no legacy variables.
from IPython import get_ipython
get_ipython().magic('reset -sf')

# Import modules
import random
import operator
import matplotlib.pyplot
import agentframework_agents as af #Uniquely labelled for Agents! practical. 

#a = af.Agent() # Old code (used to check files are connected. True.

#Sets function to calculate Pythagoras to calculate distance between agents.
def distance_between(agents_row_a, agents_row_b):
    '''
    Calculates distance between two agents.

    Parameters
    ----------
    agents_row_a : Integer
        First agent.
    agents_row_b : Integer
        Second agent.

    Returns
    -------
    Integer
        Straight line distance between two points (using Pythagoras).

    '''
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# =============================================================================
# 
# User input allowed here to change No. of agents and No. of interations. 
# 
# =============================================================================
num_of_agents = 10
num_of_iterations = 100

##########################
# Creates agents i.e. adds values to a and b
##########################

agents = [] # Create empty list which will be populated.

# Make the agents.
# Uses for loop to create agents using 2 input parameters: (1) and (2) 
#representing x and y coordinates of agents.

for i in range(num_of_agents):
    agents.append(af.Agent(random.randint(0,99), random.randint(0,99)))
# Sets up random.randint(0, 99) here - could change in agentframework.py
#Check agents are printing out correctly
for i in range(num_of_agents):
        print(agents[i].x, agents[i].y)
# Yes, 10 agents within 0-99 for x and y

# Move the agents (as detailed in Agentframework).
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
# Uses matplotlib module to graph agents in environment.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()
# Plot displays correctly.


##########################
# Uses distance function to calculate distance.
##########################

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
print(distance)
# Prints answer (fine) 


print("Finish")
                

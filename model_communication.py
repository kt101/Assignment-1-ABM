print("Start")

#Should remove all variables
from IPython import get_ipython
get_ipython().magic('reset -sf')

import csv
import operator
import matplotlib.pyplot
from datetime import datetime
import os
import agentframework_communication #Labelled for Communication practical. 
import random
import time
import sys

# Distance function that was previously here, now been moved to agentframework.


# =============================================================================
# 
# User input allowed here to change No. of agents and No. of interations. 
# 
# =============================================================================
num_of_agents = 5
num_of_iterations = 10
neighbourhood = 20
width = 50

# Set the random seed for reproducibility (for testing purposes)
# Used to initialise the random number generator. Using the same random number ensures you will get the same random number each time.
random.seed(0)

##########################
# Set environment
##########################

# Load the environment
# Import csv
f = open("in.txt", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#Set environment
environment = []
for row in reader: 
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
f.close() #Close text file after use

# Always important to test load - only required on initial load of data (or else new data files).
# Used as a quick check to ensure data is importing correcting.
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(environment) 

# Test load - only required on initial load of data.
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

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
##########################

agents = [] # Create empty list which will be populated.

# Make the agents.
for i in range(num_of_agents):
    # Sets up initial agents with 
    agents.append(agentframework_communication.Agent(agents, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          environment,
                                          random.randint(0,10)))
    
    
# Prints all the agents to ensure setting up agents worked.
for i in range(len(agents)): 
    print(agents[i])
 # Correctly uses __str__ set up in agentframework - prints all agents locations and stores.  Looks as expected.      
    
    


    
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
    '''
    Adds up the store in all the agents

    Returns
    -------
    total_store : Number
        Total store in all the agents.

    '''

    # Sum up all the stores
    total_store = 0
    for i in range(num_of_agents):
        #print("agent store", agents[i].store)
        total_store = total_store + agents[i].store
    #print("total_store", total_store)
    return total_store

print("total_store", sum_stores()) # Check as expected.


##########################
# Stimulate agents behaviour (move, eat, share with neighbours)
##########################


# Set agents to move and eat (as detailed in Agentframework).
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        random.shuffle(agents) # Shuffles the sequence agent in place
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

print("total_store", sum_stores())

# Sum up all the stores to monitor how much agents are storing.

total_store = 0
for i in range(num_of_agents):
     print("agent store", agents[i].store)
     total_store = total_store + agents[i].store
print("total_store", total_store)


# Test to check sharing with neighbours is working correctly


#Test to ensure share with neighbours functions works (using new width variable)
# Three new agents created, two close together, two further away.

agents.append(agentframework_communication.Agent(agents, 
                                          random.randint(0, 25),
                                          random.randint(0, 25), 
                                          environment,
                                          random.randint(0,10)))

agents.append(agentframework_communication.Agent(agents, 
                                          random.randint(0, 25),
                                          random.randint(0, 25), 
                                          environment,
                                          random.randint(0,10)))

agents.append(agentframework_communication.Agent(agents, 
                                          random.randint(60, 70),
                                          random.randint(60, 70), 
                                          environment,
                                          random.randint(0,10)))




# Print all the agents
for i in range(len(agents)): 
    print(agents[i]) 
# Agents 1 and 2 close together (so can share), agent 3 further away.

# Set agents to share environment with neighbourhood.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].share_with_neighbours(neighbourhood)

#Retest share agent
# Set agents to share environment with neighbourhood.
for j in range(1):
    for i in range(3):
        agents[i].share_with_neighbours(neighbourhood)
'''
When set to iterations of 1:
    pre-share values were:
        x=24, y=12, store=6
        x=8, y=1, store=8
        x=66, y=67, store=4
        
    post-share values were:
        x=24, y=12, store=7.0
        x=8, y=1, store=7.0
        x=66, y=67, store=4.0
As 6 + 8 = 14, average is 7, which is correct, so code passed test!
"""
# Testing time taken for iterations 
# Changed No. of iterations to check code is working.
# Ensure code is commented out to run 'user-defined inputs' at the top of script.

#num_of_agents = 5
#num_of_iterations = 100000
#neighbourhood = 20
#width = 50

# Used time.time to investigate differences in time taken to run with different iteratons.
#start = time.time()

'''

#for j in range(num_of_iterations):
    #for i in range(num_of_agents):
        #agents[i].move()
        #agents[i].eat()
        #agents[i].share_with_neighbours(neighbourhood)
        
#end = time.time()

#timing = ("time = " + str(end - start)) 
#print(timing) #time = 0.005965709686279297 # 5 agents, 10 iterations
#print(timing) #time = 0.1406235694885254 # 5 agents, 100 iterations
#print(timing) #time = 1.9024484157562256 # 5 agents, 1000 iterations
#print(timing) #time = 175.21657872200012 # 5 agents, 100000 iterations

#Checks new num_of_agents
num_of_agents = len(agents)
print(num_of_agents) # Note if 5, need to comment out testing code above and rerun.


# Test agents to see whether else statement working correctly
environmenttest = environment
rowlist[:] = [number - 200 for number in rowlist]



print("Finish")

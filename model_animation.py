# Remove all previously saved variables
from IPython import get_ipython
get_ipython().magic('reset -sf')

# =============================================================================
# Note to Syper users re. plot pop up

#If pop up not displaying (i.e. only plots in pane), then:
# Start by opening the Spyder preferences. 
# In the Preferences window, click on IPython console on the left side of the window, then on the Graphics tab.
# Under Graphics backend, select Automatic for the backend.
# Restart Spyder.

# =============================================================================


import csv
import operator
import matplotlib.pyplot
import matplotlib.animation 
from datetime import datetime
import os
import agentframework_animation #Labelled for Communication practical. 
import random
import time
import sys


# =============================================================================
# 
# User input allowed here to change No. of agents and No. of interations. 
# 
# =============================================================================

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Set the random seed for reproducibility (for testing purposes)
# Used to initialise the random number generator. Using the same random number ensures you will get the same random number each time.
random.seed(0)

# Set up figure for animating agents
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
print(fig)
print(ax)

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
matplotlib.pyplot.imshow(environment) 
matplotlib.pyplot.show()

# To confirm our environment is a square, a simple test will be run to check the rows equal the length of the environment.
nrows = len(environment)

nrows = len(environment) # Answer 300
print("nrows", nrows)
for i in range(nrows): # Tests whether cols == rows
    ncols = len(environment)
    if (ncols != 300):
        print("Not square - re-check source file") # Test to see if all rows have the same number of columns
print("ncols", ncols)

# Returns nrows 300, ncols 300 so square and can proceed.

##########################
# Creates agents i.e. adds values to y and x
##########################
   
# Add values to y and x 
agents = [] # Create empty list which will be populated.
# Make the agents.
for i in range(num_of_agents):
    # Sets up initial agents with 
    agents.append(agentframework_animation.Agent(agents, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          environment,
                                          random.randint(0,10)))

    
##########################
# Plots agents
##########################

matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents): 
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

# =============================================================================
# ##########################
# # Sums stores to check 'eat' function working.
# ##########################
# 
# 
# def sum_stores():
#     '''
#     Adds up the store in all the agents.
# 
#     Returns
#     -------
#     total_store : Number
#         Total store in all the agents.
# 
#     '''
#     # Sum up all the stores
#     total_store = 0
#     for i in range(num_of_agents):
#         #print("agent store", agents[i].store)
#         total_store = total_store + agents[i].store
#     #print("total_store", total_store)
#     return total_store
# 
# print("total_store", sum_stores())
# =============================================================================


##########################
# Animate agents moving, eating and sharing environment.
##########################

carry_on = True	

def update(frame_number):

    fig.clear()   
    global carry_on
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents) # Shuffles the sequence agent in place
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
    matplotlib.pyplot.imshow(environment) # Adds environment data
    matplotlib.pyplot.xlim(0, 300) # Adds x and y axes
    matplotlib.pyplot.ylim(0, 300)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x ,agents[i].y, color='black', s=60)


       
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)

matplotlib.pyplot.show()

# Can save animations: https://holypython.com/how-to-save-matplotlib-animations-the-ultimate-guide/

print ("Finish")

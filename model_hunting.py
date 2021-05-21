# Remove all previously saved variables
from IPython import get_ipython
get_ipython().magic('reset -sf')

# Import modules
import csv
import operator
import matplotlib.pyplot
import matplotlib.animation 
from datetime import datetime
import os
import agentframework_hunting as af #Labelled for wolves, sheep practical.
import random
import time
import sys

print ("Start") # Confirmation that code is running.



# =============================================================================
#  ABM FURTHER MODEL DEVELOPMENT
#
# User input allowed here to change No. of sheep, wolves, No. of interations and neighbourhoods. 
# 
# =============================================================================
num_of_sheep = 50
num_of_wolves = 5 #Used 1 to test.
num_of_iterations = 100
neighbourhood = 20
wolfneighbourhood = 60

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


"""
# Always important to test load - only required on initial load of data (or else new data files).
# Used as a quick check to ensure data is importing correcting.

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# To confirm our environment is a square, a simple test will be run to check the rows equal the length of the environment.
nrows = len(environment) # Answer 300

print("nrows", nrows)
for i in range(nrows): # Tests whether cols == rows
    ncols = len(environment)
    if (ncols != 300):
        print("Not square - re-check source file") # Test to see if all rows have the same number of columns
print("ncols", ncols)

# Returns nrows 300, ncols 300 so square and can proceed.

"""    
##########################
# Creates sheep i.e. adds values to y and x
##########################

# Add values to y and x 
sheep = [] # Create empty list which will be populated.
# Make the sheep.
for i in range(num_of_sheep):
    # Sets up initial sheep with 
    sheep.append(af.Sheep(i, sheep, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          environment,
                                          random.randint(0,10)))
    
for i in range(len(sheep)): 
    print(sheep[i])
# Sheep print out correctly.


##########################
# Creates wolves i.e. adds values to y and x
##########################

# Copied sheep code, put it through Notepad++ and found and replaced sheep/wolves (noting case sensitivity).
#Tested - worked with same parameters as sheep, then removed/changed one function at a time.


wolves = [] # Create empty list which will be populated.
# Make the wolves.
for i in range(num_of_wolves):
    # Sets up initial wolves with 
    wolves.append(af.Wolves(wolves, sheep, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          random.randint(0,30))) # Changed store to 30

for i in range(len(wolves)): 
    print(wolves[i])
#Wolves print out correctly.
    

# Print all the sheep
for i in range(len(sheep)): 
    print(sheep[i]) 
#Sheep print out correctly.
    
# Check No. of wolves and sheep, x, y and stores correct.  Yes.
 

   
# Test new sheep/wolves move function distance.
for j in range (1):
    for i in range(num_of_sheep):
        sheep[i].move(10) # Sheep moves ten each time (hence why changed iteration to 1 to check).
# Used print statements to check distance moved before and after move, e.g. 
#Before move SHEEP94: x=41, y=203, store=0
#After move SHEEP94: x=51, y=193, store=0
        
for j in range (1):
    for i in range(num_of_wolves):
        wolves[i].move(30) # Sheep moves ten each time (hence why changed iteration to 1 to check).         
# Used print statements to check distance moved before and after move, e.g. 
#Before move WOLF: x=47, y=188, store=10
#After move WOLF: x=77, y=218, store=10        
        
# Test new sheep/wolves eat/eat_sheep function.
for j in range (1):
    for i in range(num_of_sheep):
        sheep[i].eat() 
for j in range (1):
    for i in range(num_of_wolves):
        wolves[i].eat_sheep(sheep, wolfneighbourhood)        
# Used print statements to check whether all sheep eaten in neighbourhood, e.g. 
#Eating sheep SHEEP45: x=86, y=53, store=19
#After eat sheep WOLF: x=61, y=6, store=1006 - Sheep 45 in neighbourhood so got eaten.

#Used print statements to check number of sheep eaten
#number of sheep eaten 6
#[4, 17, 23, 24, 32, 43] # List of sheep eaten
#[43, 32, 24, 23, 17, 4] # Reverse list of sheep eaten
#number of sheep 46
#number of sheep after eat 40 # 6 have been eaten
#SHEEP0: x=205, y=207, store=10
#SHEEP3: x=9, y=193, store=13
#SHEEP7: x=168, y=85, store=11
#SHEEP8: x=179, y=27, store=17


print ("Finish")

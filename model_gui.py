# Remove all previously saved variables
from IPython import get_ipython
get_ipython().magic('reset -sf')

import matplotlib
matplotlib.use('TkAgg')
import csv
#import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework_gui as af #Labelled for GUI practical. 
import random
import tkinter
import requests
import bs4


print ("Start") # Confirmation that code is running.

# =============================================================================
# 
# User input allowed here to change No. of agents and No. of interations. 
# 
# =============================================================================
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Set the random seed for reproducibility (for testing purposes)
random.seed(0)


##########################
# Data from web
##########################
td_ys = [] # Creates lists to hold x and y data from web.
td_xs = []
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



##########################
# Load the environment
##########################

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


# =============================================================================
# ##########################
# # Set up agents (with web scrapped values)
# ##########################
# 
# # Not working. Error message, 'environment' and 'store' are missing positional arguments.
# # I don't understand as these are included.
#  
# agents = []
# for i in range(num_of_agents):
#     y = td_ys[i]
#     x = td_xs[i]
#     agents.append(af.Agent(agents, environment, random.randint(0,10)))
# 
# print(td_ys)
# matplotlib.pyplot.imshow(environment)
# for i in range(num_of_agents): 
#     matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
# matplotlib.pyplot.show()
# 
# print(agents[i].x)
# 
# #Tested when printed and agents don't plot. Abort. 
# # I haven't managed to get new ints into constructor.
# 
# =============================================================================

##########################
# Set up agents (with random digits)
###########################

# Create agents for code not replying on web data.
# Add values to y and x 
agents = [] # Create empty list which will be populated.
# Make the agents.
for i in range(num_of_agents):
    # Sets up initial agents with 
    agents.append(af.Agent(agents, 
                                          random.randint(0,(len(environment))-1),
                                          random.randint(0,(len(environment))-1), 
                                          environment,
                                          random.randint(0,10)))

#Check data plots
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents): 
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()
    
##########################
# Stimulate agents
##########################

# Set up figure for animating agents
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
print(fig)
print(ax)


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


# GUI
# This run function creates a window which activates our animation when the run button is pushed.

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    #canvas.show()
    canvas.draw()

# This creates a window from which we can choose the menu, and then run button.    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
#model_menu.add_command(label="Information", command=run)

    

def quit(root): #Exits Tkinter program
    root.destroy()
    
print ("finish")

tkinter.mainloop()
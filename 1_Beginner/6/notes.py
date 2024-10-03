# FUNCTIONS, CODE BLOCKS AND WHILE LOOPS
# help of Karel The Robot

# 1. Defining Functions

# Built-in functions
print("Hello")
num_char = len("Hello")
print(num_char)
# etc.

# User-Defined Functions
def myFunction():
    print("Hello")
    print("GoodBye")
# calling the function
myFunction()


# hardle game
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# define by platform
def move():
    print("m")#something
def turn_left():
    print("l")#something
def front_is_clear():
    print("c")#something
def wall_in_front():
    print("wf")#something
def wall_on_right():
    print("wr")#something
# start

def moving():
    move()
    turn_left()
    
def turn_over():
    move()
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    moving()
    turn_over()
    turn_over()
    moving()

for i in range(1,7):
    turn_around()

# hardle 2
at_goal = False
    
while at_goal!=True:
  turn_around
  
while not at_goal:
  turn_around
  
# hardle 3
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        turn_over()
        turn_over()
        moving()

# hardle 4
def moving():
    move()
    
def turn_over():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        moving()
    elif wall_in_front():
        turn_left()
        while wall_on_right():
            moving()
        turn_over()
        moving()
        turn_over()
        while front_is_clear():
            moving()
        turn_left()
        
    



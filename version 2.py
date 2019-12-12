
#Psuedocode:

#add turtles       
import turtle as trtl
import random 

shape = "circle"
maze_painter = trtl.Turtle(shape = shape)
maze_painter.ht()
maze_painter.speed(0)
maze_painter.pencolor("orange")


#import new turtle 
player = trtl.Turtle(shape = shape )
player.color("blue")
player.speed(0)
player.penup()
#program walls and width size
number_walls = 40
wall_width = 10 
door_width = 20
distance = 30
barrier = 20
wall_color = "black"
maze_painter.pencolor(wall_color)
count = 0

def drawBarrier():
    maze_painter.left(90)
    maze_painter.forward(door_width)
    maze_painter.backward(door_width)
    maze_painter.right(90)

def drawDoor():
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()

def up():
    player.setheading(90)
    player.forward(10)

def down():
    player.setheading(90)
    player.forward(-10)

def right():
    player.setheading(90)
    player.right(90)
    player.forward(10)

def left():
    player.setheading(90)
    player.left(90)
    player.forward(10)

#add gaps in the walls 
while count < number_walls:

    #add breaks in the wall
    if (count > 4):
        door = random.randint(door_width, distance - 2*door_width)
        barrier = random.randint(2*wall_width, distance - 2*door_width)
#door
        if door < barrier :
            maze_painter.forward(door)
            drawDoor()
            maze_painter.forward(barrier - door - door_width)
            drawBarrier()
            maze_painter.forward(distance - barrier)
#barrier        
        else :
            maze_painter.forward(barrier)
            drawBarrier()
            maze_painter.forward(door-barrier)
            drawDoor()
            maze_painter.forward(distance - door - door_width)
       

    maze_painter.left(90)
    count+=1
    distance += wall_width


wn=trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")

wn.listen()

wn.mainloop()

#Author:Andy Chu
#Date:Jan 17,2021

import random
import turtle as t

def get_line_length():
    choice = input('Enter line length "long, medium, short":')

    print(choice)

    if choice == 'long':
        line = 250
    elif choice == 'medium':
          line = 200
    else:
        line = 50   
    return line

def get_line_width():
    choice = input('Enter line thick "superthick, thick, thin":')

    print(choice)

    if choice == 'superthick':
        line = 40
    elif choice == 'thick':
          line = 25
    else:
        line = 10
    return line

def move_turtle(line_length):
    pen_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    t.pencolor(random.choice(pen_color))
    t.fillcolor(random.choice(pen_color))
    
    t.shapesize(3,2,1)           
    t.stamp()         
    t.right(45)
    t.forward(line_length)
            
line_length = get_line_length()
line_width = get_line_width()

t.shape('turtle')
t.fillcolor('blue')
t.pensize(line_width)

while True:
    move_turtle(line_length)

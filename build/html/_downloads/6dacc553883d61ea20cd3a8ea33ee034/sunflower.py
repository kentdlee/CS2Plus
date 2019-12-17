''' 
    Author: Kent D. Lee
    Date: 9/26/2014
    Copyright (c) 2014
    Free for educational use. Others may use with permission.

    Source: 

    I used http://fractalfoundation.org/OFC/OFC-11-3.html as a source for this 
    information. 
    
    Description:
    
    This program draws sunflower seeds in the pattern of a funflower. The ration of 
    consecutive fibonacci numbers in the sequence approach the golden ratio as the 
    sequence grows. In the limit, the ratio of two consecutive fibonacci numbers is
    the golden ratio. 
    
    In the sunflower fibonacci numbers can be observed by counting the number of seeds
    in the spiral arms. Count the number of seeds in a left spiral arm and a right spiral
    arm. You'll see that they are two fibonacci numbers. 
    
    You may have to make the radius size of the seeds constant to count the seeds. It won't
    look as pretty, but will be easier to count. You may also need to increase the forward 
    to separate the seeds. 
'''

import turtle
import math


class Circle:
    def __init__(self,radius, width=1,color="white",outline="black"):
        self.radius = radius
        self.width = width
        self.color = color
        self.outline = outline
        
    def draw(self,turtle):
        centerX = turtle.xcor()
        centerY = turtle.ycor()
        turtle.penup()
        turtle.goto(centerX+self.radius,centerY)
        turtle.pendown()
        turtle.width(self.width)
        turtle.pencolor(self.outline)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(361):
            newX = self.radius * math.cos((i/180.0) * math.pi) + centerX
            newY = self.radius * math.sin((i/180.0) * math.pi) + centerY
            turtle.goto(newX,newY)
            
        turtle.end_fill()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.pendown()
        
def main():
    
    t = turtle.Turtle()
    t.ht()
    screen = t.getscreen()
    screen.tracer(0)
    
    for x in range(400):
        c = Circle(x/16+4,width=2,color="yellow")
        c.draw(t)
        # This angle is chosen because it is approx.
        # 360/1.61803399. The 1.61803399 is the approx.
        # value of the golden angle
        t.left(222.5)
        t.penup()
        t.forward(x*2 + 8)
        screen.update()
    
    
    
    screen.exitonclick()
    
if __name__ == "__main__":
    main()
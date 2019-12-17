import turtle

def drawSpiral(t, length, color, colorBase):
    #color is a 24 bit value that is changing a bit
    #each time for a nice color effect
    if length == 0:
        return
    
    # add 2^10 to the old color modulo 2^24 
    # the modulo 2^24 prevents the color from 
    # getting too big.
    newcolor = (int(color[1:],16) + 2**10)%(2**24)
    
    # find the color base integer value
    base = int(colorBase[1:],16)
    
    # now if the new color is less than the base
    # add the base module 2^24.
    if newcolor < base:
        newcolor = (newcolor + base)%(2**24)
     
    # let newcolor be the hex string after conversion.   
    newcolor = hex(newcolor)[2:]
    
    # add a pound sign and zeroes to the front so it
    # is 6 characters long plus the pound sign for a
    # proper color string. 
    newcolor = "#"+("0"*(6-len(newcolor)))+newcolor

    t.color(newcolor)   
    t.forward(length)   
    t.left(90)
    
    drawSpiral(t, length-1, newcolor, colorBase)
        
def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100,-100)
    t.pendown()

    drawSpiral(t, 200, "#000000", "#ff00ff")
    
    screen.exitonclick()
    

if __name__ == "__main__":
    main()
        
.. _appendixH:

Appendix H: Complete Programs
-------------------------------

.. _`drawingprogram`:

The Draw Program
====================

Here is the complete Draw program implementation. This is the tkinter GUI version that reads and writes XML files.


.. code-block:: python
	:linenos:

	# The imports include turtle graphics and tkinter modules. 
	# The colorchooser and filedialog modules let the user
	# pick a color and a filename.
	import turtle
	import tkinter
	import tkinter.colorchooser
	import tkinter.filedialog
	import xml.dom.minidom

	# The following classes define the different commands that 
	# are supported by the drawing application. 
	class GoToCommand:
	    def __init__(self,x,y,width=1,color="black"):
	        self.x = x
	        self.y = y
	        self.width = width
	        self.color = color
	        
	    # The draw method for each command draws the command
	    # using the given turtle
	    def draw(self,turtle):
	        turtle.width(self.width)
	        turtle.pencolor(self.color)
	        turtle.goto(self.x,self.y)
	        
	    # The __str__ method is a special method that is called
	    # when a command is converted to a string. The string
	    # version of the command is how it appears in the graphics
	    # file format. 
	    def __str__(self):
	        return '<Command x="' + str(self.x) + '" y="' + str(self.y) + \
	               '" width="' + str(self.width) \
	               + '" color="' + self.color + '">GoTo</Command>' 
	        
	class CircleCommand:
	    def __init__(self,radius, width=1,color="black"):
	        self.radius = radius
	        self.width = width
	        self.color = color
	        
	    def draw(self,turtle):
	        turtle.width(self.width)
	        turtle.pencolor(self.color)
	        turtle.circle(self.radius)
	        
	    def __str__(self):
	        return '<Command radius="' + str(self.radius) + '" width="' + \
	               str(self.width) + '" color="' + self.color + '">Circle</Command>'
	        
	class BeginFillCommand:
	    def __init__(self,color):
	        self.color = color
	        
	    def draw(self,turtle):
	        turtle.fillcolor(self.color)
	        turtle.begin_fill()
	        
	    def __str__(self):
	        return '<Command color="' + self.color + '">BeginFill</Command>'
	        
	class EndFillCommand:
	    def __init__(self):
	        pass
	    
	    def draw(self,turtle):
	        turtle.end_fill()
	        
	    def __str__(self):
	        return "<Command>EndFill</Command>"
	        
	class PenUpCommand:
	    def __init__(self):
	        pass
	    
	    def draw(self,turtle):
	        turtle.penup()
	        
	    def __str__(self):
	        return "<Command>PenUp</Command>"
	        
	class PenDownCommand:
	    def __init__(self):
	        pass
	    
	    def draw(self,turtle):
	        turtle.pendown()
	        
	    def __str__(self):
	        return "<Command>PenDown</Command>"

	# This is the container class for a graphics sequence. It is meant
	# to hold the graphics commands sequence. 
	class GraphicsSequence:
	    def __init__(self):
	        self.gcList = []
	        
	    # The append method is used to add commands to the sequence.
	    def append(self,item):
	        self.gcList = self.gcList + [item]
	        
	    # This method is used by the undo function. It slices the sequence
	    # to remove the last item
	    def removeLast(self):
	        self.gcList = self.gcList[:-1]
	       
	    # This special method is called when iterating over the sequence.
	    # Each time yield is called another element of the sequence is returned
	    # to the iterator (i.e. the for loop that called this.)
	    def __iter__(self):
	        for c in self.gcList:
	            yield c
	    
	    # This is called when the len function is called on the sequence.        
	    def __len__(self):
	        return len(self.gcList)
	    
	    # The write method writes an XML file to the given filename
	    def write(self,filename):
	        file = open(filename, "w")
	        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
	        file.write('<GraphicsCommands>\n')
	        for cmd in self:
	            file.write('    '+str(cmd)+"\n")
	            
	        file.write('</GraphicsCommands>\n')
	            
	        file.close()  
	        
	    # The parse method adds the contents of an XML file to this sequence
	    def parse(self,filename):
	        xmldoc = xml.dom.minidom.parse(filename)
	        
	        graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]
	        
	        graphicsCommands = graphicsCommandsElement.getElementsByTagName("Command")
	        
	        for commandElement in graphicsCommands:
	            command = commandElement.firstChild.data.strip()
	            attr = commandElement.attributes
	            if command == "GoTo":
	                x = float(attr["x"].value)
	                y = float(attr["y"].value)
	                width = float(attr["width"].value)
	                color = attr["color"].value.strip()
	                cmd = GoToCommand(x,y,width,color)
	    
	            elif command == "Circle":
	                radius = float(attr["radius"].value)
	                width = int(attr["width"].value)
	                color = attr["color"].value.strip()
	                cmd = CircleCommand(radius,width,color)
	    
	            elif command == "BeginFill":
	                color = attr["color"].value.strip()
	                cmd = BeginFillCommand(color)
	    
	            elif command == "EndFill":
	                cmd = EndFillCommand()
	                
	            elif command == "PenUp":
	                cmd = PenUpCommand()
	                
	            elif command == "PenDown":
	                cmd = PenDownCommand()
	            else:
	                raise RuntimeError("Unknown Command: " + command) 
	    
	            self.append(cmd)
	        
	# This class defines the drawing application. The following line says that
	# the DrawingApplication class inherits from the Frame class. This means
	class DrawingApplication(tkinter.Frame):
	    def __init__(self, master=None):
	        super().__init__(master)
	        self.pack()
	        self.buildWindow()    
	        self.graphicsCommands = GraphicsSequence()
	 
	    # This method is called to create all the widgets, place them in the GUI,
	    # and define the event handlers for the application.
	    def buildWindow(self):
	        
	        # The master is the root window. The title is set as below. 
	        self.master.title("Draw")
	        
	        # Here is how to create a menu bar. The tearoff=0 means that menus
	        # can't be separated from the window which is a feature of tkinter.
	        bar = tkinter.Menu(self.master)
	        fileMenu = tkinter.Menu(bar,tearoff=0)
	        
	        # This code is called by the "New" menu item below when it is selected.
	        # The same applies for loadFile, addToFile, and saveFile below. The 
	        # "Exit" menu item below calls quit on the "master" or root window. 
	        def newWindow():
	            # This sets up the turtle to be ready for a new picture to be 
	            # drawn. It also sets the sequence back to empty. It is necessary
	            # for the graphicsCommands sequence to be in the object (i.e. 
	            # self.graphicsCommands) because otherwise the statement:
	            # graphicsCommands = GraphicsSequence()
	            # would make this variable a local variable in the newWindow 
	            # method. If it were local, it would not be set anymore once the
	            # newWindow method returned.
	            theTurtle.clear()
	            theTurtle.penup()
	            theTurtle.goto(0,0)
	            theTurtle.pendown()  
	            screen.update()
	            screen.listen()
	            self.graphicsCommands = GraphicsSequence()
	            
	        fileMenu.add_command(label="New",command=newWindow)
	            
	        def loadFile():

	            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
	            
	            newWindow()
	            
	            # This re-initializes the sequence for the new picture. 
	            self.graphicsCommands = GraphicsSequence()
	            
	            # calling parse will read the graphics commands from the file.
	            self.graphicsCommands.parse(filename)
	               
	            for cmd in self.graphicsCommands:
	                cmd.draw(theTurtle)
	                
	            # This line is necessary to update the window after the picture is drawn.
	            screen.update()
	            
	            
	        fileMenu.add_command(label="Load...",command=loadFile)
	        
	        def addToFile():
	            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
	            
	            theTurtle.penup()
	            theTurtle.goto(0,0)
	            theTurtle.pendown()
	            theTurtle.pencolor("#000000")
	            theTurtle.fillcolor("#000000")
	            cmd = PenUpCommand()
	            self.graphicsCommands.append(cmd)
	            cmd = GoToCommand(0,0,1,"#000000")
	            self.graphicsCommands.append(cmd)
	            cmd = PenDownCommand()
	            self.graphicsCommands.append(cmd)
	            screen.update()
	            self.graphicsCommands.parse(filename)
	               
	            for cmd in self.graphicsCommands:
	                cmd.draw(theTurtle)
	                
	            screen.update()            
	        
	        fileMenu.add_command(label="Load Into...",command=addToFile)
	        
	        def saveFile():
	            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")
	            self.graphicsCommands.write(filename)
	            
	        fileMenu.add_command(label="Save As...",command=saveFile)
	        

	        fileMenu.add_command(label="Exit",command=self.master.quit)
	        
	        bar.add_cascade(label="File",menu=fileMenu)
	        
	        # This tells the root window to display the newly created menu bar.
	        self.master.config(menu=bar)    
	        
	        # Here several widgets are created. The canvas is the drawing area on 
	        # the left side of the window. 
	        canvas = tkinter.Canvas(self,width=600,height=600)
	        canvas.pack(side=tkinter.LEFT)
	        
	        # By creating a RawTurtle, we can have the turtle draw on this canvas. 
	        # Otherwise, a RawTurtle and a Turtle are exactly the same.
	        theTurtle = turtle.RawTurtle(canvas)
	        
	        # This makes the shape of the turtle a circle. 
	        theTurtle.shape("circle")
	        screen = theTurtle.getscreen()
	        
	        # This causes the application to not update the screen unless 
	        # screen.update() is called. This is necessary for the ondrag event
	        # handler below. Without it, the program bombs after dragging the 
	        # turtle around for a while.
	        screen.tracer(0)
	    
	        # This is the area on the right side of the window where all the 
	        # buttons, labels, and entry boxes are located. The pad creates some empty 
	        # space around the side. The side puts the sideBar on the right side of the 
	        # this frame. The fill tells it to fill in all space available on the right
	        # side. 
	        sideBar = tkinter.Frame(self,padx=5,pady=5)
	        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
	        
	        # This is a label widget. Packing it puts it at the top of the sidebar.
	        pointLabel = tkinter.Label(sideBar,text="Width")
	        pointLabel.pack()
	        
	        # This entry widget allows the user to pick a width for their lines. 
	        # With the widthSize variable below you can write widthSize.get() to get
	        # the contents of the entry widget and widthSize.set(val) to set the value
	        # of the entry widget to val. Initially the widthSize is set to 1. str(1) is 
	        # needed because the entry widget must be given a string. 
	        widthSize = tkinter.StringVar()
	        widthEntry = tkinter.Entry(sideBar,textvariable=widthSize)
	        widthEntry.pack()
	        widthSize.set(str(1))
	        
	        radiusLabel = tkinter.Label(sideBar,text="Radius")
	        radiusLabel.pack()
	        radiusSize = tkinter.StringVar()
	        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
	        radiusSize.set(str(10))
	        radiusEntry.pack()
	        
	        # A button widget calls an event handler when it is pressed. The circleHandler
	        # function below is the event handler when the Draw Circle button is pressed. 
	        def circleHandler():
	            # When drawing, a command is created and then the command is drawn by calling
	            # the draw method. Adding the command to the graphicsCommands sequence means the
	            # application will remember the picture. 
	            cmd = CircleCommand(int(radiusSize.get()), int(widthSize.get()), penColor.get())
	            cmd.draw(theTurtle)
	            self.graphicsCommands.append(cmd)
	            
	            # These two lines are needed to update the screen and to put the focus back
	            # in the drawing canvas. This is necessary because when pressing "u" to undo,
	            # the screen must have focus to receive the key press. 
	            screen.update()
	            screen.listen()
	        
	        # This creates the button widget in the sideBar. The fill=tkinter.BOTH causes the 
	        # button to expand to fill the entire width of the sideBar.
	        circleButton = tkinter.Button(sideBar, text = "Draw Circle", command=circleHandler)
	        circleButton.pack(fill=tkinter.BOTH)             

	        # The color mode 255 below allows colors to be specified in RGB form (i.e. Red/
	        # Green/Blue). The mode allows the Red value to be set by a two digit hexadecimal
	        # number ranging from 00-FF. The same applies for Blue and Green values. The 
	        # color choosers below return a string representing the selected color and a slice
	        # is taken to extract the #RRGGBB hexadecimal string that the color choosers return.
	        screen.colormode(255)
	        penLabel = tkinter.Label(sideBar,text="Pen Color")
	        penLabel.pack()
	        penColor = tkinter.StringVar()
	        penEntry = tkinter.Entry(sideBar,textvariable=penColor)
	        penEntry.pack()
	        # This is the color black.
	        penColor.set("#000000")  
	        
	        def getPenColor():
	            color = tkinter.colorchooser.askcolor()
	            if color != None:
	                penColor.set(str(color)[-9:-2])
	            
	        penColorButton = tkinter.Button(sideBar, text = "Pick Pen Color", command=getPenColor)
	        penColorButton.pack(fill=tkinter.BOTH)           
	            
	        fillLabel = tkinter.Label(sideBar,text="Fill Color")
	        fillLabel.pack()
	        fillColor = tkinter.StringVar()
	        fillEntry = tkinter.Entry(sideBar,textvariable=fillColor)
	        fillEntry.pack()
	        fillColor.set("#000000")     
	        
	        def getFillColor():
	            color = tkinter.colorchooser.askcolor()
	            if color != None:    
	                fillColor.set(str(color)[-9:-2])       
	   
	        fillColorButton = \
	            tkinter.Button(sideBar, text = "Pick Fill Color", command=getFillColor)
	        fillColorButton.pack(fill=tkinter.BOTH) 


	        def beginFillHandler():
	            cmd = BeginFillCommand(fillColor.get())
	            cmd.draw(theTurtle)
	            self.graphicsCommands.append(cmd)
	            
	        beginFillButton = tkinter.Button(sideBar, text = "Begin Fill", \
	                          command=beginFillHandler)
	        beginFillButton.pack(fill=tkinter.BOTH) 
	        
	        def endFillHandler():
	            cmd = EndFillCommand()
	            cmd.draw(theTurtle)
	            self.graphicsCommands.append(cmd)
	            
	        endFillButton = tkinter.Button(sideBar, text = "End Fill", command=endFillHandler)
	        endFillButton.pack(fill=tkinter.BOTH) 
	 
	        penLabel = tkinter.Label(sideBar,text="Pen Is Down")
	        penLabel.pack()
	        
	        def penUpHandler():
	            cmd = PenUpCommand()
	            cmd.draw(theTurtle)
	            penLabel.configure(text="Pen Is Up")
	            self.graphicsCommands.append(cmd)

	        penUpButton = tkinter.Button(sideBar, text = "Pen Up", command=penUpHandler)
	        penUpButton.pack(fill=tkinter.BOTH) 
	       
	        def penDownHandler():
	            cmd = PenDownCommand()
	            cmd.draw(theTurtle)
	            penLabel.configure(text="Pen Is Down")
	            self.graphicsCommands.append(cmd)

	        penDownButton = tkinter.Button(sideBar, text = "Pen Down", command=penDownHandler)
	        penDownButton.pack(fill=tkinter.BOTH)          

	        # Here is another event handler. This one handles mouse clicks on the screen.
	        def clickHandler(x,y): 
	            # When a mouse click occurs, get the widthSize entry value and set the width of the 
	            # pen to the widthSize value. The int(widthSize.get()) is needed because
	            # the width is an integer, but the entry widget stores it as a string.
	            cmd = GoToCommand(x,y,int(widthSize.get()),penColor.get())
	            cmd.draw(theTurtle)
	            self.graphicsCommands.append(cmd)          
	            screen.update()
	            screen.listen()
	           
	        # Here is how we tie the clickHandler to mouse clicks.
	        screen.onclick(clickHandler)  
	        
	        def dragHandler(x,y):
	            cmd = GoToCommand(x,y,int(widthSize.get()),penColor.get())
	            cmd.draw(theTurtle)
	            self.graphicsCommands.append(cmd)  
	            screen.update()
	            screen.listen()
	            
	        theTurtle.ondrag(dragHandler)
	        
	        # the undoHandler undoes the last command by removing it from the 
	        # sequence and then redrawing the entire picture. 
	        def undoHandler():
	            if len(self.graphicsCommands) > 0:
	                self.graphicsCommands.removeLast()
	                theTurtle.clear()
	                theTurtle.penup()
	                theTurtle.goto(0,0)
	                theTurtle.pendown()
	                for cmd in self.graphicsCommands:
	                    cmd.draw(theTurtle)
	                screen.update()
	                screen.listen()
	                
	        screen.onkeypress(undoHandler, "u")
	        screen.listen()
	   
	# The main function in our GUI program is very simple. It creates the 
	# root window. Then it creates the DrawingApplication frame which creates 
	# all the widgets and has the logic for the event handlers. Calling mainloop
	# on the frames makes it start listening for events. The mainloop function will 
	# return when the application is exited. 
	def main():
	    root = tkinter.Tk()  
	    drawingApp = DrawingApplication(root)  

	    drawingApp.mainloop()
	    print("Program Execution Completed.")
	        
	if __name__ == "__main__":
	    main()

.. _scope-prog:

The Scope Program
=====================

Here is the complete code for the scope.py program that appeared in chapter 3. ::

	import math

	PI = math.pi

	def area(radius):
	    theArea = PI * radius ** 2
	    
	    return theArea


	def main():
	    
	    historyOfPrompts = []
	    historyOfOutput = []
	    
	    def getInput(prompt):
	        x = input(prompt)
	        historyOfPrompts.append(prompt)
	        
	        return x
	    
	    def showOutput(val):
	        historyOfOutput.append(val)
	        print(val)
	    
	    rString = getInput("Please enter the radius of a circle: ")
	    
	    r = float(rString)
	    
	    val = area(r)
	    
	    showOutput("The area of the circle is " + str(val))
	    
	if __name__ == "__main__":
	    main()

.. _`sortanim`:

The Sort Animation
=================================

Here is the sort animation program described in chapter 4. 


.. code-block:: python

	import tkinter
	import turtle
	import random
	import time
	import math

	class Point(turtle.RawTurtle):
	    def __init__(self, canvas, x, y):
	        super().__init__(canvas)
	        canvas.register_shape("dot",((3,0),(2,2),(0,3),(-2,2),(-3,0),(-2,-2),(0,-3),(2,-2)))
	        self.shape("dot")
	        self.speed(0)
	        self.penup()
	        self.goto(x,y)

	    def __str__(self):
	        return "("+str(self.xcor())+","+str(self.ycor())+")"
	    
	    def __lt__(self, other):
	        return self.ycor() < other.ycor()     

	# This class defines the animation application. The following line says that
	# the SortAnimation class inherits from the Frame class. 
	class SortAnimation(tkinter.Frame):
	    def __init__(self, master=None):
	        super().__init__(master)
	        self.pack()
	        self.buildWindow()    
	        self.paused = False
	        self.stop = False
	        self.running = False
	 

	    def buildWindow(self):
	        
	        def partition(seq, start, stop):
	            pivotIndex = start
	            pivot = seq[pivotIndex]
	            
	            theTurtle.color("red")
	            theTurtle.penup()
	            theTurtle.goto(start,pivot.ycor())
	            theTurtle.pendown()
	            theTurtle.goto(stop,pivot.ycor())
	            screen.update()
	            
	            # Why twice? Because once doesn't seem to display
	            # the line the first time through for some reason            
	            theTurtle.color("red")
	            theTurtle.penup()
	            theTurtle.goto(start,pivot.ycor())
	            theTurtle.pendown()
	            theTurtle.goto(stop,pivot.ycor())
	            screen.update()
	            
	            i = start+1
	            j = stop-1
	            
	            while i <= j:
	                while i <= j and not pivot < seq[i]:
	                    i+=1
	                while i <= j and pivot < seq[j]:
	                    j-=1
	                    
	                if i < j:
	                    tmp = seq[i]
	                    seq[i] = seq[j]
	                    seq[i].goto(i,seq[i].ycor())
	                    seq[j] = tmp
	                    seq[j].goto(j,seq[j].ycor())
	                    screen.update()
	                    i+=1
	                    j-=1
	                    
	            seq[pivotIndex] = seq[j]
	            seq[pivotIndex].goto(pivotIndex,seq[pivotIndex].ycor())
	            seq[j] = pivot
	            seq[j].goto(j,seq[j].ycor())
	            seq[j].color("green")
	            screen.update()
	                        
	            theTurtle.color("white")
	            theTurtle.penup()
	            theTurtle.goto(0,pivot.ycor())
	            theTurtle.pendown()
	            theTurtle.goto(len(seq),pivot.ycor())
	            screen.update()   
	            
	            return j
	                
	            
	        def quicksortRecursively(seq, start, stop):
	            if start >= stop-1:
	                return 
	            
	            if stopping():
	                return
	            
	            pivotIndex = partition(seq, start, stop)
	            
	            if stopping():
	                return
	            
	            quicksortRecursively(seq, start, pivotIndex)
	            
	            if stopping():
	                return
	            
	            quicksortRecursively(seq, pivotIndex+1, stop)
	            
	        def quicksort(seq):
	            quicksortRecursively(seq, 0, len(seq))   
	            
	        def merge(seq, start, mid, stop):
	            length = stop - start
	            log = math.log(length,2)
	            
	            theTurtle.color("blue")
	            theTurtle.penup()
	            theTurtle.goto(start,-3*log)
	            theTurtle.pendown()
	            theTurtle.forward(length)
	            screen.update()
	            
	            lst = []
	            i = start
	            j = mid
	            
	            # Merge the two lists while each has more elements
	            while i < mid and j < stop:
	                if seq[i] < seq[j]:
	                    lst.append(seq[i])
	                    seq[i].goto(i,seq[i].ycor())
	                    i+=1
	                else:
	                    lst.append(seq[j])
	                    seq[j].goto(j,seq[j].ycor())
	                    j+=1
	                #screen.update()
	                
	            # Copy in the rest of the start to mid sequence    
	            while i < mid:
	                lst.append(seq[i])
	                seq[i].goto(i,seq[i].ycor())
	                i+=1
	                #screen.update()
	                
			    # Many merge sort implementations copy the rest
		        # of the sequence from j to stop at this point. 
		        # This is not necessary since in the next part
		        # of the code the same part of the sequence would
		        # be copied right back to the same place. In the 
		        # animation this results in a dot remaining black
		        # at some points until it is caught up in a later
		        # merge operation.
		        # while j < stop:
		        #    lst.append(seq[j])
		        #    seq[j].goto(j,seq[j].ycor())
		        #    j+=1
	                
	            # Copy the elements back to the original sequence   
	            for i in range(len(lst)):
	                seq[start+i]=lst[i]
	                lst[i].goto(start+i,lst[i].ycor())
	                lst[i].color("green")
	                screen.update()
	            
	        def mergeSortRecursively(seq, start, stop):
	            if start >= stop-1:
	                return 
	            
	            mid = (start + stop) // 2
	            
	            if stopping():
	                return
	            
	            length = stop-start
	            log = math.log(length,2)

	            theTurtle.color("red")
	            theTurtle.penup()
	            theTurtle.goto(start,-3*log)
	            theTurtle.pendown()
	            theTurtle.forward(length)
	            screen.update()
	            
	            # Why twice? Because once doesn't seem to display
	            # the line the first time through for some reason
	            theTurtle.color("red")
	            theTurtle.penup()
	            theTurtle.goto(start,-3*log)
	            theTurtle.pendown()
	            theTurtle.forward(length)
	            screen.update()  
	            
	            mergeSortRecursively(seq, start, mid)
	            
	            if stopping():
	                return            
	            
	            mergeSortRecursively(seq, mid, stop)

	            if stopping():
	                return

	            theTurtle.color("blue")
	            theTurtle.penup()
	            theTurtle.goto(start,-3*log)
	            theTurtle.pendown()
	            theTurtle.forward(length)
	            screen.update()
	            
	            merge(seq, start, mid, stop)
	            
	            screen.update()
	            theTurtle.color("white")
	            theTurtle.goto(start-1,-3*log)
	            theTurtle.pendown()
	            theTurtle.forward(length+2)
	            screen.update()           
	            
	        def mergeSort(seq):
	            mergeSortRecursively(seq, 0, len(seq))                     
	               
	        def select(seq, start):
	            minIndex = start
	            seq[minIndex].color("green")
	            
	            for i in range(start, len(seq)):
	                if seq[minIndex] > seq[i]:
	                    seq[minIndex].color("black")
	                    minIndex = i
	                    seq[minIndex].color("green")
	        
	            return minIndex
	                
	        def selectionSort(seq):
	            for i in range(len(seq)):
	                minIndex = select(seq, i)
	                if stopping():
	                    return
	                tmp = seq[i]
	                seq[i] = seq[minIndex]
	                seq[minIndex] = tmp
	                seq[i].goto(i,seq[i].ycor())
	                seq[minIndex].goto(minIndex,seq[minIndex].ycor())
	                seq[i].color("green")        
	         
	        def pause():
	            while self.paused:
	                time.sleep(1)
	                screen.update()
	                screen.listen()                
	                
	        def stopping():
	            if self.paused:
	                pause()
	                
	            if self.stop:
	                self.pause = False
	                self.running = False
	                screen.update()
	                screen.listen()                 
	                return True
	            
	            return False
	        
	        self.master.title("Sort Animations")
	        
	        bar = tkinter.Menu(self.master)
	        fileMenu = tkinter.Menu(bar,tearoff=0)
	         
	        def clear():
	            screen.clear() 
	            screen.update()
	            screen.listen()
	            
	        def newWindow():
	            clear()
	            if self.running:
	                self.stop = True
	            
	        fileMenu.add_command(label="Clear",command=newWindow)
	        fileMenu.add_command(label="Exit",command=self.master.quit)   
	        bar.add_cascade(label="File",menu=fileMenu)
	        self.master.config(menu=bar)    
	        
	        canvas = tkinter.Canvas(self,width=600,height=600)
	        canvas.pack(side=tkinter.LEFT)
	        
	        theTurtle = turtle.RawTurtle(canvas)
	        theTurtle.ht()
	        theTurtle.speed(0)
	        screen = theTurtle.getscreen()
	        screen.tracer(0)

	        sideBar = tkinter.Frame(self,padx=5,pady=5)
	        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

	        speedLabel = tkinter.Label(sideBar,text="Animation Speed")
	        speedLabel.pack()
	        speed = tkinter.StringVar()
	        speedEntry = tkinter.Entry(sideBar,textvariable=speed)
	        speedEntry.pack()
	        speed.set("10")            

	        def selSortHandler():
	            self.running = True
	            clear()
	            screen.setworldcoordinates(0,0,200,200)
	            screen.tracer(0)
	            self.master.title("Selection Sort Animation")
	            seq = []
	            for i in range(200):
	                if stopping():
	                    return
	                
	                p = Point(screen,i,i)
	                p.color("green")
	                seq.append(p)
	                
	            screen.update()
	            screen.tracer(1)
	            
	            for i in range(200):
	                if stopping():
	                    return 
	                
	                j = random.randint(0,199)
	                
	                p = seq[i]
	                seq[i] = seq[j]
	                seq[j] = p
	                seq[i].goto(i,seq[i].ycor())
	                seq[j].goto(j,seq[j].ycor())
	                seq[i].color("black")
	                seq[j].color("black")

	            selectionSort(seq)
	            self.running = False 
	            self.stop = False
	            
	        button = tkinter.Button(sideBar, text = "Selection Sort", command=selSortHandler)
	        button.pack(fill=tkinter.BOTH) 
	        
	        def mergeSortHandler():
	            self.running = True
	            clear()
	            screen.setworldcoordinates(0,-25,200,200)
	            theTurtle.width(5)
	            screen.tracer(0)
	            self.master.title("Merge Sort Animation")
	            seq = []
	            for i in range(200):
	                if stopping():
	                    return
	                
	                p = Point(screen,i,i)
	                p.color("green")
	                seq.append(p)
	            
	            screen.update()
	            screen.tracer(1)
	            for i in range(200):
	                if stopping():
	                    return 
	                
	                j = random.randint(0,199)
	                
	                p = seq[i]
	                seq[i] = seq[j]
	                seq[j] = p
	                seq[i].goto(i,seq[i].ycor())
	                seq[j].goto(j,seq[j].ycor())
	                seq[i].color("black")
	                seq[j].color("black")
	               
	            screen.tracer(0) 
	            mergeSort(seq)
	            self.running = False 
	            self.stop = False
	            
	        button = tkinter.Button(sideBar, text = "Merge Sort", command=mergeSortHandler)
	        button.pack(fill=tkinter.BOTH)         
	        
	        def quickSortHandler():
	            self.running = True
	            clear()
	            screen.setworldcoordinates(0,0,200,200)
	            theTurtle.width(5)
	            screen.tracer(0)
	            self.master.title("Quicksort Animation")
	            seq = []
	            for i in range(200):
	                if stopping():
	                    return
	                
	                p = Point(screen,i,i)
	                p.color("green")
	                seq.append(p)
	            
	            screen.update()
	            screen.tracer(1)
	            for i in range(200):
	                if stopping():
	                    return 
	                
	                j = random.randint(0,199)
	                
	                p = seq[i]
	                seq[i] = seq[j]
	                seq[j] = p
	                seq[i].goto(i,seq[i].ycor())
	                seq[j].goto(j,seq[j].ycor())
	                seq[i].color("black")
	                seq[j].color("black")
	               
	            screen.tracer(1) 
	            quicksort(seq)
	            self.running = False 
	            self.stop = False

	            
	        button = tkinter.Button(sideBar, text = "Quicksort", command=quickSortHandler)
	        button.pack(fill=tkinter.BOTH)  
	        
	        def pauseHandler():
	            self.paused = not self.paused
	            
	        button = tkinter.Button(sideBar, text = "Pause", command=pauseHandler)
	        button.pack(fill=tkinter.BOTH)  
	        
	        def stopHandler():
	            if not self.paused and self.running:
	                self.stop = True
	            
	        button = tkinter.Button(sideBar, text = "Stop", command=stopHandler)
	        button.pack(fill=tkinter.BOTH)  
	        
	        screen.listen()
	   
	# The main function in our GUI program is very simple. It creates the 
	# root window. Then it creates the SortAnimation frame which creates 
	# all the widgets and has the logic for the event handlers. Calling mainloop
	# on the frames makes it start listening for events. The mainloop function will 
	# return when the application is exited. 
	def main():
	    root = tkinter.Tk()  
	    anim = SortAnimation(root)  

	    anim.mainloop()
	        
	if __name__ == "__main__":
	    main()

.. _`tictactoe`:

The Tic Tac Toe Application
=================================

This is the starting code for an exercise in creating a Tic Tac Toe application. 

.. code-block:: python


	from turtle import *
	import tkinter.messagebox
	import tkinter
	import random
	import math
	import datetime
	import time
	import sys

	screenMin = 0
	screenMax = 300
	Human = -1
	Computer = 1  

	class Board:
	    # When a board is constructed, you may want to make a copy of the board.
	    # This can be a shallow copy of the board because Turtle objects are 
	    # Immutable from the perspective of a board object. 
	    def __init__(self, board=None, screen=None):
	        self.screen = screen
	        if screen == None: 
	            if board!=None:
	                self.screen = board.screen
	                
	        self.items = []
	        for i in range(3):
	            rowlst = []
	            for j in range(3):
	                if board==None:
	                    rowlst.append(Dummy())
	                else:
	                    rowlst.append(board[i][j])
	                
	            self.items.append(rowlst)
	     
	    # Accessor method for the screen
	    def getscreen(self):
	        return self.screen
	    
	    # The getitem method is used to index into the board. It should 
	    # return a row of the board. That row itself is indexable (it is just 
	    # a list) so accessing a row and column in the board can be written
	    # board[row][column] because of this method.
	    def __getitem__(self,index):
	        return self.items[index]
	                
	    # This method should return true if the two boards, self and other,
	    # represent exactly the same state. 
	    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
	    def __eq__(self,other):
	        pass
	    
	    # This method will mutate this board to contain all dummy 
	    # turtles. This way the board can be reset when a new game
	    # is selected. It should NOT be used except when starting
	    # a new game. 
	    def reset(self):
	        
	        self.screen.tracer(1)
	        for i in range(3):
	            for j in range(3):
	                self.items[i][j].goto(-100,-100)
	                self.items[i][j] = Dummy()
	                
	        self.screen.tracer(0)
	        
	    # This method should return an integer representing the 
	    # state of the board. If the computer has won, return 1.
	    # If the human has won, return -1. Otherwise, return 0.
	    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
	    def eval(self):
	        pass

	    # This method should return True if the board 
	    # is completely filled up (no dummy turtles). 
	    # Otherwise, it should return False.
	    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
	    def full(self):
	        pass
	    
	    # This method should draw the X's and O's
	    # Of this board on the screen. 
	    def drawXOs(self):
	        
	        for row in range(3):
	            for col in range(3):
	                if self[row][col].eval() != 0:
	                    self[row][col].st()
	                    self[row][col].goto(col*100+50,row*100+50)
	        
	        self.screen.update()        

	# This class is just for placeholder objects when no move has been made
	# yet at a position in the board. Having eval() return 0 is convenient when no
	# move has been made. 
	class Dummy:
	    def __init__(self):
	        pass
	    
	    def eval(self):
	        return 0
	    
	    def goto(self,x,y):
	        pass
	    
	# In the X and O classes below the constructor begins by initializing the 
	# RawTurtle part of the object with the call to super().__init__(canvas). The
	# super() call returns the class of the superclass (the class above the X or O
	# in the class hierarchy). In this case, the superclass is RawTurtle. Then, 
	# calling __init__ on the superclass initializes the part of the object that is
	# a RawTurtle. 
	class X(RawTurtle):
	    def __init__(self, canvas):
	        super().__init__(canvas)
	        self.ht()
	        self.getscreen().register_shape("X",((-40,-36),(-40,-44),(0,-4),(40,-44),(40,-36), \
	                             (4,0),(40,36),(40,44),(0,4),(-40,44),(-40,36),(-4,0),(-40,-36)))
	        self.shape("X")
	        self.penup()
	        self.speed(5)
	        self.goto(-100,-100)  
	        
	    def eval(self):
	        return Computer
	    
	class O(RawTurtle):
	    def __init__(self, canvas):
	        super().__init__(canvas)
	        self.ht()
	        self.shape("circle")
	        self.penup()
	        self.speed(5)
	        self.goto(-100,-100)
	        
	    def eval(self):
	        return Human

	# The minimax function is given a player (1 = Computer, -1 = Human) and a
	# board object. When the player = Computer, minimax returns the maximum 
	# value of all possible moves that the Computer could make. When the player =
	# Human then minimax returns the minimum value of all possible moves the Human
	# could make. Minimax works by assuming that at each move the Computer will pick
	# its best move and the Human will pick its best move. It does this by making a 
	# move for the player whose turn it is, and then recursively calling minimax. 
	# The base case results when, given the state of the board, someone has won or 
	# the board is full.    
	# READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
	def minimax(player,board):
	    pass

	      

	class TicTacToe(tkinter.Frame):
	    def __init__(self, master=None):
	        super().__init__(master)
	        self.pack()
	        self.buildWindow()    
	        self.paused = False
	        self.stop = False
	        self.running = False
	        self.turn = Human
	        self.locked = False
	 
	    def buildWindow(self):
	        
	        cv = ScrolledCanvas(self,600,600,600,600)
	        cv.pack(side = tkinter.LEFT)
	        t = RawTurtle(cv)
	        screen = t.getscreen()
	        screen.tracer(100000)
	    
	        screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
	        screen.bgcolor("white")
	        t.ht()
	            
	        frame = tkinter.Frame(self)
	        frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
	        board = Board(None, screen)
	    
	        def drawGrid():
	            screen.clear()
	            screen.tracer(1000000)
	            screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
	            screen.bgcolor("white")
	            screen.tracer(0)
	            t = RawTurtle(cv)
	            t.ht()
	            t.pu()
	            t.width(10)
	            t.color("green")
	            for i in range(2):
	                t.penup()
	                t.goto(i*100+100,10)
	                t.pendown()
	                t.goto(i*100+100,290)
	                t.penup()
	                t.goto(10,i*100+100)
	                t.pendown()
	                t.goto(290,i*100+100)
	    
	            screen.update()
	    
	    
	        def newGame():
	            #drawGrid()
	            self.turn = Human
	            board.reset()
	            self.locked =False
	            screen.update()
	    
	      
	        def startHandler():
	            newGame()
	            
	        drawGrid()
	    
	        startButton = tkinter.Button(frame, text = "New Game", command=startHandler)
	        startButton.pack()  
	        
	        def quitHandler():
	            self.master.quit()
	            
	        quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
	        quitButton.pack()
	    
	        def computerTurn():
	            # The locked variable prevents another event from being 
	            # processed while the computer is making up its mind. 
	            self.locked = True
		    
	            # Call Minimax to find the best move to make.
	            # READER EXERCISE: YOU MUST COMPLETE THIS CODE
	            # After writing this code, the maxMove tuple should
	            # contain the best move for the computer. For instance,
	            # if the best move is in the first row and third column
	            # then maxMove would be (0,2).
		    
	            row, col = maxMove
	            board[row][col] = X(cv)
	            self.locked = False
	    
	      
	        def mouseClick(x,y):
	            if not self.locked:
	                row = int(y // 100)
	                col = int(x // 100)
	    
	                board[row][col] = O(cv) 
	                
	                self.turn = Computer
	                
	                board.drawXOs()
	                
	                if not board.full() and not abs(board.eval())==1:
	                    computerTurn()
	                
	                    self.turn = Human
	                    
	                    board.drawXOs()
	                else:
	                    self.locked = True
	                    
	                if board.eval() == 1:
	                    tkinter.messagebox.showwarning("Game Over","X wins!!!")
	      
	                if board.eval() == -1:
	                    tkinter.messagebox.showwarning("Game Over","O wins. How did that happen?")
	                    
	                if board.full():
	                    tkinter.messagebox.showwarning("Game Over","It was a tie.")
	     
	        screen.onclick(mouseClick)
	        
	        screen.listen()

	def main():
	    root = tkinter.Tk()
	    root.title("Tic Tac Toe")    
	    application = TicTacToe(root)  
	    application.mainloop()
	        
	if __name__ == "__main__":
	    main()

.. _`c4`:

The Connect Four Front-End
=================================

This is the starting code for an exercise in creating a connect four application. This code provides a front-end to another program that must conform to the architecture discussed at the top of this code. Pictures for the red and black checkers can be found on the text's website. The pictures must be placed in the same directory as this application. 

.. code-block:: python
	:linenos:

	import turtle
	import subprocess
	import tkinter
	import sys
	import time

	# The following program will play connect four. This
	# program and a another program communicate through pipes (both input and output)
	# according to this architecture. When a command is sent it is indicated 
	# with a right arrow indicating something is written to the other program's 
	# standard input. When the other program sends something to this Python Program
	# it is indicated with a left arrow. That means it is written to the standard
	# output of the other program. 

	# Python        Other
	#   0 ----------->     # New Game is initiated by the Other Code
	#   <----------- 0     # Other Code says OK.
	#   2 M --------->     # Human Move followed by Move Value M which is 0-6.
	#                      # Move Value M will be on separate line.
	#   <----------- 0     # Other Code says OK.
	#   1 ----------->     # Computer Move is indicated to Other Code
	#   <--------- 0 M     # Status OK and Move Value M which is 0-6.
	#   3 ----------->     # Game Over?
	#   <--------- Val     # Val is 0=Not Over, 1=Computer Won, 2=Human Won, 3=Tie.

	# This architecture must be adhered to strictly for this program to work. Here
	# is sample Lisp code that will handle this interaction. However, the other 
	# program may be written in any programming language, including Python.

	#(defun play ()
	  #(let ((gameBoard (make-hash-table :size 10))
	        #(memo (make-hash-table :size 27 :test #'equalp))
	        #(lastMove nil))

	    #(do () (nil nil)
	        #;(printBoard gameBoard)
	        #(let ((msgId (read)))
	          #(cond ((equal msgId 2) ;; Human turn to call human turn function
	                 #(setf lastMove (humanTurn gameBoard)))

	                #((equal msgId 0) ;; New Game message
	                 #(progn 
	                   #(setf gameBoard (make-hash-table :size 10))
	                   #(setf memo (make-hash-table :size 27 :test #'equalp))
	                   #(format t "0~%")))
	                   #;; Return a 0 to indicate the computer is ready

	                #((equal msgId 1) ;; Computer Turn message
	                 #(setf lastMove (computerTurn gameBoard)))
	                
	                #((equal msgId 3) ;; Get Game Status
	                 
	                 #(cond ((equal (evalBoard gameBoard lastMove) 1) (format t "1~%"))
	                       #;; The Computer Won

	                       #((equal (evalBoard gameBoard lastMove) -1) (format t "2~%"))
	                       #;; The Human Won

	                       #((fullBoard gameBoard) (format t "3~%"))
	                       #;; It's a draw

	                       #(t (format t "0~%"))))
	                       #;; The game is not over yet.

	                #(t (format t "-1~%")))))))

	Computer = 1
	Human = -1

	class Tile(turtle.RawTurtle):
	    def __init__(self,canvas,row,col,app):
	        super().__init__(canvas)
	        self.val = 0
	        self.row = row
	        self.col = col
	        self.tttApplication = app
	        self.penup()
	        self.ht()
	        self.goto(col*100+50,row*100+50)
	        
	    def setShape(self,horc,screen):
	        self.val = horc
	        
	        if horc == Computer:
	            self.shape("blackchecker.gif") 
	        else:
	            self.shape("redchecker.gif") 
	        
	        self.drop(screen) 

	    def getOwner(self):
	        return self.val
	    
	    def clicked(self):
	        print(self.row,self.col)
	        
	    def drop(self,screen):
	        self.goto(self.col*100+50,0)
	        screen.tracer(1)
	        self.speed(5)
	        self.st()
	        self.goto(self.col*100+50,self.row*100+55)
	        self.goto(self.col*100+50,self.row*100+45)
	        self.goto(self.col*100+50,self.row*100+50)
	        screen.tracer(0)

	class Connect4Application(tkinter.Frame):      
	    def __init__(self, master=None):
	        super().__init__(master)
	        self.pack()
	        self.buildWindow()
	        self.running = False

	    def buildWindow(self):

	        self.master.title("Connect Four")

	        bar = tkinter.Menu(self.master)
	        fileMenu = tkinter.Menu(bar,tearoff=0)
	                
	        fileMenu.add_command(label="Exit",command=self.master.quit)

	        bar.add_cascade(label="File",menu=fileMenu)

	        self.master.config(menu=bar)

	        canvas = tkinter.Canvas(self,width=700,height=600)
	        canvas.pack(side=tkinter.LEFT)

	        theTurtle = turtle.RawTurtle(canvas)
	        theTurtle.ht()  
	        screen = theTurtle.getscreen()  
	        screen.setworldcoordinates(0,600,700,0)
	        screen.register_shape("blackchecker.gif")
	        screen.register_shape("redchecker.gif")
	        screen.tracer(0)
	        screen.bgcolor("yellow")
	        
	        theTurtle.width(5)
	        for k in range(6):
	            theTurtle.penup()
	            theTurtle.goto(k*100+100,0)
	            theTurtle.pendown()
	            theTurtle.goto(k*100+100,600)
	            
	        theTurtle.ht()
	            
	        screen.update()
	        
	        def checkStatus():
	            toOther.write("3\n")
	            toOther.flush()
	            
	            status = int(fromOther.readline().strip())
	            
	            if status == 1:
	                tkinter.messagebox.showinfo("Game Over", "I Won!!!!!")
	            elif status == 2:
	                tkinter.messagebox.showinfo("Game Over", "You Won!!!!!") 
	            elif status == 3:
	                 tkinter.messagebox.showinfo("Game Over", "It's a tie.")
	                 
	            #print("Status is ", status)
	            return status
	        
	        def ComputerTurn():
	            toOther.write("1\n")
	            toOther.flush()
	            status = int(fromOther.readline().strip())
	            #print("Computer Turn Other Status = ", status)
	            if status == 0:
	                move = int(fromOther.readline())
	                #print("Move is", move)
	                row = move // 7
	                col = move % 7
	                
	                matrix[row][col].setShape(Computer,screen)
	                screen.update()

	        def HumanTurn(x,y):
	            if self.running: 
	                return
	            
	            #status = checkStatus()
	            
	            #if status != 0:
	                #return
	            
	            self.running = True
	            col = int(x) // 100
	            
	            row = 5
	            while row >= 0 and matrix[row][col].isvisible():
	                row = row - 1
	            
	            if row < 0:
	                #Then we clicked in a column that was already full.
	                self.running = True
	                return 
	              
	            val = row * 7 + col
	            
	            # Do the Human Turn
	            toOther.write("2\n")
	            toOther.flush()
	            toOther.write(str(val) + "\n")
	            toOther.flush()
	            
	            status = fromOther.readline().strip()
	            #print("Status is ",status)
	            
	            matrix[row][col].setShape(Human,screen)
	            screen.update()
	            
	            # Check the status of the game
	            status = checkStatus()
	            
	            if status == 0:
	                # Do a Computer Turn
	                ComputerTurn()
	                checkStatus()
	            
	            self.running = False
	            
	    
	        matrix = []       
	        
	        for i in range(6):
	            row = []
	            for j in range(7):
	                t = Tile(canvas,i,j,self)
	                row.append(t)
	            matrix.append(row)
	            
	        screen.update()
	        screen.onclick(HumanTurn)

	        sideBar = tkinter.Frame(self,padx=5,pady=5, relief=tkinter.RAISED,borderwidth="5pt")
	        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
	        
	        def NewGame():
	            toOther.write("0\n")
	            toOther.flush()
	            status = int(fromOther.readline().strip())            
	    
	            for row in matrix:
	                for token in row:
	                    token.ht()
	                    
	            screen.update()
	                    
	        kb = tkinter.Button(sideBar,text="Pass",command=ComputerTurn)
	        kb.pack()  
	        
	        ng = tkinter.Button(sideBar,text="New Game",command=NewGame)
	        ng.pack()  
	        
	        
	        proc = subprocess.Popen(["clisp","c4.fas"],stdout=subprocess.PIPE, \
	            stdin=subprocess.PIPE,universal_newlines=True)
	        fromOther = proc.stdout
	        toOther = proc.stdin   
	        
	        # To write to the other program you should use commands like this
	        # toOther.write(val+"\n")
	        # Don't forget to flush the buffer
	        # toOther.flush()        
	        
	        # To read from the other program you write
	        # line = fromOther.readline().strip()        
	        


	def main():
	    root = tkinter.Tk()
	    animApp = Connect4Application(root)

	    animApp.mainloop()
	    print("Program Execution Completed.")
	    
	if __name__ == "__main__":
	    main()
	    
	    
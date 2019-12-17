.. _`turtlegraphicsappendix`:

Appendix F: The Turtle Class
--------------------------------

The `Python 3 Documentation
<http://docs.python.org/py3k>`_ site contains this and much more extensive documentation on the Python 3 language, including the `Library Reference 
<http://docs.python.org/py3k/library/index.html>`_ which contains this documentation. This appendix was generated from the Python help system by typing help(Turtle) in the Python interpreter after importing the turtle module.

.. 			.. include:: turtle.txt

.. include:: TurtleDoc.txt


.. class Turtle(RawTurtle)
..  |  RawTurtle auto-crating (scrolled) canvas.
..  |  
..  |  When a Turtle object is created or a function derived from some
..  |  Turtle method is called a TurtleScreen object is automatically created.
..  |  
..  |  Method resolution order:
..  |      Turtle
..  |      RawTurtle
..  |      TPen
..  |      TNavigator
..  |      builtins.object
..  |  
..  |  Methods defined here:
..  |  
..  |  __init__(self, shape='classic', undobuffersize=1000, visible=True)
..  |  
..  |  ----------------------------------------------------------------------
..  |  Methods inherited from RawTurtle:
..  |  
..  |  begin_fill(self)
..  |      Called just before drawing a shape to be filled.
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.color("black", "red")
..  |      >>> turtle.begin_fill()
..  |      >>> turtle.circle(60)
..  |      >>> turtle.end_fill()
..  |  
..  |  begin_poly(self)
..  |      Start recording the vertices of a polygon.
..  |      
..  |      No argument.
..  |      
..  |      Start recording the vertices of a polygon. Current turtle position
..  |      is first point of polygon.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.begin_poly()
..  |  
..  |  clear(self)
..  |      Delete the turtle's drawings from the screen. Do not move turtle.
..  |      
..  |      No arguments.
..  |      
..  |      Delete the turtle's drawings from the screen. Do not move turtle.
..  |      State and position of the turtle as well as drawings of other
..  |      turtles are not affected.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.clear()
..  |  
..  |  clearstamp(self, stampid)
..  |      Delete stamp with given stampid
..  |      
..  |      Argument:
..  |      stampid - an integer, must be return value of previous stamp() call.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.color("blue")
..  |      >>> astamp = turtle.stamp()
..  |      >>> turtle.fd(50)
..  |      >>> turtle.clearstamp(astamp)
..  |  
..  |  clearstamps(self, n=None)
..  |      Delete all or first/last n of turtle's stamps.
..  |      
..  |      Optional argument:
..  |      n -- an integer
..  |      
..  |      If n is None, delete all of pen's stamps,
..  |      else if n > 0 delete first n stamps
..  |      else if n < 0 delete last n stamps.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> for i in range(8):
..  |              turtle.stamp(); turtle.fd(30)
..  |      ...
..  |      >>> turtle.clearstamps(2)
..  |      >>> turtle.clearstamps(-2)
..  |      >>> turtle.clearstamps()
..  |  
..  |  clone(self)
..  |      Create and return a clone of the turtle.
..  |      
..  |      No argument.
..  |      
..  |      Create and return a clone of the turtle with same position, heading
..  |      and turtle properties.
..  |      
..  |      Example (for a Turtle instance named mick):
..  |      mick = Turtle()
..  |      joe = mick.clone()
..  |  
..  |  dot(self, size=None, \*color)
..  |      Draw a dot with diameter size, using color.
..  |      
..  |      Optional argumentS:
..  |      size -- an integer >= 1 (if given)
..  |      color -- a colorstring or a numeric color tuple
..  |      
..  |      Draw a circular dot with diameter size, using color.
..  |      If size is not given, the maximum of pensize+4 and 2*pensize is used.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.dot()
..  |      >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
..  |  
..  |  end_fill(self)
..  |      Fill the shape drawn after the call begin_fill().
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.color("black", "red")
..  |      >>> turtle.begin_fill()
..  |      >>> turtle.circle(60)
..  |      >>> turtle.end_fill()
..  |  
..  |  end_poly(self)
..  |      Stop recording the vertices of a polygon.
..  |      
..  |      No argument.
..  |      
..  |      Stop recording the vertices of a polygon. Current turtle position is
..  |      last point of polygon. This will be connected with the first point.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.end_poly()
..  |  
..  |  filling(self)
..  |      Return fillstate (True if filling, False else).
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.begin_fill()
..  |      >>> if turtle.filling():
..  |              turtle.pensize(5)
..  |      else:
..  |              turtle.pensize(3)
..  |  
..  |  get_poly(self)
..  |      Return the lastly recorded polygon.
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> p = turtle.get_poly()
..  |      >>> turtle.register_shape("myFavouriteShape", p)
..  |  
..  |  get_shapepoly(self)
..  |      Return the current shape polygon as tuple of coordinate pairs.
..  |      
..  |      No argument.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("square")
..  |      >>> turtle.shapetransform(4, -1, 0, 2)
..  |      >>> turtle.get_shapepoly()
..  |      ((50, -20), (30, 20), (-50, 20), (-30, -20))
..  |  
..  |  getpen = getturtle(self)
..  |      Return the Turtleobject itself.
..  |      
..  |      No argument.
..  |      
..  |      Only reasonable use: as a function to return the 'anonymous turtle':
..  |      
..  |      Example:
..  |      >>> pet = getturtle()
..  |      >>> pet.fd(50)
..  |      >>> pet
..  |      <turtle.Turtle object at 0x0187D810>
..  |      >>> turtles()
..  |      [<turtle.Turtle object at 0x0187D810>]
..  |  
..  |  getscreen(self)
..  |      Return the TurtleScreen object, the turtle is drawing  on.
..  |      
..  |      No argument.
..  |      
..  |      Return the TurtleScreen object, the turtle is drawing  on.
..  |      So TurtleScreen-methods can be called for that object.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> ts = turtle.getscreen()
..  |      >>> ts
..  |      <turtle.TurtleScreen object at 0x0106B770>
..  |      >>> ts.bgcolor("pink")
..  |  
..  |  getturtle(self)
..  |      Return the Turtleobject itself.
..  |      
..  |      No argument.
..  |      
..  |      Only reasonable use: as a function to return the 'anonymous turtle':
..  |      
..  |      Example:
..  |      >>> pet = getturtle()
..  |      >>> pet.fd(50)
..  |      >>> pet
..  |      <turtle.Turtle object at 0x0187D810>
..  |      >>> turtles()
..  |      [<turtle.Turtle object at 0x0187D810>]
..  |  
..  |  onclick(self, fun, btn=1, add=None)
..  |      Bind fun to mouse-click event on this turtle on canvas.
..  |      
..  |      Arguments:
..  |      fun --  a function with two arguments, to which will be assigned
..  |              the coordinates of the clicked point on the canvas.
..  |      num --  number of the mouse-button defaults to 1 (left mouse button).
..  |      add --  True or False. If True, new binding will be added, otherwise
..  |              it will replace a former binding.
..  |      
..  |      Example for the anonymous turtle, i. e. the procedural way:
..  |      
..  |      >>> def turn(x, y):
..  |              left(360)
..  |      
..  |      >>> onclick(turn) # Now clicking into the turtle will turn it.
..  |      >>> onclick(None)  # event-binding will be removed
..  |  
..  |  ondrag(self, fun, btn=1, add=None)
..  |      Bind fun to mouse-move event on this turtle on canvas.
..  |      
..  |      Arguments:
..  |      fun -- a function with two arguments, to which will be assigned
..  |             the coordinates of the clicked point on the canvas.
..  |      num -- number of the mouse-button defaults to 1 (left mouse button).
..  |      
..  |      Every sequence of mouse-move-events on a turtle is preceded by a
..  |      mouse-click event on that turtle.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.ondrag(turtle.goto)
..  |      
..  |      ### Subsequently clicking and dragging a Turtle will
..  |      ### move it across the screen thereby producing handdrawings
..  |      ### (if pen is down).
..  |  
..  |  onrelease(self, fun, btn=1, add=None)
..  |      Bind fun to mouse-button-release event on this turtle on canvas.
..  |      
..  |      Arguments:
..  |      fun -- a function with two arguments, to which will be assigned
..  |              the coordinates of the clicked point on the canvas.
..  |      num --  number of the mouse-button defaults to 1 (left mouse button).
..  |      
..  |      Example (for a MyTurtle instance named joe):
..  |      >>> class MyTurtle(Turtle):
..  |              def glow(self,x,y):
..  |                      self.fillcolor("red")
..  |              def unglow(self,x,y):
..  |                      self.fillcolor("")
..  |      
..  |      >>> joe = MyTurtle()
..  |      >>> joe.onclick(joe.glow)
..  |      >>> joe.onrelease(joe.unglow)
..  |      ### clicking on joe turns fillcolor red,
..  |      ### unclicking turns it to transparent.
..  |  
..  |  reset(self)
..  |      Delete the turtle's drawings and restore its default values.
..  |      
..  |              No argument.
..  |      ,
..  |              Delete the turtle's drawings from the screen, re-center the turtle
..  |              and set variables to the default values.
..  |      
..  |              Example (for a Turtle instance named turtle):
..  |              >>> turtle.position()
..  |              (0.00,-22.00)
..  |              >>> turtle.heading()
..  |              100.0
..  |              >>> turtle.reset()
..  |              >>> turtle.position()
..  |              (0.00,0.00)
..  |              >>> turtle.heading()
..  |              0.0
..  |  
..  |  settiltangle(self, angle)
..  |      Rotate the turtleshape to point in the specified direction
..  |      
..  |      Argument: angle -- number
..  |      
..  |      Rotate the turtleshape to point in the direction specified by angle,
..  |      regardless of its current tilt-angle. DO NOT change the turtle's
..  |      heading (direction of movement).
..  |      
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("circle")
..  |      >>> turtle.shapesize(5,2)
..  |      >>> turtle.settiltangle(45)
..  |      >>> stamp()
..  |      >>> turtle.fd(50)
..  |      >>> turtle.settiltangle(-45)
..  |      >>> stamp()
..  |      >>> turtle.fd(50)
..  |  
..  |  setundobuffer(self, size)
..  |      Set or disable undobuffer.
..  |      
..  |      Argument:
..  |      size -- an integer or None
..  |      
..  |      If size is an integer an empty undobuffer of given size is installed.
..  |      Size gives the maximum number of turtle-actions that can be undone
..  |      by the undo() function.
..  |      If size is None, no undobuffer is present.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.setundobuffer(42)
..  |  
..  |  shape(self, name=None)
..  |      Set turtle shape to shape with given name / return current shapename.
..  |      
..  |      Optional argument:
..  |      name -- a string, which is a valid shapename
..  |      
..  |      Set turtle shape to shape with given name or, if name is not given,
..  |      return name of current shape.
..  |      Shape with name must exist in the TurtleScreen's shape dictionary.
..  |      Initially there are the following polygon shapes:
..  |      'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
..  |      To learn about how to deal with shapes see Screen-method register_shape.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.shape()
..  |      'arrow'
..  |      >>> turtle.shape("turtle")
..  |      >>> turtle.shape()
..  |      'turtle'
..  |  
..  |  shapesize(self, stretch_wid=None, stretch_len=None, outline=None)
..  |      Set/return turtle's stretchfactors/outline. Set resizemode to "user".
..  |      
..  |      Optinonal arguments:
..  |         stretch_wid : positive number
..  |         stretch_len : positive number
..  |         outline  : positive number
..  |      
..  |      Return or set the pen's attributes x/y-stretchfactors and/or outline.
..  |      Set resizemode to "user".
..  |      If and only if resizemode is set to "user", the turtle will be displayed
..  |      stretched according to its stretchfactors:
..  |      stretch_wid is stretchfactor perpendicular to orientation
..  |      stretch_len is stretchfactor in direction of turtles orientation.
..  |      outline determines the width of the shapes's outline.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.resizemode("user")
..  |      >>> turtle.shapesize(5, 5, 12)
..  |      >>> turtle.shapesize(outline=8)
..  |  
..  |  shapetransform(self, t11=None, t12=None, t21=None, t22=None)
..  |      Set or return the current transformation matrix of the turtle shape.
..  |      
..  |      Optional arguments: t11, t12, t21, t22 -- numbers.
..  |      
..  |      If none of the matrix elements are given, return the transformation
..  |      matrix.
..  |      Otherwise set the given elements and transform the turtleshape
..  |      according to the matrix consisting of first row t11, t12 and
..  |      second row t21, 22.
..  |      Modify stretchfactor, shearfactor and tiltangle according to the
..  |      given matrix.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("square")
..  |      >>> turtle.shapesize(4,2)
..  |      >>> turtle.shearfactor(-0.5)
..  |      >>> turtle.shapetransform()
..  |      >>> (4.0, -1.0, -0.0, 2.0)
..  |  
..  |  shearfactor(self, shear=None)
..  |      Set or return the current shearfactor.
..  |      
..  |      Optional argument: shear -- number, tangent of the shear angle
..  |      
..  |      Shear the turtleshape according to the given shearfactor shear,
..  |      which is the tangent of the shear angle. DO NOT change the
..  |      turtle's heading (direction of movement).
..  |      If shear is not given: return the current shearfactor, i. e. the
..  |      tangent of the shear angle, by which lines parallel to the
..  |      heading of the turtle are sheared.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("circle")
..  |      >>> turtle.shapesize(5,2)
..  |      >>> turtle.shearfactor(0.5)
..  |      >>> turtle.shearfactor()
..  |      >>> 0.5
..  |  
..  |  stamp(self)
..  |      Stamp a copy of the turtleshape onto the canvas and return its id.
..  |      
..  |      No argument.
..  |      
..  |      Stamp a copy of the turtle shape onto the canvas at the current
..  |      turtle position. Return a stamp_id for that stamp, which can be
..  |      used to delete it by calling clearstamp(stamp_id).
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.color("blue")
..  |      >>> turtle.stamp()
..  |      13
..  |      >>> turtle.fd(50)
..  |  
..  |  tilt(self, angle)
..  |      Rotate the turtleshape by angle.
..  |      
..  |      Argument:
..  |      angle - a number
..  |      
..  |      Rotate the turtleshape by angle from its current tilt-angle,
..  |      but do NOT change the turtle's heading (direction of movement).
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("circle")
..  |      >>> turtle.shapesize(5,2)
..  |      >>> turtle.tilt(30)
..  |      >>> turtle.fd(50)
..  |      >>> turtle.tilt(30)
..  |      >>> turtle.fd(50)
..  |  
..  |  tiltangle(self, angle=None)
..  |      Set or return the current tilt-angle.
..  |      
..  |      Optional argument: angle -- number
..  |      
..  |      Rotate the turtleshape to point in the direction specified by angle,
..  |      regardless of its current tilt-angle. DO NOT change the turtle's
..  |      heading (direction of movement).
..  |      If angle is not given: return the current tilt-angle, i. e. the angle
..  |      between the orientation of the turtleshape and the heading of the
..  |      turtle (its direction of movement).
..  |      
..  |      Deprecated since Python 3.1
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.shape("circle")
..  |      >>> turtle.shapesize(5,2)
..  |      >>> turtle.tilt(45)
..  |      >>> turtle.tiltangle()
..  |      >>>
..  |  
..  |  turtlesize = shapesize(self, stretch_wid=None, stretch_len=None, outline=None)
..  |      Set/return turtle's stretchfactors/outline. Set resizemode to "user".
..  |      
..  |      Optinonal arguments:
..  |         stretch_wid : positive number
..  |         stretch_len : positive number
..  |         outline  : positive number
..  |      
..  |      Return or set the pen's attributes x/y-stretchfactors and/or outline.
..  |      Set resizemode to "user".
..  |      If and only if resizemode is set to "user", the turtle will be displayed
..  |      stretched according to its stretchfactors:
..  |      stretch_wid is stretchfactor perpendicular to orientation
..  |      stretch_len is stretchfactor in direction of turtles orientation.
..  |      outline determines the width of the shapes's outline.
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.resizemode("user")
..  |      >>> turtle.shapesize(5, 5, 12)
..  |      >>> turtle.shapesize(outline=8)
..  |  
..  |  undo(self)
..  |      undo (repeatedly) the last turtle action.
..  |      
..  |      No argument.
..  |      
..  |      undo (repeatedly) the last turtle action.
..  |      Number of available undo actions is determined by the size of
..  |      the undobuffer.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> for i in range(4):
..  |              turtle.fd(50); turtle.lt(80)
..  |      
..  |      >>> for i in range(8):
..  |              turtle.undo()
..  |  
..  |  undobufferentries(self)
..  |      Return count of entries in the undobuffer.
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> while undobufferentries():
..  |              undo()
..  |  
..  |  write(self, arg, move=False, align='left', font=('Arial', 8, 'normal'))
..  |      Write text at the current turtle position.
..  |      
..  |      Arguments:
..  |      arg -- info, which is to be written to the TurtleScreen
..  |      move (optional) -- True/False
..  |      align (optional) -- one of the strings "left", "center" or right"
..  |      font (optional) -- a triple (fontname, fontsize, fonttype)
..  |      
..  |      Write text - the string representation of arg - at the current
..  |      turtle position according to align ("left", "center" or right")
..  |      and with the given font.
..  |      If move is True, the pen is moved to the bottom-right corner
..  |      of the text. By default, move is False.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.write('Home = ', True, align="center")
..  |      >>> turtle.write((0,0), True)
..  |  
..  |  ----------------------------------------------------------------------
..  |  Data and other attributes inherited from RawTurtle:
..  |  
..  |  screens = []
..  |  
..  |  ----------------------------------------------------------------------
..  |  Methods inherited from TPen:
..  |  
..  |  color(self, \*args)
..  |      Return or set the pencolor and fillcolor.
..  |      
..  |      Arguments:
..  |      Several input formats are allowed.
..  |      They use 0, 1, 2, or 3 arguments as follows:
..  |      
..  |      color()
..  |          Return the current pencolor and the current fillcolor
..  |          as a pair of color specification strings as are returned
..  |          by pencolor and fillcolor.
..  |      color(colorstring), color((r,g,b)), color(r,g,b)
..  |          inputs as in pencolor, set both, fillcolor and pencolor,
..  |          to the given value.
..  |      color(colorstring1, colorstring2),
..  |      color((r1,g1,b1), (r2,g2,b2))
..  |          equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
..  |          and analogously, if the other input format is used.
..  |      
..  |      If turtleshape is a polygon, outline and interior of that polygon
..  |      is drawn with the newly set colors.
..  |      For mor info see: pencolor, fillcolor
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.color('red', 'green')
..  |      >>> turtle.color()
..  |      ('red', 'green')
..  |      >>> colormode(255)
..  |      >>> color((40, 80, 120), (160, 200, 240))
..  |      >>> color()
..  |      ('#285078', '#a0c8f0')
..  |  
..  |  down = pendown(self)
..  |      Pull the pen down -- drawing when moving.
..  |      
..  |      Aliases: pendown | pd | down
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pendown()
..  |  
..  |  fillcolor(self, \*args)
..  |      Return or set the fillcolor.
..  |      
..  |      Arguments:
..  |      Four input formats are allowed:
..  |        - fillcolor()
..  |          Return the current fillcolor as color specification string,
..  |          possibly in hex-number format (see example).
..  |          May be used as input to another color/pencolor/fillcolor call.
..  |        - fillcolor(colorstring)
..  |          s is a Tk color specification string, such as "red" or "yellow"
..  |        - fillcolor((r, g, b))
..  |          *a tuple* of r, g, and b, which represent, an RGB color,
..  |          and each of r, g, and b are in the range 0..colormode,
..  |          where colormode is either 1.0 or 255
..  |        - fillcolor(r, g, b)
..  |          r, g, and b represent an RGB color, and each of r, g, and b
..  |          are in the range 0..colormode
..  |      
..  |      If turtleshape is a polygon, the interior of that polygon is drawn
..  |      with the newly set fillcolor.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.fillcolor('violet')
..  |      >>> col = turtle.pencolor()
..  |      >>> turtle.fillcolor(col)
..  |      >>> turtle.fillcolor(0, .5, 0)
..  |  
..  |  hideturtle(self)
..  |      Makes the turtle invisible.
..  |      
..  |      Aliases: hideturtle | ht
..  |      
..  |      No argument.
..  |      
..  |      It's a good idea to do this while you're in the
..  |      middle of a complicated drawing, because hiding
..  |      the turtle speeds up the drawing observably.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.hideturtle()
..  |  
..  |  ht = hideturtle(self)
..  |      Makes the turtle invisible.
..  |      
..  |      Aliases: hideturtle | ht
..  |      
..  |      No argument.
..  |      
..  |      It's a good idea to do this while you're in the
..  |      middle of a complicated drawing, because hiding
..  |      the turtle speeds up the drawing observably.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.hideturtle()
..  |  
..  |  isdown(self)
..  |      Return True if pen is down, False if it's up.
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.penup()
..  |      >>> turtle.isdown()
..  |      False
..  |      >>> turtle.pendown()
..  |      >>> turtle.isdown()
..  |      True
..  |  
..  |  isvisible(self)
..  |      Return True if the Turtle is shown, False if it's hidden.
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.hideturtle()
..  |      >>> print turtle.isvisible():
..  |      False
..  |  
..  |  pd = pendown(self)
..  |      Pull the pen down -- drawing when moving.
..  |      
..  |      Aliases: pendown | pd | down
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pendown()
..  |  
..  |  pen(self, pen=None, \*\*pendict)
..  |      Return or set the pen's attributes.
..  |      
..  |      Arguments:
..  |          pen -- a dictionary with some or all of the below listed keys.
..  |          \*\*pendict -- one or more keyword-arguments with the below
..  |                       listed keys as keywords.
..  |      
..  |      Return or set the pen's attributes in a 'pen-dictionary'
..  |      with the following key/value pairs:
..  |         "shown"      :   True/False
..  |         "pendown"    :   True/False
..  |         "pencolor"   :   color-string or color-tuple
..  |         "fillcolor"  :   color-string or color-tuple
..  |         "pensize"    :   positive number
..  |         "speed"      :   number in range 0..10
..  |         "resizemode" :   "auto" or "user" or "noresize"
..  |         "stretchfactor": (positive number, positive number)
..  |         "shearfactor":   number
..  |         "outline"    :   positive number
..  |         "tilt"       :   number
..  |      
..  |      This dictionary can be used as argument for a subsequent
..  |      pen()-call to restore the former pen-state. Moreover one
..  |      or more of these attributes can be provided as keyword-arguments.
..  |      This can be used to set several pen attributes in one statement.
..  |      
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
..  |      >>> turtle.pen()
..  |      {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
..  |      'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
..  |      'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
..  |      >>> penstate=turtle.pen()
..  |      >>> turtle.color("yellow","")
..  |      >>> turtle.penup()
..  |      >>> turtle.pen()
..  |      {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
..  |      'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
..  |      'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
..  |      >>> p.pen(penstate, fillcolor="green")
..  |      >>> p.pen()
..  |      {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
..  |      'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
..  |      'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
..  |  
..  |  pencolor(self, \*args)
..  |      Return or set the pencolor.
..  |      
..  |      Arguments:
..  |      Four input formats are allowed:
..  |        - pencolor()
..  |          Return the current pencolor as color specification string,
..  |          possibly in hex-number format (see example).
..  |          May be used as input to another color/pencolor/fillcolor call.
..  |        - pencolor(colorstring)
..  |          s is a Tk color specification string, such as "red" or "yellow"
..  |        - pencolor((r, g, b))
..  |          *a tuple* of r, g, and b, which represent, an RGB color,
..  |          and each of r, g, and b are in the range 0..colormode,
..  |          where colormode is either 1.0 or 255
..  |        - pencolor(r, g, b)
..  |          r, g, and b represent an RGB color, and each of r, g, and b
..  |          are in the range 0..colormode
..  |      
..  |      If turtleshape is a polygon, the outline of that polygon is drawn
..  |      with the newly set pencolor.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pencolor('brown')
..  |      >>> tup = (0.2, 0.8, 0.55)
..  |      >>> turtle.pencolor(tup)
..  |      >>> turtle.pencolor()
..  |      '#33cc8c'
..  |  
..  |  pendown(self)
..  |      Pull the pen down -- drawing when moving.
..  |      
..  |      Aliases: pendown | pd | down
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pendown()
..  |  
..  |  pensize(self, width=None)
..  |      Set or return the line thickness.
..  |      
..  |      Aliases:  pensize | width
..  |      
..  |      Argument:
..  |      width -- positive number
..  |      
..  |      Set the line thickness to width or return it. If resizemode is set
..  |      to "auto" and turtleshape is a polygon, that polygon is drawn with
..  |      the same line thickness. If no argument is given, current pensize
..  |      is returned.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pensize()
..  |      1
..  |      turtle.pensize(10)   # from here on lines of width 10 are drawn
..  |  
..  |  penup(self)
..  |      Pull the pen up -- no drawing when moving.
..  |      
..  |      Aliases: penup | pu | up
..  |      
..  |      No argument
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.penup()
..  |  
..  |  pu = penup(self)
..  |      Pull the pen up -- no drawing when moving.
..  |      
..  |      Aliases: penup | pu | up
..  |      
..  |      No argument
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.penup()
..  |  
..  |  resizemode(self, rmode=None)
..  |      Set resizemode to one of the values: "auto", "user", "noresize".
..  |      
..  |      (Optional) Argument:
..  |      rmode -- one of the strings "auto", "user", "noresize"
..  |      
..  |      Different resizemodes have the following effects:
..  |        - "auto" adapts the appearance of the turtle
..  |                 corresponding to the value of pensize.
..  |        - "user" adapts the appearance of the turtle according to the
..  |                 values of stretchfactor and outlinewidth (outline),
..  |                 which are set by shapesize()
..  |        - "noresize" no adaption of the turtle's appearance takes place.
..  |      If no argument is given, return current resizemode.
..  |      resizemode("user") is called by a call of shapesize with arguments.
..  |      
..  |      
..  |      Examples (for a Turtle instance named turtle):
..  |      >>> turtle.resizemode("noresize")
..  |      >>> turtle.resizemode()
..  |      'noresize'
..  |  
..  |  showturtle(self)
..  |      Makes the turtle visible.
..  |      
..  |      Aliases: showturtle | st
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.hideturtle()
..  |      >>> turtle.showturtle()
..  |  
..  |  speed(self, speed=None)
..  |      Return or set the turtle's speed.
..  |      
..  |      Optional argument:
..  |      speed -- an integer in the range 0..10 or a speedstring (see below)
..  |      
..  |      Set the turtle's speed to an integer value in the range 0 .. 10.
..  |      If no argument is given: return current speed.
..  |      
..  |      If input is a number greater than 10 or smaller than 0.5,
..  |      speed is set to 0.
..  |      Speedstrings  are mapped to speedvalues in the following way:
..  |          'fastest' :  0
..  |          'fast'    :  10
..  |          'normal'  :  6
..  |          'slow'    :  3
..  |          'slowest' :  1
..  |      speeds from 1 to 10 enforce increasingly faster animation of
..  |      line drawing and turtle turning.
..  |      
..  |      Attention:
..  |      speed = 0 : *no* animation takes place. forward/back makes turtle jump
..  |      and likewise left/right make the turtle turn instantly.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.speed(3)
..  |  
..  |  st = showturtle(self)
..  |      Makes the turtle visible.
..  |      
..  |      Aliases: showturtle | st
..  |      
..  |      No argument.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.hideturtle()
..  |      >>> turtle.showturtle()
..  |  
..  |  up = penup(self)
..  |      Pull the pen up -- no drawing when moving.
..  |      
..  |      Aliases: penup | pu | up
..  |      
..  |      No argument
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.penup()
..  |  
..  |  width = pensize(self, width=None)
..  |      Set or return the line thickness.
..  |      
..  |      Aliases:  pensize | width
..  |      
..  |      Argument:
..  |      width -- positive number
..  |      
..  |      Set the line thickness to width or return it. If resizemode is set
..  |      to "auto" and turtleshape is a polygon, that polygon is drawn with
..  |      the same line thickness. If no argument is given, current pensize
..  |      is returned.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pensize()
..  |      1
..  |      turtle.pensize(10)   # from here on lines of width 10 are drawn
..  |  
..  |  ----------------------------------------------------------------------
..  |  Data descriptors inherited from TPen:
..  |  
..  |  __dict__
..  |      dictionary for instance variables (if defined)
..  |  
..  |  __weakref__
..  |      list of weak references to the object (if defined)
..  |  
..  |  ----------------------------------------------------------------------
..  |  Methods inherited from TNavigator:
..  |  
..  |  back(self, distance)
..  |      Move the turtle backward by distance.
..  |      
..  |      Aliases: back | backward | bk
..  |      
..  |      Argument:
..  |      distance -- a number
..  |      
..  |      Move the turtle backward by distance ,opposite to the direction the
..  |      turtle is headed. Do not change the turtle's heading.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 0.00)
..  |      >>> turtle.backward(30)
..  |      >>> turtle.position()
..  |      (-30.00, 0.00)
..  |  
..  |  backward = back(self, distance)
..  |      Move the turtle backward by distance.
..  |      
..  |      Aliases: back | backward | bk
..  |      
..  |      Argument:
..  |      distance -- a number
..  |      
..  |      Move the turtle backward by distance ,opposite to the direction the
..  |      turtle is headed. Do not change the turtle's heading.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 0.00)
..  |      >>> turtle.backward(30)
..  |      >>> turtle.position()
..  |      (-30.00, 0.00)
..  |  
..  |  bk = back(self, distance)
..  |      Move the turtle backward by distance.
..  |      
..  |      Aliases: back | backward | bk
..  |      
..  |      Argument:
..  |      distance -- a number
..  |      
..  |      Move the turtle backward by distance ,opposite to the direction the
..  |      turtle is headed. Do not change the turtle's heading.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 0.00)
..  |      >>> turtle.backward(30)
..  |      >>> turtle.position()
..  |      (-30.00, 0.00)
..  |  
..  |  circle(self, radius, extent=None, steps=None)
..  |      Draw a circle with given radius.
..  |      
..  |      Arguments:
..  |      radius -- a number
..  |      extent (optional) -- a number
..  |      steps (optional) -- an integer
..  |      
..  |      Draw a circle with given radius. The center is radius units above
..  |      the turtle; extent - an angle - determines which part of the
..  |      circle is drawn. If extent is not given, draw the entire circle.
..  |      If extent is not a full circle, one endpoint of the arc is the
..  |      current pen position. Draw the arc in counterclockwise direction
..  |      if radius is positive, otherwise in clockwise direction. Finally
..  |      the direction of the turtle is changed by the amount of extent.
..  |      
..  |      As the circle is approximated by an inscribed regular polygon,
..  |      steps determines the number of steps to use. If not given,
..  |      it will be calculated automatically. Maybe used to draw regular
..  |      polygons.
..  |      
..  |      call: circle(radius)                  # full circle
..  |      --or: circle(radius, extent)          # arc
..  |      --or: circle(radius, extent, steps)
..  |      --or: circle(radius, steps=6)         # 6-sided polygon
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.circle(50)
..  |      >>> turtle.circle(120, 180)  # semicircle
..  |  
..  |  degrees(self, fullcircle=360.0)
..  |      Set angle measurement units to degrees.
..  |      
..  |      Optional argument:
..  |      fullcircle -  a number
..  |      
..  |      Set angle measurement units, i. e. set number
..  |      of 'degrees' for a full circle. Dafault value is
..  |      360 degrees.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.left(90)
..  |      >>> turtle.heading()
..  |      90
..  |      
..  |      Change angle measurement unit to grad (also known as gon,
..  |      grade, or gradian and equals 1/100-th of the right angle.)
..  |      >>> turtle.degrees(400.0)
..  |      >>> turtle.heading()
..  |      100
..  |  
..  |  distance(self, x, y=None)
..  |      Return the distance from the turtle to (x,y) in turtle step units.
..  |      
..  |      Arguments:
..  |      x -- a number   or  a pair/vector of numbers   or   a turtle instance
..  |      y -- a number       None                            None
..  |      
..  |      call: distance(x, y)         # two coordinates
..  |      --or: distance((x, y))       # a pair (tuple) of coordinates
..  |      --or: distance(vec)          # e.g. as returned by pos()
..  |      --or: distance(mypen)        # where mypen is another turtle
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pos()
..  |      (0.00, 0.00)
..  |      >>> turtle.distance(30,40)
..  |      50.0
..  |      >>> pen = Turtle()
..  |      >>> pen.forward(77)
..  |      >>> turtle.distance(pen)
..  |      77.0
..  |  
..  |  fd = forward(self, distance)
..  |      Move the turtle forward by the specified distance.
..  |      
..  |      Aliases: forward | fd
..  |      
..  |      Argument:
..  |      distance -- a number (integer or float)
..  |      
..  |      Move the turtle forward by the specified distance, in the direction
..  |      the turtle is headed.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 0.00)
..  |      >>> turtle.forward(25)
..  |      >>> turtle.position()
..  |      (25.00,0.00)
..  |      >>> turtle.forward(-75)
..  |      >>> turtle.position()
..  |      (-50.00,0.00)
..  |  
..  |  forward(self, distance)
..  |      Move the turtle forward by the specified distance.
..  |      
..  |      Aliases: forward | fd
..  |      
..  |      Argument:
..  |      distance -- a number (integer or float)
..  |      
..  |      Move the turtle forward by the specified distance, in the direction
..  |      the turtle is headed.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 0.00)
..  |      >>> turtle.forward(25)
..  |      >>> turtle.position()
..  |      (25.00,0.00)
..  |      >>> turtle.forward(-75)
..  |      >>> turtle.position()
..  |      (-50.00,0.00)
..  |  
..  |  goto(self, x, y=None)
..  |      Move turtle to an absolute position.
..  |      
..  |      Aliases: setpos | setposition | goto:
..  |      
..  |      Arguments:
..  |      x -- a number      or     a pair/vector of numbers
..  |      y -- a number             None
..  |      
..  |      call: goto(x, y)         # two coordinates
..  |      --or: goto((x, y))       # a pair (tuple) of coordinates
..  |      --or: goto(vec)          # e.g. as returned by pos()
..  |      
..  |      Move turtle to an absolute position. If the pen is down,
..  |      a line will be drawn. The turtle's orientation does not change.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> tp = turtle.pos()
..  |      >>> tp
..  |      (0.00, 0.00)
..  |      >>> turtle.setpos(60,30)
..  |      >>> turtle.pos()
..  |      (60.00,30.00)
..  |      >>> turtle.setpos((20,80))
..  |      >>> turtle.pos()
..  |      (20.00,80.00)
..  |      >>> turtle.setpos(tp)
..  |      >>> turtle.pos()
..  |      (0.00,0.00)
..  |  
..  |  heading(self)
..  |      Return the turtle's current heading.
..  |      
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.left(67)
..  |      >>> turtle.heading()
..  |      67.0
..  |  
..  |  home(self)
..  |      Move turtle to the origin - coordinates (0,0).
..  |      
..  |      No arguments.
..  |      
..  |      Move turtle to the origin - coordinates (0,0) and set its
..  |      heading to its start-orientation (which depends on mode).
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.home()
..  |  
..  |  left(self, angle)
..  |      Turn turtle left by angle units.
..  |      
..  |      Aliases: left | lt
..  |      
..  |      Argument:
..  |      angle -- a number (integer or float)
..  |      
..  |      Turn turtle left by angle units. (Units are by default degrees,
..  |      but can be set via the degrees() and radians() functions.)
..  |      Angle orientation depends on mode. (See this.)
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.heading()
..  |      22.0
..  |      >>> turtle.left(45)
..  |      >>> turtle.heading()
..  |      67.0
..  |  
..  |  lt = left(self, angle)
..  |      Turn turtle left by angle units.
..  |      
..  |      Aliases: left | lt
..  |      
..  |      Argument:
..  |      angle -- a number (integer or float)
..  |      
..  |      Turn turtle left by angle units. (Units are by default degrees,
..  |      but can be set via the degrees() and radians() functions.)
..  |      Angle orientation depends on mode. (See this.)
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.heading()
..  |      22.0
..  |      >>> turtle.left(45)
..  |      >>> turtle.heading()
..  |      67.0
..  |  
..  |  pos(self)
..  |      Return the turtle's current location (x,y), as a Vec2D-vector.
..  |      
..  |      Aliases: pos | position
..  |      
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pos()
..  |      (0.00, 240.00)
..  |  
..  |  position = pos(self)
..  |      Return the turtle's current location (x,y), as a Vec2D-vector.
..  |      
..  |      Aliases: pos | position
..  |      
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pos()
..  |      (0.00, 240.00)
..  |  
..  |  radians(self)
..  |      Set the angle measurement units to radians.
..  |      
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.heading()
..  |      90
..  |      >>> turtle.radians()
..  |      >>> turtle.heading()
..  |      1.5707963267948966
..  |  
..  |  right(self, angle)
..  |      Turn turtle right by angle units.
..  |      
..  |      Aliases: right | rt
..  |      
..  |      Argument:
..  |      angle -- a number (integer or float)
..  |      
..  |      Turn turtle right by angle units. (Units are by default degrees,
..  |      but can be set via the degrees() and radians() functions.)
..  |      Angle orientation depends on mode. (See this.)
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.heading()
..  |      22.0
..  |      >>> turtle.right(45)
..  |      >>> turtle.heading()
..  |      337.0
..  |  
..  |  rt = right(self, angle)
..  |      Turn turtle right by angle units.
..  |      
..  |      Aliases: right | rt
..  |      
..  |      Argument:
..  |      angle -- a number (integer or float)
..  |      
..  |      Turn turtle right by angle units. (Units are by default degrees,
..  |      but can be set via the degrees() and radians() functions.)
..  |      Angle orientation depends on mode. (See this.)
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.heading()
..  |      22.0
..  |      >>> turtle.right(45)
..  |      >>> turtle.heading()
..  |      337.0
..  |  
..  |  seth = setheading(self, to_angle)
..  |      Set the orientation of the turtle to to_angle.
..  |      
..  |      Aliases:  setheading | seth
..  |      
..  |      Argument:
..  |      to_angle -- a number (integer or float)
..  |      
..  |      Set the orientation of the turtle to to_angle.
..  |      Here are some common directions in degrees:
..  |      
..  |       standard - mode:          logo-mode:
..  |      -------------------\|--------------------
..  |         0 - east                0 - north
..  |        90 - north              90 - east
..  |       180 - west              180 - south
..  |       270 - south             270 - west
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.setheading(90)
..  |      >>> turtle.heading()
..  |      90
..  |  
..  |  setheading(self, to_angle)
..  |      Set the orientation of the turtle to to_angle.
..  |      
..  |      Aliases:  setheading | seth
..  |      
..  |      Argument:
..  |      to_angle -- a number (integer or float)
..  |      
..  |      Set the orientation of the turtle to to_angle.
..  |      Here are some common directions in degrees:
..  |      
..  |       standard - mode:          logo-mode:
..  |      -------------------\|--------------------
..  |         0 - east                0 - north
..  |        90 - north              90 - east
..  |       180 - west              180 - south
..  |       270 - south             270 - west
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.setheading(90)
..  |      >>> turtle.heading()
..  |      90
..  |  
..  |  setpos = goto(self, x, y=None)
..  |      Move turtle to an absolute position.
..  |      
..  |      Aliases: setpos | setposition | goto:
..  |      
..  |      Arguments:
..  |      x -- a number      or     a pair/vector of numbers
..  |      y -- a number             None
..  |      
..  |      call: goto(x, y)         # two coordinates
..  |      --or: goto((x, y))       # a pair (tuple) of coordinates
..  |      --or: goto(vec)          # e.g. as returned by pos()
..  |      
..  |      Move turtle to an absolute position. If the pen is down,
..  |      a line will be drawn. The turtle's orientation does not change.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> tp = turtle.pos()
..  |      >>> tp
..  |      (0.00, 0.00)
..  |      >>> turtle.setpos(60,30)
..  |      >>> turtle.pos()
..  |      (60.00,30.00)
..  |      >>> turtle.setpos((20,80))
..  |      >>> turtle.pos()
..  |      (20.00,80.00)
..  |      >>> turtle.setpos(tp)
..  |      >>> turtle.pos()
..  |      (0.00,0.00)
..  |  
..  |  setposition = goto(self, x, y=None)
..  |      Move turtle to an absolute position.
..  |      
..  |      Aliases: setpos | setposition | goto:
..  |      
..  |      Arguments:
..  |      x -- a number      or     a pair/vector of numbers
..  |      y -- a number             None
..  |      
..  |      call: goto(x, y)         # two coordinates
..  |      --or: goto((x, y))       # a pair (tuple) of coordinates
..  |      --or: goto(vec)          # e.g. as returned by pos()
..  |      
..  |      Move turtle to an absolute position. If the pen is down,
..  |      a line will be drawn. The turtle's orientation does not change.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> tp = turtle.pos()
..  |      >>> tp
..  |      (0.00, 0.00)
..  |      >>> turtle.setpos(60,30)
..  |      >>> turtle.pos()
..  |      (60.00,30.00)
..  |      >>> turtle.setpos((20,80))
..  |      >>> turtle.pos()
..  |      (20.00,80.00)
..  |      >>> turtle.setpos(tp)
..  |      >>> turtle.pos()
..  |      (0.00,0.00)
..  |  
..  |  setx(self, x)
..  |      Set the turtle's first coordinate to x
..  |      
..  |      Argument:
..  |      x -- a number (integer or float)
..  |      
..  |      Set the turtle's first coordinate to x, leave second coordinate
..  |      unchanged.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 240.00)
..  |      >>> turtle.setx(10)
..  |      >>> turtle.position()
..  |      (10.00, 240.00)
..  |  
..  |  sety(self, y)
..  |      Set the turtle's second coordinate to y
..  |      
..  |      Argument:
..  |      y -- a number (integer or float)
..  |      
..  |      Set the turtle's first coordinate to x, second coordinate remains
..  |      unchanged.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.position()
..  |      (0.00, 40.00)
..  |      >>> turtle.sety(-10)
..  |      >>> turtle.position()
..  |      (0.00, -10.00)
..  |  
..  |  towards(self, x, y=None)
..  |      Return the angle of the line from the turtle's position to (x, y).
..  |      
..  |      Arguments:
..  |      x -- a number   or  a pair/vector of numbers   or   a turtle instance
..  |      y -- a number       None                            None
..  |      
..  |      call: distance(x, y)         # two coordinates
..  |      --or: distance((x, y))       # a pair (tuple) of coordinates
..  |      --or: distance(vec)          # e.g. as returned by pos()
..  |      --or: distance(mypen)        # where mypen is another turtle
..  |      
..  |      Return the angle, between the line from turtle-position to position
..  |      specified by x, y and the turtle's start orientation. (Depends on
..  |      modes - "standard" or "logo")
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> turtle.pos()
..  |      (10.00, 10.00)
..  |      >>> turtle.towards(0,0)
..  |      225.0
..  |  
..  |  xcor(self)
..  |      Return the turtle's x coordinate.
..  |      
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> reset()
..  |      >>> turtle.left(60)
..  |      >>> turtle.forward(100)
..  |      >>> print turtle.xcor()
..  |      50.0
..  |  
..  |  ycor(self)
..  |      Return the turtle's y coordinate
..  |      ---
..  |      No arguments.
..  |      
..  |      Example (for a Turtle instance named turtle):
..  |      >>> reset()
..  |      >>> turtle.left(60)
..  |      >>> turtle.forward(100)
..  |      >>> print turtle.ycor()
..  |      86.6025403784
..  |  
..  |  ----------------------------------------------------------------------
..  |  Data and other attributes inherited from TNavigator:
..  |  
..  |  DEFAULT_ANGLEOFFSET = 0
..  |  
..  |  DEFAULT_ANGLEORIENT = 1
..  |  
..  |  DEFAULT_MODE = 'standard'
..  |  
..  |  START_ORIENTATION = {'logo': (0.00,1.00), 'standard': (1.00,0.00), 'wo...



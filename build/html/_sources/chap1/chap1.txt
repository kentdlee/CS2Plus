--------------------------------------
Python Programming 101
--------------------------------------

This first chapter introduces Python to readers that have never programmed in Python before. It also provides instructions for installing Python on your computer. The Wing Integrated Development Environment (IDE) is recommended for students learning to program. Wing IDE 101 is the free version of the IDE for educational use. The chapter goes on to introduce classes, objects, and object-oriented programming by developing a drawing application using the Tkinter graphical user interface library.

An understanding of object-oriented programming concepts presented in this chapter is necessary before reading the rest of the text. The PyList datatype presented in this chapter is also used in subsequent chapters including chapter 2. Even if the reader has worked through an introductory text or has a basic understanding of Python, there are concepts from this first chapter that are used throughout the text.

The Dog Class
---------------

You can download the :download:`Dog class <files/dog.py>` by clicking here.

.. literalinclude:: files/dog.py
	:language: python
	:linenos:

The Variable Length Records Draw Program
----------------------------------------------

You can download the :download:`draw program with variable length records <files/drawWithVariableLengthRecords.py>` by clicking this link.

.. literalinclude:: files/drawWithVariableLengthRecords.py
	:language: python
	:linenos:

The Final XML Draw Program
----------------------------

You can download the :download:`final draw program with XML support <files/draw.py>` from Appendix H of the text by clicking this link.

.. literalinclude:: files/draw.py
	:language: python
	:linenos:

Figures from Text
-------------------

.. figure:: wingide1.png

  The Wing IDE

.. figure:: xref.png

  A Reference and Object

.. figure:: dogobjects.png

  A Couple of Dog Objects

+-------------------------+-------------+--------------------------------------------------------------------------------+
| Method Defintion        | Operator    | Description                                                                    |
+=========================+=============+================================================================================+
| __add__(self,y)         | x + y       |  The addition of two objects. The type of *x* determines                       |
|                         |             |  which add operator is called.                                                 |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __contains__(self,y)    | y in x      | When *x* is a collection you can test to see if *y* is in it.                  |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __eq__(self,y)          | x == y      | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __ge__(self,y)          | x >= y      | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __getitem__(self,y)     | x[y]        | Returns the item at the y\ :sup:`th` position in x.                            |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __gt__(self,y)          | x > y       | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __hash__(self)          | hash(x)     | Returns an integral value for *x*.                                             |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __int__(self)           | int(x)      | Returns an integer representation of *x*.                                      |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __iter__(self)          | for v in x  | Returns an iterator object for the sequence *x*.                               |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __le__(self,y)          | x <= y      | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __len__(self)           | len(x)      | Returns the size of *x* where *x* has some length attribute.                   |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __lt__(self,y)          | x < y       | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __mod__(self,y)         | x % y       | Returns the value of *x* modulo *y*. This is the remainder of *x/y*.           |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __mul__(self,y)         | x * y       | Returns the product of *x* and *y*.                                            |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __ne__(self,y)          | x != y      | Returns *True* or *False* depending on the values of *x* and *y*.              |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __neg__(self)           | -x          | Returns the unary negation of *x*.                                             |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __repr__(self)          | repr(x)     | Returns a string version of x suitable to be evaluated by the *eval* function. |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __setitem__(self,i,y)   | x[i] = y    | Sets the item at the i\ :sup:`th` position in *x* to *y*.                      |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __str__(self)           | str(x)      | Return a string representation of *x* suitable for user-level interaction.     |
+-------------------------+-------------+--------------------------------------------------------------------------------+
| __sub__(self,y)         | x - y       | The difference of two objects.                                                 |
+-------------------------+-------------+--------------------------------------------------------------------------------+

.. figure:: pixel.png

  Python Operator Magic Methods
  
.. figure:: blockindent.png

  Adjusting Indentation in Wing IDE 101

.. figure:: Draw.png

  The Draw Program

.. figure:: labelledGUI.png

  The Draw Program Layout

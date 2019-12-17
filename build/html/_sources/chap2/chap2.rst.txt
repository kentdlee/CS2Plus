.. _chap2:

--------------------------------------------------------
Computational Complexity
--------------------------------------------------------

In the last chapter we developed a drawing program. To hold the drawing commands we built the *PyList* container class which is a lot like the built-in Python list class, but helps illustrate our first data structure. When we added a drawing command to the sequence we called the append method. It turns out that this method is called a lot. In fact, the flower picture in the first chapter took around 700 commands to draw. You can imagine that a complex picture with lots of free-hand drawing could contain thousands of drawing commands. When creating a free-hand drawing we want to append the next drawing command to the sequence quickly because there are so many commands being appended. How long does it take to append a drawing command to the sequence? Can we make a guess? Should we care about the exact amount of time?

In this chapter you'll learn how to answer these questions and you'll learn what questions are important for you as a computer programmer. First you'll read about some principles of computer architecture to understand something about how long it takes a computer to do some simple operations. With that knowledge you'll have the tools you'll need to make informed decisions about how much time it might take to execute some code you have written.

The PlotData Program
---------------------

You can :download:`download <files/PlotData.py>` the program by clicking here. This program is used to plot data written in the plot XML format presented in the text. The next program, the list timing access program, writes data in the plot XML format.

.. literalinclude:: files/PlotData.py
	:language: python
	:linenos:

.. _listaccess:

List Access Timing
---------------------

You can :download:`download <files/listaccesstiming.py>`  the program by clicking here.

.. literalinclude:: files/listaccesstiming.py
	:language: python
	:linenos:

.. _pylist:

The PyList Datatype
----------------------

This is the chapter 2 version of this datatype. In chapter 4 another, more complete version of this datatype is described. You can :download:`download the chapter 2 version of the datatype<files/PyList.py>` by clicking here.

.. literalinclude:: files/PyList.py
	:language: python
	:linenos:

Figures from Text
-------------------

.. figure:: computer.png

	Conceptual View of a Computer

.. figure:: ListAccessTime800.png

	Access Times in a Python List

.. figure:: BigOh800.png

	An Upper Bound

.. figure:: appendgraphsmall.png

	The Complexity of Appending to a PyList

.. figure:: CommonComplexities800.png

	Common Big-Oh Complexities

.. figure:: Omega700.png

	A Lower and Upper Bound

.. figure:: mypylist.png

	Append Cyber Dollars

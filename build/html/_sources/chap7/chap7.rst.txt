.. _graphchap:

--------------------------------------
Graphs
--------------------------------------

Many problems in Computer Science and Mathematics can be reduced to a set of states and a set of transitions between these states. A graph is a mathematical representation of problems like these. In the last chapter we saw that trees serve a variety of purposes in Computer Science. Trees are graphs. However, graphs are more general than trees. Abstracting away the details of a problem and studying it in its simplest form often leads to new insight. As a result, many algorithms have come out of the research in graph theory. Graph theory was first studied by mathematicians. Many of the algorithms in graph theory are named for the mathematician that developed or discovered them. Dijkstra and Kruskal are two such mathematicians and this chapter covers algorithms developed by them.

Representing a graph can be done one of several different ways. The correct way to represent a graph depends on the algorithm being implemented. Graph theory problems include graph coloring, finding a path between two states or nodes in a graph, or finding a shortest path through a graph among many others. There are many algorithms that have come from the study of graphs. To understand the formulation of these problems it is good to learn a little graph notation which is presented in this chapter as well.

Drawing Graphs
-----------------

This chapter contains several graph algorithms. Visualizing these graphs can be a challenge. Some of the pictures in the text were drawn from XML formatted files. The XML format was described in the chapter. Here are a few examples of these graph XML files.

	* :download:`graph.xml <files/graph.xml>`
	* :download:`directedgraph.xml <files/directedgraph.xml>`
	* :download:`neiowagraph.xml <files/neiowagraph.xml>`

These graphs can be drawn using turtle graphis. You can :download:`download <files/drawgraph.py>` the drawgraph.py program to draw graphs in this XML format.

There is also a very nice drawing program for Mac OS X called OmniGraffle. Most of the figures in the text were drawn with OmniGraffle. OmniGraffle saves its graphs in XML format as well. We have written a program to convert an OmniGraffle drawing of a graph to the XML format supported by the drawgraph.py program. You can :download:`download <files/graphreader.py>` the graphreader.py program here. These programs are available *As-Is* for educational use. No support is provided for using them. The graphreader.py program happens to be a nice example of using dictionaries in a program.

Figures from Text
-------------------------

.. figure:: undirectedgraph.png

	An Undirected Graph

.. figure:: directedgraph.png

	A Directed Graph

.. figure:: neiowagraph.png

	A Weighted, Undirected Graph

.. figure:: graphdfs.png

	A Path from Vertex 0 to Vertex 1

.. figure:: kruskal.png

	A Minimum Weighted Spanning Tree

.. figure:: forest1.png

	Kruskal's: Snapshot 1

.. figure:: forest2.png

	Kruskal's: Snapshot 2

.. figure:: dijkstra.png

	Minimum Cost Paths and Total Cost from Source Vertex 0

.. figure:: weighteddirected.png

	A Sample Weighted, Directed Graph

	

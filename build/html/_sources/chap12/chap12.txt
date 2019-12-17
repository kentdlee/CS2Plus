.. _chap12:

-------------------------
Heuristic Search
-------------------------

This text has focused on the interaction of algorithms with data structures. Many of the algorithms presented in this text deal with search and how to organize data so searching can be done efficiently. Many problems involve searching for an answer among many possible solutions, not all of which are correct. Sometimes, there are so many possibilities, no algorithm can be written that will efficiently find a correct solution amongst all the possible solutions. In these cases, we may be able to use a *rule of thumb*, most often called a *heuristic* in computer science, to eliminate some of these possibilities from our search space. If the *heuristic* does not eliminate possible solutions, it may at least help us order the possible solutions so we look at *better* possible solutions first, whatever *better* might mean.

In :ref:`graphchap` depth first search of a graph was presented. Sometimes search spaces for graphs or other problems grow to such an enormous size, it is impossible to blindly search for a goal node. This is where a heuristic can come in handy. This chapter uses searching a maze, which is really just a type of graph, as an example to illustrate several search algorithms that are related to depth first or breadth first search. Several applications of these search algorithms are also presented or discussed.

Heuristic search is often covered in texts on Artificial Intelligence :cite:`AIIlluminated`. As problems in AI are better understood, algorithms arise that become more commonplace over time. The heuristic algorithms presented in this chapter are covered in more detail in an AI text, but as data sizes grow, heuristic search will become more and more necessary in all sorts of applications. AI techniques may be useful in many search problems and so are covered in this chapter to provide an introduction to search algorithms designed to deal with large or infinite search spaces.

Searching Mazes
------------------

You can write your own maze search code that interacts with a front-end that is provided here. You can :download:`download <files/mazeanimate.py>` the front-end code by clicking here. The front-end code requires the :download:`tile20.gif<files/tile20.gif>` file. It also requires at least one maze file. The file maze3.txt was used in the text to demonstrate the various search algorithms. Here are three maze files for downloading.

	* :download:`maze.txt<files/maze.txt>`
	* :download:`maze2.txt<files/maze2.txt>`
	* :download:`maze3.txt<files/maze3.txt>`

Of course, you can write your own maze file as well. The format requires the number of rows on the first line, followed by the number of columns on the second line. Then the rest of the maze on the following lines must have an opening at the top for the entrance and an opening at the bottom for the exit.

The program is written as a front-end. Your challenge is to provide a back-end that supports the given search types. The architecture for your back-end is described at the top of the front-end code. The front-end is written to support five types of search, depth-first, bread-first, hill climbing, best-first, and a-star. If you wish to see a demonstration of these search types without writing your own back-end code first, you can :download:`download <files/search.fas>` the search.fas file which is a compiled CLISP back-end. You must have CLISP installed on your system to run this back-end code.

Here is the front-end code for your reference.

.. literalinclude:: files/mazeanimate.py
    :language: python
    :linenos:


N-Queens Problem
-------------------

The N-Queens problem from the text can be solved using a depth first search with forward checking. A front-end program is provided so you can visualize the search for a solution. You can :download:`download<files/queensanimate.py>` the front-end code here.

The program is written as a front-end. Your challenge is to write the back-end code for this program. The architecture for your back-end is described at the top of the front-end code.
If you wish to visualize how this program works without writing your own back-end, you can :download:`download<files/qsearch.fas>` the qsearch.fas file here. This file requires CLISP be installed to run. The qsearch.fas file must be placed in the same directory as the front-end queensanimate.py program to run.

Here is the front-end code for your reference.

.. literalinclude:: files/queensanimate.py
    :language: python
    :linenos:

Connect Four
--------------------------

The connect four game presented in the text, like the other two program presented here, is written as a front-end/back-end pair. The front-end code can be :download:`downloaded<files/c4.py>` here. The front-end requires the :download:`redchecker.gif<files/redchecker.gif>` and the :download:`blackchecker<files/blackchecker.gif>` files be in the same directory.

Your challenge is to write the back-end code for this program that beats the author's back-end code. The architecture for your back-end is described at the top of the front-end code.
If you wish to run this program works without writing your own back-end, you can :download:`download<files/c4.fas>` the c4.fas file here. This file requires CLISP be installed to run. The c4.fas file must be placed in the same directory as the front-end c4.py program to run.

Here is the front-end code for your reference.

.. literalinclude:: files/c4.py
    :language: python
    :linenos:

Figures from Text
-------------------

.. figure:: mazedfsannotated.png

	Depth First Search of a Maze

.. figure:: mazebfs.png

	Breadth First Search of a Maze

.. figure:: mazehill.png

	Hill Climbing Search of a Maze

.. figure:: knighttour.png

	A Closed 12 x 12 Knight's Tour

.. figure:: nqueens.png

	A 25-Queens Solution

.. figure:: mazebestfirst.png

	Best First Search of a Maze

.. figure:: mazeastar.png

	A-Star Search of a Maze

.. figure:: connect4.png

	The Connect Four Game

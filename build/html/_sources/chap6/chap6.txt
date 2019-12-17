.. _chap6:

--------------------------------------
Trees
--------------------------------------

When we see a tree in our everyday lives the roots are generally in the ground and the leaves are up in the air. The branches of a tree spread out from the roots in a more or less organized fashion. The word *tree* is used in Computer Science when talking about a way data may be organized. Trees have some similarilties to the linked list organization found in :ref:`chap4`. In a tree there are nodes which have links to other nodes. In a linked list each node has one link, to the next node in the list. In a tree each node may have two or more links to other nodes. A tree is not a sequential data structure. It is organized like a tree, except the root is at the top of tree data structures and the leaves are at the bottom. A tree in computer science is usually drawn inverted when compared to the trees we see in nature. There are many uses for trees in computer science.

In this chapter we'll explore trees and when it makes sense to build and or use a tree in a program. Not every program will need a tree data structure. Nevertheless, trees are used in many types of programs. A knowledge of them is not only a necessity, proper use of them can greatly simplify some types of programs.

Abstract Syntax Trees
----------------------

You can :download:`download <files/ast.py>` prefix expression parser and abstract syntax tree code here. You must have access to the :ref:`queue code from chapter 4<queuecode>` to run this program.

.. literalinclude:: files/ast.py
    :language: python
    :linenos:

Binary Search Trees
---------------------

You can :download:`download <files/binarysearchtree.py>` binary search tree code here.

.. literalinclude:: files/binarysearchtree.py
    :language: python
    :linenos:

Sudoku Test Files
--------------------
Here are two more sudoku test files. These can be solved if you implement the depth first search as described in  chapter 6 of the text.

	* :download:`sudoku7.txt <files/sudoku7.txt>`
	* :download:`sudoku8.txt <files/sudoku8.txt>`

OrderedTreeSet
----------------

Here is an :download:`OrderedTreeSet <files/orderedtreeset.py>` implementation to get you started with the ordered tree set implementation. This file has an OrderedTreeSet class with a BinarySearchTree class nested inside it.

 .. literalinclude:: files/orderedtreeset.py
    :language: python
    :linenos:

OrderedTreeSet Test Program
---------------------------

Here is an :download:`OrderedTreeSet Test Program <files/orderedtreesettest.py>` that provides some tests for the OrderedTreeSet implementation. Your ordered tree set must be saved in a file called orderedtreeset.py so it can be imported into this test program.

 .. literalinclude:: files/orderedtreesettest.py
    :language: python
    :linenos:

Figures from Text
-------------------

.. figure:: ../chap5/fib.png

  The Call Tree for Computing Fib(5)

.. figure:: ast.png

  The AST for (5 + 4) * 6 + 3

.. figure:: binarysearchtree8.png

  An empty BinarySearchTree object

.. figure:: binarysearchtree7.png

  The Tree After Inserting 5

.. figure:: binarysearchtree6.png

  The Tree After Inserting 8

.. figure:: binarysearchtree5.png

  The Tree After Inserting 2

.. figure:: binarysearchtree4.png

  The Tree After Inserting 1

.. figure:: binarysearchtree3.png

  The Tree After Inserting 4

.. figure:: binarysearchtree2.png

  The Tree After Inserting 9

.. figure:: binarysearchtree1.png

  The Tree After Inserting 6

.. figure:: binarysearchtree.png

  The Tree After Inserting 7

.. figure:: binarysearchtreefinal.png

  The Final BinarySearchTree Contents

.. figure:: binarysearchtreedelete0.png

  The Tree After Deleting 9

.. figure:: binarysearchtreedelete1.png

  The Tree After Deleting 6

.. figure:: binarysearchtreedelete2.png

  The Tree After Deleting 5

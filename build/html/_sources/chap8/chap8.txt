.. _heapchap:

--------------------------------------
Heaps
--------------------------------------

The word *heap* is used in a couple of different contexts in Computer Science. A heap sometimes refers to an area of memory used for dynamic (i.e. run-time) memory allocation. Another meaning, and the topic of this chapter, is a data structure that is conceptually a complete binary tree. Heaps are used in implementing priority queues, the heapsort algorithm, and some graph algorithms. Heaps are somewhat like binary search trees in that they maintain an ordering of the items within the tree. However, a heap does not maintain a complete ordering of its items. This has some implications for how a heap may be used.

Heap Program
-------------------------------

Here you can :download:`download <files/heap.py>` a starter shell for the heap implementation described in the chapter.
To run this program you must also :download:`download <files/person.py>` the person.py file. Place both modules in the same directory. The heap.py program file contains a main function to test your heap implementation.

This heap program can be modified to support a different number of children. For instance, a four child heap is also possible. The file defaults to a three child heap.

.. literalinclude:: files/heap.py
    :language: python
    :linenos:

Figures from Text
---------------------

.. figure:: heap1.png

  Heap Shape

.. figure:: heap2.png

  Sample Heap

.. figure:: heap3.png

  Heap Organization

.. figure:: heap4.png

  Building a Heap Part One

.. figure:: heap5.png

  Building a Heap Part Two

.. figure:: heap6.png

  Building a Heap Part Three

.. figure:: heap7.png

  Adding 98 to the Heap

.. figure:: heap8.png

  Conceptual View While Adding 98 to the Heap

.. figure:: heap9.png

  Heap After Moving 98 to Correct Location

.. figure:: heap10.png

  A Perfect Binary Tree

.. figure:: logplot.png

  Plot of log(n)

.. figure:: heap11.png

  Just Before Phase II

.. figure:: heap12.png

  After Swapping First and Last Values

.. figure:: heap13.png

  After the First Pass of Phase II

.. figure:: heap14.png

  After the Second Pass of Phase II

.. figure:: heap15.png

  After the Third Pass of Phase II

.. figure:: heap16.png

  After the Fourth and Final Pass of Phase II

.. figure:: heap17.png

  A List to be Heapsorted

.. figure:: heap18.png

  After Forming a Sub-Heap

.. figure:: heap19.png

  After Forming a Second Sub-Heap

.. figure:: heap20.png

  Sifting the 15 Down

.. figure:: heap21.png

  The Final Heap using Version 2 of Phase I

.. figure:: heap22.png

  A Binary Heap of Height 4

.. figure:: timinggraph.png

  Comparison of Several Sorting Algorithms

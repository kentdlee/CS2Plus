.. _chap4:

--------------------------------------------------------
Sequences
--------------------------------------------------------

Computers are really good at dealing with large amounts of information. They can repeat a task over and over again without getting bored. When they repeat a task they are generally doing the same thing to similar data or objects. It is natural to want to organize those objects into some kind of structure so that our program can easily switch from one object to the next. How objects are added to a sequence or collection and how we move from one item to the next has some impact on how we might want to organize the collection of data in a program.

In this chapter we look at different ways of organizing data into a sequence. We'll also examine how to use Python to make working with sequences convenient. Operator overloading in Python lets us build sequences that we can manipulate with intuitive operations. Finally, we also examine how the organization of a sequence affects the computation complexity of operations on it.


.. _ch4pylist:

The PyList Datatype
-------------------------

You can :download:`download<files/PyList.py>` the complete PyList datatype by clicking here.

.. literalinclude:: files/PyList.py
    :language: python
    :linenos:

The Sort Animation
---------------------

You can :download:`download <files/SortAnimation.py>` the complete sort animation by clicking here. You can also get source code for selection sort, merge sort, and quicksort from this animation program.

.. literalinclude:: files/SortAnimation.py
    :language: python
    :linenos:


Tic Tac Toe
------------------------------

You can :download:`download <files/tictactoe.py>` the starter code for Tic Tac Toe by clicking here.

.. literalinclude:: files/tictactoe.py
    :language: python
    :linenos:


The Linked List Datatype
------------------------

You can :download:`download <files/linkedlist.py>` the code for the linked list datatype by clicking here.

.. literalinclude:: files/linkedlist.py
    :language: python
    :linenos:

The Stack Datatype
-------------------

You can :download:`download <files/stack.py>` the code for the stack datatype by clicking here.

.. literalinclude:: files/stack.py
    :language: python
    :linenos:

.. _queuecode:

The Queue Datatype
-------------------

You can :download:`download <files/queue.py>` the code for the queue datatype by clicking here.

.. literalinclude:: files/queue.py
    :language: python
    :linenos:

Figures from Text
---------------------

+---------------+-------------+---------------+-------------------+
|   Operation   | Complexity  |    Usage      |       Method      |
+===============+=============+===============+===================+
| List creation | O(n) or O(1)| x = list(y)   | calls __init__(y) |
+---------------+-------------+---------------+-------------------+
| indexed get   | O(1)        | a = x[i]      | x.__getitem__(i)  |
+---------------+-------------+---------------+-------------------+
| indexed set   | O(1)        | x[i] = a      | x.__setitem__(i,a)|
+---------------+-------------+---------------+-------------------+
| concatenate   | O(n)        | z = x + y     | z = x.__add__(y)  |
+---------------+-------------+---------------+-------------------+
| append        | O(1)        | x.append(a)   | x.append(a)       |
+---------------+-------------+---------------+-------------------+
| insert        | O(n)        | x.insert(i,e) | x.insert(i,e))    |
+---------------+-------------+---------------+-------------------+
| delete        | O(n)        | del x[i]      | x.__delitem__(i)  |
+---------------+-------------+---------------+-------------------+
| equality      | O(n)        | x == y        | x.__eq__(y)       |
+---------------+-------------+---------------+-------------------+
| iterate       | O(n)        | for a in x:   | x.__iter__()      |
+---------------+-------------+---------------+-------------------+
| length        | O(1)        | len(x)        | x.__len__()       |
+---------------+-------------+---------------+-------------------+
| membership    | O(n)        | a in x        | x.__contains__(a) |
+---------------+-------------+---------------+-------------------+
| sort          | O(n log n)  | x.sort()      | x.sort()          |
+---------------+-------------+---------------+-------------------+

.. figure:: ../chap1/pixel.png

  Complexity of List Operations

.. figure:: samplelist.png

  A Sample PyList Object

.. figure:: selectionsort700.png

  Selection Sort Snapshot

.. figure:: selectionsortpic.png

  Selection Sort of a List

.. figure:: mergesort.png

  Merge Sort Snapshot

.. figure:: merge.png

  Merge Sort Merges

.. figure:: quicksort.png

  Quicksort Snapshot

.. figure:: quicksortpic.png

  Quicksorting a List

.. figure:: matrix.png

  A 2-Dimensional Matrix

.. figure:: samplelinkedlist.png

  A Sample LinkedList Object

+---------------+-------------+---------------------+-------------------+
|   Operation   | Complexity  |    Usage            |       Method      |
+===============+=============+=====================+===================+
| List creation | O(n) or O(1)| x = LinkedList(y)   | calls __init__(y) |
+---------------+-------------+---------------------+-------------------+
| indexed get   | O(n)        | a = x[i]            | x.__getitem__(i)  |
+---------------+-------------+---------------------+-------------------+
| indexed set   | O(n)        | x[i] = a            | x.__setitem__(i,a)|
+---------------+-------------+---------------------+-------------------+
| concatenate   | O(n)        | z = x + y           | z = x.__add__(y)  |
+---------------+-------------+---------------------+-------------------+
| append        | O(1)        | x.append(a)         | x.append(a)       |
+---------------+-------------+---------------------+-------------------+
| insert        | O(n)        | x.insert(i,e)       | x.insert(i,e))    |
+---------------+-------------+---------------------+-------------------+
| delete        | O(n)        | del x[i]            | x.__delitem__(i)  |
+---------------+-------------+---------------------+-------------------+
| equality      | O(n)        | x == y              | x.__eq__(y)       |
+---------------+-------------+---------------------+-------------------+
| iterate       | O(n)        | for a in x:         | x.__iter__()      |
+---------------+-------------+---------------------+-------------------+
| length        | O(1)        | len(x)              | x.__len__()       |
+---------------+-------------+---------------------+-------------------+
| membership    | O(n)        | a in x              | x.__contains__(a) |
+---------------+-------------+---------------------+-------------------+
| sort          | N/A         | N/A                 | N/A               |
+---------------+-------------+---------------------+-------------------+

.. figure:: ../chap1/pixel.png

  Complexity of LinkedList Operations

.. figure:: deleteitemlinkedlist.png

  Deleting a Node from a Linked List

+---------------+-------------+---------------+-----------------------------------------------------+
|   Operation   | Complexity  |    Usage      |       Description                                   |
+===============+=============+===============+=====================================================+
| Stack Creation| O(1)        | s=Stack()     | calls the constructor                               |
+---------------+-------------+---------------+-----------------------------------------------------+
| pop           | O(1)        | a=s.pop()     | returns the last item pushed and removes it from s  |
+---------------+-------------+---------------+-----------------------------------------------------+
| push          | O(1)        | s.push(a)     | pushes the item, a, on the stack, s                 |
+---------------+-------------+---------------+-----------------------------------------------------+
| top           | O(1)        | a=s.top()     | returns the top item without popping s              |
+---------------+-------------+---------------+-----------------------------------------------------+
| isEmpty       | O(1)        | s.isEmpty()   | returns True if s has no pushed items               |
+---------------+-------------+---------------+-----------------------------------------------------+

.. figure:: ../chap1/pixel.png

  Complexity of Stack Operations

+---------------+-------------+------------------+-------------------------------------------------------+
|   Operation   | Complexity  |    Usage         |       Description                                     |
+===============+=============+==================+=======================================================+
| Queue Creation| O(1)        | q=Queue()        | calls the constructor                                 |
+---------------+-------------+------------------+-------------------------------------------------------+
| dequeue       | O(1)        | a=q.dequeue()    | returns the first item enqueued and removes it from q |
+---------------+-------------+------------------+-------------------------------------------------------+
| enqueue       | O(1)        | q.enqueue(a)     | enqueues the item, a, on the queue, q                 |
+---------------+-------------+------------------+-------------------------------------------------------+
| front         | O(1)        | a=q.front()      | returns the front item without dequeueing the item    |
+---------------+-------------+------------------+-------------------------------------------------------+
| isEmpty       | O(1)        | q.isEmpty()      | returns True if q has not enqueued items              |
+---------------+-------------+------------------+-------------------------------------------------------+

.. figure:: ../chap1/pixel.png

  Complexity of Queue Operations


.. figure:: infix1.png

  Infix Evaluation Step 1

.. figure:: infix2.png

  Infix Evaluation Step 2

.. figure:: infix3.png

  Infix Evaluation Step 3

.. figure:: radixsort1.png

  Radix Sort Step 1

.. figure:: radixsort2.png

  Radix Sort Step 2

.. figure:: radixsort3.png

  Radix Sort Step 3

.. figure:: radixsort4.png

  Radix Sort Step 4 - 3rd letter

.. figure:: radixsort5.png

  Radix Sort Step 5

.. figure:: radixsort6.png

  Radix Sort Step 6 - 2nd letter

.. figure:: radixsort5.png

  Radix Sort Step 7

.. figure:: radixsort7.png

  Radix Sort Step 8 - 1st letter

.. figure:: radixsort8.png

  Radix Sort Step 9

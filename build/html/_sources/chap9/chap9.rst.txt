.. _balancedtreechap:

--------------------------------------
Balanced Binary Search Trees
--------------------------------------

In :ref:`chap6` binary search trees were defined along with a recursive insert algorithm. The discussion of binary search trees pointed out they have problems in some cases. Binary search trees can become unbalanced, actually quite often. When a tree is unbalanced the complexity of insert, delete, and lookup operations can get as bad as :math:`\Theta(n)`. This problem with unbalanced binary search trees was the motivation for the development of height-balanced AVL trees by G. M. Adelson-Velskii and E. M. Landis, two Soviet computer scientists, in 1962. AVL trees were named for these two inventors. Their paper on AVL trees :cite:`avltrees` described the first algorithm for maintaining balanced binary search trees. The chapter goes on to discuss Splay Trees as another example of balanced binary search trees.

AVL Tree Implementations
---------------------------

AVL trees maintain their own balance. The balance can be maintained in one of two ways. Either the height of each node in the tree can be maintained or the balance of each node in the tree can be maintained. If maintaining the height, there is a little more work to be done to adjust heights all the way up the tree. If balance is maintained then the code gets a little trickier, but there balances only need to be adjusted up to a pivot node.

In addition, AVL trees can be implemented with recursive or iterative *insert* and *delete* methods. Both are described in the text.

Iteratively Implemented AVL Tree
==================================

You can :download:`download<files/avltree.py>` avltree.py to work on an iterative implementation of AVL Trees.

.. literalinclude:: files/avltree.py
    :language: python
    :linenos:

Recursively Implemented AVL Tree
===================================

AVL trees may also be implemented recursively meaning that the insert and delete methods can be written recursively. The outline of this implementation can be seen in the text. It is relatively short and is not provided for download.

Splay Tree Implementations
-----------------------------

Splay trees do not maintain the balance or height. Instead they rely on rotations that always rotate a inserted or accessed element to the root of the tree. In doing this they maintain a balance in the tree, often exploiting spatial locality. Again, splay trees may be implemented recursively or iteratively.

Iteratively Implemented Splay Tree
====================================

You can :download:`download<files/splaytree.py>` splaytree.py to work on an iterative implementation of splay trees. To run this program you will need to :download:`download <../chap4/files/stack.py>` stack.py module and you'll need to :download:`download <../chap8/files/person.py>` person.py module.

.. literalinclude:: files/splaytree.py
    :language: python
    :linenos:

Recursively Implemented Splay Tree
==================================

A recursive implementation of splay trees relies on keeping track of the left or right double rotations as the recursive insert or lookup returns up the tree. To accomplish this you must call a rotate function. Calling *rotate["RL"](pivot)* would call the rotate right then left double rotation. The *rotate* variable is a dictionary (i.e. hash table) in the code provided here.

You can :download:`download <files/splay.py>` splay.py file to begin working on the recursive splay tree implementation.

.. literalinclude:: files/splay.py
    :language: python
    :linenos:

Figures from Text
---------------------

.. figure:: avlcase1.png

  AVL Tree Case 1 - No Pivot Node

.. figure:: avlcase2.png

  AVL Tree Case 2 - No Rotate

.. figure:: avlcase3a.png

  AVL Tree Case 3A - Single Rotation

.. figure:: avlcase3b.png

  AVL Tree Case 3B - Double Rotation

.. figure:: avlcase3bstep1.png

  AVL Tree Case 3B Step 1 Rotate Toward

.. figure:: avlcase3bstep2.png

  AVL Tree Case 3B Step 2 Rotate Away

.. figure:: rotateright.png

  AVL Tree Case 3A Right Rotation

.. figure:: rotateleft.png

  AVL Tree Case 3A Left Rotation

.. figure:: rotate3BStep1and2.png

  AVL Tree Case 3B Steps 1 and 2

.. figure:: splayrightright.png

  Splay Tree Double-Right Rotate

.. figure:: splayleftleft.png

  Splay Tree Double-Left Rotate

.. figure:: splayrightleft.png

  Splay Tree Right-Left Rotate

.. figure:: splayleftright.png

  Splay Tree Left-Right Rotate

.. figure:: splaysample.png

  Splay Tree Example

.. figure:: InsertLookupAverage.png

  Average Insert/Lookup Time

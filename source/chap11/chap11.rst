.. _chap11:

--------------------------------------
Membership Structures
--------------------------------------

In :ref:`setsmaps` we studied data structures that support insertion, deletion, membership testing, and iteration. For some applications testing membership may be enough. Iteration and deletion may not be necessary. The classic example is that of a spell checker. Consider the job of a spell checker. A simple one may detect errors in spelling while a more advanced spell checker may suggest alternatives of *correctly* spelled words.

Clearly a spell checker is provided with a large dictionary of words. Using the list of words the spell checker determines whether a word you have is in the dictionary and therefore a correct word. If the word does not appear in the dictionary the word processor or editor may underline the word indicating it may be incorrectly spelled. In some cases the word processor may suggest an alternative, correctly spelled word. In some cases, the word processor may simply correct the mispelling. How do these spell checkers/correctors work? What kind of data structures do they use?

An English Dictionary
-----------------------

You can :download:`download <files/wordsEn.txt>` an English dictionary of words by clicking this link.

Figures from Text
----------------------

.. figure:: bloom1.png

  An Empty Bloom Filter

.. figure:: bloom2.png

  After Inserting *cow* into the Bloom Filter

.. figure:: bloom3.png

  After inserting *cow*, *cat*, *dog* into the Bloom Filter

.. figure:: trie.png

  After inserting *cow*, *cat*, *dog* into a Trie

  

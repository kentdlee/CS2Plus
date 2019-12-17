'''
  File:  avltree.py 
  Author: Steve Hubbard,  and 
  Date:  
  Description:  This module provides the AVLNode and AVLTree classes.
'''

from person import Person
from stack import Stack

class AVLNode:
   def __init__(self, item, balance = 0):
      self.item = item
      self.left = None
      self.right = None
      self.balance = balance
      
   def __str__(self):
      '''  This performs an inorder traversal of the tree rooted at self, 
         using recursion.  Return the corresponding string.
      '''
      st = str(self.item) + ' ' + str(self.balance) + '\n'
      if self.left != None:
         st = str(self.left) +  st  # A recursive call: str(self.left)
      if self.right != None:
         st = st + str(self.right)  # Another recursive call
      return st
   
   def rotateLeft(self):
      '''  Perform a left rotation of the subtree rooted at the
       receiver.  Answer the root node of the new subtree.  
      '''
      child = self.right
      if (child == None):
         print( 'Error!  No right child in rotateLeft.' )
         return None  # redundant
      else:
         self.right = child.left
         child.left = self
         return child

   def rotateRight(self):
      '''  Perform a right rotation of the subtree rooted at the
       receiver.  Answer the root node of the new subtree.  
      '''
      child = self.left
      if (child == None):
         print( 'Error!  No left child in rotateRight.' )
         return None  # redundant
      else:
         self.left = child.right
         child.right = self
         return child

   def rotateRightThenLeft(self):
      '''Perform a double inside left rotation at the receiver.  We
       assume the receiver has a right child (the bad child), which has a left 
       child. We rotate right at the bad child then rotate left at the pivot 
       node, self. Answer the root node of the new subtree.  We call this 
       case 3, subcase 2.
      '''
      pass
      
   def rotateLeftThenRight(self):
      '''Perform a double inside right rotation at the receiver.  We
       assume the receiver has a left child (the bad child) which has a right 
       child. We rotate left at the bad child, then rotate right at 
       the pivot, self.  Answer the root node of the new subtree. We call this 
       case 3, subcase 2.
      '''
      pass
   
class AVLTree:
   def __init__(self):
      self.root = None
      self.count = 0
      
   def __str__(self):
      st = 'There are ' + str(self.count) + ' nodes in the AVL tree.\n'
      return  st + str(self.root)  # Using the string hook for AVL nodes
   
   def insert(self, newItem):
      '''  Add a new node with item newItem, if there is not a match in the 
        tree.  Perform any rotations necessary to maintain the AVL tree, 
        including any needed updates to the balances of the nodes.  Most of the 
        actual work is done by other methods.
      '''
      pass

   def adjustBalances(self, theStack, pivot, newItem):
      '''  We adjust the balances of all the nodes in theStack, up to and
         including the pivot node, if any.  Later rotations may cause
         some of the balances to change.
      '''
      pass         
      
   def case1(self, theStack, pivot, newItem):
      '''  There is no pivot node.  Adjust the balances of all the nodes
         in theStack.
      '''
      self.adjustBalances(theStack, pivot, newItem)
            
   def case2(self, theStack, pivot, newItem):
      ''' The pivot node exists.  We have inserted a new node into the
         subtree of the pivot of smaller height.  Hence, we need to adjust 
         the balances of all the nodes in the stack up to and including 
         that of the pivot node.  No rotations are needed.
      '''
      self.adjustBalances(theStack, pivot, newItem)
            
   def case3(self, theStack, pivot, newItem):
      '''  The pivot node exists.  We have inserted a new node into the
         larger height subtree of the pivot node.  Hence rebalancing and 
         rotations are needed.
      '''
      self.adjustBalances(theStack, pivot, newItem)
      # Lots more!!!!
         
   def search(self, newItem):
      '''  The AVL tree is not empty.  We search for newItem. This method will 
        return a tuple: (pivot, theStack, parent, found).  
        In this tuple, if there is a pivot node, we return a reference to it 
        (or None). We create a stack of nodes along the search path -- theStack. 
        We indicate whether or not we found an item which matches newItem.  We 
        also return a reference to the last node the search examined -- referred
        to here as the parent.  (Note that if we find an object, the parent is 
        reference to that matching node.)  If there is no match, parent is a 
        reference to the node used to add a child in insert().
      '''
      pass
            
            
def main():
   print("Our names are ")
   print()
   a = AVLNode(20, -1)
   b = AVLNode( 30, -1)
   c = AVLNode(-100)
   d = AVLNode(290)
   '''
   print(a)
   print(b)
   '''
   t = AVLTree()
   t.root = b
   b.left = a
   a.left = c
   b.right = d
   t.count = 4
   print(t)
              
   a = AVLNode(50)
   b = AVLNode(30)
   c = AVLNode(40)
   a.left = b
   b.right = c
   print("Testing rotateLeftThenRight()")
   print(a.rotateLeftThenRight())
              
   (pivot, theStack, parent, found) = t.search(-70)
   print(pivot.item, parent.item, found)
   print()
   print("The items in the nodes of the stack are: ")
   while not theStack.isEmpty():
      current = theStack.pop()
      print(current.item)
   print()

   (pivot, theStack, parent, found) = t.search(25)
   print(pivot.item, parent.item, found)
   
   (pivot, theStack, parent, found) = t.search(-100)
   print(pivot.item, parent.item, found)
   
if __name__ == '__main__': main()
'''  The output from main():
[evaluate avltree.py]
Our names are
There are 4 nodes in the AVL tree.
-100 0
20 -1
30 -1
290 0

Testing rotateLeftThenRight()
30 0
40 0
50 0

20 -100 False

The items in the nodes of the stack are: 
-100
20
30

20 20 False
20 -100 True
'''

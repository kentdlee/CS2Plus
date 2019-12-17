'''
 File: splaytree.py
 Author(s): Steve Hubbard and 
 Date: 9/17/13
 Description: This module implements the SplayTree class and the
   SplayNode class.  The classes use bottom up splaying rather than 
   top down splaying.  We do not allow duplicate objects in the tree.
'''

from person import Person
from copy import deepcopy
from stack import Stack

class SplayNode:
   ''' This module implements the SplayNode class. This
     class in turn is used by the SplayTree class.  The classes
     use bottom up splaying rather than top down splaying.  We
     do not allow duplicate objects in the tree.
   '''
   
   def __init__(self, item, left = None, right = None):
      self.left = left
      self.item = item
      self.right = right

   def __str__(self): 
      st = '('
      if (self.left == None):
         st += '*'
      else:
         st += str(self.left) # recursion
      st += str(self.item)
      if (self.right == None):
         st += '*'
      else:
         st += str(self.right) # recursion
      st += ')'
      return st
   
   def inorder(self):
      ''' Perform an inorder traversal of the subtree rooted at
        the receiver.  Print each item in this subtree during
        the traversal.  This is done with recursion.
      '''
      pass
      
   def insertInNode(self, anItem):
      ''' Try to insert a copy of anItem into the bottom up splay
       tree rooted at the receiver.  If anItem is already in the tree,
       do not insert an extra copy. In any case, splay the new node,
       or the last node on the search path, to the root.  The method
       will answer a tuple.  The first element is True or False
       according to whether a new element was added or not.  The
       second element is the new root node.
       '''
       pass
   
   def rotateLeft(self):
      '''  Perform a left rotation of the subtree rooted at the
       receiver.  Answer the root node of the new subtree.  
      '''
      child = self.right
      if (child == None):
         print( 'Error!  No right child in rotateLeft. ' )
         return None  # redundant
      else:
         self.right = child.left
         child.left = self
         return child

   def splayToRoot(self, stack):
      '''  Perform a bottom up splay beginning at the node at the
       top of the stack.  Answer the root of the new tree.
      '''
      pass
      
   '''  Many more methods! '''
      

class SplayTree:
   
   def __init__(self):
      self.size = 0
      self.root = None

   def __str__(self):
      if self.root != None:
         return str(self.root)
      else:
         return ""
   
   def delete(self, anItem):
      '''  Atempt to find a match (==) for anItem in the receiver.
      If found, splay the corresponding node to the root and answer
      the item of the node. If not found, splay the last node on
      the search path to the root. In this case, answer None.  If
      found, we remove the node and make the largest element of the
      new left subtree (from the splaying of the node to the root
      position) the new root node of the tree.  Of course finding
      the largest element uses a splaying on that left subtree.
      If there is no left subtree, the right subtree becomes the
      root.  This may leave us with an empty tree.  If found,
      decrement the size of the tree and answer the item deleted.
      If not found, answer None.
      '''
      pass

   def findMax(self):
      ''' Find the largest element in the splay tree.  Splay that
      element to the root.  Answer a deep copy of the element.
      If the tree is empty, answer None.
      '''
      pass 

   def findMin(self):
      ''' Find the smallest element in the splay tree.  Splay that
      element to the root.  Answer a deep copy of the element.  If
      the tree is empty, answer None.
      '''
      if (self.root == None):
         return None
      self.root = self.root.findMin()
      return deepcopy(self.root.getItem())

   def getSize(self):
      return self.size

   def inorder(self):
      ''' Print the contents of the receiver, in inorder.
        Print one item per line.
      '''
      if self.root != None:
         self.root.inorder()

   def insert(self, anItem):
      ''' Insert a deep copy of anItem into the bottom up splay tree.
      If anItem is already present in the tree, do not insert a new 
      copy of anItem.  If anItem is added, increment the size of
      the receiver.  In either case, we splay from
      the last node.  If anItem was added, answer anItem.  If not,
      answer None.
      '''
      pass
         
   def retrieve(self, anItem):
      pass

   def update(self, anItem):
      pass


def main():
   
   print('My name is ')
   print('Test the SplayNode class: ')
   
   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   x = c.rotateLeft()
   print( x )
   print( str(x) == '((((*10*)20(*25*))30(*35*))40(*45*))' )
   print( '' )

   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   x = c.rotateRight()
   print( x )
   print( str(x) == '((*10*)20((*25*)30((*35*)40(*45*))))' )
   print( '' )
   
   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   print( root )
   print( '' )

   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   x = root.rotateRightThenLeft()
   print( x )
   print( str(x) ==  \
   '(((((*10*)20(*25*))30((*35*)40(*45*)))50(*55*))60((*65*)70((*80*)90(*100*))))' )
   print( '' )

   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   x = root.rotateLeftThenRight()
   print( x )
   print( str(x) ==  \
   '((((*10*)20(*25*))30(*35*))40((*45*)50(((*55*)60(*65*))70((*80*)90(*100*)))))' )
   print( '' )

   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   x = root.doubleRotateLeft()
   print( x )
   print( str(x) ==  \
   '((((((*10*)20(*25*))30((*35*)40(*45*)))50((*55*)60(*65*)))70(*80*))90(*100*))' )
   print( '' )
   
   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   x = root.doubleRotateRight()
   print( x )
   print( str(x) == \
   '((*10*)20((*25*)30(((*35*)40(*45*))50(((*55*)60(*65*))70((*80*)90(*100*))))))' )
   print( '' )
   
   a = SplayNode(20, SplayNode(10), SplayNode(25))
   b = SplayNode(40, SplayNode(35), SplayNode(45))
   c = SplayNode(30, a, b)
   d = SplayNode(60, SplayNode(55), SplayNode(65))
   e = SplayNode(90, SplayNode(80), SplayNode(100))
   f = SplayNode(70, d, e)
   root = SplayNode(50, c, f)
   x = root.find(35)
   print( x )
   print( str(x) == \
   '((((*10*)20(*25*))30*)35((*40(*45*))50(((*55*)60(*65*))70((*80*)90(*100*)))))')

   print('Test the SplayTree class: ')
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   print( str(t) == '(*1(((*2(*3*))4(*5*))6(*7*)))')
   print( 'The size of the tree is ' + str(t.getSize()) )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.findMin()
   print( str(t) ==  '(*1(((*2(*3*))4(*5*))6(*7*)))')
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   t.delete(3)
   print( str(t) ==  '((*1*)2((*4(*5*))6(*7*)))' )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.retrieve(1)
   t.delete(3)
   t.findMax()
   print( str(t) == '((((*1*)2(*4(*5*)))6*)7*)')

   t = SplayTree()
   t.insert(Person('Joe', 25))
   t.insert(Person('Jill',35))
   t.insert(Person('Jon',15))
   t.insert(Person('Jack',25))
   t.insert(Person('John',30))
   t.insert(Person('Jud',95))
   t.insert(Person('Joey',27))
   st = str(t) + '\n'
   t.update(Person('James', 25))
   st += str(t) + '\n'
   x = t.retrieve(Person('',15))
   st += str(x) + '\n'
   st += str(t) + '\n'
   x = t.delete(Person('', 35))
   st += str(x) + '\n'
   st += str(t) + '\n'
   x = t.findMax()
   st += str(x) + '\n'
   st += str(t) + '\n'
   print( t )

   print( 'The size of the tree is ' + str(t.getSize()) )

   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.insert(3.5)
   print( str(t) == '((((*1*)2*)3*)3.5(((*4*)5(*6*))7*))' )
   
   t = SplayTree()
   t.insert(1)
   t.insert(2)
   t.insert(3)
   t.insert(4)
   t.insert(5)
   t.insert(6)
   t.insert(7)
   t.insert(3.5)
   t.delete(3.5)
   print( str(t) == '(((*1*)2*)3(((*4*)5(*6*))7*))')
   print( 'The size of the tree is ' + str(t.getSize()) )
   

   t = SplayTree()
   t.insert(3)
   t.insert(2)
   t.insert(1)
   t.delete(1)
   print( 'The size of the tree is ' + str(t.getSize()) )

   t = SplayTree()
   t.insert(Person('Joe', 25))
   t.insert(Person('Jill',35))
   t.insert(Person('Jon',15))
   t.insert(Person('Jack',25))
   t.insert(Person('John',30))
   t.insert(Person('Jud',95))
   t.insert(Person('Joey',27))
   t.inorder()
      
if __name__ == '__main__': main()

''' Output, from splaytree.py, wrapped around!
[evaluate splaytree.py]
My name is 
Test the SplayNode class: 
((((*10*)20(*25*))30(*35*))40(*45*))
True

((*10*)20((*25*)30((*35*)40(*45*))))
True

((((*10*)20(*25*))30((*35*)40(*45*)))50(((*55*)60(*65*))70((*80*)90(*100*))))

(((((*10*)20(*25*))30((*35*)40(*45*)))50(*55*))60((*65*)70((*80*)90(*100*))))
True

((((*10*)20(*25*))30(*35*))40((*45*)50(((*55*)60(*65*))70((*80*)90(*100*)))))
True

((((((*10*)20(*25*))30((*35*)40(*45*)))50((*55*)60(*65*)))70(*80*))90(*100*))
True

((*10*)20((*25*)30(((*35*)40(*45*))50(((*55*)60(*65*))70((*80*)90(*100*))))))
True

((((*10*)20(*25*))30*)35((*40(*45*))50(((*55*)60(*65*))70((*80*)90(*100*)))))
True
Test the SplayTree class: 
True
The size of the tree is 7
True
True
True
((((*Name: Jon Id: 15 (*Name: James Id: 25 *))Name: Joey Id: 27 *)
                                   Name: John Id: 30 *)Name: Jud Id: 95 *)
The size of the tree is 5
True
True
The size of the tree is 7
The size of the tree is 2
Name: Jon Id: 15 
Name: Joe Id: 25 
Name: Joey Id: 27 
Name: John Id: 30 
Name: Jill Id: 35 
Name: Jud Id: 95 

'''
   
      
   
      

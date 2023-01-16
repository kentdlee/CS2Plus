'''
 File: splay.py
 Author: Kent D. Lee
 Date: 8/21/2014
 Description: This module implements the SplayTree class. This
   class uses the SplayNode class.  The classes
   use bottom up splaying rather than top down splaying.  We
   do not allow duplicate objects in the tree.

   Delete is not implemented in this file currently. Test code
   should be added to thoroughly test insert, lookup, and delete. 
   Recall that looking up a value rotates it to the root. Deleting 
   an item rotates its parent to the root. 
'''

def rotateLeft(pivot):
   pass

def rotateRight(pivot):
   pass

def rotateRL(pivot):
   pass

def rotateLR(pivot):
   pass

def rotateRR(pivot):
   pass

def rotateLL(pivot):
   pass

rotate = {}
rotate["RL"] = rotateRL
rotate["LR"] = rotateLR
rotate["RR"] = rotateRR
rotate["LL"] = rotateLL

singleRotate = {}
singleRotate["R"] = rotateRight
singleRotate["L"] = rotateLeft

class SplayTree:

   class SplayNode:
      def __init__(self, item, left=None, right=None):
         self.item = item
         self.left = left
         self.right = right
         
      def __str__(self):
         st = '('
         if (self.left == None):
            st += '*'
         else:
            st += str(self.left)
         st += str(self.item)
         if (self.right == None):
            st += '*'
         else:
            st += str(self.right)
         st += ')'
         return st

   def __init__(self):
      self.root = None
      self.rString = ""


   # Pass searching = True if just searching and not 
   # really inserting. If the item is found, true is 
   # returned. If the item is not found, an exception
   # containing false is raised. 

   def insert(self,item,searching=False):

      def __insert(root,item):
         ''' return the new root after inserting
             item into the tree currently rooted at 
             root. If searching for the value and not 
             inserting, then raise Exception(False) if 
             the item is not found. 
         '''

         return root

      self.found = False

      self.root = __insert(self.root,item)

      # Handle any single rotation that must 
      # be done after inserting the value. 
      if self.rString in singleRotate:
         self.root = singleRotate[self.rString](self.root)

      self.rString = ""

      return self.found

   def lookup(self,item):

      try:
         return self.insert(item,True)
      except Exception as inst:
         if inst.args[0] == False:
            return False

         raise Exception(inst)
            
   def __str__(self):
      if self.root != None:
         return str(self.root)
      else:
         return ""

def main():
   # This should print the following.
   #(*20*)
   #((*20*)30*)
   #(*5(*20(*30*)))
   #((*5*)8(*20(*30*)))
   #(((*5*)8((*20*)30*))42*)
   #(((*5*)8*)15((*20(*30*))42*))
   #(((*5*)8*)10(*15((*20(*30*))42*)))   
   t = SplayTree2()
   t.insert(20)
   print(str(t))
   t.insert(30)
   print(str(t))
   t.insert(5)
   print(str(t))
   t.insert(8)
   print(str(t))
   t.insert(42)
   print(str(t))
   t.insert(15)
   print(str(t))
   t.insert(10)   
   print(str(t))


if __name__ == '__main__': main()

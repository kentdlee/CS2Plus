from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime
import time
import sys

screenMin = 0
screenMax = 300
Human = -1
Computer = 1  

class Board:
    # When a board is constructed, you may want to make a copy of the board.
    # This can be a shallow copy of the board because Turtle objects are 
    # Immutable from the perspective of a board object. 
    def __init__(self, board=None, screen=None):
        self.screen = screen
        if screen == None: 
            if board!=None:
                self.screen = board.screen
                
        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if board==None:
                    rowlst.append(Dummy())
                else:
                    rowlst.append(board[i][j])
                
            self.items.append(rowlst)
     
    # Accessor method for the screen
    def getscreen(self):
        return self.screen
    
    # The getitem method is used to index into the board. It should 
    # return a row of the board. That row itself is indexable (it is just 
    # a list) so accessing a row and column in the board can be written
    # board[row][column] because of this method.
    def __getitem__(self,index):
        return self.items[index]
                
    # This method should return true if the two boards, self and other,
    # represent exactly the same state. 
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def __eq__(self,other):
        pass
    
    # This method will mutate this board to contain all dummy 
    # turtles. This way the board can be reset when a new game
    # is selected. It should NOT be used except when starting
    # a new game. 
    def reset(self):
        
        self.screen.tracer(1)
        for i in range(3):
            for j in range(3):
                self.items[i][j].goto(-100,-100)
                self.items[i][j] = Dummy()
                
        self.screen.tracer(0)
        
    # This method should return an integer representing the 
    # state of the board. If the computer has won, return 1.
    # If the human has won, return -1. Otherwise, return 0.
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def eval(self):
        pass

    # This method should return True if the board 
    # is completely filled up (no dummy turtles). 
    # Otherwise, it should return False.
    # READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
    def full(self):
        pass
    
    # This method should draw the X's and O's
    # Of this board on the screen. 
    def drawXOs(self):
        
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col*100+50,row*100+50)
        
        self.screen.update()        

# This class is just for placeholder objects when no move has been made
# yet at a position in the board. Having eval() return 0 is convenient when no
# move has been made. 
class Dummy:
    def __init__(self):
        pass
    
    def eval(self):
        return 0
    
    def goto(self,x,y):
        pass
    
# In the X and O classes below the constructor begins by initializing the 
# RawTurtle part of the object with the call to super().__init__(canvas). The
# super() call returns the class of the superclass (the class above the X or O
# in the class hierarchy). In this case, the superclass is RawTurtle. Then, 
# calling __init__ on the superclass initializes the part of the object that is
# a RawTurtle. 
class X(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.getscreen().register_shape("X",((-40,-36),(-40,-44),(0,-4),(40,-44),(40,-36), \
                             (4,0),(40,36),(40,44),(0,4),(-40,44),(-40,36),(-4,0),(-40,-36)))
        self.shape("X")
        self.penup()
        self.speed(5)
        self.goto(-100,-100)  
        
    def eval(self):
        return Computer
    
class O(RawTurtle):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.ht()
        self.shape("circle")
        self.penup()
        self.speed(5)
        self.goto(-100,-100)
        
    def eval(self):
        return Human

# The minimax function is given a player (1 = Computer, -1 = Human) and a
# board object. When the player = Computer, minimax returns the maximum 
# value of all possible moves that the Computer could make. When the player =
# Human then minimax returns the minimum value of all possible moves the Human
# could make. Minimax works by assuming that at each move the Computer will pick
# its best move and the Human will pick its best move. It does this by making a 
# move for the player whose turn it is, and then recursively calling minimax. 
# The base case results when, given the state of the board, someone has won or 
# the board is full.    
# READER EXERCISE: YOU MUST COMPLETE THIS FUNCTION
def minimax(player,board):
    pass

      

class TicTacToe(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()    
        self.paused = False
        self.stop = False
        self.running = False
        self.turn = Human
        self.locked = False
 
    def buildWindow(self):
        
        cv = ScrolledCanvas(self,600,600,600,600)
        cv.pack(side = tkinter.LEFT)
        t = RawTurtle(cv)
        screen = t.getscreen()
        screen.tracer(100000)
    
        screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
        screen.bgcolor("white")
        t.ht()
            
        frame = tkinter.Frame(self)
        frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
        board = Board(None, screen)
    
        def drawGrid():
            screen.clear()
            screen.tracer(1000000)
            screen.setworldcoordinates(screenMin,screenMin,screenMax,screenMax)
            screen.bgcolor("white")
            screen.tracer(0)
            t = RawTurtle(cv)
            t.ht()
            t.pu()
            t.width(10)
            t.color("green")
            for i in range(2):
                t.penup()
                t.goto(i*100+100,10)
                t.pendown()
                t.goto(i*100+100,290)
                t.penup()
                t.goto(10,i*100+100)
                t.pendown()
                t.goto(290,i*100+100)
    
            screen.update()
    
    
        def newGame():
            #drawGrid()
            self.turn = Human
            board.reset()
            self.locked =False
            screen.update()
    
      
        def startHandler():
            newGame()
            
        drawGrid()
    
        startButton = tkinter.Button(frame, text = "New Game", command=startHandler)
        startButton.pack()  
        
        def quitHandler():
            self.master.quit()
            
        quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
        quitButton.pack()
    
        def computerTurn():
            # The locked variable prevents another event from being 
            # processed while the computer is making up its mind. 
            self.locked = True
	    
            # Call Minimax to find the best move to make.
            # READER EXERCISE: YOU MUST COMPLETE THIS CODE
            # After writing this code, the maxMove tuple should
            # contain the best move for the computer. For instance,
            # if the best move is in the first row and third column
            # then maxMove would be (0,2).
	    
            row, col = maxMove
            board[row][col] = X(cv)
            self.locked = False
    
      
        def mouseClick(x,y):
            if not self.locked:
                row = int(y // 100)
                col = int(x // 100)
    
                if board[row][col].eval() == 0:
                    board[row][col] = O(cv) 
                    
                    self.turn = Computer
                    
                    board.drawXOs()
                    
                    if not board.full() and not abs(board.eval())==1:
                        computerTurn()
                    
                        self.turn = Human
                        
                        board.drawXOs()
                    else:
                        self.locked = True
                        
                    if board.eval() == 1:
                        tkinter.messagebox.showwarning("Game Over","X wins!!!")
          
                    if board.eval() == -1:
                        tkinter.messagebox.showwarning("Game Over","O wins. How did that happen?")
                        
                    if board.full():
                        tkinter.messagebox.showwarning("Game Over","It was a tie.")
     
        screen.onclick(mouseClick)
        
        screen.listen()

def main():
    root = tkinter.Tk()
    root.title("Tic Tac Toe")    
    application = TicTacToe(root)  
    application.mainloop()
        
if __name__ == "__main__":
    main()
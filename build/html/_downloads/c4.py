import turtle
import subprocess
import tkinter
import sys
import time

# The following program will play connect four. This front-end
# program and a back-end program communicate through pipes (both input and output)
# according to this architecture. When a command is sent it is indicated 
# with a right arrow indicating something is written to the other program's 
# standard input. When the other program sends something to this Python Program
# it is indicated with a left arrow. That means it is written to the standard
# output of the other program. 

# front-end   back-end      
#   0 ----------->     # New Game is initiated by the front-end code
#   <----------- 0     # Back-end code says OK.
#   2 M --------->     # Human Move followed by Move Value M which is 0-6.
#                      # Move Value M will be on separate line.
#   <----------- 0     # Back-end code says OK.
#   1 ----------->     # Computer Move is indicated to back-end code.
#   <--------- 0 M     # Status OK and Move Value M which is 0-6.
#   3 ----------->     # Game Over?
#   <--------- Val     # Val is 0=Not Over, 1=Computer Won, 2=Human Won, 3=Tie.

# If you wish to implement your own back-end you must alter the line of code below
# that looks like this:
#
# proc = subprocess.Popen(["clisp","c4.fas"],stdout=subprocess.PIPE, \
#    stdin=subprocess.PIPE,universal_newlines=True)
#
# You must replace clisp with the program that starts your program running. If you
# have written your back-end with python 3.x then replace clisp with python3. 
# The c4.fas should be replaced by any command-line arguments to your program. If 
# you have written your program in python, then the argument should be the name of your
# program which must be in the same directory as this front-end code. 
#
# Output that you want to print for debugging purposes can be written to standard error
# instead of standard output. In this way standard output can be used to communicate
# with the front-end while you still see output printed to the terminal window for 
# debugging purposes. In python, standard error can be written to as follows:
#
# import sys
# sys.stderr.write('Your text goes here.\n')
#
# This architecture must be adhered to strictly for this program to work. Here
# is sample Lisp code that will handle this interaction. However, the other 
# program may be written in any programming language, including Python.

#(defun play ()
  #(let ((gameBoard (make-hash-table :size 10))
        #(memo (make-hash-table :size 27 :test #'equalp))
        #(lastMove nil))

    #(do () (nil nil)
        #;(printBoard gameBoard)
        #(let ((msgId (read)))
          #(cond ((equal msgId 2) ;; Human turn to call human turn function
                 #(setf lastMove (humanTurn gameBoard)))

                #((equal msgId 0) ;; New Game message
                 #(progn 
                   #(setf gameBoard (make-hash-table :size 10))
                   #(setf memo (make-hash-table :size 27 :test #'equalp))
                   #(format t "0~%")))
                   #;; Return a 0 to indicate the computer is ready

                #((equal msgId 1) ;; Computer Turn message
                 #(setf lastMove (computerTurn gameBoard)))
                
                #((equal msgId 3) ;; Get Game Status
                 
                 #(cond ((equal (evalBoard gameBoard lastMove) 1) (format t "1~%"))
                       #;; The Computer Won

                       #((equal (evalBoard gameBoard lastMove) -1) (format t "2~%"))
                       #;; The Human Won

                       #((fullBoard gameBoard) (format t "3~%"))
                       #;; It's a draw

                       #(t (format t "0~%"))))
                       #;; The game is not over yet.

                #(t (format t "-1~%")))))))

Computer = 1
Human = -1

class Tile(turtle.RawTurtle):
    def __init__(self,canvas,row,col,app):
        super().__init__(canvas)
        self.val = 0
        self.row = row
        self.col = col
        self.tttApplication = app
        self.penup()
        self.ht()
        self.goto(col*100+50,row*100+50)
        
    def setShape(self,horc,screen):
        self.val = horc
        
        if horc == Computer:
            self.shape("blackchecker.gif") 
        else:
            self.shape("redchecker.gif") 
        
        self.drop(screen) 

    def getOwner(self):
        return self.val
    
    def clicked(self):
        print(self.row,self.col)
        
    def drop(self,screen):
        self.goto(self.col*100+50,0)
        screen.tracer(1)
        self.speed(5)
        self.st()
        self.goto(self.col*100+50,self.row*100+55)
        self.goto(self.col*100+50,self.row*100+45)
        self.goto(self.col*100+50,self.row*100+50)
        screen.tracer(0)

class Connect4Application(tkinter.Frame):      
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.running = False

    def buildWindow(self):

        self.master.title("Connect Four")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)
                
        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=700,height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()  
        screen = theTurtle.getscreen()  
        screen.setworldcoordinates(0,600,700,0)
        screen.register_shape("blackchecker.gif")
        screen.register_shape("redchecker.gif")
        screen.tracer(0)
        screen.bgcolor("yellow")
        
        theTurtle.width(5)
        for k in range(6):
            theTurtle.penup()
            theTurtle.goto(k*100+100,0)
            theTurtle.pendown()
            theTurtle.goto(k*100+100,600)
            
        theTurtle.ht()
            
        screen.update()
        
        def checkStatus():
            toOther.write("3\n")
            toOther.flush()
            
            status = int(fromOther.readline().strip())
            
            if status == 1:
                tkinter.messagebox.showinfo("Game Over", "I Won!!!!!")
            elif status == 2:
                tkinter.messagebox.showinfo("Game Over", "You Won!!!!!") 
            elif status == 3:
                 tkinter.messagebox.showinfo("Game Over", "It's a tie.")
                 
            #print("Status is ", status)
            return status
        
        def ComputerTurn():
            toOther.write("1\n")
            toOther.flush()
            status = int(fromOther.readline().strip())
            #print("Computer Turn Other Status = ", status)
            if status == 0:
                move = int(fromOther.readline())
                #print("Move is", move)
                row = move // 7
                col = move % 7
                
                matrix[row][col].setShape(Computer,screen)
                screen.update()

        def HumanTurn(x,y):
            if self.running: 
                return
            
            #status = checkStatus()
            
            #if status != 0:
                #return
            
            self.running = True
            col = int(x) // 100
            
            row = 5
            while row >= 0 and matrix[row][col].isvisible():
                row = row - 1
            
            if row < 0:
                #Then we clicked in a column that was already full.
                self.running = True
                return 
              
            val = row * 7 + col
            
            # Do the Human Turn
            toOther.write("2\n")
            toOther.flush()
            toOther.write(str(val) + "\n")
            toOther.flush()
            
            status = fromOther.readline().strip()
            #print("Status is ",status)
            
            matrix[row][col].setShape(Human,screen)
            screen.update()
            
            # Check the status of the game
            status = checkStatus()
            
            if status == 0:
                # Do a Computer Turn
                ComputerTurn()
                checkStatus()
            
            self.running = False
            
    
        matrix = []       
        
        for i in range(6):
            row = []
            for j in range(7):
                t = Tile(canvas,i,j,self)
                row.append(t)
            matrix.append(row)
            
        screen.update()
        screen.onclick(HumanTurn)

        sideBar = tkinter.Frame(self,padx=5,pady=5, relief=tkinter.RAISED,borderwidth="5pt")
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        
        def NewGame():
            toOther.write("0\n")
            toOther.flush()
            status = int(fromOther.readline().strip())            
    
            for row in matrix:
                for token in row:
                    token.ht()
                    
            screen.update()
                    
        kb = tkinter.Button(sideBar,text="Pass",command=ComputerTurn)
        kb.pack()  
        
        ng = tkinter.Button(sideBar,text="New Game",command=NewGame)
        ng.pack()  
        
        
        proc = subprocess.Popen(["clisp","c4.fas"],stdout=subprocess.PIPE, \
            stdin=subprocess.PIPE,universal_newlines=True)
        fromOther = proc.stdout
        toOther = proc.stdin   
        
        # To write to the other program you should use commands like this
        # toOther.write(val+"\n")
        # Don't forget to flush the buffer
        # toOther.flush()        
        
        # To read from the other program you write
        # line = fromOther.readline().strip()        
        


def main():
    root = tkinter.Tk()
    animApp = Connect4Application(root)

    animApp.mainloop()
    print("Program Execution Completed.")
    
if __name__ == "__main__":
    main()
    
    
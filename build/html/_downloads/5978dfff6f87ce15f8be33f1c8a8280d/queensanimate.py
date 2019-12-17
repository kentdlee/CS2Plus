import turtle
import subprocess
import tkinter
import sys
import time

# The following program will animate the n-queens algorithm. This front-end
# program and a back-end program communicate through pipes (both input and output)
# according to this architecture. When a command is sent to the back-end it is indicated 
# with a right arrow indicating something is written to the back-end program's 
# standard input. When the back-end program sends something to this front-end program
# it is indicated with a left arrow. That means it is written to the standard
# output of the back-end program. 

# Each state in the search consists of the currently placed queens (up to the current 
# row) and the remaining available locations above the row the last queen was placed in.
# The architecture below repeats this state information over and over until the search
# has found a solution. 

# front-end   back-end
#   8 --------->       # A size is specified to the back-end program
#   <----------- 0 10  # these are the row column pairs of possibly assigned queen locations
#   ...                # repeating until the search is complete
#   <----------- and   # The and is printed between the assigned and remaining locations
#   <----------- 1 2   # next comes the remaining locations
#   ...                # repeating until done
#   <----------- done  # Then done is printed after each state is completely enumerated
#   ...                # These states repeat until the search has concluded. 
#   <----------- eof   # EOF is printed back to inidicate the end of the animation.

# If you wish to implement your own backend you must alter the line of code below
# that looks like this:
#
# proc = subprocess.Popen(["clisp","qsearch.fas"],stdout=subprocess.PIPE, \
#    stdin=subprocess.PIPE,universal_newlines=True)
#
# You must replace clisp with the program that starts your program running. If you
# have written your back-end with python 3.x then replace clisp with python3. 
# The qsearch.fas should be replaced by any command-line arguments to your program. If 
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
# is sample Lisp code that will handle this interaction.

#(defun queens-search (size)
   #(print-state (dfs (initialize size) #'(lambda (state) (eq (list-length 
   #                (first state)) size))))
   #(format t "eof~%"))

#(defun processCommand ()
  #(let ((size 8))


    #(setf size (parse-integer (read-line)))
    #(format *error-output* "Lisp says - Size is ~D~%"  size)

    #(queens-search size)))


#(processCommand)



class QueensAnimateApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.running = False

    def buildWindow(self):

        self.master.title("Queens Search Animation")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def run():
            if self.running:
                return
            
            try:
                colors = ["red", "black"]
                colorIndex = 0
                self.running = True
                screen = theTurtle.getscreen() 
                screen.clear()
                screen.tracer(0)
                self.screen = screen  
                size = int(self.sizevar.get())
                cellWidth = 800/size
                screen.setworldcoordinates(0,800,800,0)
            
                for i in range(size):
                    for j in range(size):
                        theTurtle.penup()
                        theTurtle.goto(j*cellWidth,i*cellWidth)
                        theTurtle.pendown()
                        theTurtle.color("black")
                        theTurtle.fillcolor(colors[colorIndex])
                        colorIndex=(colorIndex+1)%2
                        theTurtle.begin_fill()
                        theTurtle.goto(j*cellWidth+cellWidth,i*cellWidth)
                        theTurtle.goto(j*cellWidth+cellWidth,i*cellWidth+cellWidth)
                        theTurtle.goto(j*cellWidth,i*cellWidth+cellWidth)
                        theTurtle.goto(j*cellWidth,i*cellWidth)
                        theTurtle.end_fill()
                    if (size % 2 == 0):
                        colorIndex = (colorIndex+1)%2
                        
                screen.update()
                        
                matrix = []
                screen.tracer(0)
                for i in range(size):
                    row = []
                    for j in range(size):
                        t = turtle.RawTurtle(canvas)
                        t.penup()
                        t.color("yellow")
                        t.goto(j*cellWidth+cellWidth/2,i*cellWidth+cellWidth/2)
                        t.width(cellWidth)
                        t.shape("circle")
                        t.ht()
                        row.append(t)
                    matrix.append(row)
                            
                screen.update()
                
                proc = subprocess.Popen(["clisp","qsearch.fas"],stdout=subprocess.PIPE, \
                    stdin=subprocess.PIPE,universal_newlines=True)
                fromLisp = proc.stdout
                toLisp = proc.stdin
                toLisp.write(str(size)+"\n")
                toLisp.flush()
                
                line = fromLisp.readline().strip()
                
                while line != "eof" and self.running:
                    # process line of currently inspected node
                    for row in matrix:
                        for cell in row:
                            cell.ht()
                            
                    while line != "and":
                        
                        lst = line.split()
                        row = int(lst[0])
                        col = int(lst[1])
                        matrix[row][col].color("yellow")
                        matrix[row][col].st()
                        
                        # read the next line
                        line = fromLisp.readline().strip()
                        
                    line = fromLisp.readline().strip()

                    while line != "done":
                        
                        lst = line.split()
                        row = int(lst[0])
                        col = int(lst[1])
                        matrix[row][col].color("blue")
                        matrix[row][col].st()
                        
                        # read the next line
                        line = fromLisp.readline().strip()
                        
                    screen.update()
                    #time.sleep(1)
                    # read the next line
                    line = fromLisp.readline().strip()
                 

                proc.kill()
                self.running = False

                
            except Exception as ex:
                tkinter.messagebox.showwarning("Alert",str(ex))
                tb = sys.exc_info()[2]
                self.running = False
                raise ex
                
            
                
        def stop():
            self.running = False

        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=800,height=800)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()         

        sideBar = tkinter.Frame(self,padx=5,pady=5, relief=tkinter.RAISED, \
            borderwidth="5pt")
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        
        self.sizevar = tkinter.StringVar()
        self.sizevar.set("8")
        
        selectLabel = tkinter.Label(sideBar,text="Problem Size")
        selectLabel.pack()
        
        sizeEntryBox = tkinter.Entry(sideBar,textvariable=self.sizevar)
        sizeEntryBox.pack()
        
        sb = tkinter.Button(sideBar,text="Start",command=run)
        sb.pack()
        
        kb = tkinter.Button(sideBar,text="Stop",command=stop)
        kb.pack()   

def main():
    root = tkinter.Tk()
    animApp = QueensAnimateApplication(root)

    animApp.mainloop()
    print("Program Execution Completed.")
    
if __name__ == "__main__":
    main()
    
    
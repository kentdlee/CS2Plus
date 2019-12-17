import turtle
import subprocess
import tkinter
import sys
import time

# The following program will animate a search algorithm written in a language of
# your choice. The only requirement is that the programming language is able to 
# write to standard output and read from standard input following the architecture
# outlined below. The program that you write is the back-end communicating to this
# front-end code. A compiled lisp program serves as a back-end for demonstration
# purposes and can be downloaded from the text website. This front-end
# program and the back-end program communicate through pipes (both input and output)
# according to this architecture. When a command is sent to the back-end it is indicated 
# with a right arrow indicating something is written to the back-end program's 
# standard input. When the back-end program sends something to this front-end
# it is indicated with a left arrow. That means it is written to the standard
# output of the back-end program. 

# front-end    back-end
#   dfs --------->     # A search type is selected, the back-end program must read
#   maze.txt ---->     # The filename is passed to the back-end program
#   <----------- 0 10  # these are the row column pairs of visited locations
#   ...                # repeating until the search is complete
#   <----------- done  # Then done is printed by the back-end
#   <----------- 31 22 # Finally the path is printed in reverse order
#   ...                # All locations are printed
#   <----------- eof   # EOF is printed back to be sent back to this application.

# If you wish to implement your own back-end you must alter the line of code below
# that looks like this:
#
# proc = subprocess.Popen(["clisp","search.fas"],stdout=subprocess.PIPE, \
#    stdin=subprocess.PIPE,universal_newlines=True)
#
# You must replace clisp with the program that starts your program running. If you
# have written your back-end with python 3.x then replace clisp with python3. 
# The search.fas should be replaced by any command-line arguments to your program. If 
# you have written your program in python, then the argument should be the name of your
# program which must be in the same directory as this front-end code and the mazes you
# with to search. 
#
# Output that you want to print for debugging purposes can be written to standard error
# instead of standard output. In this way standard output can be used to communicate
# with the front-end while you still see output printed to the terminal window for 
# debugging purposes. In python, standard error can be written to as follows:
#
# import sys
# sys.stderr.write('Your text goes here.\n')
#
# This architecture must be adhered to strictly for this program to work. The search 
# types supported by the front-end code are: dfs, bfs, hill, best, astar. Here
# is sample Lisp code that will handle this interaction from the front-end code. 

#(defun processCommand ()
  #(let ((searchTtype "") 
        #(filename "")
        #(path nil))


    #(setf searchType (read-line))
    #(format *error-output* "Lisp says - Search Type is ~S~%"  searchType)
    #(setf filename (read-line))


    #(cond ((equal searchType "dfs") (setf path (dfsMaze filename)))
          #((equal searchType "bfs") (setf path (bfsMaze filename))))

    #(format t "done~%")
    #(printPath path)
    #(format t "eof~%")))

#(processCommand)


class MazeAnimateApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.running = False

    def buildWindow(self):

        self.master.title("Maze Search Animation")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def run():
            if self.running:
                return
            
            try:
                self.running = True
                screen = theTurtle.getscreen()
                screen.clear()
                screen.tracer(0)
                screen.setworldcoordinates(0,800,1300,0) 
                self.screen = screen            
                screen.register_shape("tile20.gif")            
                file = open(self.filename.get(),"r")
            
                firstLine = file.readline()
                rows = int(firstLine)
                secondLine = file.readline()
                cols = int(secondLine)
                
                if cols > 65 or rows > 40:
                    tkinter.messagebox.showwarning("Information", \
                        "Maximum allowed rows is 40 and the maximum allowed columns are 65")
                    self.running = False
                    return 
            
                screen.register_shape("tile20.gif")
                 
                screen.tracer(0)
                for i in range(rows):
                    line = file.readline()
                    for j in range(cols):
                        if line[j] == "*":
                            tile = turtle.RawTurtle(canvas)
                            tile.penup()
                            tile.shape("tile20.gif")
                            tile.goto(j*20+10,i*20+10)
                            
                screen.update()
                
                proc = subprocess.Popen(["clisp","search.fas"],stdout=subprocess.PIPE, \
                    stdin=subprocess.PIPE,universal_newlines=True)
                fromLisp = proc.stdout
                toLisp = proc.stdin
                print(self.rbSelection())
                toLisp.write(self.rbSelection()+"\n")
                print(self.filename.get())
                toLisp.flush()
                toLisp.write(self.filename.get()+"\n")
                toLisp.flush()
                  
                t = turtle.RawTurtle(canvas)
                t.penup()
                t.shape("circle")
                t.color("blue")
                
                line = fromLisp.readline().strip()
                screen.tracer(1)
                
                while line != "done" and self.running:
                    # process line of currently inspected node
                    lst = line.split()
                    row = int(lst[0])
                    col = int(lst[1])
                    length = int(lst[2])
                    t.goto(col*20+10,row*20+10+5)
                    #t.dot(10)
                    t.write(str(length),align="center",font=("Arial", 10, "bold"))
        
                    # read the next line
                    line = fromLisp.readline().strip()
                        
                t.color("red")
                line = fromLisp.readline().strip()
                
                while line != "eof" and self.running:
                        
                    # process line of final path node
                    lst = line.split()
                    row = int(lst[0])
                    col = int(lst[1])
                    length = int(lst[2])
                    t.goto(col*20+10,row*20+10+5)
                    t.write(str(length),align="center",font=("Arial", 10, "bold"))
                    #t.dot(10)                    
                    
                    # read the next line
                    line = fromLisp.readline().strip()                    

                proc.kill()
                t.ht()
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

        canvas = tkinter.Canvas(self,width=1300,height=800)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()         

        sideBar = tkinter.Frame(self,padx=5,pady=5, relief=tkinter.RAISED, \
            borderwidth="5pt")
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        
        self.filename = tkinter.StringVar()
        self.filename.set("maze.txt")
        
        selectLabel = tkinter.Label(sideBar,text="Select File")
        selectLabel.pack()
        
        fileEntryBox = tkinter.Entry(sideBar,textvariable=self.filename)
        fileEntryBox.pack()
 
        selectLabel = tkinter.Label(sideBar,text="Select Search")
        selectLabel.pack()
        
        RadioButtonBox = tkinter.Frame(sideBar,relief=tkinter.SUNKEN, \
            borderwidth="5pt",padx=5,pady=5)
        RadioButtonBox.pack()
        
        self.searchType = tkinter.IntVar()
        
        rb1 = tkinter.Radiobutton(RadioButtonBox, text = "Depth First", \
            variable=self.searchType, value=0, command=self.rbSelection)
        rb1.grid(sticky="w",column=0,row=0)
        
        rb2 = tkinter.Radiobutton(RadioButtonBox, text = "Breadth First", \
            variable=self.searchType, value=1, command=self.rbSelection)
        rb2.grid(sticky="w",column=0,row=1)

        rb3 = tkinter.Radiobutton(RadioButtonBox, text = "Hill Climbing", \
            variable=self.searchType, value=2, command=self.rbSelection)
        rb3.grid(sticky="w",column=0,row=2)
        
        rb4 = tkinter.Radiobutton(RadioButtonBox, text = "Best First", \
            variable=self.searchType, value=3, command=self.rbSelection)
        rb4.grid(sticky="w",column=0,row=3)
        
        rb5 = tkinter.Radiobutton(RadioButtonBox, text = "A Star", \
            variable=self.searchType, value=4, command=self.rbSelection)
        rb5.grid(sticky="w",column=0,row=4)
        
        sb = tkinter.Button(sideBar,text="Start",command=run)
        sb.pack()
        
        kb = tkinter.Button(sideBar,text="Stop",command=stop)
        kb.pack()   
        
    def rbSelection(self):
        if self.searchType.get() == 0:
            self.master.title("DFS Search")
            return "dfs"
        elif self.searchType.get() == 1:
            self.master.title("BFS Search")
            return "bfs"
        elif self.searchType.get() == 2:
            self.master.title("Hill Climbing Search")
            return "hill"
        elif self.searchType.get() == 3:
            self.master.title("Best First Search")
            return "best"
        elif self.searchType.get() == 4:
            self.master.title("A* Search")
            return "astar"

def main():
    root = tkinter.Tk()
    animApp = MazeAnimateApplication(root)

    animApp.mainloop()
    print("Program Execution Completed.")
    
if __name__ == "__main__":
    main()
    
    
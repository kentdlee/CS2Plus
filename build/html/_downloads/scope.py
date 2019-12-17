import math


PI = math.pi

def area(radius):
    global z
    z = 6
    theArea = PI * radius ** 2
    
    return theArea


def main():
    global z
    
    historyOfPrompts = []
    historyOfOutput = []
    
    def getInput(prompt):
        x = input(prompt)
        historyOfPrompts.append(prompt)
        
        return x
    
    def showOutput(val):
        historyOfOutput.append(val)
        print(val)
    
    rString = getInput("Please enter the radius of a circle: ")
    
    r = float(rString)
    
    val = area(r)
    print(z)
    showOutput("The area of the circle is " + str(val))
    
if __name__ == "__main__":
    main()
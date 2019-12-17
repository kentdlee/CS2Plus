from xml.dom import minidom
import turtle
import math

from xml.dom import minidom
import turtle

def drawArrow(turtle):
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    turtle.right(180)
    turtle.forward(8)
    turtle.left(90)
    turtle.forward(3)
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    turtle.backward(6)
    x3 = turtle.xcor()
    y3 = turtle.ycor()
    turtle.begin_fill()
    turtle.goto(x1,y1)
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.end_fill()
    
class Vertex:
    def __init__(self,vertexId,x,y,label):
        self.vertexId = vertexId
        self.x = x
        self.y = y
        self.label = int(label)
        self.edges = []
        self.previous = None
        self.previousEdge = None
        
    def draw(self,turtle,color="white"):
        x = self.x
        y = self.y
        turtle.penup()
        turtle.goto(x,y-20)
        
        turtle.pendown()
        turtle.color("black")
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x+2,y+12)
        turtle.write(self.label,align="center",font=("Arial",12,"bold"))
 
    def __str__(self):
        return "Vertex: " + "\n  label: " + str(self.label) + "\n  id: " + str(self.vertexId) + "\n  x: " + str(self.x) + "\n  y: " + str(self.y)

class Edge:
    def __init__(self,v1,v2,weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        
    def __lt__(self,other):
        return self.weight < other.weight
    
    def __str__(self):
        return "Edge: " + "\n  v1: " + str(self.v1) + "\n  v2: " + str(self.v2) 
    
    def draw(self,turtle,vertexDict,color="grey",width=1):
        turtle.color(color)
        turtle.width(width)
        x1 = float(vertexDict[self.v1].x)
        y1 = float(vertexDict[self.v1].y)
        x2 = float(vertexDict[self.v2].x)
        y2 = float(vertexDict[self.v2].y)
        x = x1-x2
        y = y1-y2
        d = math.sqrt(y**2 + x**2)
        angle = (math.acos(x/d)/math.pi)*180
        if y1 < y2:
            angle = angle + 2 * (180-angle)

        turtle.penup()
        turtle.goto(x2,y2)
        turtle.pendown()

        turtle.color(color)
        turtle.setheading(angle)
        turtle.penup()
        turtle.forward(0)
        turtle.pendown()
        turtle.forward(d-20)
        drawArrow(turtle)
        turtle.width(1)        
        if self.weight != 0:       
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            turtle.penup()
            turtle.goto(x+1,y+12)
            turtle.color("black")
            turtle.write(str(self.weight),align="center",font=("Arial",12,"bold"))
        turtle.setheading(0)

       
def minCost(unvisited,vertexDict):
    
    minVal = infinity
    minId = -1
    
    for ident in unvisited:
        if vertexDict[ident].cost < minVal:
            minId = ident
            minVal = vertexDict[ident].cost
            
    return minId
            
def main():
    xmldoc = minidom.parse("neiowagraph.xml")
    
    graph = xmldoc.getElementsByTagName("Graph")[0]
    vertices = graph.getElementsByTagName("Vertices")[0].getElementsByTagName("Vertex")
    edges = graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")
    
    width = float(graph.attributes["width"].value)
    height = float(graph.attributes["height"].value)
    turtle.setup(0.65*width,0.65*height)
    t = turtle.Turtle()
    screen = t.getscreen()
    screen.setworldcoordinates(0,height,width,0)
    screen.title("A Weighted, Directed Graph")
    screen.tracer(0)
    t.speed(100)
    t.ht()
    vertexDict = {}
    vCount = 0
    
    for vertex in vertices:
        vertexId = int(vertex.attributes["vertexId"].value)
        x = float(vertex.attributes["x"].value)
        y = float(vertex.attributes["y"].value)
        label = vertex.attributes["label"].value
        v = Vertex(vertexId, x, y, label)
        vertexDict[vertexId] = v
        vCount += 1
        
    edgeList = []
    
    for edgeNode in edges:
        edge = Edge(int(edgeNode.attributes["head"].value), int(edgeNode.attributes["tail"].value))
        if "weight" in edgeNode.attributes:       
            edge.weight = float(edgeNode.attributes["weight"].value) 
        vertexDict[edge.v2].edges.append(edge)
        edgeList.append(edge)
    
    for edge in edgeList:
        edge.draw(t,vertexDict)

    for vertexId in vertexDict:
        vertex = vertexDict[vertexId]
        vertex.draw(t,(0.8,1,0.4))

    # Run Depth First Search
    visited = []
    stack = []
    target = vertexDict[9]
    
    
    for ident in vertexDict:
        vertex = vertexDict[ident]
        if vertex.label == 0:
            source = vertex    
    
    stack.append(source)
    found = False
    
    while (len(stack) > 0) and not found:
        current = stack.pop()
        print(current)
        visited.append(current.vertexId)
        if current.vertexId == target.vertexId:
            found = True
        else:
            for edge in current.edges:
                vId = edge.v1
                vertex = vertexDict[vId]
                vertex.previous = current
                if not vId in visited:
                    stack.append(vertex)
                
    if found:
        print("Found target")
        current = target
        while current.vertexId != source.vertexId:
            next = current
            current = current.previous
            print("Coloring edge:", current)
            for edge in current.edges:
                if edge.v1 == next.vertexId:
                    print("found edge: ", edge)
                    edge.draw(t,vertexDict,"blue",2)
        
        
    ## Run Dijkstra's Algorithm
    #previous = list(range(30))
    #visited = []
    

            
    #source.cost = 0       
    #unvisited = [source.vertexId]
    
    #while len(unvisited) > 0:
        #currentId = minCost(unvisited,vertexDict)
        #current = vertexDict[currentId]
        
        #print("Examining: ", current)
        
        #visited.append(currentId)
        #unvisited.remove(currentId)
        
        #for edge in current.edges:
            #if edge.v1 == currentId:
                #adjacentId = edge.v2
            #else:
                #adjacentId = edge.v1
            
            #if not adjacentId in visited:  
                #adjacent = vertexDict[adjacentId]
                    
                #if current.cost + edge.weight < adjacent.cost:
                    #adjacent.cost = current.cost + edge.weight
                    #adjacent.previous = currentId
                    #adjacent.previousEdge = edge
                    #if not adjacentId in unvisited:
                        #unvisited.append(adjacentId)  

    #for vertexId in vertexDict:
        #vertex = vertexDict[vertexId]
        #if vertex.previousEdge != None:
            #vertex.previousEdge.draw(t,vertexDict,"purple",2)
            
    for vertexId in vertexDict:
        vertex = vertexDict[vertexId]
        vertex.draw(t,(0.8,1,0.4))
        #vertex.drawCost(t,"orange")
        
        
        
    screen.update()
    screen.exitonclick()
    
if __name__ == "__main__":
    main()

from xml.dom import minidom

def readDict(node):
    d = {}
    
    for child in node.childNodes:
        if child.nodeType == child.ELEMENT_NODE and child.tagName == "key":
            lastKey = child.firstChild.data
            
        if child.nodeType == child.ELEMENT_NODE and child.tagName != "key":
            value = child
            if child.tagName == "string":
                value = child.firstChild.data
                
            if child.tagName == "integer":
                value = int(child.firstChild.data)
                
            if child.tagName == "true":
                value = True
                
            if child.tagName == "false":
                value = False
                
            d[lastKey] = value
                     
    return d 

class Vertex:
    def __init__(self,vertexId,label,x,y):
        self.x = x
        self.y = y
        self.label = label
        self.vertexId = vertexId
        
class Edge:
    def __init__(self,v1Id,v2Id,weight=None):
        self.v1Id = v1Id
        self.v2Id = v2Id
        self.weight = weight
        
        
def main():
    xmldoc = minidom.parse("neiowagraph.graffle")
    
    top = xmldoc.getElementsByTagName("dict")[0]
    vertices = {}
    edges = {}
    weights = {}
    minX = 99999999999999999999999999
    minY = 99999999999999999999999999
    maxX = 0
    maxY = 0
    vertexId = 0
    directed = False
    weighted = False
    
    for child in top.childNodes:
        #print(child)
        if child.nodeType == child.ELEMENT_NODE and child.tagName == "key":
            lastKey = child.firstChild.data
            
        if child.nodeType == child.ELEMENT_NODE and child.tagName == "array" and lastKey == "GraphicsList":
            #print("  ", child.tagName)
            #print("Found graphicsList")
            graphicsList = child
            
            for elm in graphicsList.childNodes:
                tag = readDict(elm)
                if "Shape" in tag and tag["Shape"] == "Circle":
                    print("Found Node")
                    textDict = readDict(tag["Text"])
                    print(textDict["Text"].split()[-1][:-1])
                    bounds = tag["Bounds"]
                    lst = bounds.split()
                    x = float(lst[0][2:-1])
                    y = float(lst[1][:-2])
                    if y < minY:
                        minY = y
                    if x < minX:
                        minX = x
                    if x > maxX:
                        maxX = x
                    if y > maxY:
                        maxY = y
                    print(tag["ID"])
                    vertices[tag["ID"]] = Vertex(vertexId,textDict["Text"].split()[-1][:-1], x, y)
                    vertexId +=1
                    
                if "Class" in tag and tag["Class"] == "LineGraphic":
                    headDict = readDict(tag["Head"])
                    tailDict = readDict(tag["Tail"])
                    styleDict = readDict(tag["Style"])
                    strokeDict = readDict(styleDict["stroke"])
                    print("Line: from ", headDict["ID"], "to", tailDict["ID"])
                    if strokeDict["HeadArrow"] != "0" or strokeDict["TailArrow"] != "0":   
                        directed = True
                    
                    if strokeDict["HeadArrow"] == "0" and strokeDict["TailArrow"] != "0":    
                        edges[tag["ID"]] = Edge(readDict(tag["Head"])["ID"], readDict(tag["Tail"])["ID"])
                    else:
                        edges[tag["ID"]] = Edge(readDict(tag["Tail"])["ID"], readDict(tag["Head"])["ID"])
                        
                if "FitText" in tag and "Line" in tag:
                    lineID = readDict(tag["Line"])["ID"]
                    weight = float(readDict(tag["Text"])["Text"].split()[-1][:-1])
                    weights[lineID] = weight
                    print("Weight: ", weight)
                    
    file = open("neiowagraph.xml","w")
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    width = maxX - minX
    height = maxY - minY
    file.write('<Graph width="%1.2f" height="%1.2f" directed="%s" weighted="%s">\n'%(1.2*width,1.2*height,str(directed),str(weighted)))
    file.write('  <Vertices>\n')
    for vertexID in vertices:
        vertex = vertices[vertexID]
        file.write('    <Vertex vertexId="%d" x="%1.2f" y="%1.2f" label="%s"/>\n'%(vertex.vertexId,vertex.x - minX + 0.1 * width,vertex.y - minY + 0.1 * height,vertex.label))
    file.write('  </Vertices>\n')
    
    file.write('  <Edges>\n')
    for edgeId in edges:
        edge = edges[edgeId]
        print("Edge id is",edgeId)
        if edgeId in weights:
            weighted = True
            file.write('    <Edge tail="%s" head="%s" weight="%s"/>\n'%(vertices[edge.v1Id].vertexId,vertices[edge.v2Id].vertexId,weights[edgeId]))
        else:
            file.write('    <Edge tail="%s" head="%s"/>\n'%(vertices[edge.v1Id].vertexId,vertices[edge.v2Id].vertexId))
    file.write('  </Edges>\n')
            
    file.write('</Graph>')
    file.close()
        #if len(weights) != 0:
        #    file.write(' weight="' + str(weights[]))
                    
                    

        
if __name__ == "__main__":
    main()
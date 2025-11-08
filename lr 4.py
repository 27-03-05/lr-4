import random
class Graf():
    def __init__(self):
        self.graf={}

    def svyazi(self,x,y):
        if x not in self.graf:
            self.graf[x]=[]
        if y not in self.graf:
            self.graf[y]=[]
        self.graf[x].append(y)
        self.graf[y].append(x)
    def print_vertices(self):
        print("Вершины графа:", list(self.graf.keys()))


# создадим граф
g=Graf()
g.svyazi(1,1) 
g.svyazi(3,5)
g.svyazi(6,2)
g.svyazi(1,0)
g.svyazi(3,2)
g.svyazi(2,2)
g.svyazi(5,7)
g.svyazi(1,2)
g.svyazi(2,1)
g.svyazi(3,0)
visited=set()           
            
g.print_vertices()



def dfs(graph, start, visited):      #обход в глубину
    visited.add(start)
    print(start)
    for neighbor in graph.graf[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
visited=set()
dfs(g,0,visited)

def bfs(graph, start):        #обход в ширину
    visited = set()
    ochered = [start]
    while ochered:
        first_vershina = ochered.pop(0)
        if first_vershina not in visited:
            print(first_vershina,end = '-')
            visited.add(first_vershina)
            for neighbor in graph.graf[first_vershina]:
                if neighbor not in visited:
                    ochered.append(neighbor)
bfs(g,0)  
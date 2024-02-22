class Graph:
    def __init__(self):
        self.adjacency_list = {}



    # add vertex
    def add_vertex(self , vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    # add edge
    def add_edge(self , vertex1 , vertex2):
        if vertex1 and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    # remove edge
    def remove_edge(self , vertex1 , vertex2):
        if vertex1 and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    
    # remove vertex
    def remove_vertex(self , vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False


    # print graph
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")


    #Breadth First Search
    def breadth_first_search(self , vertex):   

        visted = []
        queue = []
        visted.append(vertex)
        queue.append(vertex)

        ''' The time complexity of the BFS algorithm is represented in the form of O(V + E), 
        where V is the number of nodes and E is the number of edges
        The space complexity of the algorithm is O(V).
         '''

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visted:
                    visted.append(adjacency_vertex)
                    queue.append(adjacency_vertex)


    def deapth_first_search(self , vertex):
        visited = set()
        visited.add(vertex)
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            print(current_vertex)
            for adj_vertex in self.adjacency_list[current_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    stack.append(adj_vertex)

    

graph = Graph()
graph.add_vertex(vertex="A")
graph.add_vertex(vertex="B")
graph.add_vertex(vertex="C")
graph.add_vertex(vertex="D")
graph.add_vertex(vertex="E")
graph.add_edge("A" , "B")
graph.add_edge("A" , "C")
graph.add_edge("B" , "C")
graph.add_edge("C" , "D")
graph.add_edge("D" , "E")
graph.add_edge("E" , "A")
graph.print_graph()

'''
A : ['B', 'C', 'E']
B : ['A', 'C']
C : ['A', 'B', 'D']
D : ['C', 'E']
E : ['D', 'A']
'''

graph.breadth_first_search("A")
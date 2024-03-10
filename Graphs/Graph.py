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
graph.remove_vertex("E")
graph.print_graph()
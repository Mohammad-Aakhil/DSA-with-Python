class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            print("vertex already exist")

        self.adjacency_list[vertex] = []
        return self
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            return "one of the vertex is not present in list"
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self
        
    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            return "invalid vertex"
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return "vertex not in graph"
        
        for del_vertex in self.adjacency_list[vertex]:
            self.adjacency_list[del_vertex].remove(vertex)
        self.adjacency_list.pop(vertex)



z = Graph()
z.add_vertex("A")
z.add_vertex("B")
z.add_vertex("C")
print(z.adjacency_list)
z.add_edge("A","B")
print("adding edge from A to B")
print(z.adjacency_list)
# z.remove_edge("B", "C")
# z.remove_edge("A", "B")
# z.remove_edge("A", "B")
# print(z.adjacency_list)




# class G:
#     def __init__(self):
#         self.adj_list = {}

#     def add_vertex(self, vertex):
#         if vertex in self.adj_list:
#             return "vertex can't be duplicate"
        
#         self.adj_list[vertex] = []

#     def add_edge(self, v1, v2):
#         if v1 or v2 not in self.adj_list:
#             print("invalid edge")

#         self.adj_list[v1].append(v2)
#         self.adj_list[v2].append(v1)


#     def 
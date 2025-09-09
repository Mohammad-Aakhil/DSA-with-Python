# class Graph:
#     def __init__(self):
#         self.adj_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list:
#             self.adj_list[vertex] = []

#     def add_edge(self, v1, v2):
#         if v1 in self.adj_list and v2 in self.adj_list:
#             self.adj_list[v1].append(v2)
#             self.adj_list[v2].append(v1)

#     def remove_edge(self, v1, v2):
#         if v1 in self.adj_list and v2 in self.adj_list:
#             if v2 in self.adj_list[v1]: 
#                 self.adj_list[v1].remove(v2)
#             if v1 in self.adj_list[v2]: 
#                 self.adj_list[v2].remove(v1)

#     def remove_vertex(self, vertex):
#         if vertex in self.adj_list:
#             for neighbor in self.adj_list[vertex]:
#                 self.adj_list[neighbor].remove(vertex)
#             del self.adj_list[vertex]


# a = Graph()
# a.add_vertex("A")
# a.add_vertex("B")
# a.add_vertex("C")
# a.add_vertex("D")
# a.add_edge("A", "B")
# a.add_edge("B", "D")
# print(a.adj_list)
# a.remove_vertex("F")
# a.remove_vertex("C")
# print(a.adj_list)




class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []


    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)


    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)

            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)


    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbour in self.adj_list[vertex]:
                self.adj_list[neighbour].remove(vertex)

            del self.adj_list[vertex]

        # else:
        #     return f"{vertex} not present"  


a = Graph()
a.add_vertex("A")
a.add_vertex("B")
a.add_vertex("C")
a.add_vertex("D")
print(a.adj_list)
print()

print("after adding edges")
a.add_edge("A", "B")
a.add_edge("B", "D")
print(a.adj_list)
print()

print("after removing vertex")
print(a.remove_vertex("F"))
a.remove_vertex("D")
print(a.adj_list)
print()

print("after removing edge from B to D")
a.remove_edge("B", "D")
print(a.adj_list)
















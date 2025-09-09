class Graph:
    def __init__(self):
        self.adj_list = {}


    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            return "vertex already exists, choose a new one"


    # def add_vertex(self, vertex):
    #     if vertex not in self.adj_list:
    #         self.adj_list[vertex] = []
    #         return f"{self.adj_list[vertex]}, {vertex} HOME"
    #     else:
    #         return "vertex already exists, choose a new one"


    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

        else:
            return "invalid edge, missing vertex/vertices"


    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list :
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)

        else:
            return "invalid, no edge exist"


    def remove_vertex(self, vertex):
        if self.adj_list[vertex]:
            for neighbours in self.adj_list[vertex]:
                self.adj_list[neighbours].remove(vertex)
            del self.adj_list[vertex]



d = Graph()
d.add_vertex("MI")
d.add_vertex("CSK")
d.add_vertex("RCB")
d.add_vertex("GT")
d.add_vertex("RR")
print(d.adj_list)

d.add_edge("MI", "CSK")    #home
d.add_edge("MI", "RCB")    #home
d.add_edge("GT", "MI")     #away
d.add_edge("RR", "MI")     #away

print(d.adj_list)




        
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display_graph(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(self.graph[vertex]))

# 创建一个图实例
g = Graph()

# 添加顶点
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# 添加边
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

# 显示图
g.display_graph()
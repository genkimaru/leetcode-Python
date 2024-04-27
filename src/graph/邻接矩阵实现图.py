class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1][vertex2] = 1
        self.graph[vertex2][vertex1] = 1

    def display_graph(self):
        for row in self.graph:
            print(row)

# 创建一个图实例
g = Graph(4)

# 添加边
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

# 显示图的邻接矩阵
g.display_graph()
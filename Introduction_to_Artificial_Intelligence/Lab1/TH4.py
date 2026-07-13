from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị có hướng
G = nx.DiGraph()

edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 6), (5, 7)]

G.add_edges_from(edges)

# Bố trí theo tầng để dễ nhìn DFS
pos = {
    0: (0, 4),
    1: (-1, 3),
    2: (0, 3),
    4: (-1.5, 2),
    3: (1, 3),
    6: (-1.5, 1),
    5: (-0.5, 2),
    7: (-0.5, 1),
}

plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True, arrows=True, node_size=2500, font_size=12)

plt.title("DFS Graph")
plt.show()


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * 8
        self.DFSUtil(v, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)

    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)

    g.addEdge(4, 6)
    g.addEdge(4, 5)

    g.addEdge(5, 7)
    print("DFS - Duyet tim kiem tu dinh 0")
    g.DFS(0)

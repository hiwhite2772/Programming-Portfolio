from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [(0, 1), (0, 2), (0, 3), (1, 4), (3, 5)]

G.add_edges_from(edges)

pos = {0: (0, 3), 1: (-1, 2), 2: (0, 2), 3: (1, 2), 4: (-1, 1), 5: (1, 1)}

plt.figure(figsize=(6, 5))

nx.draw(G, pos, with_labels=True, node_size=2000)

plt.title("Graph for DFS")
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
        visited = [False] * (max(self.graph) + 1)
        self.DFSUtil(v, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(4, 2)
    g.addEdge(1, 4)
    g.addEdge(4, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(3, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(4, 5)
    print("DFS - Duyet tim kiem tu dinh 0")
    g.DFS(0)

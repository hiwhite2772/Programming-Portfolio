from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (3, 5), (4, 5), (4, 6), (5, 7), (5, 8)]

G.add_edges_from(edges)

pos = {
    0: (0, 4),
    1: (-1, 3),
    2: (1, 3),
    3: (-1.5, 2),
    4: (0, 2),
    5: (0, 1),
    6: (1, 1),
    7: (-0.5, 0),
    8: (0.5, 0),
}

plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, font_size=12)

plt.title("Directed Graph - BFS Example")
plt.show()


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, u):
        visited = [False] * 100
        queue = []
        visited[u] = True
        queue.append(u)

        while queue:
            u = queue.pop(0)
            print(u, end=" ")
            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 7)
    g.addEdge(5, 8)

    print("BFS - duyet tim kiem bat dau tu dinh 0")
    g.BFS(0)

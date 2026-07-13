from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị vô hướng
G = nx.Graph()

# Thêm cạnh
edges = [(0, 1), (0, 2), (2, 4), (1, 4), (1, 3), (3, 4), (3, 5), (4, 5)]

G.add_edges_from(edges)

# Vị trí các đỉnh (tự sắp xếp)
pos = {0: (0, 3), 1: (-1, 2), 2: (1, 2), 3: (-1, 1), 4: (0, 1), 5: (0, 0)}

plt.figure(figsize=(6, 5))

nx.draw(G, pos, with_labels=True, node_size=2000, font_size=12)

plt.title("Graph for BFS/DFS")
plt.show()


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, u):
        visited = [False] * (len(self.graph))
        queue = []
        visited[u] = True
        queue.append(u)

        # Duyet tim kiem
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

    print("BFS - duyet tim kiem chieu rong bat dau tu dinh 0")
    g.BFS(0)

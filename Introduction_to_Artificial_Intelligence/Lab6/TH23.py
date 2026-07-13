# THUC HANH 23
# Reinforcement Learning - FSSP_BFS

import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Huong di chuyen co the: len, xuong, trai, phai
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class FSSP_BFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    # Kiem tra vi tri co nam trong dang luoi & vi tri co bi chan hay khong
    def is_valid(self, position):
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    # Tim kiem theo chieu rong de tim duong di ngan nhat tu diem bat dau den diem ket thuc
    def bfs(self):
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])

        while queue:
            current, path = queue.popleft()

            # Neu vi tri hien tai la muc tieu, tra ve duong dan
            if current == self.goal:
                return path

            # Kham pha tat ca cac duong di co the (len, xuong, trai, phai)
            for move in MOVES:
                next_r, next_c = current[0] + move[0], current[1] + move[1]
                next_position = (next_r, next_c)

                if self.is_valid(next_position) and next_position not in visited:
                    visited.add(next_position)
                    queue.append((next_position, path + [next_position]))

        return None  # Tra ve None neu khong co duong dan den dich

    # Ham truc quan dang luoi va duong dan
    def visualize(self, path):
        grid_np = np.array(self.grid)

        # Tao hinh va truc so
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(grid_np, cmap="Greys", alpha=0.8)

        # Danh dau diem bat dau va diem ket thuc bang cac ky hieu dac biet
        ax.text(self.start[1], self.start[0], "Start", color="green", fontsize=25, fontweight="bold", ha="center", va="center")
        ax.text(self.goal[1], self.goal[0], "Goal", color="red", fontsize=25, fontweight="bold", ha="center", va="center")

        # Ve duong di neu tim thay
        if path:
            path_np = np.array(path)
            ax.plot(path_np[:, 1], path_np[:, 0], color="blue", linewidth=4.0, marker="o", markersize=10, markerfacecolor="yellow", label="Path")

        # Kieu dang luoi va gan nhan
        ax.set_xticks(np.arange(self.cols))
        ax.set_yticks(np.arange(self.rows))
        ax.set_xticklabels(np.arange(self.cols))
        ax.set_yticklabels(np.arange(self.rows))
        ax.grid(which="both", color="black", linewidth=2.0)

        # Add tieu de dang luoi va truc quan bieu do
        plt.title("Grid and Path Visualization", fontsize=20, fontweight="bold")
        plt.tight_layout()
        plt.show()


# Dang luoi (0 = o trong, 1 = chuong ngai vat)
grid = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
]

# Vi tri diem bat dau va diem dich
start = (0, 0)
goal = (5, 5)

# Ham FSSP_BFS - tim kiem chieu rong
planner = FSSP_BFS(grid, start, goal)
path = planner.bfs()

if path:
    print(f"Path found: {path}")
    # Truc quan duong dan
    planner.visualize(path)
else:
    print("No path found")

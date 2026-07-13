# THUC HANH 20
# Reinforcement Learning - duong di Me cung & dang luoi 6x6
# Vi tri (x, y) - doc cot truoc dong sau

maze_size = 6  # kich thuoc me cung
obstacles = [(0, 1), (1, 1), (4, 1), (4, 2), (3, 2), (4, 3), (3, 3), (3, 4), (0, 4), (3, 5)]  # vi tri vat can
start = (0, 0)  # bat dau
goal = (0, 5)   # ket thuc


# Kiem tra vi tri nhat dinh cua (x, y) co hop le di chuyen hay khong
def is_valid(x, y):
    return (0 <= x < maze_size) and (0 <= y < maze_size) and (x, y) not in obstacles


# Ham DFS
def dfs(current, visited, path):
    x, y = current
    if current == goal:
        path.append(current)
        return True

    visited.add(current)
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for move in moves:
        if is_valid(*move) and move not in visited:
            if dfs(move, visited, path):
                path.append(current)
                return True
    return False


# Ham DFS de tim duong di
visited = set()
path = []

if dfs(start, visited, path):
    path.reverse()
    print("Path found:")
    for position in path:
        print(position)
else:
    print("No path found!")

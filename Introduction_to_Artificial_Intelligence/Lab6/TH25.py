# THUC HANH 25
# Reinforcement Learning

import numpy as np

# Dinh nghia moi truong
maze_size = 4
start = (0, 0)
goal = (3, 3)

# Khoi tao gia tri Q
Q_table = np.zeros((maze_size, maze_size, 4))

# Sieu tham so
alpha = 0.1
gamma = 0.9
epsilon = 0.1


# Ham cap nhat gia tri Q
def update_Q_table(pos, action, reward, next_pos):
    Q_table[pos[0], pos[1], action] = Q_table[pos[0], pos[1], action] + alpha * (
        reward + gamma * np.max(Q_table[next_pos[0], next_pos[1], :]) - Q_table[pos[0], pos[1], action]
    )


# Ham chon hanh dong
def choose_action(pos):
    if np.random.rand() < epsilon:
        return np.random.randint(0, 4)
    else:
        return np.argmax(Q_table[pos[0], pos[1], :])


# Huan luyen Q-learning
for episode in range(10000):
    pos = start
    while pos != goal:
        action = choose_action(pos)
        next_pos = pos

        if action == 0 and pos[0] > 0:                 # len
            next_pos = (pos[0] - 1, pos[1])
        elif action == 1 and pos[0] < maze_size - 1:   # xuong
            next_pos = (pos[0] + 1, pos[1])
        elif action == 2 and pos[1] > 0:               # trai
            next_pos = (pos[0], pos[1] - 1)
        elif action == 3 and pos[1] < maze_size - 1:   # phai
            next_pos = (pos[0], pos[1] + 1)

        reward = 0
        if next_pos == goal:
            reward = 1
        elif next_pos == pos:
            reward = -1

        update_Q_table(pos, action, reward, next_pos)
        pos = next_pos

# Xuat ra gia tri Q
print("Bang gia tri Q")
print(Q_table)

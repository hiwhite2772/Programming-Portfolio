# THUC HANH 24
# Reinforcement Learning

import numpy as np
import matplotlib.pyplot as plt

# Cac sieu tham so
n_states = 16
n_actions = 4
goal_state = 15

Q_table = np.zeros((n_states, n_actions))

alpha = 0.1          # he so alpha
gamma = 0.9          # he so gamma
exploration_prob = 0.2
epochs = 1000        # he so tap

# Quy trinh cua Q_learning
for epoch in range(epochs):
    current_state = np.random.randint(0, n_states)

    while current_state != goal_state:
        # Kham pha so voi khai thac (e-chinh sach tham lam)
        if np.random.rand() < exploration_prob:
            action = np.random.randint(0, n_actions)
        else:
            action = np.argmax(Q_table[current_state])

        # Chuyen sang trang thai tiep theo
        next_state = (current_state + 1) % n_states

        # Phan thuong 1 neu dat duoc goal_state, 0 neu khong dat
        reward = 1 if next_state == goal_state else 0

        # Cap nhat gia tri Q
        Q_table[current_state, action] += alpha * (reward + gamma * np.max(Q_table[next_state]) - Q_table[current_state, action])

        # Cap nhat trang thai hien tai
        current_state = next_state

# Truc quan bang Q dang luoi
q_values_grid = np.max(Q_table, axis=1).reshape(4, 4)

# Bieu do dang luoi cac gia tri Q
plt.figure(figsize=(6, 6))
plt.imshow(q_values_grid, cmap="coolwarm", interpolation="nearest")
plt.colorbar(label="Q-value")
plt.title("Learned Q-values for each state")
plt.xticks(np.arange(4), ["0", "1", "2", "3"])
plt.yticks(np.arange(4), ["0", "1", "2", "3"])
plt.gca().invert_yaxis()  # bo cuc dang luoi
plt.grid(True)

# Cac gia tri Q dang luoi
for i in range(4):
    for j in range(4):
        plt.text(j, i, f"{q_values_grid[i, j]:.2f}", ha="center", va="center", color="black")

plt.show()

# Xuat ra bang Q da hoc
print("Learned Q-table:")
print(Q_table)

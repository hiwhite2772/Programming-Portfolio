import numpy as np
def is_valid_state(state, num_queens):
    return len(state) == num_queens
def get_candidates(state, num_queens):
    if not state:
        return range(num_queens)
    position = len(state)
    candidates = set(range(num_queens))
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates

def search(state, solutions, num_queens):
    if is_valid_state(state, num_queens):
        solutions.append(state.copy())
        print(f"Valid State Found: {state}")
        return
    
    for candidate in get_candidates(state, num_queens):
        state.append(candidate)
        search(state, solutions, num_queens)
        print(f"backtracking from: {state}")
        state.pop()

def solve(num_queens):
    solutions = []
    state = []
    search(state, solutions, num_queens)
    return solutions

if __name__ == "__main__":
    num_queens = int(input("Enter number of queens n: "))
    solutions = solve(num_queens)
    for solution in solutions:
        board = np.full((num_queens, num_queens), "-")
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        print(f"\nSolution: {solution}")
        print(board)
    print(f"Tổng số Giải pháp: {len(solutions)}")
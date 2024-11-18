def game_of_life(board):
    n = len(board)
    m = len(board[0])
    
    # Directions for the 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Create a copy of the original board to compute the next state
    next_board = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            live_neighbors = 0
            
            # Count live neighbors
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    live_neighbors += board[x][y]
            
            # Apply the rules of the Game of Life
            if board[i][j] == 1:  # Current cell is live
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[i][j] = 0  # Cell dies
                else:
                    next_board[i][j] = 1  # Cell lives
            else:  # Current cell is dead
                if live_neighbors == 3:
                    next_board[i][j] = 1  # Cell becomes alive
                else:
                    next_board[i][j] = 0  # Remains dead
    
    return next_board

# Input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
board = []
print("Enter the board:")
for _ in range(n):
    row = list(map(int, input().strip().split()))
    board.append(row)

# Get the next state
next_state = game_of_life(board)

# Output the next state
print("Next state:")
for row in next_state:
    print(' '.join(map(str, row)))

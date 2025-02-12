import random

def generate_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    for i in range(1, size-1):
        for j in range(1, size-1):
            maze[i][j] = ' ' if random.random() > 0.2 else '#' # 20% chance of being a wall
    maze[1][1] = 'P'  # Player start position
    maze[size-2][size-2] = 'E'  # Exit position
    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def move_player(maze, direction, pos):
    x, y = pos
    moves = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)} #directions to move
    if direction in moves:
        dx, dy = moves[direction]
        new_x, new_y = x + dx, y + dy
        if maze[new_x][new_y] == ' ' or maze[new_x][new_y] == 'E':
            maze[x][y] = ' '
            maze[new_x][new_y] = 'P'
            return (new_x, new_y)
    return pos

def play_game(size=10):
    maze = generate_maze(size)
    player_pos = (1, 1)
    
    print("Welcome to the Maze Escape Game!")
    print("Type 'exit' anytime to quit the game.")
    while True:
        print_maze(maze)
        print("u: up, d: down, l: left, r: right")
        move = input("Move (UDLR or 'exit' to quit): ").lower()
        if move == 'exit':
            print("You have exited the game. Goodbye!")
            break
        player_pos = move_player(maze, move, player_pos)
        if player_pos == (size-2, size-2):
            print("Congratulations! You escaped the maze!")
            break

if __name__ == "__main__":
    play_game()

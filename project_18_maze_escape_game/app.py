import random
import tkinter as tk
from tkinter import messagebox

def generate_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    for i in range(1, size-1):
        for j in range(1, size-1):
            maze[i][j] = ' ' if random.random() > 0.2 else '#'  # 20% chance of being a wall
    maze[1][1] = 'P'  # Player start position
    maze[size-2][size-2] = 'E'  # Exit position
    return maze

def print_maze(maze):
    return "\n".join([" ".join(row) for row in maze])

class MazeGameApp:
    def __init__(self, root, size=8):  # Adjusted maze size for a smaller display
        self.root = root
        self.size = size
        self.maze = generate_maze(self.size)
        self.player_pos = (1, 1)
        self.root.title("Maze Escape Game")
        self.root.geometry("400x400")  # Adjusted window size
        self.root.resizable(False, False)

        # Canvas to display the maze
        self.canvas = tk.Canvas(self.root, width=300, height=300)  # Smaller canvas size
        self.canvas.pack(pady=10)
        self.draw_maze()

        # Button panel for movement
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Adjusted button layout for smaller window
        self.up_button = tk.Button(self.button_frame, text="Up", command=lambda: self.move_player('u'))
        self.up_button.grid(row=0, column=1)

        self.left_button = tk.Button(self.button_frame, text="Left", command=lambda: self.move_player('l'))
        self.left_button.grid(row=1, column=0)

        self.down_button = tk.Button(self.button_frame, text="Down", command=lambda: self.move_player('d'))
        self.down_button.grid(row=1, column=1)

        self.right_button = tk.Button(self.button_frame, text="Right", command=lambda: self.move_player('r'))
        self.right_button.grid(row=1, column=2)

    def draw_maze(self):
        self.canvas.delete("all")  # Clear previous maze
        cell_size = 30  # Reduced size of each cell
        for i in range(self.size):
            for j in range(self.size):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                if self.maze[i][j] == '#':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif self.maze[i][j] == ' ':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                elif self.maze[i][j] == 'P':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                elif self.maze[i][j] == 'E':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    def move_player(self, direction):
        x, y = self.player_pos
        moves = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}  # Directions to move
        if direction in moves:
            dx, dy = moves[direction]
            new_x, new_y = x + dx, y + dy
            if self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == 'E':
                self.maze[x][y] = ' '
                self.player_pos = (new_x, new_y)
                self.maze[new_x][new_y] = 'P'
                self.draw_maze()

                # Check if the player reaches the exit
                if self.player_pos == (self.size-2, self.size-2):
                    messagebox.showinfo("Congratulations!🎉", "You won the game!")
                    self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeGameApp(root, size=8)  # Reduced size for smaller maze
    root.mainloop()

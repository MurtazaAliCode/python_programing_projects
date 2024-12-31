
import tkinter as tk

def set_tile(Row, Colomn):
    global current_player

    if game_over:
        return

    if board[Row][Colomn]["text"] != " ":
        return

    board[Row][Colomn]["text"] = current_player

    if current_player == playery:
        current_player = playerx
    else:
        current_player = playery

    label["text"] = f"Now {current_player}'s turn"

    check_winner()

def check_winner():
    global turn, game_over
    turn += 1

    # Horizontal check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != " "):
            label.config(text=f"{board[row][0]['text']} wins!", bg=colour_green)
            for col in range(3):
                board[row][col].config(bg=colour_green, fg=colour_red)
            game_over = True
            return

    # Vertical check
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
                and board[0][col]["text"] != " "):
            label.config(text=f"{board[0][col]['text']} wins!", bg=colour_green)
            for row in range(3):
                board[row][col].config(bg=colour_green, fg=colour_red)
            game_over = True
            return

    # Diagonal check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != " "):
        label.config(text=f"{board[0][0]['text']} wins!", bg=colour_green)
        for i in range(3):
            board[i][i].config(bg=colour_green, fg=colour_red)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != " "):
        label.config(text=f"{board[0][2]['text']} wins!", bg=colour_green)
        board[0][2].config(bg=colour_green, fg=colour_red)
        board[1][1].config(bg=colour_green, fg=colour_red)
        board[2][0].config(bg=colour_green, fg=colour_red)
        game_over = True
        return

    # Tie check
    if turn == 9:
        label.config(text="It's a tie!", bg=colour_yellow)
        game_over = True
        return

def restart_game():
    global turn, game_over, current_player

    turn = 0
    game_over = False
    current_player = playerx

    label.config(text=current_player + "'s turn", bg=colour_red)

    for row in range(3):
        for col in range(3):
            board[row][col].config(text=" ", bg=colour_gray, fg=colour_green)

# Game setup
playerx = "X"
playery = "O"
current_player = playerx
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

colour_gray = "#808080"
colour_red = "#FF0000"
colour_green = "#00FF00"
colour_yellow = "#FFFF00"

turn = 0
game_over = False

# Create the window
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# Create the game frame
game_frame = tk.Frame(window)
label = tk.Label(game_frame, text=current_player + "'s turn", font=("Arial", 20), bg=colour_red, fg="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for Row in range(3):
    for Colomn in range(3):
        board[Row][Colomn] = tk.Button(game_frame, text=" ", font=("Arial", 20), bg=colour_gray, fg=colour_green, width=5, height=2,
                                       command=lambda Row=Row, Colomn=Colomn: set_tile(Row, Colomn))
        board[Row][Colomn].grid(row=Row + 1, column=Colomn)

restart_button = tk.Button(game_frame, text="Restart", font=("Arial", 20), bg=colour_yellow, fg="black", width=10, height=1,
                           command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

game_frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

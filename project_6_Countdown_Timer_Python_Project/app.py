import tkinter as tk
from tkinter import messagebox

# Function to start the countdown
def start_timer():
    try:
        total_seconds = int(entry.get())  # Get user input
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Function to run the countdown
def countdown(time_left):
    if time_left >= 0:
        minutes, seconds = divmod(time_left, 60)
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.after(1000, countdown, time_left - 1)
    else:
        messagebox.showinfo("Timer Completed", "⏳ Time's up!")

# Function to reset the timer
def reset_timer():
    entry.delete(0, tk.END)
    timer_label.config(text="00:00")

# Function to toggle full screen
def toggle_fullscreen():
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

# Function to exit full screen
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# Creating Tkinter window
root = tk.Tk()
root.title("⏳ Countdown Timer")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2C3E50")  # Dark Background

# Centering the window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Heading Label
title_label = tk.Label(root, text="Countdown Timer", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

# Entry for user input
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Timer Display Label (Centered)
timer_label = tk.Label(root, text="00:00", font=("Arial", 32, "bold"), bg="#34495E", fg="white", width=10)
timer_label.pack(pady=20)

# Buttons Frame
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

# Start Button
start_button = tk.Button(button_frame, text="Start", font=("Arial", 12), bg="#27AE60", fg="white", command=start_timer)
start_button.grid(row=0, column=0, padx=5)

# Reset Button
reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12), bg="#E74C3C", fg="white", command=reset_timer)
reset_button.grid(row=0, column=1, padx=5)

# Full Screen Button
fullscreen_button = tk.Button(button_frame, text="Full Screen", font=("Arial", 12), bg="#2980B9", fg="white", command=toggle_fullscreen)
fullscreen_button.grid(row=0, column=2, padx=5)

# Bind ESC key to exit full screen
root.bind("<Escape>", exit_fullscreen)

# Run the Tkinter loop
root.mainloop()

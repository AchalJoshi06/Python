import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def roll():
    return random.randint(1, 6)

# Initialize the game
def start_game():
    global players, players_score, current_player, current_score
    players = int(num_players_var.get())
    players_score = [0 for _ in range(players)]
    current_player = 0
    current_score = 0
    update_game_info()
    roll_button.config(state="normal")
    next_button.config(state="normal")
    num_players_entry.config(state="disabled")  # disable entry during game
    start_button.config(state="disabled")       # disable start button during game

def player_turn():
    global current_player, current_score
    value = roll()
    update_dice_image(value)

    if value == 1:
        current_score = 0
        next_turn()
    else:
        current_score += value
        score_label.config(text=f"Current Score: {current_score}")

def next_turn():
    global current_player, current_score, players_score
    players_score[current_player] += current_score
    current_score = 0

    if max(players_score) >= max_score:
        announce_winner()
        return

    current_player = (current_player + 1) % players
    update_game_info()

def announce_winner():
    highest = max(players_score)
    winners = [i + 1 for i, s in enumerate(players_score) if s == highest]
    if len(winners) > 1:
        messagebox.showinfo("Game Over", f"Tie! Players {', '.join(map(str, winners))} win with {highest} points!")
    else:
        messagebox.showinfo("Game Over", f"Player {winners[0]} wins with a score of {highest}!")
    roll_button.config(state="disabled")
    next_button.config(state="disabled")

def update_game_info():
    info_label.config(text=f"Player {current_player + 1}'s Turn\nTotal Score: {players_score[current_player]}")
    score_label.config(text="Current Score: 0")
    update_dice_image(0)  # clear dice image at start of turn

def update_dice_image(value):
    if value == 0:
        dice_label.config(image="")
        dice_label.image = None
    else:
        img = dice_images[value]
        dice_label.config(image=img)
        dice_label.image = img

# Main game variables
max_score = 50
players = 0
players_score = []
current_player = 0
current_score = 0

# Create the main window
root = tk.Tk()
root.title("Dice Game")
root.geometry("400x400")

# --- FIXED: Load dice images using script's directory ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dice_images = {
    i: ImageTk.PhotoImage(
        Image.open(os.path.join(BASE_DIR, f"dice_{i}.png")).resize((100, 100))
    )
    for i in range(1, 7)
}

# Validate number of players input
num_players_var = tk.StringVar(value="2")

def validate_players_input():
    try:
        value = int(num_players_var.get())
        if value < 2 or value > 4:
            raise ValueError
        start_button.config(state="normal")
    except ValueError:
        start_button.config(state="disabled")

num_players_var.trace_add("write", lambda *args: validate_players_input())

# GUI elements
tk.Label(root, text="Number of Players (2-4):").pack()
num_players_entry = tk.Entry(root, textvariable=num_players_var)
num_players_entry.pack()
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

info_label = tk.Label(root, text="Game Info", font=("Arial", 14))
info_label.pack(pady=10)
score_label = tk.Label(root, text="Current Score: 0", font=("Arial", 12))
score_label.pack()

dice_label = tk.Label(root)
dice_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll Dice", state="disabled", command=player_turn)
roll_button.pack()

next_button = tk.Button(root, text="End Turn", state="disabled", command=next_turn)
next_button.pack()

# Start the main loop
root.mainloop()

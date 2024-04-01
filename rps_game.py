import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a round
def play_round():
    global round_number
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    animate_choices(user_choice, computer_choice, result)
    update_scores(result)

    # Increment round number and update round label
    round_number += 1
    round_label.config(text=f"Round: {round_number}")

# Function to reset the game
def reset_game():
    global round_number
    user_choice_menu.config(state="active")
    play_button.config(state="active")
    user_score.set(0)
    computer_score.set(0)
    user_choice_var.set("Rock")
    result_label.config(text="")
    user_choice_label.config(text="Choose Rock, Paper, or Scissors:")
    computer_choice_label.config(text="")
    round_number = 1
    round_label.config(text=f"Round: {round_number}")
    update_score_labels()  # Reset score labels

# Function to update scores
def update_scores(result):
    if result == "You win!":
        user_score.set(user_score.get() + 1)
    elif result == "Computer wins!":
        computer_score.set(computer_score.get() + 1)

    update_score_labels()  # Update score labels

# Function to update score labels
def update_score_labels():
    user_score_label.config(text=f"Your Score: {user_score.get()}")
    computer_score_label.config(text=f"Computer Score: {computer_score.get()}")

# Function to animate choices and result
def animate_choices(user_choice, computer_choice, result):
    user_choice_menu.config(state="disabled")
    reset_button.config(state="active")

    for _ in range(5):
        user_choice_label.config(text=random.choice(choices))
        computer_choice_label.config(text=random.choice(choices))
        window.update()
        time.sleep(0.2)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    result_label.config(text=result)
    window.update()
    time.sleep(2)
    user_choice_menu.config(state="active")
    play_button.config(state="active")
    reset_button.config(state="active")

# Function to show the About page
def show_about():
    about_text = "Rock-Paper-Scissors Game\nVersion 1.0\n\nCreated by Anmol Yaseen\n© 2023"
    messagebox.showinfo("About", about_text)

# Function to show the User Guide
def show_user_guide():
    user_guide_text = """
    Rock-Paper-Scissors Game User Guide

    1. Playing the Game:
        - Choose Rock, Paper, or Scissors from the dropdown menu.
        - Click the 'Play' button to play a round.

    2. Winning a Round:
        - Rock beats Scissors.
        - Scissors beats Paper.
        - Paper beats Rock.

    3. Resetting the Game:
        - Click the 'Reset' button to start a new game.

    4. About:
        - Click the 'About' option in the menu to view information about the game.
    """
    messagebox.showinfo("User Guide", user_guide_text)

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create style for widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TLabel", font=("Helvetica", 14), padding=10)

# Create labels and buttons
title_label = ttk.Label(window, text="Rock-Paper-Scissors Game", style="TLabel", foreground="blue")
title_label.pack(pady=10)

user_choice_label = ttk.Label(window, text="Choose Rock, Paper, or Scissors:", style="TLabel")
user_choice_label.pack()

choices = ["Rock", "Paper", "Scissors"]
user_choice_var = tk.StringVar()
user_choice_var.set("Rock")  # Default choice
user_choice_menu = ttk.Combobox(window, textvariable=user_choice_var, values=choices, font=("Helvetica", 12))
user_choice_menu.pack()

play_button = ttk.Button(window, text="Play", command=play_round, style="TButton")
play_button.pack()

result_label = ttk.Label(window, text="", style="TLabel", font=("Helvetica", 18))
result_label.pack()

user_choice_label = ttk.Label(window, text="", style="TLabel")
user_choice_label.pack()

computer_choice_label = ttk.Label(window, text="", style="TLabel")
computer_choice_label.pack()

user_score = tk.IntVar()
computer_score = tk.IntVar()

user_score_label = ttk.Label(window, text="Your Score: 0", style="TLabel", font=("Helvetica", 12), foreground="green")
user_score_label.pack(padx=10)

computer_score_label = ttk.Label(window, text="Computer Score: 0", style="TLabel", font=("Helvetica", 12), foreground="red")
computer_score_label.pack(padx=10)

round_number = 1
round_label = ttk.Label(window, text=f"Round: {round_number}", style="TLabel")
round_label.pack(pady=10)

reset_button = ttk.Button(window, text="Reset", command=reset_game, style="TButton", state="active")
reset_button.pack()

# Create the main menu
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# Create the "Help" menu with "User Guide" and "About" options
help_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="User Guide", command=show_user_guide)
help_menu.add_command(label="About", command=show_about)

# Start the GUI main loop
window.mainloop()

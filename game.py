import tkinter as tk
import random
import winsound  # For Windows sound effects

choices = ["Rock", "Paper", "Scissors"]  # spelled correctly now

user_score = 0
computer_score = 0
fullscreen = False  # track fullscreen state


def play_sound(result):
    try:
        if result == "You Win!":
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
        elif result == "You Lose!":
            winsound.MessageBeep(winsound.MB_ICONHAND)
        else:
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    except:
        pass


def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
            (user_choice == "Scissors" and comp_choice == "Paper") or \
            (user_choice == "Paper" and comp_choice == "Rock"):
        return "User"
    else:
        return "Computer"


def animate_button(btn):
    original_color = btn.cget("bg")
    btn.config(bg="#ffeb3b")  # bright yellow flash
    root.after(200, lambda: btn.config(bg=original_color))


def play(user_choice):
    global user_score, computer_score
    comp_choice = random.choice(choices)

    winner = decide_winner(user_choice, comp_choice)

    user_choice_label.config(text=f"Your choice: {user_choice}", fg="#2962ff")
    comp_choice_label.config(text=f"Computer's choice: {comp_choice}", fg="#d32f2f")

    if winner == "Tie":
        result_label.config(text="It's a Tie!", fg="#f9a825")  # amber
        play_sound("Tie")
    elif winner == "User":
        user_score += 1
        result_label.config(text="You Win!", fg="#388e3c")  # green
        play_sound("You Win!")
    else:
        computer_score += 1
        result_label.config(text="You Lose!", fg="#d32f2f")  # red
        play_sound("You Lose!")

    score_label.config(text=f"Scores - You: {user_score} | Computer: {computer_score}", fg="#00796b")  # teal

    play_again_btn.config(state=tk.NORMAL, bg="#43a047")


def reset_game():
    user_choice_label.config(text="Make your choice:", fg="white")
    comp_choice_label.config(text="", fg="white")
    result_label.config(text="", fg="white")
    play_again_btn.config(state=tk.DISABLED, bg="#555")


def on_choice_click(choice, btn):
    animate_button(btn)
    for b in choice_buttons:
        b.config(state=tk.DISABLED)
    play(choice)


def play_again():
    reset_game()
    for btn in choice_buttons:
        btn.config(state=tk.NORMAL)


def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    if fullscreen:
        fullscreen_btn.config(text="Exit Fullscreen")
    else:
        fullscreen_btn.config(text="Fullscreen")


root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("450x350")
root.configure(bg="#263238")  # dark blue gray background
root.resizable(True, True)  # allow resizing

# Fullscreen toggle button at the top
fullscreen_btn = tk.Button(root, text="Fullscreen", font=("Arial", 12), bg="#1976d2", fg="white",
                           activebackground="#64b5f6", command=toggle_fullscreen)
fullscreen_btn.pack(pady=(10, 0))

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 16, "bold"), bg="#263238",
                             fg="#fff176")  # yellow
instruction_label.pack(pady=15)

btn_frame = tk.Frame(root, bg="#263238")
btn_frame.pack()

choice_buttons = []
button_colors = {"Rock": "#ef5350", "Paper": "#42a5f5", "Scissors": "#66bb6a"}  # red, blue, green

for choice in choices:
    btn = tk.Button(btn_frame, text=choice, width=12, font=("Arial", 14, "bold"),
                    bg=button_colors[choice], fg="white", activebackground="#ffee58",
                    command=lambda c=choice, b=None: on_choice_click(c, b))
    btn.pack(side=tk.LEFT, padx=15, pady=10)
    choice_buttons.append(btn)

for btn, choice in zip(choice_buttons, choices):
    btn.config(command=lambda c=choice, b=btn: on_choice_click(c, b))

user_choice_label = tk.Label(root, text="Make your choice:", font=("Arial", 14), bg="#263238", fg="white")
user_choice_label.pack(pady=10)

comp_choice_label = tk.Label(root, text="", font=("Arial", 14), bg="#263238", fg="white")
comp_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="#263238")
result_label.pack(pady=15)

score_label = tk.Label(root, text="Scores - You: 0 | Computer: 0", font=("Arial", 14), bg="#263238",
                       fg="#4db6ac")  # lighter teal
score_label.pack(pady=5)

play_again_btn = tk.Button(root, text="Play Again", font=("Arial", 14), bg="#555", fg="white",
                           activebackground="#43a047", state=tk.DISABLED, command=play_again)
play_again_btn.pack(pady=15)

root.mainloop()

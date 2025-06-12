import tkinter as tk


def is_operator(c):
    return c in "+-*/"


def adjust_font_size():
    length = len(entry.get())
    if length < 10:
        entry.config(font=("Arial", 40))
    elif length < 15:
        entry.config(font=("Arial", 30))
    elif length < 20:
        entry.config(font=("Arial", 24))
    else:
        entry.config(font=("Arial", 18))


def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            result = str(eval(current, {"__builtins__": None}, {}))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    elif text == "←":
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

    elif is_operator(text):
        if current:
            if is_operator(current[-1]):
                entry.delete(len(current) - 1, tk.END)
            entry.insert(tk.END, text)

    elif text == ".":
        tokens = current.split()
        if '.' not in tokens[-1] if tokens else current:
            entry.insert(tk.END, text)
        elif not current:
            entry.insert(tk.END, "0.")
    else:
        entry.insert(tk.END, text)

    adjust_font_size()


def key_press(event):
    key = event.char
    current = entry.get()

    if key in "0123456789":
        entry.insert(tk.END, key)

    elif key in "+-*/":
        if current:
            if is_operator(current[-1]):
                entry.delete(len(current) - 1, tk.END)
            entry.insert(tk.END, key)

    elif key == ".":
        tokens = current.split()
        if '.' not in tokens[-1] if tokens else current:
            entry.insert(tk.END, key)

    elif key == "\r":  # Enter
        try:
            result = str(eval(current, {"__builtins__": None}, {}))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif key == "\x08":  # Backspace
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

    elif key == "\x1b":  # Escape
        entry.delete(0, tk.END)

    adjust_font_size()


# Main window
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("450x500")
root.bind("<Key>", key_press)

# Entry field
entry = tk.Entry(root, font=("Arial", 40), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["←"]
]

button_colors = {
    "C": ("red", "white"),
    "=": ("green", "white"),
    "←": ("orange", "white"),
    "+": ("#1e90ff", "white"),
    "-": ("#1e90ff", "white"),
    "*": ("#1e90ff", "white"),
    "/": ("#1e90ff", "white"),
}

# Create buttons
for i, row in enumerate(button_texts):
    for j, btn_text in enumerate(row):
        bg_color, fg_color = button_colors.get(btn_text, ("lightgray", "black"))
        btn = tk.Button(root, text=btn_text, font="Arial 18", bg=bg_color, fg=fg_color)

        if btn_text == "←":
            btn.grid(row=i + 1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        else:
            btn.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)

        btn.bind("<Button-1>", click)

# Make grid responsive
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()

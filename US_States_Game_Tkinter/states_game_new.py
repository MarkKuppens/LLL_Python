import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk

# Load Data
data = pd.read_csv("50_states_new.csv")

# Screen
root = tk.Tk()
root.title("U.S. State Quiz")

# Background image
image_path = "blank_states_img.gif"
image = Image.open(image_path)
image = image.resize((725, 491))
bg_image = ImageTk.PhotoImage(image)

# Canvas for map begin @ 0.0 North West
canvas = tk.Canvas(root, width=725, height=491)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_image)

guessed_states = []

# Tkinter uses (0,0) as the left corner so coördinates are different as original csv in Turtle
def transform_coordinates(x, y):
    return x, y

def write_state(name, x, y):
    x, y = transform_coordinates(x, y)
    canvas.create_text(x, y, text=name, font=("Arial", 8, "bold"), fill="black")

# Check input
def check_state():
    state = entry.get().strip().title()
    if state.lower() == "exit":
        save_not_guessed_states()
        root.quit()
    elif state in data["state"].values and state not in guessed_states:
        guessed_states.append(state)
        state_data = data[data["state"] == state]
        x, y = int(state_data.x.iloc[0]), int(state_data.y.iloc[0])
        write_state(state, x, y)
        result_label.config(text=f"Correct guesses: {len(guessed_states)}/50")
        entry.delete(0, tk.END)
        if len(guessed_states) == 50:
            messagebox.showinfo("Congratulations!", "You've guessed all the states")
    elif state in guessed_states:
        messagebox.showwarning("Please note!", "You have already entered this state.")
    else:
        messagebox.showerror("Wrong!", "No Valid State!")

def save_not_guessed_states():
    not_guessed_states = [state for state in data["state"].values if state not in guessed_states]
    not_guessed_states_df = pd.DataFrame(not_guessed_states, columns=["state"])
    not_guessed_states_df.to_csv("states_to_learn.csv", index=False)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="What's another state's name?", font=("Arial", 14))
input_label.pack(side="left")

# Input & Button
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<Return>", lambda event: check_state())
submit_button = tk.Button(root, text="Check", command=check_state, font=("Arial", 12))
submit_button.pack(pady=5)

# Result
result_label = tk.Label(root, text="Correct guesses: 0/50", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()

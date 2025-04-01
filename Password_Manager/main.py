from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(4, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 6))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    new_data = {website: {
                    "email": username,
                    "password": password,
                }
    }

    if len(website) == 0  or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------- FIND PASSWORD -----------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n\n"
                                                       f"Password: {password}\n\n")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", anchor="w")
website_label.grid(row=1, sticky="W")

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email_user_name = Label(text="Email/Username: ", anchor="w")
email_user_name.grid(row=2, sticky="W")

user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, string="markkuppens74@gmail.com")

password_label = Label(text="Password: ", anchor="w")
password_label.grid(row=3, sticky="W")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

button_generate = Button(text="Generate Password", highlightthickness=0, width=15, command=generate_password)
button_generate.grid(column=2, row=3)

button_search = Button(text="Search", highlightthickness=0, width=15, command=find_password)
button_search.grid(column=2, row=1)

button_add = Button(text="Add", width=45, highlightthickness=0, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)





window.mainloop()
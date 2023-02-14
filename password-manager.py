import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


def search():
    search_website = website_input.get()
    with open("data.json", mode="r") as read_file:
        data = json.load(read_file)
        try:
            messagebox.showinfo("Info",
                                f"Email: {data[search_website]['email']}\n Password: {data[search_website]['password']}")
        except KeyError:
            messagebox.showerror("Error", "The details for this website have not been stored.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    generated_password = ''.join([str(elem) for elem in password_list])
    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    data_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning("Error", "Don't leave any fields empty.")
    else:
        try:
            with open(file="data.json", mode="r") as read_file:
                data = json.load(read_file)
                data.update(data_dict)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(data_dict, file, indent=4)
        else:
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)

        pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=40, pady=40)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=15)
website_input.grid(row=1, column=1, sticky="EW")
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "ombhutki@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=15)

password_input.grid(row=3, column=1, sticky="EW")

generate_pass = Button(text="Generate Password", width=14, command=generate_password)
generate_pass.grid(row=3, column=2, sticky="EW")

add_to_file = Button(text="Add", width=36, command=save_password)
add_to_file.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()

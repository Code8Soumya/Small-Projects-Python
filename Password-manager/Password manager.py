from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_l = [random.choice(letters) for _ in range(nr_letters)]
    password_s = [random.choice(symbols) for _ in range(nr_symbols)]
    password_n = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_l + password_s + password_n
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    web = web_entry.get()
    user = user_entry.get()
    keyword = password_entry.get()
    is_ok = False

    new_data = {
        web: {"email": user,
              "password": keyword,
              }
    }

    if len(web) == 0 or len(keyword) == 0 or len(user) == 0:
        messagebox.showwarning(title="Password Manager", message="OOPS! Please fill all required fields.")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager",
                                       message=f"These are the details entered: \nUser: {user}"
                                               f"\nPassword: {keyword} \nIs it ok to save?")
    if is_ok:

        try:
            f = open("Password-manager/Password.json", "r")
            data = json.load(f)
        except FileNotFoundError:
            f = open("Password-manager/Password.json", "w")
            json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            f = open("Password-manager/Password.json", "w")
            json.dump(data, f, indent=4)

        web_entry.delete(0, END)
        password_entry.delete(0, END)


def search_data():
    if len(web_entry.get()) == 0:
        messagebox.showinfo(title="Password Manager", message=f"Please fill the website field.")
    else:
        try:
            web_required = web_entry.get()
            f = open("Password-manager/Password.json", "r")
            data = json.load(f)
            data_dict = data[web_required]
            password = data_dict["password"]
            email = data_dict["email"]
        except FileNotFoundError:
            messagebox.showinfo(title="Password Manager", message=f"No data is stored.")
        except KeyError:
            messagebox.showinfo(title="Password Manager", message=f"The details for the website can not be found!")
        else:
            messagebox.showinfo(title="Password Manager", message=f"The details for the website '{web_required}' is:"
                                                                  f"\nEmail: {email}"
                                                                  f"\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")

canvas = Canvas(width=200, height=190, highlightthickness=0)
logo = PhotoImage(file="Password-manager/logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(column=2, row=1, padx=20, pady=20)

web_name = Label(text="Website", font=("courier", 10, "bold"))
web_name.grid(column=1, row=2, sticky="nsew")

web_entry = Entry(font=("courier", 10, "bold"), width=35)
web_entry.grid(column=2, row=2, sticky="nsew")
web_entry.focus()

user_name = Label(text="Email/Username", font=("courier", 10, "bold"))
user_name.grid(column=1, row=3, sticky="nsew")

user_entry = Entry(font=("courier", 10, "bold"), width=35)
user_entry.grid(column=2, row=3, columnspan=2, sticky="nsew")
user_entry.insert(0, "Soumya@gmail.com")

password_name = Label(text="Password", font=("courier", 10, "bold"))
password_name.grid(column=1, row=4, sticky="nsew")

password_entry = Entry(font=("courier", 10, "bold"), width=17)
password_entry.grid(column=2, row=4, sticky="nsew")

generate_pass = Button(text="Generate password", font=("courier", 10, "bold"), command=generate_password)
generate_pass.grid(column=3, row=4, sticky="nsew")

add = Button(text="Add", font=("courier", 10, "bold"), width=36, command=add)
add.grid(column=2, row=5, columnspan=2, sticky="nsew")

search = Button(text="Search", font=("courier", 10, "bold"), command=search_data)
search.grid(column=3, row=2, sticky="nsew")

window.mainloop()

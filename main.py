from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    new_password = "".join(password_list)
    password_imp.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
f = open("data.txt", "a")


def save():
    if len(web_inp.get()) != 0 and len(password_imp.get()) != 0:
        messagebox.askokcancel(title=web_inp.get(), message=f"these are the details entered:\nEmail:{username.get()}"
                                                            f"\nPassword: {password_imp.get()} \n is ok to save?")
        f.write(f"\nweb site:{web_inp.get()}\n")
        f.write(f"username:{username.get()}\n")
        f.write(f"password:{password_imp.get()}\n")
        password_imp.delete(0, END)
        web_inp.delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="please don´t leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_site = Label(text="Website:", font=(FONT_NAME, 15, "bold"))
web_site.grid(column=0, row=1)
web_inp = ttk.Entry(width=35)
web_inp.focus()
web_inp.grid(column=1, row=1, columnspan=2)

Email = Label(text="Email/Username:", font=(FONT_NAME, 15, "bold"))
Email.grid(column=0, row=2)
username = ttk.Entry(width=35)
username.grid(column=1, row=2, columnspan=2)
username.insert(0, "francobringas17@gmail.com")

password = Label(text="Password:", font=(FONT_NAME, 15, "bold"))
password.grid(column=0, row=3)
password_imp = ttk.Entry(width=18)
password_imp.grid(column=1, row=3)

generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

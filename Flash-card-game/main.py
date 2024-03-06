from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("Flash-card-game/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except:
    data = pandas.read_csv("Flash-card-game/french_words.csv")
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    global flip_timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)
    flip_timer = window.after(3000, func=next_card)

def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Flash-card-game/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="Flash-card-game/card_front.png")
back_image = PhotoImage(file="Flash-card-game/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0,columnspan=2,sticky="nsew")

cross_image = PhotoImage(file="Flash-card-game/wrong.png")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, activebackground=BACKGROUND_COLOR, bd=1, activeforeground=BACKGROUND_COLOR, relief="flat", command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="Flash-card-game/right.png")
known_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, activebackground=BACKGROUND_COLOR, bd=1, activeforeground=BACKGROUND_COLOR, relief="flat", command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
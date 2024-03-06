
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer",fg=GREEN)
    check.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 0:
        count_down(5)
    elif reps == 1 or reps == 5 or reps == 3 or reps == 7:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global time
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodora-app/tomato.png")
canvas.create_image(100, 112,image=tomato_img)
timer_text =  canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start = Button(text="Start", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0, activebackground=YELLOW, bd=1, activeforeground=GREEN, relief="flat", command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0, activebackground=YELLOW, bd=1, activeforeground=GREEN, relief="flat", command=reset_timer)
reset.grid(column=3, row=3)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0)
timer.grid(column=2, row=1)

check = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0)
check.grid(column=2, row=3)




window.mainloop()

import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, marks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    marks = ""
    check_marks.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    working_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work")
        count_down(working_secs)
    elif reps == 8:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, marks
    sec = count % 60
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    if reps % 2 == 0:
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=80, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(102, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(row=3, column=1)
window.mainloop()

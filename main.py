from tkinter import *
import time
import math

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
is_started = FALSE
counter = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_all():
    global reps
    global is_started

    reps = 0
    is_started = False
    ok_label.config(text=" ")
    title_label.config(text="Timer")
    window.after_cancel(counter)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global is_started

    is_started = True
    reps +=1

    if reps % 8 == 0:
        title_label.config(text="Długa przerwa")
        time = LONG_BREAK_MIN*60
        count_down(time)
    elif reps % 2 == 0:
        title_label.config(text="Krótka przerwa")
        time = SHORT_BREAK_MIN*60
        count_down(time)
    else:
        title_label.config(text="Praca")
        time = WORK_MIN*60
        count_down(time)


def start_button():
    if is_started:
        pass
    else:
        start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global counter
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0{}".format(count_sec)

    canvas.itemconfig(timer_text, text="{}:{}".format(count_min, count_sec))
    if count > 0:
        counter = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            reps_dispaly = "✔" * (int(reps/2))
            ok_label.config(text="{}".format(reps_dispaly))
# ---------------------------- UI SETUP ------------------------------- #'
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(500, 282)



canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

ok_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)

start_button = Button(text="Start", command=start_button)
reset_button = Button(text="Reset", command=reset_all)


title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

ok_label.grid(row=3, column=1)





window.mainloop()



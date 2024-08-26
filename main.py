from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ECFFE6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    print(count)
    if count > 0:
        # count -= 1
        canvas.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# grid
rows = 4
columns = 3
for row in range(rows):
    if row == 1:
        window.grid_rowconfigure(index=row, weight=2)
    window.grid_rowconfigure(index=row, weight=1)
for col in range(columns):
    if col == 1:
        window.grid_columnconfigure(index=col, weight=2)
    window.grid_columnconfigure(index=col, weight=1)

# Canvas
canvas = Canvas(width=200, height=254, background=YELLOW, highlightthickness=0)  # highlight thickness >> remove frame
tomato_img = PhotoImage(file="tomato.png")  # write Address
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill=WHITE)
canvas.grid_configure(row=1, column=1)

# Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid_configure(row=0, column=1)

check_label = Label(text="✔", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid_configure(row=3, column=1)

# Buttons
start_btn = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=WHITE, bd=0, padx=0, pady=0, highlightthickness=0,
                   command=start_timer)
start_btn.grid_configure(row=2, column=0)

reset_btn = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=WHITE, bd=0, padx=0, pady=0, highlightthickness=0)
reset_btn.grid_configure(row=2, column=2)

window.mainloop()

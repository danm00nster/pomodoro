
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
Timer_a = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    window.after_cancel(Timer_a)
    canvas.itemconfig(timer,text="00:00")
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def strat_timer():
    global reps
    reps+=1
    if reps % 2 ==0:
        time=SHORT_BREAK_MIN*60
        tytul.config(text="PRZERWA")
    elif reps % 8 ==0:
        time=LONG_BREAK_MIN*60
        tytul.config(text="dluga przerwa")
    else:
        time=WORK_MIN*60
        tytul.config(text="PRACA")

    count_down(time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    minet=math.floor(count/60)
    secunds=count%60
    if secunds<10:
        secunds=f"0{secunds}"

    canvas.itemconfig(timer,text=f"{minet}:{secunds}")
    if count >0:
        global Timer_a
        Timer_a = window.after(100,count_down,count -1)
    else:
        strat_timer()
        marks=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg=YELLOW)




tomato_img=PhotoImage(file="tomato.png")
canvas=Canvas(width=200, height=233, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer=canvas.create_text(100,130,text="00:00", fill="white", font=("arial",24,"bold"))
canvas.grid(column=2,row=2)
tytul=Label(text="Timer",foreground=GREEN,bg=YELLOW,font=("arial",27,"bold"))
check=Label(text=(""),foreground=GREEN,bg=YELLOW,font=("arial",27,"bold"))
check.grid(column=2,row=4)
tytul.grid(column=2,row=1)
reset_button=Button(text="reset", command=reset_timer)
start_button=Button(text="start", command=strat_timer)
reset_button.grid(column=1,row=3)
start_button.grid(column=3,row=3)


window,mainloop()
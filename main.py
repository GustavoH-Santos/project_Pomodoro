from tkinter import *
import random
import os
import math

from main import start

# constants #
FONT_NAME = "Courier"
RED = "#e7305b"
YELLOW = "#f7f5dd"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25

reps = 0
# Functions Setup #

def countdown(count):
    #cronometro utilizando math library#
    count_min = math.floor(count /60) # retorna o maior numero inteiro menor que o parametro
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text_id, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    #if count == 0 and count_sec == 1:
    else:
        start()
        check_mark()


def check_mark():
    check_mark = Label(text="", fg="white", bg="black", font=(FONT_NAME, 33, "bold"))
    check_mark.grid(column=2, row=4)
    mark = ""
    work_sessions = math.floor(reps/2)
    for i in range(work_sessions):   
        mark += " ✔" 
    check_mark.config(text=mark)    


def start():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title.config(text="Deveras Pausa!", fg="green", bg="black")
        countdown(long_break)

    elif reps % 2 == 0:
        title.config(text="Mini Pausa", fg=YELLOW, bg="black")
        countdown(short_break)
    else:
        title.config(text="♬ Work♫ ♬ wooRK ♫ ♬ WOrk♪", fg=RED, bg="black",font=(FONT_NAME,20,"bold"))
        countdown(work_seconds)

    start_button["state"] = "disabled"
    
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text_id, text="00:00")
    global reps
    reps = 0
    start_button["state"] = "active"

# GUI Setup #

window = Tk()
window.title("MOnaPRodutiva")
window.config(padx=80, pady=40)
window["background"] = "black"

title = Label(text="PROdutivaMONa!", font=(FONT_NAME,40, "bold"), fg="white", bg="black")
title.grid(column=2, row=1)

canvas = Canvas(width=200, height=224)
    #random choice of item in another folder

list_mona = os.listdir("png_mona")
monalisa_image = PhotoImage(file=f"png_mona/{random.choice(list_mona)}")

canvas.create_image(103, 112, image=monalisa_image)
canvas["background"] = "black"

timer_text_id = canvas.create_text(100, 200, text= "00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row= 2)

#Buttons

start_button = Button(text="Start", bg="black", fg="white", font=(FONT_NAME, 15, 'bold'), command=start)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg="black", fg="white", font=(FONT_NAME, 15, "bold"), command=reset)
reset_button.grid(column=3, row=3)


window.mainloop()
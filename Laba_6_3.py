from tkinter import Tk
from tkinter import Canvas
from time import sleep


def red():
    c.itemconfig(circle_red, fill="red")
    window.update()
    sleep(5)
    c.itemconfig(circle_red, fill="gray")


def yellow():
    c.itemconfig(circle_yellow, fill="yellow")
    window.update()
    sleep(1)
    c.itemconfig(circle_yellow, fill="gray")


def green():
    c.itemconfig(circle_green, fill="green")
    window.update()
    sleep(5)
    c.itemconfig(circle_green, fill="gray")


window = Tk()
window.title('Светoфор')

c = Canvas(window, width=400, height=700, bg="cyan")
c.create_rectangle((100, 50, 250, 510), fill="black", outline="black")
c.create_rectangle((165, 510, 185, 700), fill="gray")
circle_red = c.create_oval((110, 60, 240, 190), fill="gray", outline="black")
circle_yellow = c.create_oval((110, 215, 240, 345), fill="gray", outline="black")
circle_green = c.create_oval((110, 370, 240, 500), fill="gray", outline="black")
c.pack()

i = 0
while i < 5:
    red()
    yellow()
    green()
    yellow()
    i += 1

window.mainloop()

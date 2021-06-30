from tkinter import Tk
from tkinter import Canvas
from time import sleep


window = Tk()
window.title('Move')
window.resizable(0, 0)

c = Canvas(window, width=500, height=500, bg="white")
circle = c.create_oval((150, 150, 120, 120), fill="blue")
c.pack()
x, y = 2, 3
for i in range(10000):
    circle_left, circle_top, circle_right, circle_bot = c.coords(circle)
    c.move(circle, x, y)
    window.update()
    sleep(0.01)
    if circle_right > 500:
        x = -2
        c.itemconfig(circle, fill="black")
    if circle_bot > 500:
        y = -3
        c.itemconfig(circle, fill="green")
    if circle_left < 0:
        x = 2
        c.itemconfig(circle, fill="red")
    if circle_top < 0:
        y = 3
        c.itemconfig(circle, fill="blue")


window.mainloop()

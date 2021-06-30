from tkinter import Tk
from tkinter import Canvas
import time

petrol_type = 0
lit = ""
i = 0

window = Tk()
window.title('AZS N&B')
window.resizable(0, 0)

c = Canvas(width=700, height=400, bg='grey80')
c.pack()

# Создание геометричесих фигур
but_92 = c.create_oval((25, 100, 50, 125), fill="blue", outline="black")
but_95 = c.create_oval((25, 175, 50, 200), fill="blue", outline="black")
but_98 = c.create_oval((25, 250, 50, 275), fill="blue", outline="black")
word_92 = c.create_rectangle((75, 100, 150, 125), fill="white", outline="black")
word_95 = c.create_rectangle((75, 175, 150, 200), fill="white", outline="black")
word_98 = c.create_rectangle((75, 250, 150, 275), fill="white", outline="black")
main_word = c.create_rectangle((150, 0, 550, 50), fill="white", outline="black")
char_1 = c.create_oval((225, 100, 250, 125), fill="green", outline="green")
char_4 = c.create_oval((225, 175, 250, 200), fill="green", outline="green")
char_7 = c.create_oval((225, 250, 250, 275), fill="green", outline="green")
char_2 = c.create_oval((325, 100, 350, 125), fill="green", outline="green")
char_5 = c.create_oval((325, 175, 350, 200), fill="green", outline="green")
char_8 = c.create_oval((325, 250, 350, 275), fill="green", outline="green")
char_0 = c.create_oval((325, 325, 350, 350), fill="green", outline="green")
char_3 = c.create_oval((425, 100, 450, 125), fill="green", outline="green")
char_6 = c.create_oval((425, 175, 450, 200), fill="green", outline="green")
char_9 = c.create_oval((425, 250, 450, 275), fill="green", outline="green")
word_ok = c.create_rectangle((415, 325, 460, 350), fill="green", outline="green")
bank_card = c.create_rectangle((550, 100, 650, 125), fill="blue", outline="black")
start = c.create_oval((550, 200, 650, 300), fill="red", outline="black")

# Создание надписей
c.create_text(110, 110, text="92, 41 р/л")
c.create_text(110, 185, text="95, 44 р/л")
c.create_text(110, 260, text="98, 46 р/л")
c.create_text(435, 360, text="OK")
c.create_text(600, 250, text="START")
c.create_text(238, 135, text="1")
c.create_text(338, 135, text="2")
c.create_text(438, 135, text="3")
c.create_text(238, 210, text="4")
c.create_text(338, 210, text="5")
c.create_text(438, 210, text="6")
c.create_text(238, 288, text="7")
c.create_text(338, 288, text="8")
c.create_text(438, 288, text="9")
c.create_text(338, 360, text="0")
main_t = c.create_text(350, 25, text="ВЫБЕРИТЕ ТИП БЕНЗИНА")


def petrol(x):
    global petrol_type
    global i
    if i == 0:
        petrol_type = x
        c.itemconfig(main_t, text="НАБЕРИТЕ КОЛИЧЕСТВО ЛИТРОВ И НАЖМИТЕ 'ОК'")
        i = 1


def ch(c1):
    global i
    if i != 0 and i != 3 and i != 6:
        global lit
        lit = lit + c1
        c.itemconfig(main_t, text=lit)
        if i == 1:
            i = 2
        if i == 4:
            i = 5


# Тип бензина
def f_92(event):
    petrol(x=41)


def f_95(event):
    petrol(x=44)


def f_98(event):
    petrol(x=46)


# Цифры
def f_1(event):
    c = "1"
    ch(c)


def f_2(event):
    c = "2"
    ch(c)


def f_3(event):
    c = "3"
    ch(c)


def f_4(event):
    c = "4"
    ch(c)


def f_5(event):
    c = "5"
    ch(c)


def f_6(event):
    c = "6"
    ch(c)


def f_7(event):
    c = "7"
    ch(c)


def f_8(event):
    c = "8"
    ch(c)


def f_9(event):
    c = "9"
    ch(c)


def f_0(event):
    c = "0"
    ch(c)


def f_ok(event):
    global lit
    global petrol_type
    global i
    if i == 2:
        if lit[0] == "0":
            c.itemconfig(main_t, text="НЕКОРРЕКТНОЕ ЧИСЛО! ПОВТОРИТЕ ВВОД")
            lit = ""
            i = 1
        else:
            q_liter = int(lit)
            lit = ""
            price = petrol_type * q_liter
            price = str(price)
            tt = "ЦЕНА:  " + price + "руб.  ВСТАВЬТЕ КАРТУ"
            c.itemconfig(main_t, text=tt)
            i = 3

    if i == 5:
        a = len(lit)
        lit = ""
        if a == 4:
            c.itemconfig(main_t, text="ОПЛАТА ПРОШЛА УСПЕШНО! НАЖМИТЕ START ДЛЯ ЗАПРАВКИ")
            i = 6
        else:
            c.itemconfig(main_t, text="НЕКОРРЕКТНЫЙ ПАРОЛЬ! ЗАНОВО ВСТАВЬТЕ КАРТУ")
            i = 3


def f_bank_card(event):
    global i
    if i == 3:
        i = 4
        c.itemconfig(main_t, text="ВВЕДИТЕ 4-Х ЗНАЧНЫЙ ПАРОЛЬ И НАЖМИТЕ 'OK'")


def f_start(event):
    global i
    if i == 6:
        i = 0
        c.itemconfig(main_t, text="ЗАПРАВКА ПРОШЛА УСПЕШНО! ДО СВИДАНИЯ!")
        window.update()
        time.sleep(2)
        c.itemconfig(main_t, text="ВЫБЕРИТЕ ТИП БЕНЗИНА")


# Кнопки для выбора типа бензина
c.tag_bind(but_92, '<Button-1>', f_92)
c.tag_bind(but_95, '<Button-1>', f_95)
c.tag_bind(but_98, '<Button-1>', f_98)

#  Кнопки для набора цифр
c.tag_bind(char_1, '<Button-1>', f_1)
c.tag_bind(char_2, '<Button-1>', f_2)
c.tag_bind(char_3, '<Button-1>', f_3)
c.tag_bind(char_4, '<Button-1>', f_4)
c.tag_bind(char_5, '<Button-1>', f_5)
c.tag_bind(char_6, '<Button-1>', f_6)
c.tag_bind(char_7, '<Button-1>', f_7)
c.tag_bind(char_8, '<Button-1>', f_8)
c.tag_bind(char_9, '<Button-1>', f_9)
c.tag_bind(char_0, '<Button-1>', f_0)

# Кнопка "ОК"
c.tag_bind(word_ok, '<Button-1>', f_ok)

# Кнопка "вставка банковской карты"
c.tag_bind(bank_card, '<Button-1>', f_bank_card)

# Кнопка для начала заправки
c.tag_bind(start, '<Button-1>', f_start)

window.mainloop()

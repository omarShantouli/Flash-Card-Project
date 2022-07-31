BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import *

data = pandas.read_csv("./data/french_words.csv")

ls = data.French.to_list()


window = Tk()
window.minsize(width= 900, height= 500)
window.config(bg= BACKGROUND_COLOR)

image = PhotoImage(file= "./images/card_back.png")
canvas = Canvas(width= 800, height= 600)
image2 = PhotoImage(file= "./images/card_front.png")
img2_canvas = canvas.create_image(400, 300, image= image2)

title = canvas.create_text(400, 200, text= "Title", font= ('Arial', 35, 'normal'))
word = canvas.create_text(400, 300, text= "Word", font= ('Arial', 35, 'bold'))

canvas.grid(column= 1, row= 1, padx= 50, columnspan= 2)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)

w_f = ""


def english():
    global w_f
    canvas.itemconfig(img2_canvas, image= image)
    canvas.itemconfig(title, text = "English")
    w_e = data[data.French == w_f].English.to_string()
    canvas.itemconfig(word, text= w_e[3 : len(w_e)])


def french(x):
    global w_f, ls
    canvas.itemconfig(img2_canvas, image= image2)
    canvas.itemconfig(title, text = "French")
    w_f = choice(ls)
    if x == "right":
        ls.remove(w_f)
    canvas.itemconfig(word, text= w_f)
    window.after(3000, english)


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_but = Button(image= wrong_img, highlightthickness= 0, command= lambda : french("wrong"))
wrong_but.grid(column= 1, row= 2)

right_img = PhotoImage(file= "./images/right.png")
right_but = Button(image= right_img, highlightthickness= 0, command= lambda : french("right"))
right_but.grid(column= 2, row=2)


window.mainloop()



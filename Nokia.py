# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:29:06 2022

@author: SamuelJames
"""

from tkinter import PhotoImage, Tk, Canvas, Button, Label

master = Tk()

canvas = Canvas(master, width=300, height=500)
canvas.pack()

photo = PhotoImage(file="nokia.png")
canvas.create_image(125, 250, image=photo)

btn0 = PhotoImage(file = "RES/0.png")
btn1 = PhotoImage(file = "RES/1.png")
btn2 = PhotoImage(file = "RES/2.png")
btn3 = PhotoImage(file = "RES/3.png")
btn4 = PhotoImage(file = "RES/4.png")
btn5 = PhotoImage(file = "RES/5.png")
btn6 = PhotoImage(file = "RES/6.png")
btn7 = PhotoImage(file = "RES/7.png")
btn8 = PhotoImage(file = "RES/8.png")
btn9 = PhotoImage(file = "RES/9.png")
btnStar = PhotoImage(file = "RES/hash.png")
btnHash = PhotoImage(file = "RES/star.png")
callbtn = PhotoImage(file = "RES/call.png")

x = ''

def check_x():
    global x
    if str(x) == '1994':
        x = 'YEAR OF THE DOG'
        out_label.config(text=x)

def check_x_five():
    global x
    if str(x) == '80085':
        x = 'BOOBIES |.|.|'
        out_label.config(text=x)

def zero():
    global x
    x = x + '0'
    out_label.config(text=x)
    
def one():
    global x
    x = x + '1'
    out_label.config(text=x)
    
def two():
    global x
    x = x + '2'
    out_label.config(text=x)
    
def tre():
    global x
    x = x + '3'
    out_label.config(text=x)
    
def four():
    global x
    x = x + '4'
    check_x()
    out_label.config(text=x)
    
def fv():
    global x
    x = x + '5'
    out_label.config(text=x)
    check_x_five()
    
def six():
    global x
    x = x + '6'
    out_label.config(text=x)
    
def svn():
    global x
    x = x + '7'
    out_label.config(text=x)
    
def eight():
    global x
    x = x + '8'
    out_label.config(text=x)
    
def nine():
    global x
    x = x + '9'
    out_label.config(text=x)

def STAR():
    global x
    x = ''
    out_label.config(text=' ')

def call():
    global x
    out_label.config(text='Now Calling...\n' + x)
    

call_button = Button(master, image=callbtn, command=call, anchor='w')
call_button_window = canvas.create_window(50, 250, anchor='nw', window=call_button)    

#last row
star_button = Button(master, image=btnHash, command=master.quit, anchor='w')
star_button_window = canvas.create_window(50, 432, anchor='nw', window=star_button)

Z_button = Button(master, image=btn0, command=zero, anchor='w')
Z_button_window = canvas.create_window(105, 432, anchor='nw', window=Z_button)

hash_button = Button(master, image=btnStar, command=STAR, anchor='w')
hash_button_window = canvas.create_window(165, 432, anchor='nw', window=hash_button)

#3rd row
svn_button = Button(master, image=btn7, command=svn, anchor='w')
svn_button_window = canvas.create_window(50, 390, anchor='nw', window=svn_button)

eight_button = Button(master, image=btn8, command=eight, anchor='w')
eight_button_window = canvas.create_window(105, 390, anchor='nw', window=eight_button)

nine_button = Button(master, image=btn9, command=nine, anchor='w')
nine_button_window = canvas.create_window(165, 390, anchor='nw', window=nine_button)

#2nd row
four_button = Button(master, image=btn4, command=four, anchor='w')
four_button_window = canvas.create_window(50, 350, anchor='nw', window=four_button)

five_button = Button(master, image=btn5, command=fv, anchor='w')
five_button_window = canvas.create_window(105, 350, anchor='nw', window=five_button)

six_button = Button(master, image=btn6, command=six, anchor='w')
six_button_window = canvas.create_window(165, 355, anchor='nw', window=six_button)

#top row
one_button = Button(master, image=btn1, command=one, anchor='w')
one_button_window = canvas.create_window(50, 313, anchor='nw', window=one_button)

two_button = Button(master, image=btn2, command=two, anchor='w')
two_button_window = canvas.create_window(105, 313, anchor='nw', window=two_button)

tre_button = Button(master, image=btn3, command=tre, anchor='w')
tre_button_window = canvas.create_window(165, 313, anchor='nw', window=tre_button)

out_label = Label(master, text=" ")
out_label.config(width=20, height=7)
out_label.config(bg="green")
out_label_window = canvas.create_window(50, 145, anchor='nw', window=out_label)

master.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:19:41 2020

@author: S Shankar Narayanan
"""


import math # The main library for performing math operations
from tkinter import messagebox,Entry,Button,Tk,StringVar # This is the library to give GUI operations
win = Tk()
win.title('Zen-Cal®')
win.configure(bg='red')
win.wm_iconbitmap('cally.ico')
win.maxsize(width=453,height=550)
win.minsize(width=362,height=488)
te = StringVar()
operator = ''

#Commands After Button Click

def btnclick(number):
    global operator
    operator += str(number)
    te.set(operator)
def clear():    
    global operator
    operator = ''
    te.set(operator)
def equal():
    global operator
    try:
        result = eval(te.get())
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)
def sin():
    global operator
    try:
        result = math.sin(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)
def cos():
    global operator
    try:
        result = math.cos(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)
def tan():
    global operator
    try:
        result = math.tan(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)
def log():
    global operator
    try:
        result = math.log(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)
def sqrt():
    global operator
    try:
        result = math.sqrt(eval(te.get()))
        operator = str(result)
        te.set(operator)
    except:
        messagebox.showinfo('Notification','Check your input and try again',parent=win)


# This is the entry box function
entry1 = Entry(win,bg='orange',font = ('arial',20,'italic bold'),bd=30,
             insertwidth=4,justify='right',textvariable=te)
entry1.grid(columnspan=4)


btsin = Button(win,text='sin',font=('arial',15,'italic bold'),padx=14,pady=20,bd=8,
             bg='white',command=sin,activebackground='green',activeforeground='white')
btsin.grid(row=0,column=4)

# And these are the operations for the individual buttons

bt7 = Button(win,text='7',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(7),activebackground='green',activeforeground='white')
bt7.grid(row=1,column=0)

bt8 = Button(win,text='8',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(8),activebackground='green',activeforeground='white')
bt8.grid(row=1,column=1)

bt9 = Button(win,text='9',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(9),activebackground='green',activeforeground='white')
bt9.grid(row=1,column=2)

btaddition = Button(win,text='+',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick('+'),activebackground='green',activeforeground='white')
btaddition.grid(row=1,column=3)

btcos = Button(win,text='cos',font=('arial',15,'italic bold'),padx=14,pady=20,bd=8,
             bg='white',command=cos,activebackground='green',activeforeground='white')
btcos.grid(row=1,column=4)


bt4 = Button(win,text='4',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(4),activebackground='green',activeforeground='white')
bt4.grid(row=2,column=0)

bt5 = Button(win,text='5',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(5),activebackground='green',activeforeground='white')
bt5.grid(row=2,column=1)

bt6 = Button(win,text='6',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(6),activebackground='green',activeforeground='white')
bt6.grid(row=2,column=2)

btsubstraction = Button(win,text='- ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick('-'),activebackground='green',activeforeground='white')
btsubstraction.grid(row=2,column=3)

bttan = Button(win,text='tan',font=('arial',15,'italic bold'),padx=16,pady=20,bd=8,
             bg='white',command=cos,activebackground='green',activeforeground='white')
bttan.grid(row=2,column=4)



bt1 = Button(win,text='1',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(1),activebackground='green',activeforeground='white')
bt1.grid(row=3,column=0)

bt2 = Button(win,text='2',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(2),activebackground='green',activeforeground='white')
bt2.grid(row=3,column=1)

bt3 = Button(win,text='3',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(3),activebackground='green',activeforeground='white')
bt3.grid(row=3,column=2)

btmultiplication = Button(win,text='* ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick('*'),activebackground='green',activeforeground='white')
btmultiplication.grid(row=3,column=3)

btsqrt = Button(win,text='sqrt',font=('arial',15,'italic bold'),padx=12,pady=20,bd=8,
             bg='white',command=sqrt,activebackground='green',activeforeground='white')
btsqrt.grid(row=3,column=4)




bt0 = Button(win,text='0',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=lambda :btnclick(0),activebackground='green',activeforeground='white')
bt0.grid(row=4,column=0)

btclear = Button(win,text='C',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
                  bg='white',command=clear,activebackground='yellow',activeforeground='white')
btclear.grid(row=4,column=1)


btequal = Button(win,text='=',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,
             bg='white',command=equal,activebackground='green',activeforeground='white')
btequal.grid(row=4,column=2)


btdivision = Button(win,text='/ ',font=('arial',20,'italic bold'),padx=16,pady=16,bd=8,bg='white'
             ,command=lambda :btnclick('/'),activebackground='green',activeforeground='white')
btdivision.grid(row=4,column=3)

btlog = Button(win,text='log',font=('arial',15,'italic bold'),padx=16,pady=20,bd=8,
             bg='white',command=log,activebackground='green',activeforeground='white')
btlog.grid(row=4,column=4)

# Now I'm adding hover effect on the buttons

def changeBGEnter(buttons):
    buttons['bg'] = 'red'
def changeBGLeave(buttons):
    buttons['bg'] = 'white'

# Here I'm adding all the buttons to a list and appending the functions to them

bttns = [bt0,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,btaddition,btsubstraction,btmultiplication,btdivision,
         btsin,btlog,btcos,bttan,btsqrt,btequal,btclear,entry1,entry1]
for buttonnumber in bttns:
    buttonnumber.bind("<Enter>", lambda event, buttons=buttonnumber: changeBGEnter(buttons))
    buttonnumber.bind("<Leave>", lambda event, buttons=buttonnumber: changeBGLeave(buttons))



win.mainloop()
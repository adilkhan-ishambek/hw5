from math import *
from tkinter import *

#main window
window = Tk()
equation = StringVar()
output = Entry(window, textvariable=equation,justify = RIGHT, font = 20, width = 50)
output.grid(row = 0, column = 0, columnspan = 8)

#functions
def add_values(value):
    output.insert(END,f"{value}")
def delete_values():
    output.delete(output.index(END)-1)
def factorial(k):
    k = int(k)
    if k == 0 or k == 1:
        return 1
    else:
        fact = 1
        for i in range(k):
            fact*=(k+1)
        return fact
def result():
    try:equation.set(f"{eval(output.get())}")
    except:equation.set("ERROR")
def clear():
    output.delete(0, END)

#buttons
Button(window , text = "0",command = lambda: add_values("0"), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=1)
Button(window , text = "1",command = lambda: add_values("1"), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=0)
Button(window , text = "2",command = lambda: add_values("2"), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=1)
Button(window , text = "3",command = lambda: add_values("3"), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=2)
Button(window , text = "4",command = lambda: add_values("4"), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=0)
Button(window , text = "5",command = lambda: add_values("5"), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=1)
Button(window , text = "6",command = lambda: add_values("6"), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=2)
Button(window , text = "7",command = lambda: add_values("7"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=0)
Button(window , text = "8",command = lambda: add_values("8"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=1)
Button(window , text = "9",command = lambda: add_values("9"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=2)
Button(window , text = "N!",command = lambda: add_values("factorial("), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=3)
Button(window , text = "(",command = lambda: add_values("("), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=4)
Button(window , text = ")",command = lambda: add_values(")"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=4)
Button(window , text = "-",command = lambda: add_values("-"), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=5)
Button(window , text = "+",command = lambda: add_values("+"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=5)
Button(window , text = "sqrt(x)",command = lambda: add_values("**0.5"), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=5)
Button(window , text = "x^2",command = lambda: add_values("**2"), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=5)
Button(window , text = "*",command = lambda: add_values("*"), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=3)
Button(window , text = "/",command = lambda: add_values("/"), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=3)
Button(window , text = ".",command = lambda: add_values("."), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=0)
Button(window , text = "DEL",command = lambda: delete_values(), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=6)
Button(window , text = "=",command = lambda: result(), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=2)
Button(window , text = "C",command = lambda: clear(), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=6)
Button(window , text = "sin",command = lambda: add_values("sin("), bd = 5, font = 10,width = 5, height = 2).grid(row=3, column=6)
Button(window , text = "cos",command = lambda: add_values("cos("), bd = 5, font = 10,width = 5, height = 2).grid(row=4, column=6)
Button(window , text = "ln",command = lambda: add_values("log("), bd = 5, font = 10,width = 5, height = 2).grid(row=2, column=4)
Button(window , text = "tan",command = lambda: add_values("tan("), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=4)
Button(window , text = "exp",command = lambda: add_values("e**"), bd = 5, font = 10,width = 5, height = 2).grid(row=5, column=3)

window.mainloop()


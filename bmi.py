# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox



window = Tk()
window.title('Licznik BMI')     #title

heading = Label(window, text = 'Oblicz swoje BMI', font = 'bold')
heading.grid(row = 0, columnspan = 4)

#inserting variables

cm = IntVar()
growth = Entry(window, textvariable = cm)
kg = IntVar()
weight = Entry(window, textvariable = kg)

growth1 = Label(window, text = 'Wzrost w cm: ')
weight1 = Label(window, text = 'Waga w kg: ')

#function

def bmi():
   while True:
       try:
           centimeter = cm.get()
           c1 = centimeter/100
           kilograms = kg.get()
           if kilograms != 0:
               Ans = (kilograms / (c1 * c1))
               tkinter.messagebox._show('BMI', round(Ans, 2))
               break
           else:
               tkinter.messagebox._show('BMI', 'Wpisz wartość!')
               break
       except ZeroDivisionError:
           tkinter.messagebox._show('Wartość', 'Wpisz wartość!')
           return
       except tkinter.TclError:
           tkinter.messagebox._show('Wartość', 'Wpisz wartość!')
           return
def water():
   while True:
       try:
           kilograms = kg.get()
           if kilograms != 0:
               w = ((kilograms/10)*0.3)
               tkinter.messagebox._show('Woda', w)
               break
           else:
               tkinter.messagebox._show('Woda', 'Wpisz wartość!')
               break
       except tkinter.TclError:
           tkinter.messagebox._show('Wartość', 'Wpisz wartość!')
           return


button1 = Button(window, text = 'Przelicz BMI', fg = 'black', command = bmi)
button2 = Button(window, text = 'Ile litrów wody dziennie\n powinieneś wypić', fg = 'black',command = water)


#GUI

growth1.grid(row = 2, column = 1)
weight1.grid(row = 3, column = 1)
growth.grid(row = 2, column = 2)
weight.grid(row = 3, column = 2)
button1.grid(row = 4, column = 1,padx = 30, pady = 25)
button2.grid(row = 4, column = 2,padx = 30, pady = 25)


window.mainloop()

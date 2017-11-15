from tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox


okno = Tk()
okno.title('Licznik BMI')     #tytuł okienka

heading = Label(okno, text = 'Oblicz swoje BMI', font = 'bold')
heading.grid(row = 0, columnspan = 4)

#wprowadzenie zmiennych

cm = IntVar()
wzrost = Entry(okno, textvariable = cm)
kg = IntVar()
waga = Entry(okno, textvariable = kg)

wzrost1 = Label(okno, text = 'Wzrost w cm: ')
waga1 = Label(okno, text = 'Waga w kg: ')

#funkcje

def bmi():
   while True:
       try:
           c = cm.get()
           c1 = c/100
           k = kg.get()
           if k != 0:
               Ans = (k / (c1 * c1))
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
def woda():
   while True:
       try:
           k = kg.get()
           if k != 0:
               w = ((k/10)*0.3)
               tkinter.messagebox._show('Woda', w)
               break
           else:
               tkinter.messagebox._show('Woda', 'Wpisz wartość!')
               break
       except tkinter.TclError:
           tkinter.messagebox._show('Wartość', 'Wpisz wartość!')
           return


przycisk1 = Button(okno, text = 'Przelicz BMI', fg = 'black',padx = 30, pady = 17, command = bmi)
przycisk2 = Button(okno, text = 'Ile litrów wody dziennie\n powinieneś wypić', fg = 'black',padx = 30, pady = 10, command = woda)


#modelowanie GUI

wzrost1.grid(row = 2, column = 1)
waga1.grid(row = 3, column = 1)#, padx = 80, pady = 50)
wzrost.grid(row = 2, column = 2,padx = 30, pady = 10)#, padx = 100, pady = 70)
waga.grid(row = 3, column = 2,padx = 30, pady = 10)#, padx = 120, pady = 90)
przycisk1.grid(row = 4, column = 1,padx = 30, pady = 10)#, padx = 40, pady = 10)
przycisk2.grid(row = 4, column = 2,padx = 30, pady = 10)#, padx = 40, pady = 10)


okno.mainloop()

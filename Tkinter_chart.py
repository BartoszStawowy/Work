from matplotlib import style
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, '{program name}')

        window = tk.Frame(self)
        window.pack(side='top', fill='both', expand = True)
        window.grid_rowconfigure(0, weight = 1)
        window.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, Chart):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_gui(StartPage)

    def show_gui(self, window):
        frame = self.frames[window]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'program title')
        label.pack(pady = 10, padx = 10)


        button1 = ttk.Button(self, text = 'not used button',
                               command=lambda: window.show_gui('nothing'))
        button1.pack()

        button2 = ttk.Button(self, text = 'show chart',
                               command=lambda: window.show_gui(Chart))
        button2.pack()

class Chart(tk.Frame):

    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'chart title')
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = 'back',
                               command=lambda: window.show_gui(StartPage))
        button1.pack()

        chart_window = Figure(figsize=(10,5), dpi=100)
        chart_window.suptitle('simple chart example')
        chart = chart_window.add_subplot(111)
                '''
        just random data, to show how chart in tkinter looks
        '''
            
        years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
        cost = [3100, 3100, 3300, 3600, 3650, 3600, 3600,
                         3600, 3600, 4000]
        cost_with_tax = [4100, 4100, 4300, 4600, 4650, 4700, 4700,
                          4700, 5000, 5000]
        
        '''
        '''
        chart.plot(years, cost)
        chart.plot(years, cost_with_tax)
        chart.legend(['description 1','description 2'])

        canvas = FigureCanvasTkAgg(chart_window, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True)


tkinter_with_chart = MainWindow()
tkinter_with_chart.mainloop()

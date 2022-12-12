from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title('CLOCK')


def time():
	
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('Ds-Digital', 80, 'bold'),
			background = 'black',
			foreground = 'red')

lbl.pack(anchor = 'center')

time()

mainloop()

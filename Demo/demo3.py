# –*–coding:utf-8 –*–
from tkinter import *

def quit():
	# code to exit
	global root
	root.quit()
root = Tk()
Button(root, text="Quit", command=quit).pack()
root.mainloop()







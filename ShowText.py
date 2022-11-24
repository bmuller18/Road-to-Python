import tkinter as tk
from tkinter import *
from PIL import ImageTk

#COLORS
backcolor = "#8A82FB"
backcolor2 = "#C977FD"

def AddItem():
    print("New item")
    
    
root = tk.Tk()
root.title("My Main")


#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))


#Create TOP MENU BARNAV
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="WareHouse", menu= file_menu)
file_menu.add_cascade(label="Add Item", command=AddItem)
my_menu.add_cascade(label="Customer", menu=file_menu)


frame1 = tk.Frame(root, width=500, height=600, bg=backcolor)
frame1.pack()
root.mainloop()
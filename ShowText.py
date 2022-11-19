import tkinter as tk
from PIL import ImageTk

#COLORS
backcolor = "#8A82FB"
root = tk.Tk()
root.title("My Main")
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=500, height=600, bg=backcolor)
logo_image = ImageTk.PhotoImage(file="Assets/Logo.png")

logo_widget = tk.Label(frame1, image=logo_image)
logo_image.image = logo_image
logo_widget.pack()
frame1.pack()
root.mainloop()
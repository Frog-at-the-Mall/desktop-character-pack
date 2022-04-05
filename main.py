
# Import Module
from tkinter import * 
import tkinter as tk
 
# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("mattFrye Pxlart")
# Set geometry (widthxheight)
root.geometry('350x200')

img = tk.PhotoImage(file='Sprite-0001.gif', format= "gif")

label = Label(root, image = img).grid(row = 0, column = 2,
       columnspan = 10, rowspan = 10, padx = 5, pady = 5)


def clicked():
    
    label = 1
    
    
 
btn1 = Button(root, text = "Eyeball " ,fg = "purple",command=clicked)
btn2 = Button(root, text = "Click me " ,fg = "red",command=clicked)
btn3 = Button(root, text = "Click me " ,fg = "red",command=clicked)
btn4 = Button(root, text = "Click me " ,fg = "red",command=clicked)







btn1.grid(column=1,row=0)
btn2.grid(column=1,row=1)
btn3.grid(column=1,row=2)
btn4.grid(column=1,row=3)



# all widgets will be here
# Execute Tkinter
root.mainloop()
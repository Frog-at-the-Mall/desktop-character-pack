
# Import Module
from tkinter import * 
import tkinter as tk
 
# create root window
root = tk.Tk()
 
# root window title and dimension
root.title("mattFrye Pxlart")
# Set geometry (widthxheight)
root.geometry('640x360')

img1 = tk.PhotoImage(file='Sprite-0001.gif')

img2 = tk.PhotoImage(file='Sprite-0002.png')

label = Label(root, image = img1)
label.grid(column=2,row=0)
   




def clicked1():
    
    label = Label(root,image = img1)

def clicked2():
    
    label = Label(root, image = img2)
    
    
 
btn1 = Button(root, text = "Eyeball " ,fg = "purple",command=clicked1)
btn2 = Button(root, text = "Landscape " ,fg = "green",command=clicked2)


btn1.grid(column=1,row=0)
btn2.grid(column=1,row=1)




# all widgets will be here
# Execute Tkinter
root.mainloop()
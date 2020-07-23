import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.state('zoomed')
w,h = 2000, 2000    

canvas = tk.Canvas(root, height = w, width = h, bg = "#FFFFFF", highlightthickness = 0)
canvas.pack()

sidePanel = tk.Frame(canvas, bg = "#7FBDBA")
sidePanel.place(relwidth = 0.2, relheight = 1)

titlePanel = tk.Frame(canvas, bg = "#D3D0D0", width = 1600, height = 100)
titlePanel.place(x = 0, y = 0)

title = tk.Label(sidePanel, text = "Open File", padx = 10,
                     pady = 5, fg = "black", bg = "#D3D0D0", font = 'Verdana')
title.pack()

task = tk.Frame(canvas, width=250, height=300, bg='#97D3E8')
task.place(x = 350, y = 150)

img = ImageTk.PhotoImage(Image.open("Tasks.png"))   
panel = tk.Label(titlePanel, image = img, bd = 0)
panel.place(x = 800, y = 10)



# task.pack(padx = 100, pady = 200)

# openFile = tk.Button(frame, text = "Open File", padx = 10,
#                      pady = 5, fg = "white", bg = "#263d42")
# openFile.pack()

root.mainloop()
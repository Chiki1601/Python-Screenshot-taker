# hi I created this Screenshot taker program in Python.
import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\admin\Desktop\screenshot.png')


#With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('Screenshot taker Created by Pooja Patel')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def myScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\admin\Desktop\screenshot1.png')

myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='green',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
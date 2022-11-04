#!/user/bin/env python
# -*- coding:utf-8 -*-
# Version 2.0
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import ctypes

root=Tk()

winWidth = 720
winHeight = 480
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
root.title("Random Number Generator - Beta")
root.resizable(0,0)
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)

#-----------------------------------------------------
def control():
    a=1
    b=46
    number = randint(a,b)
    
    message = "The Random Number Is "+ str(number)
    control_info = showinfo(title='INFO',message=message)



#-----------------------------------------------------    
label_1 = Label(root,
                   text='Random Number Generator',
                   font=("Microsoft YaHei UI", 12))
label_1.pack()
label_2 = Label(root,
                   text='Current State and Instruction',
                   font=("Microsoft YaHei UI", 8))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
state.place(relx=0.03, y=70, relwidth=0.5, height=100)
state.insert(INSERT, "当前状态：空闲\n")
state.insert(INSERT, "您可以点击HIT ME产生随机数")
state.configure(state='disabled')
#state.delete('0.0', END)
control = Button(root, text ="HIT IT!", command = control)
control.pack()
label = Label(root,text="Version 2.0.3_Alpha 07",foreground="gray")
label.pack(side='left')
label_1 = Label(root,text="Made By 12sdj",foreground="gray")
label_1.pack(side='right')


root.mainloop()

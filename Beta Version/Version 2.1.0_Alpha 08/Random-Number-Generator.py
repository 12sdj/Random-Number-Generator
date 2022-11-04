#!/user/bin/env python
# -*- coding:utf-8 -*-
# Version 2.0
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import ctypes
import webbrowser

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
def github():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues')
def discuss():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/discussions')
def minimize():
    root.iconify()
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
def t_close_handler_about():
    root.attributes('-disabled', 0)
    window_about.destroy()
def about():
    global window_about
    window_about = Toplevel(root)
    window_about.geometry("680x340+200+250")
    window_about.resizable(0,0)
    window_about.attributes('-toolwindow', True)
    #window_about.mainloop()
    window_about.protocol("WM_DELETE_WINDOW", t_close_handler_about)
    root.attributes('-disabled', 1)
    #Unint
    label_a = Label(window_about,
                   text='About',
                   font=("Microsoft YaHei UI", 12))
    label_a.pack()
    tip_window = Label(window_about,
                    text='Random Number Generator \n'
                            'Version: Version 2.1.0_Alpha 08 (Build 2108 Alpha_R0P8)\n'
                            '2022/11/4 21:45(UTC+8) Update 08\n'
                            'Copyright © 2022 12sdj. All Rights Reserved.',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
    tip_window.pack()

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



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='Settings', menu=filemenu)
submenu = Menu(filemenu)
filemenu.add_command(label='About', command=about)
filemenu.add_separator()
filemenu.add_command(label='EXIT', command=root.quit)
    
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='HELP', menu=editmenu)
editmenu.add_command(label='FEEDBACK(Github)', command=github)
editmenu.add_command(label='DISCUSS(Github)', command=discuss)
root.config(menu=menubar) 

#<Button - 3>
rightmenu = Menu(root,tearoff=False)
rightmenu.add_command(label="Minimize",command=minimize)
rightmenu.add_command(label="Exit",command=root.destroy)
root.bind("<Button-3>",showPopupMenu)




root.mainloop()

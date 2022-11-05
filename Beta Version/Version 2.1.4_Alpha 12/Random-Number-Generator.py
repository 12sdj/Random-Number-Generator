#!/user/bin/env python
# -*- coding:utf-8 -*-
# Version 2.0
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import ctypes
import webbrowser
import time
import threading

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
#----------------------------------------------------------
global a
global b
global end_control
a=1
b=46

#####----------------------------------------------------------------MAIN UNIT!!!!!!
state_1 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_1.place(relx=0.01, y=210, relwidth=0.32, height=220)
state_2 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_2.place(relx=0.34, y=210, relwidth=0.32, height=220)
state_3 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_3.place(relx=0.67, y=210, relwidth=0.32, height=220)
state_1.configure(state='disabled')
state_2.configure(state='disabled')
state_3.configure(state='disabled')


####__________________________________________________________BETA

#-----------------------------------------------------
def control():
    control['state'] = DISABLED
    end['state'] = NORMAL
    end_control = 0
    def thread_1(func):

        time.sleep(1)
        while True:
            number_1 = randint(a,b)
            state_1.configure(state='normal')
            state_1.delete('0.0', END)
            state_1.insert(INSERT, number_1)
            time.sleep(0.01)
    def thread_2(func):

        time.sleep(1)
        while True:
            number_2 = randint(a,b)
            state_2.configure(state='normal')
            state_2.delete('0.0', END)
            state_2.insert(INSERT, number_2)
            time.sleep(0.01)
    def thread_3(func):

        time.sleep(1)
        while True:
            number_3 = randint(a,b)
            state_3.configure(state='normal')
            state_3.delete('0.0', END)
            state_3.insert(INSERT, number_3)
            time.sleep(0.01)
    def thread_4(func):
        pass
    threads = []
    t1 = threading.Thread(target=thread_1,args=(u'thread_state_1',))
    t2 = threading.Thread(target=thread_2,args=(u'thread_state_2',))
    t3 = threading.Thread(target=thread_3,args=(u'thread_state_3',))
    t4 = threading.Thread(target=thread_4,args=(u'thread_state_4',))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n")
    state.insert(INSERT, "您可以点击“停止运行”进行查看\n")
    state.configure(state='disabled')

    if __name__ == '__main__':
        for t in threads:

            t.daemon=True
            #t.setDaemon(True) #被t.daemon=True替代(python 3.10)
            t.start()

    

    #message = "The Random Number Is "+ str(number_1)
    #control_info = showinfo(title='INFO',message=message)
def end():
    control['state'] = NORMAL
    end['state'] = DISABLED
    state_1.configure(state='disabled')
    state_2.configure(state='disabled')
    state_3.configure(state='disabled')
    end_control = 1
#-----------------------------------------------------
def github():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues')
def discuss():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/discussions')
def minimize():
    root.iconify()
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
##----------------------------------------------------
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
                            'Version: Version 2.1.4_Alpha 12 (Build 2112 Alpha_R0P12)\n'
                            '2022/11/5 15:10(UTC+8) Update 12\n'
                            'Copyright © 2022 12sdj. All Rights Reserved.',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
    tip_window.pack()
##----------------------------------------------------
def t_close_handler_licence():
    root.attributes('-disabled', 0)
    window_licence.destroy()
def licence():
    global window_licence
    window_licence = Toplevel(root)
    window_licence.geometry("680x340+200+250")
    window_licence.resizable(0,0)
    window_licence.attributes('-toolwindow', True)
    window_licence.protocol("WM_DELETE_WINDOW", t_close_handler_licence)
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_licence,
                   text='Licence',
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()
    state = Text(window_licence, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=40, relwidth=0.96, height=320)
    state.insert(INSERT, "MIT License\n")
    state.insert(INSERT, "\n")
    state.insert(INSERT, "Copyright (c) 2022 12sdj\n")
    state.insert(INSERT, "\n")
    state.insert(INSERT, "Permission is hereby granted, free of charge, to any person obtaining a copy\n")
    state.insert(INSERT, "of this software and associated documentation files (the 'Software'), to deal\n")
    state.insert(INSERT, "in the Software without restriction, including without limitation the rights\n")
    state.insert(INSERT, "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n")
    state.insert(INSERT, "copies of the Software, and to permit persons to whom the Software is\n")
    state.insert(INSERT, "furnished to do so, subject to the following conditions:\n")
    state.insert(INSERT, "\n")
    state.insert(INSERT, "The above copyright notice and this permission notice shall be included in all\n")
    state.insert(INSERT, "copies or substantial portions of the Software.\n")
    state.insert(INSERT, "\n")
    state.insert(INSERT, "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
    state.insert(INSERT, "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
    state.insert(INSERT, "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
    state.insert(INSERT, "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
    state.insert(INSERT, "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
    state.insert(INSERT, "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n")
    state.insert(INSERT, "SOFTWARE.\n")
    state.configure(state='disabled')
##----------------------------------------------------    
def t_close_handler_setting():
    root.attributes('-disabled', 0)
    window_setting.destroy()
def setting():
    global window_setting
    window_setting = Toplevel(root)
    window_setting.geometry("680x340+200+250")
    window_setting.resizable(0,0)
    window_setting.attributes('-toolwindow', True)
    window_setting.protocol("WM_DELETE_WINDOW", t_close_handler_setting)
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_setting,
                   text='Control Panel (Settings)',
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()    
    
    
    
    
#-----------------------------------------------------    
label_1 = Label(root,
                   text='Random Number Generator',
                   font=("Microsoft YaHei UI", 12))
label_1.pack()
label_2 = Label(root,
                   text='Current State and Instruction',
                   font=("Microsoft YaHei UI", 8))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
label_3 = Label(root,
                   text='Control Center',
                   font=("Microsoft YaHei UI", 8))
label_3.place(relx=0.55, y=40, relwidth=0.45, height=25)
state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
state.place(relx=0.03, y=70, relwidth=0.5, height=120)
state.insert(INSERT, "当前状态：空闲\n")
state.insert(INSERT, "您可以在设置参数后点击“开始运行”产生随机数")
state.configure(state='disabled')
#state.delete('0.0', END)
control = Button(root, text ="开始运行", command = control)
control.place(relx=0.55, y=70, relwidth=0.4, height=40)
end = Button(root, text ="停止运行", command = end)
end.place(relx=0.55, y=110, relwidth=0.4, height=40)
end['state'] = DISABLED
setting = Button(root, text ="设置", command = setting)
setting.place(relx=0.55, y=150, relwidth=0.4, height=40)


####----------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='Shortcuts', menu=filemenu)
submenu = Menu(filemenu)
filemenu.add_command(label='About', command=about)
filemenu.add_command(label='Licence', command=licence)
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

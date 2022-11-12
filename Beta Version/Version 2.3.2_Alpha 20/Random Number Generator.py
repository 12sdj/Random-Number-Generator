#!/user/bin/env python
# -*- coding:utf-8 -*-
# Version 2.0
from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import tkinter as tk
import ctypes
import webbrowser
import time
import threading
from ttkthemes import*
#root=Tk()
root=ThemedTk(theme="adapta", toplevel=True, themebg=True)
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
state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
state_2 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
state_3 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
state_1.configure(state='disabled')
state_2.configure(state='disabled')
state_3.configure(state='disabled')


####__________________________________________________________BETA
class Job(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.set()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.01)
            global number_1
            number_1 = randint(a,b)
            state_1.delete('0.0', END)
            state_1.insert(INSERT, number_1)
            #print("1")
    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False    
class mine(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(mine, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()      
        self.__running.set()      

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()     
            time.sleep(0.01)
            global number_2
            number_2 = randint(a,b)
            state_2.delete('0.0', END)
            state_2.insert(INSERT, number_2)
            #print("2")
    def pause(self):
        self.__flag.clear()    

    def resume(self):
        self.__flag.set()    
    def stop(self):
        self.__flag.set()      
        self.__running.clear()        
class hello(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()      
            time.sleep(0.01)
            global number_3
            number_3 = randint(a,b)
            state_3.delete('0.0', END)
            state_3.insert(INSERT, number_3)
            #print("3")
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       

def thread_4(func):
    pass
threads = []
t1 = Job()
t2 = mine()
t3 = hello()
t4 = threading.Thread(target=thread_4,args=(u'thread_state_4',))
threads.append(t1)
t1.pause()
threads.append(t2)
t2.pause()
threads.append(t3)
t3.pause()
threads.append(t4)
if __name__ == '__main__':
    for t in threads:
        t.daemon=True
        #t.setDaemon(True) #被t.daemon=True替代(python 3.10)
        t.start()


#-----------------------------------------------------
def control():
    control['state'] = DISABLED
    end['state'] = NORMAL
    
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n")
    state.insert(INSERT, "您可以点击“停止运行”进行查看\n")
    state.configure(state='disabled')
    state_1.configure(state='normal')
    state_2.configure(state='normal')
    state_3.configure(state='normal')
    t1.resume()
    t2.resume()
    t3.resume()
    #message = "The Random Number Is "+ str(number_1)
    #control_info = showinfo(title='INFO',message=message)
def end():
    control['state'] = NORMAL
    end['state'] = DISABLED
    number_a = randint(a,b)
    state_1.delete('0.0', END)
    state_1.insert(INSERT, number_a)
    number_b = randint(a,b)
    state_2.delete('0.0', END)
    state_2.insert(INSERT, number_b)
    number_c = randint(a,b)
    state_3.delete('0.0', END)
    state_3.insert(INSERT, number_c)
    state_1.configure(state='disabled')
    state_2.configure(state='disabled')
    state_3.configure(state='disabled')
    t1.pause()
    t2.pause()
    t3.pause()
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：空闲\n")
    state.insert(INSERT, "您可以在设置参数后点击“开始运行”产生随机数")
    state.configure(state='disabled')

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
    def mean():
        def t_close_handler_mean():
            window_about.attributes('-disabled', 0)
            window_mean.destroy()
        global window_mean
        window_mean = Toplevel(window_about)
        window_mean.geometry("680x340+300+350")
        window_mean.resizable(0,0)
        window_mean.attributes('-toolwindow', True)
        window_mean.protocol("WM_DELETE_WINDOW", t_close_handler_mean)
        window_about.attributes('-disabled', 1)
        ti_window = Label(window_mean,
                    text='Silent(22H2)\n',
                    font=("Microsoft YaHei UI", 15),
                    foreground="black")
        ti_window.place(relx=0.2, y=40, relwidth=0.6, height=40)
        state = Text(window_mean, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.2, y=80, relwidth=0.6, height=230)
        state.insert(INSERT, "'Silent' means silent, and is a reflection of the goal of the most important version number, 22H2. In 'Silent(22H2)', the program will be presented in a static way with more beautiful layouts, plainer controls and easier interaction, aiming to set the basic structure and direction of the program in this version.\n")
        state.insert(INSERT, "'Silent'意思是静默化，是22H2这个最主要版本号的目标的体现。在'Silent(22H2)'中，程序将以静态的方式呈现更精美的布局、更朴素的控件和更方便的交互，争取将程序的基本结构和发展方向在这个版本中得到确定")
        state.configure(state='disabled')
    def update():
        webbrowser.open('https://github.com/12sdj/Random-Number-Generator/releases/')
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
                            'Version: Version 2.3.2_Alpha 20 (Build 2120 Alpha_R0P20)\n'
                            '2022/11/12 20:10(UTC+8) Update 20\n'
                            'Copyright © 2022 12sdj. All Rights Reserved.',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
    tip_window.pack()
    control = Button(window_about, text ="查看有关版本号的更多信息", command = mean)
    control.place(relx=0.2, y=290, relwidth=0.4, height=40)
    control2 = Button(window_about, text ="检查更新", command = update)
    control2.place(relx=0.6, y=290, relwidth=0.2, height=40)
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
    window_setting.geometry("720x480+150+150")
    window_setting.resizable(0,0)
    window_setting.attributes('-toolwindow', True)
    window_setting.protocol("WM_DELETE_WINDOW", t_close_handler_setting)
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_setting,
                   text='Control Panel (Settings)',
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()    
    vertical =tk.Frame(window_setting, background='red', height=410,width=1)
    horizontal =tk.Frame(window_setting, background='blue', height=1,width=700)
    vertical.place(x=359, y=40)
    horizontal.place(x=10, y=239)
    
    
##----------------------------------------------------    
def t_close_handler_changelog():
    root.attributes('-disabled', 0)
    window_changelog.destroy()
def changelog():
    global window_changelog
    window_changelog = Toplevel(root)
    window_changelog.geometry("640x340+150+150")
    window_changelog.resizable(0,0)
    window_changelog.attributes('-toolwindow', True)
    window_changelog.protocol("WM_DELETE_WINDOW", t_close_handler_changelog)
    root.attributes('-disabled', 1)
    #Unint
    label = Label(window_changelog,
                   text='Changelogs',
                   font=("Microsoft YaHei UI", 12))
    label.pack()    
    label = Label(window_changelog,
                   text='Changelogs control is not available yet, \nplease wait for the follow-up news',
                   font=("Microsoft YaHei UI", 8))
    label.pack()    
    state = Text(window_changelog, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=80, relwidth=0.96, height=260)
    state.insert(INSERT, "Changelogs control will be enabled in the release after the beta version of the program.\n")
    state.configure(state='disabled')
#-----------------------------------------------------
def t_close_handler():
    root.attributes("-disabled", 0)
    window.destroy()
def status():
    def apply():
        alpha = scale.get()
        alpha = alpha / 100
        root.attributes('-alpha',alpha)
        acc = round(alpha,2)
        viewa = "当前设定值:" + str(acc)
        
        
    if demoStatus.get():
        global window
        window = Toplevel(root)
        window.geometry("620x300+200+250")
        window.title("透明效果设置")
        root.attributes('-alpha',0.85)
        tip2_window = Label(window,
                    text='Transparent effect settings\n',
                    font=("Microsoft YaHei UI", 12),
                    foreground="black")
        tip2_window.pack()
        scale = Scale(window, from_=1, to_=100,orient=HORIZONTAL,length=220)
        scale.set(85)
        scale.pack()
        
        root.attributes('-disabled', 1)#Top=window
        tip_window = Label(window,
                    text='提示：\n'
                    '通过拖动或点击滑动条设置主窗口透明度。\n'
                            '数值越小，透明程度越高；数值越大，则反之\n'
                            '建议的值为85-98之间，默认值为85',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
        tip_window.place(relx=0.05, y=120, relwidth=0.55, height=100)
        beta_window = Label(window,
                    text='Window SET\n ',
                    font=("Microsoft YaHei UI", 16),
                    foreground="black")
        beta_window.place(relx=0.6, y=170, relwidth=0.35, height=40)
        
        
        
        
        
        apply = Button(window,
                    text='应用',
                    command=apply)
        apply.place(relx=0.4, y=260, relwidth=0.2, height=35)
        window.resizable(0,0)
        window.attributes('-toolwindow', True)
        window.protocol("WM_DELETE_WINDOW", t_close_handler)
        #window.mainloop()
        
    else:
        root.attributes('-alpha',1)
def topview():
    if homoStatus.get():
        root.attributes('-topmost', -1)
    else:
       root.attributes('-topmost', 0)    
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
label_4 = Label(root,
                   text='Outputs',
                   font=("Microsoft YaHei UI", 8))
label_4.place(relx=0.03, y=195, relwidth=0.45, height=25)
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
menubar.add_cascade(label='More OPs', menu=filemenu)
filemenu.add_command(label='About', command=about)
filemenu.add_command(label='Changelogs', command=changelog)
filemenu.add_command(label='Licence', command=licence)

winmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='Window', menu=winmenu)
demoStatus = BooleanVar()
demoStatus.set(False)
homoStatus = BooleanVar()
homoStatus.set(False)
winmenu.add_checkbutton(label = "透明效果",command=status,variable=demoStatus)
winmenu.add_checkbutton(label = "窗口前置",command=topview,variable=homoStatus)
root.config(menu=menubar)
winmenu.add_separator()
winmenu.add_command(label='EXIT', command=root.quit)
    
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

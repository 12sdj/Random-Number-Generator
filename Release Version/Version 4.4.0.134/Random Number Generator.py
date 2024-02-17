#!/user/bin/env python
# -*- coding:utf-8 -*-
# @software: Visual Studio Code
from operator import truediv
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
from time import strftime
import winsound
import socket
import getpass
import os
import sys
from tkinter.scrolledtext import ScrolledText
from plyer import notification
from zhdate import ZhDate
from datetime import datetime
from tkinter.colorchooser import*
import psutil

languageset_path = 'C:\\Random Number Generator\\'
themeset_path = 'C:\\Random Number Generator\\'
setpage_path = 'C:\\Random Number Generator\\'
if not os.path.exists(languageset_path):
    os.mkdir(languageset_path)
if not os.path.exists(themeset_path):
    os.mkdir(themeset_path)
user_name = getpass.getuser() 
hostname = socket.gethostname()
drive = os.getenv("SystemDrive")
global lan
try:
    with open(f'{languageset_path}file.txt', "r+") as k:
        lines = k.read()
        first = lines.split('\n', 1)[0]
        str(first)
    try:
        if first == "Chinese Simplified":
            lan = 1
        elif first == "American English":
            lan = 2
        elif first == "Russian":
            lan = 3
        elif first == "German":
            lan = 4
        elif first == "Japanese":
            lan = 5
        else:
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: file.txt")
            try:
                with open(f'{languageset_path}file.txt', "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('Chinese Simplified')
                lan = 2
            except Exception:
                lan = 0
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
except Exception:
    try:
        with open(f'{languageset_path}file.txt', "w+") as k:
            k.write('Chinese Simplified')
        with open(f'{languageset_path}file.txt', "r+") as k:
            lines = k.read()
            first = lines.split('\n', 1)[0]
        try:
            lan = 2
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")


global themes
try:
    with open(f'{themeset_path}file2.txt', "r+") as g:
        lines = g.read()
        second = lines.split('\n', 1)[0]
        str(second)
    try:
        if second == "Classical":
            themes = 1
        elif second == "Adapta":
            themes = 2
        else:
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: file2.txt")
            try:
                with open(f'{themeset_path}file2.txt', "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('Classical')
                themes = 1
            except Exception:
                lan = 0
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
except Exception:
    try:
        with open(f'{themeset_path}file2.txt', "w+") as g:
            g.write('Classical')
        with open(f'{themeset_path}file2.txt', "r+") as g:
            lines = g.read()
            second = lines.split('\n', 1)[0]
        try:
            themes = 1
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")

if themes == 1:
    root=Tk()
if themes == 2:
    root=ThemedTk(theme="adapta", toplevel=True, themebg=True)
  
global sound2
sound_path = 'C:\\Random Number Generator\\'
if not os.path.exists(sound_path):
    os.mkdir(sound_path)
try:
    with open(f'{sound_path}file4.txt', "r+") as k:
        lines = k.read()
        third = lines.split('\n', 1)[0]
        str(third)
    try:
        if third == "SystemAsterisk":
            sound2 = 0
        elif third == "OFF":
            sound2 = 1
        else:
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: file4.txt")
            try:
                with open(f'{sound_path}file4.txt', "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('SystemAsterisk')
                sound2 = 0
            except Exception:
                sound2 = 1
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
except Exception:
    try:
        with open(f'{sound_path}file4.txt', "w+") as k:
            k.write('SystemAsterisk')
        with open(f'{sound_path}file4.txt', "r+") as k:
            lines = k.read()
            third = lines.split('\n', 1)[0]
        try:
            sound2 = 0
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")
        
global sound3
sound_path = 'C:\\Random Number Generator\\'
if not os.path.exists(sound_path):
    os.mkdir(sound_path)
try:
    with open(f'{sound_path}file5.txt', "r+") as k:
        lines = k.read()
        third = lines.split('\n', 1)[0]
        str(third)
    try:
        if third == "SystemAsterisk":
            sound3 = 0
        elif third == "OFF":
            sound3 = 1
        else:
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: file5.txt")
            try:
                with open(f'{sound_path}file5.txt', "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('SystemAsterisk')
                sound3 = 0
            except Exception:
                sound3 = 1
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
except Exception:
    try:
        with open(f'{sound_path}file5.txt', "w+") as k:
            k.write('SystemAsterisk')
        with open(f'{sound_path}file5.txt', "r+") as k:
            lines = k.read()
            third = lines.split('\n', 1)[0]
        try:
            sound3 = 0
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")

global setpage
try:
    with open(f'{setpage_path}file6.txt', "r+") as k:
        lines = k.read()
        first = lines.split('\n', 1)[0]
        str(first)
    try:
        if first == "0":
            setpage = 0
        elif first == "1":
            setpage = 1
        elif first == "2":
            setpage = 2
        elif first == "3":
            setpage = 3
        elif first == "4":
            setpage = 4
        else:
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: file6.txt")
            try:
                with open(f'{setpage_path}file6.txt', "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('0')
                setpage = 0
            except Exception:
                setpage = 0
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
except Exception:
    try:
        with open(f'{setpage_path}file6.txt', "w+") as k:
            k.write('0')
        with open(f'{setpage_path}file6.txt', "r+") as k:
            lines = k.read()
            first = lines.split('\n', 1)[0]
        try:
            lan = 0
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
    except Exception:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")



notification.notify(
    title = 'Random Number Generator',
    message = 'Random Number Generator正在运行' if lan == 1 else "Random Number Generator is running",
    app_icon = None,
    timeout = 5,
)
#----------------------------------------------------------
global outputset
outputset = 3
global f
f = 1
global e
e = 51
global end_control
global numset
numset = 2
global alpha
alpha = 100
global got
got = 1
global turn
turn = 1
global number_t
number_t = "N/A"
global state_run
state_run = 0
global tit
tit = 1
global showspeed
showspeed = 10

#####-------------------------------------------------------------------------

winWidth = 720
winHeight = 480
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry(f"{winWidth}x{winHeight}+{x}+{y}")
root.minsize(540,360)
root.title("Random Number Generator")
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)#>=win8.1
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor/75)
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()#<win8.1
    root.title("Random Number Generator [COMPATIBILITY MODE]")
    notification.notify(
    title = 'Random Number Generator',
    message = '因检测到系统版本过低,Random Number Generator已启动兼容模式' if lan == 1 else "Random Number Generator has started compatibility mode due to detection of an under-grade system version.",
    app_icon = None,
    timeout = 5,
)


#####----------------------------------------------------------------MAIN UNIT!!!!!!
# #98D2E4
# #FF6A00
# #006DDA


state_1 = Text(root, relief="flat", fg="#98D2E4", font=("Microsoft YaHei UI", 50))
state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
state_2 = Text(root, relief="flat", fg="#FF6A00", font=("Microsoft YaHei UI", 50))
state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
state_3 = Text(root, relief="flat", fg="#006DDA", font=("Microsoft YaHei UI", 50))
state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
#3
state_4 = Text(root, relief="flat", fg="blue", font=("Microsoft YaHei UI", 70))
state_4.place(relx=0.2, y=225, relwidth=0.6, height=220)
#1
state_5 = Text(root, relief="flat", fg="#66CCFF", font=("Microsoft YaHei UI", 60))
state_5.place(relx=0.05, y=225, relwidth=0.4, height=220)
state_6 = Text(root, relief="flat", fg="#e60000", font=("Microsoft YaHei UI", 60))
state_6.place(relx=0.55, y=225, relwidth=0.4, height=220)
#2
state_x = Label(root, text='×', font=("Microsoft YaHei UI", 50))
state_x.place(relx=0.45, y=225, relwidth=0.1, height=220)
state_x2 = Label(root, text='+', font=("Microsoft YaHei UI", 50))
state_x2.place(relx=0.45, y=225, relwidth=0.1, height=220)
#2-x
state_7 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_7.place(relx=0.01, y=225, relwidth=0.23, height=220)
state_8 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_8.place(relx=0.26, y=225, relwidth=0.23, height=220)
state_9 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_9.place(relx=0.51, y=225, relwidth=0.23, height=220)
state_0 = Text(root, relief="flat", font=("Microsoft YaHei UI", 40))
state_0.place(relx=0.76, y=225, relwidth=0.23, height=220)
#4

state_4.place_forget()
state_5.place_forget()
state_6.place_forget()
state_7.place_forget()
state_8.place_forget()
state_9.place_forget()
state_0.place_forget()
state_x.place_forget()
state_x2.place_forget()

state_1.configure(state='disabled')
state_2.configure(state='disabled')
state_3.configure(state='disabled')
state_4.configure(state='disabled')
state_5.configure(state='disabled')
state_6.configure(state='disabled')
state_7.configure(state='disabled')
state_8.configure(state='disabled')
state_9.configure(state='disabled')
state_0.configure(state='disabled')
####----------------------------------------------------------#preview

label_preview = Label(root,
                   text='⚠当前版本存在大量的待测试部分，部分设置可能导致运行不稳定',
                   font=("Microsoft YaHei UI", 8))
label_preview.place(relx=0.01, y=450, relwidth=0.8, height=30)

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
            global showspeed
            time.sleep(showspeed/100)
            global number_1
            try:
                number_1 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t1.pause()
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
            global showspeed
            time.sleep(showspeed/100)
            global number_2
            try:
                number_2 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t2.pause()
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
            global showspeed
            time.sleep(showspeed/100)
            global number_3
            try:
                number_3 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t3.pause()
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
class hello2(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello2, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        global w
        t = 0
        w = 0
        while self.__running.is_set():
            self.__flag.wait()
            if turn == 1:
                global showspeed
                time.sleep(showspeed)
                global number_4
                try:
                    number_4 = randint(f,e) if numset in [2, 3] else uniform(f,e)
                except Exception:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                    t5.pause()
                state_4.delete('0.0', END)
                state_4.insert(INSERT, number_4)
            if turn == 2:
                global number_t
                try:
                    number_t = f + t
                    t += 1
                    if number_t >= e:
                        t = 0
                        number_t = f
                except Exception:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                    t5.pause()
                state_4.delete('0.0', END)
                state_4.insert(INSERT, number_t)
                
                if w <= 7:
                    y = 8*w*w+1
                    w += 1
                if 7 < w <= 16:
                    y = 1.5*w*w+2.5*w+4
                    w += 1
                    

                time.sleep(0.5-0.001*y)
    

            
            #print(4)
            #time.sleep(1)
                    
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello3(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello3, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_5
            try:
                number_5 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t6.pause()
            state_5.delete('0.0', END)
            state_5.insert(INSERT, number_5)
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello4(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello4, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_6
            try:
                number_6 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t7.pause()
            state_6.delete('0.0', END)
            state_6.insert(INSERT, number_6)
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello5(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello5, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_7
            try:
                number_7 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t8.pause()
            state_7.delete('0.0', END)
            state_7.insert(INSERT, number_7)
            #print("3")
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello6(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello6, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_8
            try:
                number_8 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t9.pause()
            state_8.delete('0.0', END)
            state_8.insert(INSERT, number_8)
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello7(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello7, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_9
            try:
                number_9 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t0.pause()
            state_9.delete('0.0', END)
            state_9.insert(INSERT, number_9)
            #print("3")
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
class hello8(threading.Thread):
    
    def __init__(self, *args, **kwargs):
        super(hello8, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()    
        self.__flag.set()       
        self.__running = threading.Event()     
        self.__running.set()      
    def run(self):
        while self.__running.is_set():
            self.__flag.wait()
            global showspeed
            time.sleep(showspeed/100)
            global number_0
            try:
                number_0 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n" if lan == 1 else "There was a problem with the program, so it could not run.\n")
                t00.pause()
            state_0.delete('0.0', END)
            state_0.insert(INSERT, number_0)
            #print("3")
    def pause(self):
        self.__flag.clear()   

    def resume(self):
        self.__flag.set()   

    def stop(self):
        self.__flag.set()       
        self.__running.clear()       
        

def thread_4(func):
    global sound
    sound_path = 'C:\\Random Number Generator\\'
    if not os.path.exists(sound_path):
        os.mkdir(sound_path)
    try:
        with open(f'{sound_path}file3.txt', "r+") as k:
            lines = k.read()
            third = lines.split('\n', 1)[0]
            str(third)
        try:
            if third == "SystemAsterisk":
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                sound = 0
            elif third == "OFF":
                sound = 1
            else:
                control_info = showerror(title='Program Error',message="Please do not change the configuration file: file3.txt")
                try:
                    with open(f'{sound_path}file3.txt', "r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('SystemAsterisk')
                    sound = 0
                except Exception:
                    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")
    except Exception:
        try:
            with open(f'{sound_path}file3.txt', "w+") as k:
                k.write('SystemAsterisk')
            with open(f'{sound_path}file3.txt', "r+") as k:
                lines = k.read()
                third = lines.split('\n', 1)[0]
            try:
                sound = 0
            except Exception:
                control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
        except Exception:
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")


    
# sourcery skip: merge-list-append, move-assign-in-block
threads = []
t1 = Job()
t2 = mine()
t3 = hello()
t4 = threading.Thread(target=thread_4,args=(u'thread_state_4',))
t5 = hello2()
t6 = hello3()
t7 = hello4()
t8 = hello5()
t9 = hello6()
t0 = hello7()
t00 = hello8()
threads.append(t1)
t1.pause()
threads.append(t2)
t2.pause()
threads.append(t3)
t3.pause()
threads.append(t5)
t5.pause()
threads.append(t6)
t6.pause()
threads.append(t7)
t7.pause()
threads.append(t8)
t8.pause()
threads.append(t9)
t9.pause()
threads.append(t0)
t0.pause()
threads.append(t00)
t00.pause()

threads.append(t4)
if __name__ == '__main__':
    for t in threads:
        t.daemon=True
        #t.setDaemon(True) #被t.daemon=True替代(python 3.10)
        t.start()


#-----------------------------------------------------
def control():#control按钮
    global state_run
    state_run = 1
    control['state'] = DISABLED
    end['state'] = NORMAL
    setting['state'] = DISABLED
    
    end.place(relx=0.55, y=80, relwidth=0.4, height=100)
    control.place_forget()
    setting.place_forget()
    
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n"if lan == 1 else "Status: RUNNING\n")
    state.insert(INSERT, "您可以点击“停止运行”或按下键盘上的\"E\"查看结果。\n" if lan == 1 else "You can click 'Stop Running' or press 'E' on your keyboard to see the results.\n")
    state.insert(INSERT, "当前设定值： "if lan == 1 else "Current setting:")
    state.insert(INSERT, f)
    state.insert(INSERT, " <-> ")
    state.insert(INSERT, e)
    state.configure(state='disabled')
    state_1.configure(state='normal')
    state_2.configure(state='normal')
    state_3.configure(state='normal')
    state_4.configure(state='normal')
    state_5.configure(state='normal')
    state_6.configure(state='normal')
    state_7.configure(state='normal')
    state_8.configure(state='normal')
    state_9.configure(state='normal')
    state_0.configure(state='normal')
    t1.resume()
    t2.resume()
    t3.resume()
    t5.resume()
    t6.resume()
    t7.resume()
    t8.resume()
    t9.resume()
    t0.resume()
    t00.resume()

    global sound2
    if sound2 == 0:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    #message = "The Random Number Is "+ str(number_1)
    #control_info = showinfo(title='INFO',message=message)
def start_key(event):#control快捷键
    global state_run
    state_run = 1
    control['state'] = DISABLED
    end['state'] = NORMAL
    setting['state'] = DISABLED
    
    end.place(relx=0.55, y=80, relwidth=0.4, height=100)
    control.place_forget()
    setting.place_forget()
    
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n"if lan == 1 else "Status: RUNNING\n")
    state.insert(INSERT, "您可以点击“停止运行”或按下键盘上的\"E\"查看结果。\n" if lan == 1 else "You can click 'Stop Running' or press 'E' on your keyboard to see the results.\n")
    state.insert(INSERT, "当前设定值： "if lan == 1 else "Current setting:")
    state.insert(INSERT, f)
    state.insert(INSERT, " <-> ")
    state.insert(INSERT, e)
    state.configure(state='disabled')
    state_1.configure(state='normal')
    state_2.configure(state='normal')
    state_3.configure(state='normal')
    state_4.configure(state='normal')
    state_5.configure(state='normal')
    state_6.configure(state='normal')
    state_7.configure(state='normal')
    state_8.configure(state='normal')
    state_9.configure(state='normal')
    state_0.configure(state='normal')
    t1.resume()
    t2.resume()
    t3.resume()
    t5.resume()
    t6.resume()
    t7.resume()
    t8.resume()
    t9.resume()
    t0.resume()
    t00.resume()
    
    global sound2
    if sound2 == 0:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#-------------------------#
def end():  # sourcery skip: avoid-builtin-shadow
    global state_run
    state_run = 0
    control['state'] = NORMAL
    end['state'] = DISABLED
    setting['state'] = NORMAL

    global w
    w = 0
    
    control.place(relx=0.55, y=70, relwidth=0.4, height=70)
    end.place_forget()
    setting.place(relx=0.55, y=140, relwidth=0.4, height=50)
    
    list=[]#4
    for _ in range(300):
        r = randint(f,e) if numset in [2, 3] else uniform(f,e)
        if r not in list: list.append(r)
    try:
        number_a = list[0]
        number_b = list[1]
        number_c = list[2]
        number_d = list[3]
        number_e = list[4]
        number_f = list[5]
        number_g = list[6]
        number_h = list[7]
        number_i = list[8]
        number_j = list[9]
    except Exception:
        if numset in [2, 3]:
            number_a = randint(f,e)
            number_b = randint(f,e)
            number_c = randint(f,e)
            number_d = randint(f,e)
            number_e = randint(f,e)
            number_f = randint(f,e)
            number_g = randint(f,e)
            number_h = randint(f,e)
            number_i = randint(f,e)
            number_j = randint(f,e)
        else:
            number_a = uniform(f,e)
            number_b = uniform(f,e)
            number_c = uniform(f,e)
            number_d = uniform(f,e)
            number_e = uniform(f,e)
            number_f = uniform(f,e)
            number_g = uniform(f,e)
            number_h = uniform(f,e)
            number_i = uniform(f,e)
            number_j = uniform(f,e)
    #L1 = sample(range(f, e), 5)
    #print(L1)


    state_1.delete('0.0', END)
    state_1.insert(INSERT, number_e)
    state_2.delete('0.0', END)
    state_2.insert(INSERT, number_f)
    state_3.delete('0.0', END)
    state_3.insert(INSERT, number_g)
    
    state_4.delete('0.0', END)
    state_4.tag_configure("center", justify='center')
    if turn == 1:
        state_4.insert(END, number_h, "center")
    else:
        state_4.insert(END, number_t, "center")
    state_5.delete('0.0', END)
    state_5.tag_configure("center", justify='center')
    state_5.insert(END, number_i, "center")
    state_6.delete('0.0', END)
    state_6.tag_configure("center", justify='center')
    state_6.insert(END, number_j, "center")
    
    state_7.delete('0.0', END)
    state_7.insert(INSERT, number_a)
    state_8.delete('0.0', END)
    state_8.insert(INSERT, number_b)
    state_9.delete('0.0', END)
    state_9.insert(INSERT, number_c)
    state_0.delete('0.0', END)
    state_0.insert(INSERT, number_d)


    state_1.configure(state='disabled')
    state_2.configure(state='disabled')
    state_3.configure(state='disabled')
    state_4.configure(state='disabled')
    state_5.configure(state='disabled')
    state_6.configure(state='disabled')
    state_7.configure(state='disabled')
    state_8.configure(state='disabled')
    state_9.configure(state='disabled')
    state_0.configure(state='disabled')
    t1.pause()
    t2.pause()
    t3.pause()
    t5.pause()
    t6.pause()
    t7.pause()
    t8.pause()
    t9.pause()
    t0.pause()
    t00.pause()

    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：空闲\n"if lan == 1 else"Status: IDLE\n")
    state.insert(INSERT, "您可以在设置参数后点击“开始运行”或按下键盘上的\"B\"启动程序并产生随机数。" if lan == 1 else "You can click 'Start Running' after setting the parameters or press 'B' on your keyboard to start the program and generate random numbers..")
    state.configure(state='disabled')
    global sound3
    if sound3 == 0:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
def end_key(event):#end快捷键  # sourcery skip: avoid-builtin-shadow
    control['state'] = NORMAL
    end['state'] = DISABLED
    setting['state'] = NORMAL

    control.place(relx=0.55, y=70, relwidth=0.4, height=70)
    end.place_forget()
    setting.place(relx=0.55, y=140, relwidth=0.4, height=50)
    
    global w
    w = 0
    
    list=[]#4
    for _ in range(300):
        r = randint(f,e) if numset in [2, 3] else uniform(f,e)
        if r not in list: list.append(r)
    try:
        number_a = list[0]
        number_b = list[1]
        number_c = list[2]
        number_d = list[3]
        number_e = list[4]
        number_f = list[5]
        number_g = list[6]
        number_h = list[7]
        number_i = list[8]
        number_j = list[9]
    except Exception:
        if numset in [2, 3]:
            number_a = randint(f,e)
            number_b = randint(f,e)
            number_c = randint(f,e)
            number_d = randint(f,e)
            number_e = randint(f,e)
            number_f = randint(f,e)
            number_g = randint(f,e)
            number_h = randint(f,e)
            number_i = randint(f,e)
            number_j = randint(f,e)
        else:
            number_a = uniform(f,e)
            number_b = uniform(f,e)
            number_c = uniform(f,e)
            number_d = uniform(f,e)
            number_e = uniform(f,e)
            number_f = uniform(f,e)
            number_g = uniform(f,e)
            number_h = uniform(f,e)
            number_i = uniform(f,e)
            number_j = uniform(f,e)
    #L1 = sample(range(f, e), 5)
    #print(L1)


    state_1.delete('0.0', END)
    state_1.insert(INSERT, number_e)
    state_2.delete('0.0', END)
    state_2.insert(INSERT, number_f)
    state_3.delete('0.0', END)
    state_3.insert(INSERT, number_g)
    
    state_4.delete('0.0', END)
    state_4.tag_configure("center", justify='center')
    if turn == 1:
        state_4.insert(END, number_h, "center")
    else:
        state_4.insert(END, number_t, "center")

    state_5.delete('0.0', END)
    state_5.tag_configure("center", justify='center')
    state_5.insert(END, number_i, "center")
    state_6.delete('0.0', END)
    state_6.tag_configure("center", justify='center')
    state_6.insert(END, number_j, "center")
    
    state_7.delete('0.0', END)
    state_7.insert(INSERT, number_a)
    state_8.delete('0.0', END)
    state_8.insert(INSERT, number_b)
    state_9.delete('0.0', END)
    state_9.insert(INSERT, number_c)
    state_0.delete('0.0', END)
    state_0.insert(INSERT, number_d)


    state_1.configure(state='disabled')
    state_2.configure(state='disabled')
    state_3.configure(state='disabled')
    state_4.configure(state='disabled')
    state_5.configure(state='disabled')
    state_6.configure(state='disabled')
    state_7.configure(state='disabled')
    state_8.configure(state='disabled')
    state_9.configure(state='disabled')
    state_0.configure(state='disabled')
    t1.pause()
    t2.pause()
    t3.pause()
    t5.pause()
    t6.pause()
    t7.pause()
    t8.pause()
    t9.pause()
    t0.pause()
    t00.pause()

    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：空闲\n"if lan == 1 else"Status: IDLE\n")
    state.insert(INSERT, "您可以在设置参数后点击“开始运行”或按下键盘上的\"B\"启动程序并产生随机数。" if lan == 1 else "You can click 'Start Running' after setting the parameters or press 'B' on your keyboard to start the program and generate random numbers.")
    state.configure(state='disabled')
    global sound3
    if sound3 == 0:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#-----------------------------------------------------
def github():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=bug_report.md&title=')
def github2():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=feature_request.md&title=')
def github3():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=seek-help.md&title=%5BSeek+Help%5D')        
def discuss():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/discussions')
def minimize():
    root.iconify()
def maxmize():
    root.state("zoomed")
def zoom():
    root.attributes("-fullscreen", True)
def diszoom():
    root.attributes("-fullscreen", False)
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
def redo_window():
    '''
    r_h = root.winfo_height()
    r_w = root.winfo_width()
    r_hg = 720
    r_wg = 480
    if r_h < r_hg:
        r_a = r_hg - r_h
        r_b = r_a // 10
        while r_h < r_hg:
            r_h += r_b
            root.geometry(f"{r_h}x{r_w}")
            time.sleep(0.1)
            #print(1)
    '''
    root.geometry('720x480')

##---------------------------------------------------
def t_close_handler_about():
    root.attributes('-disabled', 0)
    window_about.destroy()
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)
def about():
    i = 0
    al = 0.99
    while al >= 0.6:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al -= i*4
    def mean():
        def t_close_handler_mean():
            window_about.attributes('-disabled', 0)
            window_mean.destroy()
        global window_mean
        window_mean = Toplevel(window_about)
        window_mean.geometry("680x340")
        window_mean.resizable(0,0)
        window_mean.transient(window_about)
        window_mean.protocol("WM_DELETE_WINDOW", t_close_handler_mean)
        window_mean.title("About-Nature")
        window_about.attributes('-disabled', 1)
        ti_window = Label(window_mean,
                    text='Harmony(23H2)\n',
                    font=("Microsoft YaHei UI", 15),
                    foreground="black")
        ti_window.pack()
        state = Text(window_mean, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.1, y=80, relwidth=0.35, height=230)
        state.insert(INSERT, "Harmony 版本说明\n"if lan == 1 else"Release notes of Harmony\n")
        state.insert(INSERT, "更符合认知的显示效果\n"if lan == 1 else"More real\n")
        state.insert(INSERT, "更快速上手的运行逻辑\n"if lan == 1 else"More easy\n")
        state.insert(INSERT, "更简洁明了的操作界面\n"if lan == 1 else"More clear\n")
        state.insert(INSERT, "让你从中感受到和谐(Harmony)的韵味\n"if lan == 1 else"Let's have fun with Harmony!")
        state2 = Text(window_mean, relief="flat", font=("Microsoft YaHei UI", 10))
        state2.place(relx=0.55, y=80, relwidth=0.35, height=230)
        state2.insert(INSERT, "Harmony 维护状态\n" if lan == 1 else "Maintenance status of Harmony\n")
        state2.insert(INSERT, "支持状态：允许功能更新\n结束维护时间：25H2（计划）" if lan == 1 else"Status: feature updates\nEnd of support: 25H2(PLAN)")
        state2.configure(state='disabled')
    def update():
        webbrowser.open('https://github.com/12sdj/Random-Number-Generator/releases/')
    global window_about
    window_about = Toplevel(root)
    window_about.geometry("680x340")
    window_about.resizable(0,0)
    window_about.transient(root)
    window_about.title("关于"if lan == 1 else"About")
    #window_about.mainloop()
    window_about.protocol("WM_DELETE_WINDOW", t_close_handler_about)
    root.attributes('-disabled', 1)
    #Unint
    label_a = Label(window_about,
                   text="关于"if lan == 1 else"About",
                   font=("Microsoft YaHei UI", 12))
    label_a.pack()
    tip = Text(window_about, relief="flat", font=("Microsoft YaHei UI", 10))
    tip.place(relx=0.1, y=70, relwidth=0.8, height=190)
    tip.insert(INSERT, 'Random Number Generator\n')
    tip.insert(INSERT, 'Version 4.4.0.134_Release\n')
    tip.insert(INSERT, '2024/2/17 21:08(UTC+8) Update 62\n')
    tip.insert(INSERT, 'Copyright (c) 2022 12sdj')
    tip.configure(state='disabled')
    control = Button(window_about, text ="查看更多信息"if lan == 1 else "More", command = mean)
    control.place(relx=0.2, y=290, relwidth=0.3, height=40)
    control2 = Button(window_about, text ="检查更新" if lan == 1 else"Check for Updates", command = update)
    control2.place(relx=0.5, y=290, relwidth=0.3, height=40)
##----------------------------------------------------
def t_close_handler_license():
    root.attributes('-disabled', 0)
    window_license.destroy()
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)
def license():
    i = 0
    al = 0.99
    while al >= 0.6:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al -= i*4
    global window_license
    window_license = Toplevel(root)
    window_license.geometry("780x590")
    window_license.resizable(0,0)
    window_license.transient(root)
    #window_license.attributes('-toolwindow', True)
    window_license.protocol("WM_DELETE_WINDOW", t_close_handler_license)
    window_license.title('协议'if lan == 1 else "License")
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_license,
                   text='协议'if lan == 1 else "License",
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()
    state = ScrolledText(window_license, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=40, relwidth=0.96, height=530)
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
    setting['state']=NORMAL
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)

def setting():  # sourcery skip: avoid-builtin-shadow
    #setting['state']=DISABLED
    if setpage == 0:
        i = 0
        al = 0.99
        while al >= 0.6:
            root.attributes('-alpha',al)
            time.sleep(0.01+(i*3))
            i += 0.01
            al -= i*4

        def t_close_handler_interface():
            window_setting.attributes('-disabled', 0)
            window_interface.destroy()
        def interface_command():
            def func(*args):
                global lan
                if (cmb.get() == "简体中文（中国大陆）"):
                    try:
                        with open(languageset_path+"file.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('Chinese Simplified')
                        lan = 1
                        state['state'] = NORMAL
                        state.delete('0.0', END)
                        state.insert(INSERT, "语言已切换至'简体中文（中国大陆）' \n")
                        state.insert(INSERT, "程序需要重启以完成该更改")
                        state['state'] = DISABLED
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")

                else:
                    try:
                        with open(languageset_path+"file.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('American English')

                        lan = 2
                        state['state'] = NORMAL
                        state.delete('0.0', END)
                        state.insert(INSERT, "Language switched to 'English(United States)' \n")
                        state.insert(INSERT, "The program needs to be restarted to complete the change")
                        state['state'] = DISABLED

                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")                       
            def funk(*args):
                global themes
                if (cmd.get() == "Classical"):
                    try:
                        with open(themeset_path+"file2.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('Classical')
                        themes = 1
                        state['state'] = NORMAL
                        state.delete('0.0', END)
                        state.insert(INSERT, "Theme switched to 'Classical' \n")
                        state.insert(INSERT, "The program needs to be restarted to complete the change")
                        state['state'] = DISABLED
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                else:
                    try:
                        with open(themeset_path+"file2.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('Adapta')
                        themes = 2
                        state['state'] = NORMAL
                        state.delete('0.0', END)
                        state.insert(INSERT, "Theme switched to 'Adapta' \n")
                        state.insert(INSERT, "The program needs to be restarted to complete the change")
                        state['state'] = DISABLED
                    except Exception:
                        if themes == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            def apply():
                global alpha
                alpha = scale.get()
                alpha2 = alpha / 100
                root.attributes('-alpha',alpha2)
                tr_state.configure(state='normal')
                tr_state.delete('0.0', END)
                tr_state.insert(INSERT, f"{str(round(scale.get(),2))}")
                tr_state.configure(state='disabled')
            
            def ch():
                global tit
                tit = var_title.get()
                if tit == 1:
                    root.title("Random Number Generator")
                if tit == 2:
                    root.title("Random Number Generator 4")
                if tit == 3:
                    root.title("Random Number Generator HARMONY")
            
            def func3():
                pass
            
            global window_interface
            window_interface = Toplevel(window_setting)
            window_interface.geometry("720x680")
            window_interface.resizable(0,0)
            window_interface.transient(window_setting)
            window_interface.protocol("WM_DELETE_WINDOW", t_close_handler_interface)
            window_interface.title("设置-软件界面" if lan == 1 else "Setting-Software UI")
            window_setting.attributes('-disabled', 1)
            
            label_a = Label(window_interface,
                    text='显示' if lan == 1 else 'Display',
                    font=("Microsoft YaHei UI", 20))
            label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
            
            
            label_a_1 = Label(window_interface,
                    text='语言' if lan == 1 else 'Language',
                    font=("Microsoft YaHei UI", 10))
            label_a_1.place(relx=0.31, y=10, relwidth=0.15, height=40)
            label_a_1_state = Label(window_interface,
                    text='软件将使用此语言显示。' if lan == 1 else 'The software will display in this language.',
                    font=("Microsoft YaHei UI", 8))
            label_a_1_state.place(relx=0.31, y=50, relwidth=0.69, height=25)
            mode = StringVar()
            cmb = Combobox(window_interface,values=mode, state='readonly')
            cmb['value'] = ('简体中文（中国大陆）','English(United States)')
            cmb.current(lan-1)
            cmb.bind("<<ComboboxSelected>>",func)
            cmb.place(relx=0.31, y=75, relwidth=0.31, height=40)
            
            label_a_2 = Label(window_interface,
                    text='标题栏' if lan == 1 else 'Titlebar',
                    font=("Microsoft YaHei UI", 10))
            label_a_2.place(relx=0.31, y=115, relwidth=0.15, height=40)
            label_a_2_state = Label(window_interface,
                    text='主窗口标题栏将使用该配置显示。' if lan == 1 else 'The main window title bar will be displayed \nusing this configuration.',
                    font=("Microsoft YaHei UI", 8))
            label_a_2_state.place(relx=0.31, y=155, relwidth=0.69, height=45)
            var_title = IntVar()
            var_title.set(tit)
            b = Radiobutton(window_interface,text="软件名" if lan == 1 else 'Software name',variable = var_title ,value =1,command=ch)
            b.place(relx=0.31, y=200, relwidth=0.23, height=40)
            b2 = Radiobutton(window_interface,text="软件名+主版本号" if lan == 1 else 'Software Name + Major Version',variable = var_title ,value =2,command=ch)
            b2.place(relx=0.31, y=240, relwidth=0.46, height=40)
            b3 = Radiobutton(window_interface,text="软件名+宣传词" if lan == 1 else 'Software Name + Promotional Message',variable = var_title ,value =3,command=ch)
            b3.place(relx=0.31, y=280, relwidth=0.52, height=40)
            
            label_b = Label(window_interface,
                        text='个性化' if lan == 1 else 'Personali-\nzation',
                        font=("Microsoft YaHei UI", 20))
            label_b.place(relx=0.01, y=340, relwidth=0.3, height=140) 
            
            label_b_1 = Label(window_interface,
                        text='主题' if lan == 1 else 'Theme',
                        font=("Microsoft YaHei UI", 10))
            label_b_1.place(relx=0.31, y=340, relwidth=0.1, height=40) 
            label_b_1_state = Label(window_interface,
                        text='选择不同风格的主题使软件富有个性' if lan == 1 else 'Choose from a variety of themes to \npersonalize your software.',
                        font=("Microsoft YaHei UI", 8))
            label_b_1_state.place(relx=0.31, y=380, relwidth=0.69, height=45) 
            theme = StringVar()
            cmd = Combobox(window_interface,values=theme, state='readonly')
            cmd.place(relx=0.31, y=425, relwidth=0.31, height=40)
            cmd['value'] = ('Classical','Adapta')
            cmd.current(themes-1)
            cmd.bind("<<ComboboxSelected>>",funk)
            label_b_2 = Label(window_interface,
                        text='不透明度' if lan == 1 else 'Opacity',
                        font=("Microsoft YaHei UI", 10))
            label_b_2.place(relx=0.31, y=465, relwidth=0.2, height=40) 
            tr_apply = Button(window_interface,
                        text='应用'if lan == 1 else "APPLY",
                        command=apply)
            tr_apply.place(relx=0.51, y=465, relwidth=0.2, height=40)
            scale = Scale(window_interface, from_=10, to_=100,orient=HORIZONTAL,length=220)
            scale.set(alpha)
            scale.place(relx=0.31, y=515, relwidth=0.49, height=20) 
            tr_state = Text(window_interface, relief="flat", font=("Microsoft YaHei UI", 10))
            tr_state.place(relx=0.82, y=505, relwidth=0.12, height=40)
            tr_state.insert(INSERT, f"{str(round(scale.get(),2))}")
            tr_state.configure(state='disabled')
            label_b_3 = Label(window_interface,
                        text='透明过渡效果' if lan == 1 else 'Transparent Transition Effect',
                        font=("Microsoft YaHei UI", 10))
            label_b_3.place(relx=0.31, y=545, relwidth=0.6, height=40) 
            tte = StringVar()
            cmb3 = Combobox(window_interface,values=tte, state='readonly')
            cmb3['value'] = ('ON','OFF')
            cmb3['state'] = DISABLED
            cmb3.current(0)
            cmb3.bind("<<ComboboxSelected>>",func3)
            cmb3.place(relx=0.31, y=585, relwidth=0.3, height=40) 
            
            label_tip2 = Label(window_interface,
                    text='关闭窗口以保存设置项' if lan == 1 else 'CLOSE TO SAVE THE SETTINGS',
                    font=("Microsoft YaHei UI", 10))
            label_tip2.pack(side='bottom')
        
        
        def t_close_handler_output():
            window_setting.attributes('-disabled', 0)
            window_output.destroy()
        def output_command():
            def chosen():
                global numset
                global turn
                numset = var.get()
                if numset in [1, 3, 4]:
                    var5.set(1)
                    label_t.place_forget()
                    bt.place_forget()
                    bt2.place_forget()
                    turn = 1
                else:
                    if outputset == 1:
                        turn = 2
                        label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
                        bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
                        bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)

            def chosen2():
                global outputset
                outputset = var3.get()
                if outputset == 1:      
                    state_4.place(relx=0.2, y=225, relwidth=0.6, height=220)
                    state_1.place_forget()
                    state_2.place_forget()
                    state_3.place_forget()
                    state_5.place_forget()
                    state_6.place_forget()
                    state_7.place_forget()
                    state_8.place_forget()
                    state_9.place_forget()
                    state_0.place_forget()
                    state_x.place_forget()
                    state_x2.place_forget()
                    label_b.place_forget()
                    bx.place_forget()
                    bx2.place_forget()
                    bx3.place_forget()
                    var4.set(1)

                    if numset == 2:
                        label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
                        bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
                        bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)
                    else:
                        var5.set(1)
                        label_t.place_forget()
                        bt.place_forget()
                        bt2.place_forget()
                if outputset == 2:
                    state_5.place(relx=0.05, y=225, relwidth=0.4, height=220)
                    state_6.place(relx=0.55, y=225, relwidth=0.4, height=220)
                    state_1.place_forget()
                    state_2.place_forget()
                    state_3.place_forget()
                    state_4.place_forget()
                    state_7.place_forget()
                    state_8.place_forget()
                    state_9.place_forget()
                    state_0.place_forget()
                    var5.set(1)
                    label_t.place_forget()
                    bt.place_forget()
                    bt2.place_forget()


                    label_b.place(relx=0.31, y=360, relwidth=0.18, height=40)
                    bx.place(relx=0.31, y=400, relwidth=0.14, height=40)
                    bx2.place(relx=0.45, y=400, relwidth=0.14, height=40)
                    bx3.place(relx=0.59, y=400, relwidth=0.14, height=40)
                if outputset == 3:
                    state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
                    state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
                    state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
                    state_4.place_forget()
                    state_5.place_forget()
                    state_6.place_forget()
                    state_7.place_forget()
                    state_8.place_forget()
                    state_9.place_forget()
                    state_0.place_forget()
                    state_x.place_forget()
                    state_x2.place_forget()
                    label_b.place_forget()
                    bx.place_forget()
                    bx2.place_forget()
                    bx3.place_forget()
                    var4.set(1)
                    var5.set(1)
                    label_t.place_forget()
                    bt.place_forget()
                    bt2.place_forget()

                if outputset == 4:
                    state_7.place(relx=0.01, y=225, relwidth=0.23, height=220)
                    state_8.place(relx=0.26, y=225, relwidth=0.23, height=220)
                    state_9.place(relx=0.51, y=225, relwidth=0.23, height=220)
                    state_0.place(relx=0.76, y=225, relwidth=0.23, height=220)
                    state_1.place_forget()
                    state_2.place_forget()
                    state_3.place_forget()
                    state_4.place_forget()
                    state_5.place_forget()
                    state_6.place_forget()
                    state_x.place_forget()
                    state_x2.place_forget()
                    label_b.place_forget()
                    bx.place_forget()
                    bx2.place_forget()
                    bx3.place_forget()
                    var4.set(1)
                    var5.set(1)
                    label_t.place_forget()
                    bt.place_forget()
                    bt2.place_forget()


            def chosen3():
                get = var4.get()
                global got
                if get == 1:
                    state_x.place_forget()
                    state_x2.place_forget()

                    got = 1
                if get == 2:
                    state_x.place_forget()
                    state_x2.place(relx=0.45, y=225, relwidth=0.1, height=220)

                    got = 2
                if get == 3:
                    state_x2.place_forget()
                    state_x.place(relx=0.45, y=225, relwidth=0.1, height=220)

                    got = 3

            def chosen4():
                got2 = var5.get()
                global turn    
                if got2 == 1:
                    turn = 1
                if got2 == 2:
                    turn = 2


            def application():
                global f
                global e
                global numset
                try:

                    f = float(label_a_3.get())
                    e = float(label_a_4.get())

                        #####
                    if f >= e:
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（前一个控件的值不能大于或等于后一个控件的值）\n建议更改后再次检查设置\n" if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the value of the previous control cannot be greater than or equal to the value of the latter control)\nIt is recommended to check the setting again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1
                        e = 51
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)
                    if numset == 1:
                        control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")

                    if numset == 2:
                        if f <= 0 or e <= 0 or f % 1 != 0 or e % 1 != 0 or f <= 0.0 or e <= 0.0 or f % 1 != 0.0 or e % 1 != 0.0:
                            control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n"if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the values of both controls must be a positive integer)\nIt is recommended to check the settings again after changing\n")
                            control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                            f = 1
                            e = 51
                            label_a_3.delete(0, "end")
                            label_a_3.insert(0, f)
                            label_a_4.delete(0, "end")
                            label_a_4.insert(0, e)
                        else:
                            f = int(label_a_3.get())
                            e = int(label_a_4.get())
                            control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")
                    if numset == 3:
                        if f % 1 != 0 or e % 1 != 0 or f % 1 != 0.0 or e % 1 != 0.0:
                            control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the values of both controls must be an integer)\nIt is recommended to check the settings again after changing\n")
                            control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                            f = 1
                            e = 51
                            label_a_3.delete(0, "end")
                            label_a_3.insert(0, f)
                            label_a_4.delete(0, "end")
                            label_a_4.insert(0, e)
                        else:
                            f = int(label_a_3.get())
                            e = int(label_a_4.get())
                            control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")
                    if numset == 4:
                        s=str(f).split('.')
                        s1=str(e).split('.')
                        if float(s[1])==0 or float(s1[1])==0:
                            control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件必须是一个小数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values at:\n• Build Settings - Range (both controls must be a decimal)\nIt is recommended to check the settings again after changing\n")
                            control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                            f = 1.5
                            e = 51.5
                            label_a_3.delete(0, "end")
                            label_a_3.insert(0, f)
                            label_a_4.delete(0, "end")
                            label_a_4.insert(0, e)
                        else:
                            control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")

                except Exception:
                    f = str(label_a_3.get())
                    e = str(label_a_4.get())

                    if not f or not e:
                        control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个输入框不能为空，请填写符合您配置的值）。\n建议更改后再次检查设置\n"if lan == 1 else"There is a problem with the program, so Check Settings cannot be run. \nAfter preliminary judgment, the program believes that the cause of the error may be caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the two input fields cannot be empty, please fill in the values that match your configuration). \nIt is recommended to check the settings again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1
                        e = 51
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)
                    else:
                        s=str(f).split('.')
                        s1=str(e).split('.')
                        try:
                            if float(s[1])==0 or float(s1[1])==0:
                                if numset == 2:
                                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n"if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the values of both controls must be a positive integer)\nIt is recommended to check the settings again after changing\n")
                                    control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                                    f = 1
                                    e = 51
                                    label_a_3.delete(0, "end")
                                    label_a_3.insert(0, f)
                                    label_a_4.delete(0, "end")
                                    label_a_4.insert(0, e)

                                if numset == 3:                    
                                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the values of both controls must be an integer)\nIt is recommended to check the settings again after changing\n")
                                    control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                                    f = 1
                                    e = 51
                                    label_a_3.delete(0, "end")
                                    label_a_3.insert(0, f)
                                    label_a_4.delete(0, "end")
                                    label_a_4.insert(0, e)
                        except Exception:
                            control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（输入的值必须是一个有理数）。\n建议更改后再次检查设置\n" if lan == 1 else "There is a problem with the program, so Check Settings cannot be run. \nAfter preliminary judgment, the program believes that the cause of the error may be caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the value entered must be a rational number). \nIt is recommended to check the settings again after changing\n")
                            control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                            f = 1
                            e = 51
                            label_a_3.delete(0, "end")
                            label_a_3.insert(0, f)
                            label_a_4.delete(0, "end")
                            label_a_4.insert(0, e)

            def eventhandler(event):
                label_a_3.focus()
            def eventhandler2(event):
                label_a_4.focus()
            def speed():
                global showspeed
                showspeed = var6.get()
            global showspeed
            global window_output
            window_output = Toplevel(window_setting)
            window_output.geometry("720x680")
            window_output.resizable(0,0)
            window_output.transient(window_setting)
            window_output.protocol("WM_DELETE_WINDOW", t_close_handler_output)
            window_output.title("设置-输出" if lan == 1 else "Setting-Output")
            window_setting.attributes('-disabled', 1)
            
            label_a = Label(window_output,
                        text='数值' if lan == 1 else 'Numeric',
                        font=("Microsoft YaHei UI", 20))
            label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
            
            label_a_1 = Label(window_output,
                        text='类型' if lan == 1 else 'Type',
                        font=("Microsoft YaHei UI", 10))
            label_a_1.place(relx=0.31, y=10, relwidth=0.3, height=40)

            var = IntVar()
            var.set(numset)
            b = Radiobutton(window_output,text="有理数" if lan == 1 else 'Rational Number',variable = var ,value =1,command=chosen)
            b.place(relx=0.31, y=50, relwidth=0.3, height=40)
            b2 = Radiobutton(window_output,text="正整数" if lan == 1 else 'Positive Integer',variable = var ,value =2,command=chosen)
            b2.place(relx=0.31, y=90, relwidth=0.3, height=40)
            b3 = Radiobutton(window_output,text="整数" if lan == 1 else 'Integer',variable = var ,value =3,command=chosen)
            b3.place(relx=0.31, y=130, relwidth=0.2, height=40)
            b4 = Radiobutton(window_output,text="小数" if lan == 1 else 'Decimal',variable = var ,value =4,command=chosen)
            b4.place(relx=0.31, y=170, relwidth=0.2, height=40) 

            label_a_2 = Label(window_output,
                        text='范围' if lan == 1 else 'Range',
                        font=("Microsoft YaHei UI", 10))
            label_a_2.place(relx=0.31, y=210, relwidth=0.1, height=40)

            label_a_3 = Entry(window_output, font=("Microsoft YaHei UI", 10),background='gray')
            label_a_3.place(relx=0.31, y=250, relwidth=0.15, height=40)
            label_a_5 = Label(window_output,text = '-', font=("Microsoft YaHei UI", 10))
            label_a_5.place(relx=0.46, y=260, relwidth=0.02, height=30)
            label_a_4 = Entry(window_output, font=("Microsoft YaHei UI", 10),background='gray')
            label_a_4.place(relx=0.48, y=250, relwidth=0.15, height=40)
            label_a_3.bind_all('<Control-q>', eventhandler)
            label_a_4.bind_all('<Control-w>', eventhandler2)
            application = Button(window_output,
                            text='应用设置' if lan == 1 else 'APPLY',
                            command=application)

            application.place(relx=0.7, y=250, relwidth=0.2, height=40)

            def show_message(event):
                label['text'] = "使用Ctrl+q和Ctrl+w以便更快聚焦输入框" if lan == 1 else "Using Ctrl+q and Ctrl+w"

            def hide_message(event):
                label['text'] = "❔[获取提示]" if lan == 1 else "[Tip]"

            label = Label(window_output, text="❔[获取提示]" if lan == 1 else "[Tip]")
            label.place(relx=0.41, y=210, relwidth=0.71, height=40)
            label.bind("<Enter>", show_message)
            label.bind("<Leave>", hide_message)

            label_a_3.delete(0, "end")
            label_a_3.insert(0, f)
            label_a_4.delete(0, "end")
            label_a_4.insert(0, e)
            label_b_2 = Label(window_output,
                        text='数量' if lan == 1 else 'Quantity',
                        font=("Microsoft YaHei UI", 10))
            label_b_2.place(relx=0.31, y=290, relwidth=0.4, height=30)
            var3 = IntVar()
            var3.set(outputset)
            b = Radiobutton(window_output,text="1",variable = var3 ,value =1,command=chosen2)
            b.place(relx=0.31, y=320, relwidth=0.1, height=40)
            b2 = Radiobutton(window_output,text="2",variable = var3 ,value =2,command=chosen2)
            b2.place(relx=0.41, y=320, relwidth=0.1, height=40)
            b3 = Radiobutton(window_output,text="3",variable = var3 ,value =3,command=chosen2)
            b3.place(relx=0.51, y=320, relwidth=0.1, height=40)
            b4 = Radiobutton(window_output,text="4",variable = var3 ,value =4,command=chosen2)
            b4.place(relx=0.61, y=320, relwidth=0.1, height=40) 

            label_b = Label(window_output,
                        text='显示配对符号'if lan == 1 else"Pairing Symbol",
                        font=("Microsoft YaHei UI", 8))
            label_b.place(relx=0.31, y=360, relwidth=0.18, height=40)



            var4 = IntVar()
            var4.set(got)
            bx = Radiobutton(window_output,text="关闭"if lan == 1 else"OFF",variable = var4 ,value =1,command=chosen3)
            bx.place(relx=0.31, y=400, relwidth=0.14, height=40)
            bx2 = Radiobutton(window_output,text="显示'+'" if lan == 1 else "Show'+'",variable = var4 ,value =2,command=chosen3)
            bx2.place(relx=0.45, y=400, relwidth=0.14, height=40)
            bx3 = Radiobutton(window_output,text="显示'×'" if lan == 1 else "Show'×'",variable = var4 ,value =3,command=chosen3)
            bx3.place(relx=0.59, y=400, relwidth=0.14, height=40)

            if outputset != 2:
                var4.set(1)
                label_b.place_forget()
                bx.place_forget()
                bx2.place_forget()
                bx3.place_forget()



            label_t = Label(window_output,
                        text='以轮播替代随机'if lan == 1 else"Sequential Playback",
                        font=("Microsoft YaHei UI", 8))
            label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
            var5 = IntVar()
            var5.set(turn)
            bt = Radiobutton(window_output,text="关闭" if lan == 1 else 'OFF',variable = var5 ,value =1,command=chosen4)
            bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
            bt2 = Radiobutton(window_output,text="启用" if lan == 1 else 'ON',variable = var5 ,value =2,command=chosen4)
            bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)
            if outputset != 1 or numset != 2:
                var5.set(1)
                label_t.place_forget()
                bt.place_forget()
                bt2.place_forget()

            
            
            
            label_c = Label(window_output,
                text='输出' if lan == 1 else 'Output',
                font=("Microsoft YaHei UI", 20))
            label_c.place(relx=0.01, y=450, relwidth=0.3, height=90)
            label_c_1 = Label(window_output,
                text='间隔' if lan == 1 else 'Interval',
                font=("Microsoft YaHei UI", 10))
            label_c_1.place(relx=0.31, y=450, relwidth=0.3, height=40)
            var6 = IntVar()
            var6.set(showspeed)
            c = Radiobutton(window_output,text="缓慢" if lan == 1 else "Slow",variable = var6 ,value = 30,command=speed)
            c.place(relx=0.31, y=490, relwidth=0.2, height=40)
            c2 = Radiobutton(window_output,text="适中" if lan == 1 else "Normal",variable = var6 ,value = 10,command=speed)
            c2.place(relx=0.31, y=530, relwidth=0.2, height=40)
            c3 = Radiobutton(window_output,text="较快" if lan == 1 else "Fast",variable = var6 ,value = 6,command=speed)
            c3.place(relx=0.31, y=570, relwidth=0.2, height=40)
            c4 = Radiobutton(window_output,text="非常快" if lan == 1 else "Very Fast",variable = var6 ,value = 2,command=speed)
            c4.place(relx=0.31, y=610, relwidth=0.24, height=40) 
            
            label_tip2 = Label(window_output,
                    text='关闭窗口以保存设置项' if lan == 1 else 'CLOSE TO SAVE THE SETTINGS',
                    font=("Microsoft YaHei UI", 10))
            label_tip2.pack(side='bottom')
        def t_close_handler_accessibility():
            window_setting.attributes('-disabled', 0)
            window_accessibility.destroy()
        def accessibility_command():
            def func_a1():
                pass
            
            def func_b1():
                pass
            
            def func_b2():
                pass
            
            def func_b3():
                pass
            
            def func_d1(*args):
                global setpage
                if (cmbd1.get() == "OFF"):
                    try:
                        with open(setpage_path+"file6.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('0')
                        setpage = 0
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                elif (cmbd1.get() == "Software UI"):
                    try:
                        with open(setpage_path+"file6.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('1')
                        setpage = 1
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                elif (cmbd1.get() == "Output"):
                    try:
                        with open(setpage_path+"file6.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('2')
                        setpage = 2
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                elif (cmbd1.get() == "Accessibility"):
                    try:
                        with open(setpage_path+"file6.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('3')
                        setpage = 3
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                elif (cmbd1.get() == "Software Notificantion"):
                    try:
                        with open(setpage_path+"file6.txt","r+") as d:
                            d.read()
                            d.seek(0)
                            d.truncate()
                            d.write('4')
                        setpage = 4
                    except Exception:
                        if lan == 2:
                            control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                        else:
                            control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                else:
                    print("RISK:func_d1 no text")
                    print(cmbd1.get())
                
                #print(cmbd1.get())
                #print(setpage)
                #适配中文：if (cmbd1.get() == "OFF" or "关闭"): 就会产生bug：永远以第一个if设置setpage值，尽管已读取到elif值，原因未知
                
            def speed2():
                pass
            
            def bf():
                pass

            global window_accessibility
            window_accessibility = Toplevel(window_setting)
            window_accessibility.geometry("720x940")
            window_accessibility.resizable(0,0)
            window_accessibility.transient(window_setting)
            window_accessibility.protocol("WM_DELETE_WINDOW", t_close_handler_accessibility)
            window_accessibility.title("设置-辅助功能" if lan == 1 else "Setting-Accessibility")
            window_setting.attributes('-disabled', 1)
            
            label_a = Label(window_accessibility,
                        text='自动运行' if lan == 1 else 'Autorun',
                        font=("Microsoft YaHei UI", 20))
            label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
            label_a_1 = Label(window_accessibility,
                    text="自动运行模式" if lan == 1 else 'Autorun Mode',
                    font=("Microsoft YaHei UI", 10))
            label_a_1.place(relx=0.31, y=10, relwidth=0.3, height=40)
            label_a_1_state = Label(window_accessibility,
                        text='开启该模式后，可以减少外接输入设备的使用' if lan == 1 else 'Enabling this mode reduces the use of\nexternal input devices.',
                        font=("Microsoft YaHei UI", 8))
            label_a_1_state.place(relx=0.31, y=50, relwidth=0.69, height=45) 
            a1 = StringVar()
            cmba1 = Combobox(window_accessibility,values=a1, state='readonly')
            cmba1['value'] = ('ON','OFF')
            cmba1['state'] = DISABLED
            cmba1.current(1)
            cmba1.bind("<<ComboboxSelected>>",func_a1)
            cmba1.place(relx=0.31, y=95, relwidth=0.3, height=40)
            label_a_2 = Label(window_accessibility,
                    text="输出间隔" if lan == 1 else 'Output interval',
                    font=("Microsoft YaHei UI", 10))
            label_a_2.place(relx=0.31, y=135, relwidth=0.3, height=40)
            var7 = IntVar()
            var7.set(5)
            c = Radiobutton(window_accessibility,text="缓慢" if lan == 1 else "Slow",variable = var7 ,value = 8,command=speed2,state=DISABLED)
            c.place(relx=0.31, y=175, relwidth=0.2, height=40)
            c2 = Radiobutton(window_accessibility,text="适中" if lan == 1 else "Normal",variable = var7 ,value = 5,command=speed2,state=DISABLED)
            c2.place(relx=0.31, y=215, relwidth=0.2, height=40)
            c3 = Radiobutton(window_accessibility,text="较快" if lan == 1 else "Fast",variable = var7 ,value = 3,command=speed2,state=DISABLED)
            c3.place(relx=0.31, y=255, relwidth=0.2, height=40)
            

            
            label_b = Label(window_accessibility,
                        text='建议' if lan == 1 else 'Suggest-\nions',
                        font=("Microsoft YaHei UI", 20))
            label_b.place(relx=0.01, y=305, relwidth=0.3, height=150)
            label_b_1 = Label(window_accessibility,
                    text="智慧助手" if lan == 1 else 'Smart Aids',
                    font=("Microsoft YaHei UI", 10))
            label_b_1.place(relx=0.31, y=305, relwidth=0.3, height=40)
            label_b_1_state = Label(window_accessibility,
                        text='开启该功能后，可以提高使用体验' if lan == 1 else 'Enabling this feature improves the\nexperience of using.',
                        font=("Microsoft YaHei UI", 8))
            label_b_1_state.place(relx=0.31, y=345, relwidth=0.69, height=45) 
            b1 = StringVar()
            cmbb1 = Combobox(window_accessibility,values=b1, state='readonly')
            cmbb1['value'] = ('ON','OFF')
            cmbb1['state'] = DISABLED
            cmbb1.current(1)
            cmbb1.bind("<<ComboboxSelected>>",func_b1)
            cmbb1.place(relx=0.31, y=390, relwidth=0.3, height=40)
            
            label_b_2 = Label(window_accessibility,
                    text="智慧感知" if lan == 1 else 'Intelligent Perception',
                    font=("Microsoft YaHei UI", 10))
            label_b_2.place(relx=0.31, y=430, relwidth=0.5, height=40)
            b2 = StringVar()
            cmbb2 = Combobox(window_accessibility,values=b2, state='readonly')
            cmbb2['value'] = ('ON','OFF')
            cmbb2['state'] = DISABLED
            cmbb2.current(1)
            cmbb2.bind("<<ComboboxSelected>>",func_b2)
            cmbb2.place(relx=0.31, y=470, relwidth=0.3, height=40)
            label_b_3 = Label(window_accessibility,
                    text="个性化体验" if lan == 1 else 'Personalized Experience',
                    font=("Microsoft YaHei UI", 10))
            label_b_3.place(relx=0.31, y=510, relwidth=0.5, height=40)
            b3 = StringVar()
            cmbb3 = Combobox(window_accessibility,values=b3, state='readonly')
            cmbb3['value'] = ('ON','OFF')
            cmbb3['state'] = DISABLED
            cmbb3.current(1)
            cmbb3.bind("<<ComboboxSelected>>",func_b3)
            cmbb3.place(relx=0.31, y=550, relwidth=0.3, height=40)
            
            label_c = Label(window_accessibility,
                        text='无障碍' if lan == 1 else 'Barrier\nfree',
                        font=("Microsoft YaHei UI", 20))
            label_c.place(relx=0.01, y=600, relwidth=0.3, height=150)
            label_c_1 = Label(window_accessibility,
                    text="无障碍模式" if lan == 1 else 'Barrier-free Mode',
                    font=("Microsoft YaHei UI", 10))
            label_c_1.place(relx=0.31, y=600, relwidth=0.69, height=40)
            label_c_1_state = Label(window_accessibility,
                    text="该模式启用后会接管部分设置。" if lan == 1 else 'This mode takes over some of the settings\nwhen enabled.',
                    font=("Microsoft YaHei UI", 8))
            label_c_1_state.place(relx=0.31, y=640, relwidth=0.69, height=45)
            bf_mode_button = Button(window_accessibility,
                            text='启用' if lan == 1 else 'Enabled',
                            command=bf,state='disabled')
            bf_mode_button.place(relx=0.31, y=685, relwidth=0.2, height=40)
            
            label_d = Label(window_accessibility,
                        text='高效运行' if lan == 1 else 'Efficient\nOperation',
                        font=("Microsoft YaHei UI", 20))
            label_d.place(relx=0.01, y=750, relwidth=0.3, height=150)
            label_d_1 = Label(window_accessibility,
                    text="快速设置页面" if lan == 1 else 'Quick Settings Page',
                    font=("Microsoft YaHei UI", 10))
            label_d_1.place(relx=0.31, y=750, relwidth=0.69, height=40)
            label_d_1_state = Label(window_accessibility,
                    text=
                    "该设置启用后，“设置”按钮打开的窗口将被所选窗口替代。" if lan == 1 
                    else 'When this setting is enabled, the window opened\nby the Settings button will be replaced by the\nselected window.',
                    font=("Microsoft YaHei UI", 8))
            label_d_1_state.place(relx=0.31, y=790, relwidth=0.69, height=60)
            d1 = StringVar()
            cmbd1 = Combobox(window_accessibility,values=d1, state='readonly')
            cmbd1['value'] = ('OFF','Software UI','Output','Accessibility','Software Notificantion')
            global setpage
            cmbd1.current(setpage)
            cmbd1.bind("<<ComboboxSelected>>",func_d1)
            cmbd1.place(relx=0.31, y=850, relwidth=0.3, height=40)
            
            label_tip2 = Label(window_accessibility,
                    text='关闭窗口以保存设置项' if lan == 1 else 'CLOSE TO SAVE THE SETTINGS',
                    font=("Microsoft YaHei UI", 10))
            label_tip2.pack(side='bottom')
            
        def t_close_handler_notice():
            window_setting.attributes('-disabled', 0)
            window_notice.destroy()
        def notice_command():
            def func2(*args):
                global sound
                sound_path = 'C:\\Random Number Generator\\'
                if (cmb2.get() == "SystemAsterisk"):
                    with open(sound_path+"file3.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('SystemAsterisk')
                        sound = 0

                else:
                    with open(sound_path+"file3.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('OFF')
                        sound = 1
            def func4(*args):
                global sound
                sound_path = 'C:\\Random Number Generator\\'
                if (cmb4.get() == "SystemAsterisk"):
                    with open(sound_path+"file4.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('SystemAsterisk')
                        sound2 = 0

                else:
                    with open(sound_path+"file4.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('OFF')
                        sound2 = 1
            def func5(*args):
                global sound
                sound_path = 'C:\\Random Number Generator\\'
                if (cmb5.get() == "SystemAsterisk"):
                    with open(sound_path+"file5.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('SystemAsterisk')
                        sound3 = 0

                else:
                    with open(sound_path+"file5.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('OFF')
                        sound3 = 1
            
            def funcb1():
                pass

            def funcb2():
                pass

            def funcb3():
                pass
            
            global window_notice
            window_notice = Toplevel(window_setting)
            window_notice.geometry("720x680")
            window_notice.resizable(0,0)
            window_notice.transient(window_setting)
            window_notice.protocol("WM_DELETE_WINDOW", t_close_handler_notice)
            window_notice.title("设置-软件通知" if lan == 1 else "Setting-Software Notificantion")
            window_setting.attributes('-disabled', 1)
        
            label_a = Label(window_notice,
                    text='运行声效' if lan == 1 else 'Running \nSound \nEffect ',
                    font=("Microsoft YaHei UI", 20))
            label_a.place(relx=0.01, y=10, relwidth=0.3, height=150)
            label_a_1 = Label(window_notice,
                    text='启动' if lan == 1 else 'Launch',
                    font=("Microsoft YaHei UI", 10))
            label_a_1.place(relx=0.31, y=10, relwidth=0.15, height=40)
            voice = StringVar()
            cmb2 = Combobox(window_notice,values=voice, state='readonly')
            cmb2['value'] = ('SystemAsterisk','OFF')
            cmb2.current(sound)
            cmb2.bind("<<ComboboxSelected>>",func2)
            cmb2.place(relx=0.31, y=50, relwidth=0.3, height=40) 
            label_a_2 = Label(window_notice,
                    text='开始运行' if lan == 1 else 'Run',
                    font=("Microsoft YaHei UI", 10))
            label_a_2.place(relx=0.31, y=90, relwidth=0.15, height=40)
            voice = StringVar()
            cmb4 = Combobox(window_notice,values=voice, state='readonly')
            cmb4['value'] = ('SystemAsterisk','OFF')
            cmb4.current(sound2)
            cmb4.bind("<<ComboboxSelected>>",func4)
            cmb4.place(relx=0.31, y=130, relwidth=0.3, height=40) 
            label_a_3 = Label(window_notice,
                    text='结束运行' if lan == 1 else 'Stop',
                    font=("Microsoft YaHei UI", 10))
            label_a_3.place(relx=0.31, y=170, relwidth=0.15, height=40)
            voice = StringVar()
            cmb5 = Combobox(window_notice,values=voice, state='readonly')
            cmb5['value'] = ('SystemAsterisk','OFF')
            cmb5.current(sound3)
            cmb5.bind("<<ComboboxSelected>>",func5)
            cmb5.place(relx=0.31, y=210, relwidth=0.3, height=40) 
            
            label_b = Label(window_notice,
                    text='其他通知' if lan == 1 else 'Other \nNotifica-\ntions',
                    font=("Microsoft YaHei UI", 20))
            label_b.place(relx=0.01, y=260, relwidth=0.3, height=150)
            label_b_1 = Label(window_notice,
                    text="更新提示" if lan == 1 else 'Update Tip',
                    font=("Microsoft YaHei UI", 10))
            label_b_1.place(relx=0.31, y=260, relwidth=0.3, height=40)
            b1 = StringVar()
            cmbb1 = Combobox(window_notice,values=b1, state='readonly')
            cmbb1['value'] = ('ON','OFF')
            cmbb1['state'] = DISABLED
            cmbb1.current(1)
            cmbb1.bind("<<ComboboxSelected>>",funcb1)
            cmbb1.place(relx=0.31, y=300, relwidth=0.3, height=40) 
            label_b_2 = Label(window_notice,
                    text="激活提醒" if lan == 1 else 'Activation Alert',
                    font=("Microsoft YaHei UI", 10))
            label_b_2.place(relx=0.31, y=340, relwidth=0.3, height=40)
            b2 = StringVar()
            cmbb2 = Combobox(window_notice,values=b2, state='readonly')
            cmbb2['value'] = ('ON','OFF')
            cmbb2['state'] = DISABLED
            cmbb2.current(1)
            cmbb2.bind("<<ComboboxSelected>>",funcb2)
            cmbb2.place(relx=0.31, y=380, relwidth=0.3, height=40)
            label_b_3 = Label(window_notice,
                    text="启动提醒" if lan == 1 else 'Launch Alert',
                    font=("Microsoft YaHei UI", 10))
            label_b_3.place(relx=0.31, y=420, relwidth=0.3, height=40)
            b3 = StringVar()
            cmbb3 = Combobox(window_notice,values=b3, state='readonly')
            cmbb3['value'] = ('ON','OFF')
            cmbb3['state'] = DISABLED
            cmbb3.current(1)
            cmbb3.bind("<<ComboboxSelected>>",funcb3)
            cmbb3.place(relx=0.31, y=460, relwidth=0.3, height=40)
            label_tip2 = Label(window_notice,
                    text='关闭窗口以保存设置项' if lan == 1 else 'CLOSE TO SAVE THE SETTINGS',
                    font=("Microsoft YaHei UI", 10))
            label_tip2.pack(side='bottom')
            


            
        global window_setting
        window_setting = Toplevel(root)
        window_setting.geometry("720x480")
        window_setting.resizable(0,0)
        window_setting.transient(root)
        window_setting.protocol("WM_DELETE_WINDOW", t_close_handler_setting)
        window_setting.title("设置" if lan == 1 else "Setting")
        root.attributes('-disabled', 1)
        #Unint
        label_b = Label(window_setting,
                    text='设置' if lan == 1 else 'Setting',
                    font=("Microsoft YaHei UI", 18))
        label_b.pack()


        


        
        interface = Button(window_setting,
                        text='软件\n界面' if lan == 1 else 'Software\nUI',
                        command=interface_command)
        interface.place(relx=0.03, y=80, relwidth=0.15, height=130)
        interface_state = Text(window_setting, relief="flat", font=("Microsoft YaHei UI", 10))
        interface_state.place(relx=0.21, y=80, relwidth=0.27, height=130)
        interface_state.insert(INSERT, "显示（语言、标题栏）\n" if lan == 1 else 'Display (Language, Titlebar)\n')
        interface_state.insert(INSERT, "个性化（主题、透明度、透明过渡效果）" if lan == 1 else 'Personalization (Theme, Transparency, TTE)')
        interface_state.configure(state='disabled')
        
        output = Button(window_setting,
                        text='输出' if lan == 1 else 'Output',
                        command=output_command)
        output.place(relx=0.52, y=80, relwidth=0.15, height=130)
        output_state = Text(window_setting, relief="flat", font=("Microsoft YaHei UI", 10))
        output_state.place(relx=0.7, y=80, relwidth=0.27, height=130)
        output_state.insert(INSERT, "数值（类型、数量、范围）\n" if lan == 1 else 'Numeric (Type, Quantity, Range)\n')
        output_state.insert(INSERT, "输出（间隔）" if lan == 1 else 'Output (Interval)')
        output_state.configure(state='disabled')
        
        accessibility = Button(window_setting,
                        text='辅助\n功能' if lan == 1 else 'Accessib-\nility',
                        command=accessibility_command)
        accessibility.place(relx=0.03, y=270, relwidth=0.15, height=130)
        accessibility_state = Text(window_setting, relief="flat", font=("Microsoft YaHei UI", 10))
        accessibility_state.place(relx=0.21, y=270, relwidth=0.27, height=130)
        accessibility_state.insert(INSERT, "自动运行\n" if lan == 1 else 'Autorun\n')
        accessibility_state.insert(INSERT, "建议（智慧助手）\n" if lan == 1 else 'Suggestions (Smart Aids)\n')
        accessibility_state.insert(INSERT, "无障碍\n" if lan == 1 else 'Barrier-free\n')
        accessibility_state.insert(INSERT, "高效运行" if lan == 1 else 'Efficient Operation')
        accessibility_state.configure(state='disabled')
        
        notice = Button(window_setting,
                        text='软件\n通知' if lan == 1 else 'Software\nNotifica-\ntion',
                        command=notice_command)
        notice.place(relx=0.52, y=270, relwidth=0.15, height=130)
        notice_state = Text(window_setting, relief="flat", font=("Microsoft YaHei UI", 10))
        notice_state.place(relx=0.7, y=270, relwidth=0.27, height=130)
        notice_state.insert(INSERT, "运行声效（启动、开始运行、结束运行）\n" if lan == 1 else 'Running Sound Effect (Launch, Run, Stop)\n')
        notice_state.insert(INSERT, "其他通知（更新提示）" if lan == 1 else 'Other Notifications(Update Tips)')
        notice_state.configure(state='disabled')
        
        label_tip1 = Label(window_setting,
                    text='点击按钮进入对应设置' if lan == 1 else 'CLICK THE BUTTON TO ENTER THE CORRESPONDING SETTINGS',
                    font=("Microsoft YaHei UI", 10))
        label_tip1.pack(side='bottom')
    
    if setpage == 1:
        def func(*args):
            global lan
            if (cmb.get() == "简体中文（中国大陆）"):
                try:
                    with open(languageset_path+"file.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('Chinese Simplified')
                    lan = 1
                    state['state'] = NORMAL
                    state.delete('0.0', END)
                    state.insert(INSERT, "语言已切换至'简体中文（中国大陆）' \n")
                    state.insert(INSERT, "程序需要重启以完成该更改")
                    state['state'] = DISABLED
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")

            else:
                try:
                    with open(languageset_path+"file.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('American English')

                    lan = 2
                    state['state'] = NORMAL
                    state.delete('0.0', END)
                    state.insert(INSERT, "Language switched to 'English(United States)' \n")
                    state.insert(INSERT, "The program needs to be restarted to complete the change")
                    state['state'] = DISABLED

                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")                       
        def funk(*args):
            global themes
            if (cmd.get() == "Classical"):
                try:
                    with open(themeset_path+"file2.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('Classical')
                    themes = 1
                    state['state'] = NORMAL
                    state.delete('0.0', END)
                    state.insert(INSERT, "Theme switched to 'Classical' \n")
                    state.insert(INSERT, "The program needs to be restarted to complete the change")
                    state['state'] = DISABLED
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            else:
                try:
                    with open(themeset_path+"file2.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('Adapta')
                    themes = 2
                    state['state'] = NORMAL
                    state.delete('0.0', END)
                    state.insert(INSERT, "Theme switched to 'Adapta' \n")
                    state.insert(INSERT, "The program needs to be restarted to complete the change")
                    state['state'] = DISABLED
                except Exception:
                    if themes == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
        def apply():
            global alpha
            alpha = scale.get()
            alpha2 = alpha / 100
            root.attributes('-alpha',alpha2)
            tr_state.configure(state='normal')
            tr_state.delete('0.0', END)
            tr_state.insert(INSERT, f"{str(round(scale.get(),2))}")
            tr_state.configure(state='disabled')
        
        def ch():
            global tit
            tit = var_title.get()
            if tit == 1:
                root.title("Random Number Generator")
            if tit == 2:
                root.title("Random Number Generator 4")
            if tit == 3:
                root.title("Random Number Generator HARMONY")
        
        def func3():
            pass
        
        def dis():
            try:
                with open(setpage_path+"file6.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('0')
                setpage = 0
                control_ = showerror(title='Program Info',message="Please restart the software.\n")
                control['state'] = DISABLED
            except Exception:
                if lan == 2:
                    control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                else:
                    control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                    
        global window_interface
        window_interface = Toplevel(root)
        window_interface.geometry("720x680")
        window_interface.resizable(0,0)
        window_interface.transient(root)
        window_interface.title("设置-软件界面" if lan == 1 else "Setting-Software UI")      
        label_a = Label(window_interface,
                text='显示' if lan == 1 else 'Display',
                font=("Microsoft YaHei UI", 20))
        label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
        
        
        label_a_1 = Label(window_interface,
                text='语言' if lan == 1 else 'Language',
                font=("Microsoft YaHei UI", 10))
        label_a_1.place(relx=0.31, y=10, relwidth=0.15, height=40)
        label_a_1_state = Label(window_interface,
                text='软件将使用此语言显示。' if lan == 1 else 'The software will display in this language.',
                font=("Microsoft YaHei UI", 8))
        label_a_1_state.place(relx=0.31, y=50, relwidth=0.69, height=25)
        mode = StringVar()
        cmb = Combobox(window_interface,values=mode, state='readonly')
        cmb['value'] = ('简体中文（中国大陆）','English(United States)')
        cmb.current(lan-1)
        cmb.bind("<<ComboboxSelected>>",func)
        cmb.place(relx=0.31, y=75, relwidth=0.31, height=40)
        
        label_a_2 = Label(window_interface,
                text='标题栏' if lan == 1 else 'Titlebar',
                font=("Microsoft YaHei UI", 10))
        label_a_2.place(relx=0.31, y=115, relwidth=0.15, height=40)
        label_a_2_state = Label(window_interface,
                text='主窗口标题栏将使用该配置显示。' if lan == 1 else 'The main window title bar will be displayed \nusing this configuration.',
                font=("Microsoft YaHei UI", 8))
        label_a_2_state.place(relx=0.31, y=155, relwidth=0.69, height=45)
        var_title = IntVar()
        var_title.set(tit)
        b = Radiobutton(window_interface,text="软件名" if lan == 1 else 'Software name',variable = var_title ,value =1,command=ch)
        b.place(relx=0.31, y=200, relwidth=0.23, height=40)
        b2 = Radiobutton(window_interface,text="软件名+主版本号" if lan == 1 else 'Software Name + Major Version',variable = var_title ,value =2,command=ch)
        b2.place(relx=0.31, y=240, relwidth=0.46, height=40)
        b3 = Radiobutton(window_interface,text="软件名+宣传词" if lan == 1 else 'Software Name + Promotional Message',variable = var_title ,value =3,command=ch)
        b3.place(relx=0.31, y=280, relwidth=0.52, height=40)
        
        label_b = Label(window_interface,
                    text='个性化' if lan == 1 else 'Personali-\nzation',
                    font=("Microsoft YaHei UI", 20))
        label_b.place(relx=0.01, y=340, relwidth=0.3, height=140) 
        
        label_b_1 = Label(window_interface,
                    text='主题' if lan == 1 else 'Theme',
                    font=("Microsoft YaHei UI", 10))
        label_b_1.place(relx=0.31, y=340, relwidth=0.1, height=40) 
        label_b_1_state = Label(window_interface,
                    text='选择不同风格的主题使软件富有个性' if lan == 1 else 'Choose from a variety of themes to \npersonalize your software.',
                    font=("Microsoft YaHei UI", 8))
        label_b_1_state.place(relx=0.31, y=380, relwidth=0.69, height=45) 
        theme = StringVar()
        cmd = Combobox(window_interface,values=theme, state='readonly')
        cmd.place(relx=0.31, y=425, relwidth=0.31, height=40)
        cmd['value'] = ('Classical','Adapta')
        cmd.current(themes-1)
        cmd.bind("<<ComboboxSelected>>",funk)
        label_b_2 = Label(window_interface,
                    text='不透明度' if lan == 1 else 'Opacity',
                    font=("Microsoft YaHei UI", 10))
        label_b_2.place(relx=0.31, y=465, relwidth=0.2, height=40) 
        tr_apply = Button(window_interface,
                    text='应用'if lan == 1 else "APPLY",
                    command=apply)
        tr_apply.place(relx=0.51, y=465, relwidth=0.2, height=40)
        scale = Scale(window_interface, from_=10, to_=100,orient=HORIZONTAL,length=220)
        scale.set(alpha)
        scale.place(relx=0.31, y=515, relwidth=0.49, height=20) 
        tr_state = Text(window_interface, relief="flat", font=("Microsoft YaHei UI", 10))
        tr_state.place(relx=0.82, y=505, relwidth=0.12, height=40)
        tr_state.insert(INSERT, f"{str(round(scale.get(),2))}")
        tr_state.configure(state='disabled')
        label_b_3 = Label(window_interface,
                    text='透明过渡效果' if lan == 1 else 'Transparent Transition Effect',
                    font=("Microsoft YaHei UI", 10))
        label_b_3.place(relx=0.31, y=545, relwidth=0.6, height=40) 
        tte = StringVar()
        cmb3 = Combobox(window_interface,values=tte, state='readonly')
        cmb3['value'] = ('ON','OFF')
        cmb3['state'] = DISABLED
        cmb3.current(0)
        cmb3.bind("<<ComboboxSelected>>",func3)
        cmb3.place(relx=0.31, y=585, relwidth=0.3, height=40) 
        
        control = Button(window_interface, text ="禁用“快速设置页面”" if lan == 1 else "Disabled 'Quick Settings Page'", command = dis)
        control.pack(side='bottom')
    if setpage == 2:
        def chosen():
            global numset
            global turn
            numset = var.get()
            if numset in [1, 3, 4]:
                var5.set(1)
                label_t.place_forget()
                bt.place_forget()
                bt2.place_forget()
                turn = 1
            else:
                if outputset == 1:
                    turn = 2
                    label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
                    bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
                    bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)

        def chosen2():
            global outputset
            outputset = var3.get()
            if outputset == 1:      
                state_4.place(relx=0.2, y=225, relwidth=0.6, height=220)
                state_1.place_forget()
                state_2.place_forget()
                state_3.place_forget()
                state_5.place_forget()
                state_6.place_forget()
                state_7.place_forget()
                state_8.place_forget()
                state_9.place_forget()
                state_0.place_forget()
                state_x.place_forget()
                state_x2.place_forget()
                label_b.place_forget()
                bx.place_forget()
                bx2.place_forget()
                bx3.place_forget()
                var4.set(1)

                if numset == 2:
                    label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
                    bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
                    bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)
                else:
                    var5.set(1)
                    label_t.place_forget()
                    bt.place_forget()
                    bt2.place_forget()
            if outputset == 2:
                state_5.place(relx=0.05, y=225, relwidth=0.4, height=220)
                state_6.place(relx=0.55, y=225, relwidth=0.4, height=220)
                state_1.place_forget()
                state_2.place_forget()
                state_3.place_forget()
                state_4.place_forget()
                state_7.place_forget()
                state_8.place_forget()
                state_9.place_forget()
                state_0.place_forget()
                var5.set(1)
                label_t.place_forget()
                bt.place_forget()
                bt2.place_forget()


                label_b.place(relx=0.31, y=360, relwidth=0.18, height=40)
                bx.place(relx=0.31, y=400, relwidth=0.14, height=40)
                bx2.place(relx=0.45, y=400, relwidth=0.14, height=40)
                bx3.place(relx=0.59, y=400, relwidth=0.14, height=40)
            if outputset == 3:
                state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
                state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
                state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
                state_4.place_forget()
                state_5.place_forget()
                state_6.place_forget()
                state_7.place_forget()
                state_8.place_forget()
                state_9.place_forget()
                state_0.place_forget()
                state_x.place_forget()
                state_x2.place_forget()
                label_b.place_forget()
                bx.place_forget()
                bx2.place_forget()
                bx3.place_forget()
                var4.set(1)
                var5.set(1)
                label_t.place_forget()
                bt.place_forget()
                bt2.place_forget()

            if outputset == 4:
                state_7.place(relx=0.01, y=225, relwidth=0.23, height=220)
                state_8.place(relx=0.26, y=225, relwidth=0.23, height=220)
                state_9.place(relx=0.51, y=225, relwidth=0.23, height=220)
                state_0.place(relx=0.76, y=225, relwidth=0.23, height=220)
                state_1.place_forget()
                state_2.place_forget()
                state_3.place_forget()
                state_4.place_forget()
                state_5.place_forget()
                state_6.place_forget()
                state_x.place_forget()
                state_x2.place_forget()
                label_b.place_forget()
                bx.place_forget()
                bx2.place_forget()
                bx3.place_forget()
                var4.set(1)
                var5.set(1)
                label_t.place_forget()
                bt.place_forget()
                bt2.place_forget()


        def chosen3():
            get = var4.get()
            global got
            if get == 1:
                state_x.place_forget()
                state_x2.place_forget()

                got = 1
            if get == 2:
                state_x.place_forget()
                state_x2.place(relx=0.45, y=225, relwidth=0.1, height=220)

                got = 2
            if get == 3:
                state_x2.place_forget()
                state_x.place(relx=0.45, y=225, relwidth=0.1, height=220)

                got = 3

        def chosen4():
            got2 = var5.get()
            global turn    
            if got2 == 1:
                turn = 1
            if got2 == 2:
                turn = 2


        def application():
            global f
            global e
            global numset
            try:

                f = float(label_a_3.get())
                e = float(label_a_4.get())

                    #####
                if f >= e:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（前一个控件的值不能大于或等于后一个控件的值）\n建议更改后再次检查设置\n" if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the value of the previous control cannot be greater than or equal to the value of the latter control)\nIt is recommended to check the setting again after changing\n")
                    control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                    f = 1
                    e = 51
                    label_a_3.delete(0, "end")
                    label_a_3.insert(0, f)
                    label_a_4.delete(0, "end")
                    label_a_4.insert(0, e)
                if numset == 1:
                    control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")

                if numset == 2:
                    if f <= 0 or e <= 0 or f % 1 != 0 or e % 1 != 0 or f <= 0.0 or e <= 0.0 or f % 1 != 0.0 or e % 1 != 0.0:
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n"if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the values of both controls must be a positive integer)\nIt is recommended to check the settings again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1
                        e = 51
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)
                    else:
                        f = int(label_a_3.get())
                        e = int(label_a_4.get())
                        control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")
                if numset == 3:
                    if f % 1 != 0 or e % 1 != 0 or f % 1 != 0.0 or e % 1 != 0.0:
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the values of both controls must be an integer)\nIt is recommended to check the settings again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1
                        e = 51
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)
                    else:
                        f = int(label_a_3.get())
                        e = int(label_a_4.get())
                        control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")
                if numset == 4:
                    s=str(f).split('.')
                    s1=str(e).split('.')
                    if float(s[1])==0 or float(s1[1])==0:
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件必须是一个小数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values at:\n• Build Settings - Range (both controls must be a decimal)\nIt is recommended to check the settings again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1.5
                        e = 51.5
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)
                    else:
                        control_info = showinfo(title='Program Info',message="没有发现已知错误。\n程序经过检查，认为你可以正常使用Random Number Generator!\n" if lan == 1 else"No known bugs were found. \nThe program checked and thought you could use Random Number Generator normally!\n")

            except Exception:
                f = str(label_a_3.get())
                e = str(label_a_4.get())

                if not f or not e:
                    control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个输入框不能为空，请填写符合您配置的值）。\n建议更改后再次检查设置\n"if lan == 1 else"There is a problem with the program, so Check Settings cannot be run. \nAfter preliminary judgment, the program believes that the cause of the error may be caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the two input fields cannot be empty, please fill in the values that match your configuration). \nIt is recommended to check the settings again after changing\n")
                    control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                    f = 1
                    e = 51
                    label_a_3.delete(0, "end")
                    label_a_3.insert(0, f)
                    label_a_4.delete(0, "end")
                    label_a_4.insert(0, e)
                else:
                    s=str(f).split('.')
                    s1=str(e).split('.')
                    try:
                        if float(s[1])==0 or float(s1[1])==0:
                            if numset == 2:
                                control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n"if lan == 1 else "There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the values of both controls must be a positive integer)\nIt is recommended to check the settings again after changing\n")
                                control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                                f = 1
                                e = 51
                                label_a_3.delete(0, "end")
                                label_a_3.insert(0, f)
                                label_a_4.delete(0, "end")
                                label_a_4.insert(0, e)

                            if numset == 3:                    
                                control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n" if lan == 1 else"There was a problem with the program, so the setting could not be enabled. \nAfter checking, the program found that the cause of the error was caused by your improper settings. \nPlease check the values in the following locations:\n• Build Settings - Range (the values of both controls must be an integer)\nIt is recommended to check the settings again after changing\n")
                                control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                                f = 1
                                e = 51
                                label_a_3.delete(0, "end")
                                label_a_3.insert(0, f)
                                label_a_4.delete(0, "end")
                                label_a_4.insert(0, e)
                    except Exception:
                        control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  生成设置 - 范围（输入的值必须是一个有理数）。\n建议更改后再次检查设置\n" if lan == 1 else "There is a problem with the program, so Check Settings cannot be run. \nAfter preliminary judgment, the program believes that the cause of the error may be caused by your improper settings. \nPlease check the values for:\n• Build Settings - Range (the value entered must be a rational number). \nIt is recommended to check the settings again after changing\n")
                        control_info = showwarning(title='Program Warning',message="鉴于你的不当设置，为避免程序运行出错，程序已自动恢复默认设置！\n" if lan == 1 else "In view of your improper settings, the program has automatically restored the default settings to avoid running errors!\n")
                        f = 1
                        e = 51
                        label_a_3.delete(0, "end")
                        label_a_3.insert(0, f)
                        label_a_4.delete(0, "end")
                        label_a_4.insert(0, e)

        def eventhandler(event):
            label_a_3.focus()
        def eventhandler2(event):
            label_a_4.focus()
        def speed():
            global showspeed
            showspeed = var6.get()
            
            
        def dis():
            try:
                with open(setpage_path+"file6.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('0')
                setpage = 0
                control_ = showerror(title='Program Info',message="Please restart the software.\n")
                control['state'] = DISABLED
            except Exception:
                if lan == 2:
                    control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                else:
                    control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                    
        global showspeed
        global window_output
        window_output = Toplevel(root)
        window_output.geometry("720x680")
        window_output.resizable(0,0)
        window_output.transient(root)
        window_output.title("设置-输出" if lan == 1 else "Setting-Output")
        
        label_a = Label(window_output,
                    text='数值' if lan == 1 else 'Numeric',
                    font=("Microsoft YaHei UI", 20))
        label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
        
        label_a_1 = Label(window_output,
                    text='类型' if lan == 1 else 'Type',
                    font=("Microsoft YaHei UI", 10))
        label_a_1.place(relx=0.31, y=10, relwidth=0.3, height=40)

        var = IntVar()
        var.set(numset)
        b = Radiobutton(window_output,text="有理数" if lan == 1 else 'Rational Number',variable = var ,value =1,command=chosen)
        b.place(relx=0.31, y=50, relwidth=0.3, height=40)
        b2 = Radiobutton(window_output,text="正整数" if lan == 1 else 'Positive Integer',variable = var ,value =2,command=chosen)
        b2.place(relx=0.31, y=90, relwidth=0.3, height=40)
        b3 = Radiobutton(window_output,text="整数" if lan == 1 else 'Integer',variable = var ,value =3,command=chosen)
        b3.place(relx=0.31, y=130, relwidth=0.2, height=40)
        b4 = Radiobutton(window_output,text="小数" if lan == 1 else 'Decimal',variable = var ,value =4,command=chosen)
        b4.place(relx=0.31, y=170, relwidth=0.2, height=40) 

        label_a_2 = Label(window_output,
                    text='范围' if lan == 1 else 'Range',
                    font=("Microsoft YaHei UI", 10))
        label_a_2.place(relx=0.31, y=210, relwidth=0.1, height=40)

        label_a_3 = Entry(window_output, font=("Microsoft YaHei UI", 10),background='gray')
        label_a_3.place(relx=0.31, y=250, relwidth=0.15, height=40)
        label_a_5 = Label(window_output,text = '-', font=("Microsoft YaHei UI", 10))
        label_a_5.place(relx=0.46, y=260, relwidth=0.02, height=30)
        label_a_4 = Entry(window_output, font=("Microsoft YaHei UI", 10),background='gray')
        label_a_4.place(relx=0.48, y=250, relwidth=0.15, height=40)
        label_a_3.bind_all('<Control-q>', eventhandler)
        label_a_4.bind_all('<Control-w>', eventhandler2)
        application = Button(window_output,
                        text='应用设置' if lan == 1 else 'APPLY',
                        command=application)

        application.place(relx=0.7, y=250, relwidth=0.2, height=40)

        def show_message(event):
            label['text'] = "使用Ctrl+q和Ctrl+w以便更快聚焦输入框" if lan == 1 else "Using Ctrl+q and Ctrl+w"

        def hide_message(event):
            label['text'] = "❔[获取提示]" if lan == 1 else "[Tip]"

        label = Label(window_output, text="❔[获取提示]" if lan == 1 else "[Tip]")
        label.place(relx=0.41, y=210, relwidth=0.71, height=40)
        label.bind("<Enter>", show_message)
        label.bind("<Leave>", hide_message)

        label_a_3.delete(0, "end")
        label_a_3.insert(0, f)
        label_a_4.delete(0, "end")
        label_a_4.insert(0, e)
        label_b_2 = Label(window_output,
                    text='数量' if lan == 1 else 'Quantity',
                    font=("Microsoft YaHei UI", 10))
        label_b_2.place(relx=0.31, y=290, relwidth=0.4, height=30)
        var3 = IntVar()
        var3.set(outputset)
        b = Radiobutton(window_output,text="1",variable = var3 ,value =1,command=chosen2)
        b.place(relx=0.31, y=320, relwidth=0.1, height=40)
        b2 = Radiobutton(window_output,text="2",variable = var3 ,value =2,command=chosen2)
        b2.place(relx=0.41, y=320, relwidth=0.1, height=40)
        b3 = Radiobutton(window_output,text="3",variable = var3 ,value =3,command=chosen2)
        b3.place(relx=0.51, y=320, relwidth=0.1, height=40)
        b4 = Radiobutton(window_output,text="4",variable = var3 ,value =4,command=chosen2)
        b4.place(relx=0.61, y=320, relwidth=0.1, height=40) 

        label_b = Label(window_output,
                    text='显示配对符号'if lan == 1 else"Pairing Symbol",
                    font=("Microsoft YaHei UI", 8))
        label_b.place(relx=0.31, y=360, relwidth=0.18, height=40)



        var4 = IntVar()
        var4.set(got)
        bx = Radiobutton(window_output,text="关闭"if lan == 1 else"OFF",variable = var4 ,value =1,command=chosen3)
        bx.place(relx=0.31, y=400, relwidth=0.14, height=40)
        bx2 = Radiobutton(window_output,text="显示'+'" if lan == 1 else "Show'+'",variable = var4 ,value =2,command=chosen3)
        bx2.place(relx=0.45, y=400, relwidth=0.14, height=40)
        bx3 = Radiobutton(window_output,text="显示'×'" if lan == 1 else "Show'×'",variable = var4 ,value =3,command=chosen3)
        bx3.place(relx=0.59, y=400, relwidth=0.14, height=40)

        if outputset != 2:
            var4.set(1)
            label_b.place_forget()
            bx.place_forget()
            bx2.place_forget()
            bx3.place_forget()



        label_t = Label(window_output,
                    text='以轮播替代随机'if lan == 1 else"Sequential Playback",
                    font=("Microsoft YaHei UI", 8))
        label_t.place(relx=0.31, y=360, relwidth=0.4, height=40)
        var5 = IntVar()
        var5.set(turn)
        bt = Radiobutton(window_output,text="关闭" if lan == 1 else 'OFF',variable = var5 ,value =1,command=chosen4)
        bt.place(relx=0.31, y=400, relwidth=0.12, height=40)
        bt2 = Radiobutton(window_output,text="启用" if lan == 1 else 'ON',variable = var5 ,value =2,command=chosen4)
        bt2.place(relx=0.43, y=400, relwidth=0.14, height=40)
        if outputset != 1 or numset != 2:
            var5.set(1)
            label_t.place_forget()
            bt.place_forget()
            bt2.place_forget()

        
        
        
        label_c = Label(window_output,
            text='输出' if lan == 1 else 'Output',
            font=("Microsoft YaHei UI", 20))
        label_c.place(relx=0.01, y=450, relwidth=0.3, height=90)
        label_c_1 = Label(window_output,
            text='间隔' if lan == 1 else 'Interval',
            font=("Microsoft YaHei UI", 10))
        label_c_1.place(relx=0.31, y=450, relwidth=0.3, height=40)
        var6 = IntVar()
        var6.set(showspeed)
        c = Radiobutton(window_output,text="缓慢" if lan == 1 else "Slow",variable = var6 ,value = 30,command=speed)
        c.place(relx=0.31, y=490, relwidth=0.2, height=40)
        c2 = Radiobutton(window_output,text="适中" if lan == 1 else "Normal",variable = var6 ,value = 10,command=speed)
        c2.place(relx=0.31, y=530, relwidth=0.2, height=40)
        c3 = Radiobutton(window_output,text="较快" if lan == 1 else "Fast",variable = var6 ,value = 6,command=speed)
        c3.place(relx=0.31, y=570, relwidth=0.2, height=40)
        c4 = Radiobutton(window_output,text="非常快" if lan == 1 else "Very Fast",variable = var6 ,value = 2,command=speed)
        c4.place(relx=0.31, y=610, relwidth=0.24, height=40) 
        
        control = Button(window_output, text ="禁用“快速设置页面”" if lan == 1 else "Disabled 'Quick Settings Page'", command = dis)
        control.pack(side='bottom')
        
    if setpage == 3:
        def func_a1():
            pass
        
        def func_b1():
            pass
        
        def func_b2():
            pass
        
        def func_b3():
            pass
        
        def func_d1(*args):
            global setpage
            if (cmbd1.get() == "OFF"):
                try:
                    with open(setpage_path+"file6.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('0')
                    setpage = 0
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            elif (cmbd1.get() == "Software UI"):
                try:
                    with open(setpage_path+"file6.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('1')
                    setpage = 1
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            elif (cmbd1.get() == "Output"):
                try:
                    with open(setpage_path+"file6.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('2')
                    setpage = 2
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            elif (cmbd1.get() == "Accessibility"):
                try:
                    with open(setpage_path+"file6.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('3')
                    setpage = 3
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            elif (cmbd1.get() == "Software Notificantion"):
                try:
                    with open(setpage_path+"file6.txt","r+") as d:
                        d.read()
                        d.seek(0)
                        d.truncate()
                        d.write('4')
                    setpage = 4
                except Exception:
                    if lan == 2:
                        control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                    else:
                        control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
            else:
                print("RISK:func_d1 no text")
                print(cmbd1.get())
            
            #print(cmbd1.get())
            #print(setpage)
            #适配中文：if (cmbd1.get() == "OFF" or "关闭"): 就会产生bug：永远以第一个if设置setpage值，尽管已读取到elif值，原因未知
            
        def speed2():
            pass
        
        def bf():
            pass

        def dis():
            try:
                with open(setpage_path+"file6.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('0')
                setpage = 0
                control_ = showerror(title='Program Info',message="Please restart the software.\n")
                control['state'] = DISABLED
            except Exception:
                if lan == 2:
                    control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                else:
                    control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                    
        global window_accessibility
        window_accessibility = Toplevel(root)
        window_accessibility.geometry("720x940")
        window_accessibility.resizable(0,0)
        window_accessibility.transient(root)
        window_accessibility.title("设置-辅助功能" if lan == 1 else "Setting-Accessibility")
        
        label_a = Label(window_accessibility,
                    text='自动运行' if lan == 1 else 'Autorun',
                    font=("Microsoft YaHei UI", 20))
        label_a.place(relx=0.01, y=10, relwidth=0.3, height=90)
        label_a_1 = Label(window_accessibility,
                   text="自动运行模式" if lan == 1 else 'Autorun Mode',
                   font=("Microsoft YaHei UI", 10))
        label_a_1.place(relx=0.31, y=10, relwidth=0.3, height=40)
        label_a_1_state = Label(window_accessibility,
                    text='开启该模式后，可以减少外接输入设备的使用' if lan == 1 else 'Enabling this mode reduces the use of\nexternal input devices.',
                    font=("Microsoft YaHei UI", 8))
        label_a_1_state.place(relx=0.31, y=50, relwidth=0.69, height=45) 
        a1 = StringVar()
        cmba1 = Combobox(window_accessibility,values=a1, state='readonly')
        cmba1['value'] = ('ON','OFF')
        cmba1['state'] = DISABLED
        cmba1.current(1)
        cmba1.bind("<<ComboboxSelected>>",func_a1)
        cmba1.place(relx=0.31, y=95, relwidth=0.3, height=40)
        label_a_2 = Label(window_accessibility,
                   text="输出间隔" if lan == 1 else 'Output interval',
                   font=("Microsoft YaHei UI", 10))
        label_a_2.place(relx=0.31, y=135, relwidth=0.3, height=40)
        var7 = IntVar()
        var7.set(5)
        c = Radiobutton(window_accessibility,text="缓慢" if lan == 1 else "Slow",variable = var7 ,value = 8,command=speed2,state=DISABLED)
        c.place(relx=0.31, y=175, relwidth=0.2, height=40)
        c2 = Radiobutton(window_accessibility,text="适中" if lan == 1 else "Normal",variable = var7 ,value = 5,command=speed2,state=DISABLED)
        c2.place(relx=0.31, y=215, relwidth=0.2, height=40)
        c3 = Radiobutton(window_accessibility,text="较快" if lan == 1 else "Fast",variable = var7 ,value = 3,command=speed2,state=DISABLED)
        c3.place(relx=0.31, y=255, relwidth=0.2, height=40)
        

        
        label_b = Label(window_accessibility,
                    text='建议' if lan == 1 else 'Suggest-\nions',
                    font=("Microsoft YaHei UI", 20))
        label_b.place(relx=0.01, y=305, relwidth=0.3, height=150)
        label_b_1 = Label(window_accessibility,
                   text="智慧助手" if lan == 1 else 'Smart Aids',
                   font=("Microsoft YaHei UI", 10))
        label_b_1.place(relx=0.31, y=305, relwidth=0.3, height=40)
        label_b_1_state = Label(window_accessibility,
                    text='开启该功能后，可以提高使用体验' if lan == 1 else 'Enabling this feature improves the\nexperience of using.',
                    font=("Microsoft YaHei UI", 8))
        label_b_1_state.place(relx=0.31, y=345, relwidth=0.69, height=45) 
        b1 = StringVar()
        cmbb1 = Combobox(window_accessibility,values=b1, state='readonly')
        cmbb1['value'] = ('ON','OFF')
        cmbb1['state'] = DISABLED
        cmbb1.current(1)
        cmbb1.bind("<<ComboboxSelected>>",func_b1)
        cmbb1.place(relx=0.31, y=390, relwidth=0.3, height=40)
        
        label_b_2 = Label(window_accessibility,
                   text="智慧感知" if lan == 1 else 'Intelligent Perception',
                   font=("Microsoft YaHei UI", 10))
        label_b_2.place(relx=0.31, y=430, relwidth=0.5, height=40)
        b2 = StringVar()
        cmbb2 = Combobox(window_accessibility,values=b2, state='readonly')
        cmbb2['value'] = ('ON','OFF')
        cmbb2['state'] = DISABLED
        cmbb2.current(1)
        cmbb2.bind("<<ComboboxSelected>>",func_b2)
        cmbb2.place(relx=0.31, y=470, relwidth=0.3, height=40)
        label_b_3 = Label(window_accessibility,
                   text="个性化体验" if lan == 1 else 'Personalized Experience',
                   font=("Microsoft YaHei UI", 10))
        label_b_3.place(relx=0.31, y=510, relwidth=0.5, height=40)
        b3 = StringVar()
        cmbb3 = Combobox(window_accessibility,values=b3, state='readonly')
        cmbb3['value'] = ('ON','OFF')
        cmbb3['state'] = DISABLED
        cmbb3.current(1)
        cmbb3.bind("<<ComboboxSelected>>",func_b3)
        cmbb3.place(relx=0.31, y=550, relwidth=0.3, height=40)
        
        label_c = Label(window_accessibility,
                    text='无障碍' if lan == 1 else 'Barrier\nfree',
                    font=("Microsoft YaHei UI", 20))
        label_c.place(relx=0.01, y=600, relwidth=0.3, height=150)
        label_c_1 = Label(window_accessibility,
                   text="无障碍模式" if lan == 1 else 'Barrier-free Mode',
                   font=("Microsoft YaHei UI", 10))
        label_c_1.place(relx=0.31, y=600, relwidth=0.69, height=40)
        label_c_1_state = Label(window_accessibility,
                   text="该模式启用后会接管部分设置。" if lan == 1 else 'This mode takes over some of the settings\nwhen enabled.',
                   font=("Microsoft YaHei UI", 8))
        label_c_1_state.place(relx=0.31, y=640, relwidth=0.69, height=45)
        bf_mode_button = Button(window_accessibility,
                        text='启用' if lan == 1 else 'Enabled',
                        command=bf,state='disabled')
        bf_mode_button.place(relx=0.31, y=685, relwidth=0.2, height=40)
        
        label_d = Label(window_accessibility,
                    text='高效运行' if lan == 1 else 'Efficient\nOperation',
                    font=("Microsoft YaHei UI", 20))
        label_d.place(relx=0.01, y=750, relwidth=0.3, height=150)
        label_d_1 = Label(window_accessibility,
                   text="快速设置页面" if lan == 1 else 'Quick Settings Page',
                   font=("Microsoft YaHei UI", 10))
        label_d_1.place(relx=0.31, y=750, relwidth=0.69, height=40)
        label_d_1_state = Label(window_accessibility,
                   text=
                   "该设置启用后，“设置”按钮打开的窗口将被所选窗口替代。" if lan == 1 
                   else 'When this setting is enabled, the window opened\nby the Settings button will be replaced by the\nselected window.',
                   font=("Microsoft YaHei UI", 8))
        label_d_1_state.place(relx=0.31, y=790, relwidth=0.69, height=60)
        d1 = StringVar()
        cmbd1 = Combobox(window_accessibility,values=d1, state='readonly')
        cmbd1['value'] = ('OFF','Software UI','Output','Accessibility','Software Notificantion')
        cmbd1.current(setpage)
        cmbd1.bind("<<ComboboxSelected>>",func_d1)
        cmbd1.place(relx=0.31, y=850, relwidth=0.3, height=40)
        
        
        control = Button(window_accessibility, text ="禁用“快速设置页面”" if lan == 1 else "Disabled 'Quick Settings Page'", command = dis)
        control.pack(side='bottom')
    if setpage == 4:
        def func2(*args):
            global sound
            sound_path = 'C:\\Random Number Generator\\'
            if (cmb2.get() == "SystemAsterisk"):
                with open(sound_path+"file3.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('SystemAsterisk')
                    sound = 0

            else:
                with open(sound_path+"file3.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('OFF')
                    sound = 1
        def func4(*args):
            global sound
            sound_path = 'C:\\Random Number Generator\\'
            if (cmb4.get() == "SystemAsterisk"):
                with open(sound_path+"file4.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('SystemAsterisk')
                    sound2 = 0

            else:
                with open(sound_path+"file4.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('OFF')
                    sound2 = 1
        def func5(*args):
            global sound
            sound_path = 'C:\\Random Number Generator\\'
            if (cmb5.get() == "SystemAsterisk"):
                with open(sound_path+"file5.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('SystemAsterisk')
                    sound3 = 0

            else:
                with open(sound_path+"file5.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('OFF')
                    sound3 = 1
        
        def funcb1():
            pass

        def funcb2():
            pass

        def funcb3():
            pass
        
        def dis():
            try:
                with open(setpage_path+"file6.txt","r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('0')
                setpage = 0
                control_ = showerror(title='Program Info',message="Please restart the software.\n")
                control['state'] = DISABLED
            except Exception:
                if lan == 2:
                    control_ = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue!\n")
                else:
                    control_ = showerror(title='Program Error',message="未知错误！请前往我们的'Github - Issue'一栏中反馈该问题!\n")
                    
        global window_notice
        window_notice = Toplevel(root)
        window_notice.geometry("720x680")
        window_notice.resizable(0,0)
        window_notice.transient(root)
        window_notice.title("设置-软件通知" if lan == 1 else "Setting-Software Notificantion")
    
        label_a = Label(window_notice,
                   text='运行声效' if lan == 1 else 'Running \nSound \nEffect ',
                   font=("Microsoft YaHei UI", 20))
        label_a.place(relx=0.01, y=10, relwidth=0.3, height=150)
        label_a_1 = Label(window_notice,
                   text='启动' if lan == 1 else 'Launch',
                   font=("Microsoft YaHei UI", 10))
        label_a_1.place(relx=0.31, y=10, relwidth=0.15, height=40)
        voice = StringVar()
        cmb2 = Combobox(window_notice,values=voice, state='readonly')
        cmb2['value'] = ('SystemAsterisk','OFF')
        cmb2.current(sound)
        cmb2.bind("<<ComboboxSelected>>",func2)
        cmb2.place(relx=0.31, y=50, relwidth=0.3, height=40) 
        label_a_2 = Label(window_notice,
                   text='开始运行' if lan == 1 else 'Run',
                   font=("Microsoft YaHei UI", 10))
        label_a_2.place(relx=0.31, y=90, relwidth=0.15, height=40)
        voice = StringVar()
        cmb4 = Combobox(window_notice,values=voice, state='readonly')
        cmb4['value'] = ('SystemAsterisk','OFF')
        cmb4.current(sound2)
        cmb4.bind("<<ComboboxSelected>>",func4)
        cmb4.place(relx=0.31, y=130, relwidth=0.3, height=40) 
        label_a_3 = Label(window_notice,
                   text='结束运行' if lan == 1 else 'Stop',
                   font=("Microsoft YaHei UI", 10))
        label_a_3.place(relx=0.31, y=170, relwidth=0.15, height=40)
        voice = StringVar()
        cmb5 = Combobox(window_notice,values=voice, state='readonly')
        cmb5['value'] = ('SystemAsterisk','OFF')
        cmb5.current(sound3)
        cmb5.bind("<<ComboboxSelected>>",func5)
        cmb5.place(relx=0.31, y=210, relwidth=0.3, height=40) 
        
        label_b = Label(window_notice,
                   text='其他通知' if lan == 1 else 'Other \nNotifica-\ntions',
                   font=("Microsoft YaHei UI", 20))
        label_b.place(relx=0.01, y=260, relwidth=0.3, height=150)
        label_b_1 = Label(window_notice,
                   text="更新提示" if lan == 1 else 'Update Tip',
                   font=("Microsoft YaHei UI", 10))
        label_b_1.place(relx=0.31, y=260, relwidth=0.3, height=40)
        b1 = StringVar()
        cmbb1 = Combobox(window_notice,values=b1, state='readonly')
        cmbb1['value'] = ('ON','OFF')
        cmbb1['state'] = DISABLED
        cmbb1.current(1)
        cmbb1.bind("<<ComboboxSelected>>",funcb1)
        cmbb1.place(relx=0.31, y=300, relwidth=0.3, height=40) 
        label_b_2 = Label(window_notice,
                   text="激活提醒" if lan == 1 else 'Activation Alert',
                   font=("Microsoft YaHei UI", 10))
        label_b_2.place(relx=0.31, y=340, relwidth=0.3, height=40)
        b2 = StringVar()
        cmbb2 = Combobox(window_notice,values=b2, state='readonly')
        cmbb2['value'] = ('ON','OFF')
        cmbb2['state'] = DISABLED
        cmbb2.current(1)
        cmbb2.bind("<<ComboboxSelected>>",funcb2)
        cmbb2.place(relx=0.31, y=380, relwidth=0.3, height=40)
        label_b_3 = Label(window_notice,
                   text="启动提醒" if lan == 1 else 'Launch Alert',
                   font=("Microsoft YaHei UI", 10))
        label_b_3.place(relx=0.31, y=420, relwidth=0.3, height=40)
        b3 = StringVar()
        cmbb3 = Combobox(window_notice,values=b3, state='readonly')
        cmbb3['value'] = ('ON','OFF')
        cmbb3['state'] = DISABLED
        cmbb3.current(1)
        cmbb3.bind("<<ComboboxSelected>>",funcb3)
        cmbb3.place(relx=0.31, y=460, relwidth=0.3, height=40)
        control = Button(window_notice, text ="禁用“快速设置页面”" if lan == 1 else "Disabled 'Quick Settings Page'", command = dis)
        control.pack(side='bottom')
    
# #FF6A00
# #006DDA
##----------------------------------------------------    
def t_close_handler_changelog():
    root.attributes('-disabled', 0)
    window_changelog.destroy()
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)
def changelog():
    
    def function2(*args):
        global lan
        if (cmb.get() == "Harmony(V4)"):
            state.configure(state='normal')
            state.delete('0.0', END)
            state.insert(INSERT, "> 4.4.0.134_Release Update 62\n")
            state.insert(INSERT, "    Optimize the Settings interface.\n")
            state.insert(INSERT, "    Optimize the About interface.\n")
            state.insert(INSERT, "    Allow configuration of software notifications.\n")
            state.insert(INSERT, "    Allows more detailed settings of the software interface, outputs.\n")
            state.insert(INSERT, "    Under the new runtime logic, it is allowed to set the window opened by the 'Settings' button.\n")
            state.insert(INSERT, "> 4.3.2.2_Release Update 55\n")
            state.insert(INSERT, "    Optimized the display effect of some interfaces.\n")
            state.insert(INSERT, "> 4.3.1.28_Release Update 53\n")
            state.insert(INSERT, "    Optimized running prompts.\n")
            state.insert(INSERT, "    Optimized the display of English(United States).\n")
            state.insert(INSERT, "> 4.3.0.12_Release Update 50\n")
            state.insert(INSERT, "    Optimized window management capabilities.\n")
            state.insert(INSERT, "    Optimized window right-click and window menus.\n")
            state.insert(INSERT, "    Fixed some bugs.\n")
            state.insert(INSERT, "> 4.2.5.0_Release Update 49\n")
            state.insert(INSERT, "    Fixed some bugs.\n")
            state.insert(INSERT, "> 4.2.4.8_Release Update 47\n")
            state.insert(INSERT, "    Support Restrict window closure gracefully.\n")
            state.insert(INSERT, "    Optimized the display effect of some interfaces.\n")
            state.insert(INSERT, "> 4.2.3.11_Release Update 46\n")
            state.insert(INSERT, "    Optimized the display effect of some interfaces.\n")
            state.insert(INSERT, "    Support 'Classical'(theme)\n")
            state.insert(INSERT, "> 4.2.2.05_Release Update 45\n")
            state.insert(INSERT, "    Optimized the display effect of some interfaces.\n")
            state.insert(INSERT, "> 4.2.1.64_Release Update 44\n")
            state.insert(INSERT, "    Support Windows 7 and Windows 8/8.1\n")
            state.insert(INSERT, "> 4.2.0.60_Release Update 43\n")
            state.insert(INSERT, "    Support English (United States)\n")
            state.insert(INSERT, "    Correct misrepresentations.\n")
            state.insert(INSERT, "> 4.1.0.34_Release Update 42\n")
            state.insert(INSERT, "    Fixed a bug where combobox could not display default values.\n")
            state.insert(INSERT, "    New Performance Monitor tool.\n")
            state.insert(INSERT, "    Experience optimization.\n")
            state.insert(INSERT, "> 4.0.0.146_Release Update 41\n")
            state.insert(INSERT, "    Welcome to Random Number Genertor 4.0.0. We will continue to update to bring you a better experience.\n")
            state.insert(INSERT, "    [Modified]\n")
            state.insert(INSERT, "    1. Modified the display logic of the control program running button to ensure a good touch control experience.\n")
            state.insert(INSERT, "    2. Modified the settings interface. Saving settings is now easier, the layout is cleaner, and the introduction is more intuitive!\n")
            state.insert(INSERT, "    3. Modify the error message of \"Error Retrieval Program\" (formerly \"Automatic Repair fixes\").\n")
            state.insert(INSERT, "    4. The 'Clock' window now allows for maximization and minimization, and improves running speed.\n")
            state.insert(INSERT, "    5. Increase window fade effect.\n")
            state.insert(INSERT, "    6. Optimized the experience of pop-ups.\n")
            state.insert(INSERT, "    7. Enable centered display for numeric values under certain conditions.\n")
            state.insert(INSERT, "    [New]\n")
            state.insert(INSERT, "    1. Added some windows.\n")
            state.insert(INSERT, "    2. The number of generated values now supports displaying 4 at the same time.\n")
            state.insert(INSERT, "    3. Added shortcut key support for some operations.\n")
            state.insert(INSERT, "    4. Added 'canvas' tool.\n")
            state.insert(INSERT, "    5. Added hints for some features.\n")
            state.insert(INSERT, "    6. When the number of outputs is set to 2, the pairing symbol is supported.\n")
            state.insert(INSERT, "    7. Added startup prompt.\n")
            state.insert(INSERT, "    8. Added \"Carousel instead of random\" (displayed when \"Positive integer\" and \"1\" are selected).\n")
            state.insert(INSERT, "    [Tool Upgrade]\n")
            state.insert(INSERT, "    1. Compiler update: Python 3.10.10 -> Python 3.10.11\n")
            state.insert(INSERT, "    2. Upgrade some third-party libraries.\n")
            state.configure(state='disabled')
        if (cmb.get() == "Silent(V3)"):
            state.configure(state='normal')
            state.delete('0.0', END)
            state.insert(INSERT, "> 3.7.1_Release (Build 2149 R6P1) Update 61\n")
            state.insert(INSERT, "    Update Policy.\n")
            state.insert(INSERT, "> 3.7.0_Release (Build 2148 R6P0) Update 60\n")
            state.insert(INSERT, "    Open and freely adjust the size of the window.\n")
            state.insert(INSERT, "> 3.6.1_Release (Build 2147 R5P1) Update 59\n")
            state.insert(INSERT, "    Optimize the application of 'Clock'\n")
            state.insert(INSERT, "> 3.6.0_Release (Build 2146 R5P0) Update 58\n")
            state.insert(INSERT, "    Comprehensive sinicization.\n")
            state.insert(INSERT, "    Optimize the application of 'Clock'\n")
            state.insert(INSERT, "> 3.5.2_Release (Build 2145 R4P2) Update 57\n")
            state.insert(INSERT, "    Optimized the display of some interfaces.\n")
            state.insert(INSERT, "> 3.5.1_Release (Build 2144 R4P1) Update 56\n")
            state.insert(INSERT, "    Optimized the about-more interface.\n")
            state.insert(INSERT, "> 3.5.0_Release (Build 2143 R4P0) Update 54\n")
            state.insert(INSERT, "    Added support for switching themes.\n")
            state.insert(INSERT, "> 3.4.0_Release (Build 2142 R3P0) Update 52\n")
            state.insert(INSERT, "    Added support for adjusting the startup sound.\n")
            state.insert(INSERT, "    Optimized the display of some interfaces.\n")
            state.insert(INSERT, "> 3.3.2_Release (Build 2141 R2P2) Update 51\n")
            state.insert(INSERT, "    Fixed some bugs.\n")
            state.insert(INSERT, "    Optimized the display of some interfaces.\n")
            state.insert(INSERT, "> 3.3.1_Release (Build 2140 R2P1) Update 48\n")
            state.insert(INSERT, "    Fixed some bugs.\n")
            state.insert(INSERT, "> 3.3.0_Release (Build 2139 R2P0) Update 40\n")
            state.insert(INSERT, "    Fix bugs! Fix a bug where the program cannot run with default settings\n")
            state.insert(INSERT, "    New! It is now supported to output 1 or 2 or 3 random numbers on the main page\n")
            state.insert(INSERT, "> 3.2.3_Release (Build 2138 R1P8) Update 39\n")
            state.insert(INSERT, "    Optimized the display of some interfaces\n")
            state.insert(INSERT, "> 3.2.2_Release (Build 2137 R1P7) Update 38\n")
            state.insert(INSERT, "    Optimize! With this update, we've added scroll bars to some text controls.\n")
            state.insert(INSERT, "    Optimize! With this update, we have resized some windows.\n")
            state.insert(INSERT, "> 3.2.1_Release (Build 2136 R1P6) Update 37\n")
            state.insert(INSERT, "    Fix bugs! This update fixes a [<设置><检查并应用设置>of<自动修复程序>] judgment error under certain configurations\n")
            state.insert(INSERT, "> 3.2.0_Release (Build 2135 R1P5) Update 36\n")
            state.insert(INSERT, "    Optimized some code\n")
            state.insert(INSERT, "    Optimized the display of some interfaces\n")
            state.insert(INSERT, "    Optimized the introduction of some errors\n")
            state.insert(INSERT, "    Bug fixes: Fixed a bug where Automatic Repair fixes specific configurations that did not work as expected\n")
            state.insert(INSERT, "    New! It is now supported to generate random numbers, and the output of the 'outputs' column is not duplicated\n")
            state.insert(INSERT, "> 3.1.0_Release (Build 2134 R1P4) Update 35\n")
            state.insert(INSERT, "    Modified parts of the menu bar so that you can now quickly select the issue type from the menu bar for feedback\n")
            state.insert(INSERT, "    Optimized the settings interface\n")
            state.insert(INSERT, "    Optimized the display of some interfaces\n")
            state.insert(INSERT, "    Disable some features under development in the menu bar\n")
            state.insert(INSERT, "    Upgrade compiler: Python 3.10.8->3.10.9\n")
            state.insert(INSERT, "> 3.0.3_Release (Build 2133 R1P3) Update 34\n")
            state.insert(INSERT, "    Repair procedural errors: when the program reports an error because the value of 'range' in the settings is empty or the value does not meet the requirements, the program automatically fixes the program abnormality, which makes it impossible to run\n")
            state.insert(INSERT, "    Repair language error: 'Changelog' -> 'Changelogs' in the menu\n")
            state.insert(INSERT, "    Changed the introduction of major version numbers\n")
            state.insert(INSERT, "    Changed the 'license', 'changelogs' interface size\n")
            state.insert(INSERT, "> 3.0.2_Release (Build 2132 R1P2) Update 33\n")
            state.insert(INSERT, "    Optimize the experience.Now, the program supports remembering your values in the '范围' input box (only remembering once is valid)\n")
            state.insert(INSERT, "    Change the recording order of Changelogs\n")
            state.insert(INSERT, "> 3.0.1_Release (Build 2131 R1P1) Update 32\n")
            state.insert(INSERT, "    Optimize the Settings interface\n")
            state.insert(INSERT, "    Fix language syntax error: Change '应用并检查设置' to '检查并应用设置'\n")
            state.insert(INSERT, "    Tips for optimizing the '检查并应用设置' option in Settings\n")
            state.insert(INSERT, "> 3.0.0_Release (Build 2130 R1P0) Update 31\n")
            state.insert(INSERT, "    Release Procedure\n")
            state.configure(state='disabled')
        if (cmb.get() == "Beta(V2)"):
            state.configure(state='normal')
            state.delete('0.0', END)
            state.insert(INSERT, "No content")
            state.configure(state='disabled')
        if (cmb.get() == "Alpha(V1)"):
            state.configure(state='normal')
            state.delete('0.0', END)
            state.insert(INSERT, "No content")
            state.configure(state='disabled')
    i = 0
    al = 0.99
    while al >= 0.6:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al -= i*4
    global window_changelog
    window_changelog = Toplevel(root)
    window_changelog.geometry("780x500")
    window_changelog.resizable(0,0)
    window_changelog.transient(root)
    window_changelog.protocol("WM_DELETE_WINDOW", t_close_handler_changelog)
    window_changelog.title("更新日志"if lan == 1 else "Changelogs")
    root.attributes('-disabled', 1)
    #Unint
    label = Label(window_changelog,
                   text="更新日志"if lan == 1 else "Changelogs",
                   font=("Microsoft YaHei UI", 12))
    label.pack()    
    mode = StringVar()
    cmb = Combobox(window_changelog,values=mode, state='normal')
    cmb.set('<PLEASE CHOOSE>')
    cmb.configure(state="readonly")
    cmb['value'] = ('Harmony(V4)','Silent(V3)','Beta(V2)','Alpha(V1)')
    cmb.bind("<<ComboboxSelected>>",function2)
    cmb.pack()
    
    
    state = ScrolledText(window_changelog, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=70, relwidth=0.96, height=410)
    
    state.insert(INSERT, "Please select the version you want to view above.\n\n")
    state.insert(INSERT, "This software has been updated so far, and there are four major versions.\n")
    state.insert(INSERT, "You can select an item in the drop-down bar above and view the changelog for that major version. \n(No change log for development and beta versions)")
     
    state.configure(state='disabled')
#-----------------------------------------------------

def topview():
    if homoStatus.get():
        root.attributes('-topmost', -1)
    else:
       root.attributes('-topmost', 0)    
def t_close_handler_clock():
    root.attributes('-disabled', 0)
    window_clock.destroy()
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)
def clock():
    i = 0
    al = 0.99
    while al >= 0.6:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al -= i*4
    global window_clock
    window_clock = Toplevel(root)
    window_clock.geometry("720x480")
    #window_clock.resizable(0,0)
    #window_clock.attributes('-toolwindow', True)
    window_clock.protocol("WM_DELETE_WINDOW", t_close_handler_clock)
    window_clock.title("Clock")
    root.attributes('-disabled', 1)

    lbl = tk.Label(window_clock, font=("arial", 40, "bold"), bg="black", fg="white")
    lbl.pack(anchor="center", fill="both", expand=1)
    global mode
    mode = 'hour'
    
    def showtime():
        if mode == 'hour':
            string = strftime("%H:%M:%S %p") 
        else: 
            string = strftime("%Y-%m-%d")#, ZhDate.today()
        lbl.config(text=string)
        lbl.after(100, showtime)

    def mouse_click(event):
        global mode
        mode = 'day' if mode == 'hour' else 'hour'

    lbl.bind("<Button>", mouse_click)
    showtime()

def t_close_handler_canvas():
    root.attributes('-disabled', 0)
    canvas_window.destroy()
    i = 0
    al = 0.6
    while al <= alpha/100:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al += i*4
    root.attributes('-alpha',alpha/100)
# 创建绘制函数
def canvas():
    global color
    i = 0
    al = 0.99
    while al >= 0.6:
        root.attributes('-alpha',al)
        time.sleep(0.01+(i*3))
        i += 0.01
        al -= i*4
    def colorselect():
        global color             # 设置全局变量
        colors = askcolor()
	# 设置color的颜色（R, G, B）, 因为在后面会传入只能传入整数，所以这里利用int() 进行四舍五入
        color = (int(colors[0][0]),int(colors[0][1]),int(colors[0][2])) 
        choosedcolor.set(str(color))         # 设置choosedcolor 变量的值
    def paint(event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        w.create_oval(x1, y1, x2, y2, fill='#%02x%02x%02x' %color, outline='#%02x%02x%02x' %color)  # 设置颜色为colorchooser所选择的
    global canvas_window
    canvas_window = Toplevel(root)
    canvas_window.geometry("820x615")
    canvas_window.resizable(0,0)
    canvas_window.transient(root)
    canvas_window.protocol("WM_DELETE_WINDOW", t_close_handler_canvas)
    canvas_window.title("画布" if lan == 1 else"Canvas")
    root.attributes('-disabled', 1)
    
    

    
    color = (0,0,0)
    choosedcolor = StringVar()
    choosedcolor.set(str(color))   # 设置初始颜色

    Label(canvas_window, text="画布" if lan == 1 else"Canvas").pack(padx=10,pady=10)
    Button(canvas_window, text="清除所有内容" if lan == 1 else"Clean All", command=(lambda a='all':w.delete(a))).place(x=610, y=0)
    frame1 = Frame(canvas_window)
    tk.Button(frame1, text="选择颜色" if lan == 1 else "Choose Color", relief='flat',command=colorselect).pack(side='left',padx=3, pady=3)
    
    Label(frame1, textvariable=choosedcolor).pack(side='left',padx=3, pady=3)
    frame1.pack(anchor='w')

    w = Canvas(canvas_window, width=810, height=500)
    w.pack()

    w.bind("<B1-Motion>", paint)   # 绘制函数绑定鼠标左键

    

    canvas_window.mainloop()


def cpu():
    global window_cpu
    window_cpu = Toplevel(root)
    window_cpu.geometry("640x320")
    window_cpu.resizable(0,0)
    window_cpu.attributes('-toolwindow', True)
    window_cpu.title("Performance Monitor")
    state = ScrolledText(window_cpu, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=40, relwidth=0.96, height=270)
    def refresh():
        state.configure(state='normal')
        state.delete('0.0', END)
        state.insert(INSERT, "刷新时间：" if lan == 1 else "Refresh time:")
        state.insert(INSERT, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        state.insert(INSERT, "\nCPU")
        state.insert(INSERT, "\nCPU逻辑数量\n" if lan == 1 else "\nThe number of CPU logics\n")
        state.insert(INSERT, psutil.cpu_count())
        state.insert(INSERT, "\nCPU物理核心数量\n" if lan == 1 else "\nThe number of physical CPU cores\n")
        state.insert(INSERT, psutil.cpu_count(logical=False))
        state.insert(INSERT, "\nCPU使用率\n" if lan == 1 else "\nCPU usage\n")
        state.insert(INSERT, psutil.cpu_percent(interval=0.5, percpu=True))
        state.insert(INSERT, "\nCPU频率\n" if lan == 1 else "\nCPU frequency\n")
        state.insert(INSERT, psutil.cpu_freq())
        state.insert(INSERT, "\n\n内存" if lan == 1 else "\n\nMemory")
        state.insert(INSERT, "\n内存使用情况\n" if lan == 1 else "\nMemory usage\n")
        state.insert(INSERT, psutil.virtual_memory())
        state.insert(INSERT, "\n\n磁盘" if lan == 1 else "\n\nDisk")
        state.insert(INSERT, "\n磁盘分区、系统盘使用率和磁盘IO\n" if lan == 1 else "\nDisk partitions, system disk usage, and disk I/O\n")
        state.insert(INSERT, psutil.disk_partitions())
        state.insert(INSERT, "\n")
        state.insert(INSERT, psutil.disk_usage("C:\\"))
        state.insert(INSERT, "\n")
        state.insert(INSERT, psutil.disk_io_counters())
        state.insert(INSERT, "\n\n网络" if lan == 1 else "\n\nNetwork")
        state.insert(INSERT, "\n网卡信息\n" if lan == 1 else "\nNIC information\n")
        state.insert(INSERT, psutil.net_io_counters(pernic=True))
        state.configure(state='disabled')
    refresh = Button(window_cpu, text ="刷新" if lan == 1 else "REFRESH", command = refresh)
    refresh.pack(anchor='ne')

def exit_pre():
    root.protocol('WM_DELETE_WINDOW',root)
    winmenu.entryconfig('禁止关闭' if lan == 1 else 'Forbidden Close', state=DISABLED)
def mini_pre():
    root.resizable(0,0)
    root.attributes('-toolwindow', True)
    winmenu.entryconfig('禁止最小化和最大化' if lan == 1 else 'Forbidden Minimization And Maximization', state=DISABLED)
    try:
        winmenu.entryconfig('锁定窗口大小' if lan == 1 else 'Lock Window Size', state=DISABLED)
    except:
        pass
def lock_window():
    root.resizable(0,0)
    winmenu.entryconfig('锁定窗口大小' if lan == 1 else 'Lock Window Size', state=DISABLED)
def callback_fuction(event):
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：焦点丢失\n"if lan == 1 else"Status: LOST FOCUS\n")
    state.insert(INSERT, "请重新聚焦本窗口以保证功能正常运行" if lan == 1 else "Please refocus this window to ensure proper functioning.")
    state.configure(state='disabled')
def callin_fuction(event):
    state.configure(state='normal')
    state.delete('0.0', END)
    if state_run == 0:
        state.insert(INSERT, "当前状态：空闲\n"if lan == 1 else"Status: IDLE\n")
        state.insert(INSERT, "您可以在设置参数后点击“开始运行”或按下键盘上的\"B\"启动程序并产生随机数。" if lan == 1 else "You can click 'Start Running' after setting the parameters or press 'B' on your keyboard to start the program and generate random numbers.")
    if state_run == 1:
        state.insert(INSERT, "当前状态：正在运行\n"if lan == 1 else "Status: RUNNING\n")
        state.insert(INSERT, "您可以点击“停止运行”或按下键盘上的\"E\"查看结果。\n" if lan == 1 else "You can click 'Stop Running' or press 'E' on your keyboard to see the results.\n")
        state.insert(INSERT, "当前设定值： "if lan == 1 else "Current setting:")
        state.insert(INSERT, f)
        state.insert(INSERT, " <-> ")
        state.insert(INSERT, e)
    state.configure(state='disabled')
    
#-----------------------------------------------------

label_1 = Label(root, text="Random Number Generator", font=("Microsoft YaHei UI", 12))
label_1.pack()

label_2 = Label(root,
                   text='运行提示'if lan == 1 else"Tips",
                   font=("Microsoft YaHei UI", 8))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
label_3 = Label(root,
                   text='控制台'if lan == 1 else"Control Center",
                   font=("Microsoft YaHei UI", 8))
label_3.place(relx=0.55, y=40, relwidth=0.45, height=25)
label_4 = Label(root,
                   text='输出栏' if lan == 1 else"Output Bar",
                   font=("Microsoft YaHei UI", 8))
label_4.place(relx=0.03, y=195, relwidth=0.45, height=25)
state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
state.place(relx=0.03, y=70, relwidth=0.5, height=120)
state.insert(INSERT, "当前状态：空闲\n"if lan == 1 else"Status: IDLE\n")
state.insert(INSERT, "您可以在设置参数后点击“开始运行”或按下键盘上的\"B\"启动程序并产生随机数。" if lan == 1 else "You can click 'Start Running' after setting the parameters or press 'B' on your keyboard to start the program and generate random numbers.")
state.configure(state='disabled')
#state.delete('0.0', END)
control = Button(root, text ="开始运行[B]" if lan == 1 else "RUN[B]", command = control)
control.place(relx=0.55, y=70, relwidth=0.4, height=70)
end = Button(root, text ="停止运行[E]" if lan == 1 else "STOP[E]", command = end)
end.place(relx=0.55, y=80, relwidth=0.4, height=100)
end['state'] = DISABLED
end.place_forget()
setting = Button(root, text ="设置" if lan == 1 else "Settings", command = setting)
setting.place(relx=0.55, y=140, relwidth=0.4, height=50)
root.bind("<b>",start_key)
root.bind("<e>",end_key)

####----------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='程序' if lan == 1 else 'Program', menu=filemenu)
filemenu.add_command(label='关于' if lan == 1 else 'About', command=about)
filemenu.add_command(label='更新日志' if lan == 1 else 'Changelogs', command=changelog)
filemenu.add_command(label='协议' if lan == 1 else 'License', command=license)

winmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='窗口' if lan == 1 else 'Window', menu=winmenu)
demoStatus = BooleanVar()
demoStatus.set(False)
homoStatus = BooleanVar()
homoStatus.set(False)
winmenu.add_checkbutton(label = "窗口前置" if lan == 1 else 'Front window',command=topview,variable=homoStatus)
winmenu.add_command(label='禁止关闭' if lan == 1 else 'Forbidden Close', command=exit_pre)
winmenu.add_command(label='禁止最小化和最大化' if lan == 1 else 'Forbidden Minimization And Maximization', command=mini_pre)
winmenu.add_command(label='锁定窗口大小' if lan == 1 else 'Lock Window Size', command=lock_window)
root.config(menu=menubar)
winmenu.add_separator()
winmenu.add_command(label='退出' if lan == 1 else 'EXIT', command=root.quit)

    
    
filemenu2 = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='工具' if lan == 1 else 'Tools', menu=filemenu2)
filemenu2.add_command(label='时钟' if lan == 1 else 'Clock', command=clock)
filemenu2.add_command(label='画布' if lan == 1 else 'Canvas', command=canvas)
filemenu2.add_separator()
filemenu2.add_command(label='性能监视器' if lan == 1 else 'Performance Monitor', command=cpu)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='获取帮助' if lan == 1 else 'HELP', menu=editmenu)
editmenu.add_command(label='Bug Report', command=github)
editmenu.add_command(label='Feature Request', command=github2)
editmenu.add_command(label='Seek Help', command=github3)
editmenu.add_command(label='Discussions', command=discuss)
root.config(menu=menubar) 

#<Button - 3>
rightmenu = Menu(root,tearoff=False)
rightmenu.add_command(label="恢复窗口大小" if lan == 1 else 'Restore Window Size',command=redo_window)
rightmenu.add_command(label="最大化" if lan == 1 else 'Maxmize',command=maxmize)
rightmenu.add_command(label="最小化" if lan == 1 else 'Minimize',command=minimize)
rightmenu.add_command(label="全屏" if lan == 1 else 'Full Screen',command=zoom)
rightmenu.add_command(label="解除全屏" if lan == 1 else 'Dismiss Full Screen',command=diszoom)
rightmenu.add_command(label="退出" if lan == 1 else 'Exit',command=root.destroy)
root.bind("<Button-3>",showPopupMenu)



root.bind("<FocusOut>",callback_fuction)
root.bind("<FocusIn>",callin_fuction)
root.mainloop()

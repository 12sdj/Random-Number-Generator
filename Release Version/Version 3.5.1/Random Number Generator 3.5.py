#!/user/bin/env python
# -*- coding:utf-8 -*-
# @software: Visual Studio Code
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



themeset_path = 'C:\\Random Number Generator\\'
if not os.path.exists(themeset_path):
    os.mkdir(themeset_path)
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



winWidth = 720
winHeight = 480
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry(f"{winWidth}x{winHeight}+{x}+{y}")
root.title("Random Number Generator")
root.resizable(0,0)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)#>=win8.1
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()#<win8.1
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
#----------------------------------------------------------
global outputset
outputset = 3
global f
f = 1
global e
e = 50
global end_control
global numset
numset = 1

#####LANGUAGE_________________________________________------------------------
'''
user_name = getpass.getuser() # 获取当前用户名
hostname = socket.gethostname()
drive = os.getenv("SystemDrive")
global lan
#languageset_path = drive + "\\User\\" + user_name + "\AppData\Local\Random Number Generator\LanguageSet.txt"
languageset_path = "D:"+ "\\LanguageSet.txt"
print(languageset_path)
try:
    with open(languageset_path,"r+") as f:
        lines = f.read() ##Assume the sample file has 3 lines
        first = lines.split('\n', 1)[0]
        str(first)
        #print(first)#test code
    #win32api.SetFileAttributes('LanguageSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
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
            control_info = showerror(title='Program Error',message="Please do not change the configuration file: LanguageSet.txt")

            

            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('American English')
                lan = 2
            except:
                lan = 0
    except:
        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #01")

            

except:
    try:

        with open(languageset_path,"w+") as f:
            f.write('American English')
        #win32api.SetFileAttributes('LanguageSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
        with open(languageset_path,"r+") as f:
            lines = f.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]
        try:
            lan = 2
        except:
  
            control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #02")
            
            

    except:

        control_info = showerror(title='Program Error',message="Known Error! Please go to our 'Github - Issue' to feedback the issue #03")
 

'''
#####-------------------------------------------------------------------------
#####----------------------------------------------------------------MAIN UNIT!!!!!!
# #98D2E4
# #FF6A00
# #006DDA


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
            try:
                number_1 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n")
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
            time.sleep(0.01)
            global number_2
            try:
                number_2 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n")
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
            time.sleep(0.01)
            global number_3
            try:
                number_3 = randint(f,e) if numset in [2, 3] else uniform(f,e)
            except Exception:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法运行。\n")
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
    setting['state'] = DISABLED
    state.configure(state='normal')
    state.delete('0.0', END)
    state.insert(INSERT, "当前状态：正在运行\n")
    state.insert(INSERT, "您可以点击“停止运行”进行查看\n")
    state.insert(INSERT, "当前设定值： ")
    state.insert(INSERT, f)
    state.insert(INSERT, " <-> ")
    state.insert(INSERT, e)
    state.configure(state='disabled')
    state_1.configure(state='normal')
    state_2.configure(state='normal')
    state_3.configure(state='normal')
    t1.resume()
    t2.resume()
    t3.resume()
    #message = "The Random Number Is "+ str(number_1)
    #control_info = showinfo(title='INFO',message=message)
def end():  # sourcery skip: avoid-builtin-shadow
    control['state'] = NORMAL
    end['state'] = DISABLED
    setting['state'] = NORMAL

    list=[]
    for _ in range(100):
        r = randint(f,e) if numset in [2, 3] else uniform(f,e)
        if r not in list: list.append(r)
    try:
        number_a = list[0]
        number_b = list[1]
        number_c = list[2]
    except Exception:
        if numset in [2, 3]:
            number_a = randint(f,e)
            number_b = randint(f,e)
            number_c = randint(f,e)
        else:
            number_a = uniform(f,e)
            number_b = uniform(f,e)
            number_c = uniform(f,e)
    #L1 = sample(range(f, e), 5)
    #print(L1)

    state_1.delete('0.0', END)
    state_1.insert(INSERT, number_a)

    state_2.delete('0.0', END)
    state_2.insert(INSERT, number_b)

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
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=bug_report.md&title=')
def github2():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=feature_request.md&title=')
def github3():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/issues/new?assignees=&labels=&template=seek-help.md&title=%5BSeek+Help%5D')        
def discuss():
    webbrowser.open('https://github.com/12sdj/Random-Number-Generator/discussions')
def minimize():
    root.iconify()
def showPopupMenu(event):
    rightmenu.post(event.x_root,event.y_root)
##---------------------------------------------------
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
        window_mean.transient(root)
        window_mean.protocol("WM_DELETE_WINDOW", t_close_handler_mean)
        window_mean.title("Abort-More")
        window_about.attributes('-disabled', 1)
        ti_window = Label(window_mean,
                    text='Silent(22H2)\n',
                    font=("Microsoft YaHei UI", 15),
                    foreground="black")
        ti_window.pack()
        state = Text(window_mean, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.1, y=80, relwidth=0.35, height=230)
        state.insert(INSERT, "Silent 版本说明\n")
        state.insert(INSERT, "'Silent' 是22H2这个最主要版本号的目标的体现。在'Silent(22H2)'中，程序将以静态的方式呈现更精美的布局、更朴素的控件和更方便的交互，争取将程序的基本结构和发展方向在这个版本中得到确定")
        state.configure(state='disabled')
        state2 = Text(window_mean, relief="flat", font=("Microsoft YaHei UI", 10))
        state2.place(relx=0.55, y=80, relwidth=0.35, height=230)
        state2.insert(INSERT, "Silent 维护周期\n")
        state2.insert(INSERT, "支持状态：允许功能更新（到24H1）\n结束维护时间：24H2")
        state2.configure(state='disabled')
    def update():
        webbrowser.open('https://github.com/12sdj/Random-Number-Generator/releases/')
    global window_about
    window_about = Toplevel(root)
    window_about.geometry("680x340+200+250")
    window_about.resizable(0,0)
    window_about.attributes('-toolwindow', True)
    window_about.title("About")
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
                            'Version 3.5.1_Release (Build 2144 R4P1)\n'
                            '2024/2/12 20:48(UTC+8) Update 56\n'
                            'Copyright (c) 2022 12sdj',
                    font=("Microsoft YaHei UI", 10),
                    foreground="black")
    tip_window.pack()
    control = Button(window_about, text ="更多信息", command = mean)
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
    window_licence.geometry("780x590+200+250")
    window_licence.resizable(0,0)
    window_licence.transient(root)
    window_licence.protocol("WM_DELETE_WINDOW", t_close_handler_licence)
    window_licence.title("License")
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_licence,
                   text='License',
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()
    state = ScrolledText(window_licence, relief="flat", font=("Microsoft YaHei UI", 10))
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
def setting():  # sourcery skip: avoid-builtin-shadow
    global num
    num = 1

    def func(*args):
        pass

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


    def chosen():
        global numset
        numset = var.get()

    def chosen2():
        global outputset
        outputset = var3.get()
        if outputset == 1:
            state_1.place_forget()
            state_2.place_forget()
            state_3.place_forget()
            state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
            state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
            state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
            state_1.place_forget()
            state_3.place_forget()
        if outputset == 2:
            state_1.place_forget()
            state_2.place_forget()
            state_3.place_forget()
            state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
            state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
            state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
            state_2.place_forget()
        if outputset == 3:
            state_1.place_forget()
            state_2.place_forget()
            state_3.place_forget()
            state_1.place(relx=0.01, y=225, relwidth=0.32, height=220)
            state_2.place(relx=0.34, y=225, relwidth=0.32, height=220)
            state_3.place(relx=0.67, y=225, relwidth=0.32, height=220)
        

    def chosen_seed():
        global sum
        global ar
        sum = var2.get()
        if sum == 1:
            input['state'] = DISABLED
        else:
            input['state'] = NORMAL
            ar = str(input.get())
            seed(ar)

    def application():
        global f
        global e
        global numset
        try:
            
            f = float(label_b_1.get())
            e = float(label_b_3.get())
            
                #####
            if f >= e:
                control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（前一个控件的值不能大于或等于后一个控件的值）\n建议更改后再次检查设置\n")
                control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                f = 1
                e = 50
                label_b_1.delete(0, "end")
                label_b_1.insert(0, f)
                label_b_3.delete(0, "end")
                label_b_3.insert(0, e)
            if numset == 1:
                control_info = showinfo(title='Program Info',message="没有发现原则性错误。\n程序经过检查，发现你的设置没有原则性错误，你可以正常使用Random Number Generator!\n")

            if numset == 2:
                if f <= 0 or e <= 0 or f % 1 != 0 or e % 1 != 0 or f <= 0.0 or e <= 0.0 or f % 1 != 0.0 or e % 1 != 0.0:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n")
                    control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                    f = 1
                    e = 50
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)
                else:
                    f = int(label_b_1.get())
                    e = int(label_b_3.get())
                    control_info = showinfo(title='Program Info',message="没有发现原则性错误。\n程序经过检查，发现你的设置没有原则性错误，你可以正常使用Random Number Generator!\n")
            if numset == 3:
                if f % 1 != 0 or e % 1 != 0 or f % 1 != 0.0 or e % 1 != 0.0:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n")
                    control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                    f = 1
                    e = 50
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)
                else:
                    f = int(label_b_1.get())
                    e = int(label_b_3.get())
                    control_info = showinfo(title='Program Info',message="没有发现原则性错误。\n程序经过检查，发现你的设置没有原则性错误，你可以正常使用Random Number Generator!\n")
            if numset == 4:
                s=str(f).split('.')
                s1=str(e).split('.')
                if float(s[1])==0 or float(s1[1])==0:
                    control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件必须是一个小数）\n建议更改后再次检查设置\n")
                    control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                    f = 1.5
                    e = 50.5
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)
                else:
                    control_info = showinfo(title='Program Info',message="没有发现原则性错误。\n程序经过检查，发现你的设置没有原则性错误，你可以正常使用Random Number Generator!\n")

        except Exception:
            f = str(label_b_1.get())
            e = str(label_b_3.get())

            if not f or not e:
                control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个输入框不能为空，请填写符合您配置的值）。\n建议更改后再次检查设置\n")
                control_info = showinfo(title='Program Info',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                f = 1
                e = 50
                label_b_1.delete(0, "end")
                label_b_1.insert(0, f)
                label_b_3.delete(0, "end")
                label_b_3.insert(0, e)
            else:
                s=str(f).split('.')
                s1=str(e).split('.')
                if float(s[1])==0 or float(s1[1])==0:
                    if numset == 2:
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个正整数）\n建议更改后再次检查设置\n")
                        control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                        f = 1
                        e = 50
                        label_b_1.delete(0, "end")
                        label_b_1.insert(0, f)
                        label_b_3.delete(0, "end")
                        label_b_3.insert(0, e)
                        
                    if numset == 3:                    
                        control_info = showerror(title='Program Error',message="程序出现问题，因此无法启用设置。\n经过检查，程序发现：出错的原因是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（两个控件的值必须是一个整数）\n建议更改后再次检查设置\n")
                        control_info = showwarning(title='Program Warning',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                        f = 1
                        e = 50
                        label_b_1.delete(0, "end")
                        label_b_1.insert(0, f)
                        label_b_3.delete(0, "end")
                        label_b_3.insert(0, e)
                else:
                    control_info = showwarning(title='Program Warning',message="程序出现问题，因此无法运行“检查设置”。\n经过初步判断，程序认为：出错的原因可能是你的设置不当所引起的。\n请检查以下位置的值：\n•  抽取设置 - 范围（输入的值必须是一个有理数）。\n建议更改后再次检查设置\n")
                    control_info = showinfo(title='Program Info',message="没有发现程序不可修复的错误。\n程序经过检查，发现你的设置没有原则性错误。你的不当设置程序可以自动修复，因此你可以正常使用Random Number Generator!\n")
                    f = 1
                    e = 50
                    label_b_1.delete(0, "end")
                    label_b_1.insert(0, f)
                    label_b_3.delete(0, "end")
                    label_b_3.insert(0, e)
            '''There was a problem with the program, so the settings could not be enabled.
After checking, the program found that the reason for the error was caused by your improper settings.
Please check the value in the following position: Extraction Settings - Range (the value of the previous control cannot be greater than the value of the next control)
It is recommended to change and check the settings again
'''

    def application2():
        global outputset
        outputset = 3
        global numset
        numset = 1
        global f,e
        var.set(1)
        var2.set(1)
        var3.set(outputset)
        f = 1
        e = 50
        label_b_1.delete(0, "end")
        label_b_1.insert(0, f)
        label_b_3.delete(0, "end")
        label_b_3.insert(0, e)
        input.delete(0, 'end')
        input['state'] = DISABLED
        control_info = showinfo(title='Program Info',message="已恢复Random Number Generator默认设置\n")



    global window_setting
    window_setting = Toplevel(root)
    window_setting.geometry("850x600+350+550")
    window_setting.resizable(0,0)
    window_setting.transient(root)
    window_setting.protocol("WM_DELETE_WINDOW", t_close_handler_setting)
    window_setting.title("设置")
    root.attributes('-disabled', 1)
    #Unint
    label_b = Label(window_setting,
                   text='设置',
                   font=("Microsoft YaHei UI", 12))
    label_b.pack()    

    vertical =tk.Frame(window_setting, background='red', height=500,width=1)
    horizontal =tk.Frame(window_setting, background='blue', height=1,width=830)
    vertical.place(x=424, y=40)
    horizontal.place(x=10, y=319)
    label1 = Label(window_setting,
                   text='基础设置',
                   font=("Microsoft YaHei UI", 10))
    label1.place(relx=0.35, y=289, relwidth=0.14, height=30)
    #label1.place_forget()
    label2 = Label(window_setting,
                   text='抽取设置',
                   font=("Microsoft YaHei UI", 10))
    label2.place(relx=0.55, y=289, relwidth=0.14, height=30)
    label3 = Label(window_setting,
                   text='辅助功能',
                   font=("Microsoft YaHei UI", 10))
    label3.place(relx=0.35, y=320, relwidth=0.14, height=30)
    label4 = Label(window_setting,
                   text='高级设置',
                   font=("Microsoft YaHei UI", 10))
    label4.place(relx=0.55, y=320, relwidth=0.14, height=30)

    label_a_1 = Label(window_setting,
                   text='语言',
                   font=("Microsoft YaHei UI", 8))
    label_a_1.place(relx=0.01, y=40, relwidth=0.15, height=25)
    label_a_2 = Label(window_setting,
                   text='主题',
                   font=("Microsoft YaHei UI", 8))
    label_a_2.place(relx=0.01, y=120, relwidth=0.15, height=25) 

    mode = StringVar()
    cmb = Combobox(window_setting,values=mode, state='readonly')
    cmb['value'] = ('简体中文（中国大陆）')
    cmb.current(0)
    cmb.bind("<<ComboboxSelected>>",func)
    cmb.place(relx=0.01, y=70, relwidth=0.3, height=40) 

    theme = StringVar()
    cmd = Combobox(window_setting,values=theme, state='readonly')
    cmd.place(relx=0.01, y=150, relwidth=0.3, height=40)
    cmd['value'] = ('Classical','Adapta')
    cmd.current(themes-1)
    cmd.bind("<<ComboboxSelected>>",funk)



    label_b = Label(window_setting,
                   text='随机数类型',
                   font=("Microsoft YaHei UI", 8))
    label_b.place(relx=0.51, y=40, relwidth=0.3, height=30)

    var = IntVar()
    var.set(numset)
    b = Radiobutton(window_setting,text="有理数",variable = var ,value =1,command=chosen)
    b.place(relx=0.51, y=70, relwidth=0.24, height=40)
    b2 = Radiobutton(window_setting,text="正整数",variable = var ,value =2,command=chosen)
    b2.place(relx=0.75, y=70, relwidth=0.24, height=40)
    b3 = Radiobutton(window_setting,text="整数",variable = var ,value =3,command=chosen)
    b3.place(relx=0.51, y=110, relwidth=0.24, height=40)
    b4 = Radiobutton(window_setting,text="小数",variable = var ,value =4,command=chosen)
    b4.place(relx=0.75, y=110, relwidth=0.24, height=40) 

    label_b = Label(window_setting,
                   text='范围',
                   font=("Microsoft YaHei UI", 8))


    label_b.place(relx=0.51, y=150, relwidth=0.1, height=30)
    label_b_1 = Entry(window_setting, font=("Microsoft YaHei UI", 10),background='gray')
    label_b_1.place(relx=0.61, y=150, relwidth=0.15, height=30)
    label_b_2 = Label(window_setting,text = '-', font=("Microsoft YaHei UI", 10))
    label_b_2.place(relx=0.77, y=150, relwidth=0.02, height=30)
    label_b_3 = Entry(window_setting, font=("Microsoft YaHei UI", 10),background='gray')
    label_b_3.place(relx=0.8, y=150, relwidth=0.15, height=30)

    label_b_1.delete(0, "end")
    label_b_1.insert(0, f)
    label_b_3.delete(0, "end")
    label_b_3.insert(0, e)

    label_b_2 = Label(window_setting,
                   text='输出数量',
                   font=("Microsoft YaHei UI", 8))
    label_b_2.place(relx=0.51, y=200, relwidth=0.6, height=30)
    var3 = IntVar()
    var3.set(outputset)
    b = Radiobutton(window_setting,text="1",variable = var3 ,value =1,command=chosen2)
    b.place(relx=0.51, y=230, relwidth=0.12, height=40)
    b2 = Radiobutton(window_setting,text="2",variable = var3 ,value =2,command=chosen2)
    b2.place(relx=0.63, y=230, relwidth=0.12, height=40)
    b3 = Radiobutton(window_setting,text="3",variable = var3 ,value =3,command=chosen2)
    b3.place(relx=0.74, y=230, relwidth=0.12, height=40)



 





    label_c = Label(window_setting,
                   text='启动声效',
                   font=("Microsoft YaHei UI", 8))
    label_c.place(relx=0.01, y=360, relwidth=0.4, height=30)
    voice = StringVar()
    cmb2 = Combobox(window_setting,values=voice, state='readonly')
    cmb2['value'] = ('SystemAsterisk','OFF')
    cmb2.current(sound)
    cmb2.bind("<<ComboboxSelected>>",func2)
    cmb2.place(relx=0.01, y=390, relwidth=0.3, height=40) 

    label_d = Label(window_setting,
                   text='Python Random Seed Setting',
                   font=("Microsoft YaHei UI", 8))
    label_d.place(relx=0.51, y=360, relwidth=0.35, height=30)
    var2 = IntVar()
    var2.set(1)
    b4 = Radiobutton(window_setting,text="Off",variable = var2 ,value =1,command=chosen_seed)
    b4.place(relx=0.51, y=390, relwidth=0.12, height=40)
    b5 = Radiobutton(window_setting,text="On",variable = var2 ,value =2,command=chosen_seed)
    b5.place(relx=0.63, y=390, relwidth=0.12, height=40)
    input = Entry(window_setting, font=("Microsoft YaHei UI", 10),background='gray')
    input.place(relx=0.75, y=395, relwidth=0.2, height=30)
    input['state'] = DISABLED

    application = Button(window_setting,
                    text='检查并应用设置',
                    command=application)

    application.place(relx=0.02, y=560, relwidth=0.25, height=35)
    application2 = Button(window_setting,
                    text='恢复默认设置',
                    command=application2)

    application2.place(relx=0.27, y=560, relwidth=0.25, height=35)
    label_tip2 = Label(window_setting,
                   text='您对程序的配置会产生不同的效果',
                   font=("Microsoft YaHei UI", 9))
    label_tip2.place(relx=0.66, y=560, relwidth=0.32, height=35) 
##----------------------------------------------------    
def t_close_handler_changelog():
    root.attributes('-disabled', 0)
    window_changelog.destroy()
def changelog():
    global window_changelog
    window_changelog = Toplevel(root)
    window_changelog.geometry("780x500+150+150")
    window_changelog.resizable(0,0)
    window_changelog.transient(root)
    window_changelog.protocol("WM_DELETE_WINDOW", t_close_handler_changelog)
    window_changelog.title("Changelogs")
    root.attributes('-disabled', 1)
    #Unint
    label = Label(window_changelog,
                   text='更新日志',
                   font=("Microsoft YaHei UI", 12))
    label.pack()    
    label = Label(window_changelog,
                   text='更新日志仅记录3.x版本下的更改',
                   font=("Microsoft YaHei UI", 8))
    label.pack()    
    state = ScrolledText(window_changelog, relief="flat", font=("Microsoft YaHei UI", 10))
    state.place(relx=0.02, y=70, relwidth=0.96, height=410)
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
        viewa = f"当前设定值:{str(acc)}"
                
            

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
        scale = Scale(window, from_=10, to_=96,orient=HORIZONTAL,length=220)
        scale.set(85)
        scale.pack()

        root.attributes('-disabled', 1)#Top=window
        tip_window = Label(window,
                    text=
                    '通过拖动或点击滑动条设置主窗口透明度。\n'
                            '数值越小，透明程度越高；数值越大，则反之\n'
                            '建议的值为85-95之间，默认值为85',
                    font=("Microsoft YaHei UI", 8),
                    foreground="black")
        tip_window.pack()






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
def t_close_handler_clock():
    root.attributes('-disabled', 0)
    window_clock.destroy()
def clock():
    global window_clock
    window_clock = Toplevel(root)
    window_clock.geometry("640x340+150+150")
    window_clock.resizable(0,0)
    window_clock.attributes('-toolwindow', True)
    window_clock.protocol("WM_DELETE_WINDOW", t_close_handler_clock)
    window_clock.title("Clock")
    root.attributes('-disabled', 1)

    lbl = tk.Label(window_clock, font=("arial", 40, "bold"), bg="black", fg="white")
    lbl.pack(anchor="center", fill="both", expand=1)
    global mode
    mode = 'hour'
    def showtime():
        string = strftime("%H:%M:%S %p") if mode == 'hour' else strftime("%Y-%m-%d")
        lbl.config(text=string)
        lbl.after(1000, showtime)

    def mouse_click(event):
        global mode
        mode = 'day' if mode == 'hour' else 'hour'

    lbl.bind("<Button>", mouse_click)
    showtime()


#-----------------------




#-----------------------------------------------------
label_1 = Label(root,
                   text='Random Number Generator',
                   font=("Microsoft YaHei UI", 12))
label_1.pack()
label_2 = Label(root,
                   text='状态',
                   font=("Microsoft YaHei UI", 8))
label_2.place(relx=0.03, y=40, relwidth=0.45, height=25)
label_3 = Label(root,
                   text='控制',
                   font=("Microsoft YaHei UI", 8))
label_3.place(relx=0.55, y=40, relwidth=0.45, height=25)
label_4 = Label(root,
                   text='输出',
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
menubar.add_cascade(label='更多选项', menu=filemenu)
filemenu.add_command(label='关于本程序', command=about)
filemenu.add_command(label='更新日志', command=changelog)
filemenu.add_command(label='开源协议', command=licence)

winmenu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='窗口', menu=winmenu)
demoStatus = BooleanVar()
demoStatus.set(False)
homoStatus = BooleanVar()
homoStatus.set(False)
winmenu.add_checkbutton(label = "透明效果",command=status,variable=demoStatus)
winmenu.add_checkbutton(label = "窗口前置",command=topview,variable=homoStatus)
root.config(menu=menubar)
winmenu.add_separator()
winmenu.add_command(label='退出应用', command=root.quit)
    
    
filemenu2 = Menu(menubar, tearoff=0)  
menubar.add_cascade(label='工具', menu=filemenu2)
filemenu2.add_command(label='Clock', command=clock)



editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='帮助', menu=editmenu)
editmenu.add_command(label='Bug Report', command=github)
editmenu.add_command(label='Feature Request', command=github2)
editmenu.add_command(label='Seek Help', command=github3)
editmenu.add_command(label='Discussions', command=discuss)
root.config(menu=menubar) 

#<Button - 3>
rightmenu = Menu(root,tearoff=False)
rightmenu.add_command(label="最小化",command=minimize)
rightmenu.add_command(label="退出",command=root.destroy)
root.bind("<Button-3>",showPopupMenu)




root.mainloop()

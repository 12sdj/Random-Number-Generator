import tkinter as tk  
import tkinter.messagebox
import tkinter.simpledialog
from random import*
from time import*
import os
import wave
import sys


upwin = []


window = tk.Tk()

window.title('数值生成器')
 

window.geometry('550x350') 
 

var = tk.StringVar()

l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()


k = tk.Label(window, bg='red', width=20, text='empty')
k.pack()


# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
on_hit1 = False

def hit_me():
    global on_hit

    if on_hit == False:
        on_hit = True
        try:
            var.set('BEGINNING!')
            ########
            ag = randint(1,result)
            global a1
            a1=0
            if a1 == ag:
                ag = randint(1,result)
            else:
                if ag in upwin:
                    var.set(ag)
                    print("生成数值：",ag,"重复!")
                    a1=ag
                    sleep(0.01)
                else:
                    var.set(ag)
                    print("生成数值：",ag)
                    a1=ag
                    sleep(0.01)
                    upwin.append(ag)
            on_hit = False
        except IndexError:
            abc1 = tkinter.messagebox.showwarning(title = 'Error',message='索引错误：运行程序时输入的参数个数不够')
        except ValueError:
            abc2 = tkinter.messagebox.showwarning(title = 'Error',message='数值错误：程序只能接收正整数参数！')
        except ArithmeticError:
            abc3 = tkinter.messagebox.showwarning(title = 'Error',message='算术错误：其中一个数可能包含0！')
        except Exception:
            abc4 = tkinter.messagebox.showwarning(title = 'Error',message='未知异常！ERRORCODE_001E')
    else:
        on_hit = False
        var.set('Turn Off')

def settings():
    global result
    result = tkinter.simpledialog.askinteger(title = 'Settings',prompt='             Set the number of people             ',initialvalue = '50')
    global r
    r=0
    for o in range(result):
        acb = []
        
        r+=1
        acb.append(r)
  
    print(acb)
    # 打印内容
    
def about():
    result = tkinter.messagebox.showinfo(title = 'About this',message='Made by Python3.10 Tkinter')
    #print("Now is playing Capo Productions - Inspire")
    #d = open('About.txt', 'r')
    #f = open('Beginning.mp3', 'r')
    #playsound('Beginning.mp3')

    #file_path = os.path.join(py_dir,'Beginning.mp3') 


def exit_1():
    global on_hit1
    if on_hit1 == False:
        var.set('continue')
        on_hit1 = True
    else:
        var.set('Turn Off')
        exit(0)
def print_selection():
    l.config(text='you have selected ' + var.get())
    if var.get()=='A':
        var.set('Open cmd')
        try:
            os.system('cmd')
        except IndexError:
            abc1 = tkinter.messagebox.showwarning(title = 'Error',message='索引错误：运行程序时输入的参数个数不够')
        except ValueError:
            abc2 = tkinter.messagebox.showwarning(title = 'Error',message='数值错误：程序只能接收正整数参数！')
        except ArithmeticError:
            abc3 = tkinter.messagebox.showwarning(title = 'Error',message='算术错误：其中一个数可能包含0！')
        except Exception:
            abc4 = tkinter.messagebox.showwarning(title = 'Error',message='未知异常！ERRORCODE_001E')
    if var.get()=='B':
        var.set('Open calc')
        try:
            os.system('start calc.exe')
        except IndexError:
            abc1 = tkinter.messagebox.showwarning(title = 'Error',message='索引错误：运行程序时输入的参数个数不够')
        except ValueError:
            abc2 = tkinter.messagebox.showwarning(title = 'Error',message='数值错误：程序只能接收正整数参数！')
        except ArithmeticError:
            abc3 = tkinter.messagebox.showwarning(title = 'Error',message='算术错误：其中一个数可能包含0！')
        except Exception:
            abc4 = tkinter.messagebox.showwarning(title = 'Error',message='未知异常！ERRORCODE_001E')
    if var.get()=='C':
        var.set('shutdown')
        try:
            os.system('shutdown -s -f -t 0')
        except IndexError:
            abc1 = tkinter.messagebox.showwarning(title = 'Error',message='索引错误：运行程序时输入的参数个数不够')
        except ValueError:
            abc2 = tkinter.messagebox.showwarning(title = 'Error',message='数值错误：程序只能接收正整数参数！')
        except ArithmeticError:
            abc3 = tkinter.messagebox.showwarning(title = 'Error',message='算术错误：其中一个数可能包含0！')
        except Exception:
            abc4 = tkinter.messagebox.showwarning(title = 'Error',message='未知异常！ERRORCODE_001E')


            #####
    if var.get()=='D':
        var.set('Timer')
        global numb
        numb = 0


        def run_num(target):
            def counting():
                global numb
                numb += 0.5
                target.config(text=str(numb))
                target.after(500, counting)   # 间隔1000毫秒再次执行counting函数
            counting()
        run_num(k)




def print_selection1(v):
    k.config(text='you have selected ' + v)
# 第5步，在窗口界面设置放置Button按键
b1 = tk.Button(window, text='Settings', font=('Arial', 12), width=14, height=1, command=settings)
b1.pack()
b2 = tk.Button(window, text='About & helps', font=('Arial', 12), width=14, height=1, command=about)
b2.pack()
b = tk.Button(window, text='hit me', font=('Arial', 14), width=18, height=1, command=hit_me)
b.pack()
b3 = tk.Button(window, text='Exit', font=('Arial', 11), width=12, height=1, command=exit_1)
b3.pack()
r1 = tk.Radiobutton(window, text='Option A(cmd)', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B(calc)', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C(shutdown 0)', variable=var, value='C', command=print_selection)
r3.pack()
r4 = tk.Radiobutton(window, text='Option D(timer)', variable=var, value='D', command=print_selection)
r4.pack()


 
# 第6步，主窗口循环显示
window.mainloop()

from tkinter import*
from random import*
from tkinter.ttk import*
from tkinter.messagebox import*
import ctypes

root=Tk()
'''


'''
winWidth = 480
winHeight = 330
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
control = Button(root, text ="HIT IT!", command = control)
control.pack()
label = Label(root,text="Version 2.0.1_Alpha 05",foreground="gray")
label.pack()
label_1 = Label(root,text="Made By 12sdj",foreground="gray")
label_1.pack()


root.mainloop()

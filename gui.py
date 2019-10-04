#!/usr/bin/python
# -*- coding: UTF-8 -*-

import test
import tkinter as tk

window = tk.Tk()
window.title('Luke_J制作密码强度检测器')
window.geometry('300x300')
e = tk.Entry(window,show=None)
e.pack()

def insert_point():
    
    var = e.get()
    w = test.password(var)
    t.insert('insert',w)
def clear():
    t.delete('1.0','end')
b1 = tk.Button(window,text='强度检测',width=15,
            height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='清除文本框',width=15,
            height=2,command=clear)
b2.pack()
t = tk.Text(window,height=2)
t.pack()

window.mainloop()

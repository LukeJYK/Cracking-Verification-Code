import tkinter as tk

window = tk.Tk()
window.title('姜彦凯自制登陆界面')
window.geometry('450x300')

# welcome image

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='captcha.gif')
image = canvas.create_image(300,140, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 50)
tk.Label(window, text='Password:').place(x=50, y= 90)
tk.Label(window, text='CAPTCHA:').place(x=50, y= 130)
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=50)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=90)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=140)
def usr_login():
    pass
def usr_sign_up():
    pass

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=50, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()

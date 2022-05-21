import tkinter as tk
from utils import * 
from tkinter import ttk
from tkinter import messagebox
import re
def signUpButtonOnClick():
        if fullNameEntry.get() and fullNameEntry.get().strip() and re.search(emailPattern, emailEntry.get()) and len(passwordEntry.get()) >= 10 and passwordEntry.get() == passwordConfirmationEntry.get() and checkVar.get() == 1:
            messagebox.showinfo("Logged In", "You are logged in")
            return 
        else:
            messagebox.showerror("Error", "Something is wrong")
            return 
window = Window('SignUp',700,450).window
image = Image('./login.png',5,32).image
signUpImage = Label(window, image=image,compound='image').label
signUpImage.config(background='#49EBB6',padding=50)
signUpImage.pack(
    ipadx=0,
    ipady=0,
    expand=False,
    fill='both',
    side='left'
)
mainFrame = tk.Frame(window)
frame = tk.Frame(mainFrame)
signUpLable = Label(frame, text='SignUp').label
signUpLable.grid(column=0,row=0,sticky=tk.S)
fullNameImage = Image('./user.png').image
fullNameLable = Label(frame, image=fullNameImage, text='Full Name', compound='left').label
fullNameLable.grid(column=0,row=1,sticky=tk.W, pady=(10,0))
fullNameEntry = Entry(frame).entry
fullNameEntry.focus()
fullNameEntry.grid(column=0,row=2,sticky=tk.E)
emailImage = Image('./email.png').image
emailLable = Label(frame, image=emailImage, text='Email', compound='left').label
emailLable.grid(column=0,row=3,sticky=tk.W, pady=(10,0))
emailEntry = Entry(frame).entry
emailEntry.grid(column=0,row=4,sticky=tk.E)
passwordImage = Image('./password.png').image
passwordLable = Label(frame, image=passwordImage, text='Password', compound='left').label
passwordLable.grid(column=0,row=5,sticky=tk.W,pady=(10,0))
passwordEntry = Entry(frame,width=15,show='*').entry
passwordEntry.grid(column=0,row=6,sticky=tk.W)
passwordConfirmationImage = Image('./password.png').image
passwordConfirmationLable = Label(frame, image=passwordConfirmationImage, text='Confirmation', compound='left').label
passwordConfirmationLable.grid(column=0,row=5,sticky=tk.E,pady=(10,0))
passwordConfirmationEntry = Entry(frame,width=15,show='*').entry
passwordConfirmationEntry.grid(column=0,row=6,sticky=tk.E, padx=(30,0))
checkVar = tk.IntVar(value=0)
checkbutton = ttk.Checkbutton(frame,text='Being Agree to Term of service',  variable = checkVar)
checkbutton.grid(column=0,row=7,sticky=tk.W, pady=(10,0))
tk.Button(frame, width=45,height=2,fg='white',bg='#49EBB6',border=0,text='SignUp', command=signUpButtonOnClick).grid(column=0,row=8,sticky=tk.S, pady=(25,0))
frame.pack(expand=True)
mainFrame.pack(
    ipadx=10,
    ipady=0,
    expand=True,
    fill='both',
    side='right'
)
window.mainloop()

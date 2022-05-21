import tkinter as tk
from utils import *
from tkinter import ttk
from tkinter import messagebox
import re

class ImageButton(tk.Button):
    def __init__(self, master, image1, image2, *args, **kwargs):
        self.unclickedImage = image1
        self.clickedImage = image2
        super().__init__(master, *args, image = self.unclickedImage, **kwargs)
        self.toggleState = 1
        self.bind("<Button-1>", self.clickFunction)
    def clickFunction(self, event = None):
        if self.cget("state") != "disabled":
            self.toggleState *= -1
            if self.toggleState == -1:
                self.config(image = self.clickedImage)
            else:
                self.config(image = self.unclickedImage)
 def hideShowPassword():
    if(passwordEntry.cget('show') == ''):
        passwordEntry.config(show='*')
    else:
        passwordEntry.config(show='')
def loginButtonOnClick():
        if re.search(emailPattern, emailEntry.get()) and len(passwordEntry.get()) >= 10:
            messagebox.showinfo("Logged In", "You are logged in")
            return 
        else:
            messagebox.showerror("Error", "Something is wrong")
            return 
window = Window('Login',600,450).window

image = Image('./login.png',5,32).image
loginImage = Label(window, image=image,compound='image').label
loginImage.config(background='#49EBB6',padding=50)
loginImage.pack(
    ipadx=0,
    ipady=0,
    expand=False,
    fill='both',
    side='left'
)
mainFrame = tk.Frame(window)
frame = tk.Frame(mainFrame)
loginLable = Label(frame, text='Login').label
loginLable.grid(column=0,row=0,sticky=tk.S)
emailImage = Image('./email.png').image
emailLable = Label(frame, image=emailImage, text='Email', compound='left').label
emailLable.grid(column=0,row=1,sticky=tk.W, pady=(10,0))
emailEntry = Entry(frame).entry
emailEntry.focus()
emailEntry.grid(column=0,row=2,sticky=tk.W)
passwordImage = Image('./password.png').image
passwordLable = Label(frame, image=passwordImage, text='Password', compound='left').label
passwordLable.grid(column=0,row=3,sticky=tk.W,pady=(10,0))
passwordEntry = Entry(frame,width=25,show='*').entry
passwordEntry.grid(column=0,row=4,sticky=tk.W)
hidePasswordImage = Image('./hide.png').image
showPasswordImage = Image('./show.png').image
showPasswordButton = ImageButton(frame, image1=hidePasswordImage,image2=showPasswordImage, border=1, command=hideShowPassword)
showPasswordButton.place(x=270,y=126)
tk.Button(frame, width=45,height=2,fg='white',bg='#49EBB6',border=0,text='Login', command=loginButtonOnClick).grid(column=0,row=5,sticky=tk.S, pady=(25,0))
frame.pack(expand=True)
mainFrame.pack(
    ipadx=10,
    ipady=0,
    expand=True,
    fill='both',
    side='right'
)
window.mainloop()

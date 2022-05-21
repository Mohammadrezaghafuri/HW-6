import tkinter as tk
from tkinter import ttk

smallFont = ('consolas', 14)
emailPattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
class Window :
	def __init__(self, title,width, height):
			window = tk.Tk()
			screen_width = window.winfo_screenwidth()
			screen_height = window.winfo_screenheight()
			center_x = int(screen_width/2 - width / 2)
			center_y = int(screen_height/2 - height / 2)
			window.geometry(f'{width}x{height}+{center_x}+{center_y}')
			window.title(title)
			window.resizable(False, False)
			self.window = window
class Label:
	def __init__(self, root,image=None,text='',compound='none'):
		label = ttk.Label(root, image=image, text=text,compound=compound)
		label.config(font=smallFont)
		self.label = label

class Image :
	def __init__(self, url, zoom=1,subsample=24):
		image = tk.PhotoImage(file=url)
		image = image.zoom(zoom) 
		image = image.subsample(subsample)
		self.image = image

class Entry:
	def __init__(self, root, width=31,show=''):
		entry = tk.Entry(root,width=width,show=show,highlightthickness=1)
		entry.configure(highlightbackground="#E9EAEB", highlightcolor="#2FA6FF")
		entry.config(font=smallFont)
		self.entry = entry




				
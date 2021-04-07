import pyperclip
import pyshorteners
from tkinter import font
import tkinter as tk
...
root = tk.Tk()
...


root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url = StringVar()
url_addrerss = StringVar()

def urlshortener():
	urladdress  = url.get()
	url:short = pyshorteners.Shortener().tinyurl.short(urladdress)
	url_addrerss.set(url_short)

def copyurl():
	url_short = urladdress.get()
	pyperclip.copy(url_short)

label(root, text="My URL Shortener", font="Comic Sans MS").pack(pady=5)
entry(root, textvariable=url).pack(pady=5)
Button(root, text="generate Short Url", command=urlshortener).pack(pady=7)
entry(root, textvariable=url_addrerss).pack(pady=5)
Button(root, text="Copy URL", command = copyurl).pack(pady=5)

root.mainloop()
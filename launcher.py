import requests, io, zipfile, os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def install17():
    zipfile.ZipFile(io.BytesIO(requests.get("https://github.com/epimetheusgames/OGPC-Season-17/releases/download/test/OGPC17Exports.zip", stream=True).content)).extractall()

def run17():
    os.system("\"OGPC17Exports\\OGPC Season 17.exe\"")

def run17compat():
    os.system("\"OGPC17Exports\\OGPC Season 17.exe\" --rendering-driver opengl3")

root = Tk()
root.title("Epimetheus Launcher")

frame = ttk.Frame(root, padding=300)
frame.grid()

ttk.Label(frame, text="Epimetheus Launcher", font=("Arial", 25)).grid(column = 0, row = 0)
ttk.Label(frame, text="Launcher For Epimetheus Games' OGPC Projects", font=("Arial", 10)).grid(column = 0, row = 1)
ttk.Label(frame, text="", font=("Arial", 10)).grid(column = 0, row = 2)
ttk.Button(frame, text="Install OGPC 17", command = install17).grid(column = 0, row = 3)
ttk.Button(frame, text="Run OGPC 17", command = run17).grid(column = 0, row = 4)
ttk.Button(frame, text="Run OGPC 17 Efficiently", command = run17compat).grid(column = 0, row = 5)
root.mainloop()

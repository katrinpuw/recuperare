import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

root = tkinter.Tk()
root.title("Test")
root.minsize(width=500, height=400)
root.maxsize(width=1024, height=400)
text = tkinter.Text(root, width=400, height=400, wrap="word")

scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()

FILE_NAME = tkinter.NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
        messagebox.showinfo(message="File saved!")
    except Exception:
        showerror(title="Error", message="Saving file error....")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name

    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

menuBar = Menu(root)

fileMenu = Menu(menuBar, tearoff=False)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

menuBar.add_cascade(label="File", menu=fileMenu)

root.config(menu=menuBar)
root.mainloop()


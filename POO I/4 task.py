from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Interface test")
root.geometry("700x350")
frm = root.frame = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Open Explorer",
           command=filedialog.askopenfilename).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6)
root.mainloop()

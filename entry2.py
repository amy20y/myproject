from tkinter import *
from tkinter import ttk
root=Tk()
root.title("configration")
entry1=ttk.Entry(root,width=40)
entry1.pack()
button=ttk.Button(root,text="click here")
button.pack()
def butclick():
    print(entry1.get())
    f1=open("File","w+")
    f1.write(entry1.get())
    f1.close()
    entry1.delete(0,END)
button.config(command=butclick)
root.mainloop()
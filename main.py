from tkinter import *

root=Tk()
root.geometry("400x500")
root.resizable(False,False)
root.title("Calculator")
icon=PhotoImage(file="icons/calculator.png")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucia 30 bold")
screen.pack(fill=X,ipadx=10,pady=10,padx=10,ipady=10)
root.iconphoto(False,icon)
root.mainloop()
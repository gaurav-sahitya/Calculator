from tkinter import *

root=Tk()
root.resizable(False,False)
root.title("Calculator")
icon=PhotoImage(file="icons/calculator.png")
root.iconphoto(False,icon)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucia 30 bold",width=15)
screen.grid(row=0,columnspan=4,sticky=W+E,ipady=21,padx=5,ipadx=3)

l=[["C","(",")","÷"],["7","8","9","x"],["4","5","6","−"],["1","2","3","+"],[".","0","⬅","="]]

for i in range(5):
    for j in range(4):
        b=Button(root,text=l[i][j],font="lucia 21",width=5,height=3)
        b.grid(row=i+1,column=j)

root.mainloop()
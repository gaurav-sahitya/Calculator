from tkinter import *

def click(event):
    global scvalue,prev_key
    key=event.widget.cget("text")
    if prev_key=="=" and key.isdecimal():
        scvalue.set(key)
    elif key =="C":
        scvalue.set("")
    elif key=="=":
        try:
            if "xx" not in scvalue.get() and "//" not in scvalue.get():
                sval=scvalue.get()
                while sval[0]=="0" and sval[1].isdecimal():
                    sval=sval[1:]
                cal=eval(sval.replace("x", "*").replace("÷", "/").replace("−","-"))
                if int(cal)==cal:
                    cal=int(cal)
                scvalue.set(round(cal,12))
            else:
                scvalue.set("Error")
        except Exception as e:
            scvalue.set("Error")
    elif key=="⬅":
        scvalue.set(scvalue.get()[:-1])
    else:
        scvalue.set(scvalue.get()+key)
    screen.update()
    prev_key=key

prev_key=""

root=Tk()
root.resizable(False,False)
root.title("Calculator")
icon=PhotoImage(file="icons/calculator.png")
root.iconphoto(False,icon)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucia 30 bold",width=15,justify=RIGHT)
screen.grid(row=0,columnspan=4,sticky=W+E,ipady=21,padx=5,ipadx=3)

l=[["C","(",")","÷"],["7","8","9","x"],["4","5","6","−"],["1","2","3","+"],[".","0","⬅","="]]

for i in range(5):
    for j in range(4):
        b=Button(root,text=l[i][j],font="lucia 21",width=5,height=3)
        b.bind("<Button-1>",click)
        b.grid(row=i+1,column=j)

root.mainloop()
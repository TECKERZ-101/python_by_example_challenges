#Created By Isaac Clifton

from tkinter import *

def tablee_show():
    num=int(num_box.get())
    value=1
    for i in range (1,13):
        answer=i*num
        num_list.insert(END,(i, "x", num, "=", answer))
        value=value+1
    num_box.delete(0,END)
    num_box.focus()

def clear_list():
    num_box.delete(0,END)
    num_list.delete(0,END)
    num_box.focus()

window=Tk()
window.title=("Times Table - By Isaac")
window.geometry("400x280")

label1=Label(text="Enter a number: ")
label1.place(x=20, y=20, width=100, height=25)

"created by isaac"

num_box=Entry(text=0)
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

button1=Button(text="-> View Times Table <-", command=tablee_show)
button1.place(x=250, y=20, width=120, height=25)

num_list=Listbox()
num_list.place(x=120, y=50, width=100, height=200)

button2=Button(text="-> Clear <-", command=clear_list)
button2.place(x=250, y=50, width=120, height=25)

window.mainloop()

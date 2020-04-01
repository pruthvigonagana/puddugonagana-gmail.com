from tkinter import*
from tkinter import messagebox

def show():
 print(CheckVar1.get())
def sel():
 selection = "You selected the option " + str(CheckVar1.get())
 label.config(text = selection)

top = Tk()
CheckVar1 = IntVar()

C1 = Checkbutton(top, text = "option 1", variable = CheckVar1, \
 onvalue = 5, offvalue = 0, height=5, \
 width = 20, )
B1=Button(top,text="show",command=show)
C1.pack()
B1.pack()
b2=Button(top,text="exit",command=top.destroy)
b2.pack()
R1 = Radiobutton(top, text = "Option 2",variable = CheckVar1, value = 1,
 command = sel)
R1.pack()
label=Label(top)
label.pack()
top.mainloop()

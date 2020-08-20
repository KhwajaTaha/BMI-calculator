from tkinter import*
from tkinter import messagebox
top=Tk()
L1=Label(top,text="BMI calculator:")
L1.place(x=70,y=10)
L1=Label(top,text="Enter name")
L1.place(x=15,y=30)
E1=Entry(top,bd=5)
E1.place(x=90,y=30)
L2=Label(top,text=" Weight (kg)")
L2.place(x=15,y=60)
E2=Entry(top,bd=5)
E2.place(x=90,y=60)
L3=Label(top,text=" Height (m)")
L3.place(x=15,y=90)
E3=Entry(top,bd=5)
E3.place(x=90,y=90)


def helloCallBack():
    a=int(E2.get())
    b=int(E3.get())
    d=str(E1.get())
    c = a / (b ** 2)
    if c < 25:
        messagebox.showinfo((d), "is underweight")
    else:
        messagebox.showinfo((d),"is overweight")
    L4.configure(text=B)
B=Button(top,text="Show",command=helloCallBack)
B.place(x=100,y=150)
top.geometry("250*250")
top.mainloop()


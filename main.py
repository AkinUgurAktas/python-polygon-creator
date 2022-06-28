from tkinter import *
import turtle as trt
window = Tk()
window.title("POLYGON CREATOR !")
window.geometry("500x500")
tt=trt.Turtle()

tt.speed(0)
def f(x,y):

    x = int(x)
    y = int(y)


    angle = (180)-((y-2)*180/y)

    for i in range(y):
        tt.forward(x)
        tt.left(angle)




L1 = Label(window,text="LENGTH OF A EDGE")
L1.place(bordermode=OUTSIDE,height=30, width=120,x=0,y=50)
L2 = Label(window,text="EDGE OF POLYGON ?")
L2.place(bordermode=OUTSIDE,height=30, width=120,x=0,y=80)

E1 = Entry(window,)
E1.place(bordermode=OUTSIDE,height=30, width=120,x=120,y=50)
E2 = Entry(window,)
E2.place(bordermode=OUTSIDE,height=30, width=120,x=120,y=80)

B1 = Button(window, text="EDGES",relief="raised",command=lambda:f(E1.get(),E2.get()))
B1.place(bordermode=OUTSIDE, height=30, width=70,x=120,y=110)





window.mainloop()

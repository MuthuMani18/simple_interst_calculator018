from tkinter import *

window = Tk()
window.title("Interest Calculator")
window.geometry("400x360")
window.resizable(False,False)
def calculate():
    principal_info = int(entry1.get())
    interest_info = int(entry2.get())
    time_info = int(entry3.get())
    amount = (principal_info * interest_info * time_info)/100
    Label(window,text="Interest",font="impack 15 bold").place(x=30,y=210)
    Label(window,text=amount,font="impack 15 bold").place(x=175, y=210)

#heading
Label(window,text="simple Interest Calculator",font="impack 20 bold",bg="orange").pack(fill="x")

Label(window,text="Principle Amount",font="20").place(x=30,y=80)
Label(window,text="Interest Rate(%)",font="20").place(x=30,y=120)
Label(window,text="Time(Year)",font="20").place(x=30,y=160)

#Entry Box

entry1=Entry(window,font="15",width=15,bd=3)
entry1.place(x=175,y=80)

entry2=Entry(window,font="15",width=15,bd=3)
entry2.place(x=175,y=120)

entry3=Entry(window,font="15",width=15,bd=3)
entry3.place(x=175,y=160)

#Button
Button(window,text="Calculate",font="25",bg="green",fg="white",command=calculate).place(x=100,y=280)
Button(window,text="Exit",font="25",bg="red",fg="white",width=8,command=lambda:exit()).place(x=210,y=280)

mainloop()


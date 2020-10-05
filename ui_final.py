from tkinter import *
from ocr_final import ocr
from connect import db_add
root = Tk()
root.title("Car Parking")
frame = LabelFrame(root, text="Welcome to car parking lot",padx=50,pady=50)
frame.pack(padx=50,pady=50)


def park():
    top = Toplevel();
    frame_inner = LabelFrame(top, text="Welcome to Parking", padx=50, pady=50)
    frame_inner.pack(padx=50, pady=50)

    e = Entry(frame_inner, width=35, borderwidth=5)
    e.pack(padx=5, pady=10)


    def enter():
        top1 = Toplevel();
        frame_inner1 = LabelFrame(top1, text="", padx=50, pady=50)
        frame_inner1.pack(padx=50, pady=50)
        innerLabel=Label(frame_inner1, text="You parking spot is")
        innerLabel.pack()
        a = ocr(e.get())
        print(a)
        myLabel1 = Label(frame_inner1, text=db_add(ocr(e.get())))
        myLabel1.pack()

    button_enter = Button(frame_inner, text="Enter Car Number", padx=5, pady=10, command=enter)
    button_enter.pack()
    myLabel = Label(frame_inner, text=e.get())
    myLabel.pack()

def leave():
    top = Toplevel();
    frame_inner = LabelFrame(top, text="Thank you for Parking", padx=50, pady=50)
    frame_inner.pack(padx=50, pady=50)

    e = Entry(frame_inner, width=35, borderwidth=5)
    e.pack(padx=5, pady=10)

    def enter():
        top1 = Toplevel();
        frame_inner1 = LabelFrame(top1, text="", padx=50, pady=50)
        frame_inner1.pack(padx=50, pady=50)
        innerLabel = Label(frame_inner1, text="Please pay a amount of ")
        innerLabel.pack()
        myLabel1 = Label(frame_inner1, text=e.get())
        myLabel1.pack()

    button_enter = Button(frame_inner, text="Enter Car Number", padx=5, pady=10, command=enter)
    button_enter.pack()
    myLabel = Label(frame_inner, text=e.get())
    myLabel.pack()


button1 = Button(frame, text="Park ", command=park)
button2 = Button(frame, text="Leave", command=leave)

button1.pack(padx=5, pady=10)
button2.pack()

root.mainloop()


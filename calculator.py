from tkinter import *
def buttonclick(number):
    global value
    value=value+str(number)
    data.set(value)
def buttonclear():
    global value
    value=""
    data.set("")
def buttonequal():
    global value
    result=str(eval(value))
    data.set(result)   
root=Tk()
root.title("my calculator")
root.geometry("400x400")
value=""
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
b7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(7))
b7.grid(row=1,column=0)
b8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(8))
b8.grid(row=1,column=1)
b9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(9))
b9.grid(row=1,column=2)
b_addition=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick("+"))
b_addition.grid(row=1,column=3)

b4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(6))
b6.grid(row=2,column=2)
b_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick("-"))
b_sub.grid(row=2,column=3)

b3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(3))
b3.grid(row=3,column=0)
b2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(2))
b2.grid(row=3,column=1)
b1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(1))
b1.grid(row=3,column=2)
b_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick("*"))
b_mul.grid(row=3,column=3)

b_c=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=buttonclear)
b_c.grid(row=4,column=0)
b0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick(0))
b0.grid(row=4,column=1)
b_div=Button(root,text="%",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:buttonclick("%"))
b_div.grid(row=4,column=2)
b_equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=buttonequal)
b_equal.grid(row=4,column=3)
root.mainloop()
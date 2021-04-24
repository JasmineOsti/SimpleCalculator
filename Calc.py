from tkinter import*
from tkinter import Tk
from tkinter import Image

#Defining the working of button click
def btnpress(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

#Defining the working of button equals
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

#Defining the working of button display
def btnClearDisplay():
    global operator
    text_Input.set("")
    operator = ""

window = Tk()
window.title("Simple Calculator")
window.geometry("362x368")
operator =""
text_Input = StringVar()

txtDisplay = Entry(window , font=('calibri', 20, 'bold'),
                   textvariable = text_Input, bd=30, insertwidth=4, bg="grey", justify='right').grid(columnspan=4)

button_1=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20 , 'bold'), text="1", bg="white", command=lambda:btnpress(1)).grid(row=1, column=0)
button_2=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20 , 'bold'), text="2", bg="white", command=lambda:btnpress(2)).grid(row=1, column=1)
button_3=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20 , 'bold'), text="3", bg="white", command=lambda:btnpress(3)).grid(row=1, column=2)
Add=Button(window , padx=18, bd=8 , fg="black",font=('calibri', 20 , 'bold'), text="+", bg="white", command=lambda:btnpress("+")).grid(row=1, column=3)


button_4=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20, 'bold'), text="4", bg="white", command=lambda:btnpress(4)).grid(row=2, column=0)
button_5=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20, 'bold'), text="5", bg="white", command=lambda:btnpress(5)).grid(row=2, column=1)
button_6=Button(window , padx=18 , bd=8 , fg="black",font=('calibri', 20, 'bold'), text="6", bg="white", command=lambda:btnpress(6)).grid(row=2, column=2)
Sub=Button(window , padx=18, bd=8 , fg="black",font=('calibri', 20, 'bold'), text="-", bg="white", command=lambda:btnpress("-")).grid(row=2, column=3)


button_7=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="7", bg="white" , command=lambda:btnpress(7)).grid(row=3, column=0)
button_8=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="8", bg="white" , command=lambda:btnpress(8) ).grid(row=3, column=1)
button_9=Button(window , padx=18, bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="9", bg="white" , command=lambda:btnpresd(9)).grid(row=3, column=2)
Div=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="/", bg="white" , command=lambda:btnpress("/")).grid(row=3, column=3)


clear=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="C", bg="white" , command=btnClearDisplay ).grid(row=4, column=0)
button_0=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="0", bg="white" , command=lambda:btnpress(0)).grid(row=4, column=1)
Result=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="=", bg="white" , command=btnEqualsInput ).grid(row=4, column=2)
Mul=Button(window , padx=18 , bd=8 , fg="black" ,font=('calibri', 20 , 'bold'), text="*", bg="white" , command=lambda:btnpress("*")).grid(row=4, column=3)




window.mainloop()
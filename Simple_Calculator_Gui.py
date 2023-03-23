from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("349x470")

input_field = Entry(root, width=26, font=("arial", 17, "bold"), justify=RIGHT)

expresion = ""

def Click(btn):
    global expresion
    expresion += str(btn)
    input_field.delete(0, END)
    input_field.insert(0, str(expresion))   


def Clear():
    global expresion
    input_field.delete(0, END)
    expresion = ""


def Calculate():
	global expresion
    #input_field.delete(0, END)
	if expresion == "" :
		global input_field
		expresion = input_field.get()
		input_field.delete(0, END)
		input_field.insert(0, eval(str(expresion)))
	else :
		try:
			input_field.delete(0, END)
			input_field.insert(0, eval(str(expresion)))
		except:
			input_field.insert(0, "Value Error")
    
	expresion = ""




# creating items

button9 = Button(root, text="9", width=9, height=3,padx=9, pady=7,  bg="#222222", fg="#FFFFFF", command=lambda: Click(9))
button8 = Button(root, text="8", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(8))
button7 = Button(root, text="7", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(7))

button6 = Button(root, text="6", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(6))
button5 = Button(root, text="5", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(5))
button4 = Button(root, text="4", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(4))

button3 = Button(root, text="3", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(3))
button2 = Button(root, text="2", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(2))
button1 = Button(root, text="1", width=9,height=3, padx=9, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(1))

button0 = Button(root, text="0", width=18,height=3, padx=21, pady=7, bg="#222222", fg="#FFFFFF", command=lambda: Click(0))

button_point = Button(root, text=".", width=9,height=3 ,padx=9, pady=7,  bg="#434242", fg="#FFFFFF", command=lambda: Click("."))
button_AC = Button(root, text="C", width=9,height=3,padx=9, pady=7,  bg="#434242", fg="#FFFFFF", command=lambda: Clear())
button_dvid = Button(root, text="/", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click("/"))
button_add = Button(root, text="+", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click("+"))
button_sub = Button(root, text="-", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click("-"))
button_malti = Button(root, text="x", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click("*"))
button_Lpri = Button(root, text="(", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click("("))
button_Rpri = Button(root, text=")", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Click(")"))
button_equal = Button(root, text="=", width=9,height=3, padx=9, pady=7, bg="#434242", fg="#FFFFFF", command=lambda: Calculate())




# griding items

input_field.grid(row=0, column=0,columnspan=4, ipady=39)


button_AC.grid(row=1, column=0)
button_Lpri.grid(row=1, column=1)
button_Rpri.grid(row=1, column=2)
button_dvid.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_malti.grid(row=2, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button0.grid(row=5, column=0, columnspan=2)
button_point.grid(row=5, column=2)
button_equal.grid(row=5, column=3)





root.mainloop()

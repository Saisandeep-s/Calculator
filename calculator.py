from tkinter import *

root = Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title('CALCULATOR')

expression = ""

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

input_text = StringVar()
input_frame = Frame(root, width=312, height=50, bd=0, highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for label in buttons:
    if label == '=':
        Button(btns_frame, text=label, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_equal).grid(row=row_val, column=col_val, padx=1, pady=1)
        col_val += 1
    else:
        Button(btns_frame, text=label, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda label=label: btn_click(label)).grid(row=row_val, column=col_val, padx=1, pady=1)
        col_val += 1
    
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

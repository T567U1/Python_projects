import tkinter as tk
root = tk.Tk()
root.title('Calculator')
root.geometry("400x400")
table = tk.Entry(root, font = 24,  width = 30, borderwidth = 5)
table.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)

def buttom_click(val):
    curr = table.get()
    table.delete(0, 30)
    table.insert(0, curr + str(val))
    return

def clear_():
    table.delete(0, 30)
    return

def plus_():
    global num1, simbol
    simbol = '+'
    num1 = table.get()
    table.delete(0, 30)
    return

def minus_():
    global num1, simbol
    simbol = '-'
    num1 = table.get()
    table.delete(0, 30)
    return

def mul_():
    global num1, simbol
    simbol = '*'
    num1 = table.get()
    table.delete(0, 30)
    return

def div_():
    global num1, simbol
    simbol = '/'
    num1 = table.get()
    table.delete(0, 30)
    return

def equals_():
    global str
    curr = table.get()
    table.delete(0, 30)
    if simbol == '+':
        table.insert(0, str(int(num1) + int(curr)))
    if simbol == '-':
        table.insert(0, str(int(num1) - int(curr)))
    if simbol == '*':
        table.insert(0, str(int(num1) * int(curr)))
    if simbol == '/':
        table.insert(0, str(int(num1) / int(curr)))
    return

#grid
buttom_0 = tk.Button(root, text = '0', padx = 40, pady = 20, command = lambda: buttom_click(0))
buttom_1 = tk.Button(root, text = '1', padx = 40, pady = 20, command = lambda: buttom_click(1))
buttom_2 = tk.Button(root, text = '2', padx = 40, pady = 20, command = lambda: buttom_click(2))
buttom_3 = tk.Button(root, text = '3', padx = 40, pady = 20, command = lambda: buttom_click(3))
buttom_4 = tk.Button(root, text = '4', padx = 40, pady = 20, command = lambda: buttom_click(4))
buttom_5 = tk.Button(root, text = '5', padx = 40, pady = 20, command = lambda: buttom_click(5))
buttom_6 = tk.Button(root, text = '6', padx = 40, pady = 20, command = lambda: buttom_click(6))
buttom_7 = tk.Button(root, text = '7', padx = 40, pady = 20, command = lambda: buttom_click(7))
buttom_8 = tk.Button(root, text = '8', padx = 40, pady = 20, command = lambda: buttom_click(8))
buttom_9 = tk.Button(root, text = '9', padx = 40, pady = 20, command = lambda: buttom_click(9))

buttom_plus = tk.Button(root, text = '+', padx = 39, pady = 20, command = plus_)
buttom_minus = tk.Button(root, text = '-', padx = 39, pady = 20, command = minus_)
buttom_mul = tk.Button(root, text = '*', padx = 39, pady = 20, command = mul_)
buttom_div = tk.Button(root, text = '/', padx = 39, pady = 20, command = div_)

buttom_clear = tk.Button(root, text = 'clear', padx = 85, pady = 20, command = clear_)
buttom_equals = tk.Button(root, text = '=', padx = 145, pady = 20, command = equals_)

#num buttoms
buttom_0.grid(row = 4, column = 0)

buttom_1.grid(row = 3, column = 0)
buttom_2.grid(row = 3, column = 1)
buttom_3.grid(row = 3, column = 2)

buttom_4.grid(row = 2, column = 0)
buttom_5.grid(row = 2, column = 1)
buttom_6.grid(row = 2, column = 2)

buttom_7.grid(row = 1, column = 0)
buttom_8.grid(row = 1, column = 1)
buttom_9.grid(row = 1, column = 2)

#operation buttons
buttom_plus.grid(row = 1, column = 4)
buttom_minus.grid(row = 2, column = 4)
buttom_mul.grid(row = 3, column = 4)
buttom_div.grid(row = 4, column = 4)

buttom_clear.grid(row = 4, column = 1, columnspan = 2)
buttom_equals.grid(row = 5, column = 0, columnspan = 3)

root.mainloop()

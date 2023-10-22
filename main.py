from tkinter import *
import keyboard

root = Tk()
root.title("Calculator")


e = Entry(root, width = 20, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady= 10)

def bClick(number):
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current) + str(number))

def bClear():
  e.delete(0, END)

def bAdd():
  first_number = e.get()
  global f_num
  global math
  math = "addition"
  f_num = int(first_number)
  e.delete(0, END)

def bsubtract():
  first_number = e.get()
  global f_num
  global math
  math = "subtract"
  f_num = int(first_number)
  e.delete(0, END)

def bmultiply():
  first_number = e.get()
  global f_num
  global math
  math = "Multiply"
  f_num = int(first_number)
  e.delete(0, END)
  
def bdivide():
  first_number = e.get()
  global f_num
  global math
  math = "division"
  f_num = int(first_number)
  e.delete(0, END)

def bEqual():
  s_num = e.get()
  e.delete(0, END)
  
  if math == "addition":
    e.insert(0, f_num + int(s_num))

  elif math == "subtract":
    e.insert(0, f_num - int(s_num))

  elif math == "Multiply":
    e.insert(0, f_num * int(s_num))

  elif math == "division":
    e.insert(0, f_num / int(s_num))

def DCM():
    k = Label(root, text = "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n").grid(row = 0, column = 0)


b1 = Button(root, text="1", padx = 35, pady = 20, bg = "white", command =lambda: bClick(1)).grid(row = 4, column = 0)


b2 = Button(root, text="2", padx = 35, pady = 20, bg = "white", command =lambda: bClick(2)).grid(row = 4, column = 1)
b3 = Button(root, text="3", padx = 35, pady = 20, bg = "white", command = lambda: bClick(3)).grid(row = 4, column = 2)
b4 = Button(root, text="4", padx = 35, pady = 20, bg = "white", command = lambda: bClick(4)).grid(row = 3, column = 0)
b5 = Button(root, text="5", padx = 35, pady = 20, bg = "white", command = lambda: bClick(5)).grid(row = 3, column = 1)
b6 = Button(root, text="6", padx = 35, pady = 20, bg = "white", command =lambda: bClick(6)).grid(row = 3, column = 2)
b7 = Button(root, text="7", padx = 35, pady = 20, bg = "white", command = lambda: bClick(7)).grid(row = 2, column = 0)
b8 = Button(root, text="8", padx = 35, pady = 20, bg = "white", command = lambda: bClick(8)).grid(row = 2, column = 1)
b9 = Button(root, text="9", padx = 35, pady = 20, bg = "white", command = lambda: bClick(9)).grid(row = 2, column = 2)
b0 = Button(root, text="0", padx = 35, pady = 20, bg = "white", command = lambda: bClick(0)).grid(row = 1, column = 0)
bAdd = Button(root, text = "+", padx = 35, pady=20, bg = "white", command = bAdd).grid(row = 1, column = 1)
bSubtract = Button(root, text = "-", padx = 35, pady = 20, bg = "white", command = bsubtract).grid(row = 1, column = 2)
bMultiply = Button(root, text = "×", padx = 35, pady = 20, bg = "white", command = bmultiply).grid(row = 2, column = 3)
bDivide = Button(root, text = "÷", padx = 35, pady = 20, bg = "white", command = bdivide).grid(row = 3, column = 3)
bEquals = Button(root, text = "=", padx = 35, pady = 20, bg = "white", command = bEqual).grid(row = 1, column = 3)
bAC = Button(root, text = "AC", padx = 35, pady = 20, bg = "white", command = lambda: bClear()).grid(row = 4, column = 3)
bDCM = Button(root, text = "Don't click me", padx= 50, pady = 20, bg = "white", command =DCM).grid(row = 4, column = 4)
 
root.mainloop()
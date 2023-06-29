from tkinter import * 
from decimal import *
from math import sin, cos, tan
import sqlite3 as db
import os

def extra_page(text_, name):
    """for show notfication of success or error"""
    win = Tk()
    win.geometry("%dx%d+%d+%d" % (500, 100, 100, 100))
    win.title(name)
    t = Label(win, text= text_, font= "tahoma 15 normal")
    t.place(x = 50, y = 10)
    b = Button(win, text= "Ok", font= "tahoma 15 normal", command= win.destroy)
    b.place(x = 230, y = 50)
    win.mainloop()

def tablee(lst, name):
    """shows that item in the table shape"""
    win = Tk()
    win.title(name)
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            e = Entry(win, width= 10,font= "tahom 12 normal")
            e.grid(row=i, column=j)
            e.insert(END, lst[i][j])
    win.mainloop()

class Databasee():
    def __init__(self):
        if os.path.exists("e://a//calc.db") != True:
            """creat data base"""
            con = db.connect("e://a//calc.db")
            c =con.cursor ()
            c.execute("create table Calculate(phrase text primary key, result floating)")
            con.commit()
            con.close()
        else:
            pass
    @staticmethod
    def save(phr, re):
        """save history of calc in database"""
        con = db.connect("e://a//calc.db")
        c =con.cursor ()
        c.execute("insert into Calculate values ('{}', {})".format(phr, re))
        con.commit()
        con.close()
    @staticmethod
    def show():
        try:
            '''all element from the database that shown'''
            con = db.connect("e://a//calc.db")
            c = con.cursor()
            c.execute("select * from Calculate")
            q = c.fetchall()
            con.commit()
            con.close()
            print(q)
            tablee(q, "history")
        except:
            extra_page("the data base doest have a history recorded", "error")
    @staticmethod
    def clear():
        try:
            '''clear data base'''
            con = db.connect("e://a//calc.db")
            c = con.cursor()
            c.execute("select * from Calculate")
            q = c.fetchall()
            ph, re = zip(*(q))
        
            for i in (ph):
                print(i)
                c.execute("delete from Calculate where phrase = '{}'".format(i))
            con.commit()
            con.close()
            extra_page("                    the history clear", "success")
        except:
            extra_page("                the history was clearing", "error")

class Stack():
    def __init__(self):
        self.s = []
    def push(self, data):
        """ add item to stack"""
        self.s.append(data)
    def pop(self):
        """ remove item from last of stack"""
        self.s.pop()
    def peek(self):
        "shows the last item in stack if stack is empity nothing do"
        if len(self.s) < 1:
            return 
        return self.s[-1]
    def join(self):
        '''for convert stack to str'''
        self.st = [str(i) for i in self.s]
        return "".join(self.st)

    def isenpity(self):
        """check the stack is emipity of not"""
        return self.s == []

    def make_empit(self):
        """clear stack or make empity"""
        self.s.clear()

    def slicing(self):
        """for control than . because we dont have this the user can input 99.99.0 if the come at first of middle"""
        self.especial = ["(", "+", "-", "/", "*"]
        self.ind = [self.s.index(i) for i in self.s if i in self.especial]
        print(self.ind)
        if len(self.ind) < 1:
            self.l = self.s[:]
        elif len(self.ind) > 1:
            self.l = self.s[self.ind[-1]:]
        if "." in self.l:
            return False
        return True


s = Stack()
parantez = 0



"""there are after click bottom will be happen"""
def clear():
    '''clear the entery'''
    v1.set("")
    v.set("")
    s.make_empit()

def sin_():
    """control that after sin must be come + - / *"""
    if s.peek() not in (")", ".", "sin", "cos", "tan", "1/tan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        s.push("sin")
        v1.set(s.join())
    pass


def cos_():
    """control that after cos must be come + - / *"""
    if s.peek() not in (")", ".", "sin", "cos", "tan", "1/tan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        s.push("cos")
        v1.set(s.join())
    pass

def tan_():
    """control that after tan must be come + - / *"""
    if s.peek() not in (")", ".", "sin", "cos", "tan", "1/tan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        s.push("tan")
        v1.set(s.join())
    pass

def cot_():
    """control that after cot must be come + - / *"""
    if s.peek() not in (")", ".", "sin", "cos", "tan", "1/tan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
        s.push("1/tan")
        v1.set(s.join())
    pass

def back():
    """remove the last item from statck and then make clear result entry """
    if s.isenpity() == True:
        return
    s.pop()
    v1.set(s.join())   
    v.set("")

def mult():
    """control that can comes afrer numers and )"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", "*", "+", "-", "/", "(") and s.isenpity() == False:
        s.push("*")
        v1.set(s.join())
    pass

def divi():
    """control that can comes afrer numers and )"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", "*", "+", "-", "/", "(") and s.isenpity() == False:
        s.push("/")
        v1.set(s.join())   
    pass

def subc():
    """control that can comes afrer numers and )"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", "*", "+", "-", "/", "(") and s.isenpity() == False:
        s.push("-")
        v1.set(s.join())

def plus():
    """control that can comes afrer numers and )"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", "*", "+", "-", "/", "(") and s.isenpity() == False:
        s.push("+")
        v1.set(s.join())
    pass

def negative():
    """for write negative number that method control that in can comes after ("""
    if s.peek() == "(":
        s.push("-")
        v1.set(s.join())
    pass

def dot():
    """shows that the . as make float number can come after numbers"""
    if s.peek() in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and s.slicing() == True:
        s.push(".")
        v1.set(s.join())
    pass

def zero():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")") and s.isenpity() == False:
        s.push(0)
        v1.set(s.join())
    pass

def one():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(1)
        v1.set(s.join())
    pass

def tow():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(2)
        v1.set(s.join())
    pass

def three():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(3)
        v1.set(s.join())
    pass

def four():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(4)
        v1.set(s.join())
    pass

def five():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(5)
        v1.set(s.join())
    pass

def six():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(6)
        v1.set(s.join())
    pass

def seven():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(7)
        v1.set(s.join())
    pass

def eight():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(8)
        v1.set(s.join())
    pass

def nine():
    """shows that the numbers can comes after numbers and + - * /"""
    if s.peek() not in ("sin", "cos", "tan", "1/tan", ")"):
        s.push(9)
        v1.set(s.join())
    pass

def paran():
    """shows that the parantez can comes at the first and after + - * / sin cos tan cot"""
    global parantez
    if parantez == 0 and (s.peek() in ("+", "-", "/", "*", "sin", "cos", "tan", "1/tan") or s.isenpity() == True):
        s.push("(")
        parantez = 1
    elif parantez == 1 and s.peek() in (1, 2, 3, 5, 4, 6, 7, 8, 9, 0, ")"):
        s.push(")")
        parantez = 0
    v1.set(s.join())

def equl():
        """shows that when we comprees = buttum do every math plrase if fhrase have some ploblem will be write teh except part"""
        """and save in data base"""
    # try:
        if s.isenpity() == True:
            return
        ph = s.join()
        re = Decimal(eval(ph))
        v.set(format(re,  '.6e'))
        ob = Databasee()
        ob.save(ph, re)
    # except:
    #     v.set("there is sth wrong!")

w = Tk()
w.geometry("%dx%d+%d+%d" % (400, 400, 100, 100))
w.title("calculater")


v = StringVar()
e = Entry(textvariable= v, font= "tahoma 20 normal", state= "disable")
e.place(x = 50, y = 70, width= 300, height= 40)

b_history = Button(text= "history", command= Databasee.show , font= "tahoma 15 normal")
b_history.place(x = 80, y = 340)

b_h_clear = Button(text= "clear history", command= Databasee.clear , font= "tahoma 15 normal")
b_h_clear.place(x = 170, y = 340)

v1 = StringVar()
e1 = Entry(textvariable= v1, font= "tahoma 20 normal", state= "disable")
e1.place(x = 50, y = 20, width= 300, height= 40)



b1 = Button(text= "C", command= clear, font= "tahoma 15 normal", bg= "red", fg= "white", width= 3)
b1.place(x = 50, y = 130)

b2 = Button(text= "sin", command= sin_, font= "tahoma 15 normal", bg= "light gray", width= 3)
b2.place(x = 100, y = 130)

b3 = Button(text= "cos", command= cos_, font= "tahoma 15 normal", bg= "light gray", width= 3)
b3.place(x = 150, y = 130)

b4 = Button(text= "tan", command= tan_, font= "tahoma 15 normal", bg= "light gray", width= 3)
b4.place(x = 200, y = 130)

b5 = Button(text= "cot", command= cot_, font= "tahoma 15 normal", bg= "light gray", width= 3)
b5.place(x = 250, y = 130)

b6 = Button(text= "X", command= back, font= "tahoma 15 normal", bg= "light blue", width= 3)
b6.place(x = 300, y = 130)

b7 = Button(text= "*", command= mult, font= "tahoma 15 normal", bg= "light gray", width= 3)
b7.place(x = 300, y = 180)

b8 = Button(text= "/", command= divi, font= "tahoma 15 normal", bg= "light gray", width= 3)
b8.place(x = 250, y = 180)

b9 = Button(text= "-", command= subc, font= "tahoma 15 normal", bg= "light gray", width= 3)
b9.place(x = 200, y = 180)

b10 = Button(text= "+", command= plus, font= "tahoma 15 normal", bg= "light gray", width= 3)
b10.place(x = 150, y = 180)

b12 = Button(text= "+/-", command= negative, font= "tahoma 15 normal", bg= "light gray", width= 3)
b12.place(x = 100, y = 180)

b11 = Button(text= "=", command= equl, font= "tahoma 15 normal", bg= "light green", width= 3)
b11.place(x = 50, y = 180)

b13  = Button(text= ".", command= dot, font= "tahoma 15 normal", bg= "light gray", width= 3)
b13.place(x = 50, y = 230)

b14  = Button(text= "0", command= zero , font= "tahoma 15 normal", bg= "light gray", width= 3)
b14.place(x = 100, y = 230)

b15 = Button(text= "1", command= one, font= "tahoma 15 normal", bg= "light gray", width= 3)
b15.place(x = 150, y = 230)

b16 = Button(text= "2", command= tow, font= "tahoma 15 normal", bg= "light gray", width= 3)
b16.place(x = 200, y = 230)

b17 = Button(text= "3", command= three, font= "tahoma 15 normal", bg= "light gray", width= 3)
b17.place(x = 250, y = 230)

b18 = Button(text= "4", command= four, font= "tahoma 15 normal", bg= "light gray", width= 3)
b18.place(x = 300, y = 230)


b20  = Button(text= "5", command= five, font= "tahoma 15 normal", bg= "light gray", width= 3)
b20.place(x = 50, y = 280)

b21  = Button(text= "6", command= six , font= "tahoma 15 normal", bg= "light gray", width= 3)
b21.place(x = 100, y = 280)

b22 = Button(text= "7", command= seven, font= "tahoma 15 normal", bg= "light gray", width= 3)
b22.place(x = 150, y = 280)

b23 = Button(text= "8", command= eight, font= "tahoma 15 normal", bg= "light gray", width= 3)
b23.place(x = 200, y = 280)

b24 = Button(text= "9", command= nine, font= "tahoma 15 normal", bg= "light gray", width= 3)
b24.place(x = 250, y = 280)

b25 = Button(text= "()", command= paran, font= "tahoma 15 normal", bg= "light gray", width= 3)
b25.place(x = 300, y = 280)

w.mainloop()

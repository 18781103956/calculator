import tkinter
from tkinter import *
import comUI2


class Compute(comUI2.ComputorFunc):
    def __init__(self):
        self.win = tkinter.Tk()
        # 创建一个变量
        self.show = tkinter.StringVar()
        # 输入列表
        self.list = []
        self.centerUi()
        self.buttonCompute()
        self.win.mainloop()

    def centerUi(self):
        win_width = 355
        win_height = 415
        # 获取屏幕尺寸
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        # 获取窗口在屏幕的位置
        x = (screenwidth - win_width)/2
        y = (screenheight - win_height)/2
        alignstr = '%dx%d+%d+%d' % (win_width, win_height, (screenwidth - win_width) / 2, (screenheight - win_height) / 2)
        self.win.geometry(alignstr)
        self.win.title("计算器")
        self.win.wm_resizable(width=False, height=False)
        # 设置计算器窗口图标
        self.win.iconbitmap('C.ico')

    def buttonCompute(self):
        self.in_entry = tkinter.Entry(self.win, bg='#FCF4F0', bd=3, font=("宋体", 30), textvariable=self.show)
        self.in_entry.place(x=15, y=15, width=325, height=80)

        clear_button = tkinter.Button(self.win, bg='#5B7FA7', text='Clear', command=lambda: (self.showClear()))
        clear_button.place(x=15, y=110, width=70, height=50)
        back_button = tkinter.Button(self.win, bg='#C8CDFF', text='Back', command=lambda: (self.showBack()))
        back_button.place(x=100, y=110, width=70, height=50)
        button1 = tkinter.Button(self.win, bg='gray', text='(', command=lambda: (self.symbol_1()))
        button1.place(x=185, y=110, width=70, height=50)
        button2 = tkinter.Button(self.win, bg='gray', text='/', command=lambda: (self.symbol_2()))
        button2.place(x=270, y=110, width=70, height=50)

        button3 = tkinter.Button(self.win, bg='gray', text='7', command=lambda: (self.seven()))
        button3.place(x=15, y=170, width=70, height=50)
        button4 = tkinter.Button(self.win, bg='gray', text='8', command=lambda: (self.eight()))
        button4.place(x=100, y=170, width=70, height=50)
        button5 = tkinter.Button(self.win, bg='gray', text='9', command=lambda: (self.nine()))
        button5.place(x=185, y=170, width=70, height=50)
        button6 = tkinter.Button(self.win, bg='gray', text='*', command=lambda: (self.symbol_3()))
        button6.place(x=270, y=170, width=70, height=50)

        button7 = tkinter.Button(self.win, bg='gray', text='4', command=lambda: (self.four()))
        button7.place(x=15, y=230, width=70, height=50)
        button8 = tkinter.Button(self.win, bg='gray', text='5', command=lambda: (self.five()))
        button8.place(x=100, y=230, width=70, height=50)
        button9 = tkinter.Button(self.win, bg='gray', text='6', command=lambda: (self.six()))
        button9.place(x=185, y=230, width=70, height=50)
        button10 = tkinter.Button(self.win, bg='gray', text='-', command=lambda: (self.symbol_4()))
        button10.place(x=270, y=230, width=70, height=50)

        button11 = tkinter.Button(self.win, bg='gray', text='1', command=lambda: (self.one()))
        button11.place(x=15, y=290, width=70, height=50)
        button12 = tkinter.Button(self.win, bg='gray', text='2', command=lambda: (self.two()))
        button12.place(x=100, y=290, width=70, height=50)
        button13 = tkinter.Button(self.win, bg='gray', text='3', command=lambda: (self.three()))
        button13.place(x=185, y=290, width=70, height=50)
        button14 = tkinter.Button(self.win, bg='gray', text='+', command=lambda: (self.symbol_5()))
        button14.place(x=270, y=290, width=70, height=50)

        button15 = tkinter.Button(self.win, bg='gray', text=')', command=lambda: (self.symbol_7()))
        button15.place(x=15, y=350, width=70, height=50)
        button16 = tkinter.Button(self.win, bg='gray', text='0', command=lambda: (self.zero()))
        button16.place(x=100, y=350, width=70, height=50)
        button17 = tkinter.Button(self.win, bg='gray', text='.', command=lambda: (self.symbol_6()))
        button17.place(x=185, y=350, width=70, height=50)
        button18 = tkinter.Button(self.win, bg='#C8CDFF', text='=', command=lambda: (self.result()))
        button18.place(x=270, y=350, width=70, height=50)

    def showClear(self):
        self.in_entry.delete(0, END)
        self.list.clear()

    def showBack(self):
        if len(self.list) == 0:
            pass
        else:
            self.in_entry.delete(len(self.list)-1, END)
            del self.list[-1]

    def one(self):
        self.list.insert(len(self.list), 1)
        self.in_entry.insert(INSERT, "1")

    def two(self):
        self.list.insert(len(self.list), 2)
        self.in_entry.insert(INSERT, "2")

    def three(self):
        self.list.insert(len(self.list), 3)
        self.in_entry.insert(INSERT, "3")

    def four(self):
        self.list.insert(len(self.list), 4)
        self.in_entry.insert(INSERT, "4")

    def five(self):
        self.list.insert(len(self.list), 5)
        self.in_entry.insert(INSERT, "5")

    def six(self):
        self.list.insert(len(self.list), 6)
        self.in_entry.insert(INSERT, "6")

    def seven(self):
        self.list.insert(len(self.list), 7)
        self.in_entry.insert(INSERT, "7")

    def eight(self):
        self.list.insert(len(self.list), 8)
        self.in_entry.insert(INSERT, "8")

    def nine(self):
        self.list.insert(len(self.list), 9)
        self.in_entry.insert(INSERT, "9")

    def zero(self):
        self.list.insert(len(self.list), 0)
        self.in_entry.insert(INSERT, "0")

    def symbol_1(self):
        # if self.islegal():
        self.list.insert(len(self.list), '(')
        self.in_entry.insert(INSERT, '(')

    def symbol_2(self):
        L = len(self.list)
        if self.islegal():
            self.list.insert(len(self.list), '/')
            self.in_entry.insert(INSERT, "/")

    def symbol_3(self):
        L = len(self.list)
        if self.islegal():
            self.list.insert(len(self.list), '*')
            self.in_entry.insert(INSERT, "*")

    def symbol_4(self):
        L = len(self.list)
        if self.islegal():
            self.list.insert(len(self.list), '-')
            self.in_entry.insert(INSERT, "-")

    def symbol_5(self):
        L = len(self.list)
        if self.islegal():
            self.list.insert(len(self.list), '+')
            self.in_entry.insert(INSERT, "+")

    def symbol_6(self):
        if self.islegal():
            self.list.insert(len(self.list), '.')
            self.in_entry.insert(INSERT, ".")

    def symbol_7(self):
        # if self.islegal():
        self.list.insert(len(self.list), ')')
        self.in_entry.insert(INSERT, ')')

    def isdigit(self, c):
        if c == '0' or c == '1' or c == '2' or c == '3' or c == '4'or c == '5'or c == '6'or c == '7'or c == '8'or c == '9':
            return True
        return False

    def isSymbol(self, c):
        # if ((c == '(') or (c == ')')):
            # return True
        if c == '+':
            return True
        elif c == '-':
            return True
        elif c == '*':
            return True
        elif c == '/':
            return True
        elif c == '%':
            return True
        elif c == '.':
            return True
        return False

    def islegal(self):
        L = len(self.list)
        if L == 0:
            return False
        elif self.isdigit(self.list[L-1]):
            return False
        elif self.isSymbol(self.list[L-1]):
            return False
        else:
            return True
    def result(self):
        expr = ""
        for item in self.list:
            expr = expr + str(item)
        ans = self.runComputor(expr)
        self.showClear()
        for i in str(ans):
            if self.isdigit(i):
                self.list.append(int(i))
            else:
                self.list.append(i)
        self.in_entry.insert(INSERT, ans)
        print(ans)


if __name__ == '__main__':
    Compute()
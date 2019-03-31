import tkinter as tk

class Stack:
    def __init__(self):
        self.s=[]

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty(): print("Empty Stack")
        else:
            return self.s.pop(-1)

    def peek(self):
        if self.isEmpty() == False :
            return self.s[-1]
        else :
            return None

    def isEmpty(self):
        if len(self.s)>0:
            return False
        else :
            return True

    def size(self):
        return len(self.s)

    def print(self):
        print(self.s)


def eqCheck(eq):
    """
    :param eq: str 형 equation
    :return: T/F
    """
    s=Stack()
    for i in range(len(eq)):
        if i == "(" :
            s.push(eq[i])
        elif i == ")" :
            if s.isEmpty() : return False
            s.pop()
        if s.isEmpty():
            return True
        else :
            return False


def isOper(item):

    if item == '+' or item == '-' or item == '*' or item =='/':
        return True
    else :
        return False

def isNum(s):
    try :
        float(s)
        return True
    except ValueError :
        return False

def posEq(eq):
    """
    :param eq: str형 띄어쓰기로 구분된 equation
    :return: 후입표기식 equation list
    """
    eqList= eq.split(" ")
    s=Stack()
    posteq=[]
    for item in eqList:

        if item == "(":
            s.push(item)

        elif item == ")" :
            while True:
                _tmp= s.pop()
                if _tmp != "(" :
                    posteq.append(_tmp)
                else :
                    break
        elif item == '+' or item == '-' :
            while isOper(s.peek()) == True :
                posteq.append(s.pop())
            s.push(item)

        elif item == "*" or item == "/" :
            while s.peek() == "*" or s.peek() == "/" :
                posteq.append(s.pop())
            s.push(item)

        elif isNum(item) :
            posteq.append(item)

    while s.isEmpty() == False :
        posteq.append(s.pop())

    return posteq

def calEq(eq):
    """
    :param eq: 후입처리된 연산
    :return: result(scalar)
    """
    s = Stack()
    for item in eq :
        if not isOper(item) :
            s.push(item)
        else :
            num1 = float(s.pop())
            num2 = float(s.pop())
            print( num1, num2)
            if item == "+" : s.push(str(num2 + num1))
            elif item == "-" : s.push(str(num2 - num1))
            elif item == "*": s.push(str(num2 * num1))
            elif item == "/": s.push(str(num2 / num1))
    return s.pop()

class Window:
    def __init__(self):
        window = tk.Tk()
        window.title("Simple Calc")

        f1 = tk.Frame(window, relief="solid", bd=2, padx=2, pady=2)
        f2 = tk.Frame(window, relief="solid", bd=2, padx=2, pady=2)

        # Frame 1
        self.eq = "0"
        large_font = ('Verdana',21)
        self.entryVar = tk.StringVar(value=self.eq)

        eqEntry = tk.Entry(f1, bg="yellow", width=11, textvariable=self.entryVar,font=large_font, justify='right')
        delButton = tk.Button(f1, text="del", height=2, width=6, command=self.delete)
        eqEntry.pack(side=tk.LEFT, padx=4)
        delButton.pack(side=tk.LEFT, padx=0)

        # Frame 2
        buttonList = ["7","8","9","+","c",
                      "4","5","6","-","(",
                      "1","2","3","*",")",
                      "0",".","=","/"," "]

        rowIdx=0
        colIdx=0

        butList=[None] * 20
        i = 0

        for btn in buttonList:
            butList[i] = tk.Button(f2, text=btn, height=3, width=6, command=(lambda char=btn: self.butEvent(char)))
            butList[i].grid(row=rowIdx, column=colIdx)
            if btn==" ": butList[i]['state'] = 'disabled'
            i += 1
            colIdx += 1
            if colIdx > 4:
                colIdx = 0
                rowIdx += 1

        f1.pack(pady=2)
        f2.pack()

        window.mainloop()

    def butEvent(self,key):
        if key=="c":
            self.eq="0"
        elif key=="=":
            if self.eqCheck(self.eq) == True :
                self.eq = self.calEq(self.posEq(self.eq))
            else :
                print(" Wrong Equation !")
        else:
            if self.eq=="0":
                self.eq = key
            else:
                self.eq += key

        self.entryVar.set(self.eq)

    def delete(self):
        self.eq = self.eq[0:len(self.eq)-1]
        if len(self.eq)==0: eq = "0"
        self.entryVar.set(self.eq)

    def eqCheck(self,eq):
        """
        :param eq: str 형 equation
        :return: T/F
        """
        s = Stack()
        for i in range(len(eq)):
            if i == "(":
                s.push(eq[i])
            elif i == ")":
                if s.isEmpty(): return False
                s.pop()
            if s.isEmpty():
                return True
            else:
                return False

    def posEq(self, eq):
        """
        :param eq: str형 equation
        :return: 후입표기식 equation list
        """
        eq_sign = ['+', '-', '/', "*", "(", ")"]
        eqList = []
        j=0
        for i in range(len(eq)) :
            if eq[i] in eq_sign :
                eqList.append(eq[j:i])
                eqList.append(eq[i])
                j=i+1
        eqList.append(eq[j:])
        s = Stack()
        posteq = []
        for item in eqList:

            if item == "(":
                s.push(item)

            elif item == ")":
                while True:
                    _tmp = s.pop()
                    if _tmp != "(":
                        posteq.append(_tmp)
                    else:
                        break
            elif item == '+' or item == '-':
                while isOper(s.peek()) == True:
                    posteq.append(s.pop())
                s.push(item)

            elif item == "*" or item == "/":
                while s.peek() == "*" or s.peek() == "/":
                    posteq.append(s.pop())
                s.push(item)

            elif isNum(item):
                posteq.append(item)

        while s.isEmpty() == False:
            posteq.append(s.pop())

        return posteq

    def calEq(self, eq):
        """
        :param eq: 후입처리된 연산
        :return: result(scalar)
        """
        s = Stack()
        for item in eq:
            if not isOper(item):
                s.push(item)
            else:
                num1 = float(s.pop())
                num2 = float(s.pop())
                print(num1, num2)
                if item == "+":
                    s.push(str(num2 + num1))
                elif item == "-":
                    s.push(str(num2 - num1))
                elif item == "*":
                    s.push(str(num2 * num1))
                elif item == "/":
                    s.push(str(num2 / num1))

        return s.pop()

a=Window()
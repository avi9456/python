class conversion:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        #this array is used a stack
        self.array=[]
        #precdence setting
        self.output=[]
        self.precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def isempty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isempty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def isoperand(self,ch):
        return ch.isalpha()
    def notgreater(self,i):
        try:
            a=self.precedence[i]
            b=self.precedence[self.peek()]
            return True if a<=b else False
        except keyerror:
            return False
    def infixtopostfix(self,exp):
        for i in exp:
            if self.isoperand(i):
                self.output.append(i)
            elif i== '(':
                self.push(i)
            elif i== ')':
                while ((not self.isempty()) and self.peek()!='('):
                    a=self.pop()
                    self.output.append(a)
                if (not self.isempty() and self.peek()!='('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isempty and self.notgreater(i)):
                    if i=='^' and self.array[-1]==i:
                        break
                    self.output.append(self.pop())
                self.push(i)
        while not self.isempty():
            self.output.append(self.pop())
        print("".join(self.output))
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = conversion(len(exp))
obj.infixtopostfix(exp)
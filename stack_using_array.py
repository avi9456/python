def createstack():
    stack=[]
    return stack
def isempty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def push(stack,data):
    stack.append(data)
    print(f"{data} pushed inside the stack")
def pop(stack):
    if isempty(stack):
        print("stack is empty")
    else:
        popped=stack.pop()
        print(f"{popped} is deleted")
def peek(stack):
    if isempty(stack):
        print("stack is empty")
    else:
        print(f"{stack[len(stack)-1]}")
stack1=createstack()
push(stack1,10)
push(stack1,20)
push(stack1,30)
peek(stack1)
pop(stack1)
peek(stack1)
pop(stack1)
peek(stack1)
pop(stack1)
peek(stack1)
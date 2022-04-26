print("enter list element")
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
while 1:
    print('''
    1 inster element
    2 delete element
    0 get final answer
    ''')
    op=int(input("select any one: "))
    if op==1:
        print('''
        1 insert at begening
        2 insert at end
        3 insert at specific location
        ''')
        op=int(input("select any one: "))
        if op==1:
            ele=int(input("enter element to insert: "))
            a.insert(0,ele)
        elif op==2:
            ele=int(input("enter element to insert: "))
            a.append(ele)
        elif op==3:
            ele=int(input("enter element to insert: "))
            pos=int(input("enter position: "))
            a.insert(pos,ele)
        else:
            continue
    elif op==2:
        print('''
        1 delete at begening
        2 delete at end
        3 delete at specific element
        ''')
        op=int(input("select any one: "))
        if op==1:
            a.pop(0)
        elif op==2:
            a.pop(len(a)-1)
        elif op==3:
            ele=int(input("enter element to delete: "))
            a.remove(ele)
        else:
            continue
    else:
        break
print(a)

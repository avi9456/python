a=int(input("enter first number: "))
b=int(input("enter second number: "))
if a>b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")
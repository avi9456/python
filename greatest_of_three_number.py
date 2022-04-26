a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a==b==c:
    print(f"{a}, {b}, and {c} are equal")
elif a==b:
    if a>c:
        print(f"{a} and {b} are equal and greater than {c}")
    else:
        print(f"{c} is greater than {a} and {b}, where {a} and {b} are equal")
elif a==c:
    if a>b:
        print(f"{a} and {c} are equal and greater than {b}")
    else:
        print(f"{b} is greater than {a} and {c}, where {a} and {c} are equal")
elif b==c:
    if a>b:
        print(f"{b} and {c} are equal and greater than {a}")
    else:
        print(f"{c} is greater than {b} and {c}, where {b} and {c} are equal")
else:
    if a>b and a>c:
        print(f"{a} is greater than {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is greater tahn {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
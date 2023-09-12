plus = []
minus = []
multiply = []
divide = []
str = " "
while True:
    a = int(input())
    b = int(input())
    c = input()
    if c=="+":
        str = f"{a}+{b}={a + b}"
        plus.append(str)
        print(str)
        print(f"+ {plus}\n- {minus}\n* {multiply}\n/ {divide}")
    elif c=="-":
        str = f"{a}-{b}={a - b}"
        minus.append(str)
        print(str)
        print(f"+ {plus}\n- {minus}\n* {multiply}\n/ {divide}")
    elif c=="*":
        str = f"{a}*{b}={a * b}"
        multiply.append(str)
        print(str)
        print(f"+ {plus}\n- {minus}\n* {multiply}\n/ {divide}")
    else:
        str = f"{a}/{b}={a // b}"
        divide.append(str)
        print(str)
        print(f"+ {plus}\n- {minus}\n* {multiply}\n/ {divide}")

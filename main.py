m1 = []
m2 = []
m3 = []
m4 = []
str = " "
while True:
    a = int(input())
    b = int(input())
    c = input()
    if c=="+":
        str = f"{a}+{b}={a + b}"
        m1.append(str)
        print(str)
        print(f"+ {m1}\n- {m2}\n* {m3}\n/ {m4}")
    elif c=="-":
        str = f"{a}-{b}={a - b}"
        m2.append(str)
        print(str)
        print(f"+ {m1}\n- {m2}\n* {m3}\n/ {m4}")
    elif c=="*":
        str = f"{a}*{b}={a * b}"
        m3.append(str)
        print(str)
        print(f"+ {m1}\n- {m2}\n* {m3}\n/ {m4}")
    else:
        str = f"{a}/{b}={a // b}"
        m4.append(str)
        print(str)
        print(f"+ {m1}\n- {m2}\n* {m3}\n/ {m4}")
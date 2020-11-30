crt = False
while crt == False:
    try:
        a = int(input("Enter a integer : "))
        b = int(input("Enter an another integer : "))
        crt = True
        op = input("Enter a operation : +, -, *, / ? ")
        if op == '+':
            print(f"{a} + {b} = {a+b}")
        elif op == '-':
            print(f"{a} - {b} = {a-b}")
        elif op == '*':
            print(f"{a} * {b} = {a*b}")
        elif op == '/':
            if(b == 0):
                raise ZeroDivisionError("Enter non zero value for b")
            print(f"{a} / {b} = {a/b}")
            print("Enter the correct value for b")
    except ValueError:
        print("Enter correct integer values")
